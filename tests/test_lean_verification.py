"""The Lean verification pipeline accepts valid proofs and rejects deficient ones.

The negative tests use the deliberately deficient modules in
``formalization/NegativeTests``. Each test asserts not only that the verdict is
``failed`` but that the *intended* check is the one that fails.
"""

from __future__ import annotations

import copy
import json

import pytest

import verify_lean
from verify_lean import FAILED, NOT_RUN, PASSED

pytestmark = pytest.mark.lean


def negative(module: str, registry: dict | None = None, replay: bool = False) -> verify_lean.Report:
    registry = registry or {"theorems": []}
    return verify_lean.verify(module=f"NegativeTests.{module}", prefix="NegativeTests", registry=registry, replay=replay)


def details(report: verify_lean.Report, name: str) -> str:
    return "\n".join(report.check(name).details)


# ---------------------------------------------------------------- positive --


def test_library_passes_every_check():
    report = verify_lean.verify()
    assert {check.name: check.status for check in report.checks} == {
        "toolchain": PASSED,
        "build": PASSED,
        "sources": PASSED,
        "axioms": PASSED,
        "registry": PASSED,
        "replay": PASSED,
    }
    assert report.verdict == PASSED
    used = {axiom for declaration in report.declarations for axiom in declaration["axioms"]}
    assert used <= verify_lean.ALLOWED_AXIOMS


def test_skipped_replay_is_not_a_pass():
    report = verify_lean.verify(replay=False)
    assert report.check("replay").status == NOT_RUN
    assert report.verdict == FAILED


# ---------------------------------------------------------------- negative --


def test_sorry_is_rejected():
    report = negative("SorryProof")
    assert report.check("build").status == PASSED  # Lean only warns about sorry
    assert report.check("sources").status == FAILED
    assert report.check("axioms").status == FAILED
    assert "sorryAx" in details(report, "axioms")
    assert report.verdict == FAILED


def test_custom_axiom_is_rejected():
    report = negative("CustomAxiom")
    assert report.check("build").status == PASSED
    assert report.check("axioms").status == FAILED
    assert "NegativeTests.convenient" in details(report, "axioms")
    assert "project-declared axiom" in details(report, "axioms")


def test_native_decide_is_rejected():
    report = negative("NativeDecide")
    assert report.check("build").status == PASSED
    assert report.check("axioms").status == FAILED
    assert "native_decide" in details(report, "axioms")
    assert report.check("sources").status == FAILED


def test_false_statement_fails_to_build():
    report = negative("WrongProof")
    assert report.check("build").status == FAILED
    assert report.check("axioms").status == FAILED  # nothing could be audited
    assert report.check("replay").status == NOT_RUN
    assert report.verdict == FAILED


def test_unsafe_definition_and_disabled_kernel_are_rejected():
    report = negative("UnsafeDef")
    assert report.check("axioms").status == FAILED
    assert "is unsafe" in details(report, "axioms")
    assert "debug.skipKernelTC" in details(report, "sources")


def test_vacuous_theorem_is_rejected_without_witness():
    registry = {
        "theorems": [
            {
                "name": "NegativeTests.vacuous_claim",
                "kind": "research",
                "catalogue_id": "CJ-0000",
                "source_statement": "fictitious",
                "statement_fingerprint": "",
            }
        ]
    }
    report = negative("Vacuous", registry=registry)
    # Kernel-valid and axiom-free: only the registry policy can catch it.
    assert report.check("build").status == PASSED
    assert report.check("sources").status == PASSED
    assert report.check("axioms").status == PASSED
    assert report.check("registry").status == FAILED
    assert "non-vacuity" in details(report, "registry")


def test_kernel_bypass_is_caught_by_replay_not_by_axiom_audit():
    report = negative("KernelBypass", replay=True)
    assert report.check("build").status == PASSED
    # `bogus : False` depends on no axioms, so the axiom audit alone accepts it.
    assert report.check("axioms").status == PASSED
    assert report.check("replay").status == FAILED
    assert report.verdict == FAILED


def test_changed_statement_invalidates_registry():
    registry = json.loads(verify_lean.REGISTRY.read_text(encoding="utf-8"))
    tampered = copy.deepcopy(registry)
    tampered["theorems"][0]["statement_fingerprint"] = "0" * 64
    report = verify_lean.verify(registry=tampered, replay=False)
    assert report.check("registry").status == FAILED
    assert "fingerprint differs" in details(report, "registry")


def test_unregistered_theorem_name_is_rejected():
    registry = {
        "theorems": [
            {
                "name": "Conjectura.Calibration.does_not_exist",
                "kind": "calibration",
                "nonvacuity": {"not_needed": "n/a"},
                "statement_fingerprint": "",
            }
        ]
    }
    report = verify_lean.verify(registry=registry, replay=False)
    assert report.check("registry").status == FAILED
    assert "not found" in details(report, "registry")
