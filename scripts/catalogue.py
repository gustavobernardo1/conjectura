#!/usr/bin/env python3
"""Validate, rank and render the Conjectura research records.

``research/catalogue.json`` is the single authoritative machine-readable record
of every problem the project has considered. ``research/discoveries.json`` is
the single authoritative record of every registered mathematical contribution.
This script

* validates both (schemas, cross-field status rules, references, evidence),
* computes the heuristic ranking defined in ``research/priorities.json``,
* renders the generated views ``research/INDEX.md`` and ``research/summary.json``.

Usage::

    python scripts/catalogue.py validate
    python scripts/catalogue.py rank
    python scripts/catalogue.py render [--check]
    python scripts/catalogue.py show CJ-0001          (or MD-0001)
    python scripts/catalogue.py fingerprint MD-0001

Exit status is non-zero whenever a check fails.
"""

from __future__ import annotations

import argparse
import collections
import copy
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import jsonschema
import referencing

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "research" / "catalogue.json"
PRIORITIES = ROOT / "research" / "priorities.json"
SCHEMA = ROOT / "research" / "schema" / "catalogue.schema.json"
INDEX = ROOT / "research" / "INDEX.md"
REGISTRY = ROOT / "research" / "discoveries.json"
REGISTRY_SCHEMA = ROOT / "research" / "schema" / "discoveries.schema.json"
SUMMARY = ROOT / "research" / "summary.json"
LEAN_REGISTRY = ROOT / "formalization" / "registry.json"

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
# Statuses that assert the statement is settled by this project.
SETTLED_STATUSES = {"proved", "disproved"}
ACTIVE_FILES = ["STATE.md", "journal.md"]
# Statuses of a contribution that assert a complete argument for its statement.
COMPLETE_ARGUMENT_STATUSES = {"candidate-proof", "candidate-counterexample"} | SETTLED_STATUSES
# Novelty values that assert a search was made and found nothing.
SEARCHED_NOVELTY = {"preliminary-search-completed", "no-prior-resolution-found"}
# The authoritative records from which research/summary.json is generated.
SUMMARY_SOURCES = [CATALOGUE, REGISTRY, PRIORITIES, LEAN_REGISTRY]
STATUS_DIMENSIONS = ["mathematical", "formal", "novelty", "external_review"]
# The ``public`` block of the summary (docs/public-summary.md). Its links resolve on
# the branch the summary is served from: ``research`` holds the investigations and
# everything that is on ``main``.
PUBLIC_SCHEMA = ROOT / "research" / "schema" / "public-summary.schema.json"
PUBLIC_BRANCH = "research"
# Contribution types counted under a heading of their own; every other type is "other".
PUBLIC_CATEGORIES = {"lemma": "lemmas", "theorem": "theorems", "counterexample": "counterexamples"}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_registry() -> dict:
    return load_json(REGISTRY)


def schema_errors(schema_path: Path, document: dict, label: str) -> list[str]:
    """Validate against one of the two schemas; the registry schema refers to the catalogue's."""
    schemas = [load_json(SCHEMA), load_json(REGISTRY_SCHEMA)]
    resources = referencing.Registry().with_resources(
        [(schema["$id"], referencing.Resource.from_contents(schema)) for schema in schemas]
    )
    validator = jsonschema.Draft202012Validator(load_json(schema_path), registry=resources)
    errors = []
    for error in sorted(validator.iter_errors(document), key=lambda e: [str(part) for part in e.absolute_path]):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"{label}: {location}: {error.message}")
    return errors


def fingerprint(statement: str) -> str:
    """Identity of a statement: SHA-256 of its text, whitespace and Unicode form normalised."""
    text = " ".join(unicodedata.normalize("NFC", statement).split())
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_lf(path: Path) -> str:
    """SHA-256 with line endings normalised to LF, as in the verification receipts."""
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def standing(record: dict) -> str:
    """Where a contribution stands, derived from its status. Never stored."""
    status = record["status"]
    if status["mathematical"] in {"rejected", "superseded"}:
        return "withdrawn"
    if status["novelty"] == "prior-resolution-identified":
        return "rediscovered"
    if status["mathematical"] in SETTLED_STATUSES:
        return "established"
    return "candidate"


