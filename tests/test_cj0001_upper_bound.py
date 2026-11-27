"""Regression tests for `upper_bound.py` (CJ-0001, session 12).

Values marked "by hand" can be recomputed on paper from Laplacian spectra; the other counts are regression values
obtained by running the script.  Negative controls check that a false inequality and a wrong merge identity are
reported as failures.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import pytest

EXPERIMENT = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"
sys.path.insert(0, str(EXPERIMENT))

import upper_bound as ub  # noqa: E402


def assert_no_failure(part: dict) -> None:
    assert part["completed"]
    assert part["failures_total"] == 0, part["first_failures"]
    assert all(row["cases"] > 0 and row["failures"] == 0 for row in part["checks"].values())


def test_trace_by_hand_and_three_methods():
    # Laplacian spectra: P_2 {0,2}; P_3 {0,1,3}; K_{1,3} {0,1,1,4}; P_4 {0, 2-sqrt2, 2, 2+sqrt2}
    cases = [(1, [], Fraction(1)),
             (2, [(0, 1)], Fraction(4, 3)),
             (3, [(0, 1), (1, 2)], Fraction(7, 4)),
             (4, [(0, 1), (0, 2), (0, 3)], Fraction(11, 5))]
    for n, e, want in cases:
        assert ub.tr_charpoly(n, e) == ub.tr_inverse(n, e) == ub.tr_gauss(n, e) == want
    # P_4: 1 + 1/3 + 1/(3-sqrt2) + 1/(3+sqrt2) = 1 + 1/3 + 6/7 = 46/21
    assert ub.tr_charpoly(4, ub.path_edges(4)) == ub.tr_path_continuant(4) == Fraction(46, 21)
    v = ub.part_V(8, 20)
    assert_no_failure(v)
    assert [r["trees"] for r in v["rows"]] == [1, 1, 1, 2, 3, 6, 11, 23]


def test_path_minimality_small_and_equality_only_for_path():
    a, c = ub.part_AC(10, 10)
    assert_no_failure(a)
    assert [r["trees"] for r in a["rows"]] == [1, 1, 2, 3, 6, 11, 23, 47, 106]
    assert all(r["paths"] == 1 for r in a["rows"])
    # by hand, order 4: the star has tr = 11/5 = 231/105, the path 46/21 = 230/105: difference 1/105
    row4 = a["rows"][2]
    assert row4["non_paths"] == 1
    star, path = ub.tr_charpoly(4, [(0, 1), (0, 2), (0, 3)]), ub.tr_path_continuant(4)
    assert row4["min_tr_minus_tr_path_over_non_paths"]["exact"] == "%d/%d" % ((star - path).numerator, (star - path).denominator)
    assert star - path == Fraction(1, 105)
    assert_no_failure(c)
    assert [r["trees"] for r in c["rows"]] == [1, 2, 3, 6, 11, 23, 47, 106]


def test_peak_condition_by_hand_and_negative_control():
    # P_4: d = (3, 16, 20), peak index 2; 5*16 = 80 < (5*2+3)^2 = 169: holds.  A peak at n-1 would give m = 1:
    # 80 < 64 is false (bound n - n/sqrt5 + 3/5 = 2.81 < 3).
    assert ub.peak_condition(4, 2) and not ub.peak_condition(4, 3)
    assert ub.peak_slack(4, 2) == 169 - 80
    # negative control: pretend the peak of every tree of order 6 is at index 5 (= n-1); the condition fails
    assert not ub.peak_condition(6, 5)
    # the threshold is exact: n = 5, p = 2 (m = 3): 125 < 144 holds, p = 3 (m = 2): 125 < 169 holds, p = 4: 125 < 64 fails
    assert ub.peak_condition(5, 3) and not ub.peak_condition(5, 4)


def test_path_peaks_and_closed_form():
    res = ub.part_C_path(70, 30)
    assert_no_failure(res)
    assert res["matrix_checked_to"] == 30 and res["n_with_peak_neither"] == [] and res["n_with_tied_peak"] == []
    # n <= 60 with peak ceil(n - n/sqrt 5): as in results/tree-shift.json
    assert [n for n in res["first_ceil_cases"] if n <= 60] == [9, 18, 27, 36, 45, 47, 54, 56]
    assert float(res["min_fractional_part_when_peak_is_ceil"]["value"]) > 0.4


def test_path_value_bounds():
    b1 = ub.part_B1(60)
    assert_no_failure(b1)
    # by hand: tr(P_1) - 2/5 = 3/5 > 1/sqrt5 = 0.447
    assert Fraction(3, 5) ** 2 > Fraction(1, 5)
    b2 = ub.part_B2(20)
    assert_no_failure(b2)
    assert float(b2["max_relative_difference"]) < 1e-50
    # negative control: n/sqrt5 + 1/2 is not the value (the constant matters), so the 50-digit comparison would fail
    from decimal import Decimal, getcontext
    getcontext().prec = 90
    s5 = Decimal(5).sqrt()
    t = ub.tr_path_continuant(10)
    assert abs(Decimal(t.numerator) / Decimal(t.denominator) - (10 / s5 + Decimal(1) / 2)) > Decimal(10) ** -3
    getcontext().prec = 28


def test_pendant_path_merging():
    d = ub.part_D(5, 6)
    assert_no_failure(d)
    # rooted trees of order 2..5: 1 + 2 + 4 + 9 = 16; pairs (p,q) with q <= p, p+q <= 6: 1+1+2+2+3 = 9 (sums 2..6)
    assert d["rooted_trees"] == 16 and d["pairs_pq"] == 9 and d["cases"] == 144
    # by hand: X = an edge rooted at an end, p = q = 1: the root has degree 3, T(1,1) is the star K_{1,3}, tr = 11/5;
    # T(2,0) = P_4, tr = 46/21; 11/5 - 46/21 = 1/105 > 0.
    n1, e1 = ub.glue_paths(2, [(0, 1)], 0, [1, 1])
    n2, e2 = ub.glue_paths(2, [(0, 1)], 0, [2])
    assert n1 == n2 == 4 and ub.tr_charpoly(n1, e1) == Fraction(11, 5) and ub.tr_charpoly(n2, e2) == ub.tr_path_continuant(4)
    assert ub.tr_charpoly(n1, e1) > ub.tr_charpoly(n2, e2)


def test_path_inequality_c0_c_r():
    e = ub.part_E(12)
    assert_no_failure(e)
    assert e["equalities"] == [[2, 1]]
    # by hand, N = 2: (I+L)^{-1} for P_3 = (1/8)[[5,2,1],[2,4,2],[1,2,5]]; c(0) = [(Q^2)_00]/Q_00 = (30/64)/(5/8) = 3/4
    # and c(1) = (24/64)/(4/8) = 3/4: equal.
    Q = ub.inverse_entries(3, ub.path_edges(3))
    assert Q[0][0] == Fraction(5, 8) and Q[1][1] == Fraction(1, 2)
    c0 = sum(Q[0][j] * Q[j][0] for j in range(3)) / Q[0][0]
    c1 = sum(Q[1][j] * Q[j][1] for j in range(3)) / Q[1][1]
    assert c0 == c1 == Fraction(3, 4)


def test_merge_identity_and_negative_control():
    m = ub.part_M(4)
    assert_no_failure(m)
    # rooted trees with 1..4 vertices: 1 + 1 + 2 + 4 = 8, ordered pairs 64
    assert m["rooted_trees"] == 8 and m["ordered_pairs"] == 64
    # by hand: A = B = a single vertex: T = a single vertex, g = k = 1, eps = 0, g_T = 1, tr = 1 + 1 - 1 - 0 = 1
    assert ub.merge_sides(Fraction(1), Fraction(1), Fraction(1), Fraction(1), Fraction(1), Fraction(1)) == (1, 1)
    # negative control: the flipped sign of the correction term is reported as a failure
    wrong = ub.part_M(4, perturb=True)
    assert wrong["checks"]["M_tr_T_identity"]["failures"] > 0
    assert wrong["checks"]["M_g_T_equals_1_over_1_plus_eps_sum"]["failures"] == 0


def test_exploratory_interlacing_small():
    f = ub.part_F(8)
    assert_no_failure(f)
    assert "EXPLORATORY" in f["kind"]


def test_stored_result():
    path = EXPERIMENT / "results" / "upper-bound.json"
    if not path.exists():
        pytest.skip("stored result not yet written")
    stored = json.loads(path.read_text(encoding="utf-8"))
    assert stored["summary"]["completed"]
    assert stored["summary"]["failures_of_exact_checks"] == 0 and stored["summary"]["failures_of_exploratory_checks"] == 0
    for part in ("V", "A", "B1", "B2", "C_path", "C_all_trees", "D", "E", "M", "F_exploratory"):
        assert_no_failure(stored[part])
