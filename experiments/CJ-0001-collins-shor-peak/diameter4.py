"""The caterpillars K(a,0,c) of diameter 4 with no leaf at the centre: closed forms around the middle index.

K(a,0,c) has a spine v1 - v2 - v3 in which v1 and v3 carry a, c >= 1 pendant
leaves and v2 none (order n = a + c + 3). For n >= 6 the notes
(notes/diameter4-caterpillars.md, Theorem T3) show that the formula of
Lemma C1 of notes/spine3.md remains valid at b = 0,

    d_k = sum_{j=0}^{6} g_j(a, 0, c) C(n - 6, k - j),      0 <= k <= n - 2,

and that the identities of Lemma C2 hold with u = a + c = n - 3. With
m = floor(n/2), v = a c, K*(m) = K(m, n - 3) and H*(m) = (n - 4) K* + R(m, n - 3),
the proof needs K* > 0 and H* > 0 for m >= 3 in the four cases.

What is computed:

1. K* and H*, symbolically, from the forms stated in spine3.py, and their
   agreement with the factorizations stated in the notes;
2. K* > 0 and H* > 0 for 3 <= m <= --max-m (a finite check of what the notes
   prove for all m >= 3);
3. for every K(a,0,c) with 3 <= a + c <= --direct-max-sum: equality of the whole
   sequence given by the closed form with the direct n x n determinant, which
   tests the extension of Lemma C1 to b = 0 against the tree;
4. for every K(a,0,c) with a + c <= --max-sum: the identities of Lemma C2 at
   b = 0 as identities between integers, d_{m-1} < d_m > d_{m+1}, and (up to
   --sequence-max-sum) the location of every maximizing index;
5. the path on five vertices, K(1,0,1), by the direct determinant.

All arithmetic is exact. A finite check is not a proof; the proof is in the notes.

Usage:
    python experiments/CJ-0001-collins-shor-peak/diameter4.py \
        --out experiments/CJ-0001-collins-shor-peak/results/diameter4.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from flint import fmpz_poly

sys.path.insert(0, str(Path(__file__).resolve().parent))

import distpoly  # noqa: E402
import spine3  # noqa: E402


def parents(a: int, c: int) -> list[int]:
    """K(a,0,c): spine 0 - 1 - 2, a leaves at 0, c leaves at 2."""
    return [-1, 0, 1] + [0] * a + [2] * c


def stated_at_centre_empty(case: str, m):
    """(K*, H*) as stated in the notes (Theorem T3, Step 2). Works for integers and polynomials."""
    if case == "even-lower":
        return 20 * m * (m + 1) * (2 * m - 5), 2 * (2 * m - 5) * (50 * m**3 - 111 * m**2 + 49 * m - 30)
    if case == "even-upper":
        return 8 * (m + 1) * (2 * m - 5) * (4 * m - 3), 10 * (2 * m - 5) * (22 * m**3 - 39 * m**2 - 7 * m + 18)
    if case == "odd-lower":
        return 4 * (m + 1) * (m + 2) * (23 * m - 36), 4 * (2 * m - 3) * (65 * m**3 + 53 * m**2 - 80 * m - 92)
    if case == "odd-upper":
        return 12 * (m + 1) * (m + 2) * (m - 2), 12 * (2 * m - 3) * (m + 2) * (5 * m**2 + 3 * m - 6)
    raise ValueError(case)


def symbolic_check() -> dict[str, str]:
    """K(m, n - 3) and (n - 4) K + R at u = n - 3, from the forms of spine3.stated, against the notes."""
    m = fmpz_poly([0, 1])
    report = {}
    for case in spine3.CASES:
        u = 2 * m - 3 if case.startswith("even") else 2 * m - 2
        k, r, *_ = spine3.stated(case, m, u)
        k_star, h_star = stated_at_centre_empty(case, m)
        assert k == k_star and (u - 1) * k + r == h_star, case
        report[case] = "K(m, n-3) and (n-4) K + R at u = n-3 equal the factorizations stated in the notes"
    return report


def matches_direct(a: int, c: int) -> bool:
    n = a + c + 3
    d = spine3.coefficients(a, 0, c)
    return distpoly.scaled_coefficients(parents(a, c)) == [d[k] << (n - 2) for k in range(n - 1)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--max-sum", type=int, default=600, help="check the closed forms for a + c up to this value")
    parser.add_argument("--sequence-max-sum", type=int, default=100, help="examine the whole sequence up to this value")
    parser.add_argument("--direct-max-sum", type=int, default=40, help="compare with the n x n determinant up to this value")
    parser.add_argument("--max-m", type=int, default=2000, help="check K* > 0 and H* > 0 for 3 <= m <= this value")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    report: dict = {
        "experiment": "CJ-0001 caterpillars K(a,0,c) of diameter 4: closed forms around the middle index",
        "arithmetic": "exact integers",
        "run": distpoly.run_metadata(),
    }

    report["symbolic"] = symbolic_check()
    print("symbolic: K* and H* agree with the factorizations stated in the notes")

    for m in range(3, args.max_m + 1):
        for case in spine3.CASES:
            k_star, h_star = stated_at_centre_empty(case, m)
            assert k_star > 0 and h_star > 0, (case, m)
    report["sign_conditions"] = {"range": f"3 <= m <= {args.max_m}", "checked": "K* > 0 and H* > 0 in the four cases", "failures": 0}
    print(f"sign conditions hold for 3 <= m <= {args.max_m}")

    checked = sequences = direct = 0
    for total in range(3, args.max_sum + 1):
        n = total + 3
        m = n // 2
        low, high = distpoly.conjectured_interval(n)
        for a in range(1, total // 2 + 1):
            c = total - a
            if total <= args.sequence_max_sum:
                d = spine3.coefficients(a, 0, c)
                sequence = [d[k] for k in range(n - 1)]
                assert all(value > 0 for value in sequence), (a, c)
                assert distpoly.peak_indices(sequence) == [m], (a, c)
                sequences += 1
            else:
                d = spine3.coefficients(a, 0, c, [m - 1, m, m + 1])
            assert spine3.closed_forms_hold(a, 0, c, d), (a, c)
            assert d[m - 1] < d[m] > d[m + 1] and low <= m <= high, (a, c)
            if total <= args.direct_max_sum:
                assert matches_direct(a, c), (a, c)
                direct += 1
            checked += 1
    larger = [(1, 70), (35, 36), (10, 55)]
    for a, c in larger:
        assert matches_direct(a, c), (a, c)
    report["caterpillars"] = {
        "range": f"1 <= a <= c, 3 <= a + c <= {args.max_sum} (orders 6 to {args.max_sum + 3})",
        "trees_checked": checked,
        "closed_form_failures": 0,
        "inequality_failures": 0,
        "whole_sequence_examined": sequences,
        "whole_sequence_range": f"a + c <= {args.sequence_max_sum}: positive, maximum at floor(n/2) only",
        "compared_with_direct_determinant": direct + len(larger),
        "direct_range": f"a + c <= {args.direct_max_sum}, and {larger}",
    }
    print(f"K(a,0,c): {checked} trees, closed forms and inequalities hold; {sequences} whole sequences; {direct + len(larger)} compared with the direct determinant")

    path5 = distpoly.scaled_coefficients(distpoly.path_parents(5))
    assert path5 == [value << 3 for value in (4, 30, 70, 50)] and distpoly.peak_indices(path5) == [2]
    report["path_on_five_vertices"] = {"normalized_coefficients": [4, 30, 70, 50], "maximizing_indices": [2], "floor_n_over_2": 2}
    print("P_5 = K(1,0,1): normalized coefficients 4, 30, 70, 50; maximum at index 2 only")

    report["seconds"] = round(time.perf_counter() - started, 1)
    if args.out:
        args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