def publicly_established(record: dict) -> bool:
    """What the public summary counts: promoted, and original within a thorough documented search.

    Promotion (``proved``/``disproved``) already requires a review, a recorded
    novelty search and a result package; a search that is only preliminary is
    not enough here.
    """
    return standing(record) == "established" and record["status"]["novelty"] == "no-prior-resolution-found"


def current_reviews(record: dict) -> list[dict]:
    """Review evidence bound to the statement as it reads now."""
    current = fingerprint(record["statement"])
    return [
        item
        for item in record["evidence"]
        if item["kind"] == "review" and item.get("statement_fingerprint") == current
    ]


def work_dir_name(problem: dict) -> str:
    return f"{problem['id']}-{problem['slug']}"


def _is_date(text: str | None) -> bool:
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


# ------------------------------------------------------------------ validation --


def status_rule_errors(pid: str, record: dict, root: Path) -> list[str]:
    """Status rules shared by problems and contributions (AGENTS.md section 4)."""
    errors: list[str] = []
    status = record["status"]
    mathematical = status["mathematical"]

    if mathematical in SETTLED_STATUSES:
        if "result" not in record:
            errors.append(f"{pid}: status {mathematical!r} requires a 'result' package path")
        elif not (root / record["result"]).is_file():
            errors.append(f"{pid}: result package {record['result']} does not exist")
        if status["external_review"] == "not-reviewed":
            errors.append(f"{pid}: status {mathematical!r} is not allowed while external_review is 'not-reviewed'")
        if status["novelty"] == "unknown":
            errors.append(f"{pid}: status {mathematical!r} requires a documented novelty search")
        if not _is_date(record.get("resolved_on")):
            errors.append(f"{pid}: status {mathematical!r} requires the date 'resolved_on'")

    if mathematical == "previously-resolved":
        if status["novelty"] != "prior-resolution-identified":
            errors.append(f"{pid}: 'previously-resolved' requires novelty 'prior-resolution-identified'")
    if status["novelty"] == "prior-resolution-identified" and "resolution_source" not in record:
        errors.append(f"{pid}: novelty 'prior-resolution-identified' requires 'resolution_source'")

    if status["formal"] == "complete":
        if "formal_receipt" not in record:
            errors.append(f"{pid}: formal status 'complete' requires 'formal_receipt'")
        else:
            receipt_path = root / record["formal_receipt"]
            if not receipt_path.is_file():
                errors.append(f"{pid}: receipt {record['formal_receipt']} does not exist")
            else:
                receipt = load_json(receipt_path)
                if receipt.get("verdict") != "passed":
                    errors.append(f"{pid}: receipt verdict is {receipt.get('verdict')!r}, not 'passed'")
                registered = {entry.get("catalogue_id") for entry in receipt.get("registry", [])}
                if pid not in registered:
                    errors.append(f"{pid}: receipt does not cover a theorem registered for this record")
    return errors


