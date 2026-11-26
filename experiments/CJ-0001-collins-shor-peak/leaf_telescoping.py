"""CJ-0001: the leaf recursion for the distance polynomial and star minimality in the cone order.

Exact integer arithmetic throughout.  Notation of
research/active/CJ-0001-collins-shor-peak/notes/leaf-telescoping.md:

  l_T(x)   = (n-1) det(I + xL) - x tau^T adj(I + xL) tau        (tau_v = 2 - deg v)
           = sum_{k <= n-2} d_k x^k - 4 x^n                       (d_k the normalized coefficients)
  r_u(T)   = (1 + 4x) Psi_u + Omega_u                             (the polynomial r_A of the notes for A = {u})
  C_d      = the cone of non-negative combinations of x^e (1+x)^(d-2e), 2e < d, and x^e, d <= 2e <= 2d.

Part A (every tree of order 1..max_rooted, every vertex u):
  A1  l_T from the Laplacian formula equals the coefficients of the distance matrix
      (python-flint characteristic polynomial; orders >= 3), with top coefficients 0 and -4;
  A2  R(T, 0) = x l_T - (1 + 4x) Phi_T;
  A3  leaf recursion  l_{T + leaf at u} = (1 + x) l_T + r_u(T);
  A4  r_u(T) in C_n;
  A5  r_u(T) - (1 + 4x)(1 + x)^(n-1) in C_n;
  A6  R(T, e_u) in C_{n+1};
  A7  Phi(T, e_u) - (1 + x)^n in C_n;
  A8  telescoping along the vertex order of the level sequence.
Part B (every tree of order 3..max_order, from the distance matrix only):
  B1  l_star = (1 + x)^(n-2) [(n-1) + 4(n-2) x - 4x^2];
  B2  l_T - l_star in C_{n-1};
  B3  l_T + 4x (1 + x)^(n-1) in C_{n-1};
  B4  the smallest value of (d_m - d_{m-1})(T) - (d_m - d_{m-1})(star), m = floor(n/2).
"""
import argparse
import json
import subprocess
import sys
import time
from math import comb

import networkx as nx

from distpoly import layouts, parents_from_layout, scaled_coefficients, star_parents
from rooted_state import WT, half_gamma, in_cone, padd, pmul, pscale, psub, ptrim, state


def ell_laplacian(T):
    """(n-1) Phi - x tau^T adj tau for a WT with zero weights."""
    n = T.j
    tau = [2 - T.deg[v] for v in range(n)]
    q = []
    for a in range(n):
        for b in range(n):
            q = padd(q, pscale(T.adj[a][b], tau[a] * tau[b]))
    return ptrim(psub(pscale(T.phi, n - 1), [0] + q))


def edges_of(par):
    return [(par[v], v) for v in range(1, len(par))]


def binom_row(k):
    return [comb(k, i) for i in range(k + 1)]


