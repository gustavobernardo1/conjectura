"""Three spine vertices: the mixed second partials of d_m - d_{m-1} as polynomials in m.

For the caterpillar K(a,b,c) and a fixed order n >= 6 (m = floor(n/2), N = n - 6),

    D_n(a,b,c) = sum_j g_j(a,b,c) [C(N, m - j) - C(N, m - 1 - j)]

with (a,b,c) free and n a parameter (notes/vertex-principle.md). Multiplied by
the positive factor sigma/c_0 (even order) or sigma/e_0 (odd order) of Lemma C2
of notes/spine3.md, it is a polynomial in m, a, b, c of degree at most 1 in each
of a, b, c. This script derives it symbolically from the g_j and checks:

1. on the slice b = n - 3 - a - c it equals the polynomial v K + R of Lemma C2
   (case "lower");
2. its three mixed partials equal the forms stated in the notes
   (function ``stated_mixed_partials``), each of the shape P0(m) + P1(m) y with
   y = b, c - 1 or a - 1;
3. P0 and P1 have non-negative coefficients as polynomials in t = m - 3, so
   they are non-negative for every m >= 3: Hypothesis V for three spine
   vertices, for every order n >= 6;
4. its values at the two kinds of vertex of the slice, (n-4, 0, 1) and
   (1, n-5, 1), equal the polynomials H* of notes/diameter4-caterpillars.md
   and H(m, 2) of notes/spine3.md, and have positive coefficients in t.

All arithmetic is exact (integer polynomials). The identities are computed, not
derived by hand.

Usage:
    python experiments/CJ-0001-collins-shor-peak/mixed_partials_s3.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from flint import fmpz_mpoly_ctx, fmpz_poly

sys.path.insert(0, str(Path(__file__).resolve().parent))

import diameter4  # noqa: E402
import spine3  # noqa: E402

LOWS = {"a": 1, "b": 0, "c": 1}
INDEX = {"a": 1, "b": 2, "c": 3}


def stated_mixed_partials(parity: str, m):
    """{(first, second): (P0, P1)} with d^2 D / d first d second = P0 + P1 * (third - lower bound of third)."""
    if parity == "even":
        top = 3 * m * (m - 1) * (m + 1)
        outer = 20 * m * (m + 1) * (2 * m - 5)
        inner = 3 * m * (m + 1) * (5 * m - 11)
    else:
        top = 12 * m * (m + 1) * (m + 2)
        outer = 4 * (m + 1) * (m + 2) * (23 * m - 36)
        inner = 4 * (m + 1) * (m + 2) * (13 * m - 15)
    return {("a", "c"): (outer, top), ("a", "b"): (inner, top), ("b", "c"): (inner, top)}


def coefficients_in_t(polynomial) -> list[int]:
    """Coefficients, in t = m - 3, of a polynomial in m alone."""
    by_degree: dict[int, int] = {}
    for exponents, coefficient in polynomial.to_dict().items():
        assert not any(exponents[1:])
        by_degree[exponents[0]] = int(coefficient)
    in_m = fmpz_poly([by_degree.get(i, 0) for i in range(max(by_degree, default=0) + 1)])
    return [int(value) for value in in_m(fmpz_poly([3, 1])).coeffs()]


def check() -> dict:
    _, g_abc = spine3.symbolic_g()
    ctx = fmpz_mpoly_ctx.get(("m", "a", "b", "c"), "lex")
    m, a, b, c = ctx.gens()
    zero = ctx.from_dict({})
    variables = {"a": a, "b": b, "c": c}
    g = [zero + sum(int(co) * a**da * b**db * c**dc for (da, db, dc, _), co in poly.to_dict().items()) for poly in g_abc]
    report = {}
    for parity, name in ((0, "even"), (1, "odd")):

        def scaled_binomial(i: int):
            i = abs(i) if parity == 0 else (i if i >= 0 else -1 - i)
            first = m - 2 if parity == 0 else m - 1
            value = zero + 1
            for step in range(4):
                value = value * ((m - 3 - step) if step < i else (first + step))
            return value

        offset = 3 if parity == 0 else 2
        difference = zero
        for j in range(7):
            difference = difference + g[j] * (scaled_binomial(offset - j) - scaled_binomial(offset - 1 - j))
        n = 2 * m + parity
        k, r, _, at_two, _, _ = spine3.stated(f"{name}-lower", m, a + c)
        assert difference.compose(m, a, n - 3 - a - c, c) == a * c * k + r, name

        entry = {}
        for (first, second), (p0, p1) in stated_mixed_partials(name, m).items():
            third = next(v for v in "abc" if v not in (first, second))
            mixed = zero
            for exponents, coefficient in difference.to_dict().items():
                if exponents[INDEX[first]] == 1 and exponents[INDEX[second]] == 1:
                    rest = list(exponents)
                    rest[INDEX[first]] = rest[INDEX[second]] = 0
                    mixed = mixed + ctx.from_dict({tuple(rest): int(coefficient)})
            assert mixed == p0 + p1 * (variables[third] - LOWS[third]), (name, first, second)
            in_t = (coefficients_in_t(p0), coefficients_in_t(p1))
            assert all(value >= 0 for part in in_t for value in part), (name, first, second)
            entry[f"d2D/d{first}d{second}"] = {"P0 in t = m - 3": in_t[0], "P1 in t = m - 3": in_t[1], "third variable": f"{third} - {LOWS[third]}"}

        _, h_star = diameter4.stated_at_centre_empty(f"{name}-lower", m)
        vertices = {"(n-4, 0, 1)": (n - 4, zero, zero + 1, h_star), "(1, n-5, 1)": (zero + 1, n - 5, zero + 1, at_two)}
        for label, (va, vb, vc, expected) in vertices.items():
            value = difference.compose(m, va + zero, vb + zero, vc + zero)
            assert value == expected, (name, label)
            in_t = coefficients_in_t(value)
            assert all(coefficient > 0 for coefficient in in_t), (name, label)
            entry[f"D at the vertex {label}, in t = m - 3"] = in_t
        report[name] = entry
    return report


def main() -> int:
    for name, entry in check().items():
        for key, value in entry.items():
            print(f"{name}: {key}: {value}")
    print("three spine vertices: the mixed partials have the stated forms, non-negative for every m >= 3; both vertex values are positive")
    return 0


if __name__ == "__main__":
    sys.exit(main())
