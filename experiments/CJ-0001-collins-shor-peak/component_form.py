"""CJ-0001, session 7: real roots of r_A, the component form of Gamma, and the
companion recurrence for the adjugate (exact integer arithmetic throughout).

Notation of notes/skeleton-locality.md, notes/gamma-reduction.md and
notes/gamma-components.md. Polynomials are lists of Python integers (lowest
degree first). det(I + xL) and adj(I + xL) are obtained from the
Faddeev-LeVerrier recursion for the integer matrix L (exact; the divisions by
k are exact and are asserted to be).

Part 1 (skeletons). For every tree S with 2 to --max-skeleton vertices (one per
isomorphism class, enumeration of networkx) and every A with 1 <= |A| <= s-1:
  r_A is computed as the second form of Proposition S7 (it is compared with
  the definition by locality_check.py, not here), and the script checks
  (1a) all roots of r_A are real and negative, and deg r_A = t + 1
       (Sturm sequence of the square-free part, exact);
  (1b) lead(r_A) = (s+3) det(L_B) - tau_B^T adj(L_B) tau_B, and
       lead(r_A) >= 4 det(L_B) with equality exactly when |A| = 1;
  (1c) for |A| >= 2: (lead(r_A)/det(L_B) - 4) * (1^T adj(P_A) 1) = 2 det(P_A),
       P_A the distance matrix of S restricted to A;
  (1d) for A independent: r_A = (1+4x) Phi_B + sum_i R_i prod_{l != i} Phi_l
       over the components of S[B], and whether each R_i has a non-negative
       half-gamma expansion of degree t_i + 1.

Part 2 (weighted trees). For every tree T with 1 to --max-component vertices
and every integer weight nu in {0..--max-weight}^j, nu != 0:
  (2a) whether R(T, nu) = Phi [(N-1)(1+x) + (j-4+3N)x] - x^2 Q has a
       non-negative half-gamma expansion of degree j + 1;
  (2b) for every leaf w such that nu != 0 on T - w: the companion recurrence
       for every entry of adj(M), and whether
       Delta = R(T, nu) - (1 + (1+nu_w)x) R(T - w, nu) has a non-negative
       half-gamma expansion of degree j + 1.

Part 3 (same loop, trees with at most --max-component3 vertices): with
n = nu_w, T' = T - w, u the neighbour of w, Psi = adj(M(T', nu))_uu,
pi' = e_u^T adj(M(T', nu)) p(T', nu), p_v = 1 + (2 - g_v) x:
  (3a) R(T, nu) = (N + j - 1)(1+x) Phi - p^T adj(M) p          (third form);
  (3b) R(T, nu) = R0 + n E + n(n-1) x Phi(T', nu + e_u), where
       R0 = (1+x) R(T', nu) + x [nu_u (1+x) Psi + sum_i R_i prod_{l != i} Phi_l],
       E  = (1+x) Phi(T, nu with nu_w = 0) + x R(T', nu + e_u) + Estar,
       Estar = 2 x^2 pi' + (3x + 2x^2) Phi(T', nu) + 3 x^2 Psi;
  (3c) whether R0, E, E - x R(T', nu + e_u) and Estar have non-negative half-gamma
       expansions of degree j + 1.

Command:

    uv run python experiments/CJ-0001-collins-shor-peak/component_form.py --max-skeleton 8 --max-component 7 --max-weight 2 --out experiments/CJ-0001-collins-shor-peak/results/component-form.json
"""
import argparse
import json
import subprocess
import sys
import time
from fractions import Fraction
from itertools import combinations, product
from math import comb

import networkx as nx

ap = argparse.ArgumentParser()
ap.add_argument("--max-skeleton", type=int, default=8)
ap.add_argument("--max-component", type=int, default=7)
ap.add_argument("--max-weight", type=int, default=2)
ap.add_argument("--max-component3", type=int, default=6)
ap.add_argument("--out", default=None)
args = ap.parse_args()
start = time.time()


# ---------- integer polynomials as lists ----------
def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]


def pscale(p, c):
    return [c * v for v in p]


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
    assert len(c) <= d + 1
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


def hg_ok(c, d):
    return min(half_gamma(c, d)) >= 0


