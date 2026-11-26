#!/usr/bin/env python3
"""Validate, rank and render the Conjectura research catalogue.

``research/catalogue.json`` is the single authoritative machine-readable record
of every problem the project has considered. This script

* validates it (schema, cross-field status rules, dossiers, directories),
* computes the heuristic ranking defined in ``research/priorities.json``,
* renders the generated view ``research/INDEX.md``.

Usage::

    python scripts/catalogue.py validate
    python scripts/catalogue.py rank
    python scripts/catalogue.py render [--check]
    python scripts/catalogue.py show CJ-0001

Exit status is non-zero whenever a check fails.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "research" / "catalogue.json"
PRIORITIES = ROOT / "research" / "priorities.json"
SCHEMA = ROOT / "research" / "schema" / "catalogue.schema.json"
INDEX = ROOT / "research" / "INDEX.md"

# Every dossier must contain these second-level headings with non-empty bodies.
DOSSIER_HEADINGS = [
    "Definitions and hypotheses",
    "Known partial results",
    "Relevant literature",
    "Open-status evidence",
    "Novelty search coverage and limitations",
    "Computational approaches",
    "Mathematical approaches",
    "Formalization feasibility",
    "Prerequisites",
]

# Mathematical statuses that require a working directory under research/active/.
ACTIVE_STATUSES = {
    "active-investigation",
    "partial-result",
    "candidate-proof",
    "candidate-counterexample",
}
# Statuses that assert the problem is settled by this project.
SETTLED_STATUSES = {"proved", "disproved"}
ACTIVE_FILES = ["STATE.md", "journal.md"]


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def work_dir_name(problem: dict) -> str:
    return f"{problem['id']}-{problem['slug']}"


def _is_date(text: str) -> bool:
    try:
        dt.date.fromisoformat(text)
    except (TypeError, ValueError):
        return False
    return True


def dossier_sections(text: str) -> dict[str, str]:
    """Map each ``## Heading`` of a Markdown document to its body text."""
    sections: dict[str, str] = {}
    current: str | None = None
    for line in text.splitlines():
        match = re.match(r"^##\s+(.*?)\s*$", line)
        if match:
            current = match.group(1)
            sections[current] = ""
        elif current is not None:
            sections[current] += line + "\n"
    return sections


