"""CJ-0001, session 8: the rooted state of a weighted tree, the refutation of
statements (E'') and (S), and statement (Lambda) (exact integer arithmetic).

Notation of notes/gamma-components.md and notes/rooted-calculus.md. For a tree
T on j vertices with integer weights nu >= 0: M = I + x(L_T + diag nu),
Phi = det M, p_v = 1 + (2 - k_v - nu_v) x, pi_u = e_u^T adj(M) p,
R(T, nu) = (N + j - 1)(1 + x) Phi - p^T adj(M) p. For a root u:

    Psi = adj(M)_uu,   H = (Phi - Psi)/x,   G = (1 + 2x) Psi - pi_u,
    Omega = sum_i R(T_i, nu + e_{u_i}) prod_{l != i} Phi(T_l, nu + e_{u_l})
            over the components T_i of T - u (u_i the neighbour of u in T_i),
    F = (1 + 5x + 3x^2) Phi + (x + 4x^2) Psi + 2x^2 pi_u          (session 7),
    Lambda = x [(1 - x) Phi + 2x Psi + R(T, nu + e_u) - 2x G].

Part A (identities; every tree with at most --max-order vertices, one per
isomorphism class, every weight in {0..--max-weight}^j, zero included, every
root u):
  A1  G and Omega have non-negative coefficients;
  A2  G = x [2 Psi - H + sum_v adj(M)_uv (k_v + 2 nu_v - 2)];
  A3  raising the root weight:
      R(T, nu + e_u) - R(T, nu) = [(1+2x)^2 + nu_u x(1+x)] Psi + x(1+x) H + x Omega - 2x G;
  A4  a new root r of weight 0 above u (tree T^):
      Psi^ = Phi + x Psi,  H^ = Phi,  G^ = x (x H + G),  Omega^ = R(T, nu + e_u),
      R^ = (1+x) R + x [nu_u (1+x) Psi + Omega];
  A5  E := R(T^, nu + e_r) - R(T^, nu) = (1+2x)^2 Psi^ + Lambda(T, nu, u)
        = x R + x^2 Omega + [(1+x)^2 (1+4x) + x (1+2x)^2 + nu_u x^2 (1+x)] Psi
          + x (1 + 6x + 4x^2) H - 4 x^2 G,      and  E = x R(T, nu + e_u) + F;
  A6  R(T, nu + e_u) - R(T, nu) = Psi [(1+2x)^2 + 2 x nu_u]
        + sum_c Lambda(T_c, nu, c) prod_{l != c} Phi(T_l, nu + e_l),
      the sum over the components of T - u rooted at the neighbour of u;
  A7  merging two rooted trees at their roots (weights added at the root), for
      every ordered pair of rooted weighted trees with at most --max-merge
      vertices each: Psi, H, G, Omega as in the note, and
      R = R1 Psi2 + R2 Psi1 + x (H1 Omega2 + H2 Omega1)
          + x (1+x) (nu2 H1 Psi2 + nu1 H2 Psi1) + (1+2x)^2 Psi1 Psi2 - 2 G1 G2.
Part B (cone memberships on the same range; C_d = non-negative half-gamma
expansion of degree d):
  B1  F in C_{j+2}          (statement (E'') of session 7, all nu >= 0);
  B2  x [F(T, nu + e_v, u) - 2 x^3 adj(M)_uv] in C_{j+3}, every v   (statement (S));
  B3  Lambda in C_{j+2}                                     (statement (Lambda));
  B4  R(T, nu + e_u) - R(T, nu) in C_{j+1} when nu != 0     (monotonicity);
  B5  R(T, nu) in C_{j+1} when nu != 0                      (Gamma_c).
Part C (stars with centre 0 of weight n_0 and q leaves of weights n_i; all
multisets of leaf weights in {0..--star-weight}, q <= --star-leaves, n_0 in
{0, 1, 3}; roots: the centre and one leaf of each weight):
  C1  [x^{q+3}] F(star, centre) = prod(1 + n_i) * (4 + n_0 - sum n_i/(1 + n_i));
  C2  B1 to B5 for these rooted stars, with the smallest failures.
Part D (random trees, seed --seed, 2 to --random-order vertices, weights up to
1, 2, 4, 8 or 20, every root): B1 to B5.

Command:

    uv run python experiments/CJ-0001-collins-shor-peak/rooted_state.py --out experiments/CJ-0001-collins-shor-peak/results/rooted-state.json
"""
import argparse
import json
import random
import subprocess
import sys
import time
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import comb

