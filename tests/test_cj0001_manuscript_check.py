"""Regression tests for `manuscript_check.py` (CJ-0001, session 14).

The script checks, from the definitions of manuscripts/CJ-0001-collins-shor/main.tex, the identities and cone
memberships of the lower half. Negative controls check that the cone test rejects non-members and that a wrong
identity would be counted as a failure.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

EXPERIMENT = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"
sys.path.insert(0, str(EXPERIMENT))

import manuscript_check as mc  # noqa: E402


def test_cone_membership_by_hand():
    # x = x^1 (1+x)^0 has weight 2: in K_2, not in K_3; x(1+x) has weight 3.
    assert mc.inK([0, 1], 2)
    assert not mc.inK([0, 1], 3)
    assert mc.inK([0, 1, 1], 3)
    # (1+x)^2 - x = 1 + x + x^2 is in K_1 but not in K_2 (its coordinate at (1+x)^2 is 1, then -x remains).
    assert mc.inK([1, 1, 1], 1)
    assert not mc.inK([1, 1, 1], 2)
    assert not mc.inK([-1], 0)


def test_star_polynomial_by_hand():
    # ell of K_2 is 1 - 4x^2; of P_3 = S_3 is (1+x)(2+4x-4x^2) = 2 + 6x + 0x^2 - 4x^3.
    assert mc.ell_direct(2, [(0, 1)]) == [1, 0, -4]
    assert mc.ell_direct(3, [(0, 1), (1, 2)]) == [2, 6, 0, -4]


def test_small_run_has_no_failure():
    res = mc.main(5, 7, 5)
    assert res["failures_total"] == 0, res["first_failures"]
    assert res["cases_total"] > 600
    assert all(row["cases"] > 0 for row in res["checks"].values())


def test_negative_control_wrong_identity_is_reported():
    t = mc.Tally()
    t.ok("wrong", mc.add([1], [1]) == [Fraction(3)], "witness")
    assert t.f["wrong"] == 1 and t.first["wrong"] == "witness"