def part_A(max_rooted):
    keys = ("A1_distance_matrix", "A2_R0", "A3_leaf_recursion", "A4_r_in_cone", "A5_r_lower_bound",
            "A6_R_unit_weight", "A7_Phi_lower_bound", "A8_telescoping")
    rows = []
    examples = {}
    for n in range(1, max_rooted + 1):
        fail = {k: 0 for k in keys}
        trees = rooted = 0
        for lay in layouts(n):
            par = parents_from_layout(lay)
            T = WT(n, edges_of(par), [0] * n)
            ell = ell_laplacian(T)
            trees += 1
            if n >= 3:
                s = scaled_coefficients(par)
                want = [c // 2 ** (n - 2) for c in s] + [0, -4]
                if any(c % 2 ** (n - 2) for c in s) or want != ell:
                    fail["A1_distance_matrix"] += 1
            if ptrim(psub([0] + ell, pmul([1, 4], T.phi))) != ptrim(T.R()):
                fail["A2_R0"] += 1
            # A8: build the tree leaf by leaf in the order of the level sequence
            acc = pscale([0] + binom_row(n - 1), -4)
            for k in range(1, n):
                Tk = WT(k, edges_of(par[:k]), [0] * k)
                sk = state(Tk, par[k])
                rk = padd(pmul([1, 4], sk["Psi"]), sk["Om"])
                acc = padd(acc, pmul(binom_row(n - 1 - k), rk))
            if ptrim(acc) != ell:
                fail["A8_telescoping"] += 1
            for u in range(n):
                rooted += 1
                st = state(T, u)
                r = padd(pmul([1, 4], st["Psi"]), st["Om"])
                T2 = WT(n + 1, edges_of(par) + [(u, n)], [0] * (n + 1))
                if ptrim(padd(pmul([1, 1], ell), r)) != ell_laplacian(T2):
                    fail["A3_leaf_recursion"] += 1
                if not in_cone(r, n):
                    fail["A4_r_in_cone"] += 1
                    examples.setdefault("A4_r_in_cone", dict(parents=par, u=u, r=ptrim(r)))
                if not in_cone(psub(r, pmul([1, 4], binom_row(n - 1))), n):
                    fail["A5_r_lower_bound"] += 1
                    examples.setdefault("A5_r_lower_bound", dict(parents=par, u=u, r=ptrim(r)))
                Tu = T.raised(u)
                if not in_cone(Tu.R(), n + 1):
                    fail["A6_R_unit_weight"] += 1
                    examples.setdefault("A6_R_unit_weight", dict(parents=par, u=u, R=ptrim(Tu.R())))
                if not in_cone(psub(Tu.phi, binom_row(n)), n):
                    fail["A7_Phi_lower_bound"] += 1
        rows.append(dict(order=n, trees=trees, rooted=rooted, failures=fail))
        print("A", rows[-1], file=sys.stderr, flush=True)
    return dict(rows=rows, first_failures=examples)


def part_B(max_order):
    rows = []
    examples = {}
    for n in range(3, max_order + 1):
        t0 = time.time()
        m = n // 2
        star = scaled_coefficients(star_parents(n))
        closed = pmul(binom_row(n - 2), [n - 1, 4 * (n - 2), -4])
        star_formula_ok = [c * 2 ** (n - 2) for c in closed[: n - 1]] == star and closed[n - 1:] == [0, -4]
        four = [0] + [2 ** n * c for c in binom_row(n - 1)]
        trees = bad_min = bad_G = equal = 0
        least = None
        for lay in layouts(n):
            par = parents_from_layout(lay)
            s = scaled_coefficients(par)
            trees += 1
            diff = [a - b for a, b in zip(s, star)]
            if not any(diff):
                equal += 1
            else:
                if min(half_gamma(diff, n - 1)) < 0:
                    bad_min += 1
                    examples.setdefault("B2_star_minimality", dict(order=n, parents=par))
                gap = diff[m] - diff[m - 1]
                if least is None or gap < least[0]:
                    least = (gap, par)
            G = [a + b for a, b in zip(s + [0], four[:n])]
            if min(half_gamma(G, n - 1)) < 0:
                bad_G += 1
                examples.setdefault("B3_G", dict(order=n, parents=par))
        rows.append(dict(
            order=n, trees=trees, trees_with_l_equal_to_star=equal, B1_star_formula=star_formula_ok,
            B2_failures=bad_min, B3_failures=bad_G,
            B4_least_gap_scaled_by_2_pow_n_minus_2=None if least is None else least[0],
            B4_least_gap_tree=None if least is None else least[1],
            star_gap_scaled=star[m] - star[m - 1], seconds=round(time.time() - t0, 1),
        ))
        print("B", {k: v for k, v in rows[-1].items() if k != "B4_least_gap_tree"}, file=sys.stderr, flush=True)
    return dict(rows=rows, first_failures=examples)


def git(*a):
    try:
        return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:  # noqa: BLE001
        return "unavailable"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-rooted", type=int, default=10)
    ap.add_argument("--max-order", type=int, default=18)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    start = time.time()
    # Revision and state of the tree are read before the computation starts.
    revision, dirty = git("rev-parse", "HEAD"), bool(git("status", "--porcelain"))
    res = dict(part_A=part_A(args.max_rooted), part_B=part_B(args.max_order))
    res["provenance"] = dict(
        command=" ".join(sys.argv), revision=revision,
        dirty_tree_at_start=dirty, python=sys.version.split()[0],
        networkx=nx.__version__, seconds=round(time.time() - start, 1), arguments=vars(args),
    )
    text = json.dumps(res, indent=1)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    print(json.dumps(dict(provenance=res["provenance"]), indent=1))
