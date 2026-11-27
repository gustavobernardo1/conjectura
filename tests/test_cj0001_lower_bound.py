"""Regression tests for `lower_bound.py` (CJ-0001, session 11; notes/lower-bound.md).

Values marked "by hand" can be recomputed on paper; the other counts are regression values obtained
by running the script. The last three tests are negative controls: the checker must report failures
when it is given a wrong formula.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

EXPERIMENT = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"
sys.path.insert(0, str(EXPERIMENT))

import lower_bound as lb  # noqa: E402


def assert_no_failure(part: dict) -> None:
    assert part["completed"]
    assert part["failures_total"] == 0, part["first_failures"]
    assert part["first_failures"] == {}
    assert all(row["cases"] > 0 and row["failures"] == 0 for row in part["checks"].values())


def test_cone_membership_by_hand():
    # (1+2x)^2 = (1+x)^2 + 2x(1+x) + x^2 is in C_2;  1 + x + x^2 = (1+x)^2 - x is not.
    assert lb.in_C([1, 4, 4], 2)
    assert not lb.in_C([1, 1, 1], 2)
    # Degree above d is a failure; the zero polynomial is in every cone; x is in C_2 (e = 1, i = 0).
    assert not lb.in_C([1, 1, 1], 1)
    assert lb.in_C([], -1) and lb.in_C([0, 0], 0) and not lb.in_C([1], -1)
    assert lb.in_C([0, 1], 2) and not lb.in_C([0, -1], 2)
    assert lb.lam([1, 4, 6, 4, 1], 2) == 2 and lb.lam([3], 1) == -3


def test_single_vertex_and_edge_by_hand():
    # One vertex (proof of Theorem T5, a = 1): Psi = 1, H = G = Omega = 0, R = -(1+2x)^2, E = 0.
    r = lb.rooted_record([], 1, 0)
    assert (r["Psi"], r["H"], r["G"], r["Om"], r["R"], r["E"]) == ([1], [], [], [], [-1, -4, -4], [])
    assert r["av"] == {} and r["R1"] == [] and r["Q1"] == []
    # One edge rooted at an end: Phi = 1 + 2x, Psi = 1 + x, H = a_v = 1, G = Omega = 0,
    # R = x l - (1+4x) Phi with l = 1 - 4x^2, E = R + (1+2x)^2 (1+x) = 0,
    # R(A, e_u) = Q1 + x^2 a_v = x + x^2, with Q1 = adj(M1)_{uv} = x.
    r = lb.rooted_record([(0, 1)], 2, 0)
    assert (r["Phi"], r["Psi"], r["H"], r["G"], r["Om"]) == ([1, 2], [1, 1], [1], [], [])
    assert r["R"] == [-1, -5, -8, -4] and r["E"] == []
    assert r["av"] == {1: [1]} and r["Q1"] == [0, 1] and r["R1"] == [0, 1, 1]
    # The planted tree is the path on three vertices rooted at an end: H^ = Phi, Omega^ = R(A, e_u).
    assert r["planted"]["H"] == [1, 2] and r["planted"]["Om"] == [0, 1, 1]


def test_rooted_trees_are_counted_by_A000081():
    assert [len(lb.rooted_trees(a)) for a in range(1, 9)] == [1, 1, 2, 4, 9, 20, 48, 115]


def test_distance_polynomial_by_hand():
    # P_3: l = 2 + 6x - 4x^3.  P_4: det(D - xI) = x^4 - 20x^2 - 32x - 12, so d = (3, 16, 20).
    assert lb.ell_distance([-1, 0, 1]) == [2, 6, 0, -4]
    assert lb.d_coefficients([-1, 0, 1, 2]) == [3, 16, 20]
    # The same from the edge list, and from R(T, 0) (Proposition S23(a)).
    assert lb.parents_from_edges(4, [(2, 3), (1, 2), (0, 1)]) == [-1, 0, 1, 2]
    assert lb.ell_from_R(lb.WT(4, [(0, 1), (1, 2), (2, 3)], [0] * 4)) == [3, 16, 20, 0, -4]
    # Star on 4 vertices: (1+x)^2 (3 + 8x - 4x^2) = 3 + 14x + 15x^2 - 4x^4.
    assert lb.star_closed_form(4) == [3, 14, 15, 0, -4]
    assert lb.ell_distance(lb.star_parents(4)) == [3, 14, 15, 0, -4]


def test_contraction_of_the_middle_edge_of_P4_by_hand():
    # T = P_4, T' = the star: l_T - l_T' = 2x + 5x^2; S36 with A = B = an edge (H = 1, E = G = 0)
    # gives x(2 + 5x).
    par = [-1, 0, 1, 2]
    assert lb.contracted_parents(par, 2) == [-1, 0, 1, 1]
    diff = [a - b for a, b in zip(lb.d_coefficients(par), lb.d_coefficients(lb.contracted_parents(par, 2)))]
    assert diff == [0, 2, 5] and lb.in_C(diff, 3)
    edge = lb.rooted_record([(0, 1)], 2, 0)
    assert lb.s36_right_side(edge, edge) == [0, 2, 5]
    eT, eTp = lb.s36_trees(edge, edge)
    assert sorted(eT) == [(0, 1), (0, 2), (2, 3)] and sorted(eTp) == [(0, 1), (0, 2), (0, 3)]


def test_parts_on_small_orders():
    a, records = lb.part_A(6)
    assert_no_failure(a)
    assert a["rooted_trees_by_order"] == {"1": 1, "2": 1, "3": 2, "4": 4, "5": 9, "6": 20}
    # by hand: 20 checks per rooted tree, 3 per pair (rooted tree, vertex other than the root), 6 counts
    assert a["cases_total"] == 37 * 20 + 3 * (1 + 2 * 2 + 3 * 4 + 4 * 9 + 5 * 20) + 6 == 1205

    b = lb.part_B(records, 6)
    assert_no_failure(b)
    # by hand: orders (1, 1..6), (2, 2..5), (3, 3..4): 37 + 16 + 12 pairs, 4 checks each
    assert b["pairs"] == 65 and b["cases_total"] == 4 * 65
    assert b["pairs_by_orders"]["1,6"] == 20 and b["pairs_by_orders"]["3,4"] == 8

    c = lb.part_C(records, 7)
    assert_no_failure(c)
    assert c["pairs"] == 65 and c["pairs_with_a_single_vertex_tree"] == 37 and c["cases_total"] == 5 * 65

    d = lb.part_D(9)
    assert_no_failure(d)
    assert [row["trees"] for row in d["rows"]] == [2, 3, 6, 11, 23, 47]
    assert [row["tree_edge_pairs"] for row in d["rows"]] == [1, 3, 9, 23, 60, 150]
    assert d["cases_total"] == 4 * 246

    e = lb.part_E(9)
    assert_no_failure(e)
    assert [row["trees"] for row in e["rows"]] == [1, 1, 2, 3, 6, 11, 23, 47]
    # Equality in T6(c) for exactly one tree of each order (the star).
    assert [row["trees_with_gap_equal_to_star"] for row in e["rows"]][1:] == [1] * 7
    # by hand (Remark 3 of Theorem T6): n = 4, 6, 8 give 1, 10, 49.
    assert [row["star_gap"] for row in e["rows"]] == [None, 4, 1, 20, 10, 84, 49, 336]
    assert e["cases_total"] == 8 + 7 + 3 + 94 + 94 + 93 + 93


def test_negative_control_wrong_formula_for_s36():
    # x(2 + 4x) instead of x(2 + 5x): the formula must fail exactly on the pairs with a, b >= 2.
    _, records = lb.part_A(5)
    c = lb.part_C(records, 6, middle=(0, 2, 4))
    wrong = c["checks"]["S36_formula"]
    # by hand: orders (1, 1..5), (2, 2..4), (3, 3): 17 + 7 + 4 pairs, 17 of them with a single vertex
    assert wrong["cases"] == c["pairs"] == 28
    assert wrong["failures"] == c["pairs"] - c["pairs_with_a_single_vertex_tree"] == 11
    assert "S36_formula" in c["first_failures"]
    assert c["checks"]["S36_difference_in_C(n-1)"]["failures"] == 0


def test_negative_control_wrong_star():
    # 4(n-1)x instead of 4(n-2)x in the closed form of the star.
    def wrong_star(n):
        return lb.pmul(lb.binom_row(n - 2), [n - 1, 4 * (n - 1), -4])

    e = lb.part_E(8, star=wrong_star)
    assert e["checks"]["S23d_star_closed_form"] == {"cases": 7, "failures": 7}
    assert e["checks"]["T6b_l_minus_star_in_C(n-1)"]["failures"] > 0
    assert e["first_failures"]["S23d_star_closed_form"]["order"] == 2


def test_negative_control_contraction_reversed_and_tally():
    # l_T' - l_T is the negative of a non-zero element of the cone, hence not in it.
    par = [-1, 0, 1, 2, 3, 3]
    d, dp = lb.d_coefficients(par), lb.d_coefficients(lb.contracted_parents(par, 3))
    assert lb.in_C([a - b for a, b in zip(d, dp)], 5)
    assert not lb.in_C([b - a for a, b in zip(d, dp)], 5)
    tally = lb.Tally()
    assert tally.check("demo", True) and not tally.check("demo", False, lambda: {"case": 1})
    tally.check("demo", False, lambda: {"case": 2})
    assert tally.as_dict() == {"checks": {"demo": {"cases": 3, "failures": 2}}, "cases_total": 3,
                               "failures_total": 2, "first_failures": {"demo": {"case": 1}}}


def test_stored_result():
    stored = json.loads((EXPERIMENT / "results" / "lower-bound.json").read_text(encoding="utf-8"))
    assert stored["summary"]["completed"] and stored["summary"]["failures_total"] == 0
    for part in "ABCDE":
        assert_no_failure(stored[part])
    assert stored["A"]["rooted_trees"] == 486
    assert stored["B"]["pairs"] == 1064 and stored["C"]["pairs"] == 1064
    # The pairs of the scratch run of session 11 (both orders at most 8): 778.
    assert stored["B"]["pairs"] - stored["B"]["pairs_by_orders"]["1,9"] == 778
    assert stored["D"]["tree_edge_pairs"] == 220181 and stored["E"]["trees"] == 32507