def validate(catalogue: dict, model: dict, root: Path = ROOT) -> list[str]:
    """Return a list of human-readable errors; an empty list means valid."""
    errors: list[str] = []

    schema = load_json(SCHEMA)
    validator = jsonschema.Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(catalogue), key=lambda e: list(e.absolute_path)):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"schema: {location}: {error.message}")
    if errors:
        return errors  # later checks assume the schema holds

    if not _is_date(catalogue["updated"]):
        errors.append("updated: not an ISO date")

    criteria = [criterion["key"] for criterion in model["criteria"]]
    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()

    for problem in catalogue["problems"]:
        pid = problem["id"]
        if pid in seen_ids:
            errors.append(f"{pid}: duplicate id")
        seen_ids.add(pid)
        if problem["slug"] in seen_slugs:
            errors.append(f"{pid}: duplicate slug {problem['slug']!r}")
        seen_slugs.add(problem["slug"])

        for label, value in (
            ("source.accessed", problem["source"]["accessed"]),
            ("open_status.as_of", problem["open_status"]["as_of"]),
            ("novelty_search.as_of", problem["novelty_search"]["as_of"]),
        ):
            if not _is_date(value):
                errors.append(f"{pid}: {label} is not an ISO date")

        # Scores: exactly the criteria of the model.
        missing = [key for key in criteria if key not in problem["scores"]]
        extra = [key for key in problem["scores"] if key not in criteria]
        if missing:
            errors.append(f"{pid}: missing scores {missing}")
        if extra:
            errors.append(f"{pid}: unknown score criteria {extra}")

        # Dossier.
        dossier = root / problem["dossier"]
        if not dossier.is_file():
            errors.append(f"{pid}: dossier {problem['dossier']} does not exist")
        else:
            sections = dossier_sections(dossier.read_text(encoding="utf-8"))
            for heading in DOSSIER_HEADINGS:
                if heading not in sections:
                    errors.append(f"{pid}: dossier lacks section '## {heading}'")
                elif not sections[heading].strip():
                    errors.append(f"{pid}: dossier section '## {heading}' is empty")

        status = problem["status"]
        mathematical = status["mathematical"]

        # A statement not compared with any source cannot be worked on.
        if mathematical != "candidate" and problem["source"]["statement_checked_against"] == "not-checked":
            errors.append(f"{pid}: status {mathematical!r} requires a statement checked against a source")

        if mathematical in ACTIVE_STATUSES:
            work_dir = root / "research" / "active" / work_dir_name(problem)
            for name in ACTIVE_FILES:
                if not (work_dir / name).is_file():
                    errors.append(f"{pid}: status {mathematical!r} requires research/active/{work_dir_name(problem)}/{name}")

        if mathematical in SETTLED_STATUSES:
            if "result" not in problem:
                errors.append(f"{pid}: status {mathematical!r} requires a 'result' package path")
            elif not (root / problem["result"]).is_file():
                errors.append(f"{pid}: result package {problem['result']} does not exist")
            if status["external_review"] == "not-reviewed":
                errors.append(f"{pid}: status {mathematical!r} is not allowed while external_review is 'not-reviewed'")
            if status["novelty"] == "unknown":
                errors.append(f"{pid}: status {mathematical!r} requires a documented novelty search")

        if mathematical == "previously-resolved":
            if status["novelty"] != "prior-resolution-identified":
                errors.append(f"{pid}: 'previously-resolved' requires novelty 'prior-resolution-identified'")
        if status["novelty"] == "prior-resolution-identified" and "resolution_source" not in problem:
            errors.append(f"{pid}: novelty 'prior-resolution-identified' requires 'resolution_source'")

        if status["formal"] == "complete":
            if "formal_receipt" not in problem:
                errors.append(f"{pid}: formal status 'complete' requires 'formal_receipt'")
            else:
                receipt_path = root / problem["formal_receipt"]
                if not receipt_path.is_file():
                    errors.append(f"{pid}: receipt {problem['formal_receipt']} does not exist")
                else:
                    receipt = load_json(receipt_path)
                    if receipt.get("verdict") != "passed":
                        errors.append(f"{pid}: receipt verdict is {receipt.get('verdict')!r}, not 'passed'")
                    registered = {entry.get("catalogue_id") for entry in receipt.get("registry", [])}
                    if pid not in registered:
                        errors.append(f"{pid}: receipt does not cover a theorem registered for this problem")

    # Working directories must correspond to catalogue entries in an active status.
    active_root = root / "research" / "active"
    if active_root.is_dir():
        expected = {
            work_dir_name(problem)
            for problem in catalogue["problems"]
            if problem["status"]["mathematical"] in ACTIVE_STATUSES
        }
        for child in sorted(active_root.iterdir()):
            if child.is_dir() and child.name not in expected:
                errors.append(f"research/active/{child.name}: no catalogue entry in an active status")

    # Shortlist refers to existing, eligible problems.
    shortlist = model.get("shortlist", {})
    for pid in shortlist.get("problems", []):
        if pid not in seen_ids:
            errors.append(f"priorities.json: shortlisted id {pid} is not in the catalogue")
    if shortlist.get("problems") and not _is_date(shortlist.get("decided") or ""):
        errors.append("priorities.json: shortlist.decided must be an ISO date when a shortlist is recorded")
    eligible = {entry["id"] for entry in rank(catalogue, model) if entry["eligible"]}
    for pid in shortlist.get("problems", []):
        if pid in seen_ids and pid not in eligible:
            errors.append(f"priorities.json: shortlisted id {pid} fails an eligibility gate")

    return errors


def rank(catalogue: dict, model: dict) -> list[dict]:
    """Return problems ordered by the weighted-sum heuristic (highest first)."""
    criteria = model["criteria"]
    top = model["scale"]["max"]
    total_weight = sum(criterion["weight"] for criterion in criteria)
    ranked = []
    for problem in catalogue["problems"]:
        scores = problem["scores"]
        weighted = sum(criterion["weight"] * scores[criterion["key"]]["score"] for criterion in criteria if criterion["key"] in scores)
        failed_gates = [
            gate["criterion"]
            for gate in model.get("gates", [])
            if scores.get(gate["criterion"], {}).get("score", 0) < gate["minimum"]
        ]
        override = problem.get("priority_override", {}).get("decision")
        closed = problem["status"]["mathematical"] in {"previously-resolved", "rejected", "superseded", "proved", "disproved"}
        ranked.append(
            {
                "id": problem["id"],
                "name": problem["name"],
                "score": round(100 * weighted / (top * total_weight), 1),
                "failed_gates": failed_gates,
                "eligible": not failed_gates and not closed and override != "exclude",
                "override": override,
            }
        )
    ranked.sort(key=lambda entry: (not entry["eligible"], -entry["score"], entry["id"]))
    return ranked


