"""Tests for experiments/CJ-0001-collins-shor-peak/path_formula_check.py (session 15)."""
import importlib.util
from fractions import Fraction as Fr
from math import comb
from pathlib import Path

import pytest

pytest.importorskip("flint")

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "path_formula_check", ROOT / "experiments" / "CJ-0001-collins-shor-peak" / "path_formula_check.py"
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def test_small_paths_pass():
    res = mod.main(10)
    assert res["failures"] == 0 and res["cases"] == 9


def test_interpolation_exact():
    # x^2 - 3x + 2 through 0, 1, 2
    assert mod.interp([0, 1, 2], [Fr(2), Fr(0), Fr(0)]) == [Fr(2), Fr(-3), Fr(1)]


def test_negative_control_wrong_formula_is_detected():
    # d_{n-k}(P_5) from the distance matrix differs from C(n+k-1,2k-1)(k-1)n/k with n/k replaced by 1
    n = 5
    D = [[abs(i - j) for j in range(n)] for i in range(n)]
    from flint import fmpz_mat
    cp = fmpz_mat(D).charpoly().coeffs()
    d = [abs(int(cp[j])) * 2 ** j // 2 ** (n - 2) for j in range(n - 1)]
    assert all(Fr(d[n - k]) == Fr(comb(n + k - 1, 2 * k - 1) * (k - 1) * n, k) for k in range(2, n + 1))
    assert any(Fr(d[n - k]) != comb(n + k - 1, 2 * k - 1) * (k - 1) for k in range(2, n + 1))
