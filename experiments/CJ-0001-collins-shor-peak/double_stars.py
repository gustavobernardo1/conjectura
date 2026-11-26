"""Double stars: closed forms for the normalized coefficients around the middle index.

The double star S(a,b) has two adjacent centres carrying a and b pendant leaves
(a, b >= 1, order n = a + b + 2). By the caterpillar formula (Lemma L3, spine
length 2) its normalized coefficients are

    d_k = sum_{j=0}^{4} g_j C(n - 4, k - j),      0 <= k <= n - 2,

with, for s = a + b and t = a b,

    g_0 = s + 1,  g_1 = 2t + 6s + 2,  g_2 = 5t + 9s - 3,  g_3 = 4s - 8,  g_4 = -4.

With m = floor(n/2) the claims checked here are (notes/double-stars.md):

    n = 2m:     (d_m - d_{m-1}) (m-1) m (m+1) = C(2m-4, m-2) (3t m(m+1) + 24m^3 - 88m^2 + 98m - 30)
    n = 2m+1:   (d_m - d_{m-1}) m (m+1) (m+2) = C(2m-3, m-1) (10t (m+1)(m+2) + 16m (2m-1)(2m+1))

    d_{m-1} < d_m,  and  d_{m+1} < d_m  whenever m + 1 <= n - 2,

so that m is the only maximizing index. The same is checked for stars, with
d_k = (n-1) C(n-2, k) + 4(n-2) C(n-2, k-1) - 4 C(n-2, k-2).

What is computed:

1. the polynomials g_j, symbolically, from the 4 x 4 quotient determinant;
2. for every double star with a + b <= --max-sum: the closed forms, the two
   inequalities, the peak, and agreement of the whole sequence with the numeric
   quotient-matrix computation of near_star_families.py;
3. for every double star with a + b <= --direct-max-sum, and a few larger ones:
   agreement of the whole sequence with the direct n x n determinant;
4. the same for stars.

All arithmetic is exact. A finite check is not a proof; the proof is in the notes.

Usage:
    python experiments/CJ-0001-collins-shor-peak/double_stars.py \
        --out experiments/CJ-0001-collins-shor-peak/results/double-stars.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from itertools import permutations
from math import comb
from pathlib import Path

from flint import fmpz_mpoly_ctx

sys.path.insert(0, str(Path(__file__).resolve().parent))

import distpoly  # noqa: E402
import near_star_families  # noqa: E402

# 4 g_j as polynomials in (a, b): {(degree in a, degree in b): coefficient}.
EXPECTED_4G = [
    {(1, 0): 4, (0, 1): 4, (0, 0): 4},
    {(1, 1): 8, (1, 0): 24, (0, 1): 24, (0, 0): 8},
    {(1, 1): 20, (1, 0): 36, (0, 1): 36, (0, 0): -12},
    {(1, 0): 16, (0, 1): 16, (0, 0): -32},
    {(0, 0): -16},
]


def symbolic_4g() -> list[dict[tuple[int, int], int]]:
    """Coefficients of -det(2xI - Q) in x, as polynomials in (a, b), for the quotient matrix Q of S(a,b)."""
    ctx = fmpz_mpoly_ctx.get(("a", "b", "x"), "lex")
    a, b, x = ctx.gens()

    def const(value: int):
        return ctx.from_dict({(0, 0, 0): value}) if value else ctx.from_dict({})

    # Lemma L3 with spine length 2: rows and columns are (centre 1, centre 2, leaves of 1, leaves of 2).
    quotient = [
        [const(0), const(1), a, 2 * b],
        [const(1), const(0), 2 * a, b],
        [const(1), const(2), 2 * a - 2, 3 * b],
        [const(2), const(1), 3 * a, 2 * b - 2],
    ]
    matrix = [[(2 * x if i == j else const(0)) - quotient[i][j] for j in range(4)] for i in range(4)]
    determinant = const(0)
    for permutation in permutations(range(4)):
        inversions = sum(1 for i in range(4) for j in range(i + 1, 4) if permutation[i] > permutation[j])
        term = const(-1 if inversions % 2 else 1)
        for row in range(4):
            term = term * matrix[row][permutation[row]]
        determinant = determinant + term
    result: list[dict[tuple[int, int], int]] = [{} for _ in range(5)]
    for (degree_a, degree_b, degree_x), coefficient in determinant.to_dict().items():
        result[degree_x][(degree_a, degree_b)] = -int(coefficient)
    return result


def double_star_parents(a: int, b: int) -> list[int]:
    return [-1, 0] + [0] * a + [1] * b


def double_star_coefficients(a: int, b: int) -> list[int]:
    """[d_0, ..., d_{n-2}] of S(a,b) from the closed formula (exact integers)."""
    s, t = a + b, a * b
    g = [s + 1, 2 * t + 6 * s + 2, 5 * t + 9 * s - 3, 4 * s - 8, -4]
    free = s - 2  # n - 4
    return [sum(g[j] * comb(free, k - j) for j in range(5) if 0 <= k - j <= free) for k in range(s + 1)]


def star_coefficients(n: int) -> list[int]:
    """[d_0, ..., d_{n-2}] of the star of order n from the closed formula (exact integers)."""
    h = [n - 1, 4 * (n - 2), -4]
    return [sum(h[j] * comb(n - 2, k - j) for j in range(3) if 0 <= k - j <= n - 2) for k in range(n - 1)]


def double_star_closed_form_holds(a: int, b: int, d: list[int]) -> bool:
    n, t = a + b + 2, a * b
    m = n // 2
    gap = d[m] - d[m - 1]
    if n % 2 == 0:
        return gap * (m - 1) * m * (m + 1) == comb(2 * m - 4, m - 2) * (3 * t * m * (m + 1) + 24 * m**3 - 88 * m**2 + 98 * m - 30)
    return gap * m * (m + 1) * (m + 2) == comb(2 * m - 3, m - 1) * (10 * t * (m + 1) * (m + 2) + 16 * m * (2 * m - 1) * (2 * m + 1))


def star_closed_form_holds(n: int, d: list[int]) -> bool:
    m = n // 2
    gap = d[m] - d[m - 1]
    if n % 2 == 0:
        return gap * m * (m + 1) == comb(2 * m - 2, m - 1) * (2 * m - 1) * (3 * m - 5)
    return gap * (m + 1) * (m + 2) == comb(2 * m - 1, m) * 8 * m * (2 * m + 1)


def middle_is_the_only_peak(d: list[int]) -> bool:
    """d_{m-1} < d_m, d_{m+1} < d_m when that index exists, and the maximum is attained at m only."""
    n = len(d) + 1
    m = n // 2
    after = m + 1 > n - 2 or d[m + 1] < d[m]
    low, high = distpoly.conjectured_interval(n)
    return d[m - 1] < d[m] and after and distpoly.peak_indices(d) == [m] and low <= m <= high


def matches_direct(parents: list[int], d: list[int]) -> bool:
    n = len(parents)
    return distpoly.scaled_coefficients(parents) == [value << (n - 2) for value in d]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--max-sum", type=int, default=200, help="check every double star with a + b up to this value")
    parser.add_argument("--direct-max-sum", type=int, default=40, help="compare with the n x n determinant up to this value")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    report: dict = {
        "experiment": "CJ-0001 double stars: closed forms around the middle index",
        "arithmetic": "exact integers and rationals",
        "run": distpoly.run_metadata(),
    }

    symbolic = symbolic_4g()
    assert symbolic == EXPECTED_4G, symbolic
    report["four_times_g_j_as_polynomials_in_a_b"] = [
        {f"a^{i} b^{j}": value for (i, j), value in sorted(polynomial.items())} for polynomial in symbolic
    ]
    print("symbolic quotient determinant agrees with the stated polynomials g_0..g_4")

    checked = direct = 0
    smallest_margin = None
    for total in range(2, args.max_sum + 1):
        for a in range(1, total // 2 + 1):
            b = total - a
            n = total + 2
            d = double_star_coefficients(a, b)
            assert all(value > 0 for value in d), (a, b)
            assert double_star_closed_form_holds(a, b, d), (a, b)
            assert middle_is_the_only_peak(d), (a, b)
            numeric = near_star_families.caterpillar_coefficients([a, b], list(range(n - 1)))
            assert all(numeric[k] * d[0] == numeric[0] * d[k] for k in range(n - 1)), (a, b)
            if total <= args.direct_max_sum:
                assert matches_direct(double_star_parents(a, b), d), (a, b)
                direct += 1
            m = n // 2
            margin = (d[m] - d[m - 1], d[m])
            if smallest_margin is None or margin[0] * smallest_margin[1][1] < smallest_margin[1][0] * margin[1]:
                smallest_margin = ((a, b), margin)
            checked += 1
    larger = [(60, 60), (1, 150), (37, 90), (100, 101)]
    for a, b in larger:
        assert matches_direct(double_star_parents(a, b), double_star_coefficients(a, b)), (a, b)
    (a, b), (gap, top) = smallest_margin
    report["double_stars"] = {
        "range": f"1 <= a <= b, a + b <= {args.max_sum} (orders 4 to {args.max_sum + 2})",
        "trees_checked": checked,
        "closed_form_failures": 0,
        "inequality_failures": 0,
        "compared_with_numeric_quotient_matrix": checked,
        "compared_with_direct_determinant": direct + len(larger),
        "direct_range": f"a + b <= {args.direct_max_sum}, and {larger}",
        "smallest_relative_margin": {"a": a, "b": b, "one_minus_q": f"{gap}/{top}", "decimal": gap / top},
    }
    print(f"double stars: {checked} trees, closed forms and inequalities hold; {direct + len(larger)} compared with the direct determinant")

    stars = direct_stars = 0
    for n in range(3, args.max_sum + 3):
        d = star_coefficients(n)
        assert all(value > 0 for value in d), n
        assert star_closed_form_holds(n, d), n
        assert middle_is_the_only_peak(d), n
        if n <= args.direct_max_sum + 2:
            assert matches_direct(distpoly.star_parents(n), d), n
            direct_stars += 1
        stars += 1
    report["stars"] = {
        "range": f"orders 3 to {args.max_sum + 2}",
        "trees_checked": stars,
        "closed_form_failures": 0,
        "inequality_failures": 0,
        "compared_with_direct_determinant": direct_stars,
    }
    print(f"stars: {stars} trees, closed forms and inequalities hold; {direct_stars} compared with the direct determinant")

    report["seconds"] = round(time.perf_counter() - started, 1)
    if args.out:
        args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
