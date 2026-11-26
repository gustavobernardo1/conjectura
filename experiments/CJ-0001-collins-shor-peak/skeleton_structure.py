"""Trees made of a skeleton with pendant leaves: structure of the coefficient polynomials.

Let S be a tree on s >= 2 vertices (the skeleton) with distance matrix P, and
let T be obtained by attaching c_v >= 0 pendant leaves at each vertex v of S
(order n = s + sum c_v). The twin partition (the s skeleton vertices and the s
leaf classes) has the 2s x 2s quotient matrix, with C = diag(c) and J all ones,

    Q(c) = [[ P,      (P + J) C        ],
            [ P + J,  (P + 2J) C - 2I  ]],

and  -det(2xI - Q(c)) / 4^(s-1) = sum_j g_j(c) x^j  with g_j of degree at most
1 in each c_v. For n >= 2s,  d_k(T) = sum_j g_j(c) C(n - 2s, k - j)
(notes/skeleton-identity.md, Lemma S1). Caterpillars are the case S = path.

What is computed, for every tree S with 2 <= s <= --max-skeleton vertices
(one per isomorphism class):

1. Lemma S1: the closed form against the direct n x n determinant of T, for
   leaf numbers in a small box, zeros included;
2. Proposition S2 (expansion over subsets): for every subset A of the skeleton,
   the coefficient of prod_{v in A} c_v in det(2xI - Q(c)) equals
       (2x + 2)^(s - |A|) (2x)^|A| det( 2x I_{A^c} - P - 1_A 1^T - 1 1_A^T - (|A| / 2x) J ),
   checked as an identity between polynomials in x by exact evaluation at
   more points than the degree;
3. Proposition S3 (top coefficient): the product of all c_v occurs only in
   g_{s-1} and g_s, with coefficients s and s + 3, whatever the skeleton;
4. Hypothesis V for general skeletons: for every order n from 2s to
   --max-order, the certificate of mixed_partials.py for the mixed second
   partials of d_m - d_{m-1} on the domain c >= 0, and the sign of the value
   at each vertex (n - s) e_p of the slice.

5. Property Gamma (order-independent): for every subset A with |A| >= 2, the
   coefficient polynomial p_A(x) = sum_j alpha_{j,A} x^j is divisible by
   x^(|A|-1) (1+x)^(s-|A|), and the quotient r_A, of degree at most
   d = s - |A| + 1, has non-negative coefficients in the basis
       x^e (1+x)^(d-2e)  (2e < d),      x^e  (2e >= d).
   By Proposition S4 of the notes this implies that every multi-affine
   coefficient of d_m - d_{m-1} of degree >= 2 is non-negative for EVERY order
   n >= 2s, hence Hypothesis V for that skeleton and every order.

6. Two observations of the notes (not proved): for A = V minus one vertex w of
   degree g, the expansion is rho_0 = s - 1, sigma_1 = (g-1)s + 2g + 1,
   sigma_2 = (g-1)(s + 6 - g) + 3; and (locality) for |V - A| <= 4 the
   expansion of r_A depends only on s and on the principal submatrix of the
   Laplacian of S on V - A, up to simultaneous permutation.

All arithmetic is exact. Items 1 to 3 check statements proved in the notes;
item 4 is evidence for a hypothesis in a finite range of orders; item 5 is,
for each skeleton on which it holds, a computer-assisted proof of the
hypothesis for all orders (given Proposition S4).

Usage:
    python experiments/CJ-0001-collins-shor-peak/skeleton_structure.py \
        --out experiments/CJ-0001-collins-shor-peak/results/skeleton-structure.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, prod
from pathlib import Path

from flint import fmpq, fmpq_mat, fmpz_mat

sys.path.insert(0, str(Path(__file__).resolve().parent))

import distpoly  # noqa: E402
import mixed_partials  # noqa: E402


def skeleton_distances(parents: list[int]) -> list[list[int]]:
    return distpoly.distance_matrix(parents)


def quotient(dist: list[list[int]], leaves: list[int]) -> list[list[int]]:
    s = len(dist)
    q = [[0] * (2 * s) for _ in range(2 * s)]
    for i in range(s):
        for j in range(s):
            q[i][j] = dist[i][j]
            q[i][s + j] = (dist[i][j] + 1) * leaves[j]
            q[s + i][j] = dist[i][j] + 1
            q[s + i][s + j] = (dist[i][j] + 2) * leaves[j] - (2 if i == j else 0)
    return q


def g_at(dist: list[list[int]], leaves: list[int]) -> list[int]:
    s = len(dist)
    charpoly = fmpz_mat(quotient(dist, leaves)).charpoly()
    values = [-(int(charpoly[j]) << j) for j in range(2 * s + 1)]
    assert all(value % 4 ** (s - 1) == 0 for value in values)
    return [value // 4 ** (s - 1) for value in values]


def multiaffine_g(dist: list[list[int]]) -> list[dict[frozenset, int]]:
    """alpha[j][A]: coefficient of prod_{v in A} c_v in g_j (Moebius inversion on {0,1}^s)."""
    s = len(dist)
    at = {bits: g_at(dist, list(bits)) for bits in product((0, 1), repeat=s)}
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


def tree_parents(skeleton: list[int], leaves: list[int]) -> list[int]:
    parents = list(skeleton)
    for vertex, count in enumerate(leaves):
        parents += [vertex] * count
    return parents


def closed_form(alpha, leaves: list[int]) -> list[int]:
    s = len(leaves)
    n = s + sum(leaves)
    free = n - 2 * s
    g = [mixed_partials.evaluate(alpha[j], leaves) for j in range(2 * s + 1)]
    return [sum(g[j] * comb(free, k - j) for j in range(2 * s + 1) if 0 <= k - j <= free) for k in range(n - 1)]


def subset_formula_value(dist: list[list[int]], subset: tuple[int, ...], x: Fraction) -> Fraction:
    """(2x+2)^(s-|A|) (2x)^|A| det(2x I_{A^c} - P - 1_A 1^T - 1 1_A^T - (|A|/2x) J) at a rational x != 0."""
    s = len(dist)
    size = len(subset)
    inside = set(subset)
    rows = []
    for i in range(s):
        row = []
        for j in range(s):
            value = Fraction(-dist[i][j]) - (1 if i in inside else 0) - (1 if j in inside else 0) - Fraction(size) / (2 * x)
            if i == j and i not in inside:
                value += 2 * x
            row.append(fmpq(value.numerator, value.denominator))
        rows.append(row)
    det = fmpq_mat(rows).det()
    return (2 * x + 2) ** (s - size) * (2 * x) ** size * Fraction(int(det.p), int(det.q))


def subset_coefficient_value(alpha, s: int, subset: tuple[int, ...], x: Fraction) -> Fraction:
    """Coefficient of prod_{v in A} c_v in det(2xI - Q(c)) = -4^(s-1) sum_j g_j x^j, at x."""
    key = frozenset(subset)
    return -(4 ** (s - 1)) * sum(alpha[j].get(key, 0) * x**j for j in range(2 * s + 1))


def half_gamma_expansion(alpha, s: int, subset: tuple[int, ...]) -> tuple[list[int], list[int]] | None:
    """(rho, sigma) with r_A = sum_{2e<d} rho_e x^e (1+x)^(d-2e) + sum_{2e>=d} sigma_e x^e; None if not divisible."""
    key = frozenset(subset)
    a = len(subset)
    d = s - a + 1
    p = [alpha[j].get(key, 0) for j in range(2 * s + 1)]
    if any(p[: a - 1]):
        return None
    r = p[a - 1 :]
    for _ in range(s - a):  # exact division by (1 + x), synthetic, from the lowest degree
        quotient_coefficients = []
        carry = 0
        for coefficient in r:
            carry = coefficient - carry
            quotient_coefficients.append(carry)
        if quotient_coefficients[-1] != 0:
            return None
        r = quotient_coefficients[:-1]
    if any(r[d + 1 :]):
        return None
    r = (r + [0] * (d + 1))[: d + 1]
    rho = []
    for e in range((d + 1) // 2):  # all e with 2e < d
        rho.append(r[e])
        for step in range(d - 2 * e + 1):
            r[e + step] -= rho[-1] * comb(d - 2 * e, step)
    assert not any(r[: (d + 1) // 2])
    return rho, r[(d + 1) // 2 :]


def laplacian_key(skeleton: list[int], outside: tuple[int, ...]) -> tuple:
    """Canonical form, under simultaneous permutation, of the Laplacian of the skeleton restricted to `outside`."""
    s = len(skeleton)
    degree = [sum(1 for parent in skeleton if parent == v) + (skeleton[v] >= 0) for v in range(s)]
    adjacent = lambda u, v: skeleton[u] == v or skeleton[v] == u  # noqa: E731
    return min(
        tuple(degree[u] if u == v else -int(adjacent(u, v)) for u in order for v in order)
        for order in permutations(outside)
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--max-skeleton", type=int, default=7)
    parser.add_argument("--max-order", type=int, default=100)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    report: dict = {
        "experiment": "CJ-0001 trees made of a skeleton with pendant leaves: structure of the coefficient polynomials",
        "arithmetic": "exact integers and rationals",
        "run": distpoly.run_metadata(),
        "skeletons": [],
    }
    totals = {"skeletons": 0, "closed_form_trees": 0, "subset_identities": 0, "certificate_failures": 0, "nonpositive_vertices": 0}
    local: dict[tuple, set] = {}
    one_vertex_checked = 0
    for s in range(2, args.max_skeleton + 1):
        box = 2 if s <= 5 else 1
        for layout in distpoly.layouts(s):
            skeleton = distpoly.parents_from_layout(layout)
            dist = skeleton_distances(skeleton)
            alpha = multiaffine_g(dist)
            entry: dict = {"vertices": s, "parents": skeleton, "degrees": sorted((sum(1 for p in skeleton if p == v) + (skeleton[v] >= 0) for v in range(s)), reverse=True)}

            # 1. Lemma S1 against the direct determinant.
            checked = 0
            for leaves in product(range(box + 1), repeat=s):
                if sum(leaves) >= s:
                    n = s + sum(leaves)
                    direct = distpoly.scaled_coefficients(tree_parents(skeleton, list(leaves)))
                    assert direct == [value << (n - 2) for value in closed_form(alpha, list(leaves))], (skeleton, leaves)
                    checked += 1
            entry["closed_form_against_direct_determinant"] = f"{checked} trees, leaf numbers in 0..{box}, n >= 2s"
            totals["closed_form_trees"] += checked

            # 2. Proposition S2 at 2s + 2 rational points (both sides have degree at most 2s in x).
            points = [Fraction(value) for value in range(1, 2 * s + 3)]
            identities = 0
            for size in range(s + 1):
                for subset in combinations(range(s), size):
                    for x in points:
                        assert subset_formula_value(dist, subset, x) == subset_coefficient_value(alpha, s, subset, x), (skeleton, subset, x)
                    identities += 1
            entry["subset_expansion_identities"] = identities
            totals["subset_identities"] += identities

            # 3. Proposition S3.
            full = frozenset(range(s))
            top = {j: polynomial[full] for j, polynomial in enumerate(alpha) if full in polynomial}
            assert top == {s - 1: s, s: s + 3}, (skeleton, top)
            entry["top_coefficient"] = {str(j): value for j, value in top.items()}

            # 4. Hypothesis V on the domain c >= 0.
            lows = [0] * s
            failures, nonpositive, positions = [], [], set()
            for n in range(2 * s, args.max_order + 1):
                beta = mixed_partials.difference(alpha, s, n, -1)
                for i, k in combinations(range(s), 2):
                    if mixed_partials.smallest_certificate_coefficient(beta, s, i, k, lows) < 0:
                        failures.append([n, i, k])
                values = []
                for position in range(s):
                    c = [0] * s
                    c[position] = n - s
                    values.append(mixed_partials.evaluate(beta, c))
                    if values[-1] <= 0:
                        nonpositive.append([n, position])
                positions.add(values.index(min(values)))
            entry["hypothesis_V_on_c_nonnegative"] = {
                "orders": f"{2 * s} to {args.max_order}",
                "pairs_and_orders_where_the_certificate_fails": len(failures),
                "first_failures": failures[:8],
                "vertices_with_nonpositive_value": len(nonpositive),
                "first_nonpositive_vertices": nonpositive[:8],
                "minimizing_vertex_positions": sorted(positions),
            }
            # 5. Property Gamma for every subset with at least two elements.
            gamma_failures = []
            for size in range(2, s + 1):
                for subset in combinations(range(s), size):
                    expansion = half_gamma_expansion(alpha, s, subset)
                    if expansion is None or min(expansion[0] + expansion[1]) < 0:
                        gamma_failures.append([list(subset), expansion])
            # 6. The one-vertex formula and locality.
            degree = [sum(1 for parent in skeleton if parent == v) + (skeleton[v] >= 0) for v in range(s)]
            for size in range(max(2, s - 4), s):
                for subset in combinations(range(s), size):
                    outside = tuple(v for v in range(s) if v not in subset)
                    expansion = half_gamma_expansion(alpha, s, subset)
                    assert expansion is not None, (skeleton, subset)
                    local.setdefault((s, laplacian_key(skeleton, outside)), set()).add((tuple(expansion[0]), tuple(expansion[1])))
                    if len(outside) == 1:
                        g = degree[outside[0]]
                        assert expansion == ([s - 1], [(g - 1) * s + 2 * g + 1, (g - 1) * (s + 6 - g) + 3]), (skeleton, outside, expansion)
                        one_vertex_checked += 1
            entry["property_gamma"] = {"subsets_checked": 2**s - s - 1, "failures": len(gamma_failures), "first_failures": gamma_failures[:6]}
            entry["top_expansion"] = half_gamma_expansion(alpha, s, tuple(range(s)))
            totals["gamma_failures"] = totals.get("gamma_failures", 0) + len(gamma_failures)
            totals["gamma_subsets"] = totals.get("gamma_subsets", 0) + 2**s - s - 1
            totals["certificate_failures"] += len(failures)
            totals["nonpositive_vertices"] += len(nonpositive)
            totals["skeletons"] += 1
            report["skeletons"].append(entry)
    totals["one_vertex_formula_checked"] = one_vertex_checked
    totals["locality_classes"] = len(local)
    totals["locality_classes_with_more_than_one_expansion"] = sum(1 for values in local.values() if len(values) > 1)
    report["totals"] = totals
    report["seconds"] = round(time.perf_counter() - started, 1)
    print(json.dumps(totals))
    for entry in report["skeletons"]:
        v = entry["hypothesis_V_on_c_nonnegative"]
        if entry["property_gamma"]["failures"]:
            print("   gamma fails:", entry["vertices"], entry["degrees"], entry["property_gamma"]["failures"], entry["property_gamma"]["first_failures"][:3])
        if v["pairs_and_orders_where_the_certificate_fails"] or v["vertices_with_nonpositive_value"]:
            print("  ", entry["vertices"], entry["degrees"], v["pairs_and_orders_where_the_certificate_fails"], v["first_failures"][:3], v["vertices_with_nonpositive_value"], v["first_nonpositive_vertices"][:3])
    if args.out:
        args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