# ---------- det and adjugate of I + xL ----------
def det_adj(L):
    """Phi = det(I + xL) (list) and adj(I + xL) (matrix of lists), L an integer matrix."""
    n = len(L)
    if n == 0:
        return [1], []
    ident = [[1 if i == k else 0 for k in range(n)] for i in range(n)]
    N = ident
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


def quad(adj, p, q):
    n = len(p)
    r = []
    for i in range(n):
        for c in range(n):
            if p[i] and q[c]:
                r = padd(r, pscale(adj[i][c], p[i] * q[c]))
    return r


def int_det(M):
    n = len(M)
    if n == 0:
        return Fraction(1)
    A = [[Fraction(v) for v in row] for row in M]
    d = Fraction(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if A[r][i] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            d = -d
        d *= A[i][i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            if f:
                for c in range(i, n):
                    A[r][c] -= f * A[i][c]
    return d


def int_adj(M):
    n = len(M)
    out = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        for c in range(n):
            minor = [[M[r][k] for k in range(n) if k != i] for r in range(n) if r != c]
            out[i][c] = (-1) ** (i + c) * int_det(minor)
    return out


# ---------- Sturm sequences (rational) ----------
def fdivmod(p, q):
    p = [Fraction(v) for v in p]
    q = ptrim(q)
    quo = [Fraction(0)] * max(len(p) - len(q) + 1, 1)
    while len(ptrim(p)) >= len(q):
        p = ptrim(p)
        k = len(p) - len(q)
        f = p[-1] / q[-1]
        quo[k] = f
        for i, v in enumerate(q):
            p[i + k] -= f * v
    return ptrim(quo), ptrim(p)


def fgcd(p, q):
    p, q = ptrim(p), ptrim(q)
    while q:
        p, q = q, fdivmod(p, q)[1]
    return p


def pderiv(p):
    return [i * p[i] for i in range(1, len(p))]


def sign_at(p, where):
    """Sign of p at 0 (where = 0) or at -infinity (where = -1)."""
    p = ptrim(p)
    if not p:
        return 0
    if where == 0:
        return (p[0] > 0) - (p[0] < 0)
    s = (p[-1] > 0) - (p[-1] < 0)
    return s if (len(p) - 1) % 2 == 0 else -s


def negative_real_roots(p):
    """(degree of the square-free part, number of its roots in (-infinity, 0))."""
    p = ptrim([Fraction(v) for v in p])
    g = fgcd(p, pderiv(p))
    sq = fdivmod(p, g)[0] if len(g) > 1 else p
    seq = [sq, pderiv(sq)]
    while ptrim(seq[-1]):
        rem = fdivmod(seq[-2], seq[-1])[1]
        seq.append([-v for v in rem])
    seq = [q for q in seq if ptrim(q)]

    def changes(where):
        signs = [s for s in (sign_at(q, where) for q in seq) if s != 0]
        return sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])

    return len(sq) - 1, changes(-1) - changes(0)


# ---------- weighted trees ----------
def weighted(T, order, nu):
    """Phi, adj, z, Q, R for the tree T (networkx) with vertex order and weights nu (dict)."""
    j = len(order)
    idx = {v: i for i, v in enumerate(order)}
    L = [[0] * j for _ in range(j)]
    for v in order:
        L[idx[v]][idx[v]] = T.degree(v) + nu[v]
    for u, v in T.edges():
        L[idx[u]][idx[v]] = L[idx[v]][idx[u]] = -1
    phi, adj = det_adj(L)
    z = [T.degree(v) + 2 * nu[v] - 2 for v in order]
    Q = quad(adj, z, z)
    N = sum(nu[v] for v in order)
    bracket = [N - 1, (N - 1) + (j - 4 + 3 * N)]
    R = padd(pmul(phi, bracket), pscale([0, 0] + Q, -1))
    return phi, adj, z, Q, R, L


res = {"part1": {}, "part2": {}}

