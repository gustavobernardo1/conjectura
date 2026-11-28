"""CJ-0001, session 15: exact checks behind revision 3 of the manuscript.

Parts (all exact: integers, fractions.Fraction, and exact sign tests in Q(sqrt 5)):

A  Remark 9.6 (rem:AMW) of manuscripts/CJ-0001-collins-shor/main.tex: for every
   tree T of order 2..--max-identity, the matching numbers of the subdivision S(T)
   are the coefficients of det(I + t L_T), and avm(S(T)) = n - tr(I + L_T)^{-1}.
B  The path is the unique maximizer of avm among all trees of order 2..--max-avm.
C  avm(P_N) > aN + b, a = (5 - sqrt5)/10, b = (7 sqrt5 - 17)/10, for 4 <= N <= --max-path
   (the comparison used in Remark 9.6 with Theorem 4.4 of arXiv:1903.09825).
D  Section 12, item 1: the orders n in [3, --max-open] for which p(T) <= p(P_n) is
   settled by the upper bound (p(P_n) = ceil(xi - 2/5), xi = n - n/sqrt5), with p(P_n)
   from the criterion of Lemma 11.1 (lem:S47); integer arithmetic only.
E  The tie at order 13 (Section 13, item 1): every tree of order 13, its maximizing
   indices and the common value (needs python-flint).

Usage: uv run python experiments/CJ-0001-collins-shor-peak/amw_reduction_check.py [--out FILE]
"""
import os
import sys
import time
from fractions import Fraction as Fr
from math import isqrt

import networkx as nx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from manuscript_check import det_inv, interp, lap  # noqa: E402


def trees(n):
    if n == 1:
        g = nx.Graph()
        g.add_node(0)
        yield g
        return
    for t in nx.nonisomorphic_trees(n):
        yield nx.convert_node_labels_to_integers(t)


def matching_numbers(tree):
    """Numbers m_k of matchings with k edges of a tree, by dynamic programming."""
    nodes = list(tree.nodes())
    root = nodes[0]
    parent = {root: None}
    order = [root]
    for v in order:
        for w in tree[v]:
            if w not in parent:
                parent[w] = v
                order.append(w)

    def add(p, q):
        r = [0] * max(len(p), len(q))
        for i, c in enumerate(p):
            r[i] += c
        for i, c in enumerate(q):
            r[i] += c
        return r

    def mul(p, q):
        r = [0] * (len(p) + len(q) - 1)
        for i, c in enumerate(p):
            for j, d in enumerate(q):
                r[i + j] += c * d
        return r

    free, used = {}, {}
    for v in reversed(order):
        kids = [w for w in tree[v] if parent.get(w) == v]
        tot = {w: add(free[w], used[w]) for w in kids}
        a = [1]
        for w in kids:
            a = mul(a, tot[w])
        b = [0]
        for w in kids:
            prod = mul([0, 1], free[w])
            for u in kids:
                if u != w:
                    prod = mul(prod, tot[u])
            b = add(b, prod)
        free[v], used[v] = a, b
    m = add(free[root], used[root])
    while len(m) > 1 and m[-1] == 0:
        m.pop()
    return m


def avm(m):
    return Fr(sum(k * c for k, c in enumerate(m)), sum(m))


def subdivision(tree):
    s = nx.Graph()
    n = tree.number_of_nodes()
    s.add_nodes_from(range(n))
    for i, (u, v) in enumerate(tree.edges()):
        s.add_edge(u, n + i)
        s.add_edge(n + i, v)
    return s


def part_a(maxn):
    cases = fails = 0
    for n in range(2, maxn + 1):
        for t in trees(n):
            L = lap(n, list(t.edges()))
            # det(I + tL) at t = 0..n, then exact interpolation
            xs = list(range(n + 1))
            ys = [det_inv([[int(i == j) + s * L[i][j] for j in range(n)] for i in range(n)])[0] for s in xs]
            coeffs = interp(xs, ys)
            coeffs = [c for c in coeffs] + [Fr(0)] * (n + 1 - len(coeffs))
            m = matching_numbers(subdivision(t))
            ok = all(coeffs[k] == (m[k] if k < len(m) else 0) for k in range(n + 1))
            _, inv = det_inv([[int(i == j) + L[i][j] for j in range(n)] for i in range(n)])
            tr = sum(inv[i][i] for i in range(n))
            ok = ok and avm(m) == n - tr
            cases += 1
            fails += not ok
    return {"orders": [2, maxn], "cases": cases, "failures": fails}


def part_b(maxn):
    cases = fails = 0
    for N in range(2, maxn + 1):
        vals = []
        for t in trees(N):
            vals.append((avm(matching_numbers(t)), max(d for _, d in t.degree()) <= 2))
        best = max(v for v, _ in vals)
        winners = [p for v, p in vals if v == best]
        cases += len(vals)
        fails += winners != [True]
    return {"orders": [2, maxn], "trees": cases, "failures": fails}


