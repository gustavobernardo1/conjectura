"""Independent exact check of the identities and cone memberships as restated in the
manuscript manuscripts/CJ-0001-collins-shor/main.tex (lower half).

Written from the manuscript's definitions only (not from the notes' code). Polynomials are
lists of Fractions (coefficient of x^k at index k). Matrix polynomials are computed by exact
evaluation at integer points and Lagrange interpolation.
"""
import sys, time
from fractions import Fraction as Fr
from itertools import combinations
import networkx as nx

# ---------- polynomials ----------
def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p

def add(*ps):
    n = max((len(p) for p in ps), default=0)
    return trim([sum((p[i] if i < len(p) else 0) for p in ps) for i in range(n)])

def scal(c, p):
    return trim([c * a for a in p])

def mul(p, q):
    if not p or not q:
        return []
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                r[i + j] += a * b
    return trim(r)

def sub(p, q):
    return add(p, scal(-1, q))

X = [0, 1]
ONE = [1]
def P(*c):
    return trim(list(c))
def xp(k):
    return [0] * k + [1]
def opx(k):  # (1+x)^k
    r = [1]
    for _ in range(k):
        r = mul(r, [1, 1])
    return r

def divx(p):
    assert not p or p[0] == 0
    return trim(p[1:])

def interp(xs, ys):
    """Exact Lagrange interpolation."""
    n = len(xs)
    res = []
    for i in range(n):
        num = [Fr(1)]
        den = Fr(1)
        for j in range(n):
            if j != i:
                num = mul(num, [Fr(-xs[j]), Fr(1)])
                den *= (xs[i] - xs[j])
        res = add(res, scal(Fr(ys[i]) / den, num))
    return res

def kcoords(p, d):
    """Coordinates in the basis {x^e(1+x)^(d-2e): 2e<d} U {x^e: 2e>=d} (any degree);
    K_d is the set where all coordinates are >= 0 (generators x^e(1+x)^i, 2e+i>=d)."""
    c = list(p) + [0] * 2
    out = []
    e = 0
    while 2 * e < d:
        g = c[e] if e < len(c) else 0
        out.append(g)
        b = opx(d - 2 * e)
        for i, bi in enumerate(b):
            while e + i >= len(c):
                c.append(0)
            c[e + i] -= g * bi
        e += 1
    out.extend(c[e:])
    return out

def inK(p, d):
    if d <= 0:
        return all(a >= 0 for a in p)
    return min(kcoords(p, d), default=0) >= 0

