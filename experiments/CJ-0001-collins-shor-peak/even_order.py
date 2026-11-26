"""CJ-0001, session 10: the even orders.  Exact integer arithmetic throughout.

Notation of research/active/CJ-0001-collins-shor-peak/notes/even-order.md:

  l_T(x)   = sum_{k <= n-2} d_k x^k - 4 x^n          (from the characteristic polynomial of the distance matrix)
  M = I + xL,  Phi = det M,  Pi_S = det M[V - S],  Psi_u = Pi_{u}
  Theta    = (Phi - (1+x)^(n-1)) / x
  Omega_T  = l_T + 4x(1+x)^(n-1) - (1+4x) Theta
  lam_m(f) = [x^m] f - [x^(m-1)] f

Part A (every tree of order 2..max_a, every vertex c):
  A1  rooted form      l_T = sum_e Pi_e + 4 sum_{v != c} delta_v x^delta_v Pi_{cv} - 4x Psi_c
                             + sum_{u<v, d(u,v) >= 2} (delta_u - delta_v)^2 x^(d-1) Pi_{uv}          (Proposition S28)
  A2  leaf polynomial  l_{T+leaf at c} - (1+x) l_T = (1+4x) Psi_c + x sum_{e not at c} Pi_{e+c}
                             + sum_{a<b, d(a,b) >= 2, c not on path} (delta_a - delta_b)^2 x^d Pi_{path+c}
                             + sum_{delta_a >= 2} (delta_a - 1)^2 x^delta_a Pi_{path(a,c)}           (Proposition S29)
Part B (every tree of order 3..max_b):
  B1  Omega_T has non-negative coefficients                                                         (Proposition S30)
  B2  Omega_T in C_{n-1}   [statement (SM+); not proved]
  B3  Theta - (n-1)(1+x)^(n-2) in C_{n-2}
Part C (inequality (3) of wiener-form.md, even orders):
  rhs3 = lam_m( 4(W - nx) Phi + sum_e (n - 2n_e)^2 Pi_e ),  m = n/2
  C1  every tree of even order 6..max_c: sign of rhs3
  C2  the spiders with (n-2)/2 legs of length 2 and one pendant vertex, even n in the given range:
      rhs3 by two implementations (python-flint characteristic polynomials; a pure-Python tree recursion),
      and d_m - d_{m-1} from the distance matrix.
"""
import argparse
import json
import sys
import time
from fractions import Fraction
from math import comb

import networkx as nx
from flint import fmpz_mat

from distpoly import run_metadata


# ---------- polynomials as lists of integers ----------
def padd(p, q):
    r = [0] * max(len(p), len(q))
    for i, c in enumerate(p):
        r[i] += c
    for i, c in enumerate(q):
        r[i] += c
    return r


def pmul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                r[i + j] += a * b
    return r


def pscale(c, p):
    return [c * a for a in p]


def pshift(p, k):
    return [0] * k + list(p)


def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def peq(p, q):
    return ptrim(p) == ptrim(q)


def binom_poly(k):
    return [comb(k, j) for j in range(k + 1)]


def lam(p, m):
    g = lambda k: p[k] if 0 <= k < len(p) else 0
    return g(m) - g(m - 1)


def half_gamma(p, d):
    """Coefficients of the unique expansion sum_{2e<d} rho_e x^e (1+x)^(d-2e) + sum_{d<=2e<=2d} sigma_e x^e; None if deg p > d."""
    p = ptrim(p)
    if len(p) > d + 1:
        return None
    r = list(p) + [0] * (d + 1 - len(p))
    out = []
    e = 0
    while 2 * e < d:
        c = r[e]
        out.append(c)
        for j in range(d - 2 * e + 1):
            r[e + j] -= c * comb(d - 2 * e, j)
        e += 1
    out.extend(r[e:])
    return out


def in_cone(p, d):
    h = half_gamma(p, d)
    return h is not None and all(c >= 0 for c in h)


# ---------- determinants ----------
def det_I_plus_xA(A):
    k = len(A)
    if k == 0:
        return [1]
    cp = fmpz_mat(A).charpoly()
    c = [int(cp[i]) for i in range(k + 1)]
    return [(-1) ** j * c[k - j] for j in range(k + 1)]


