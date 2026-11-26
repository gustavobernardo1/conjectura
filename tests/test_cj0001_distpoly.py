"""Validation of the CJ-0001 computation against known facts and an independent method."""

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"))

import distpoly  # noqa: E402
import independent_check  # noqa: E402


def edges_of(parents):
    return [(parent, vertex) for vertex, parent in enumerate(parents) if parent >= 0]


def canonical_form(n, edges):
    """Canonical string of an unlabelled tree: minimum AHU encoding over its centre(s)."""
    adjacency = {v: set() for v in range(n)}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)

    def encode(vertex, parent):
        return "(" + "".join(sorted(encode(child, vertex) for child in adjacency[vertex] if child != parent)) + ")"

    degree = {v: len(adjacency[v]) for v in range(n)}
    remaining = set(range(n))
    leaves = [v for v in remaining if degree[v] <= 1]
    while len(remaining) > 2:
        new_leaves = []
        for leaf in leaves:
            remaining.discard(leaf)
            for neighbour in adjacency[leaf]:
                if neighbour in remaining:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        new_leaves.append(neighbour)
        leaves = new_leaves
    return min(encode(centre, -1) for centre in remaining)


def test_path_on_three_vertices_by_hand():
    # D = [[0,1,2],[1,0,1],[2,1,0]]; det(D - xI) = -x^3 + 6x + 4, so delta_0 = 4, delta_1 = 6,
    # d_0 = 4/2 = 2, d_1 = 6, and s_k = 2 d_k.
    assert distpoly.distance_matrix(distpoly.path_parents(3)) == [[0, 1, 2], [1, 0, 1], [2, 1, 0]]
    assert distpoly.scaled_coefficients(distpoly.path_parents(3)) == [4, 12]
    assert independent_check.normalized_coefficients(3, [(0, 1), (1, 2)]) == [2, 6]


@pytest.mark.parametrize("order", range(1, 13))
def test_enumeration_counts_match_oeis_a000055(order):
    assert sum(1 for _ in distpoly.layouts(order)) == distpoly.A000055[order]


@pytest.mark.parametrize("order", range(2, 11))
def test_enumeration_yields_pairwise_nonisomorphic_trees(order):
    forms = set()
    for layout in distpoly.layouts(order):
        parents = distpoly.parents_from_layout(layout)
        assert all(parent < vertex for vertex, parent in enumerate(parents))
        forms.add(canonical_form(order, edges_of(parents)))
    assert len(forms) == distpoly.A000055[order]


@pytest.mark.parametrize("order", range(3, 10))
def test_flint_and_independent_method_agree_on_all_trees(order):
    for layout in distpoly.layouts(order):
        parents = distpoly.parents_from_layout(layout)
        scaled = distpoly.scaled_coefficients(parents)
        independent = independent_check.normalized_coefficients(order, edges_of(parents))
        assert [Fraction(value, 2 ** (order - 2)) for value in scaled] == independent


@pytest.mark.parametrize("order", range(3, 12))
def test_known_coefficients_on_all_trees(order):
    for layout in distpoly.layouts(order):
        parents = distpoly.parents_from_layout(layout)
        matrix = distpoly.distance_matrix(parents)
        scaled = distpoly.scaled_coefficients(parents)
        # Graham–Pollak: det D = (-1)^(n-1) (n-1) 2^(n-2), so d_0 = n - 1.
        assert scaled[0] == (order - 1) * 2 ** (order - 2)
        # d_{n-2} = sum_{i<j} D_ij^2 (Edelberg–Garey–Graham), so s_{n-2} = 2^(n-2) * that sum.
        assert scaled[-1] == 2 ** (order - 2) * sum(matrix[i][j] ** 2 for i, j in combinations(range(order), 2))


