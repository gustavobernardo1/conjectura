"""The registry of mathematical contributions and the generated project summary."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import catalogue as cat  # noqa: E402

RECEIPT = "verification/receipts/20261126T065234Z-89343c82fa-passed.json"


@pytest.fixture(scope="module")
def data():
    return cat.load_json(cat.CATALOGUE), cat.load_json(cat.PRIORITIES)


def record(**fields) -> dict:
    """A minimal exploratory record: the required fields and nothing else."""
    base = {
        "id": "MD-9001",
        "type": "lemma",
        "title": "A lemma used only by the tests",
        "statement": "For every natural number n, n + 0 = n.",
        "registered": "2026-11-26",
        "provenance": {
            "contributors": [{"who": "test-model", "kind": "ai-model", "role": "statement and proof"}],
            "record": "AGENTS.md",
        },
        "evidence": [],
        "status": {"mathematical": "candidate", "formal": "not-started", "novelty": "unknown", "external_review": "not-reviewed"},
    }
    return base | fields


def status(**changes) -> dict:
    return record()["status"] | changes


def registry(*records) -> dict:
    return {"schema_version": 1, "updated": "2026-11-26", "discoveries": list(records)}


def review_of(target: dict, date: str = "2026-11-26") -> dict:
    return {
        "kind": "review",
        "path": "AGENTS.md",
        "by": "another-model",
        "date": date,
        "revision": "0652128",
        "statement_fingerprint": cat.fingerprint(target["statement"]),
    }


def errors(data, *records) -> str:
    return "\n".join(cat.validate_discoveries(registry(*records), data[0]))


# ------------------------------------------------------------------ registry --


def test_committed_registry_is_valid_and_summary_is_current(data):
    committed = cat.load_registry()
    assert cat.validate_discoveries(committed, data[0]) == []
    previous = cat.load_json(cat.SUMMARY)
    rebuilt = cat.build_summary(*data, committed, previous, rebind=False)
    assert cat.SUMMARY.read_text(encoding="utf-8") == cat.summary_text(rebuilt)


def test_minimal_exploratory_record_is_enough(data):
    assert errors(data, record()) == ""


def test_identifier_is_independent_of_type_and_statuses_are_those_of_the_catalogue(data):
    assert errors(data, record(type="conjecture")) == ""
    assert "discoveries schema" in errors(data, record(id="L-1"))
    assert "discoveries schema" in errors(data, record(type="miracle"))
    assert "discoveries schema" in errors(data, record(status=status(novelty="novel")))
    assert "duplicate id" in errors(data, record(), record())
    assert "describes a catalogued problem" in errors(data, record(status=status(mathematical="active-investigation")))


def test_documented_types_and_relations_match_the_schema():
    schema = cat.load_json(cat.REGISTRY_SCHEMA)["$defs"]["discovery"]["properties"]
    policy = (ROOT / "docs" / "research-policy.md").read_text(encoding="utf-8")
    for value in schema["type"]["enum"] + schema["relations"]["items"]["properties"]["type"]["enum"]:
        assert f"`{value}`" in policy, f"docs/research-policy.md does not name {value}"


def test_standing_separates_candidates_established_rediscovered_and_withdrawn():
    assert cat.standing(record()) == "candidate"
    assert cat.standing(record(status=status(mathematical="candidate-proof"))) == "candidate"
    assert cat.standing(record(status=status(mathematical="proved", novelty="no-prior-resolution-found"))) == "established"
    known = status(mathematical="previously-resolved", novelty="prior-resolution-identified")
    assert cat.standing(record(status=known)) == "rediscovered"
    assert cat.standing(record(status=status(mathematical="rejected"))) == "withdrawn"


def test_a_registered_statement_is_not_thereby_proved_new_or_reviewed(data):
    """Each stronger status needs its own evidence; the identifier supplies none."""
    reviewed = record(status=status(external_review="ai-reviewed"))
    assert "requires review evidence bound to the statement" in errors(data, reviewed)
    searched = record(status=status(novelty="no-prior-resolution-found"))
    assert "requires a documented 'novelty_search'" in errors(data, searched)
    known = record(status=status(mathematical="previously-resolved", novelty="prior-resolution-identified"))
    assert "requires 'resolution_source'" in errors(data, known)
    formal = record(status=status(formal="complete"), formal_receipt=RECEIPT)
    assert "receipt does not cover a theorem registered for this record" in errors(data, formal)
    proved = errors(data, record(status=status(mathematical="proved")))
    for message in ("requires a 'result' package", "'not-reviewed'", "documented novelty search", "'resolved_on'"):
        assert message in proved


def test_a_review_is_bound_to_the_statement_it_covered(data):
    reviewed = record(status=status(external_review="ai-reviewed"))
    reviewed["evidence"] = [review_of(reviewed)]
    assert errors(data, reviewed) == ""
    assert cat.stale_evidence(registry(reviewed)) == []

    changed = copy.deepcopy(reviewed)
    changed["statement"] = "For every integer n, n + 0 = n."
    assert "requires review evidence bound to the statement" in errors(data, changed)
    assert "covers an earlier statement" in cat.stale_evidence(registry(changed))[0]

    reformatted = copy.deepcopy(reviewed)
    reformatted["statement"] = "For every natural   number n,\nn + 0 = n."
    assert errors(data, reformatted) == ""

    incomplete = copy.deepcopy(reviewed)
    del incomplete["evidence"][0]["revision"]
    assert "lacks ['revision']" in errors(data, incomplete)


def test_proof_dependencies_are_pinned_and_a_changed_statement_forces_reassessment(data):
    lemma = record()
    exploratory = record(id="MD-9002", depends_on=[{"ref": "MD-9001"}, {"citation": "Graham and Pollak (1971), determinant of the distance matrix"}])
    assert errors(data, lemma, exploratory) == ""

    claimed = copy.deepcopy(exploratory) | {"status": status(mathematical="candidate-proof")}
    assert "to be pinned to a statement fingerprint" in errors(data, lemma, claimed)
    claimed["depends_on"][0]["statement_fingerprint"] = cat.fingerprint(lemma["statement"])
    assert errors(data, lemma, claimed) == ""

    restated = lemma | {"statement": "For every natural number n, 0 + n = n."}
    assert "at a statement that has since changed; reassess MD-9002" in errors(data, restated, claimed)

    assert "unknown contribution MD-9003" in errors(data, record(depends_on=[{"ref": "MD-9003"}]))
    assert "depends on itself" in errors(data, record(depends_on=[{"ref": "MD-9001"}]))
    cycle = record(depends_on=[{"ref": "MD-9002"}])
    assert "circular proof dependency" in errors(data, cycle, exploratory)


def test_promotion_requires_established_dependencies(data):
    lemma = record()
    theorem = record(
        id="MD-9002",
        type="theorem",
        status=status(mathematical="proved", novelty="no-prior-resolution-found", external_review="ai-reviewed"),
        depends_on=[{"ref": "MD-9001", "statement_fingerprint": cat.fingerprint(lemma["statement"])}],
    )
    assert "not allowed while its dependency MD-9001 is 'candidate'" in errors(data, lemma, theorem)


def test_relations_are_contextual_and_must_resolve(data):
    related = record(
        relations=[
            {"type": "originated_from", "target": "CJ-0001", "local_id": "L9"},
            {"type": "contributes_to", "target": "CJ-0002"},
            {"type": "generalizes", "target": "MD-9002"},
        ]
    )
    assert errors(data, related, record(id="MD-9002")) == ""
    assert errors(data, record(id="MD-9002")) == ""  # a contribution needs no parent
    assert "points to unknown MD-9002" in errors(data, related)
    assert "points to unknown CJ-9999" in errors(data, record(relations=[{"type": "refutes", "target": "CJ-9999"}]))
    assert "discoveries schema" in errors(data, record(relations=[{"type": "depends_on", "target": "CJ-0001"}]))
    misplaced = record(relations=[{"type": "implies", "target": "MD-9002", "local_id": "L9"}])
    assert "local_id is only meaningful" in errors(data, misplaced, record(id="MD-9002"))

    old = record(status=status(mathematical="superseded"))
    assert "'superseded' requires another contribution" in errors(data, old)
    new = record(id="MD-9002", relations=[{"type": "supersedes", "target": "MD-9001"}])
    assert errors(data, old, new) == ""


def test_evidence_is_referenced_not_copied_and_a_pinned_file_may_not_change(data, tmp_path):
    (tmp_path / "notes.md").write_text("origin\n", encoding="utf-8")
    proof = tmp_path / "proof.md"
    proof.write_text("Proof. Trivial.\n", encoding="utf-8")
    pinned = record(evidence=[{"kind": "proof", "path": "proof.md#lemma", "sha256": cat.sha256_lf(proof)}])
    pinned["provenance"]["record"] = "notes.md"
    assert cat.validate_discoveries(registry(pinned), data[0], tmp_path) == []

    proof.write_text("Proof. By induction.\n", encoding="utf-8")
    assert "changed since it was recorded" in "\n".join(cat.validate_discoveries(registry(pinned), data[0], tmp_path))
    missing = record(evidence=[{"kind": "note", "path": "no-such-file.md"}])
    assert "evidence no-such-file.md does not exist" in errors(data, missing)


def test_a_project_conjecture_becomes_a_problem_only_through_its_registry_record(data):
    catalogue, model = copy.deepcopy(data[0]), data[1]
    catalogue["problems"][0]["discovery"] = "MD-9001"
    as_lemma = "\n".join(cat.validate(catalogue, model, registry=registry(record())))
    assert "is not a registered contribution of type 'conjecture'" in as_lemma
    as_conjecture = "\n".join(cat.validate(catalogue, model, registry=registry(record(type="conjecture"))))
    assert "is not a registered contribution" not in as_conjecture
    assert "(investigated as CJ-0001)" in cat.render(catalogue, model, registry(record(type="conjecture")))


# ------------------------------------------------------------------- summary --

LATEST = [
    "highest_priority_investigation",
    "latest_proved_conjecture",
    "latest_disproved_conjecture",
    "latest_registered_contribution",
    "latest_reviewed_contribution",
    "latest_formally_verified_contribution",
    "latest_contribution_with_originality_assessment",
]


def test_summary_uses_explicit_nulls_when_nothing_qualifies(data):
    catalogue = copy.deepcopy(data[0])
    for problem in catalogue["problems"]:
        problem["status"]["mathematical"] = "candidate"
    summary = cat.summarize(catalogue, data[1], registry())
    assert all(key in summary and summary[key] is None for key in LATEST)
    assert summary["active_investigations"] == []
    assert summary["counts"]["contributions"]["by_standing"] == {"candidate": 0, "established": 0, "rediscovered": 0, "withdrawn": 0}


def test_summary_excludes_rediscovered_results_and_calibration(data):
    conjecture = record(type="conjecture", registered="2026-11-20")
    lemma = record(id="MD-9002", registered="2026-11-22", status=status(external_review="ai-reviewed"))
    lemma["evidence"] = [review_of(lemma, "2026-11-23")]
    searched = record(
        id="MD-9003",
        type="bound",
        registered="2026-11-21",
        status=status(novelty="preliminary-search-completed"),
        novelty_search={"as_of": "2026-11-24", "coverage": "One arXiv listing search.", "limitations": "No citation search was made."},
    )
    known = record(
        id="MD-9004",
        type="identity",
        registered="2026-11-25",
        status=status(mathematical="previously-resolved", novelty="prior-resolution-identified", external_review="ai-reviewed"),
        resolution_source={"citation": "A textbook.", "url": "https://example.org/"},
    )
    known["evidence"] = [review_of(known, "2026-11-26")]
    everything = registry(conjecture, lemma, searched, known)
    assert cat.validate_discoveries(everything, data[0]) == []

    summary = cat.summarize(*data, everything)
    counts = summary["counts"]
    assert counts["contributions"]["registered"] == 4
    assert counts["contributions"]["counted"] == 3
    assert counts["contributions"]["by_type"] == {"bound": 1, "conjecture": 1, "lemma": 1}
    assert counts["contributions"]["by_status"]["external_review"] == {"ai-reviewed": 1, "not-reviewed": 2}
    assert counts["contributions"]["by_standing"]["rediscovered"] == 1
    assert counts["excluded_from_contribution_counts"] == {"rediscovered": 1, "withdrawn": 0, "calibration_theorems": 2}

    # The rediscovered identity is the most recent record and the most recently reviewed one.
    assert summary["latest_registered_contribution"]["id"] == "MD-9002"
    assert summary["latest_reviewed_contribution"]["id"] == "MD-9002"
    assert summary["latest_reviewed_contribution"]["review"]["by"] == "another-model"
    assert summary["latest_contribution_with_originality_assessment"]["id"] == "MD-9003"
    assert summary["latest_formally_verified_contribution"] is None
    assert summary["latest_proved_conjecture"] is None
    assert summary["latest_registered_contribution"]["evidence"] == ["AGENTS.md"]


def test_summary_names_its_sources_and_is_stable_when_they_do_not_change(data):
    committed = cat.load_registry()
    first = cat.build_summary(*data, committed)
    generated = first["generated"]
    assert set(generated) == {"date", "branch", "revision", "sources_committed", "sources"}
    assert generated["sources"]["research/discoveries.json"] == cat.git_blob_id(cat.REGISTRY)
    stale = copy.deepcopy(first)
    stale["generated"] |= {"date": "2001-01-01", "revision": "0" * 40}
    assert cat.build_summary(*data, committed, stale, rebind=False) == stale
    stale["generated"]["sources"]["research/discoveries.json"] = "0" * 40
    assert cat.build_summary(*data, committed, stale, rebind=False)["generated"]["date"] != "2001-01-01"


# ------------------------------------------------------------ public summary --


def public_errors(block: dict) -> list[str]:
    validator = cat.jsonschema.Draft202012Validator(cat.load_json(cat.PUBLIC_SCHEMA))
    return [error.message for error in validator.iter_errors(block)]


SEARCH = {"as_of": "2026-11-19", "coverage": "A documented search.", "limitations": "Stated."}


def promoted(**fields) -> dict:
    settled = status(mathematical="proved", novelty="no-prior-resolution-found", external_review="ai-reviewed")
    return record(**({"status": settled, "result": "results/README.md", "resolved_on": "2026-11-20", "novelty_search": SEARCH} | fields))


def test_public_block_of_the_committed_summary_follows_its_schema(data):
    block = cat.load_json(cat.SUMMARY)["public"]
    assert public_errors(block) == []
    assert public_errors(block | {"unannounced_field": 1}) != []
    assert block["primary_investigation"] == (block["active_investigations"] or [None])[0]


def test_public_block_uses_zeros_and_explicit_nulls_when_nothing_qualifies(data):
    catalogue = copy.deepcopy(data[0])
    for problem in catalogue["problems"]:
        problem["status"]["mathematical"] = "candidate"
    # A candidate proof is registered, and it is not counted.
    block = cat.summarize(catalogue, data[1], registry(record(status=status(mathematical="candidate-proof"))))["public"]
    assert public_errors(block) == []
    assert block["active_investigations"] == [] and block["primary_investigation"] is None
    assert block["established_original_discoveries"] == {"lemmas": 0, "theorems": 0, "counterexamples": 0, "other": 0, "total": 0}
    assert block["resolved_conjectures"] == {"proved": 0, "disproved": 0, "total": 0}
    assert block["latest_established_original_discovery"] is None
    assert block["latest_formally_verified_original_contribution"] is None


def test_public_block_counts_only_promoted_original_records_and_each_once(data):
    preliminary = status(mathematical="proved", novelty="preliminary-search-completed", external_review="ai-reviewed")
    records = [
        promoted(id="MD-9001", type="lemma", resolved_on="2026-11-21"),
        promoted(id="MD-9002", type="theorem", resolved_on="2026-11-23", formal_receipt=RECEIPT, status=promoted()["status"] | {"formal": "complete"}),
        promoted(id="MD-9003", type="counterexample"),
        promoted(id="MD-9004", type="bound"),
        promoted(id="MD-9005", type="theorem", status=preliminary, resolved_on="2026-11-25"),
        promoted(id="MD-9006", type="theorem", status=promoted()["status"] | {"mathematical": "candidate-proof"}),
        record(id="MD-9007", status=status(mathematical="previously-resolved", novelty="prior-resolution-identified")),
        promoted(id="MD-9008", status=promoted()["status"] | {"mathematical": "superseded"}),
        record(id="MD-9009", type="conjecture"),
    ]
    catalogue = copy.deepcopy(data[0])
    settled = {"result": "results/README.md", "resolved_on": "2026-11-22"}
    first, second, third, fourth = catalogue["problems"][1:5]
    first |= settled | {"status": promoted()["status"]}
    second |= settled | {"status": promoted()["status"] | {"mathematical": "disproved"}}
    third |= settled | {"status": preliminary}  # originality not sufficiently assessed
    fourth |= settled | {"status": promoted()["status"], "discovery": "MD-9009"}  # formulated by the project

    block = cat.summarize(catalogue, data[1], registry(*records))["public"]
    assert public_errors(block) == []
    counts = block["established_original_discoveries"]
    assert counts == {"lemmas": 1, "theorems": 1, "counterexamples": 1, "other": 1, "total": 4}
    assert counts["total"] == sum(value for key, value in counts.items() if key != "total")
    # The theorem MD-9002 is counted as a theorem; the conjectures are counted apart from it.
    assert block["resolved_conjectures"] == {"proved": 1, "disproved": 1, "total": 2}

    latest = block["latest_established_original_discovery"]
    assert (latest["id"], latest["type"], latest["established_on"]) == ("MD-9002", "theorem", "2026-11-23")
    assert latest["url"] == "https://github.com/gustavobernardo1/conjectura/blob/research/results/README.md"
    assert latest["status"]["external_review"] == "ai-reviewed"
    verified = block["latest_formally_verified_original_contribution"]
    assert verified["id"] == "MD-9002" and verified["verified_utc"] == cat.load_json(ROOT / RECEIPT)["created_utc"]

    primary = block["primary_investigation"]
    assert primary == block["active_investigations"][0] and primary["id"] == "CJ-0001"
    assert primary["url"].startswith("https://github.com/gustavobernardo1/conjectura/blob/research/research/candidates/CJ-0001-")
    assert block["reviewed_results_url"] == "https://github.com/gustavobernardo1/conjectura/tree/research/results"