class Tree:
    def __init__(self, G):
        G = nx.convert_node_labels_to_integers(G)
        self.G = G
        self.n = n = G.number_of_nodes()
        self.L = [[0] * n for _ in range(n)]
        for u, v in G.edges():
            self.L[u][v] -= 1
            self.L[v][u] -= 1
            self.L[u][u] += 1
            self.L[v][v] += 1
        self.dist = dict(nx.all_pairs_shortest_path_length(G))
        self._cache = {}

    def pi(self, removed):
        """det (I + xL)[V - removed], by python-flint."""
        key = frozenset(removed)
        if key not in self._cache:
            keep = [w for w in range(self.n) if w not in key]
            self._cache[key] = ptrim(det_I_plus_xA([[self.L[a][b] for b in keep] for a in keep]))
        return self._cache[key]

    def pi_dp(self, removed):
        """The same determinant by a recursion over the forest T - removed (no characteristic polynomial)."""
        removed = set(removed)
        G, seen, total = self.G, set(), [1]
        for root in range(self.n):
            if root in removed or root in seen:
                continue
            order, parent = [], {root: None}
            stack = [root]
            while stack:
                v = stack.pop()
                seen.add(v)
                order.append(v)
                for w in G.neighbors(v):
                    if w not in removed and w != parent[v]:
                        parent[w] = v
                        stack.append(w)
            P, Q = {}, {}
            for v in reversed(order):
                ch = [w for w in G.neighbors(v) if w not in removed and parent.get(w) == v and w != parent[v]]
                pre = [[1]]
                for c in ch:
                    pre.append(pmul(pre[-1], P[c]))
                suf = [[1]]
                for c in reversed(ch):
                    suf.append(pmul(suf[-1], P[c]))
                suf.reverse()
                Q[v] = pre[-1]
                s = [0]
                for i, c in enumerate(ch):
                    s = padd(s, pmul(pmul(pre[i], suf[i + 1]), Q[c]))
                P[v] = ptrim(padd(pmul([1, G.degree(v)], Q[v]), pscale(-1, pshift(s, 2))))
            total = pmul(total, P[root])
        return ptrim(total)

    def path(self, u, v):
        return nx.shortest_path(self.G, u, v)

    def ell(self):
        n = self.n
        D = [[self.dist[u][v] for v in range(n)] for u in range(n)]
        cp = fmpz_mat(D).charpoly()  # det(yI - D)
        out = []
        for k in range(n + 1):
            c = Fraction(-int(cp[k]) * 2**k, 2 ** (n - 2))
            assert c.denominator == 1
            out.append(int(c))
        return out

    def wiener_parts(self, pi):
        """W and the list of (n_e, Pi_e) over the edges, with the determinant routine `pi`."""
        n, W, parts = self.n, 0, []
        for u, v in self.G.edges():
            ne = sum(1 for w in range(n) if self.dist[w][u] < self.dist[w][v])
            W += ne * (n - ne)
            parts.append((ne, pi({u, v})))
        return W, parts


def rhs3(T, pi):
    n = T.n
    m = n // 2
    phi = pi(set())
    W, parts = T.wiener_parts(pi)
    main = 4 * (W * lam(phi, m) - n * lam(pshift(phi, 1), m))
    edges = sum((n - 2 * ne) ** 2 * lam(pe, m) for ne, pe in parts)
    return main, edges


