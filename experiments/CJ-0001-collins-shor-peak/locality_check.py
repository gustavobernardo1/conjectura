"""CJ-0001, session 6: exact checks of the reduction of r_A to the Laplacian block.

For a tree S on s vertices with distance matrix P and A a subset of V
(a = |A|, B = V minus A, t = |B|), notes/skeleton-identity.md defines

    N_A(x) = 2x I_B - P - 1_A 1^T - 1 1_A^T - (a/2x) J,
    r_A(x) = -2^(2-s) x det N_A(x)          (a polynomial of degree <= t + 1).

This script compares, as exact rational numbers at more points than the
degree, the definition with the three statements of notes/skeleton-locality.md:

  S6  r_A(x) = (s-1) x det(I - K G), with the (t+1) x (t+1) matrices
      K = [[-beta, 1^T], [1, 2x I]], beta = 2 + a/(2x),
      G = v v^T / (2(s-1)) - diag(0, L_B)/2, v = (2, tau_B),
      L_B = L[B, B] the principal block of the Laplacian, tau = 2 - deg.
  S7  r_A(x) = det(I + x L_B) [a + x (s + 3 - 1^T tau_B)]
               + x (L_B 1 - tau_B)^T adj(I + x L_B) (1 + x tau_B).
  S7' (the same, rearranged) with h = deg - 1 on B, z = 2h - k, k_w the number
      of neighbours of w inside B, e_B the number of edges inside B:
      r_A(x) = det(I + x L_B) [a (1+x) + (3 + 3 sum(h) - 2 e_B) x]
               - x^2 z^T adj(I + x L_B) z.
  S10 for B independent and non-empty, Phi = prod_B (1 + g_w x),
      Phi_w = Phi / (1 + g_w x), H = sum(h):
      r_A(x) = (a - H)(1+x) Phi + 3x Phi
               + sum_w [h_w (1+x)^2 + 3 h_w x (1+x) + h_w^2 x] Phi_w,  and a - H >= 1.
  S8  for B = {w}, deg(w) = g:
      r_A(x) = (s-1)(1+x)^2 + [(g-1)s + 2g + 1] x + [(g-1)(s+6-g) + 3] x^2.
  S9  for B = {u, w} of degrees g, h, with e = 1 if u, w are adjacent and 0
      otherwise, Sg = g + h, Pi = g h:
      r_A(x) = (s-2)(1+x)^3 + rho1 x(1+x) + sigma2 x^2 + sigma3 x^3,
      rho1   = (s+1) Sg - 2s + 1 - 2e,
      sigma2 = (s+6)(Pi - e) - Sg^2 + (2+2e) Sg - s - 3,
      sigma3 = (s+11-2e) Pi - Sg Pi - 4(1-e) Sg - (s+11) e - s + 2.

It also compares Corollary 6 of Collins, "Factoring distance matrix
polynomials" (as printed in the author's manuscript read in session 6), with
the distance characteristic polynomial of the balanced double star.

Trees: one per isomorphism class, from networkx.nonisomorphic_trees. The code
shares nothing with skeleton_structure.py. Arithmetic: exact rationals
(python-flint fmpq). Command:

    uv run python experiments/CJ-0001-collins-shor-peak/locality_check.py \
        --max-skeleton 8 --out experiments/CJ-0001-collins-shor-peak/results/locality-check.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from itertools import combinations

import networkx as nx
from flint import fmpq, fmpq_mat

POINTS = [fmpq(p, q) for p, q in
          [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (3, 2), (2, 3), (5, 1),
           (5, 2), (7, 3), (7, 1), (4, 5), (4, 3), (9, 2)]]  # positive: I + x L_B is then invertible


def det(rows):
    n = len(rows)
    if n == 0:
        return fmpq(1)
    return fmpq_mat(n, n, [e for row in rows for e in row]).det()


def r_definition(P, s, A, x):
    inA = [1 if v in A else 0 for v in range(s)]
    a = len(A)
    N = [[(2 * x if (u == v and not inA[u]) else fmpq(0)) - P[u][v] - inA[u] - inA[v] - fmpq(a) / (2 * x)
          for v in range(s)] for u in range(s)]
    return -fmpq(4) / fmpq(2) ** s * x * det(N)


def r_reduced(s, a, LB, tauB, x):
    t = len(tauB)
    beta = 2 + fmpq(a) / (2 * x)
    K = [[-beta] + [fmpq(1)] * t] + [[fmpq(1)] + [2 * x if i == j else fmpq(0) for j in range(t)] for i in range(t)]
    v = [fmpq(2)] + [fmpq(z) for z in tauB]
    G = [[v[i] * v[j] / (2 * (s - 1)) - (fmpq(LB[i - 1][j - 1]) / 2 if i and j else 0) for j in range(t + 1)]
         for i in range(t + 1)]
    M = [[(1 if i == j else 0) - sum(K[i][k] * G[k][j] for k in range(t + 1)) for j in range(t + 1)]
         for i in range(t + 1)]
    return (s - 1) * x * det(M)


def r_forest(s, a, LB, tauB, x):
    t = len(tauB)
    phi_mat = [[(1 if i == j else 0) + x * LB[i][j] for j in range(t)] for i in range(t)]
    phi = det(phi_mat)
    total = phi * (a + x * (s + 3 - sum(tauB)))
    if t:
        rhs = fmpq_mat(t, 1, [1 + x * z for z in tauB])
        sol = fmpq_mat(t, t, [e for row in phi_mat for e in row]).inv() * rhs  # phi != 0 at the points used
        left = [sum(LB[i]) - tauB[i] for i in range(t)]
        total += x * phi * sum(left[i] * sol[i, 0] for i in range(t))
    return total


def r_clean(s, a, LB, x):
    t = len(LB)
    phi_mat = [[(1 if i == j else 0) + x * LB[i][j] for j in range(t)] for i in range(t)]
    phi = det(phi_mat)
    h = [LB[i][i] - 1 for i in range(t)]
    k = [-sum(LB[i][j] for j in range(t) if j != i) for i in range(t)]
    z = [2 * h[i] - k[i] for i in range(t)]
    total = phi * (a * (1 + x) + (3 + 3 * sum(h) - sum(k)) * x)  # sum(k) = 2 e_B
    if t:
        sol = fmpq_mat(t, t, [e for row in phi_mat for e in row]).inv() * fmpq_mat(t, 1, z)
        total -= x * x * phi * sum(z[i] * sol[i, 0] for i in range(t))
    return total


def r_independent(a, degB, x):
    h = [g - 1 for g in degB]
    phi = fmpq(1)
    for g in degB:
        phi *= 1 + g * x
    total = (a - sum(h)) * (1 + x) * phi + 3 * x * phi
    for g, hw in zip(degB, h):
        total += (hw * (1 + x) ** 2 + 3 * hw * x * (1 + x) + hw * hw * x) * phi / (1 + g * x)
    return total


def collins_corollary_6(max_n):
    """CPD(2S_n) = det(D - lambda I) for the balanced double star S(n, n)."""
    rows = []
    for n in range(1, max_n + 1):
        g = nx.Graph([(0, 1)] + [(0, 2 + i) for i in range(n)] + [(1, 2 + n + i) for i in range(n)])
        N = 2 * n + 2
        dist = dict(nx.all_pairs_shortest_path_length(g))
        printed_ok = corrected_ok = True
        for lam in range(-N - 3, N + 4):  # 2N + 7 points, degree N
            lam = fmpq(lam)
            direct = det([[fmpq(dist[u][v]) - (lam if u == v else 0) for v in range(N)] for u in range(N)])
            common = (lam + 2) ** (2 * (n - 1))
            printed = common * (lam + n) * (lam + 1) * (lam * lam - (5 * n - 1) * lam - 9 * n)
            corrected = common * (lam * lam + (n + 3) * lam + 2) * (lam * lam - (5 * n - 1) * lam - 4 * n - 2)
            printed_ok &= direct == printed
            corrected_ok &= direct == corrected
        rows.append({"n": n, "order": N, "printed_formula_matches": bool(printed_ok),
                     "formula_with_factors_l2+(n+3)l+2_and_l2-(5n-1)l-4n-2_matches": bool(corrected_ok)})
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-skeleton", type=int, default=8)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    start = time.time()
    totals = {"trees": 0, "subsets": 0, "S6_failures": 0, "S7_failures": 0,
              "S7prime_failures": 0, "S10_cases": 0, "S10_failures": 0, "S10_min_a_minus_H": None,
              "S8_cases": 0, "S8_failures": 0, "S9_cases": 0, "S9_failures": 0,
              "S9_min_coefficients_when_A_has_at_least_2_elements": None,
              "points_per_subset": len(POINTS)}
    s9_min = None
    per_order = {}
    for s in range(2, args.max_skeleton + 1):
        count = 0
        for g in nx.nonisomorphic_trees(s):
            count += 1
            dist = dict(nx.all_pairs_shortest_path_length(g))
            P = [[dist[u][v] for v in range(s)] for u in range(s)]
            deg = [g.degree(v) for v in range(s)]
            for a in range(s + 1):
                for A in combinations(range(s), a):
                    setA = set(A)
                    B = [v for v in range(s) if v not in setA]
                    LB = [[deg[u] if u == v else (-1 if g.has_edge(u, v) else 0) for v in B] for u in B]
                    tauB = [2 - deg[u] for u in B]
                    totals["subsets"] += 1
                    ok6 = ok7 = ok8 = ok9 = ok7p = ok10 = True
                    indep = bool(B) and all(LB[i][j] == 0 for i in range(len(B)) for j in range(len(B)) if i != j)
                    if indep:
                        slack = a - sum(deg[u] - 1 for u in B)
                        totals["S10_cases"] += 1
                        cur_min = totals["S10_min_a_minus_H"]
                        totals["S10_min_a_minus_H"] = slack if cur_min is None else min(cur_min, slack)
                    if len(B) == 2:
                        gg, hh = deg[B[0]], deg[B[1]]
                        e = 1 if g.has_edge(B[0], B[1]) else 0
                        Sg, Pi = gg + hh, gg * hh
                        rho1 = (s + 1) * Sg - 2 * s + 1 - 2 * e
                        sigma2 = (s + 6) * (Pi - e) - Sg * Sg + (2 + 2 * e) * Sg - s - 3
                        sigma3 = (s + 11 - 2 * e) * Pi - Sg * Pi - 4 * (1 - e) * Sg - (s + 11) * e - s + 2
                        if a >= 2:
                            cur = [s - 2, rho1, sigma2, sigma3]
                            s9_min = cur if s9_min is None else [min(p, q) for p, q in zip(s9_min, cur)]
                    for x in POINTS:
                        ref = r_definition(P, s, setA, x)
                        ok6 &= ref == r_reduced(s, a, LB, tauB, x)
                        ok7 &= ref == r_forest(s, a, LB, tauB, x)
                        ok7p &= ref == r_clean(s, a, LB, x)
                        if indep:
                            ok10 &= ref == r_independent(a, [deg[u] for u in B], x)
                        if len(B) == 1:
                            gg = deg[B[0]]
                            ok8 &= ref == ((s - 1) * (1 + x) ** 2 + ((gg - 1) * s + 2 * gg + 1) * x
                                           + ((gg - 1) * (s + 6 - gg) + 3) * x * x)
                        if len(B) == 2:
                            ok9 &= ref == ((s - 2) * (1 + x) ** 3 + rho1 * x * (1 + x) + sigma2 * x * x
                                           + sigma3 * x ** 3)
                    if len(B) == 2:
                        totals["S9_cases"] += 1
                        totals["S9_failures"] += not ok9
                    totals["S6_failures"] += not ok6
                    totals["S7prime_failures"] += not ok7p
                    totals["S10_failures"] += not ok10
                    totals["S7_failures"] += not ok7
                    if len(B) == 1:
                        totals["S8_cases"] += 1
                        totals["S8_failures"] += not ok8
        per_order[s] = count
        totals["trees"] += count
    totals["S9_min_coefficients_when_A_has_at_least_2_elements"] = s9_min
    collins = collins_corollary_6(6)
    try:
        rev = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    except OSError:
        rev = "unknown"
    out = {
        "experiment": "CJ-0001 reduction of r_A to the Laplacian block (S6 to S10); Collins 1993 Corollary 6",
        "arithmetic": "exact rationals (python-flint fmpq); polynomial identities compared at more points than the degree",
        "run": {"command": sys.argv, "git_revision_at_run": rev, "python": sys.version.split()[0],
                "networkx": nx.__version__},
        "trees_per_order": per_order,
        "totals": totals,
        "collins_1993_corollary_6": collins,
        "seconds": round(time.time() - start, 1),
    }
    text = json.dumps(out, indent=1)
    print(text)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    return 0 if not (totals["S6_failures"] or totals["S7_failures"] or totals["S8_failures"]
                     or totals["S9_failures"]
                     or totals["S7prime_failures"] or totals["S10_failures"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