def render(catalogue: dict, model: dict) -> str:
    by_id = {problem["id"]: problem for problem in catalogue["problems"]}
    lines = [
        "<!-- GENERATED by `python scripts/catalogue.py render` from research/catalogue.json. Do not edit by hand. -->",
        "",
        "# Research index",
        "",
        f"Catalogue last updated: {catalogue['updated']}. Scoring model version: {model['model_version']}.",
        "",
        "The score is a weighted-sum heuristic used to order the queue of candidate problems.",
        "It is **not** a probability of success. Read each score together with its written",
        "justification in `research/catalogue.json` and the linked dossier.",
        "",
    ]
    if not catalogue["problems"]:
        lines += ["The catalogue is empty.", ""]
        return "\n".join(lines)

    lines += [
        "| Rank | ID | Problem | Fields | Score | Mathematical | Formal | Novelty | External review |",
        "| ---: | --- | --- | --- | ---: | --- | --- | --- | --- |",
    ]
    position = 0
    for entry in rank(catalogue, model):
        problem = by_id[entry["id"]]
        status = problem["status"]
        if entry["eligible"]:
            position += 1
            rank_cell = str(position)
        else:
            rank_cell = "–"
        dossier = problem["dossier"].removeprefix("research/")
        name = problem["name"].replace("|", "\\|")
        lines.append(
            f"| {rank_cell} | {problem['id']} | [{name}]({dossier}) | {', '.join(problem['fields'])} | "
            f"{entry['score']:.1f} | {status['mathematical']} | {status['formal']} | {status['novelty']} | "
            f"{status['external_review']} |"
        )
    lines.append("")

    notes = []
    for entry in rank(catalogue, model):
        if entry["failed_gates"]:
            notes.append(f"- {entry['id']} is unranked: it fails the gate(s) {', '.join(entry['failed_gates'])}.")
        elif not entry["eligible"]:
            notes.append(f"- {entry['id']} is unranked: its status or a director override removes it from the queue.")
    if notes:
        lines += ["Unranked entries:", ""] + notes + [""]

    shortlist = model.get("shortlist", {})
    if shortlist.get("problems"):
        lines += [
            f"## Shortlist (decided {shortlist['decided']})",
            "",
            ", ".join(shortlist["problems"]) + ".",
            "",
            shortlist.get("rationale", ""),
            "",
        ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate", help="check the catalogue; exit 1 on any error")
    commands.add_parser("rank", help="print the heuristic ranking")
    render_parser = commands.add_parser("render", help="write research/INDEX.md")
    render_parser.add_argument("--check", action="store_true", help="fail if INDEX.md is out of date instead of writing it")
    show_parser = commands.add_parser("show", help="print one catalogue record")
    show_parser.add_argument("id")
    args = parser.parse_args(argv)

    catalogue = load_json(CATALOGUE)
    model = load_json(PRIORITIES)

    if args.command == "validate":
        errors = validate(catalogue, model)
        for error in errors:
            print(f"ERROR {error}")
        print(f"{len(catalogue.get('problems', []))} problem(s), {len(errors)} error(s)")
        return 1 if errors else 0

    if args.command == "rank":
        for position, entry in enumerate(rank(catalogue, model), start=1):
            flag = "" if entry["eligible"] else "  [unranked]"
            print(f"{position:>2}  {entry['id']}  {entry['score']:5.1f}  {entry['name']}{flag}")
        return 0

    if args.command == "render":
        text = render(catalogue, model)
        if args.check:
            current = INDEX.read_text(encoding="utf-8") if INDEX.is_file() else ""
            if current != text:
                print("ERROR research/INDEX.md is out of date; run `python scripts/catalogue.py render`")
                return 1
            print("research/INDEX.md is up to date")
            return 0
        INDEX.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {INDEX.relative_to(ROOT).as_posix()}")
        return 0

    if args.command == "show":
        for problem in catalogue["problems"]:
            if problem["id"] == args.id:
                print(json.dumps(problem, indent=2, ensure_ascii=False))
                return 0
        print(f"ERROR no problem with id {args.id}")
        return 1

    return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
