"""CJ-0001, session 15: exact check of a direct proof of Collins's formula for the path.

Claims checked (notes/path-formula.md), for the path P_n on vertices 1..n:
  (a) Phi_n = det(I + x L) has [x^(n-k)] Phi_n = C(n+k-1, 2k-1)            (1 <= k <= n);
  (b) A_n = det((I + x L)[V minus {1}]) has [x^(n-r)] A_n = C(n+r-2, 2r-2)  (1 <= r <= n),
      i.e. [x^(n-k-1)] A_n = C(n+k-1, 2k) for 1 <= k <= n-1, and degree n-1;
  (c) ell_{P_n} = (n-1) Phi_n - 2x A_n - 2x^n, with ell_T = -2^{-(n-2)} det(2xI - D);
  (d) d_{n-k}(P_n) = C(n+k-1, 2k-1) (k-1) n / k for 2 <= k <= n, against the normalized
      coefficients d_j = 2^{j-(n-2)} |delta_j| of det(D - xI) from the distance matrix.
  (e) the two composition sums behind (a), (b), by brute force over compositions, n <= 12.
All exact: determinants of rational matrices (python-flint), evaluation at integer points
and Lagrange interpolation over fractions.Fraction.

Usage: uv run python experiments/CJ-0001-collins-shor-peak/path_formula_check.py [--max-n N] [--out FILE]
"""
import itertools
import sys
import time
from fractions import Fraction as Fr
from math import comb, prod

from flint import fmpq_mat, fmpz_mat


def fr(q):
    return Fr(int(q.p), int(q.q))


def det(rows):
    n = len(rows)
    if n == 0:
        return Fr(1)
    return fr(fmpq_mat(n, n, [v for row in rows for v in row]).det())


def interp(xs, ys):
    """Coefficients (low to high) of the polynomial through (xs, ys), exact."""
    res = [Fr(0)] * len(xs)
    for i, xi in enumerate(xs):
        num = [Fr(1)]
        den = Fr(1)
        for j, xj in enumerate(xs):
            if j != i:
                num = [Fr(0)] + num
                for t in range(len(num) - 1):
                    num[t] -= xj * num[t + 1]
                den *= (xi - xj)
        for t, c in enumerate(num):
            res[t] += ys[i] * c / den
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def poly_of(matrix_at, size, degree):
    xs = list(range(degree + 1))
    return interp(xs, [det(matrix_at(s)) if size else Fr(1) for s in xs])


def c(p, j):
    return p[j] if 0 <= j < len(p) else Fr(0)


def main(max_n):
    cases = fails = 0
    first = None
    for n in range(2, max_n + 1):
        L = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            L[i][i] += 1
            L[i + 1][i + 1] += 1
            L[i][i + 1] -= 1
            L[i + 1][i] -= 1
        D = [[abs(i - j) for j in range(n)] for i in range(n)]
        Phi = poly_of(lambda s: [[int(i == j) + s * L[i][j] for j in range(n)] for i in range(n)], n, n)
        A = poly_of(lambda s: [[int(i == j) + s * L[i][j] for j in range(1, n)] for i in range(1, n)], n - 1, n - 1)
        ell = poly_of(lambda s: [[2 * s * int(i == j) - D[i][j] for j in range(n)] for i in range(n)], n, n)
        ell = [-v / Fr(2) ** (n - 2) for v in ell]
        ok = all(c(Phi, n - k) == comb(n + k - 1, 2 * k - 1) for k in range(1, n + 1))
        # [x^(n-r)] A_n = C(n+r-2, 2r-2) for 1 <= r <= n (r = k+1; r = 1 gives the top coefficient 1)
        ok &= all(c(A, n - r) == comb(n + r - 2, 2 * r - 2) for r in range(1, n + 1)) and len(A) == n
        rhs = [Fr(0)] * (n + 1)
        for j, v in enumerate(Phi):
            rhs[j] += (n - 1) * v
        for j, v in enumerate(A):
            rhs[j + 1] -= 2 * v
        rhs[n] -= 2
        while len(rhs) > 1 and rhs[-1] == 0:
            rhs.pop()
        ok &= (ell == rhs)
        if n >= 3:
            cp = fmpz_mat(D).charpoly().coeffs()  # det(xI - D), low to high
            d = []
            for j in range(n - 1):
                num = abs(int(cp[j])) * 2 ** j
                assert num % 2 ** (n - 2) == 0
                d.append(num // 2 ** (n - 2))
            ok &= all(Fr(d[n - k]) == Fr(comb(n + k - 1, 2 * k - 1) * (k - 1) * n, k) for k in range(2, n + 1))
            ok &= all(c(ell, j) == d[j] for j in range(n - 1))
        cases += 1
        if not ok:
            fails += 1
            first = first or n
    def compositions(n, k):
        for cuts in itertools.combinations(range(1, n), k - 1):
            pts = (0,) + cuts + (n,)
            yield tuple(pts[i + 1] - pts[i] for i in range(k))

    ecases = efails = 0
    for n in range(1, 13):
        for k in range(1, n + 1):
            comps = list(compositions(n, k))
            ecases += 1
            efails += sum(prod(q) for q in comps) != comb(n + k - 1, 2 * k - 1)
            if k <= n - 1:
                comps1 = list(compositions(n, k + 1))
                ecases += 1
                efails += sum(prod(q[1:]) for q in comps1) != comb(n + k - 1, 2 * k)
    return {"paths": [2, max_n], "cases": cases, "failures": fails + efails, "first_failure": first,
            "composition_sums": {"cases": ecases, "failures": efails}}


if __name__ == "__main__":
    import argparse
    import json
    import platform
    import subprocess
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=40)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    t0 = time.time()
    res = main(args.max_n)
    res["elapsed_seconds"] = round(time.time() - t0, 1)
    print(json.dumps(res, indent=2))
    if args.out:
        def git(*a):
            try:
                return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()
            except Exception:
                return None
        status = git("status", "--porcelain")
        res = {"run": {"command": "uv run python experiments/CJ-0001-collins-shor-peak/path_formula_check.py "
                                  + " ".join(sys.argv[1:]),
                       "git_revision": git("rev-parse", "HEAD"),
                       "tree_clean": (status == "") if status is not None else None,
                       "python": platform.python_version(),
                       "arithmetic": "exact (python-flint determinants, fractions.Fraction interpolation)"},
               **res}
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=2)
            fh.write("\n")