def spider2(n):
    """(n-2)/2 legs of length 2 and one pendant vertex at the centre; n even."""
    G = nx.Graph()
    nxt = 1
    for _ in range((n - 2) // 2):
        G.add_edge(0, nxt)
        G.add_edge(nxt, nxt + 1)
        nxt += 2
    G.add_edge(0, nxt)
    assert G.number_of_nodes() == n
    return G


# ---------- parts ----------
def part_a(max_a):
    res = {"trees": 0, "rooted_cases": 0, "A1_failures": 0, "A2_failures": 0}
    for n in range(2, max_a + 1):
        for G in nx.nonisomorphic_trees(n):
            T = Tree(G)
            res["trees"] += 1
            ell = T.ell()
            pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
            for c in range(n):
                res["rooted_cases"] += 1
                dl = T.dist[c]
                # A1
                s = pscale(-4, pshift(T.pi({c}), 1))
                for u, v in T.G.edges():
                    s = padd(s, T.pi({u, v}))
                for v in range(n):
                    if v != c:
                        s = padd(s, pscale(4 * dl[v], pshift(T.pi(T.path(c, v)), dl[v])))
                for u, v in pairs:
                    d = T.dist[u][v]
                    if d >= 2 and dl[u] != dl[v]:
                        s = padd(s, pscale((dl[u] - dl[v]) ** 2, pshift(T.pi(T.path(u, v)), d - 1)))
                if not peq(s, ell):
                    res["A1_failures"] += 1
                # A2
                Gp = T.G.copy()
                Gp.add_edge(c, n)
                lhs = padd(Tree(Gp).ell(), pscale(-1, pmul([1, 1], ell)))
                r = pmul([1, 4], T.pi({c}))
                for u, v in T.G.edges():
                    if c not in (u, v):
                        r = padd(r, pshift(T.pi({u, v, c}), 1))
                for a, b in pairs:
                    d = T.dist[a][b]
                    if d >= 2 and dl[a] != dl[b]:
                        p = T.path(a, b)
                        if c not in p:
                            r = padd(r, pscale((dl[a] - dl[b]) ** 2, pshift(T.pi(set(p) | {c}), d)))
                for a in range(n):
                    if dl[a] >= 2:
                        r = padd(r, pscale((dl[a] - 1) ** 2, pshift(T.pi(T.path(a, c)), dl[a])))
                if not peq(r, lhs):
                    res["A2_failures"] += 1
    return res


def part_b(max_b):
    res = {"trees": 0, "B1_failures": 0, "B2_failures": 0, "B3_failures": 0, "omega_zero": 0, "per_order": {}}
    for n in range(3, max_b + 1):
        cnt = 0
        for G in nx.nonisomorphic_trees(n):
            T = Tree(G)
            cnt += 1
            ell, phi = T.ell(), T.pi(set())
            b = binom_poly(n - 1)
            theta = [phi[k + 1] - (b[k + 1] if k + 1 < len(b) else 0) for k in range(n - 1)]
            assert phi[0] == 1
            omega = padd(padd(ell, pscale(4, pshift(b, 1))), pscale(-1, pmul([1, 4], theta)))
            if any(c < 0 for c in omega):
                res["B1_failures"] += 1
            if not in_cone(omega, n - 1):
                res["B2_failures"] += 1
            if all(c == 0 for c in omega):
                res["omega_zero"] += 1
            if not in_cone(padd(theta, pscale(-(n - 1), binom_poly(n - 2))), n - 2):
                res["B3_failures"] += 1
        res["trees"] += cnt
        res["per_order"][str(n)] = cnt
    return res


def part_c(max_c, fam_lo, fam_hi):
    res = {"C1": {}, "C2": []}
    for n in range(6, max_c + 1, 2):
        cnt = neg = 0
        least = None
        for G in nx.nonisomorphic_trees(n):
            T = Tree(G)
            cnt += 1
            main, edges = rhs3(T, T.pi)
            if main + edges <= 0:
                neg += 1
            q = Fraction(main + edges, main)
            if least is None or q < least:
                least = q
        res["C1"][str(n)] = {"trees": cnt, "rhs3_not_positive": neg, "least_rhs3_over_main": str(least)}
    for n in range(fam_lo, fam_hi + 1, 2):
        T = Tree(spider2(n))
        a = rhs3(T, T.pi)
        b = rhs3(T, T.pi_dp)
        ell = T.ell()
        m = n // 2
        res["C2"].append({"n": n, "rhs3_flint": str(a[0] + a[1]), "rhs3_recursion": str(b[0] + b[1]),
                          "implementations_agree": a == b, "rhs3_sign": (a[0] + a[1] > 0) - (a[0] + a[1] < 0),
                          "main_term": str(a[0]), "edge_terms": str(a[1]),
                          "d_m_minus_d_m_minus_1_positive": lam(ell, m) > 0})
    negs = [r["n"] for r in res["C2"] if r["rhs3_sign"] <= 0]
    res["C2_first_n_with_rhs3_not_positive"] = negs[0] if negs else None
    res["C2_all_agree"] = all(r["implementations_agree"] for r in res["C2"])
    res["C2_conjectured_inequality_holds_on_family"] = all(r["d_m_minus_d_m_minus_1_positive"] for r in res["C2"])
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-a", type=int, default=9)
    ap.add_argument("--max-b", type=int, default=15)
    ap.add_argument("--max-c", type=int, default=14)
    ap.add_argument("--family", type=int, nargs=2, default=[80, 110])
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    meta = run_metadata()
    t0 = time.time()
    out = {"metadata": meta, "parameters": vars(args)}
    out["A"] = part_a(args.max_a)
    print("A", out["A"], flush=True)
    out["B"] = part_b(args.max_b)
    print("B", out["B"], flush=True)
    out["C"] = part_c(args.max_c, *args.family)
    print("C1", out["C"]["C1"], flush=True)
    print("C2 first n with rhs3 <= 0:", out["C"]["C2_first_n_with_rhs3_not_positive"], "agree:", out["C"]["C2_all_agree"],
          "conjecture holds on family:", out["C"]["C2_conjectured_inequality_holds_on_family"], flush=True)
    out["seconds"] = round(time.time() - t0, 1)
    print("seconds", out["seconds"])
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, indent=1)
            fh.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
