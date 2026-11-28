"""Tests for experiments/CJ-0001-collins-shor-peak/amw_reduction_check.py (session 15)."""
import importlib.util
from fractions import Fraction as Fr
from pathlib import Path

import networkx as nx

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "amw_reduction_check", ROOT / "experiments" / "CJ-0001-collins-shor-peak" / "amw_reduction_check.py"
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def test_sign_in_q_sqrt5():
    assert mod.sign_q5(Fr(3), Fr(-1)) == 1      # 3 - sqrt5 > 0
    assert mod.sign_q5(Fr(2), Fr(-1)) == -1     # 2 - sqrt5 < 0
    assert mod.sign_q5(Fr(-11, 5), Fr(1)) == 1  # sqrt5 - 11/5 > 0
    assert mod.sign_q5(Fr(-9, 4), Fr(1)) == -1  # sqrt5 - 9/4 < 0
    assert mod.sign_q5(Fr(0), Fr(0)) == 0


def test_matching_numbers_and_avm():
    star = nx.star_graph(3)                      # K_{1,3}: m = [1, 3]
    assert mod.matching_numbers(star) == [1, 3]
    assert mod.avm([1, 3]) == Fr(3, 4)
    path = nx.path_graph(5)                      # P_5: m = [1, 4, 3]
    assert mod.matching_numbers(path) == [1, 4, 3]
    # the subdivision of K_{1,3} is the spider with three legs of length 2
    s = mod.subdivision(nx.convert_node_labels_to_integers(star))
    assert s.number_of_nodes() == 7 and nx.is_tree(s)


def test_small_parts_pass():
    assert mod.part_a(6)["failures"] == 0
    assert mod.part_b(9)["failures"] == 0
    assert mod.part_c(40)["failures"] == 0
    d = mod.part_d(60)
    assert d["failures"] == 0
    assert 9 in d["first_ceiling_case"] and d["first_open"][:4] == [3, 5, 7, 8]


def test_negative_control_bound_fails_for_small_paths():
    # the bound avm(P_N) > aN + b is false at N = 3 (where P_3 is the only tree),
    # so the test of part C is not vacuous
    from math import comb
    N = 3
    m = [comb(N - k, k) for k in range(N // 2 + 1)]
    A = mod.avm(m)
    assert mod.sign_q5(10 * A - 5 * N + 17, Fr(N - 7)) == -1