# ---------- Part 1 ----------
p1 = dict(
    trees=0, subsets=0, not_all_real_negative=0, degree_not_t_plus_1=0, lead_identity_failures=0,
    kappa_below_4=0, kappa_equal_4_with_a_at_least_2=0, kappa_not_4_with_a_1=0,
    magnitude_identity_failures=0, magnitude_cases=0,
    independent_A=0, component_identity_failures=0, components=0, component_R_not_in_cone=0,
    min_kappa_minus_4_num_den=None,
)
min_k4 = None
for s in range(2, args.max_skeleton + 1):
    for S in nx.nonisomorphic_trees(s):
        p1["trees"] += 1
        V = list(S.nodes())
        dist = dict(nx.all_pairs_shortest_path_length(S))
        g = {v: S.degree(v) for v in V}
        for a in range(1, s):
            for A in combinations(V, a):
                p1["subsets"] += 1
                Aset = set(A)
                B = [v for v in V if v not in Aset]
                t = len(B)
                idx = {v: i for i, v in enumerate(B)}
                LB = [[0] * t for _ in range(t)]
                for v in B:
                    LB[idx[v]][idx[v]] = g[v]
                eB = 0
                for u, v in S.edges():
                    if u in idx and v in idx:
                        LB[idx[u]][idx[v]] = LB[idx[v]][idx[u]] = -1
                        eB += 1
                phi, adj = det_adj(LB)
                k = {v: sum(1 for u in S.neighbors(v) if u in idx) for v in B}
                z = [2 * (g[v] - 1) - k[v] for v in B]
                H = sum(g[v] - 1 for v in B)
                beta = 3 + 3 * H - 2 * eB
                Q = quad(adj, z, z)
                r = ptrim(padd(pmul(phi, [a, a + beta]), pscale([0, 0] + Q, -1)))
                # (1a)
                if len(r) - 1 != t + 1:
                    p1["degree_not_t_plus_1"] += 1
                dsq, nneg = negative_real_roots(r)
                if nneg != dsq:
                    p1["not_all_real_negative"] += 1
                # (1b)
                detL = phi[t]
                adjL = [[adj[i][c][t - 1] for c in range(t)] for i in range(t)]
                tau = [2 - g[v] for v in B]
                tAt = sum(tau[i] * adjL[i][c] * tau[c] for i in range(t) for c in range(t))
                lead = r[-1] if len(r) == t + 2 else 0
                if lead != (s + 3) * detL - tAt:
                    p1["lead_identity_failures"] += 1
                if lead < 4 * detL:
                    p1["kappa_below_4"] += 1
                if lead == 4 * detL and a >= 2:
                    p1["kappa_equal_4_with_a_at_least_2"] += 1
                if lead != 4 * detL and a == 1:
                    p1["kappa_not_4_with_a_1"] += 1
                # (1c)
                if a >= 2:
                    p1["magnitude_cases"] += 1
                    PA = [[dist[u][v] for v in A] for u in A]
                    dP = int_det(PA)
                    aP = int_adj(PA)
                    one_adj_one = sum(sum(row) for row in aP)
                    k4 = Fraction(lead, detL) - 4
                    if k4 * one_adj_one != 2 * dP:
                        p1["magnitude_identity_failures"] += 1
                    if min_k4 is None or k4 < min_k4:
                        min_k4 = k4
                # (1d)
                if not any(S.has_edge(u, v) for u, v in combinations(A, 2)):
                    p1["independent_A"] += 1
                    comps = [sorted(c) for c in nx.connected_components(S.subgraph(B))]
                    pieces = []
                    for comp in comps:
                        Tc = S.subgraph(comp)
                        nu = {v: g[v] - k[v] for v in comp}
                        ph, _, _, _, R, _ = weighted(Tc, comp, nu)
                        pieces.append((ph, R, len(comp)))
                        p1["components"] += 1
                        if not hg_ok(R, len(comp) + 1):
                            p1["component_R_not_in_cone"] += 1
                    total = pmul([1, 4], phi)
                    for i, (ph, R, _) in enumerate(pieces):
                        term = R
                        for l, (ph2, _, _) in enumerate(pieces):
                            if l != i:
                                term = pmul(term, ph2)
                        total = padd(total, term)
                    if not peq(total, r):
                        p1["component_identity_failures"] += 1
p1["min_kappa_minus_4_num_den"] = [min_k4.numerator, min_k4.denominator] if min_k4 is not None else None
res["part1"] = p1