import networkx as nx


# ---------- integer polynomials as lists (lowest degree first) ----------
def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]


def pscale(p, c):
    return [c * v for v in p]


def psub(p, q):
    return padd(p, pscale(q, -1))


def pmul(p, q):
    if not p or not q:
        return []
    r = [0] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        if u:
            for k, v in enumerate(q):
                r[i + k] += u * v
    return r


def ptrim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def peq(p, q):
    return ptrim(p) == ptrim(q)


def half_gamma(c, d):
    """Coefficients (rho_e for 2e < d, sigma_e for d <= 2e <= 2d) of a polynomial of degree <= d."""
    c = ptrim(c)
    assert len(c) <= d + 1, (c, d)
    c = c + [0] * (d + 1 - len(c))
    out = []
    for e in range(d + 1):
        if 2 * e < d:
            g = c[e]
            out.append(g)
            for i in range(d - 2 * e + 1):
                c[e + i] -= g * comb(d - 2 * e, i)
        else:
            out.append(c[e])
    return out


def in_cone(c, d):
    return min(half_gamma(c, d)) >= 0


def det_adj(L):
    """det(I + xL) and adj(I + xL) for an integer matrix L (Faddeev-LeVerrier, exact)."""
    n = len(L)
    N = [[1 if i == k else 0 for k in range(n)] for i in range(n)]
    coeffs = [1]
    mats = [N]
    for k in range(1, n + 1):
        LN = [[sum(L[i][m] * N[m][c] for m in range(n)) for c in range(n)] for i in range(n)]
        tr = sum(LN[i][i] for i in range(n))
        assert tr % k == 0
        ck = -tr // k
        coeffs.append(ck)
        N = [[LN[i][c] + (ck if i == c else 0) for c in range(n)] for i in range(n)]
        if k < n:
            mats.append(N)
        else:
            assert all(v == 0 for row in N for v in row)
    phi = [(-1) ** k * coeffs[k] for k in range(n + 1)]
    adj = [[[(-1) ** k * mats[k][i][c] for k in range(n)] for c in range(n)] for i in range(n)]
    return phi, adj


class WT:
    """A weighted tree: vertices 0..j-1, a list of edges, a list of weights."""

    def __init__(self, j, edges, nu):
        self.j, self.edges, self.nu = j, [tuple(e) for e in edges], list(nu)
        self.deg = [0] * j
        L = [[0] * j for _ in range(j)]
        for a, b in self.edges:
            self.deg[a] += 1
            self.deg[b] += 1
            L[a][b] = L[b][a] = -1
        for v in range(j):
            L[v][v] = self.deg[v] + self.nu[v]
        self.phi, self.adj = det_adj(L)
        self.p = [[1, 2 - self.deg[v] - self.nu[v]] for v in range(j)]
        self.N = sum(self.nu)
        self._R = None

    def pi(self, u):
        r = []
        for v in range(self.j):
            r = padd(r, pmul(self.adj[u][v], self.p[v]))
        return r

    def R(self):
        if self._R is None:
            V = []
            for a in range(self.j):
                for b in range(self.j):
                    V = padd(V, pmul(pmul(self.p[a], self.p[b]), self.adj[a][b]))
            c = self.N + self.j - 1
            self._R = psub(pmul([c, c], self.phi), V)
        return self._R

    def F(self, u):
        return padd(padd(pmul([1, 5, 3], self.phi), pmul([0, 1, 4], self.adj[u][u])), pscale([0, 0] + self.pi(u), 2))

    def raised(self, u):
        nu = list(self.nu)
        nu[u] += 1
        return WT(self.j, self.edges, nu)


def components_minus(T, u):
    """The components of T - u, each as (WT with nu raised by 1 at the neighbour of u, local index of that neighbour)."""
    G = nx.Graph()
    G.add_nodes_from(range(T.j))
    G.add_edges_from(T.edges)
    nb = set(G.neighbors(u))
    G.remove_node(u)
    out = []
    for comp in nx.connected_components(G):
        comp = sorted(comp)
        idx = {v: i for i, v in enumerate(comp)}
        edges = [(idx[a], idx[b]) for a, b in T.edges if a in idx and b in idx]
        root = [idx[v] for v in comp if v in nb]
        assert len(root) == 1
        nu = [T.nu[v] + (1 if v in nb else 0) for v in comp]
        out.append((WT(len(comp), edges, nu), root[0]))
    return out