# ---------- exact linear algebra on rationals ----------
def det_inv(A):
    n = len(A)
    M = [[Fr(v) for v in row] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    det = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return Fr(0), None
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        inv = 1 / M[c][c]
        M[c] = [v * inv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return det, [row[n:] for row in M]

def det(A):
    if len(A) == 0:
        return Fr(1)
    return det_inv(A)[0]

# ---------- trees ----------
def lap(n, edges):
    L = [[0] * n for _ in range(n)]
    for a, b in edges:
        L[a][a] += 1; L[b][b] += 1; L[a][b] -= 1; L[b][a] -= 1
    return L

def degs(n, edges):
    k = [0] * n
    for a, b in edges:
        k[a] += 1; k[b] += 1
    return k

def dist_from(n, edges, u):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    d = [-1] * n; d[u] = 0; st = [u]
    while st:
        v = st.pop()
        for w in adj[v]:
            if d[w] < 0:
                d[w] = d[v] + 1; st.append(w)
    return d

def poly_of(fun, deg):
    xs = list(range(deg + 2))
    return interp(xs, [fun(Fr(x0)) for x0 in xs])

def rooted_quantities(n, edges, u, w):
    """Psi, Phi_w, pi_w, R_w for the rooted tree with root weight w (manuscript definitions)."""
    L = lap(n, edges); k = degs(n, edges)
    def at(x0):
        M = [[(1 if i == j else 0) + x0 * L[i][j] + (x0 * w if i == j == u else 0) for j in range(n)] for i in range(n)]
        D, Minv = det_inv(M)
        adj = [[D * Minv[i][j] for j in range(n)] for i in range(n)]
        p = [1 + (2 - k[v]) * x0 - (w * x0 if v == u else 0) for v in range(n)]
        pAp = sum(p[i] * adj[i][j] * p[j] for i in range(n) for j in range(n))
        R = (w + n - 1) * (1 + x0) * D - pAp
        pi = sum(adj[u][j] * p[j] for j in range(n))
        sub_ = [[M[i][j] for j in range(n) if j != u] for i in range(n) if i != u]
        Psi = det(sub_)
        return D, pi, R, Psi
    deg = n + 3
    xs = list(range(deg + 2))
    vals = [at(Fr(x0)) for x0 in xs]
    return [interp(xs, [v[t] for v in vals]) for t in range(4)]  # Phi, pi, R, Psi

def ell_direct(n, edges):
    """ell_T = -2^{-(n-2)} det(2xI - D)."""
    D = [dist_from(n, edges, v) for v in range(n)]
    def at(x0):
        A = [[(2 * x0 if i == j else 0) - D[i][j] for j in range(n)] for i in range(n)]
        return -det(A) / Fr(2) ** (n - 2)
    return poly_of(at, n + 1)

def all_trees(n):
    if n == 1:
        yield (1, [])
        return
    for G in nx.nonisomorphic_trees(n):
        yield (n, list(G.edges()))

def rooted_trees(n):
    if n == 1:
        yield (1, [], 0)
        return
    for G in nx.nonisomorphic_trees(n):
        seen = set()
        for u in G.nodes():
            # one representative per isomorphism class of rooted trees (AHU canonical code)
            key = rooted_code(G, u)
            if key in seen:
                continue
            seen.add(key)
            yield (n, list(G.edges()), u)

def rooted_code(G, u, parent=None):
    return "(" + "".join(sorted(rooted_code(G, w, u) for w in G[u] if w != parent)) + ")"

# ---------- state of a rooted tree (manuscript, root weight 0) ----------
def state(n, edges, u):
    Phi0, pi0, R0, Psi = rooted_quantities(n, edges, u, 0)
    Phi1, pi1, R1, Psi_ = rooted_quantities(n, edges, u, 1)
    assert Psi == Psi_
    H = divx(sub(Phi0, Psi))
    G = sub(mul(P(1, 2), Psi), pi0)
    # branches
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    branches = []
    for c in adj[u]:
        # component of T - u containing c
        comp = {c}; st = [c]
        while st:
            v = st.pop()
            for w2 in adj[v]:
                if w2 != u and w2 not in comp:
                    comp.add(w2); st.append(w2)
        idx = {v: i for i, v in enumerate(sorted(comp))}
        e2 = [(idx[a], idx[b]) for a, b in edges if a in comp and b in comp]
        Ph1, _, Rb1, _ = rooted_quantities(len(comp), e2, idx[c], 1)
        branches.append((Ph1, Rb1))
    Psi_b = ONE
    for Ph1, _ in branches:
        Psi_b = mul(Psi_b, Ph1)
    Omega = []
    for i, (Ph1, Rb1) in enumerate(branches):
        t = Rb1
        for l, (Ph1l, _) in enumerate(branches):
            if l != i:
                t = mul(t, Ph1l)
        Omega = add(Omega, t)
    E = add(R0, scal(-1, Omega), mul(P(1, 4, 4), Psi), scal(-2, mul(X, G)))
    return dict(Phi0=Phi0, Phi1=Phi1, pi0=pi0, pi1=pi1, R0=R0, R1=R1, Psi=Psi, Psib=Psi_b,
                H=H, G=G, Omega=Omega, E=E)

def a_polys(n, edges, u, w=0):
    """a_v = x^{delta_v - 1} det M[A \\ path(u,v)] (M with root weight w; minor avoids u)."""
    L = lap(n, edges)
    dl = dist_from(n, edges, u)
    G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(edges)
    out = {}
    for v in range(n):
        if v == u:
            continue
        path = set(nx.shortest_path(G, u, v))
        rest = [i for i in range(n) if i not in path]
        def at(x0):
            M = [[(1 if i == j else 0) + x0 * L[i][j] for j in rest] for i in rest]
            return det(M)
        Pi = poly_of(at, n)
        out[v] = mul(xp(dl[v] - 1), Pi)
    return out, dl

class Tally:
    def __init__(self):
        self.c = {}; self.f = {}; self.first = {}
    def ok(self, name, cond, wit=None):
        self.c[name] = self.c.get(name, 0) + 1
        self.f.setdefault(name, 0)
        if not cond:
            self.f[name] += 1
            self.first.setdefault(name, wit)

def main(maxr=8, maxsm=12, maxmerge=8):
    t0 = time.time(); T = Tally()
    recs = {}
    for a in range(1, maxr + 1):
        for (n, edges, u) in rooted_trees(a):
            s = state(n, edges, u)
            wit = (n, edges, u)
            # (star) for w = 0, 1, 2
            for w in (0, 1, 2):
                Phi, pi, R, Psi = rooted_quantities(n, edges, u, w)
                lhs = mul(Psi, R)
                rhs = sub(mul(Phi, add(scal(w, mul(P(1, 1), Psi)), s["Omega"])), mul(pi, pi))
                T.ok("star(w=%d)" % w, lhs == rhs, wit)
            T.ok("Psi = prod Phi1(branch)", s["Psi"] == s["Psib"], wit)
            # raise identity
            rhs = add(s["R0"], mul(P(1, 4, 4), s["Psi"]), mul(P(0, 1, 1), s["H"]), mul(X, s["Omega"]), scal(-2, mul(X, s["G"])))
            T.ok("raise R1", s["R1"] == rhs, wit)
            T.ok("E = R1 - (1+x)(Omega + xH)", s["E"] == sub(s["R1"], mul(P(1, 1), add(s["Omega"], mul(X, s["H"])))), wit)
            # S33
            av, dl = a_polys(n, edges, u)
            H2 = add(*av.values()) if av else []
            T.ok("H = sum a_v", s["H"] == H2, wit)
            G2 = mul(X, add(*[scal(dl[v] - 1, av[v]) for v in av])) if av else []
            T.ok("G = x sum (delta-1) a_v", s["G"] == G2, wit)
            # R1 = Phi1 sum delta^2 - delta^T adj(M1) delta ; and = Q1 + x^2 sum delta^2 a_v
            L = lap(n, edges)
            def at(x0):
                M = [[(1 if i == j else 0) + x0 * L[i][j] + (x0 if i == j == u else 0) for j in range(n)] for i in range(n)]
                D_, Mi = det_inv(M)
                adj = [[D_ * Mi[i][j] for j in range(n)] for i in range(n)]
                v1 = D_ * sum(d * d for d in dl) - sum(dl[i] * adj[i][j] * dl[j] for i in range(n) for j in range(n))
                q1 = sum((dl[i] - dl[j]) ** 2 * adj[i][j] for i in range(n) for j in range(i + 1, n))
                return v1, q1
            xs = list(range(n + 4)); vals = [at(Fr(z)) for z in xs]
            V1 = interp(xs, [v[0] for v in vals]); Q1 = interp(xs, [v[1] for v in vals])
            T.ok("R1 = variance form", s["R1"] == V1, wit)
            W2 = add(*[scal(dl[v] ** 2, av[v]) for v in av]) if av else []
            T.ok("R1 = Q1 + x^2 W", s["R1"] == add(Q1, mul(xp(2), W2)), wit)
            # memberships
            T.ok("Psi in K_{a-1}", inK(s["Psi"], a - 1), wit)
            T.ok("H in K_{a-2}", inK(s["H"], a - 2), wit)
            T.ok("G/x in K_{a-1}", inK(divx(s["G"]), a - 1), wit)
            T.ok("Omega in K_a", inK(s["Omega"], a), wit)
            T.ok("E in K_{a+1}", inK(s["E"], a + 1), wit)
            T.ok("R1 in K_{a+1}", inK(s["R1"], a + 1), wit)
            T.ok("deg R1 <= a+1", len(s["R1"]) <= a + 2, wit)
            T.ok("Q1 in K_a", inK(Q1, a), wit)
            for v in av:
                T.ok("a_v in K_{a+delta-3}", inK(av[v], a + dl[v] - 3), wit)
            T.ok("Phi1 - (1+x)^a in K_a", inK(sub(s["Phi1"], opx(a)), a), wit)
            # L1 and R0 = x ell - (1+4x) Phi
            ell = ell_direct(n, edges) if n >= 1 else None
            T.ok("R0 = x ell - (1+4x)Phi", s["R0"] == sub(mul(X, ell), mul(P(1, 4), s["Phi0"])), wit)
            # plant
            n2 = n + 1; e2 = edges + [(u, n)]
            sp = state(n2, e2, n) if a <= maxr - 1 else None
            if sp is not None:
                T.ok("plant Psi", sp["Psi"] == s["Phi1"], wit)
                T.ok("plant Omega", sp["Omega"] == s["R1"], wit)
                T.ok("plant H", sp["H"] == s["Phi0"], wit)
                T.ok("plant G", sp["G"] == mul(X, add(mul(X, s["H"]), s["G"])), wit)
                T.ok("plant R0", sp["R0"] == add(mul(P(1, 1), s["R0"]), mul(X, s["Omega"])), wit)
                T.ok("plant Phi0", sp["Phi0"] == add(mul(P(1, 1), s["Phi0"]), mul(X, s["Psi"])), wit)
                Ehat = mul(X, add(s["E"], s["Omega"], scal(2, s["G"]), mul(P(0, 3, 2), s["H"])))
                T.ok("plant E", sp["E"] == Ehat, wit)
                # leaf recursion
                ell2 = ell_direct(n2, e2)
                T.ok("leaf recursion", ell2 == add(mul(P(1, 1), ell), mul(P(1, 4), s["Psi"]), s["Omega"]), wit)
            recs.setdefault(a, []).append((n, edges, u, s, av, dl, Q1))
    # merge and S35 on pairs
    for a1 in range(1, maxmerge):
        for a2 in range(1, maxmerge - a1 + 1):
            if a1 + a2 - 1 > maxmerge:
                continue
            for r1 in recs.get(a1, []):
                for r2 in recs.get(a2, []):
                    n1, e1, u1, s1, av1, dl1, Q11 = r1
                    n2_, e2_, u2, s2, av2, dl2, Q12 = r2
                    # merged: identify u2 with u1
                    off = n1
                    mp = {}
                    k = n1
                    for v in range(n2_):
                        if v == u2:
                            mp[v] = u1
                        else:
                            mp[v] = k; k += 1
                    em = e1 + [(mp[a], mp[b]) for a, b in e2_]
                    sm = state(k, em, u1)
                    wit = (r1[:3], r2[:3])
                    T.ok("merge Psi", sm["Psi"] == mul(s1["Psi"], s2["Psi"]), wit)
                    for key in ("H", "G", "Omega"):
                        T.ok("merge " + key, sm[key] == add(mul(s1[key], s2["Psi"]), mul(s2[key], s1["Psi"])), wit)
                    Rm = add(mul(s1["R0"], s2["Psi"]), mul(s2["R0"], s1["Psi"]),
                             mul(X, add(mul(s1["H"], s2["Omega"]), mul(s2["H"], s1["Omega"]))),
                             mul(P(1, 4, 4), mul(s1["Psi"], s2["Psi"])), scal(-2, mul(s1["G"], s2["G"])))
                    T.ok("merge R0", sm["R0"] == Rm, wit)
                    Em = add(mul(s1["E"], s2["Psi"]), mul(s2["E"], s1["Psi"]),
                             mul(X, add(mul(s1["H"], s2["Omega"]), mul(s2["H"], s1["Omega"]))), scal(-2, mul(s1["G"], s2["G"])))
                    T.ok("merge E", sm["E"] == Em, wit)
                    # S35 for the two planted trees
                    if a1 + a2 + 1 <= maxmerge + 1:
                        H1h = add(s1["Psi"], mul(X, s1["H"])); H2h = add(s2["Psi"], mul(X, s2["H"]))
                        G1h = mul(X, add(mul(X, s1["H"]), s1["G"])); G2h = mul(X, add(mul(X, s2["H"]), s2["G"]))
                        lhs = sub(mul(X, add(mul(H1h, s2["R1"]), mul(H2h, s1["R1"]))), scal(2, mul(G1h, G2h)))
                        sq = []
                        for v in av1:
                            for v2 in av2:
                                sq = add(sq, scal((dl1[v] - dl2[v2]) ** 2, mul(av1[v], av2[v2])))
                        rhs = add(mul(X, add(mul(s1["Psi"], s2["R1"]), mul(s2["Psi"], s1["R1"]))),
                                  mul(xp(2), add(mul(s1["H"], Q12), mul(s2["H"], Q11))), mul(xp(4), sq))
                        T.ok("S35", lhs == rhs, wit)
                        T.ok("S35 cone", inK(lhs, a1 + a2 + 2), wit)
    # star minimality and the lower bound
    for n in range(2, maxsm + 1):
        star = add(mul(scal(n - 1, P(1, 4)), opx(n - 2)), scal(-4, mul(X, opx(n - 1))))
        cnt = 0
        for (nn, edges) in all_trees(n):
            ell = ell_direct(nn, edges)
            diff = sub(ell, star)
            T.ok("SM in K_{n-1}", inK(diff, n - 1), (n, edges))
            T.ok("deg(SM) <= n-2", len(diff) <= n - 1, (n, edges))
            if n >= 3:
                m = n // 2
                lam = (ell[m] if m < len(ell) else 0) - ell[m - 1]
                lams = star[m] - star[m - 1]
                T.ok("d_m - d_{m-1} >= star > 0", lam >= lams > 0, (n, edges))
    elapsed = time.time() - t0
    print("elapsed %.1f s" % elapsed)
    tot = 0; fails = 0
    for k in T.c:
        print("%-32s cases %6d failures %d" % (k, T.c[k], T.f[k]))
        tot += T.c[k]; fails += T.f[k]
        if T.f[k]:
            print("   first:", T.first[k])
    print("TOTAL cases", tot, "failures", fails)
    return {
        "parameters": {"max_rooted": maxr, "max_order_sm": maxsm, "max_merge": maxmerge},
        "checks": {k: {"cases": T.c[k], "failures": T.f[k]} for k in T.c},
        "first_failures": {k: repr(v) for k, v in T.first.items()},
        "cases_total": tot,
        "failures_total": fails,
        "elapsed_seconds": round(elapsed, 1),
    }


def _run_block(argv):
    import platform, subprocess
    def git(*a):
        try:
            return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()
        except Exception:
            return None
    status = git("status", "--porcelain")
    return {
        "command": "uv run python experiments/CJ-0001-collins-shor-peak/manuscript_check.py " + " ".join(argv),
        "git_revision": git("rev-parse", "HEAD"),
        "tree_clean": (status == "") if status is not None else None,
        "python": platform.python_version(),
        "networkx": nx.__version__,
        "arithmetic": "exact (fractions.Fraction); evaluation at integer points and Lagrange interpolation",
    }


if __name__ == "__main__":
    import argparse, json
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-rooted", type=int, default=8)
    ap.add_argument("--max-order-sm", type=int, default=12)
    ap.add_argument("--max-merge", type=int, default=8)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    res = main(args.max_rooted, args.max_order_sm, args.max_merge)
    if args.out:
        res = {"run": _run_block(sys.argv[1:]), **res}
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=2)
            fh.write("\n")
