"""CJ-0001: the Wiener form of the distance polynomial of a tree and the bound floor((n-1)/2) on the peak.

Exact integer arithmetic.  Notation of
research/active/CJ-0001-collins-shor-peak/notes/wiener-form.md:

  l_T(x) = sum_{k <= n-2} d_k x^k - 4 x^n     (d_k the normalized coefficients, from the distance matrix)
  Phi    = det(I + xL),  adj = adj(I + xL),  t = D 1 (transmissions),  W = Wiener index
  mu     = floor((n-1)/2),  lam(f) = [x^mu] f - [x^(mu-1)] f

For every tree of order 2..max_order:
  W1  n^2 l_T = 4 (W - n x) Phi + (1/x) sum_{u<v} (t_u - t_v)^2 adj_uv        (Proposition S25)
  W2  adj_uv = x^d(u,v) * prod over the components K of T - path(u,v) of Phi(K, e_attachment)   (Lemma S24)
  W3  Phi in C_{n-1} (Proposition S26);  adj_uv / x^d in C_{n-d-1}
  W4  lam(x^(d-1) Pi_uv) >= 0 for every pair u < v                               (pair terms in the proof of Theorem T4)
  W5  lam((W - n x) Phi) > 0   (orders >= 5)                                    (main term in the proof of Theorem T4)
  W6  d_{mu-1} < d_mu   (orders >= 3)                                           (Theorem T4)
  W7  n^2 (d_mu - d_{mu-1}) = 4 lam((W - n x) Phi) + sum_{u<v} (t_u - t_v)^2 lam(x^(d-1) Pi_uv)
  W8  W >= (n-1)^2
"""
import argparse
import json
import subprocess
import sys
import time

import networkx as nx

from distpoly import distance_matrix, layouts, parents_from_layout, scaled_coefficients
from rooted_state import WT, in_cone, padd, pmul, pscale, psub, ptrim

KEYS = ("W1_wiener_form", "W2_adjugate_product", "W3_cones", "W4_pair_terms", "W5_main_term",
        "W6_peak_inequality", "W7_decomposition", "W8_wiener_bound")


def coeff(p, k):
    return p[k] if 0 <= k < len(p) else 0


def lam(p, mu):
    return coeff(p, mu) - coeff(p, mu - 1)


def path_between(G, u, v):
    return nx.shortest_path(G, u, v)


def product_off_path(G, n, edges, path):
    """prod_K Phi(K, e_a): K the components of T - path, a the vertex of K adjacent to the path."""
    on = set(path)
    H = G.subgraph([v for v in range(n) if v not in on])
    prod = [1]
    for comp in nx.connected_components(H):
        comp = sorted(comp)
        idx = {v: i for i, v in enumerate(comp)}
        e2 = [(idx[a], idx[b]) for a, b in edges if a in idx and b in idx]
        nu = [sum(1 for w in G.neighbors(v) if w in on) for v in comp]
        assert sum(nu) == 1
        prod = pmul(prod, WT(len(comp), e2, nu).phi)
    return prod


def run(max_order):
    rows = []
    for n in range(2, max_order + 1):
        t0 = time.time()
        fail = {k: 0 for k in KEYS}
        trees = pairs = 0
        mu = (n - 1) // 2
        least_main = None
        for lay in layouts(n):
            par = parents_from_layout(lay)
            edges = [(par[v], v) for v in range(1, n)]
            T = WT(n, edges, [0] * n)
            G = nx.Graph()
            G.add_nodes_from(range(n))
            G.add_edges_from(edges)
            D = distance_matrix(par)
            t = [sum(row) for row in D]
            W = sum(t) // 2
            trees += 1
            if n >= 3:
                s = scaled_coefficients(par)
                assert all(c % 2 ** (n - 2) == 0 for c in s)
                ell = [c // 2 ** (n - 2) for c in s] + [0, -4]
            else:
                ell = [1, 0, -4]
            if W < (n - 1) ** 2:
                fail["W8_wiener_bound"] += 1
            if not in_cone(T.phi, n - 1):
                fail["W3_cones"] += 1
            main = pmul([W, -n], T.phi)
            total = pscale(main, 4)
            lam_sum = 4 * lam(main, mu)
            for u in range(n):
                for v in range(u + 1, n):
                    pairs += 1
                    d = D[u][v]
                    a = T.adj[u][v]
                    if any(a[:d]):
                        fail["W2_adjugate_product"] += 1
                    Pi = ptrim(a[d:])
                    if Pi != ptrim(product_off_path(G, n, edges, path_between(G, u, v))):
                        fail["W2_adjugate_product"] += 1
                    if not in_cone(Pi, n - d - 1):
                        fail["W3_cones"] += 1
                    term = [0] * (d - 1) + Pi
                    w = (t[u] - t[v]) ** 2
                    total = padd(total, pscale(term, w))
                    lt = lam(term, mu)
                    lam_sum += w * lt
                    if mu >= 1 and lt < 0:
                        fail["W4_pair_terms"] += 1
            if ptrim(total) != ptrim(pscale(ell, n * n)):
                fail["W1_wiener_form"] += 1
            if n >= 3:
                gap = ell[mu] - ell[mu - 1]
                if gap <= 0:
                    fail["W6_peak_inequality"] += 1
                if n * n * gap != lam_sum:
                    fail["W7_decomposition"] += 1
                lm = lam(main, mu)
                if n >= 5 and lm <= 0:
                    fail["W5_main_term"] += 1
                if least_main is None or lm < least_main:
                    least_main = lm
        rows.append(dict(order=n, trees=trees, pairs=pairs, failures=fail,
                         least_lam_of_main_term=least_main, seconds=round(time.time() - t0, 1)))
        print(rows[-1], file=sys.stderr, flush=True)
    return rows


def peak_only(lo, hi):
    """W6 alone, from the distance matrix, for larger orders."""
    rows = []
    for n in range(lo, hi + 1):
        t0 = time.time()
        mu = (n - 1) // 2
        bad = trees = 0
        for lay in layouts(n):
            s = scaled_coefficients(parents_from_layout(lay))
            trees += 1
            if s[mu] <= s[mu - 1]:
                bad += 1
        rows.append(dict(order=n, trees=trees, W6_failures=bad, seconds=round(time.time() - t0, 1)))
        print(rows[-1], file=sys.stderr, flush=True)
    return rows


def git(*a):
    try:
        return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:  # noqa: BLE001
        return "unavailable"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-order", type=int, default=11)
    ap.add_argument("--peak-order", type=int, default=17)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    start = time.time()
    revision, dirty = git("rev-parse", "HEAD"), bool(git("status", "--porcelain"))
    res = dict(full_checks=run(args.max_order), peak_only=peak_only(args.max_order + 1, args.peak_order))
    res["provenance"] = dict(
        command=" ".join(sys.argv), revision=revision, dirty_tree_at_start=dirty,
        python=sys.version.split()[0], networkx=nx.__version__,
        seconds=round(time.time() - start, 1), arguments=vars(args),
    )
    text = json.dumps(res, indent=1)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    print(json.dumps(dict(provenance=res["provenance"]), indent=1))
