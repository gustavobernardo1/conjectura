"""Regression tests for the CJ-0001 computations of session 7 and of objective O7.

`component_form.py` runs its whole computation at import time, so it is run as a script with small
parameters. `slope_family.py` (search) and `slope_family_verify.py` (independent checker, different
method) are imported. Pinned counts are regression values obtained by running the scripts; the
values marked "by hand" can be recomputed on paper.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

EXPERIMENT = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"
sys.path.insert(0, str(EXPERIMENT))

import slope_family  # noqa: E402
import slope_family_extension  # noqa: E402
import slope_family_verify  # noqa: E402

# Failure counters that are zero in the stored full run (results/component-form.json).
# `part3_estar_not_in_cone` is not in this list: it is 972 in the full run.
COMPONENT_FORM_ZERO = {
    "part1": [
        "not_all_real_negative", "degree_not_t_plus_1", "lead_identity_failures", "kappa_below_4",
        "kappa_equal_4_with_a_at_least_2", "kappa_not_4_with_a_1", "magnitude_identity_failures",
        "component_identity_failures", "component_R_not_in_cone",
    ],
    "part2": [
        "R_not_in_cone", "recurrence_failures", "delta_not_in_cone", "trees_with_no_good_leaf",
        "trees_with_some_bad_leaf", "part3_weight_formula_failures", "part3_R0_not_in_cone",
        "part3_E_not_in_cone", "part3_E_minus_xR_not_in_cone", "part3_third_form_failures",
    ],
}


def test_stored_component_form_result_has_the_zero_counters_asserted_below():
    stored = json.loads((EXPERIMENT / "results" / "component-form.json").read_text(encoding="utf-8"))
    for part, keys in COMPONENT_FORM_ZERO.items():
        for key in keys:
            assert stored[part][key] == 0, (part, key)
    assert stored["part2"]["part3_estar_not_in_cone"] > 0


def test_component_form_small_run():
    done = subprocess.run(
        [sys.executable, str(EXPERIMENT / "component_form.py"), "--max-skeleton", "5", "--max-component", "4",
         "--max-weight", "2", "--max-component3", "4"],
        capture_output=True, text=True,
    )
    assert done.returncode == 0, done.stdout[-2000:] + done.stderr[-2000:]
    res = json.loads(done.stdout)
    for part, keys in COMPONENT_FORM_ZERO.items():
        for key in keys:
            assert res[part][key] == 0, (part, key)
    p1, p2 = res["part1"], res["part2"]
    # By hand: the trees with 2, 3, 4, 5 vertices number 1, 1, 2, 3, and a tree with s vertices has
    # 2^s - 2 subsets A with 1 <= |A| <= s - 1.
    assert p1["trees"] == 1 + 1 + 2 + 3 == 7
    assert p1["subsets"] == (2**2 - 2) + (2**3 - 2) + 2 * (2**4 - 2) + 3 * (2**5 - 2) == 126
    # By hand: the non-zero weights in {0, 1, 2}^j on the trees with 1, 2, 3, 4 vertices (1, 1, 1, 2 trees).
    assert p2["weighted_trees"] == (3 - 1) + (3**2 - 1) + (3**3 - 1) + 2 * (3**4 - 1) == 196
    # Regression values (obtained by running the script with these parameters).
    assert p1["magnitude_cases"] == 98
    assert p1["independent_A"] == 62
    assert p1["components"] == 90
    assert p1["min_kappa_minus_4_num_den"] == [1, 1]
    assert p2["leaf_cases"] == 450
    assert p2["part3_leaf_cases"] == 450
    assert {j: c["weighted_trees"] for j, c in p2["by_order"].items()} == {"1": 2, "2": 8, "3": 26, "4": 160}
    assert {j: c["leaf_cases"] for j, c in p2["by_order"].items()} == {"1": 0, "2": 12, "3": 48, "4": 390}
    assert p2["part3_estar_not_in_cone"] == 0  # regression value for this small range only


def test_slope_family_single_vertex_by_hand():
    # One vertex of weight nu: Phi = 1 + nu x, adj = 1, p = 1 + (2 - nu) x, so
    # F = (1 + 5x + 3x^2)(1 + nu x) + (x + 4x^2) + 2x^2 (1 + (2 - nu) x)
    #   = 1 + (6 + nu) x + (9 + 5 nu) x^2 + (4 + nu) x^3.
    assert slope_family.F_value([], [0], 0) == [1, 6, 9, 4]
    assert slope_family.F_value([], [1], 0) == [1, 7, 14, 5]
    assert slope_family.F_value([], [2], 0) == [1, 8, 19, 6]
    for nu in range(6):
        assert slope_family.F_value([], [nu], 0) == [1, 6 + nu, 9 + 5 * nu, 4 + nu]
        assert slope_family_verify.f_polynomial(1, [], [nu], 0) == [1, 6 + nu, 9 + 5 * nu, 4 + nu]


def test_slope_family_path_on_three_vertices_by_hand():
    # Path 0 - 1 - 2 with weights (1, 0, 2): M = [[1+2x, -x, 0], [-x, 1+2x, -x], [0, -x, 1+3x]],
    # det M = (1+2x)[(1+2x)(1+3x) - x^2] - x^2 (1+3x) = 1 + 7x + 14x^2 + 7x^3,
    # adj_00 = (1+2x)(1+3x) - x^2, adj_01 = x(1+3x), adj_02 = x^2.
    phi, adj, _ = slope_family.weighted_data({0: [1], 1: [0, 2], 2: [1]}, (0, 1, 2), (1, 0, 2))
    assert phi == [1, 7, 14, 7]
    assert [slope_family.ptrim(entry) for entry in adj[0]] == [[1, 5, 5], [0, 1, 3], [0, 0, 1]]


def test_half_gamma_by_hand():
    # (1+x)^2 = 1 * (1+x)^2; 2 + 5x + x^2 = 2(1+x)^2 + x - x^2 is not in C_2 (twice the example of
    # notes/gamma-components.md); 1 + 6x + 9x^2 + 4x^3 = (1+x)^3 + 3x(1+x) + 3x^2 + 3x^3.
    assert slope_family.half_gamma([1, 2, 1], 2) == [1, 0, 0]
    assert slope_family.half_gamma([2, 5, 1], 2) == [2, 1, -1]
    assert not slope_family.hg_ok([2, 5, 1], 2)
    assert slope_family.half_gamma([1, 6, 9, 4], 3) == [1, 3, 3, 3]
    for poly, d in (([1, 2, 1], 2), ([2, 5, 1], 2), ([1, 6, 9, 4], 3)):
        assert slope_family_verify.cone_report(poly, d)["expansion"] == slope_family.half_gamma(poly, d)


def test_slope_family_small_range():
    res = slope_family.run(3, 1)
    assert res["complete"]
    # By hand: one tree for each of j = 1, 2, 3; 2^j weights; j vertices u; j^2 pairs (u, v).
    assert res["trees"] == 3
    assert res["weighted_trees"] == 2 + 4 + 8
    e2, leaf, s = res["E2"], res["leaf"], res["S"]
    assert (e2["cases_nu_zero"], e2["cases_nu_nonzero"]) == (1 + 2 + 3, 1 * 1 + 2 * 3 + 3 * 7)
    assert (e2["failures_nu_zero"], e2["failures_nu_nonzero"]) == (0, 0)
    # By hand: j = 2 has 2 pairs (leaf w, u != w), all with v = u; the path on 3 vertices has 2 leaves
    # and for each of them u = v (the centre) or u = the other leaf.
    assert leaf["leaf_cases"] == 4 * 2 + 8 * 4 == 40
    assert (leaf["cases_v_eq_u"], leaf["cases_v_ne_u"]) == (4 * 2 + 8 * 2, 8 * 2)
    assert leaf["slope_cases"] == 2 * 2 + 4 * 4 == 20  # weights with nu_w >= 1: half of them when W = 1
    assert leaf["identity_failures_v_ne_u"] == 0
    assert leaf["identity_failures_v_eq_u"] == 0
    assert leaf["slope_identity_failures"] == 0
    assert s["cases"] == 1 * 2 + 4 * 4 + 9 * 8 == 90
    assert s["failures"] == 0
    assert s["bracket_not_in_C_j_plus_2"] == 0
    # The bracket has constant term 1 and degree at most j + 2, so it is never in C_{j+3}.
    assert s["bracket_not_in_C_j_plus_3"] == s["cases"]


def test_slope_family_leaf_cases_for_five_vertices_and_weights_up_to_two():
    # The range of the scratch computation recorded in STATE.md (10,089 cases): for each tree,
    # 3^j weights times the number of pairs (leaf w, vertex u != w).
    res = slope_family.run(5, 2)
    by_hand = 9 * 2 + 27 * 4 + 81 * (2 * 3 + 3 * 3) + 243 * (2 * 4 + 3 * 4 + 4 * 4)
    assert res["leaf"]["leaf_cases"] == by_hand == 10089
    assert res["leaf"]["identity_failures_v_ne_u"] == 0
    assert res["leaf"]["identity_failures_v_eq_u"] == 0
    assert res["leaf"]["slope_identity_failures"] == 0
    assert res["E2"]["failures_nu_zero"] == res["E2"]["failures_nu_nonzero"] == 0
    assert res["S"]["failures"] == 0


def test_counterexample_to_E2_on_the_star_with_five_leaves_by_hand():
    # Star with centre 0 of weight 0 and five leaves of weight 4, u = the centre. By hand, with m = 1 + 5x:
    # Phi = m^4 (1 + 10x + 20x^2), adj_uu = m^5, pi_u = m^4 (1 - 3x)(1 + 10x), so
    # F = m^4 [(1+5x+3x^2)(1+10x+20x^2) + (x+4x^2)(1+5x) + 2x^2 (1-3x)(1+10x)] = m^4 (1 + 16x + 84x^2 + 164x^3):
    # the terms in x^4 cancel (60 - 60). F has degree 7 and F(0) = 1, and a polynomial P in C_8 has
    # [x^8] P >= P(0); so F is not in C_8 = C_{j+2}: statement (E'') of STATE.md fails here (nu != 0).
    edges = [[1, 0], [0, 2], [0, 3], [0, 4], [0, 5]]
    nu = [0, 4, 4, 4, 4, 4]
    by_hand = slope_family.pmul([1, 20, 150, 500, 625], [1, 16, 84, 164])
    assert by_hand == [1, 36, 554, 4744, 24505, 76600, 134500, 102500]
    assert slope_family.F_value(edges, nu, 0) == by_hand
    assert slope_family_verify.f_polynomial(6, edges, nu, 0) == by_hand
    assert slope_family.half_gamma(by_hand, 8) == [1, 28, 358, 2836, 16055, 71856, 133946, 102464, -1]
    check = slope_family_verify.check_f_instance(dict(order=6, edges=edges, nu=nu, u=0, F=by_hand))
    assert check["hypotheses_hold"] and check["nu_nonzero"] and check["violation_confirmed"]
    # With leaf weights at most 3 the same star is in the cone (regression value).
    assert slope_family.hg_ok(slope_family.F_value(edges, [0, 3, 3, 3, 3, 3], 0), 8)


def test_counterexample_to_S_on_the_star_with_four_leaves():
    # The smallest failure of (S) in the stored run (results/slope-family.json): star with centre 0 of
    # weight 0, leaves of weights 2, 3, 4, 4, u = v = the centre. S has a negative leading coefficient.
    edges = [[1, 0], [0, 2], [0, 3], [0, 4]]
    nu = [0, 2, 3, 4, 4]
    expected = [0, 1, 28, 324, 1994, 6905, 12765, 9824, -5]
    assert slope_family_verify.s_polynomial(5, edges, nu, 0, 0) == expected
    nbrs = {0: [1, 2, 3, 4], 1: [0], 2: [0], 3: [0], 4: [0]}
    _, adj, _ = slope_family.weighted_data(nbrs, (0, 1, 2, 3, 4), tuple(nu))
    bracket = slope_family.padd(slope_family.F_value(edges, [1, 2, 3, 4, 4], 0),
                                [0, 0, 0] + slope_family.pscale(adj[0][0], -2))
    assert [0] + bracket == expected
    assert not slope_family.hg_ok(expected, 8)
    check = slope_family_verify.check_s_instance(dict(order=5, edges=edges, nu=nu, u=0, v=0, S=expected))
    assert check["hypotheses_hold"] and check["violation_confirmed"] and check["cone"]["has_negative_coefficient"]
    # The leaf extension: a sixth vertex attached at the centre with weight n; F leaves C_8 first at n = 59.
    ext = slope_family_extension.extend(dict(order=5, edges=edges, nu=nu, u=0, v=0, S=expected), 60)
    assert ext["E2_scan"]["first_failure_n"] == 59
    assert ext["difference_equals_S"] is True
    assert ext["E_scan"] == dict(n_from=1, n_to=60, cases=60, failures=0, first_failure_n=None)
    assert ext["E_equals_xR_plus_F"] is True


def test_stored_slope_family_result():
    # The stored run (orders 1 to 6, weights 0 to 4): case counts by hand, and the recorded outcome.
    stored = json.loads((EXPERIMENT / "results" / "slope-family.json").read_text(encoding="utf-8"))
    assert stored["complete"] and stored["provenance"]["arguments"]["max_order"] == 6
    assert stored["provenance"]["arguments"]["max_weight"] == 4
    trees = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 6}
    assert stored["trees"] == sum(trees.values()) == 14
    assert stored["weighted_trees"] == sum(t * 5**j for j, t in trees.items()) == 104530
    e2, leaf, s = stored["E2"], stored["leaf"], stored["S"]
    assert e2["cases_nu_zero"] == sum(t * j for j, t in trees.items()) == 65
    assert e2["cases_nu_zero"] + e2["cases_nu_nonzero"] == sum(t * j * 5**j for j, t in trees.items()) == 614805
    assert s["cases"] == sum(t * j * j * 5**j for j, t in trees.items()) == 3630605
    # Numbers of leaves of the trees with j vertices, summed over the trees: 2, 2, 5, 9, 21.
    leaves = {2: 2, 3: 2, 4: 5, 5: 9, 6: 21}
    assert leaf["leaf_cases"] == sum(n * (j - 1) * 5**j for j, n in leaves.items()) == 1763050
    assert leaf["slope_cases"] == sum(n * (j - 1) * 4 * 5 ** (j - 1) for j, n in leaves.items()) == 1410440
    assert leaf["cases_v_ne_u"] + leaf["cases_v_eq_u"] == leaf["leaf_cases"]
    assert leaf["identity_failures_v_ne_u"] == leaf["identity_failures_v_eq_u"] == 0
    assert leaf["slope_identity_failures"] == 0
    assert (e2["failures_nu_zero"], e2["failures_nu_nonzero"]) == (0, 1)
    assert (s["failures"], s["failures_nu_zero"], s["bracket_not_in_C_j_plus_2"]) == (7225, 0, 7655)
    assert s["smallest_failure"]["nu"] == [0, 2, 3, 4, 4]
    verify = json.loads((EXPERIMENT / "results" / "slope-family-verify.json").read_text(encoding="utf-8"))
    assert verify["summary"] == dict(S_instances=5, S_confirmed=5, E2_instances=6, E2_confirmed=6,
                                     E_instances=6, E_agreeing=6, E_in_cone=6)


def test_search_and_checker_agree_on_small_weighted_trees():
    # F and S from the Faddeev-LeVerrier code of slope_family.py against the evaluation and
    # interpolation of slope_family_verify.py, on every weighted tree with at most 4 vertices and
    # weights 0 and 1 (F, every u) and on the path with 3 vertices (S, every u and v).
    for j in range(1, 5):
        for tree in slope_family.trees_of_order(j):
            edges = [list(e) for e in tree.edges()]
            for mask in range(2**j):
                nu = [(mask >> i) & 1 for i in range(j)]
                for u in range(j):
                    assert slope_family.F_value(edges, nu, u) == slope_family_verify.f_polynomial(j, edges, nu, u)
    edges = [[0, 1], [1, 2]]
    nbrs = {0: [1], 1: [0, 2], 2: [1]}
    for nu in ([0, 0, 0], [1, 0, 2], [3, 1, 0]):
        _, adj, _ = slope_family.weighted_data(nbrs, (0, 1, 2), tuple(nu))
        for u in range(3):
            for v in range(3):
                raised = list(nu)
                raised[v] += 1
                bracket = slope_family.padd(slope_family.F_value(edges, raised, u),
                                            [0, 0, 0] + slope_family.pscale(adj[u][v], -2))
                assert slope_family.ptrim([0] + bracket) == slope_family_verify.s_polynomial(3, edges, nu, u, v)
