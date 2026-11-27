"""Regression tests for `tree_shift.py` (CJ-0001, session 12; notes/path-maximality.md).

Values marked "by hand" can be recomputed on paper; the other counts are regression values obtained by running
the script.  The negative controls check that a wrong formula, a reversed difference and a reversed shift are
reported as failures.  Part A (sympy) is tested only if sympy is importable.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

EXPERIMENT = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"
sys.path.insert(0, str(EXPERIMENT))

import lower_bound as lb  # noqa: E402
import tree_shift as ts  # noqa: E402


def assert_no_failure(part: dict) -> None:
    assert part["completed"]
    assert part["failures_total"] == 0, part["first_failures"]
    assert all(row["cases"] > 0 and row["failures"] == 0 for row in part["checks"].values())


def test_cone_K_by_hand():
    # x = x^1 (2e >= d for d = 2): in K_2; in K_3 the coordinates are (0, 1, -1): not in K_3.
    assert ts.in_K([0, 1], 2) and not ts.in_K([0, 1], 3)
    assert lb.ptrim(ts.k_coordinates([0, 1], 3)) == [0, 1, -1]
    # 1 + x = (1+x)^1 in K_1; 1 is not in K_1 (coordinates (1, -1)).
    assert ts.in_K([1, 1], 1) and not ts.in_K([1], 1)
    assert lb.ptrim(ts.k_coordinates([1], 1)) == [1, -1]
    # (1+2x)^2 = (1+x)^2 + 2x + 3x^2 in K_2 (basis (1+x)^2, x, x^2), coordinates (1, 2, 3); 1 + x + x^2 is not in K_2.
    assert lb.ptrim(ts.k_coordinates([1, 4, 4], 2)) == [1, 2, 3] and not ts.in_K([1, 1, 1], 2)
    # K_d is above its degree: x^5 is in K_2 but not in C_2; zero is in every cone; the cones are nested K_{d+1} in K_d.
    assert ts.in_K([0, 0, 0, 0, 0, 1], 2) and not ts.in_Cd([0, 0, 0, 0, 0, 1], 2) and ts.in_K([], 4)
    # agreement with lower_bound.in_C on polynomials of degree <= d
    for p, d in (([1, 4, 4], 2), ([1, 1, 1], 2), ([0, 2, 5], 3), ([0, -1], 2), ([3, 14, 15, 0, -4], 4)):
        assert ts.in_Cd(p, d) == lb.in_C(p, d)


def test_shifts_by_hand():
    # P_5 has the three shifts (1,2), (2,3), (1,3); the star none; the chair (spider 1,1,2) exactly one.
    assert len(ts.tree_shifts(ts.adjacency(5, [(0, 1), (1, 2), (2, 3), (3, 4)]))) == 3
    assert ts.tree_shifts(ts.adjacency(5, [(0, 1), (0, 2), (0, 3), (0, 4)])) == []
    n, e = ts.spider([1, 1, 2])
    assert len(ts.tree_shifts(ts.adjacency(n, e))) == 1
    # P_4: the shift along the middle edge gives the star (S36 with A = B = an edge).
    adjl = ts.adjacency(4, [(0, 1), (1, 2), (2, 3)])
    (x, y, path), = ts.tree_shifts(adjl)
    assert (x, y, path) == (1, 2, [1, 2])
    assert sorted(ts.apply_shift([(0, 1), (1, 2), (2, 3)], adjl, x, y, path)) == [(0, 1), (1, 2), (1, 3)]


def test_independent_method_agrees_with_flint():
    # P_4: det(D - xI) = x^4 - 20x^2 - 32x - 12, d = (3, 16, 20); the independent method shares no code with flint.
    n, e = 4, [(0, 1), (1, 2), (2, 3)]
    assert ts.independent_d(n, e) == [3, 16, 20] == ts.d_of(n, e)
    for edges in ([(0, 1), (0, 2), (0, 3), (0, 4), (4, 5)], [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (4, 6)]):
        n = len(edges) + 1
        assert ts.independent_d(n, edges) == ts.d_of(n, edges)


def test_sequences_of_S37_by_hand():
    a = ts.a_seq(4)
    # a_0 = 1, a_1 = 1+2x, a_2 = (1+2x)^2 - x^2 = 1 + 4x + 3x^2
    assert a[:3] == [[1], [1, 2], [1, 4, 3]]
    # gamma_1 = 1, gamma_2 = a_1 + x a_0 = 1 + 3x; rho_1 = 0, rho_2 = x * (1*1*x^0*a_0) = x, rho_3 = x(2*a_0*... ) see below
    assert ts.gamma_k(a, 1) == [1] and ts.gamma_k(a, 2) == [1, 3] and ts.rho_k(a, 1) == [] and ts.rho_k(a, 2) == [0, 1]
    # rho_3 = x [ (1)(2) a_1 + (2)(1) x a_0 ] = x (2 + 4x + 2x) = 2x + 6x^2
    assert ts.rho_k(a, 3) == [0, 2, 6]


def test_lemma_S37_on_trees_and_negative_control():
    b = ts.part_B(8, 3)
    assert_no_failure(b)
    assert b["pairs"] > 0 and "S37_identity" in b["checks"]
    # k = 1 is Proposition S36 (A = B = an edge: H = 1, E = G = 0): difference x(2+5x).
    _, records = lb.part_A(2)
    edge = records[2][0]
    lT, lTp = (ts.d_of(4, ts.build_Tk(edge, edge, 1)), ts.d_of(4, ts.build_Tk_prime(edge, edge, 1)))
    assert [p - q for p, q in zip(lT, lTp)] == [0, 2, 5]
    # negative control: a wrong coefficient (6x instead of 2x in the G-hat G-hat term) is detected exactly where
    # G-hat_A G-hat_B != 0, and every other check still passes
    wrong = ts.part_B(8, 3, scales=(1, 3, 1, 1))
    assert wrong["checks"]["S37_identity"]["failures"] > 0
    assert "S37_identity" in wrong["first_failures"]


def test_theorem_T7_T8_and_reversal_negative_controls():
    rc, re1, pm = ts.part_CE1(9, 9)
    assert_no_failure(rc)
    assert_no_failure(re1)
    assert [r["trees"] for r in rc["rows"]] == [3, 6, 11, 23, 47]
    assert [r["shifts"] for r in rc["rows"]][:2] == [4, 13]  # order 5: by hand (3 + 0 + 1)
    d = ts.part_D(10, 9)
    assert_no_failure(d)
    assert [r["trees"] for r in d["rows"]] == [2, 3, 6, 11, 23, 47, 106]
    assert [r["trees_with_l_equal_to_path"] for r in d["rows"]] == [1] * 7
    # reversed difference: for a shift T -> T', l_T' - l_T is not in the cone (non-zero element of a pointed cone)
    n = 6
    e = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5)]
    adjl = ts.adjacency(n, e)
    x, y, path = ts.tree_shifts(adjl)[0]
    dT, dTp = ts.d_of(n, e), ts.d_of(n, ts.apply_shift(e, adjl, x, y, path))
    diff = [p - q for p, q in zip(dT, dTp)]
    assert any(diff) and ts.in_Cd(diff, n - 1) and not ts.in_Cd([-c for c in diff], n - 1)


def test_PM_reversed_shift_is_a_violation():
    # (PM) holds along shifts; for some shift of an order-9 tree the peak strictly decreases, and then the REVERSED
    # pair (T', T) is reported as a violation by the same test.
    found = False
    for lay in ts.layouts(9):
        edges = lb.tree_edges(ts.parents_from_layout(lay))
        adjl = ts.adjacency(9, edges)
        dT = ts.d_of(9, edges)
        for x, y, path in ts.tree_shifts(adjl):
            dTp = ts.d_of(9, ts.apply_shift(edges, adjl, x, y, path))
            ok_max, ok_min, m1, m2 = ts.pm_margins(dT, dTp)
            assert ok_max and ok_min
            if ts.peaks(dTp)[1] < ts.peaks(dT)[1]:
                rev = ts.pm_margins(dTp, dT)
                assert not rev[0]
                found = True
    assert found


def test_E_families_and_random_small():
    e2 = ts.part_E2([20], 50, 10, 60, seed=1)
    assert_no_failure(e2)
    assert e2["trees"] > 0 and e2["shifts_tested"] > 0
    e3 = ts.part_E3(5, 5, 30, 40, seed=2)
    assert_no_failure(e3)
    # every generated family tree is a tree of the stated order
    for fam, nm, (n, edges) in ts.families(20):
        assert n == 20 and len(edges) == 19, nm
    assert len(ts.prufer_tree(30, __import__("random").Random(0))) == 29


def test_path_closed_form_and_peaks():
    # by hand: P_4 d = (3, 16, 20), P_3 d = (2, 6)
    assert ts.collins_d(3) == [2, 6] and ts.collins_d(4) == [3, 16, 20]
    f = ts.part_F(70, 60)
    assert_no_failure(f)
    assert f["matrix_checked_to"] == 60
    # P_4: M = 4 - isqrt(16 // 5) = 3, the peak is at 2 = floor(n - n/sqrt 5) = M - 1
    assert ts.peaks(ts.collins_d(4)) == (2, 2, 20)
    assert f["pmax_equals"]["neither"] == [] and f["pmin_equals"]["neither"] == []


def test_part_A_sympy_or_skip():
    res = ts.part_A(3)
    try:
        import sympy  # noqa: F401
    except ImportError:
        assert res["skipped"] and res["failures_total"] == 0
        return
    assert not res["skipped"]
    assert_no_failure(res)
    assert res["checks"]["A_det_factorization"]["cases"] == 1 and res["checks"]["A_Delta_k_equals_c_k"]["cases"] == 3


def test_stored_result():
    path = EXPERIMENT / "results" / "tree-shift.json"
    if not path.exists():
        pytest.skip("stored result not yet written")
    stored = json.loads(path.read_text(encoding="utf-8"))
    assert stored["summary"]["completed"] and stored["summary"]["failures_of_checked_statements"] == 0
    assert stored["summary"]["pm_violations_found"] == 0
    for part in ("B", "C", "D", "F", "E_i_exhaustive", "E_ii_families", "E_iii_random"):
        assert_no_failure(stored[part])