def validate_discoveries(registry: dict, catalogue: dict, root: Path = ROOT) -> list[str]:
    """Errors in the registry of contributions; an empty list means valid."""
    errors = schema_errors(REGISTRY_SCHEMA, registry, "discoveries schema")
    if errors:
        return errors  # later checks assume the schema holds
    if not _is_date(registry["updated"]):
        errors.append("discoveries: updated is not an ISO date")

    problem_ids = {problem["id"] for problem in catalogue.get("problems", [])}
    records: dict[str, dict] = {}
    for record in registry["discoveries"]:
        if record["id"] in records:
            errors.append(f"{record['id']}: duplicate id")
        records[record["id"]] = record
    prints = {did: fingerprint(record["statement"]) for did, record in records.items()}
    superseded = {
        relation["target"]
        for record in records.values()
        for relation in record.get("relations", [])
        if relation["type"] == "supersedes"
    }

    for did, record in records.items():
        status = record["status"]
        mathematical = status["mathematical"]
        if not _is_date(record["registered"]):
            errors.append(f"{did}: registered is not an ISO date")
        if mathematical == "active-investigation":
            errors.append(f"{did}: 'active-investigation' describes a catalogued problem, not a contribution")
        if mathematical == "superseded" and did not in superseded:
            errors.append(f"{did}: 'superseded' requires another contribution with a 'supersedes' relation to it")

        origin = record["provenance"]["record"]
        if not (root / origin.split("#")[0]).exists():
            errors.append(f"{did}: provenance record {origin} does not exist")

        for item in record["evidence"]:
            path = root / item["path"].split("#")[0]
            if not path.exists():
                errors.append(f"{did}: evidence {item['path']} does not exist")
            elif "sha256" in item and path.is_file() and sha256_lf(path) != item["sha256"]:
                errors.append(f"{did}: evidence {item['path']} changed since it was recorded; reassess, then update its sha256")
            if "date" in item and not _is_date(item["date"]):
                errors.append(f"{did}: evidence {item['path']}: date is not an ISO date")
            if item["kind"] == "review":
                missing = [key for key in ("by", "date", "revision", "statement_fingerprint") if key not in item]
                if missing:
                    errors.append(f"{did}: review evidence {item['path']} lacks {missing}")

        if status["external_review"] != "not-reviewed" and not current_reviews(record):
            errors.append(
                f"{did}: external_review {status['external_review']!r} requires review evidence bound to the "
                f"statement as it reads now (fingerprint {prints[did]})"
            )
        if status["novelty"] in SEARCHED_NOVELTY:
            if "novelty_search" not in record:
                errors.append(f"{did}: novelty {status['novelty']!r} requires a documented 'novelty_search'")
            elif not _is_date(record["novelty_search"]["as_of"]):
                errors.append(f"{did}: novelty_search.as_of is not an ISO date")
        errors += status_rule_errors(did, record, root)

        for dependency in record.get("depends_on", []):
            ref = dependency.get("ref")
            if ref is None:
                continue  # an external result, cited
            if ref == did or ref not in records:
                errors.append(f"{did}: depends on {'itself' if ref == did else 'unknown contribution ' + ref}")
                continue
            pin = dependency.get("statement_fingerprint")
            if pin is None and mathematical in COMPLETE_ARGUMENT_STATUSES:
                errors.append(f"{did}: status {mathematical!r} requires the dependency on {ref} to be pinned to a statement fingerprint")
            if pin is not None and pin != prints[ref]:
                errors.append(f"{did}: depends on {ref} at a statement that has since changed; reassess {did}, then update the pin")
            needed = records[ref]["status"]["mathematical"]
            if mathematical in SETTLED_STATUSES and needed not in {"proved", "previously-resolved"}:
                errors.append(f"{did}: status {mathematical!r} is not allowed while its dependency {ref} is {needed!r}")

        for relation in record.get("relations", []):
            target = relation["target"]
            if target == did or (target not in problem_ids and target not in records):
                errors.append(f"{did}: relation {relation['type']!r} points to {'itself' if target == did else 'unknown ' + target}")
            if "local_id" in relation and target not in problem_ids:
                errors.append(f"{did}: a local_id is only meaningful for a relation to a catalogued problem")

    # A proof cannot depend on itself through other contributions.
    def reaches(start: str, goal: str, seen: set[str]) -> bool:
        for dependency in records.get(start, {}).get("depends_on", []):
            ref = dependency.get("ref")
            if ref == goal or (ref in records and ref not in seen and reaches(ref, goal, seen | {ref})):
                return True
        return False

    errors += [f"{did}: circular proof dependency" for did in records if reaches(did, did, {did})]
    return errors


def stale_evidence(registry: dict) -> list[str]:
    """Evidence bound to an earlier wording of a statement. Kept as history; it supports nothing."""
    notes = []
    for record in registry.get("discoveries", []):
        current = fingerprint(record["statement"])
        for item in record["evidence"]:
            if item.get("statement_fingerprint", current) != current:
                notes.append(f"{record['id']}: {item['kind']} {item['path']} covers an earlier statement of this record")
    return notes