def state(T, u):
    """The rooted state, each entry computed from its definition."""
    Psi = T.adj[u][u]
    xH = ptrim(psub(T.phi, Psi))
    assert xH[:1] in ([], [0])
    comps = components_minus(T, u)
    Om = []
    for i, (C, _) in enumerate(comps):
        term = C.R()
        for l, (C2, _) in enumerate(comps):
            if l != i:
                term = pmul(term, C2.phi)
        Om = padd(Om, term)
    return dict(Psi=Psi, H=xH[1:], G=psub(pmul([1, 2], Psi), T.pi(u)), Om=Om, R=T.R(), nu=T.nu[u], Phi=T.phi, comps=comps)


def Lambda(T, u, s=None):
    s = s or state(T, u)
    inner = padd(padd(pmul([1, -1], T.phi), pscale([0] + s["Psi"], 2)), psub(T.raised(u).R(), pscale([0] + s["G"], 2)))
    return [0] + inner


def S_poly(T, u, v):
    """x [F(T, nu + e_v, u) - 2 x^3 adj(M(T, nu))_uv]."""
    return [0] + psub(T.raised(v).F(u), pscale([0, 0, 0] + T.adj[u][v], 2))


def plant(T, u):
    return WT(T.j + 1, T.edges + [(u, T.j)], T.nu + [0]), T.j


def merge(T1, u1, T2, u2):
    off = T1.j

    def lab(v):
        return u1 if v == u2 else off + (v if v < u2 else v - 1)

    edges = list(T1.edges) + [(lab(a), lab(b)) for a, b in T2.edges]
    nu = list(T1.nu) + [T2.nu[v] for v in range(T2.j) if v != u2]
    nu[u1] += T2.nu[u2]
    return WT(T1.j + T2.j - 1, edges, nu), u1


def all_trees(j):
    return [[]] if j == 1 else [list(T.edges()) for T in nx.nonisomorphic_trees(j)]


CONE_KEYS = ("B1_F", "B2_S", "B3_Lambda", "B4_monotone", "B5_R")


def cone_checks(T, u, tally, examples, label):
    """B1 to B5 for the rooted weighted tree (T, u); failures counted in tally, the first of each kind kept."""
    j = T.j

    def record(key, ok, poly, d, extra=None):
        tally[key + "_cases"] += 1
        if not ok:
            tally[key + "_failures"] += 1
            if key not in examples:
                examples[key] = dict(where=label, edges=[list(e) for e in T.edges], nu=T.nu, root=u,
                                     polynomial=ptrim(poly), degree=d, half_gamma=half_gamma(poly, d), **(extra or {}))

    F = T.F(u)
    record("B1_F", in_cone(F, j + 2), F, j + 2)
    for v in range(j):
        Sp = S_poly(T, u, v)
        record("B2_S", in_cone(Sp, j + 3), Sp, j + 3, dict(v=v))
    Lam = Lambda(T, u)
    record("B3_Lambda", in_cone(Lam, j + 2), Lam, j + 2)
    if any(T.nu):
        d = psub(T.raised(u).R(), T.R())
        record("B4_monotone", in_cone(d, j + 1), d, j + 1)
        record("B5_R", in_cone(T.R(), j + 1), T.R(), j + 1)


def new_tally():
    t = {}
    for k in CONE_KEYS:
        t[k + "_cases"] = 0
        t[k + "_failures"] = 0
    return t