@pytest.mark.parametrize("order", range(3, 41))
def test_star_peak_is_floor_half(order):
    # Collins (1989), Theorem 1, as reported in arXiv:1507.02341.
    assert distpoly.peak_indices(distpoly.scaled_coefficients(distpoly.star_parents(order))) == [order // 2]


def test_conjectured_interval_exact_arithmetic():
    # ceil(n - n/sqrt(5)) compared with high-precision decimals.
    from decimal import ROUND_CEILING, Decimal, getcontext

    getcontext().prec = 60
    for n in range(1, 2000):
        expected = int((Decimal(n) - Decimal(n) / Decimal(5).sqrt()).to_integral_value(rounding=ROUND_CEILING))
        assert distpoly.conjectured_interval(n) == (n // 2, expected)


@pytest.mark.parametrize("order", range(3, 12))
def test_d1_formula_first_zagreb_index(order):
    # Lemma L2 of the investigation: d_1(T) = 2n^2 - 6 - sum_v deg(v)^2.
    for layout in distpoly.layouts(order):
        parents = distpoly.parents_from_layout(layout)
        degree = [0] * order
        for u, v in edges_of(parents):
            degree[u] += 1
            degree[v] += 1
        scaled = distpoly.scaled_coefficients(parents)
        assert Fraction(scaled[1], 2 ** (order - 2)) == 2 * order * order - 6 - sum(d * d for d in degree)


def test_refutation_of_star_minimality_at_order_20_by_both_methods():
    # Hypothesis A(i) at k = floor(n/2) - 1 fails for the double star S(9,9), n = 20:
    # rho_9(S(9,9)) < rho_9(S_20), i.e. q(S(9,9)) > q(S_20), while both stay below 1.
    n, m = 20, 10
    double_star = [-1, 0] + [0] * 9 + [1] * 9
    star = distpoly.star_parents(n)
    q = {}
    for name, parents in (("double", double_star), ("star", star)):
        scaled = distpoly.scaled_coefficients(parents)
        independent = independent_check.normalized_coefficients(n, edges_of(parents))
        assert [Fraction(value, 2 ** (n - 2)) for value in scaled] == independent
        q[name] = Fraction(scaled[m - 1], scaled[m])
    assert q["star"] < q["double"] < 1
    assert distpoly.peak_indices(distpoly.scaled_coefficients(double_star)) == [m]


@pytest.mark.parametrize("leaves", [[1], [4], [1, 1], [9, 9], [1, 1, 1], [5, 7, 9, 4], [3, 1, 2, 1, 6], [2, 1, 1, 1, 3, 1]])
def test_caterpillar_quotient_formula_matches_direct_computation(leaves):
    # Lemma L3: every coefficient, not only the critical ratio.
    import near_star_families

    assert near_star_families.sequences_proportional(leaves)


def test_double_star_closed_forms_and_peak():
    # Theorem T1 (notes/double-stars.md) on every double star of order 4 to 32, against the
    # direct determinant, and on a few of them against the independent Laplacian method.
    import double_stars

    assert double_stars.symbolic_4g() == double_stars.EXPECTED_4G
    for m in range(40):
        assert 24 * m**3 - 88 * m**2 + 98 * m - 30 == 2 * (2 * m - 1) * (2 * m - 3) * (3 * m - 5)
    for total in range(2, 31):
        for a in range(1, total // 2 + 1):
            b = total - a
            d = double_stars.double_star_coefficients(a, b)
            assert double_stars.matches_direct(double_stars.double_star_parents(a, b), d)
            assert double_stars.double_star_closed_form_holds(a, b, d)
            assert double_stars.middle_is_the_only_peak(d)
    for a, b in [(1, 1), (1, 2), (3, 5), (9, 9), (2, 13)]:
        parents = double_stars.double_star_parents(a, b)
        independent = independent_check.normalized_coefficients(len(parents), edges_of(parents))
        assert independent == [Fraction(value) for value in double_stars.double_star_coefficients(a, b)]
    for n in range(3, 33):
        d = double_stars.star_coefficients(n)
        assert double_stars.matches_direct(distpoly.star_parents(n), d)
        assert double_stars.star_closed_form_holds(n, d) and double_stars.middle_is_the_only_peak(d)


def test_spine3_closed_forms_and_peak():
    # Theorem T2 (notes/spine3.md): the caterpillars K(a,b,c) with a, b, c >= 1. The symbolic
    # derivation of Lemmas C1 and C2, the sign conditions of Step 3 for small m, and every
    # K(a,b,c) of order 6 to 17 against the direct determinant; a few against the
    # independent Laplacian method, which uses neither the determinant code nor Lemma L3.
    import spine3

    assert set(spine3.symbolic_differences()) == set(spine3.CASES)
    assert all(spine3.sign_conditions_hold(m) for m in range(3, 200))
    for total in range(3, 15):
        n, m = total + 3, (total + 3) // 2
        for a in range(1, total - 1):
            for c in range(a, total - a):
                b = total - a - c
                d = spine3.coefficients(a, b, c)
                assert spine3.matches_direct(a, b, c)
                assert spine3.closed_forms_hold(a, b, c, d)
                assert distpoly.peak_indices([d[k] for k in range(n - 1)]) == [m]
    for a, b, c in [(1, 1, 1), (1, 2, 1), (2, 1, 3), (4, 4, 4), (1, 9, 2)]:
        parents = spine3.parents(a, b, c)
        independent = independent_check.normalized_coefficients(len(parents), edges_of(parents))
        d = spine3.coefficients(a, b, c)
        assert independent == [Fraction(d[k]) for k in range(len(parents) - 1)]


def test_diameter4_caterpillars_without_central_leaf():
    # Theorem T3 (notes/diameter4-caterpillars.md): K(a,0,c) with a, c >= 1 and a + c >= 3.
    # The formula of Lemma C1 at b = 0 against the direct determinant, the identities of
    # Lemma C2 there, the sign conditions for small m, and the path on five vertices.
    import diameter4
    import spine3

    assert set(diameter4.symbolic_check()) == set(spine3.CASES)
    for m in range(3, 200):
        for case in spine3.CASES:
            k_star, h_star = diameter4.stated_at_centre_empty(case, m)
            assert k_star > 0 and h_star > 0
    for total in range(3, 21):
        n, m = total + 3, (total + 3) // 2
        for a in range(1, total // 2 + 1):
            c = total - a
            d = spine3.coefficients(a, 0, c)
            assert diameter4.matches_direct(a, c)
            assert spine3.closed_forms_hold(a, 0, c, d)
            assert distpoly.peak_indices([d[k] for k in range(n - 1)]) == [m]
    for a, c in [(1, 2), (2, 2), (1, 6), (4, 5)]:
        parents = diameter4.parents(a, c)
        independent = independent_check.normalized_coefficients(len(parents), edges_of(parents))
        d = spine3.coefficients(a, 0, c)
        assert independent == [Fraction(d[k]) for k in range(len(parents) - 1)]
    path5 = distpoly.path_parents(5)
    assert independent_check.normalized_coefficients(5, edges_of(path5)) == [4, 30, 70, 50]


def test_mixed_partial_certificate_on_small_spines():
    # Hypothesis V (notes/vertex-principle.md) for 2 to 4 spine vertices and small orders: the
    # interpolated closed form against the direct determinant (an empty inner class included),
    # and non-negative certificate coefficients for every pair of spine vertices.
    import mixed_partials

    for s in (2, 3, 4):
        alpha = mixed_partials.multiaffine_g(s)
        assert mixed_partials.matches_direct(alpha, [2] + [0] * (s - 2) + [3])
        assert mixed_partials.matches_direct(alpha, [1] * (s - 1) + [4])
        lows = [1] + [0] * (s - 2) + [1]
        for n in range(max(2 * s, s + 3), 40):
            beta = mixed_partials.difference(alpha, s, n, -1)
            for i, k in combinations(range(s), 2):
                assert mixed_partials.smallest_certificate_coefficient(beta, s, i, k, lows) >= 0


def test_top_coefficient_of_the_caterpillar_polynomials():
    # Observation of notes/vertex-principle.md, for 2 to 6 spine vertices: the product of all
    # leaf numbers occurs only in g_{s-1} and g_s, with coefficients s and s + 3.
    import mixed_partials

    for s in range(2, 7):
        full = frozenset(range(s))
        found = {j: polynomial[full] for j, polynomial in enumerate(mixed_partials.multiaffine_g(s)) if full in polynomial}
        assert found == {s - 1: s, s: s + 3}


def test_skeleton_expansion_and_property_gamma():
    # notes/skeleton-identity.md, for every tree with 2 to 5 vertices as skeleton: Proposition S2
    # (expansion over subsets) at enough rational points, Proposition S3 (top coefficient), and the
    # non-negative half-gamma expansion of r_A for every subset with at least two elements.
    import skeleton_structure

    for s in range(2, 6):
        for layout in distpoly.layouts(s):
            skeleton = distpoly.parents_from_layout(layout)
            dist = skeleton_structure.skeleton_distances(skeleton)
            alpha = skeleton_structure.multiaffine_g(dist)
            full = frozenset(range(s))
            assert {j: p[full] for j, p in enumerate(alpha) if full in p} == {s - 1: s, s: s + 3}
            assert skeleton_structure.half_gamma_expansion(alpha, s, tuple(range(s))) == ([s], [3])
            for size in range(s + 1):
                for subset in combinations(range(s), size):
                    for x in (Fraction(1), Fraction(2), Fraction(-3, 2), Fraction(5, 7)) + tuple(Fraction(v) for v in range(3, 2 * s + 2)):
                        left = skeleton_structure.subset_formula_value(dist, subset, x)
                        assert left == skeleton_structure.subset_coefficient_value(alpha, s, subset, x)
                    if size >= 2:
                        rho, sigma = skeleton_structure.half_gamma_expansion(alpha, s, subset)
                        assert min(rho + sigma) >= 0


def test_reduction_of_r_A_to_the_laplacian_block(monkeypatch, capsys):
    # notes/skeleton-locality.md, for every tree with 2 to 5 vertices and every subset: Propositions S6,
    # S7 (both forms), S8, S9 and the identity of S10 against the definition of r_A, and the comparison
    # of Corollary 6 of Collins's manuscript with the balanced double stars. The script returns 0 only
    # if no identity fails.
    import locality_check

    monkeypatch.setattr(sys, "argv", ["locality_check.py", "--max-skeleton", "5"])
    assert locality_check.main() == 0
    out = capsys.readouterr().out
    assert '"S10_min_a_minus_H": 1' in out
    assert '"printed_formula_matches": true' not in out


def test_pieces_of_the_laplacian_form():
    # notes/gamma-reduction.md, trees with 2 to 5 vertices: Lemma F and Corollary F' (weights of Phi_B and
    # of the positive part) and Property Gamma extended to subsets with one element. Exit code 0 only
    # if nothing fails.
    import subprocess

    script = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak" / "gamma_pieces.py"
    done = subprocess.run([sys.executable, str(script), "--max-skeleton", "5"], capture_output=True, text=True)
    assert done.returncode == 0, done.stdout[-2000:] + done.stderr[-2000:]