def validate(catalogue: dict, model: dict, root: Path = ROOT, registry: dict | None = None) -> list[str]:
    """Return a list of human-readable errors; an empty list means valid."""
    errors = schema_errors(SCHEMA, catalogue, "schema")
    if errors:
        return errors  # later checks assume the schema holds
    if registry is None:
        registry = load_registry()
    errors += validate_discoveries(registry, catalogue, root)
    conjectures = {
        record.get("id")
        for record in registry.get("discoveries", [])
        if isinstance(record, dict) and record.get("type") == "conjecture"
    }

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

        errors += status_rule_errors(pid, problem, root)

        # A problem formulated by the project points to its registered conjecture.
        if "discovery" in problem and problem["discovery"] not in conjectures:
            errors.append(f"{pid}: 'discovery' {problem['discovery']} is not a registered contribution of type 'conjecture'")

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


# --------------------------------------------------------------------- ranking --


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


# ------------------------------------------------------------- generated index --


def render_contributions(catalogue: dict, registry: dict) -> list[str]:
    """The section of INDEX.md that lists the registered contributions."""
    lines = [
        "## Mathematical contributions",
        "",
        "Generated from `research/discoveries.json`. An identifier establishes identity, not",
        "correctness or novelty: read each row through its four status columns. *Standing* is",
        "derived from them: `candidate` (not promoted), `established` (reviewed and packaged under",
        "`results/`), `rediscovered` (found in the literature after it was derived here) or",
        "`withdrawn`.",
        "",
    ]
    records = registry.get("discoveries", [])
    if not records:
        return lines + ["No contribution is registered.", ""]

    problems = collections.defaultdict(list)
    for problem in catalogue["problems"]:
        if "discovery" in problem:
            problems[problem["discovery"]].append(problem["id"])
    lines += [
        "| ID | Type | Contribution | Origin | Mathematical | Formal | Novelty | External review | Standing |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in sorted(records, key=lambda record: record["id"]):
        status = record["status"]
        origins = [
            relation["target"] + (f" ({relation['local_id']})" if "local_id" in relation else "")
            for relation in record.get("relations", [])
            if relation["type"] == "originated_from"
        ]
        title = record["title"].replace("|", "\\|")
        if problems[record["id"]]:
            title += f" (investigated as {', '.join(problems[record['id']])})"
        lines.append(
            f"| {record['id']} | {record['type']} | {title} | {', '.join(origins) or '–'} | "
            f"{status['mathematical']} | {status['formal']} | {status['novelty']} | "
            f"{status['external_review']} | {standing(record)} |"
        )
    lines.append("")
    return lines


def render(catalogue: dict, model: dict, registry: dict | None = None) -> str:
    if registry is None:
        registry = load_registry()
    by_id = {problem["id"]: problem for problem in catalogue["problems"]}
    lines = [
        "<!-- GENERATED by `python scripts/catalogue.py render` from research/catalogue.json and research/discoveries.json. Do not edit by hand. -->",
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
        return "\n".join(lines + render_contributions(catalogue, registry))

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
    return "\n".join(lines + render_contributions(catalogue, registry))


# ----------------------------------------------------------- generated summary --


def _latest(entries: list[tuple[str, dict]]) -> dict | None:
    """The entry with the latest date; ties go to the highest identifier. None when empty."""
    return max(entries, key=lambda pair: (pair[0], pair[1]["id"]))[1] if entries else None


def _counts(values) -> dict[str, int]:
    return dict(sorted(collections.Counter(values).items()))


def public_summary(active: list[dict], problems: list[dict], records: list[dict], repository: str | None, root: Path = ROOT) -> dict:
    """The block of the summary meant for presentation outside the repository.

    Field definitions and counting rules: docs/public-summary.md. Every record is
    counted at most once, under its ``type``; resolved conjectures are problems
    of the catalogue and are counted apart from the contributions.
    """

    def url(path: str, view: str = "blob") -> str | None:
        return f"{repository}/{view}/{PUBLIC_BRANCH}/{path}" if repository else None

    def entry(record: dict, title: str, path: str, **extra) -> dict:
        return {"id": record["id"], "title": title} | extra | {"url": url(path), "status": dict(record["status"])}

    def discovery(record: dict, **extra) -> dict:
        return entry(record, record["title"], record["result"], type=record["type"], **extra)

    investigations = [entry(problem, problem["name"], problem["dossier"]) for problem in active]
    established = [record for record in records if publicly_established(record)]
    by_category = {name: 0 for name in [*PUBLIC_CATEGORIES.values(), "other"]}
    for record in established:
        by_category[PUBLIC_CATEGORIES.get(record["type"], "other")] += 1
    # A problem the project formulated itself ('discovery') is a contribution, not a resolved conjecture.
    resolved = [problem for problem in problems if publicly_established(problem) and "discovery" not in problem]
    by_outcome = {value: sum(1 for problem in resolved if problem["status"]["mathematical"] == value) for value in ("proved", "disproved")}
    verified = [
        (stamp, discovery(record, verified_utc=stamp))
        for record in established
        if record["status"]["formal"] == "complete"
        for stamp in [load_json(root / record["formal_receipt"])["created_utc"]]
    ]
    return {
        "schema_version": 1,
        "active_investigations": investigations,
        "primary_investigation": investigations[0] if investigations else None,
        "established_original_discoveries": by_category | {"total": len(established)},
        "resolved_conjectures": by_outcome | {"total": len(resolved)},
        "latest_established_original_discovery": _latest(
            [(record["resolved_on"], discovery(record, established_on=record["resolved_on"])) for record in established]
        ),
        "latest_formally_verified_original_contribution": _latest(verified),
        "research_catalogue_url": url(INDEX.relative_to(ROOT).as_posix()),
        "reviewed_results_url": url("results", "tree"),
    }


def summarize(catalogue: dict, model: dict, registry: dict, root: Path = ROOT) -> dict:
    """The project summary without its ``generated`` block. Absent items are explicit nulls."""
    problems = {problem["id"]: problem for problem in catalogue["problems"]}
    records = registry.get("discoveries", [])
    # Rediscovered and withdrawn records are kept in the registry and left out of every metric.
    original = [record for record in records if standing(record) in {"candidate", "established"}]

    def problem_entry(problem: dict, **extra) -> dict:
        return {
            "id": problem["id"],
            "name": problem["name"],
            "status": dict(problem["status"]),
            "record": CATALOGUE.relative_to(ROOT).as_posix(),
            "dossier": problem["dossier"],
        } | extra

    def contribution_entry(record: dict, **extra) -> dict:
        return {
            "id": record["id"],
            "type": record["type"],
            "title": record["title"],
            "registered": record["registered"],
            "standing": standing(record),
            "status": dict(record["status"]),
            "record": REGISTRY.relative_to(ROOT).as_posix(),
            "evidence": sorted({item["path"] for item in record["evidence"]}),
        } | extra

    active = [
        problem_entry(
            problems[entry["id"]],
            priority_score=entry["score"],
            state=f"research/active/{work_dir_name(problems[entry['id']])}/STATE.md",
        )
        for entry in rank(catalogue, model)
        if problems[entry["id"]]["status"]["mathematical"] in ACTIVE_STATUSES
    ]

    def settled(value: str) -> dict | None:
        return _latest(
            [
                (problem["resolved_on"], problem_entry(problem, resolved_on=problem["resolved_on"], result=problem["result"]))
                for problem in problems.values()
                if problem["status"]["mathematical"] == value
            ]
        )

    reviewed = []
    for record in original:
        reviews = current_reviews(record)
        if record["status"]["external_review"] != "not-reviewed" and reviews:
            last = max(reviews, key=lambda item: item["date"])
            review = {key: last[key] for key in ("by", "date", "revision", "path")}
            reviewed.append((last["date"], contribution_entry(record, review=review)))

    formal = []
    for kind, items, make in (("problem", problems.values(), problem_entry), ("contribution", original, contribution_entry)):
        for item in items:
            if item["status"]["formal"] == "complete":
                verified = load_json(root / item["formal_receipt"])["created_utc"]
                formal.append((verified, make(item, kind=kind, receipt=item["formal_receipt"], verified_utc=verified)))

    assessed = [
        (record["novelty_search"]["as_of"], contribution_entry(record, novelty_search=record["novelty_search"]))
        for record in original
        if record["status"]["novelty"] in SEARCHED_NOVELTY
    ]

    lean_registry = load_json(LEAN_REGISTRY) if LEAN_REGISTRY.is_file() else {"theorems": []}
    repository = None
    citation = root / "CITATION.cff"
    if citation.is_file():
        match = re.search(r'^repository-code:\s*"?([^"\s]+)"?\s*$', citation.read_text(encoding="utf-8"), flags=re.M)
        repository = match.group(1) if match else None

    by_standing = {key: 0 for key in ("candidate", "established", "rediscovered", "withdrawn")}
    by_standing |= _counts(standing(record) for record in records)
    return {
        "schema_version": 1,
        "project": "Conjectura",
        "repository": repository,
        "active_investigations": active,
        "highest_priority_investigation": active[0] if active else None,
        "latest_proved_conjecture": settled("proved"),
        "latest_disproved_conjecture": settled("disproved"),
        "latest_registered_contribution": _latest([(record["registered"], contribution_entry(record)) for record in original]),
        "latest_reviewed_contribution": _latest(reviewed),
        "latest_formally_verified_contribution": _latest(formal),
        "latest_contribution_with_originality_assessment": _latest(assessed),
        "public": public_summary(
            [problems[entry["id"]] for entry in active], list(problems.values()), records, repository, root
        ),
        "counts": {
            "problems": {
                "catalogued": len(problems),
                "by_mathematical_status": _counts(problem["status"]["mathematical"] for problem in problems.values()),
            },
            "contributions": {
                "registered": len(records),
                "by_standing": by_standing,
                "counted": len(original),
                "by_type": _counts(record["type"] for record in original),
                "by_status": {
                    dimension: _counts(record["status"][dimension] for record in original) for dimension in STATUS_DIMENSIONS
                },
            },
            "excluded_from_contribution_counts": {
                "rediscovered": by_standing["rediscovered"],
                "withdrawn": by_standing["withdrawn"],
                "calibration_theorems": sum(1 for theorem in lean_registry["theorems"] if theorem.get("kind") == "calibration"),
            },
        },
        "reading_notes": [
            "An identifier (CJ-XXXX, MD-XXXX) establishes identity, not correctness or novelty.",
            "The four status dimensions are independent; 'ai-reviewed' is not human or peer review.",
            "Novelty values other than 'prior-resolution-identified' hold only within the documented search coverage.",
            "A null value means that no record qualifies.",
            "Counts and 'latest' entries cover contributions of standing 'candidate' or 'established' only.",
            "The block 'public' is stricter: beyond its investigations it covers only promoted records with novelty 'no-prior-resolution-found' (docs/public-summary.md).",
        ],
    }


def _git(*arguments: str) -> str | None:
    try:
        done = subprocess.run(["git", *arguments], cwd=ROOT, capture_output=True, text=True, check=False)
    except OSError:
        return None
    return done.stdout.strip() if done.returncode == 0 else None


def git_blob_id(path: Path) -> str:
    """The Git blob identifier of a text file as committed (line endings normalised to LF)."""
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()


# Fields of the ``generated`` block that do not depend on the content of the records.
VOLATILE = ("date", "branch", "revision", "sources_committed")


def generated_block() -> dict:
    """When and from what the summary was generated.

    ``sources`` gives the Git blob of each authoritative record and so identifies
    its exact content. ``revision`` is the commit that was checked out;
    ``sources_committed`` says whether that commit contains exactly these blobs.
    """
    sources = [path for path in SUMMARY_SOURCES if path.is_file()]
    relative = [path.relative_to(ROOT).as_posix() for path in sources]
    dirty = _git("status", "--porcelain", "--", *relative)
    return {
        "date": dt.datetime.now(dt.timezone.utc).date().isoformat(),
        "branch": _git("rev-parse", "--abbrev-ref", "HEAD"),
        "revision": _git("rev-parse", "HEAD"),
        "sources_committed": None if dirty is None else dirty == "",
        "sources": {name: git_blob_id(path) for name, path in zip(relative, sources)},
    }


def build_summary(catalogue: dict, model: dict, registry: dict, previous: dict | None = None, rebind: bool = True) -> dict:
    """The full summary. Volatile fields are kept from ``previous`` when nothing else changed.

    With ``rebind``, a summary generated before its sources were committed is
    regenerated once they are, so that ``revision`` names a commit containing them.
    """
    summary = summarize(catalogue, model, registry)
    summary["generated"] = generated_block()
    if previous is not None:
        kept = copy.deepcopy(summary)
        kept["generated"] |= {key: previous.get("generated", {}).get(key) for key in VOLATILE}
        newly_bound = rebind and summary["generated"]["sources_committed"] and not kept["generated"]["sources_committed"]
        if kept == previous and not newly_bound:
            return kept
    return summary


def summary_text(summary: dict) -> str:
    return json.dumps(summary, indent=2, ensure_ascii=False) + "\n"


# ------------------------------------------------------------------------- CLI --


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate", help="check the catalogue and the registry; exit 1 on any error")
    commands.add_parser("rank", help="print the heuristic ranking")
    render_parser = commands.add_parser("render", help="write research/INDEX.md and research/summary.json")
    render_parser.add_argument("--check", action="store_true", help="fail if a generated view is out of date instead of writing it")
    show_parser = commands.add_parser("show", help="print one problem or contribution record")
    show_parser.add_argument("id")
    print_parser = commands.add_parser("fingerprint", help="print the statement fingerprint of a contribution")
    print_parser.add_argument("id")
    args = parser.parse_args(argv)

    catalogue = load_json(CATALOGUE)
    model = load_json(PRIORITIES)
    registry = load_registry()

    if args.command == "validate":
        errors = validate(catalogue, model, registry=registry)
        for error in errors:
            print(f"ERROR {error}")
        for note in stale_evidence(registry):
            print(f"NOTE  {note}")
        print(
            f"{len(catalogue.get('problems', []))} problem(s), "
            f"{len(registry.get('discoveries', []))} contribution(s), {len(errors)} error(s)"
        )
        return 1 if errors else 0

    if args.command == "rank":
        for position, entry in enumerate(rank(catalogue, model), start=1):
            flag = "" if entry["eligible"] else "  [unranked]"
            print(f"{position:>2}  {entry['id']}  {entry['score']:5.1f}  {entry['name']}{flag}")
        return 0

    if args.command == "render":
        previous = load_json(SUMMARY) if SUMMARY.is_file() else None
        views = {
            INDEX: render(catalogue, model, registry),
            SUMMARY: summary_text(build_summary(catalogue, model, registry, previous, rebind=not args.check)),
        }
        status = 0
        for path, text in views.items():
            name = path.relative_to(ROOT).as_posix()
            current = path.read_text(encoding="utf-8") if path.is_file() else ""
            if current == text:
                print(f"{name} is up to date")
            elif args.check:
                print(f"ERROR {name} is out of date; run `python scripts/catalogue.py render`")
                status = 1
            else:
                path.write_text(text, encoding="utf-8", newline="\n")
                print(f"wrote {name}")
        return status

    records = catalogue["problems"] + registry["discoveries"]
    record = next((record for record in records if record["id"] == args.id), None)
    if record is None:
        print(f"ERROR no record with id {args.id}")
        return 1
    if args.command == "show":
        print(json.dumps(record, indent=2, ensure_ascii=False))
        return 0
    if args.command == "fingerprint":
        if "type" not in record:
            print("ERROR statement fingerprints are defined for contributions (MD-XXXX)")
            return 1
        print(fingerprint(record["statement"]))
        return 0
    return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
