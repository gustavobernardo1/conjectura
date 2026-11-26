"""Regression tests for `wiener_form.py` and `leaf_telescoping.py` (CJ-0001, session 9;
notes/wiener-form.md and notes/leaf-telescoping.md).

Values marked "by hand" can be recomputed on paper; the counts are regression values obtained by
running the scripts.
"""

from __future__ import annotations

import sys
from math import comb
from pathlib import Path

EXPERIMENT = Path(__file__).resolve().parents[1] / "experiments" / "CJ-0001-collins-shor-peak"
sys.path.insert(0, str(EXPERIMENT))

import leaf_telescoping as lt  # noqa: E402
import rooted_state as rs  # noqa: E402
import wiener_form as wf  # noqa: E402


def test_path_on_three_vertices_by_hand():
    # P_3: D = [[0,1,2],[1,0,1],[2,1,0]], det(2xI - D) = 8x^3 - 12x - 4, l = -det/2 = 2 + 6x - 4x^3.
    T = rs.WT(3, [(0, 1), (1, 2)], [0, 0, 0])
    assert lt.ell_laplacian(T) == [2, 6, 0, -4]
    # Wiener form: W = 4, t = (3, 2, 3), Phi = (1+x)(1+3x); the two edges have Pi = 1 + x.
    # 9 l = 4 (4 - 3x)(1 + 4x + 3x^2) + 2 (1 + x) = 18 + 54x - 36x^3.
    assert rs.ptrim(rs.pmul([4, -3], T.phi)) == [4, 13, 0, -9]


def test_star_closed_form_by_hand():
    # l_star = (1+x)^(n-2) [(n-1) + 4(n-2)x - 4x^2]; star with centre 0.
    for n in range(2, 8):
        T = rs.WT(n, [(0, v) for v in range(1, n)], [0] * n)
        closed = rs.pmul([comb(n - 2, i) for i in range(n - 1)], [n - 1, 4 * (n - 2), -4])
        assert lt.ell_laplacian(T) == rs.ptrim(closed)


def test_lambda_functional_by_hand():
    # lam(f) = [x^mu] f - [x^(mu-1)] f;  (1+x)^4 with mu = 2: 6 - 4.
    assert wf.lam([1, 4, 6, 4, 1], 2) == 2
    assert wf.lam([1, 4, 6, 4, 1], 1) == 3
    assert wf.lam([1], 3) == 0


def test_wiener_form_small_orders():
    rows = wf.run(8)
    assert [row["trees"] for row in rows] == [1, 1, 2, 3, 6, 11, 23]
    assert [row["pairs"] for row in rows] == [1, 3, 12, 30, 90, 231, 644]
    for row in rows:
        assert all(value == 0 for value in row["failures"].values()), row
    # regression values of the smallest main term
    assert [row["least_lam_of_main_term"] for row in rows][1:] == [9, 41, 125, 446, 1029, 3381]


def test_peak_inequality_from_distance_matrix():
    rows = wf.peak_only(9, 12)
    assert [row["trees"] for row in rows] == [47, 106, 235, 551]
    assert all(row["W6_failures"] == 0 for row in rows)


def test_leaf_recursion_and_star_minimality_small_orders():
    a = lt.part_A(7)
    assert [row["rooted"] for row in a["rows"]] == [1, 2, 3, 8, 15, 36, 77]
    for row in a["rows"]:
        assert all(value == 0 for value in row["failures"].values()), row
    assert a["first_failures"] == {}
    b = lt.part_B(11)
    assert [row["trees"] for row in b["rows"]] == [1, 2, 3, 6, 11, 23, 47, 106, 235]
    for row in b["rows"]:
        assert row["B1_star_formula"] and row["B2_failures"] == 0 and row["B3_failures"] == 0
        assert row["trees_with_l_equal_to_star"] == 1
    assert b["first_failures"] == {}
