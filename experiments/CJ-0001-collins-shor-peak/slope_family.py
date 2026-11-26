"""CJ-0001, objective O7: the polynomial F(T, nu, u), its leaf recurrences and the
slope statement (S). Exact integer arithmetic throughout; finite checks only.

Notation of notes/gamma-components.md. A weighted tree is a tree T on j >= 1
vertices with an integer weight nu >= 0 on its vertices; k_v is the degree of v
in T, M(T, nu) = I + x (L_T + diag nu), Phi(T, nu) = det M(T, nu),
p_v = 1 + (2 - k_v - nu_v) x, pi_u(T, nu) = e_u^T adj(M(T, nu)) p. C_d is the cone
of the polynomials with a non-negative half-gamma expansion of degree d, that is

    sum_{2e < d} rho_e x^e (1+x)^(d-2e) + sum_{d <= 2e <= 2d} sigma_e x^e,   rho_e, sigma_e >= 0

(the function half_gamma of component_form.py, copied here). The object is

    F(T, nu, u) = (1 + 5x + 3x^2) Phi(T, nu) + (x + 4x^2) adj(M(T, nu))_uu + 2 x^2 pi_u(T, nu).

Search space. For every j with 1 <= j <= --max-order: one tree per isomorphism
class (networkx.nonisomorphic_trees; the single vertex for j = 1), with the
vertex labels 0..j-1 of networkx, and EVERY weight nu in {0..--max-weight}^j on
those labelled vertices, nu = 0 included. Weightings that differ by an
automorphism of the tree are counted separately, and so are the vertices u, v.

(1) Statement (E''), extended to nu = 0: for every vertex u, is F(T, nu, u) in
    C_{j+2}? Cases and failures are counted separately for nu = 0 and nu != 0.

(2) For every leaf w of T (j >= 2) and every vertex u != w, with v the
    neighbour of w, n = nu_w, m = 1 + (1+n)x, theta = x(1 + nx), T - w carrying
    the restriction of nu:
    (2a) v != u:  F(T, nu, u) = m F(T-w, nu, u)
                               + theta F(T_c, nu + e_{v_c}, u) prod_{l != c} Phi_l
                               - 4 n x^4 adj(M(T-w, nu))_uv,
         where T_1..T_q are the components of T - w - v, v_l is the vertex of
         T_l adjacent to v, Phi_l = Phi(T_l, nu + e_{v_l}), and T_c contains u;
    (2b) v = u:   F(T, nu, u) = m F(T-w, nu, u)
                               + [x + (5+n)x^2 + (3+5n)x^3 - n x^4] adj(M(T-w, nu))_uu;
    (2c) slope:   F(T, nu, u) - F(T, nu - e_w, u)
                    = x [F(T-w, nu + e_v, u) - 2 x^3 adj(M(T-w, nu))_uv]   for nu_w >= 1.
         The right-hand side does not involve nu_w, so (2c) on the whole range
         says that F is affine in nu_w on {0..--max-weight}. The script checks
         it in the forward form: for nu_w <= max-weight - 1 it compares
         F(T, nu + e_w, u) - F(T, nu, u) with the right-hand side. This is the
         same set of cases (substitute nu + e_w for nu).

(3) Statement (S): for all vertices u, v of T (u = v included), is
        S(T, nu, u, v) = x [F(T, nu + e_v, u) - 2 x^3 adj(M(T, nu))_uv]
    in C_{j+3}? Recorded in addition: whether the bracket
    F(T, nu + e_v, u) - 2 x^3 adj(M(T, nu))_uv is in C_{j+2} (which implies (S),
    because x C_d is contained in C_{d+1}) and whether it is in C_{j+3}.

det and adj of I + xL come from the Faddeev-LeVerrier recursion for the integer
matrix L; the divisions by k are exact and asserted to be. Every polynomial is a
list of Python integers, lowest degree first. No floating point is used.

These are finite exact checks on the range stated. They are evidence, not proof,
for (E'') and (S); the identities of (2) are confirmed on that range only.

Command of the stored run:

    uv run python experiments/CJ-0001-collins-shor-peak/slope_family.py --max-order 6 --max-weight 4 --out experiments/CJ-0001-collins-shor-peak/results/slope-family.json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from itertools import product
from math import comb
from pathlib import Path

import networkx as nx

MAX_EXAMPLES = 5


# ---------- integer polynomials as lists (copied from component_form.py) ----------
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
    """Phi = det(I + xL) (list) and adj(I + xL) (matrix of lists), L an integer matrix.

    Faddeev-LeVerrier, as in component_form.py; the product L N only visits the
    non-zero entries of each row of L, which changes nothing in the result.
    """
    n = len(L)
    if n == 0:
        return [1], []
    rows = [[(m, L[i][m]) for m in range(n) if L[i][m]] for i in range(n)]
    N = [[1 if i == k else 0 for k in range(n)] for i in range(n)]
    coeffs = [1]
    mats = [N]
    for k in range(1, n + 1):
        LN = [[sum(val * N[m][c] for m, val in rows[i]) for c in range(n)] for i in range(n)]
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


# ---------- weighted trees ----------
def trees_of_order(j):
    """One tree per isomorphism class on j vertices (labels 0..j-1)."""
    return [nx.empty_graph(1)] if j == 1 else list(nx.nonisomorphic_trees(j))


def neighbours(T):
    return {v: sorted(T.neighbors(v)) for v in T.nodes()}


def weighted_data(nbrs, verts, nu):
    """Phi, adj and F for the subtree induced by `verts` with the weights `nu`.

    nbrs: adjacency of the ambient tree (dict vertex -> list of neighbours);
    verts: tuple of vertices inducing a connected subgraph; nu: tuple of
    integer weights aligned with verts. Degrees are taken in the induced
    subtree. Returns (phi, adj, F): adj[a][b] is the entry of adj(M) at
    (verts[a], verts[b]) and F[a] = F(T[verts], nu, verts[a]).
    """
    k = len(verts)
    idx = {v: i for i, v in enumerate(verts)}
    L = [[0] * k for _ in range(k)]
    for v in verts:
        i = idx[v]
        deg = 0
        for u in nbrs[v]:
            if u in idx:
                L[i][idx[u]] = -1
                deg += 1
        L[i][i] = deg + nu[i]
    phi, adj = det_adj(L)
    p = [[1, 2 - L[i][i]] for i in range(k)]  # p_v = 1 + (2 - k_v - nu_v) x
    base = pmul([1, 5, 3], phi)
    F = []
    for a in range(k):
        pi = []
        for b in range(k):
            pi = padd(pi, pmul(adj[a][b], p[b]))
        F.append(padd(padd(base, pmul([0, 1, 4], adj[a][a])), [0, 0] + pscale(pi, 2)))
    return phi, adj, F


def F_value(edges, nu, u):
    """F(T, nu, u) for the tree with vertices 0..len(nu)-1 and the given edges (convenience, for tests)."""
    j = len(nu)
    nbrs = {v: [] for v in range(j)}
    for a, b in edges:
        nbrs[a].append(b)
        nbrs[b].append(a)
    return ptrim(weighted_data(nbrs, tuple(range(j)), tuple(nu))[2][u])


def leaf_structure(nbrs, verts):
    """For every leaf w: (w, v, T - w, components of T - w - v with their vertex adjacent to v)."""
    out = []
    if len(verts) < 2:
        return out
    for w in verts:
        if len(nbrs[w]) != 1:
            continue
        v = nbrs[w][0]
        o1 = tuple(x for x in verts if x != w)
        rest = set(o1) - {v}
        comps = []
        while rest:
            start = min(rest)
            comp = {start}
            stack = [start]
            while stack:
                a = stack.pop()
                for b in nbrs[a]:
                    if b in rest and b not in comp:
                        comp.add(b)
                        stack.append(b)
            rest -= comp
            comp_t = tuple(sorted(comp))
            attach = [x for x in comp_t if v in nbrs[x]]
            assert len(attach) == 1
            comps.append((comp_t, attach[0]))
        out.append((w, v, o1, comps))
    return out


def empty_result():
    return {
        "E2": dict(
            cases_nu_zero=0, failures_nu_zero=0, cases_nu_nonzero=0, failures_nu_nonzero=0, failure_examples=[],
            smallest_failure=None,
        ),
        "leaf": dict(
            leaf_cases=0,
            cases_v_ne_u=0, identity_failures_v_ne_u=0,
            cases_v_eq_u=0, identity_failures_v_eq_u=0,
            slope_cases=0, slope_identity_failures=0,
            failure_examples=[],
        ),
        "S": dict(
            cases=0, cases_u_eq_v=0, cases_nu_zero=0,
            failures=0, failures_u_eq_v=0, failures_nu_zero=0, failure_examples=[],
            smallest_failure=None, failures_by_tree=[],
            bracket_not_in_C_j_plus_2=0, bracket_not_in_C_j_plus_2_examples=[],
            bracket_not_in_C_j_plus_3=0, bracket_not_in_C_j_plus_3_examples=[],
        ),
        "trees": 0,
        "weighted_trees": 0,
        "by_order": {},
    }


def check_tree(T, W, res, cnt, deadline=None):
    """All checks for one tree. Returns False if the deadline was reached before the end."""
    verts = tuple(sorted(T.nodes()))
    j = len(verts)
    assert verts == tuple(range(j))
    nbrs = neighbours(T)
    edges = [list(e) for e in T.edges()]
    leaves = leaf_structure(nbrs, verts)
    e2, lf, st = res["E2"], res["leaf"], res["S"]

    sub_memo = {}

    def sub(vs, ws):
        key = (vs, ws)
        hit = sub_memo.get(key)
        if hit is None:
            hit = sub_memo[key] = weighted_data(nbrs, vs, ws)
        return hit

    g_memo = {}

    def g_terms(w, v, comps, nu):
        """u -> F(T_c, nu + e_{v_c}, u) prod_{l != c} Phi_l for the components of T - w - v."""
        key = (w, tuple(nu[x] for comp, _ in comps for x in comp))
        hit = g_memo.get(key)
        if hit is None:
            data = [sub(comp, tuple(nu[x] + (1 if x == vl else 0) for x in comp)) for comp, vl in comps]
            hit = {}
            for c, (comp, _) in enumerate(comps):
                others = [1]
                for l, d in enumerate(data):
                    if l != c:
                        others = pmul(others, d[0])
                for a, u in enumerate(comp):
                    hit[u] = pmul(data[c][2][a], others)
            g_memo[key] = hit
        return hit

    # data of (T, nu') computed ahead of the main loop (nu' = nu + e_v inside the range);
    # an entry is removed when the main loop reaches nu' (every use of it comes earlier,
    # because nu' - e_v precedes nu' in the lexicographic order of itertools.product).
    ahead = {}
    tree_failures = 0
    tree_cases_before = st["cases"]

    for nu in product(range(W + 1), repeat=j):
        if deadline is not None and time.time() > deadline:
            return False
        data = ahead.pop(nu, None)
        if data is None:
            data = weighted_data(nbrs, verts, nu)
        phi, adj, F = data
        res["weighted_trees"] += 1
        cnt["weighted_trees"] += 1
        zero = not any(nu)

        # (1) F(T, nu, u) in C_{j+2}
        for u in verts:
            ok = hg_ok(F[u], j + 2)
            if zero:
                e2["cases_nu_zero"] += 1
                e2["failures_nu_zero"] += 0 if ok else 1
            else:
                e2["cases_nu_nonzero"] += 1
                e2["failures_nu_nonzero"] += 0 if ok else 1
            cnt["E2_cases"] += 1
            if not ok:
                cnt["E2_failures"] += 1
                example = dict(order=j, edges=edges, nu=list(nu), u=u, F=ptrim(F[u]),
                               half_gamma=half_gamma(F[u], j + 2))
                if len(e2["failure_examples"]) < MAX_EXAMPLES:
                    e2["failure_examples"].append(example)
                best = e2["smallest_failure"]
                if best is None or [j, sum(nu), max(nu)] < [best["order"], sum(best["nu"]), max(best["nu"])]:
                    e2["smallest_failure"] = example

        # (3) S(T, nu, u, v) = x [F(T, nu + e_v, u) - 2 x^3 adj(M(T, nu))_uv] in C_{j+3}
        raised = []
        for v in verts:
            nu_v = nu[:v] + (nu[v] + 1,) + nu[v + 1:]
            if nu[v] + 1 <= W:
                d = ahead.get(nu_v)
                if d is None:
                    d = ahead[nu_v] = weighted_data(nbrs, verts, nu_v)
                Fr = d[2]
            else:
                Fr = weighted_data(nbrs, verts, nu_v)[2]  # used by this nu only
            raised.append(Fr)
            for u in verts:
                bracket = padd(Fr[u], [0, 0, 0] + pscale(adj[u][v], -2))
                s_poly = [0] + bracket
                st["cases"] += 1
                cnt["S_cases"] += 1
                if u == v:
                    st["cases_u_eq_v"] += 1
                if zero:
                    st["cases_nu_zero"] += 1
                if not hg_ok(s_poly, j + 3):
                    st["failures"] += 1
                    cnt["S_failures"] += 1
                    if u == v:
                        st["failures_u_eq_v"] += 1
                    if zero:
                        st["failures_nu_zero"] += 1
                    tree_failures += 1
                    example = None
                    if len(st["failure_examples"]) < MAX_EXAMPLES:
                        example = dict(order=j, edges=edges, nu=list(nu), u=u, v=v, S=ptrim(s_poly),
                                       half_gamma=half_gamma(s_poly, j + 3))
                        st["failure_examples"].append(example)
                    # smallest failure: least order, then least total weight, then least largest weight
                    # (first one met in the enumeration among equals)
                    size = [j, sum(nu), max(nu)]
                    best = st["smallest_failure"]
                    if best is None or size < [best["order"], sum(best["nu"]), max(best["nu"])]:
                        st["smallest_failure"] = example or dict(
                            order=j, edges=edges, nu=list(nu), u=u, v=v, S=ptrim(s_poly),
                            half_gamma=half_gamma(s_poly, j + 3))
                if not hg_ok(bracket, j + 2):
                    st["bracket_not_in_C_j_plus_2"] += 1
                    cnt["bracket_not_in_C_j_plus_2"] += 1
                    if len(st["bracket_not_in_C_j_plus_2_examples"]) < MAX_EXAMPLES:
                        st["bracket_not_in_C_j_plus_2_examples"].append(dict(
                            order=j, edges=edges, nu=list(nu), u=u, v=v, bracket=ptrim(bracket),
                            half_gamma=half_gamma(bracket, j + 2)))
                if not hg_ok(bracket, j + 3):
                    st["bracket_not_in_C_j_plus_3"] += 1
                    cnt["bracket_not_in_C_j_plus_3"] += 1
                    if len(st["bracket_not_in_C_j_plus_3_examples"]) < MAX_EXAMPLES:
                        st["bracket_not_in_C_j_plus_3_examples"].append(dict(
                            order=j, edges=edges, nu=list(nu), u=u, v=v, bracket=ptrim(bracket),
                            half_gamma=half_gamma(bracket, j + 3)))

        # (2) removal of a leaf w != u
        for w, v, o1, comps in leaves:
            n = nu[w]
            nu1 = tuple(nu[x] for x in o1)
            _, adjX, F1 = sub(o1, nu1)
            F1p = sub(o1, tuple(nu[x] + (1 if x == v else 0) for x in o1))[2]
            i1 = {x: i for i, x in enumerate(o1)}
            m = [1, 1 + n]
            theta = [0, 1, n]
            G = g_terms(w, v, comps, nu) if comps else {}
            for u in o1:
                lf["leaf_cases"] += 1
                cnt["leaf_cases"] += 1
                a_uv = adjX[i1[u]][i1[v]]
                if u != v:
                    lf["cases_v_ne_u"] += 1
                    rhs = padd(padd(pmul(m, F1[i1[u]]), pmul(theta, G[u])), [0, 0, 0, 0] + pscale(a_uv, -4 * n))
                    key = "identity_failures_v_ne_u"
                else:
                    lf["cases_v_eq_u"] += 1
                    rhs = padd(pmul(m, F1[i1[u]]), pmul([0, 1, 5 + n, 3 + 5 * n, -n], a_uv))
                    key = "identity_failures_v_eq_u"
                if not peq(F[u], rhs):
                    lf[key] += 1
                    cnt["leaf_identity_failures"] += 1
                    if len(lf["failure_examples"]) < MAX_EXAMPLES:
                        lf["failure_examples"].append(dict(
                            kind=key, order=j, edges=edges, nu=list(nu), u=u, w=w, v=v,
                            F=ptrim(F[u]), claimed=ptrim(rhs)))
                if n + 1 <= W:
                    # slope, forward form: the case (T, nu + e_w, w, u) of (2c)
                    lf["slope_cases"] += 1
                    cnt["slope_cases"] += 1
                    slope = [0] + padd(F1p[i1[u]], [0, 0, 0] + pscale(a_uv, -2))
                    diff = padd(raised[w][u], pscale(F[u], -1))
                    if not peq(diff, slope):
                        lf["slope_identity_failures"] += 1
                        cnt["slope_identity_failures"] += 1
                        if len(lf["failure_examples"]) < MAX_EXAMPLES:
                            nu_up = list(nu)
                            nu_up[w] += 1
                            lf["failure_examples"].append(dict(
                                kind="slope_identity_failures", order=j, edges=edges, nu=nu_up, u=u, w=w, v=v,
                                difference=ptrim(diff), claimed=ptrim(slope)))
    assert not ahead
    if tree_failures:
        st["failures_by_tree"].append(dict(
            order=j, edges=edges, cases=st["cases"] - tree_cases_before, failures=tree_failures))
    return True


ORDER_KEYS = (
    "trees", "weighted_trees", "E2_cases", "E2_failures", "leaf_cases", "leaf_identity_failures",
    "slope_cases", "slope_identity_failures", "S_cases", "S_failures",
    "bracket_not_in_C_j_plus_2", "bracket_not_in_C_j_plus_3",
)


def run(max_order, max_weight, time_limit=None):
    """Run every check for 1 <= j <= max_order and weights 0..max_weight. Returns the result dictionary."""
    start = time.time()
    deadline = None if time_limit is None else start + time_limit
    res = empty_result()
    complete = True
    stopped_at = None
    for j in range(1, max_order + 1):
        cnt = dict.fromkeys(ORDER_KEYS, 0)
        res["by_order"][str(j)] = cnt
        for index, T in enumerate(trees_of_order(j)):
            if not check_tree(T, max_weight, res, cnt, deadline):
                complete = False
                stopped_at = dict(order=j, tree_index=index, edges=[list(e) for e in T.edges()])
                break
            res["trees"] += 1
            cnt["trees"] += 1
        if not complete:
            break
    res["complete"] = complete
    res["stopped_at"] = stopped_at
    res["seconds"] = round(time.time() - start, 1)
    return res


def git(*a):
    try:
        root = Path(__file__).resolve().parents[2]
        return subprocess.run(["git", *a], capture_output=True, text=True, check=True, cwd=root).stdout.strip()
    except Exception:  # noqa: BLE001
        return "unavailable"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--max-order", type=int, default=6)
    ap.add_argument("--max-weight", type=int, default=4)
    ap.add_argument("--time-limit", type=float, default=600.0,
                    help="seconds of wall-clock; the run stops there and records how far it got")
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    res = run(args.max_order, args.max_weight, args.time_limit)
    seconds = res.pop("seconds")
    res["search_space"] = (
        "one tree per isomorphism class with 1..max_order vertices (networkx.nonisomorphic_trees; the single "
        "vertex for order 1), every weight in {0..max_weight}^j on its labelled vertices (zero included; "
        "weightings equivalent under automorphisms counted separately), every vertex u; for (2) every leaf "
        "w != u; for (3) every ordered pair (u, v), u = v included"
    )
    res["provenance"] = dict(
        command=" ".join(sys.argv if argv is None else ["slope_family.py", *argv]),
        revision=git("rev-parse", "HEAD"),
        dirty_tree=bool(git("status", "--porcelain")), python=sys.version.split()[0],
        networkx=nx.__version__, seconds=seconds, arguments=vars(args),
    )
    text = json.dumps(res, indent=1)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    print(text)
    failures = (
        res["leaf"]["identity_failures_v_ne_u"] + res["leaf"]["identity_failures_v_eq_u"]
        + res["leaf"]["slope_identity_failures"]
    )
    return 0 if res["complete"] and failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
