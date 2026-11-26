"""Caterpillars with s spine vertices: are the mixed second partials of d_m - d_{m-1} non-negative?

Exploration for Hypothesis V of notes/vertex-principle.md. A caterpillar has a
spine v_1 ... v_s and c_i pendant leaves at v_i, with c_1, c_s >= 1 and
c_i >= 0 inside (order n = s + sum c_i). For n >= 2s,

    d_k = sum_{j=0}^{2s} g_j(c) C(n - 2s, k - j),

where the g_j are the coefficients of -det(2xI - Q)/4^(s-1) for the 2s x 2s
quotient matrix Q of Lemma L3; they are polynomials in c of degree at most 1
in each c_i. For a fixed order n and m = floor(n/2),

    D_n(c) = sum_j g_j(c) [C(n - 2s, m - j) - C(n - 2s, m - 1 - j)]

equals d_m - d_{m-1} on the slice sum c_i = n - s and is multi-affine in c.
If every mixed partial d^2 D_n / dc_i dc_k is >= 0 on the domain, D_n is
concave along every direction e_i - e_k and its minimum over the slice is
attained at a point with a single spine vertex above its lower bound
(Lemma L4 of the notes).

What is computed, for each s and each order n in the range:

1. the g_j as multi-affine polynomials, by exact interpolation on {0,1}^s of
   the integer characteristic polynomial of Q; validated against the direct
   n x n determinant on every caterpillar with leaf numbers in a small box
   (zeros allowed inside), which also tests the formula when a class is empty;
2. a certificate for each pair i < k: with y = c - lower bounds, every
   coefficient of d^2 D_n / dc_i dc_k as a polynomial in the remaining y is
   >= 0. This is sufficient, not necessary, for non-negativity on the domain,
   and it ignores the constraint on the sum;
3. the value of D_n at each vertex of the slice, and which vertex minimizes it;
4. the same for the upper difference d_m - d_{m+1} (reported separately: the
   peak of a caterpillar with a long spine need not be at m).

All arithmetic is exact. This is evidence for a hypothesis, not a proof.

Usage:
    python experiments/CJ-0001-collins-shor-peak/mixed_partials.py --max-spine 6 --max-order 200 \
        --out experiments/CJ-0001-collins-shor-peak/results/mixed-partials.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from itertools import combinations, product
from math import comb, prod
from pathlib import Path

from flint import fmpz_mat

sys.path.insert(0, str(Path(__file__).resolve().parent))

import distpoly  # noqa: E402
import near_star_families  # noqa: E402


def g_at(leaves: list[int]) -> list[int]:
    """Coefficients of -det(2xI - Q)/4^(s-1) at integer leaf numbers (the formula of Q, zeros included)."""
    s = len(leaves)
    quotient = [[0] * (2 * s) for _ in range(2 * s)]
    for i in range(s):
        for j in range(s):
            gap = abs(i - j)
            quotient[i][j] = gap
            quotient[i][s + j] = (gap + 1) * leaves[j]
            quotient[s + i][j] = gap + 1
            quotient[s + i][s + j] = (gap + 2) * leaves[j] if i != j else 2 * (leaves[i] - 1)
    charpoly = fmpz_mat(quotient).charpoly()
    values = [-(int(charpoly[j]) << j) for j in range(2 * s + 1)]
    assert all(value % 4 ** (s - 1) == 0 for value in values)
    return [value // 4 ** (s - 1) for value in values]


def multiaffine_g(s: int) -> list[dict[frozenset, int]]:
    """alpha[j][S] with g_j(c) = sum_S alpha[j][S] prod_{i in S} c_i (Moebius inversion on {0,1}^s)."""
    at = {bits: g_at(list(bits)) for bits in product((0, 1), repeat=s)}
    alpha: list[dict[frozenset, int]] = [{} for _ in range(2 * s + 1)]
    for bits in product((0, 1), repeat=s):
        support = [i for i in range(s) if bits[i]]
        for j in range(2 * s + 1):
            total = 0
            for size in range(len(support) + 1):
                for subset in combinations(support, size):
                    point = tuple(1 if i in subset else 0 for i in range(s))
                    total += (-1) ** (len(support) - size) * at[point][j]
            if total:
                alpha[j][frozenset(support)] = total
    return alpha


def evaluate(polynomial: dict[frozenset, int], c: list[int]) -> int:
    return sum(coefficient * prod(c[i] for i in subset) for subset, coefficient in polynomial.items())


def closed_form(alpha, leaves: list[int]) -> list[int]:
    s = len(leaves)
    n = s + sum(leaves)
    free = n - 2 * s
    g = [evaluate(alpha[j], leaves) for j in range(2 * s + 1)]
    return [sum(g[j] * comb(free, k - j) for j in range(2 * s + 1) if 0 <= k - j <= free) for k in range(n - 1)]


def matches_direct(alpha, leaves: list[int]) -> bool:
    n = len(leaves) + sum(leaves)
    direct = distpoly.scaled_coefficients(near_star_families.caterpillar_parents(leaves))
    return direct == [value << (n - 2) for value in closed_form(alpha, leaves)]


def difference(alpha, s: int, n: int, other_shift: int) -> dict[frozenset, int]:
    """Multi-affine coefficients of d_m - d_{m + other_shift} at order n (other_shift = -1 or +1)."""
    m, free = n // 2, n - 2 * s

    def binomial(k: int) -> int:
        return comb(free, k) if 0 <= k <= free else 0

    beta: dict[frozenset, int] = {}
    for j in range(2 * s + 1):
        delta = binomial(m - j) - binomial(m + other_shift - j)
        if delta:
            for subset, coefficient in alpha[j].items():
                beta[subset] = beta.get(subset, 0) + coefficient * delta
    return beta


def smallest_certificate_coefficient(beta, s: int, i: int, k: int, lows: list[int]) -> int:
    """Smallest coefficient of d^2 D / dc_i dc_k written in y = c - lows; >= 0 certifies non-negativity."""
    rest = [r for r in range(s) if r not in (i, k)]
    smallest = None
    for size in range(len(rest) + 1):
        for subset in combinations(rest, size):
            others = [r for r in rest if r not in subset]
            total = 0
            for extra_size in range(len(others) + 1):
                for extra in combinations(others, extra_size):
                    total += beta.get(frozenset(subset + extra + (i, k)), 0) * prod(lows[r] for r in extra)
            smallest = total if smallest is None else min(smallest, total)
    return smallest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--max-spine", type=int, default=6)
    parser.add_argument("--max-order", type=int, default=200)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    report: dict = {
        "experiment": "CJ-0001 caterpillars: sign of the mixed second partials of d_m - d_{m-1} (Hypothesis V)",
        "arithmetic": "exact integers",
        "run": distpoly.run_metadata(),
        "spines": [],
    }
    for s in range(2, args.max_spine + 1):
        alpha = multiaffine_g(s)
        box = 3 if s <= 5 else (2 if s <= 7 else 1)
        validated = 0
        for leaves in product(range(box + 1), repeat=s):
            if leaves[0] >= 1 and leaves[-1] >= 1 and sum(leaves) >= s:
                assert matches_direct(alpha, list(leaves)), leaves
                validated += 1
        entry: dict = {
            "spine_vertices": s,
            "closed_form_validated": f"{validated} caterpillars with leaf numbers in 0..{box} (ends >= 1, n >= 2s) against the direct determinant",
            "domains": [],
        }
        for name, lows in (("all c_i >= 1", [1] * s), ("c_1, c_s >= 1 and c_i >= 0 inside", [1] + [0] * (s - 2) + [1])):
            first = max(2 * s, s + sum(lows) + 1)
            result: dict = {"domain": name, "orders": f"{first} to {args.max_order}"}
            for label, shift in (("lower difference d_m - d_{m-1}", -1), ("upper difference d_m - d_{m+1}", 1)):
                certificate_failures, nonpositive_vertices, minimizing_positions = [], [], set()
                for n in range(first, args.max_order + 1):
                    beta = difference(alpha, s, n, shift)
                    for i, k in combinations(range(s), 2):
                        if smallest_certificate_coefficient(beta, s, i, k, lows) < 0:
                            certificate_failures.append([n, i + 1, k + 1])
                    spare = n - s - sum(lows)
                    values = []
                    for position in range(s):
                        c = list(lows)
                        c[position] += spare
                        values.append(evaluate(beta, c))
                        if values[-1] <= 0:
                            nonpositive_vertices.append([n, c])
                    minimizing_positions.add(values.index(min(values)) + 1)
                result[label] = {
                    "pairs_and_orders_where_the_certificate_fails": len(certificate_failures),
                    "first_failures": certificate_failures[:10],
                    "vertices_with_nonpositive_value": len(nonpositive_vertices),
                    "first_nonpositive_vertices": nonpositive_vertices[:10],
                    "positions_of_the_minimizing_vertex": sorted(minimizing_positions),
                }
            entry["domains"].append(result)
            lower = result["lower difference d_m - d_{m-1}"]
            upper = result["upper difference d_m - d_{m+1}"]
            print(
                f"s = {s}, {name}, orders {first}..{args.max_order}: lower: {lower['pairs_and_orders_where_the_certificate_fails']} "
                f"certificate failures, {lower['vertices_with_nonpositive_value']} non-positive vertices, minimizing position "
                f"{lower['positions_of_the_minimizing_vertex']}; upper: {upper['pairs_and_orders_where_the_certificate_fails']} "
                f"certificate failures, {upper['vertices_with_nonpositive_value']} non-positive vertices"
            )
        report["spines"].append(entry)
    report["seconds"] = round(time.perf_counter() - started, 1)
    if args.out:
        args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
