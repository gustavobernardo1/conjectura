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
