"""Source scanning and receipt freshness (no Lean toolchain required)."""

from __future__ import annotations

import json

import verify_lean


def test_scan_finds_forbidden_constructs():
    assert verify_lean.scan_source("theorem t : 1 = 2 := by\n  sorry\n") == ["sorry"]
    assert verify_lean.scan_source("axiom a : False\n") == ["axiom declaration"]
    assert verify_lean.scan_source("private axiom a : False\n") == ["axiom declaration"]
    assert verify_lean.scan_source("theorem t : 2 = 2 := by native_decide\n") == ["native_decide"]
    assert verify_lean.scan_source("unsafe def f : Nat := 0\n") == ["unsafe"]
    assert verify_lean.scan_source("set_option debug.skipKernelTC true in\n") == ["debug.skipKernelTC"]
    assert verify_lean.scan_source('@[implemented_by g] def f := 0\n') == ["implemented_by"]


def test_scan_ignores_comments_strings_and_identifiers():
    clean = "\n".join(
        [
            "/- This proof used to be `sorry`. /- nested: axiom -/ still a comment -/",
            "-- unsafe native_decide admit",
            'def message : String := "sorry, no axiom here"',
            "theorem axiomatic_name : True := trivial  -- identifier containing 'axiom'",
            "theorem sorry_free (h : True) : True := h",
        ]
    )
    assert verify_lean.scan_source(clean) == []


def test_comment_stripping_preserves_line_structure():
    text = "a\n/- x\ny -/\nb -- c\n"
    assert verify_lean.strip_comments_and_strings(text).count("\n") == text.count("\n")


def test_latest_passing_receipt_matches_current_sources(root):
    """A receipt is evidence only for the exact files it hashed.

    If this fails, a verified input changed after the last verification:
    rerun `python scripts/verify_lean.py` and commit the new receipt.
    """
    receipts = sorted((root / "verification" / "receipts").glob("*-passed.json"))
    assert receipts, "no passing verification receipt is committed"
    receipt = json.loads(receipts[-1].read_text(encoding="utf-8"))
    assert receipt["verdict"] == "passed"
    assert all(check["status"] == "passed" for check in receipt["checks"])
    assert set(receipt["declarations"]["axioms_used"]) <= verify_lean.ALLOWED_AXIOMS
    recorded = {source["path"]: source["sha256_lf"] for source in receipt["sources"]}
    current = {
        path.relative_to(root).as_posix(): verify_lean.sha256_text_file(path)
        for path in verify_lean.tracked_inputs(receipt["module"])
    }
    assert recorded == current, "verified inputs changed since the latest receipt"
