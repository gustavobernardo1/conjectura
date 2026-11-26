"""How close do near-star trees come to violating the lower bound floor(n/2)?

For a tree T of order n let m = floor(n/2) and

    q(T) = d_{m-1}(T) / d_m(T).

By unimodality, every maximizing index of d_0..d_{n-2} is >= m exactly when
q(T) < 1. So q(T) >= 1 for a single tree would refute the Collins–Shor lower
bound, and 1 - q(T) measures the margin.

Caterpillars are handled exactly at any order through an equitable partition:
if the spine has s vertices carrying c_1, ..., c_s >= 1 leaves, the distance
matrix has eigenvalue -2 with multiplicity n - 2s and the remaining 2s
eigenvalues are those of an explicit 2s x 2s quotient matrix Q, so

    ell_T(x) = -2^(-(2s-2)) (x + 1)^(n-2s) det(2xI - Q)

and d_k is a short sum of binomial coefficients. The formula is validated
against the direct n x n computation before it is used.

All arithmetic is exact (integers and Fractions); floats appear only in the
printed and stored decimal renderings of exact rationals.

Usage:
    python experiments/CJ-0001-collins-shor-peak/near_star_families.py \
        --out experiments/CJ-0001-collins-shor-peak/results/near-star-families.json
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path

from flint import fmpz_mat

sys.path.insert(0, str(Path(__file__).resolve().parent))

import distpoly  # noqa: E402


def caterpillar_parents(leaves: list[int]) -> list[int]:
    spine = len(leaves)
    parents = [-1] + list(range(spine - 1))
    for index, count in enumerate(leaves):
        parents += [index] * count
    return parents


def caterpillar_coefficients(leaves: list[int], indices: list[int]) -> dict[int, Fraction]:
    """Rationals proportional (by one positive factor) to d_k for k in indices; needs all c_i >= 1.

    With N = n - 2s, d_k is proportional to sum_j g_j C(N, k - j). To keep the
    numbers small at large n, binomials are taken relative to C(N, anchor) and
    obtained from the exact recurrences C(N, i+1) = C(N, i) (N - i)/(i + 1).
    """
    if min(leaves) < 1:
        raise ValueError("every spine vertex must carry at least one leaf")
    s = len(leaves)
    n = s + sum(leaves)
    quotient = [[0] * (2 * s) for _ in range(2 * s)]
    for i in range(s):
        for j in range(s):
            gap = abs(i - j)
            quotient[i][j] = gap
            quotient[i][s + j] = (gap + 1) * leaves[j]
            quotient[s + i][j] = gap + 1
            quotient[s + i][s + j] = (gap + 2) * leaves[j] if i != j else 2 * (leaves[i] - 1)
    charpoly = fmpz_mat(quotient).charpoly()
    g = [-(int(charpoly[j]) << j) for j in range(2 * s + 1)]  # coefficients of -det(2xI - Q)
    free = n - 2 * s
    low, high = max(0, min(indices) - 2 * s), min(free, max(indices))
    anchor = min(max((low + high) // 2, 0), free)
    relative = {anchor: Fraction(1)}
    for i in range(anchor, high):
        relative[i + 1] = relative[i] * Fraction(free - i, i + 1)
    for i in range(anchor, low, -1):
        relative[i - 1] = relative[i] * Fraction(i, free - i + 1)
    return {k: sum(g[j] * relative.get(k - j, 0) for j in range(2 * s + 1) if 0 <= k - j <= free) for k in indices}


def critical_ratio_direct(parents: list[int]) -> Fraction:
    m = len(parents) // 2
    sequence = distpoly.scaled_coefficients(parents)
    return Fraction(sequence[m - 1], sequence[m])


def critical_ratio_caterpillar(leaves: list[int]) -> Fraction:
    m = (len(leaves) + sum(leaves)) // 2
    values = caterpillar_coefficients(leaves, [m - 1, m])
    return values[m - 1] / values[m]


def balanced(n: int, spine: int) -> list[int]:
    base, extra = divmod(n - spine, spine)
    return [base + (1 if index < extra else 0) for index in range(spine)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    report: dict = {"experiment": "CJ-0001 near-star families and the lower-bound margin", "arithmetic": "exact; decimals are renderings"}

    # 1. Validation of the quotient formula against the direct computation.
    validation = [[29, 29], [19, 19, 19], [5, 7, 9, 4], [1, 1, 1], [3, 1, 2, 1, 6], [12, 1, 1, 30]]
    for leaves in validation:
        assert critical_ratio_caterpillar(leaves) == critical_ratio_direct(caterpillar_parents(leaves)), leaves
    report["quotient_formula_validated_on"] = validation
    print(f"quotient formula agrees with the direct computation on {len(validation)} caterpillars")

    # 2. Smallest even order at which some double star has a larger critical ratio than the star.
    report["double_star_vs_star"] = []
    for n in range(6, 41, 2):
        star = critical_ratio_direct(distpoly.star_parents(n))
        best = max((critical_ratio_direct(caterpillar_parents([a, n - 2 - a])), a) for a in range(1, (n - 2) // 2 + 1))
        entry = {"order": n, "star_q": str(star), "best_double_star": [best[1], n - 2 - best[1]], "best_double_star_q": str(best[0]),
                 "double_star_exceeds_star": best[0] > star, "best_double_star_q_below_1": best[0] < 1}
        report["double_star_vs_star"].append(entry)
    first = next((entry["order"] for entry in report["double_star_vs_star"] if entry["double_star_exceeds_star"]), None)
    report["first_even_order_where_a_double_star_exceeds_the_star"] = first
    print(f"first even order (6..40) at which a double star has q larger than the star: {first}")

    # 3. Balanced caterpillars at large even orders: n * (1 - q) by spine length.
    report["balanced_caterpillars"] = []
    for n in (10**3, 10**4, 10**5, 10**6):
        row = {"order": n, "by_spine": []}
        for spine in range(1, 17):
            q = critical_ratio_caterpillar(balanced(n, spine))
            row["by_spine"].append({"spine": spine, "q_below_1": q < 1, "n_times_one_minus_q": float(n * (1 - q)),
                                    "comparison_6_over_2s_plus_3": 6 / (2 * spine + 3)})
        report["balanced_caterpillars"].append(row)
        print(f"n={n}: all q<1: {all(item['q_below_1'] for item in row['by_spine'])}; n(1-q): "
              + " ".join(f"{item['spine']}:{item['n_times_one_minus_q']:.4f}" for item in row["by_spine"]))

    # 4. For each even order, the balanced caterpillar (any spine length) closest to violation.
    report["best_balanced_caterpillar"] = []
    for n in (100, 200, 400, 1000, 2000, 4000, 10000, 100000):
        best = max((critical_ratio_caterpillar(balanced(n, spine)), spine) for spine in range(1, min(n // 2, 80) + 1))
        entry = {"order": n, "best_spine": best[1], "one_minus_q": float(1 - best[0]), "q_below_1": best[0] < 1}
        report["best_balanced_caterpillar"].append(entry)
        print(f"n={n}: closest balanced caterpillar has spine {best[1]}, 1-q = {entry['one_minus_q']:.3e}, q<1: {entry['q_below_1']}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
