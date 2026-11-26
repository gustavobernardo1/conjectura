"""CJ-0001, session 6: the pieces of the Laplacian form of r_A, on small trees (exact).

Notation of notes/skeleton-locality.md and notes/gamma-reduction.md. For every
tree S with 2 to --max-skeleton vertices (one per isomorphism class) and every
A with 1 <= |A| < s (B = V minus A, t = |B|), this script computes, as exact
rational polynomials (values at t + 3 integer points, Lagrange interpolation),

    Phi_B = det(I + x L_B),      T = z^T adj(I + x L_B) z,
    pos   = Phi_B [a(1+x) + (3 + 3H - 2 e_B) x],      r_A = pos - x^2 T,

and reports how often
  - Phi_B fails to have a non-negative half-gamma expansion of degree t (Lemma F says: never),
  - pos fails to have one of degree t + 1 (never, by Lemma F),
  - T has a negative coefficient (an observation; not proved),
  - r_A fails to have one of degree t + 1, separately for |A| = 1 and |A| >= 2
    (Conjecture Gamma concerns |A| >= 2; |A| = 1 is the extension used by Proposition S11).

The identity r_A = pos - x^2 T is Proposition S7 and is checked against the
definition of r_A by locality_check.py, not here. Command:

    uv run python experiments/CJ-0001-collins-shor-peak/gamma_pieces.py --max-skeleton 8 --out experiments/CJ-0001-collins-shor-peak/results/gamma-pieces.json
"""
import argparse
import json
import subprocess
import sys
import time
from fractions import Fraction
from itertools import combinations
from math import comb

import networkx as nx
from flint import fmpq, fmpq_mat

ap = argparse.ArgumentParser()
ap.add_argument("--max-skeleton", type=int, default=8)
ap.add_argument("--out", default=None)
args = ap.parse_args()
start = time.time()


def interp(xs, ys):
    n = len(xs)
    coeffs = [Fraction(0)] * n
    for i in range(n):
        num = [Fraction(1)]
        den = Fraction(1)
        for j in range(n):
            if j != i:
                num = [Fraction(0)] + num
                for k in range(len(num) - 1):
                    num[k] -= xs[j] * num[k + 1]
                den *= xs[i] - xs[j]
        for k in range(n):
            coeffs[k] += ys[i] * num[k] / den
    return coeffs


def half_gamma(c, d):
    c = list(c) + [Fraction(0)] * (d + 1 - len(c))
    assert all(v == 0 for v in c[d + 1:]), (c, d)
    c = c[:d + 1]
    rho = []
    e = 0
    while 2 * e < d:
        r = c[e]
        rho.append(r)
        for i in range(d - 2 * e + 1):
            c[e + i] -= r * comb(d - 2 * e, i)
        e += 1
    assert all(v == 0 for v in c[:e])
    return rho, c[e:]


def nonneg(c, d):
    rho, sig = half_gamma(c, d)
    return all(v >= 0 for v in rho) and all(v >= 0 for v in sig)


stats = {"r_fail_by_a": {}, "r_cases_by_a": {}, "r_fail_examples": [], "cases": 0, "phi_weight_t_fail": 0, "T_coeff_negative": 0, "pos_part_fail": 0,
         "phi_weight_t_fail_examples": [], "T_neg_examples": []}
maxs = args.max_skeleton
for s in range(2, maxs + 1):
    for g in nx.nonisomorphic_trees(s):
        deg = [g.degree(v) for v in range(s)]
        for a in range(1, s + 1):
            for A in combinations(range(s), a):
                B = [v for v in range(s) if v not in A]
                t = len(B)
                if t == 0:
                    continue
                LB = [[deg[u] if u == v else (-1 if g.has_edge(u, v) else 0) for v in B] for u in B]
                xs = [Fraction(i) for i in range(1, t + 4)]
                phis, Ts = [], []
                h = [deg[u] - 1 for u in B]
                k = [sum(1 for v in B if g.has_edge(u, v)) for u in B]
                z = [2 * h[i] - k[i] for i in range(t)]
                for x in xs:
                    fx = fmpq(x.numerator, x.denominator)
                    pm = fmpq_mat(t, t, [(1 if i == j else 0) + fx * LB[i][j] for i in range(t) for j in range(t)])
                    phi = pm.det()
                    sol = pm.inv() * fmpq_mat(t, 1, z)
                    T = phi * sum(z[i] * sol[i, 0] for i in range(t))
                    phis.append(Fraction(int(phi.p), int(phi.q)))
                    Ts.append(Fraction(int(T.p), int(T.q)))
                phi_c = interp(xs, phis)
                T_c = interp(xs, Ts)
                stats["cases"] += 1
                if not nonneg(phi_c, t):
                    stats["phi_weight_t_fail"] += 1
                    if len(stats["phi_weight_t_fail_examples"]) < 3:
                        stats["phi_weight_t_fail_examples"].append([s, sorted(g.edges()), B, [str(c) for c in phi_c]])
                if any(c < 0 for c in T_c):
                    stats["T_coeff_negative"] += 1
                    if len(stats["T_neg_examples"]) < 3:
                        stats["T_neg_examples"].append([s, sorted(g.edges()), B, [str(c) for c in T_c]])
                # positive part Phi*[a(1+x) + (3+3H-2e)x] at degree t+1
                lin = [Fraction(a), Fraction(a + 3 + 3 * sum(h) - sum(k))]
                pos = [Fraction(0)] * (t + 2)
                for i, c in enumerate(phi_c[:t + 1]):
                    pos[i] += c * lin[0]
                    pos[i + 1] += c * lin[1]
                if not nonneg(pos, t + 1):
                    stats["pos_part_fail"] += 1
                r_c = [pos[i] - (T_c[i - 2] if 2 <= i < len(T_c) + 2 else 0) for i in range(t + 2)]
                assert all(c == 0 for c in T_c[t:])
                key = "1" if a == 1 else ">=2"
                stats["r_cases_by_a"][key] = stats["r_cases_by_a"].get(key, 0) + 1
                if not nonneg(r_c, t + 1):
                    stats["r_fail_by_a"][key] = stats["r_fail_by_a"].get(key, 0) + 1
                    if len(stats["r_fail_examples"]) < 4:
                        stats["r_fail_examples"].append([s, sorted(g.edges()), list(A), [str(c) for c in r_c]])
rev = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
out = {"experiment": "CJ-0001 pieces of the Laplacian form of r_A (Lemma F, Proposition S11, extension of Property Gamma to |A| = 1)",
       "arithmetic": "exact rationals; polynomials by interpolation at more points than the degree",
       "run": {"command": sys.argv, "git_revision_at_run": rev, "python": sys.version.split()[0], "networkx": nx.__version__},
       "max_skeleton": maxs, "totals": stats, "seconds": round(time.time() - start, 1)}
text = json.dumps(out, indent=1)
print(text)
if args.out:
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text + chr(10))
bad = stats["phi_weight_t_fail"] or stats["pos_part_fail"] or stats["T_coeff_negative"] or stats["r_fail_by_a"]
raise SystemExit(1 if bad else 0)