# ---------- Part 2 ----------
p2 = dict(
    weighted_trees=0, R_not_in_cone=0, R_failures_examples=[],
    leaf_cases=0, recurrence_failures=0, delta_not_in_cone=0,
    trees_with_no_good_leaf=0, trees_with_some_bad_leaf=0, delta_failure_examples=[],
    by_order={},
    part3_leaf_cases=0, part3_weight_formula_failures=0, part3_R0_not_in_cone=0, part3_E_not_in_cone=0, part3_E_minus_xR_not_in_cone=0,
    part3_estar_not_in_cone=0, part3_estar_examples=[], part3_third_form_failures=0,
)
for j in range(1, args.max_component + 1):
    trees = [nx.empty_graph(1)] if j == 1 else list(nx.nonisomorphic_trees(j))
    cnt = dict(weighted_trees=0, R_not_in_cone=0, leaf_cases=0, delta_not_in_cone=0)
    for T in trees:
        order = list(T.nodes())
        for w_tuple in product(range(args.max_weight + 1), repeat=j):
            if not any(w_tuple):
                continue
            nu = dict(zip(order, w_tuple))
            phi, adj, z, Q, R, L = weighted(T, order, nu)
            cnt["weighted_trees"] += 1
            if not hg_ok(R, j + 1):
                cnt["R_not_in_cone"] += 1
                if len(p2["R_failures_examples"]) < 5:
                    p2["R_failures_examples"].append(
                        dict(edges=[list(e) for e in T.edges()], nu=list(w_tuple), R=R, half_gamma=half_gamma(R, j + 1)))
            if j == 1:
                continue
            good = bad = 0
            for w in order:
                if T.degree(w) != 1 or not any(nu[v] for v in order if v != w):
                    continue
                cnt["leaf_cases"] += 1
                u = next(iter(T.neighbors(w)))
                o1 = [v for v in order if v != w]
                T1 = T.subgraph(o1)
                phi1, adjX, z1, Q1, R1, _ = weighted(T1, o1, nu)
                # Y: T - w - u with weights nu + e_{u_i}
                o2 = [v for v in o1 if v != u]
                i2 = {v: i for i, v in enumerate(o2)}
                LY = [[0] * len(o2) for _ in o2]
                for v in o2:
                    LY[i2[v]][i2[v]] = T.degree(v) + nu[v]
                for p_, q_ in T.edges():
                    if p_ in i2 and q_ in i2:
                        LY[i2[p_]][i2[q_]] = LY[i2[q_]][i2[p_]] = -1
                psi, adjY = det_adj(LY)
                i0 = {v: i for i, v in enumerate(order)}
                i1 = {v: i for i, v in enumerate(o1)}
                m = [1, 1 + nu[w]]
                th = [0, 1, nu[w]]  # x (1 + nu_w x)
                ok = peq(adj[i0[w]][i0[w]], padd(phi1, [0] + psi))
                ok = ok and peq(psi, adjX[i1[u]][i1[u]])
                ok = ok and peq(phi, padd(pmul(m, phi1), pmul(th, psi)))
                for v in o1:
                    ok = ok and peq(adj[i0[w]][i0[v]], [0] + adjX[i1[u]][i1[v]])
                    for v2 in o1:
                        rhs = pmul(m, adjX[i1[v]][i1[v2]])
                        if v != u and v2 != u:
                            rhs = padd(rhs, pmul(th, adjY[i2[v]][i2[v2]]))
                        ok = ok and peq(adj[i0[v]][i0[v2]], rhs)
                if not ok:
                    p2["recurrence_failures"] += 1
                if j <= args.max_component3:
                    # Part 3: the leaf formula in the weight n = nu_w (notes/gamma-components.md, G3 and G4)
                    p2["part3_leaf_cases"] += 1
                    n = nu[w]
                    comps = [sorted(c) for c in nx.connected_components(T.subgraph(o2))]
                    pcs = []
                    for comp in comps:
                        nuc = {v: nu[v] + (1 if T.has_edge(v, u) else 0) for v in comp}
                        ph, _, _, _, Rc, _ = weighted(T.subgraph(comp), comp, nuc)
                        pcs.append((ph, Rc))
                    S_ = []
                    for i, (_, Rc) in enumerate(pcs):
                        term = Rc
                        for l, (ph2, _) in enumerate(pcs):
                            if l != i:
                                term = pmul(term, ph2)
                        S_ = padd(S_, term)
                    pprime = [[1, 2 - (T1.degree(v) + nu[v])] for v in o1]
                    pi1 = []
                    for v in o1:
                        pi1 = padd(pi1, pmul(adjX[i1[u]][i1[v]], pprime[i1[v]]))
                    nu_plus = dict(nu)
                    nu_plus[u] += 1
                    _, _, _, _, R1plus, _ = weighted(T1, o1, {v: nu_plus[v] for v in o1})
                    phi1plus = padd(phi1, [0] + psi)
                    R0 = padd(pmul([1, 1], R1), [0] + padd(pmul([nu[u], nu[u]], psi), S_))
                    estar = padd(padd(pscale([0, 0] + pi1, 2), pmul([0, 3, 2], phi1)), pscale([0, 0] + psi, 3))
                    phi0 = padd(pmul([1, 1], phi1), [0] + psi)
                    E = padd(padd(pmul([1, 1], phi0), [0] + R1plus), estar)
                    total = padd(padd(R0, pscale(E, n)), pscale([0] + phi1plus, n * (n - 1)))
                    if not peq(total, R):
                        p2["part3_weight_formula_failures"] += 1
                    if not hg_ok(E, j + 1):
                        p2["part3_E_not_in_cone"] += 1
                    if not hg_ok(padd(pmul([1, 1], phi0), estar), j + 1):
                        p2["part3_E_minus_xR_not_in_cone"] += 1
                    if not hg_ok(R0, j + 1):
                        p2["part3_R0_not_in_cone"] += 1
                    if not hg_ok(estar, j + 1):
                        p2["part3_estar_not_in_cone"] += 1
                        if len(p2["part3_estar_examples"]) < 5:
                            p2["part3_estar_examples"].append(
                                dict(edges=[list(e) for e in T1.edges()], vertices=o1, nu=[nu[v] for v in o1],
                                     root=u, estar=ptrim(estar), half_gamma=half_gamma(estar, j + 1)))
                    # third form of R: (N + j - 1)(1+x) Phi - p^T adj p
                    pvec = [[1, 2 - (T.degree(v) + nu[v])] for v in order]
                    Vq = []
                    for a_ in range(j):
                        for b_ in range(j):
                            Vq = padd(Vq, pmul(pmul(pvec[a_], pvec[b_]), adj[a_][b_]))
                    Ntot = sum(w_tuple)
                    if not peq(R, padd(pmul([Ntot + j - 1, Ntot + j - 1], phi), pscale(Vq, -1))):
                        p2["part3_third_form_failures"] += 1
                delta = padd(R, pscale(pmul(m, R1), -1))
                if hg_ok(delta, j + 1):
                    good += 1
                else:
                    bad += 1
                    cnt["delta_not_in_cone"] += 1
                    if len(p2["delta_failure_examples"]) < 5:
                        p2["delta_failure_examples"].append(
                            dict(edges=[list(e) for e in T.edges()], nu=list(w_tuple), leaf=w,
                                 delta=ptrim(delta), half_gamma=half_gamma(delta, j + 1)))
            if good + bad > 0 and good == 0:
                p2["trees_with_no_good_leaf"] += 1
            if bad > 0:
                p2["trees_with_some_bad_leaf"] += 1
    p2["by_order"][str(j)] = cnt
    for key in ("weighted_trees", "R_not_in_cone", "leaf_cases", "delta_not_in_cone"):
        p2[key] += cnt[key]
res["part2"] = p2


def git(*a):
    try:
        return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:  # noqa: BLE001
        return "unavailable"


res["provenance"] = dict(
    command=" ".join(sys.argv), revision=git("rev-parse", "HEAD"),
    dirty_tree=bool(git("status", "--porcelain")), python=sys.version.split()[0],
    networkx=nx.__version__, seconds=round(time.time() - start, 1),
    arguments=vars(args),
)
text = json.dumps(res, indent=1)
if args.out:
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
print(text)