def sign_q5(r, s):
    """Sign of r + s*sqrt(5) for rationals r, s (exact)."""
    if r >= 0 and s >= 0:
        return 0 if r == 0 and s == 0 else 1
    if r <= 0 and s <= 0:
        return -1
    # opposite signs: compare r^2 with 5 s^2
    if r > 0:
        return 1 if r * r > 5 * s * s else -1
    return 1 if 5 * s * s > r * r else -1


def part_c(maxN):
    from math import comb
    cases = fails = 0
    for N in range(4, maxN + 1):
        m = [comb(N - k, k) for k in range(N // 2 + 1)]
        A = avm(m)
        # 10(avm - aN - b) = (10 avm - 5N + 17) + sqrt5 (N - 7)
        cases += 1
        fails += sign_q5(10 * A - 5 * N + 17, Fr(N - 7)) != 1
    return {"N": [4, maxN], "cases": cases, "failures": fails}


def floor_over_sqrt5(n):
    j = isqrt(n * n // 5)
    while 5 * (j + 1) ** 2 <= n * n:
        j += 1
    while 5 * j * j > n * n:
        j -= 1
    return j


def ceil_xi_minus_two_fifths(n):
    # ceil(n - 2/5 - n/sqrt5) = n - floor(n/sqrt5 + 2/5); floor(n/sqrt5 + 2/5) = max j with 5j - 2 <= sqrt5 n
    j = floor_over_sqrt5(n) + 1
    while not (5 * j - 2 <= 0 or (5 * j - 2) ** 2 <= 5 * n * n):
        j -= 1
    return n - j


def path_peak(n):
    k = 2
    while not (5 * k ** 3 + 2 * k ** 2 - 4 * k - 2 > k * n * n):
        k += 1
    return n - k


def part_d(maxn):
    small, ceil_case, open_ = [], [], []
    fails = 0
    for n in range(3, maxn + 1):
        K = ceil_xi_minus_two_fifths(n)
        fl_xi, cl_xi = n - floor_over_sqrt5(n) - 1, n - floor_over_sqrt5(n)
        p = path_peak(n)
        fails += p not in (fl_xi, cl_xi)
        fails += not (p <= K)
        if K == fl_xi:
            small.append(n)
        elif p == cl_xi:
            ceil_case.append(n)
        else:
            open_.append(n)
    return {"n": [3, maxn], "fractional_part_below_two_fifths": len(small),
            "path_at_ceiling_with_fractional_part_above_two_fifths": len(ceil_case),
            "open": len(open_), "first_open": open_[:10], "first_ceiling_case": ceil_case[:10],
            "failures": fails}


def part_e():
    try:
        from flint import fmpz_mat
    except ImportError:
        return {"skipped": "python-flint not importable"}
    n = 13
    ties = []
    count = 0
    for t in trees(n):
        count += 1
        dist = dict(nx.all_pairs_shortest_path_length(t))
        cp = fmpz_mat([[dist[i][j] for j in range(n)] for i in range(n)]).charpoly().coeffs()
        d = []
        for k in range(n - 1):
            num = abs(int(cp[k])) * 2 ** k
            assert num % 2 ** (n - 2) == 0
            d.append(num // 2 ** (n - 2))
        mx = max(d)
        idx = [k for k, v in enumerate(d) if v == mx]
        if len(idx) > 1:
            ties.append({"indices": idx, "value": mx, "edges": sorted(t.edges())})
    return {"order": n, "trees": count, "ties": ties}


def _run_block(argv):
    import platform
    import subprocess

    def git(*a):
        try:
            return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()
        except Exception:
            return None
    status = git("status", "--porcelain")
    return {
        "command": "uv run python experiments/CJ-0001-collins-shor-peak/amw_reduction_check.py " + " ".join(argv),
        "git_revision": git("rev-parse", "HEAD"),
        "tree_clean": (status == "") if status is not None else None,
        "python": platform.python_version(),
        "networkx": nx.__version__,
        "arithmetic": "exact (integers, fractions.Fraction, sign tests in Q(sqrt5))",
    }


if __name__ == "__main__":
    import argparse
    import json
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-identity", type=int, default=9)
    ap.add_argument("--max-avm", type=int, default=16)
    ap.add_argument("--max-path", type=int, default=200)
    ap.add_argument("--max-open", type=int, default=2000)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    t0 = time.time()
    res = {
        "A_identity": part_a(args.max_identity),
        "B_path_maximizes_avm": part_b(args.max_avm),
        "C_path_above_AMW_bound": part_c(args.max_path),
        "D_open_orders": part_d(args.max_open),
        "E_tie_order_13": part_e(),
    }
    res["failures_total"] = sum(v.get("failures", 0) for v in res.values() if isinstance(v, dict))
    res["elapsed_seconds"] = round(time.time() - t0, 1)
    print(json.dumps(res, indent=2))
    if args.out:
        res = {"run": _run_block(sys.argv[1:]), **res}
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=2)
            fh.write("\n")
