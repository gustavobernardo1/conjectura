"""Regression tests for `even_order.py` (CJ-0001, session 10; notes/even-order.md).

Values marked "by hand" can be recomputed on paper; the counts are regression values obtained by
running the script.
"""

from __future__ import annotations

import sys
from math import comb
from pathlib import Path

import networkx as nx

EXPERIMENT = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"
sys.path.insert(0, str(EXPERIMENT))

import even_order as eo  # noqa: E402


def test_path_on_three_vertices_by_hand():
    # P_3: l = 2 + 6x - 4x^3, Phi = (1+x)(1+3x) = 1 + 4x + 3x^2.
    T = eo.Tree(nx.path_graph(3))
    assert T.ell() == [2, 6, 0, -4]
    assert T.pi(set()) == [1, 4, 3] == T.pi_dp(set())
    # Theta = (Phi - (1+x)^2)/x = 2 + 2x;  Omega = l + 4x(1+x)^2 - (1+4x)(2+2x) = 0 (P_3 is a star).
    theta = [2, 2]
    omega = eo.padd(eo.padd(T.ell(), [0, 4, 8, 4]), eo.pscale(-1, eo.pmul([1, 4], theta)))
    assert eo.ptrim(omega) == [0]


def test_path_on_four_vertices_by_hand():
    # P_4: Phi = 1 + 6x + 10x^2 + 4x^3; pendant edge removed: 1 + 3x + x^2; middle edge removed: (1+x)^2.
    T = eo.Tree(nx.path_graph(4))
    assert T.pi(set()) == [1, 6, 10, 4]
    assert T.pi({0, 1}) == [1, 3, 1] == T.pi_dp({0, 1})
    assert T.pi({1, 2}) == [1, 2, 1] == T.pi_dp({1, 2})


def test_lambda_and_half_gamma_by_hand():
    assert eo.lam([1, 4, 6, 4, 1], 2) == 2
    # 1 + 3x + x^2 = (1+x)^2 + x: expansion with centre 2.
    assert eo.half_gamma([1, 3, 1], 2) == [1, 1, 0]
    assert eo.in_cone([1, 3, 1], 2) and not eo.in_cone([1, 1, 1], 2)


def test_two_determinant_routines_agree_on_small_trees():
    for n in range(2, 8):
        for G in nx.nonisomorphic_trees(n):
            T = eo.Tree(G)
            assert T.pi(set()) == T.pi_dp(set())
            for u, v in T.G.edges():
                assert T.pi({u, v}) == T.pi_dp({u, v})


def test_parts_small_parameters():
    a = eo.part_a(6)
    assert (a["trees"], a["rooted_cases"], a["A1_failures"], a["A2_failures"]) == (13, 64, 0, 0)
    b = eo.part_b(8)
    assert (b["trees"], b["B1_failures"], b["B2_failures"], b["B3_failures"], b["omega_zero"]) == (46, 0, 0, 0, 6)
    c = eo.part_c(8, 20, 22)
    assert c["C1"]["6"]["rhs3_not_positive"] == 0 and c["C1"]["8"]["rhs3_not_positive"] == 0
    assert c["C2_all_agree"] and c["C2_first_n_with_rhs3_not_positive"] is None


def test_star_margin_formula_by_hand():
    # S30(d), equality for the star: d_m - d_{m-1} = (n-1)(3m-5)/(m+1) Cat_{m-1}, n = 2m.
    for m in range(2, 7):
        n = 2 * m
        ell = eo.Tree(nx.star_graph(n - 1)).ell()
        cat = comb(2 * m - 2, m - 1) // m
        assert (m + 1) * eo.lam(ell, m) == (n - 1) * (3 * m - 5) * cat
