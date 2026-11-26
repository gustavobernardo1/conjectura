"""Regression tests for `rooted_state.py` (CJ-0001, session 8; notes/rooted-calculus.md).

Values marked "by hand" can be recomputed on paper from the formulas of the note; the other counts
are regression values obtained by running the script.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

EXPERIMENT = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"
sys.path.insert(0, str(EXPERIMENT))

import rooted_state as rs  # noqa: E402

IDENTITY_FAILURES = [
    "A1_G_negative", "A1_Omega_negative", "A2_failures", "A3_failures", "A4_failures",
    "A5_failures", "A6_failures", "A7_failures",
]


def test_single_vertex_state_by_hand():
    # One vertex of weight n: Psi = 1, H = n, G = n x, Omega = 0, R = (n-1)(1+5x+4x^2) + (n-1)^2 x.
    for n in range(4):
        T = rs.WT(1, [], [n])
        s = rs.state(T, 0)
        assert rs.ptrim(s["Psi"]) == [1]
        assert rs.ptrim(s["H"]) == rs.ptrim([n])
        assert rs.ptrim(s["G"]) == rs.ptrim([0, n])
        assert rs.ptrim(s["Om"]) == []
        assert rs.ptrim(s["R"]) == rs.ptrim([n - 1, 5 * (n - 1) + (n - 1) ** 2, 4 * (n - 1)])
        # Lambda = x [(n+1) + (n^2 + 6n + 1) x + n x^2]
        assert rs.ptrim(rs.Lambda(T, 0)) == rs.ptrim([0, n + 1, n * n + 6 * n + 1, n])


def test_half_gamma_by_hand():
    # 1 + x + x^2 = (1+x)^2 - x is not in C_2;  (1+2x)^2 = (1+x)^2 + 2x(1+x) + x^2 is in C_2.
    assert rs.half_gamma([1, 1, 1], 2) == [1, -1, 0]
    assert rs.half_gamma([1, 4, 4], 2) == [1, 2, 3]
    assert rs.in_cone([1, 4, 4], 2) and not rs.in_cone([1, 1, 1], 2)


def test_identities_on_a_small_range():
    out = rs.part_A(3, 1, 2)
    ident = out["identities"]
    assert ident["rooted"] == 1 * 2 + 2 * 4 + 3 * 8  # by hand: trees with 1, 2, 3 vertices, weights 0/1, every root
    assert ident["A7_pairs"] == (1 * 2 + 2 * 4) ** 2  # by hand: ordered pairs of rooted trees with at most 2 vertices
    for key in IDENTITY_FAILURES:
        assert ident[key] == 0, key
    cone = out["cone"]
    for key in rs.CONE_KEYS:
        assert cone[key + "_failures"] == 0, key
    assert out["first_failures"] == {}


def test_leading_coefficients_on_stars_by_hand():
    # Proposition S21: [x^{q+3}] F = prod(1+n_i) (4 + n_0 - sum n_i/(1+n_i)); six leaves of weight 3: 4^6 (4 - 9/2).
    T = rs.star(6, 0, [3] * 6)
    F = rs.ptrim(T.F(0))
    assert len(F) - 1 == 9 and F[-1] == -2048
    # (S) with u = v the centre, four leaves of weight 4: 5^4 (3 - 16/5).
    T = rs.star(4, 0, [4] * 4)
    S = rs.ptrim(rs.S_poly(T, 0, 0))
    assert len(S) - 1 == 8 and S[-1] == -125


def test_counterexamples_and_what_survives():
    ex = rs.named_examples()
    five = ex["E2_star_5_leaves_weight_4"]
    assert five["F"] == [1, 36, 554, 4744, 24505, 76600, 134500, 102500]
    assert five["half_gamma_F_degree_8"][-1] == -1 and not five["F_in_cone"]
    assert five["E"][-1] == 112500  # by hand: 5^5 (4 + 8 * 4)
    assert five["E_in_cone"] and five["Lambda_in_cone"] and five["R_in_cone"]
    assert not ex["E2_star_6_leaves_weight_3"]["F_in_cone"]
    assert ex["E2_star_6_leaves_weight_3"]["Lambda_in_cone"]
    assert not ex["S_star_4_leaves_weight_4_u_v_centre"]["S_in_cone"]


def test_stored_result_has_no_identity_failure_and_no_failure_of_lambda():
    stored = json.loads((EXPERIMENT / "results" / "rooted-state.json").read_text(encoding="utf-8"))
    for key in IDENTITY_FAILURES:
        assert stored["part_A_B"]["identities"][key] == 0, key
    assert stored["part_C"]["counts"]["C1_failures"] == 0
    for part in ("part_A_B", "part_C", "part_D"):
        cone = stored[part]["cone"]
        for key in ("B3_Lambda", "B4_monotone", "B5_R"):
            assert cone[key + "_cases"] > 0 and cone[key + "_failures"] == 0, (part, key)
    # (E'') and (S) hold on the exhaustive range of session 7 and fail on stars with heavier leaves.
    assert stored["part_A_B"]["cone"]["B1_F_failures"] == 0
    assert stored["part_A_B"]["cone"]["B2_S_failures"] == 0
    assert stored["part_C"]["cone"]["B1_F_failures"] > 0
    assert stored["part_C"]["cone"]["B2_S_failures"] > 0