def part_A(max_order, max_weight, max_merge):
    cnt = dict(rooted=0, A1_G_negative=0, A1_Omega_negative=0, A2_failures=0, A3_failures=0, A4_failures=0,
               A5_failures=0, A6_failures=0, A7_pairs=0, A7_failures=0)
    tally, examples, pool = new_tally(), {}, []
    for j in range(1, max_order + 1):
        for edges in all_trees(j):
            for nu in product(range(max_weight + 1), repeat=j):
                T = WT(j, edges, nu)
                for u in range(j):
                    s = state(T, u)
                    cnt["rooted"] += 1
                    if j <= max_merge:
                        pool.append((T, u, s))
                    if min(s["G"] + [0]) < 0:
                        cnt["A1_G_negative"] += 1
                    if min(s["Om"] + [0]) < 0:
                        cnt["A1_Omega_negative"] += 1
                    az = []
                    for v in range(j):
                        az = padd(az, pscale(T.adj[u][v], T.deg[v] + 2 * T.nu[v] - 2))
                    if not peq(s["G"], [0] + padd(psub(pscale(s["Psi"], 2), s["H"]), az)):
                        cnt["A2_failures"] += 1
                    Rp = T.raised(u).R()
                    delta = psub(Rp, s["R"])
                    rhs = padd(padd(pmul(padd([1, 4, 4], pscale([0, 1, 1], s["nu"])), s["Psi"]), pmul([0, 1, 1], s["H"])),
                               psub([0] + s["Om"], pscale([0] + s["G"], 2)))
                    if not peq(delta, rhs):
                        cnt["A3_failures"] += 1
                    Tp, r = plant(T, u)
                    sp = state(Tp, r)
                    ok = peq(sp["Psi"], padd(T.phi, [0] + s["Psi"])) and peq(sp["H"], T.phi)
                    ok = ok and peq(sp["G"], [0] + padd([0] + s["H"], s["G"])) and peq(sp["Om"], Rp)
                    ok = ok and peq(sp["R"], padd(pmul([1, 1], s["R"]), [0] + padd(pmul([s["nu"], s["nu"]], s["Psi"]), s["Om"])))
                    if not ok:
                        cnt["A4_failures"] += 1
                    Lam = Lambda(T, u, s)
                    E = psub(Tp.raised(r).R(), sp["R"])
                    E2 = padd(padd([0] + s["R"], [0, 0] + s["Om"]),
                              padd(pmul(padd(padd(pmul([1, 2, 1], [1, 4]), [0, 1, 4, 4]), pscale([0, 0, 1, 1], s["nu"])), s["Psi"]),
                                   psub(pmul([0, 1, 6, 4], s["H"]), pscale([0, 0] + s["G"], 4))))
                    ok = peq(E, padd(pmul([1, 4, 4], sp["Psi"]), Lam)) and peq(E, E2) and peq(E, padd([0] + Rp, T.F(u)))
                    if not ok:
                        cnt["A5_failures"] += 1
                    tot = pmul(padd([1, 4, 4], [0, 2 * s["nu"]]), s["Psi"])
                    for i, (C, c) in enumerate(s["comps"]):
                        nuc = list(C.nu)
                        nuc[c] -= 1
                        term = Lambda(WT(C.j, C.edges, nuc), c)
                        for l, (C2, _) in enumerate(s["comps"]):
                            if l != i:
                                term = pmul(term, C2.phi)
                        tot = padd(tot, term)
                    if not peq(tot, delta):
                        cnt["A6_failures"] += 1
                    cone_checks(T, u, tally, examples, "part A/B (exhaustive)")
    for (T1, u1, s1) in pool:
        for (T2, u2, s2) in pool:
            Tm, um = merge(T1, u1, T2, u2)
            sm = state(Tm, um)
            cnt["A7_pairs"] += 1
            ok = peq(sm["Psi"], pmul(s1["Psi"], s2["Psi"]))
            for key in ("H", "G", "Om"):
                ok = ok and peq(sm[key], padd(pmul(s1[key], s2["Psi"]), pmul(s2[key], s1["Psi"])))
            Rm = padd(pmul(s1["R"], s2["Psi"]), pmul(s2["R"], s1["Psi"]))
            Rm = padd(Rm, [0] + padd(pmul(s1["H"], s2["Om"]), pmul(s2["H"], s1["Om"])))
            Rm = padd(Rm, pmul([0, 1, 1], padd(pscale(pmul(s1["H"], s2["Psi"]), s2["nu"]), pscale(pmul(s2["H"], s1["Psi"]), s1["nu"]))))
            Rm = padd(Rm, pmul([1, 4, 4], pmul(s1["Psi"], s2["Psi"])))
            Rm = psub(Rm, pscale(pmul(s1["G"], s2["G"]), 2))
            if not (ok and peq(sm["R"], Rm)):
                cnt["A7_failures"] += 1
    return dict(identities=cnt, cone=tally, first_failures=examples)


def star(q, n0, ws):
    return WT(q + 1, [(0, i + 1) for i in range(q)], [n0] + list(ws))


