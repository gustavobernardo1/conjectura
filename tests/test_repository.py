"""Consistency of the repository: catalogue, generated views, instructions, links."""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import catalogue as cat  # noqa: E402


@pytest.fixture(scope="module")
def data():
    return cat.load_json(cat.CATALOGUE), cat.load_json(cat.PRIORITIES)


# ---------------------------------------------------------------- catalogue --


def test_catalogue_is_valid(data):
    assert cat.validate(*data) == []


def test_generated_index_is_current(data):
    assert cat.INDEX.read_text(encoding="utf-8") == cat.render(*data)


def test_ranking_is_a_weighted_sum_and_respects_gates(data):
    catalogue, model = data
    ranking = cat.rank(catalogue, model)
    eligible = [entry for entry in ranking if entry["eligible"]]
    assert [entry["score"] for entry in eligible] == sorted((entry["score"] for entry in eligible), reverse=True)
    assert all(0 <= entry["score"] <= 100 for entry in ranking)
    for entry in ranking:
        if entry["failed_gates"]:
            assert not entry["eligible"]


def mutated(data, mutate):
    catalogue, model = copy.deepcopy(data[0]), copy.deepcopy(data[1])
    mutate(catalogue["problems"][0], model)
    return cat.validate(catalogue, model)


def test_proved_requires_review_novelty_search_and_package(data):
    def mutate(problem, model):
        problem["status"]["mathematical"] = "proved"
        problem["status"]["novelty"] = "unknown"
        problem["status"]["external_review"] = "not-reviewed"
        problem.pop("result", None)

    errors = "\n".join(mutated(data, mutate))
    assert "requires a 'result' package" in errors
    assert "not allowed while external_review is 'not-reviewed'" in errors
    assert "requires a documented novelty search" in errors


def test_formal_complete_requires_receipt(data):
    def mutate(problem, model):
        problem["status"]["formal"] = "complete"
        problem.pop("formal_receipt", None)

    assert any("requires 'formal_receipt'" in error for error in mutated(data, mutate))


def test_prior_resolution_requires_source(data):
    def mutate(problem, model):
        problem["status"]["mathematical"] = "previously-resolved"
        problem["status"]["novelty"] = "unknown"

    errors = "\n".join(mutated(data, mutate))
    assert "'previously-resolved' requires novelty 'prior-resolution-identified'" in errors


def test_unknown_status_value_is_rejected(data):
    def mutate(problem, model):
        problem["status"]["novelty"] = "novel"

    assert any(error.startswith("schema:") for error in mutated(data, mutate))


def test_missing_score_and_missing_dossier_are_rejected(data):
    def mutate(problem, model):
        problem["scores"].pop("tractability")
        problem["dossier"] = "research/candidates/does-not-exist.md"

    errors = "\n".join(mutated(data, mutate))
    assert "missing scores ['tractability']" in errors
    assert "does not exist" in errors


def test_active_status_requires_working_directory(data):
    def mutate(problem, model):
        problem["slug"] = "no-such-directory"
        problem["status"]["mathematical"] = "candidate-proof"

    assert any("requires research/active/" in error for error in mutated(data, mutate))


def test_unchecked_statement_cannot_become_active(data):
    def mutate(problem, model):
        problem["status"]["mathematical"] = "active-investigation"
        problem["source"]["statement_checked_against"] = "not-checked"

    assert any("requires a statement checked against a source" in error for error in mutated(data, mutate))


def test_shortlist_must_be_eligible(data):
    catalogue, model = copy.deepcopy(data[0]), copy.deepcopy(data[1])
    gated = next(entry["id"] for entry in cat.rank(catalogue, model) if entry["failed_gates"])
    model["shortlist"] = {"decided": "2026-11-26", "problems": [gated], "rationale": "test"}
    assert any("fails an eligibility gate" in error for error in cat.validate(catalogue, model))


# ------------------------------------------------------------- instructions --


def test_status_values_in_agents_md_match_the_schema():
    schema = cat.load_json(cat.SCHEMA)
    status = schema["$defs"]["problem"]["properties"]["status"]["properties"]
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    rows = {"Mathematical": "mathematical", "Formal verification": "formal", "Novelty": "novelty", "External review": "external_review"}
    for label, key in rows.items():
        row = next(line for line in agents.splitlines() if line.startswith(f"| {label} |"))
        assert re.findall(r"`([a-z-]+)`", row) == status[key]["enum"], label


def test_claude_md_imports_agents_md_and_agent_files_are_well_formed():
    assert "@AGENTS.md" in (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    agents = sorted((ROOT / ".claude" / "agents").glob("*.md"))
    assert len(agents) == 7
    for path in agents:
        text = path.read_text(encoding="utf-8")
        front = text.split("---")[1]
        assert f"name: {path.stem}" in front and "description:" in front
        assert "AGENTS.md" in text, f"{path.name} must defer to AGENTS.md"
    for skill in ("research-session", "review-claim"):
        text = (ROOT / ".claude" / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
        assert f"name: {skill}" in text.split("---")[1]


def test_allowed_axioms_are_stated_consistently():
    import verify_lean

    for document in ("AGENTS.md", "docs/verification-policy.md"):
        text = (ROOT / document).read_text(encoding="utf-8")
        for axiom in verify_lean.ALLOWED_AXIOMS:
            assert f"`{axiom}`" in text, f"{document} does not name {axiom}"


def test_relative_markdown_links_resolve():
    skip_parts = {".venv", ".lake", ".git", "node_modules", ".pytest_cache"}
    broken = []
    for path in ROOT.rglob("*.md"):
        if skip_parts & set(path.parts) or "templates" in path.parts:
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        # Only targets that look like paths; formulas such as "](1+x" are not links.
        for target in re.findall(r"\]\(([A-Za-z0-9_.~/#%-]+)\)", text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            if not resolved.exists():
                broken.append(f"{path.relative_to(ROOT).as_posix()} -> {target}")
    assert not broken, "\n".join(broken)


def test_no_result_is_claimed_without_a_package(data):
    catalogue, _ = data
    packages = [p for p in (ROOT / "results").iterdir() if p.is_dir()]
    settled = [p for p in catalogue["problems"] if p["status"]["mathematical"] in cat.SETTLED_STATUSES]
    assert len(packages) == len(settled)


def test_registry_and_lean_root_are_consistent():
    registry = json.loads((ROOT / "formalization" / "registry.json").read_text(encoding="utf-8"))
    root_module = (ROOT / "formalization" / "Conjectura.lean").read_text(encoding="utf-8")
    assert "NegativeTests" not in re.sub(r"/-.*?-/", "", root_module, flags=re.S)
    for entry in registry["theorems"]:
        assert entry["kind"] in {"calibration", "research"}
        assert re.fullmatch(r"[0-9a-f]{64}", entry["statement_fingerprint"])
