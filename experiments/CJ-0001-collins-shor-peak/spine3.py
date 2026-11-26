"""The caterpillars K(a,b,c) with a, b, c >= 1: closed forms around the middle index.

The caterpillar K(a,b,c) has a spine v1 - v2 - v3 carrying a, b, c >= 1 pendant
leaves (order n = a + b + c + 3 >= 6). By the caterpillar formula (Lemma L3,
spine length 3) its normalized coefficients are

    d_k = sum_{j=0}^{6} g_j C(n - 6, k - j),      0 <= k <= n - 2,

with g_0, ..., g_6 polynomials in (a, b, c) (function ``g_values``). With
m = floor(n/2), u = a + c and v = a c, the notes (notes/spine3.md) reduce the
two differences d_m - d_{m-1} and d_m - d_{m+1}, for each parity of n, to

    scale * difference = binomial * (v K(m,u) + R(m,u)),

and prove positivity from: K > 0 on the domain; v >= u - 1; H(m,u) = (u-1) K + R
is concave in u; H is positive at both ends of the range of u.

What is computed:

1. the polynomials g_j, symbolically, from the 6 x 6 quotient determinant;
2. the four polynomials v K + R, symbolically, from the g_j and the binomial
   recurrences, and their agreement with the forms stated in the notes
   (K, R, H, the leading coefficient of H in u, and H at both endpoints);
3. for every m up to --max-m: the sign conditions the proof uses (a finite
   check of inequalities that the notes prove for all m >= 3);
4. for every caterpillar with a + b + c <= --max-sum (a <= c): the four closed
   forms as integer identities, and d_{m-1} < d_m > d_{m+1};
5. for a + b + c <= --sequence-max-sum: positivity of the whole sequence, the
   location of every maximizing index, and proportionality of the whole
   sequence to the numeric quotient-matrix computation of near_star_families.py;
6. for a + b + c <= --direct-max-sum, and a few larger ones: agreement of the
   whole sequence with the direct n x n determinant.

All arithmetic is exact. A finite check is not a proof; the proof is in the notes.

Usage:
    python experiments/CJ-0001-collins-shor-peak/spine3.py \
        --out experiments/CJ-0001-collins-shor-peak/results/spine3.json
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

CASES = ("even-lower", "even-upper", "odd-lower", "odd-upper")


def g_values(a: int, b: int, c: int) -> list[int]:
    """g_0, ..., g_6 of K(a,b,c) as stated in the notes (Lemma C1)."""
    return [
        a + b + c + 2,
        2 * (a * b + a * c + b * c) + 10 * a + 8 * b + 10 * c + 12,
        3 * a * b * c + 9 * a * b + 14 * a * c + 9 * b * c + 31 * a + 22 * b + 31 * c + 24,
        6 * a * b * c + 12 * a * b + 24 * a * c + 12 * b * c + 40 * a + 28 * b + 40 * c + 16,
        5 * a * b + 12 * a * c + 5 * b * c + 22 * a + 17 * b + 22 * c - 6,
        4 * (a + b + c) - 12,
        -4,
    ]


def coefficients(a: int, b: int, c: int, indices=None) -> dict[int, int]:
    """d_k of K(a,b,c) from the closed formula (exact integers), for the given indices (default: all)."""
    n = a + b + c + 3
    free = n - 6
    g = g_values(a, b, c)
    if indices is None:
        indices = range(n - 1)
    return {k: sum(g[j] * comb(free, k - j) for j in range(7) if 0 <= k - j <= free) for k in indices}


def parents(a: int, b: int, c: int) -> list[int]:
    return near_star_families.caterpillar_parents([a, b, c])


# ------------------------------------------------------------ stated closed forms --


def stated(case: str, m, u):
    """(K, R, leading coefficient of H in u, H at u = 2, H at the largest u, largest u), as in the notes.

    Works for integers and for polynomials alike.
    """
    if case == "even-lower":
        k = m * (m + 1) * (6 * m**2 + 25 * m - 91 - 3 * (m - 1) * u)
        r = (24 * m**4 * u + 96 * m**4 - 12 * m**3 * u**2 - 60 * m**3 * u - 592 * m**3 + 18 * m**2 * u**2
             - 24 * m**2 * u + 1272 * m**2 + 30 * m * u**2 + 60 * m * u - 1100 * m + 300)
        lead = -3 * m * (m + 1) * (5 * m - 11)
        low = 15 * (m - 1) * (2 * m - 5) * (5 * m**2 - 7 * m + 4)
        high = 5 * (2 * m - 5) * (23 * m**3 - 52 * m**2 + 9 * m - 12)
        top = 2 * m - 4
    elif case == "even-upper":
        k = (m + 1) * (30 * m**3 - 47 * m**2 - 109 * m + 120 - 3 * m * (5 * m - 11) * u)
        r = (88 * m**4 * u + 224 * m**4 - 44 * m**3 * u**2 - 316 * m**3 * u - 976 * m**3 + 114 * m**2 * u**2
             + 152 * m**2 * u + 1144 * m**2 + 38 * m * u**2 + 316 * m * u - 236 * m - 120 * u**2 - 240 * u - 60)
        lead = -(m + 1) * (59 * m**2 - 191 * m + 120)
        low = (2 * m - 5) * (215 * m**3 - 378 * m**2 - 53 * m + 180)
        high = (2 * m - 5) * (279 * m**3 - 554 * m**2 - 149 * m + 324)
        top = 2 * m - 4
    elif case == "odd-lower":
        k = 4 * (m + 1) * (m + 2) * (6 * m**2 + 17 * m - 36 - 3 * m * u)
        r = (80 * m**4 * u + 256 * m**4 - 40 * m**3 * u**2 + 80 * m**3 * u - 384 * m**3 - 60 * m**2 * u**2
             - 260 * m**2 * u - 64 * m**2 + 100 * m * u**2 - 140 * m * u + 96 * m + 120 * u**2 + 120 * u)
        lead = -4 * (m + 1) * (m + 2) * (13 * m - 15)
        low = 4 * (110 * m**4 - 67 * m**3 - 197 * m**2 - 32 * m + 108)
        high = 8 * (78 * m**4 - 58 * m**3 - 243 * m**2 + 67 * m + 234)
        top = 2 * m - 3
    elif case == "odd-upper":
        k = 6 * (m + 1) * (m + 2) * (2 * m**2 - 4 - m * u)
        r = (32 * m**4 * u + 64 * m**4 - 16 * m**3 * u**2 + 32 * m**3 * u + 128 * m**3 - 24 * m**2 * u**2
             - 104 * m**2 * u - 208 * m**2 + 40 * m * u**2 - 56 * m * u - 320 * m + 48 * u**2 + 48 * u + 192)
        lead = -2 * (m + 1) * (m + 2) * (11 * m - 12)
        low = 4 * (m + 2) * (35 * m**3 - 32 * m**2 - 73 * m + 54)
        high = 4 * (m + 2) * (41 * m**3 - 53 * m**2 - 70 * m + 84)
        top = 2 * m - 3
    else:
        raise ValueError(case)
    return k, r, lead, low, high, top


def closed_forms_hold(a: int, b: int, c: int, d: dict[int, int]) -> bool:
    """The two identities of the notes for the parity of n, as identities between integers."""
    n = a + b + c + 3
    m, u, v = n // 2, a + c, a * c
    if n % 2 == 0:
        scale, binomial, prefix = (m - 2) * (m - 1) * m * (m + 1), comb(2 * m - 6, m - 3), "even"
    else:
        scale, binomial, prefix = (m - 1) * m * (m + 1) * (m + 2), comb(2 * m - 5, m - 2), "odd"
    for suffix, other in (("lower", m - 1), ("upper", m + 1)):
        k, r, *_ = stated(f"{prefix}-{suffix}", m, u)
        if scale * (d[m] - d[other]) != binomial * (v * k + r):
            return False
    return True


# ---------------------------------------------------------------- symbolic part --


def symbolic_g():
    """Coefficients of -det(2xI - Q)/16 in x, for the 6 x 6 quotient matrix Q of K(a,b,c) (Lemma L3)."""
    ctx = fmpz_mpoly_ctx.get(("a", "b", "c", "x"), "lex")
    a, b, c, x = ctx.gens()
    zero = ctx.from_dict({})
    leaves = [a, b, c]
    quotient = [[zero] * 6 for _ in range(6)]
    for i in range(3):
        for j in range(3):
            gap = abs(i - j)
            quotient[i][j] = zero + gap
            quotient[i][3 + j] = (gap + 1) * leaves[j]
            quotient[3 + i][j] = zero + (gap + 1)
            quotient[3 + i][3 + j] = (gap + 2) * leaves[j] if i != j else 2 * leaves[i] - 2
    matrix = [[(2 * x if i == j else zero) - quotient[i][j] for j in range(6)] for i in range(6)]
    determinant = zero
    for permutation in permutations(range(6)):
        inversions = sum(1 for i in range(6) for j in range(i + 1, 6) if permutation[i] > permutation[j])
        term = zero + (-1 if inversions % 2 else 1)
        for row in range(6):
            term = term * matrix[row][permutation[row]]
        determinant = determinant + term
    g = [zero] * 7
    for (da, db, dc, dx), coefficient in determinant.to_dict().items():
        assert int(coefficient) % 16 == 0
        g[dx] = g[dx] + ctx.from_dict({(da, db, dc, 0): -int(coefficient) // 16})
    assert g == [zero + value for value in g_values(a, b, c)], "the g_j of the notes differ from the determinant"
    return ctx, g


def symbolic_differences() -> dict[str, str]:
    """Derive the four polynomials v K + R from the g_j and compare them with the stated forms.

    Even n = 2m: N = 2m - 6 and c_i = C(N, m - 3 + i) = c_{-i}, with
    (m-2) c_1 = (m-3) c_0, (m-1) c_2 = (m-4) c_1, m c_3 = (m-5) c_2, (m+1) c_4 = (m-6) c_3.
    Odd n = 2m + 1: N = 2m - 5 and e_i = C(N, m - 2 + i) = e_{-1-i}, with
    (m-1) e_1 = (m-3) e_0, m e_2 = (m-4) e_1, (m+1) e_3 = (m-5) e_2, (m+2) e_4 = (m-6) e_3.
    """
    _, g_abc = symbolic_g()
    ctx = fmpz_mpoly_ctx.get(("m", "a", "c", "u", "v"), "lex")
    m, a, c, u, v = ctx.gens()
    zero = ctx.from_dict({})
    report = {}
    for parity, prefix in ((0, "even"), (1, "odd")):
        n = 2 * m + parity
        b = n - 3 - a - c
        g = [zero + sum(int(co) * a**da * b**db * c**dc for (da, db, dc, _), co in poly.to_dict().items()) for poly in g_abc]

        def scaled_binomial(i: int):
            """c_i (even) or e_i (odd), multiplied by the scale and divided by c_0 or e_0."""
            i = abs(i) if parity == 0 else (i if i >= 0 else -1 - i)
            first = m - 2 if parity == 0 else m - 1  # the four denominators are first, ..., first + 3
            value = zero + 1
            for step in range(4):
                value = value * ((m - 3 - step) if step < i else (first + step))
            return value

        offset = 3 if parity == 0 else 2  # C(N, m - j) is c_{3-j} or e_{2-j}
        for suffix, shift in (("lower", -1), ("upper", 1)):
            case = f"{prefix}-{suffix}"
            derived = zero
            for j in range(7):
                derived = derived + g[j] * (scaled_binomial(offset - j) - scaled_binomial(offset + shift - j))
            k, r, lead, low, high, top = stated(case, m, u)
            expected = (v * k + r).compose(m, a, c, a + c, a * c)
            assert derived == expected, f"{case}: the stated form differs from the derived one"
            # H(m, u) = (u - 1) K + R: degree 2 in u with the stated leading coefficient and endpoint values.
            h = (u - 1) * k + r
            by_degree = {}
            for (dm, da, dc, du, dv), co in h.to_dict().items():
                assert da == dc == dv == 0
                by_degree[du] = by_degree.get(du, zero) + ctx.from_dict({(dm, 0, 0, 0, 0): int(co)})
            assert set(by_degree) <= {0, 1, 2} and by_degree[2] == lead, case
            assert h.compose(m, a, c, zero + 2, v) == low, case
            assert h.compose(m, a, c, top, v) == high, case
            report[case] = "derived from the g_j; equals v K + R as stated; H has the stated leading coefficient and endpoint values"
    return report


def sign_conditions_hold(m: int) -> bool:
    """The inequalities the proof uses at this m: K > 0 for every admissible u, H concave, H > 0 at both ends."""
    for case in CASES:
        _, _, lead, low, high, top = stated(case, m, 0)
        if not (lead < 0 and low > 0 and high > 0 and top >= 2):
            return False
        if any(stated(case, m, u)[0] <= 0 for u in range(2, top + 1)):
            return False
    return True


def matches_direct(a: int, b: int, c: int) -> bool:
    n = a + b + c + 3
    d = coefficients(a, b, c)
    return distpoly.scaled_coefficients(parents(a, b, c)) == [d[k] << (n - 2) for k in range(n - 1)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--max-sum", type=int, default=300, help="check the closed forms for a + b + c up to this value")
    parser.add_argument("--sequence-max-sum", type=int, default=60, help="examine the whole sequence up to this value")
    parser.add_argument("--direct-max-sum", type=int, default=20, help="compare with the n x n determinant up to this value")
    parser.add_argument("--max-m", type=int, default=2000, help="check the sign conditions of the proof for 3 <= m <= this value")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    report: dict = {
        "experiment": "CJ-0001 caterpillars with spine length 3: closed forms around the middle index",
        "arithmetic": "exact integers and rationals",
        "run": distpoly.run_metadata(),
    }

    report["symbolic"] = symbolic_differences()
    print("symbolic: the g_j and the four polynomials v K + R agree with the forms stated in the notes")

    assert all(sign_conditions_hold(m) for m in range(3, args.max_m + 1))
    report["sign_conditions"] = {
        "range": f"3 <= m <= {args.max_m}",
        "checked": "for each of the four cases: K > 0 for every integer u in [2, largest u]; leading coefficient of H negative; H > 0 at u = 2 and at the largest u",
        "failures": 0,
    }
    print(f"sign conditions of the proof hold for 3 <= m <= {args.max_m}")

    checked = sequences = direct = 0
    smallest_margin = None
    for total in range(3, args.max_sum + 1):
        n = total + 3
        m = n // 2
        low, high = distpoly.conjectured_interval(n)
        for a in range(1, total - 1):
            for c in range(a, total - a):
                b = total - a - c
                d = coefficients(a, b, c, [m - 1, m, m + 1])
                assert closed_forms_hold(a, b, c, d), (a, b, c)
                assert d[m - 1] < d[m] > d[m + 1] and low <= m <= high, (a, b, c)
                margin = (d[m] - d[m - 1], d[m])
                if n % 2 == 0 and (smallest_margin is None or margin[0] * smallest_margin[1][1] < smallest_margin[1][0] * margin[1]):
                    smallest_margin = ((a, b, c), margin)
                if total <= args.sequence_max_sum:
                    full = coefficients(a, b, c)
                    sequence = [full[k] for k in range(n - 1)]
                    assert all(value > 0 for value in sequence), (a, b, c)
                    assert distpoly.peak_indices(sequence) == [m], (a, b, c)
                    numeric = near_star_families.caterpillar_coefficients([a, b, c], list(range(n - 1)))
                    assert all(numeric[k] * sequence[0] == numeric[0] * sequence[k] for k in range(n - 1)), (a, b, c)
                    sequences += 1
                if total <= args.direct_max_sum:
                    assert matches_direct(a, b, c), (a, b, c)
                    direct += 1
                checked += 1
    larger = [(1, 1, 1), (20, 20, 20), (1, 58, 1), (30, 1, 29), (7, 3, 50), (2, 40, 19)]
    for a, b, c in larger:
        assert matches_direct(a, b, c), (a, b, c)
    (a, b, c), (gap, top) = smallest_margin
    report["caterpillars"] = {
        "range": f"1 <= a <= c, b >= 1, a + b + c <= {args.max_sum} (orders 6 to {args.max_sum + 3})",
        "trees_checked": checked,
        "closed_form_failures": 0,
        "inequality_failures": 0,
        "whole_sequence_examined": sequences,
        "whole_sequence_range": f"a + b + c <= {args.sequence_max_sum}: positive, maximum at floor(n/2) only, proportional to the numeric quotient-matrix computation",
        "compared_with_direct_determinant": direct + len(larger),
        "direct_range": f"a + b + c <= {args.direct_max_sum}, and {larger}",
        "smallest_relative_margin_even_order": {"a": a, "b": b, "c": c, "one_minus_q": f"{gap}/{top}", "decimal": gap / top},
    }
    print(f"caterpillars: {checked} trees, closed forms and inequalities hold; {sequences} whole sequences; {direct + len(larger)} compared with the direct determinant")

    report["seconds"] = round(time.perf_counter() - started, 1)
    if args.out:
        args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