def part_C(star_leaves, star_weight):
    cnt = dict(stars=0, rooted=0, C1_failures=0)
    tally, examples = new_tally(), {}
    for q in range(1, star_leaves + 1):
        for ws in combinations_with_replacement(range(star_weight + 1), q):
            for n0 in (0, 1, 3):
                T = star(q, n0, ws)
                cnt["stars"] += 1
                F = T.F(0)
                F = F + [0] * (q + 4 - len(F))
                pr = 1
                for n in ws:
                    pr *= 1 + n
                if F[q + 3] != pr * (4 + n0 - sum(Fraction(n, 1 + n) for n in ws)):
                    cnt["C1_failures"] += 1
                roots = [0] + [1 + i for i in range(q) if i == 0 or ws[i] != ws[i - 1]]
                for u in roots:
                    cnt["rooted"] += 1
                    cone_checks(T, u, tally, examples, "part C (stars)")
    return dict(counts=cnt, cone=tally, first_failures=examples)


def part_D(trials, max_order, seed):
    rng = random.Random(seed)
    tally, examples = new_tally(), {}
    trees = rooted = 0
    for _ in range(trials):
        j = rng.randint(2, max_order)
        kind = rng.random()
        edges = []
        for v in range(1, j):
            if kind < 0.35:
                par = 0 if rng.random() < 0.8 else rng.randrange(v)
            elif kind < 0.5:
                par = v - 1 if rng.random() < 0.7 else rng.randrange(v)
            else:
                par = rng.randrange(v)
            edges.append((par, v))
        W = rng.choice([1, 2, 4, 8, 20])
        nu = [rng.randint(0, W) for _ in range(j)]
        if rng.random() < 0.4:
            nu[0] = 0
        T = WT(j, edges, nu)
        trees += 1
        for u in range(j):
            rooted += 1
            cone_checks(T, u, tally, examples, "part D (random)")
    return dict(trees=trees, rooted=rooted, cone=tally, first_failures=examples)


def named_examples():
    """The explicit counterexamples quoted in notes/rooted-calculus.md."""
    out = {}
    T = star(5, 0, [4] * 5)
    F = T.F(0)
    Tp, r = plant(T, 0)
    E = psub(Tp.raised(r).R(), Tp.R())
    out["E2_star_5_leaves_weight_4"] = dict(
        F=ptrim(F), half_gamma_F_degree_8=half_gamma(F, 8), F_in_cone=in_cone(F, 8),
        E=ptrim(E), E_in_cone=in_cone(E, 8), Lambda_in_cone=in_cone(Lambda(T, 0), 8),
        R_in_cone=in_cone(T.R(), 7))
    T = star(6, 0, [3] * 6)
    F = T.F(0)
    out["E2_star_6_leaves_weight_3"] = dict(F=ptrim(F), leading_coefficient=F[-1], F_in_cone=in_cone(F, 9),
                                             Lambda_in_cone=in_cone(Lambda(T, 0), 9))
    T = star(4, 0, [4] * 4)
    Sp = S_poly(T, 0, 0)
    out["S_star_4_leaves_weight_4_u_v_centre"] = dict(S=ptrim(Sp), half_gamma_degree_8=half_gamma(Sp, 8), S_in_cone=in_cone(Sp, 8))
    return out


def git(*a):
    try:
        return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:  # noqa: BLE001
        return "unavailable"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-order", type=int, default=5)
    ap.add_argument("--max-weight", type=int, default=2)
    ap.add_argument("--max-merge", type=int, default=3)
    ap.add_argument("--star-leaves", type=int, default=6)
    ap.add_argument("--star-weight", type=int, default=6)
    ap.add_argument("--random-trials", type=int, default=1500)
    ap.add_argument("--random-order", type=int, default=9)
    ap.add_argument("--seed", type=int, default=20261126)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    start = time.time()
    res = dict(
        part_A_B=part_A(args.max_order, args.max_weight, args.max_merge),
        part_C=part_C(args.star_leaves, args.star_weight),
        part_D=part_D(args.random_trials, args.random_order, args.seed),
        named_examples=named_examples(),
    )
    res["provenance"] = dict(
        command=" ".join(sys.argv), revision=git("rev-parse", "HEAD"),
        dirty_tree=bool(git("status", "--porcelain")), python=sys.version.split()[0],
        networkx=nx.__version__, seconds=round(time.time() - start, 1), arguments=vars(args),
    )
    text = json.dumps(res, indent=1)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    print(text)
