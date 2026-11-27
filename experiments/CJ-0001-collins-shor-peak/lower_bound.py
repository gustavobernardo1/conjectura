"""CJ-0001, session 11: exact checks of the statements of notes/lower-bound.md.

Exact integer arithmetic throughout (Python integers; python-flint for the characteristic polynomial
of the distance matrix).  No floating point.  These are finite checks of identities and of cone
memberships on the ranges stated below.  They are not proofs.

Notation of research/active/CJ-0001-collins-shor-peak/notes/lower-bound.md.  A rooted tree (A, u)
has weight zero, order a, delta_v = dist(u, v), M = I + x L_A, Phi = det M, and

  state of (A, 0, u):  Psi, H, G, Omega, R        (rooted_state.state: each from its definition)
  E      = R - Omega + (1+2x)^2 Psi - 2x G
  Pi_uv  = det M[A - V(path(u, v))],   a_v = x^(delta_v - 1) Pi_uv            (v != u)
  M1     = M + x e_u e_u^T,   R1 = R(A, e_u),   Q1 = sum_{v<v'} (delta_v - delta_v')^2 adj(M1)_{vv'}
  l_T    = sum_{k <= n-2} d_k x^k - 4 x^n        (d_k from the distance matrix, distpoly.py)
  C_d    = non-negative combinations of x^e (1+x)^(d-2e), 2e < d, and of x^e, d <= 2e <= 2d.

The note states its memberships in the cones K_d.  What is tested here is membership in C_d at the
same index d, which is equivalent for a polynomial of degree at most d ((K1) and (K4) of the note);
a polynomial of degree above d is counted as a failure.

Part A.  Every rooted tree of order 1..max_rooted, one per isomorphism class of rooted trees (the
  trees of distpoly.layouts, every vertex as root, duplicates removed by the canonical code of the
  rooted tree; the number per order is compared with OEIS A000081):
    Lemma S24      x a_v = adj(M)_uv, with a_v from the minor (definition)
    S33(b)         H = sum_v a_v
    S33(c)         x divides G;  G/x = sum_v (delta_v - 1) a_v
    S33(e)         R1 = Q1 + x^2 sum_v delta_v^2 a_v
    S34(a)         E = R1 - (1+x)(Omega + xH)
    S34(b), plant  Psi^ = (1+x)Psi + xH,  Psi^ = Phi(A, e_u),  H^ = Psi + xH = Phi,  G^ = x(xH + G),
                   Omega^ = R1,  R^ = (1+x)R + x Omega,  E^ = x[E + Omega + 2G + x(3+2x)H]
                   (the state of the planted tree computed from its definition)
    cones          Psi in C_{a-1}, H in C_{a-2}, G/x in C_{a-1}, Omega in C_a, E in C_{a+1},
                   R1 in C_{a+1}, Q1 in C_a, a_v in C_{a-2}, a_v in C_{a+delta_v-3} (S33(a)),
                   (1+4x)Psi + Omega - (1+4x)(1+x)^(a-1) in C_a (Theorem T6(a))
Part B.  Every pair of rooted trees of part A of orders a1 <= a2 with a1 + a2 - 1 <= max_merge
  (for a1 = a2 every ordered pair):
    S19(d)         Psi = Psi1 Psi2,  X = X1 Psi2 + X2 Psi1 for X = H, G, Omega    (merged tree, definition)
    S34(c)         E = E1 Psi2 + E2 Psi1 + x(H1 Omega2 + H2 Omega1) - 2 G1 G2
    S35            x(H^1 Omega^2 + H^2 Omega^1) - 2 G^1 G^2
                     = x(Psi1 R1_2 + Psi2 R1_1) + x^2 (H1 Q1_2 + H2 Q1_1)
                       + x^4 sum_{v, v'} (delta_v - delta_v')^2 a_v a_v'
                   (the left side from the states of the two planted trees), and the left side in
                   C_{a1+a2+2}
Part C.  Every pair of rooted trees of part A of orders a <= b with a + b <= max_pairs (for a = b
  every ordered pair).  T = A + B + the edge uv;  T' = A and B with u = v identified, plus a pendant
  vertex at the identified vertex;  n = a + b:
    S23(a)         (R(T, 0) + (1+4x) Phi_T)/x equals l_T of the distance matrix (T and T')
    S36            l_T - l_T' = H_A E_B + H_B E_A + x(2+5x) H_A H_B + 2 G_A G_B / x   (l from the
                   distance matrix), and the difference in C_{n-1}
  For a = 1 the edge uv is pendant, T = T' and both sides are zero; these pairs are counted apart.
Part D.  Every tree of order 4..max_contract (distpoly.layouts) and every non-pendant edge, l from
  the distance matrix only:
    S36            l_T - l_T' in C_{n-1};  lam_m(l_T - l_T') >= 0, m = floor(n/2);
    Remark 1       [x^1](l_T - l_T') = 2 (k_u - 1)(k_v - 1)
Part E.  Theorem T6(b), (c) directly.  For every order n = 2..max_contract:
    S23(d)         l_star = (1+x)^(n-2) [(n-1) + 4(n-2)x - 4x^2] against the distance matrix of the star
    Remark 3       n = 2m >= 4: (m-1)(m+1) (d_m - d_{m-1})(star) = C(2m-2, m-2)(2m-1)(3m-5)
  and for every tree T of order n (distance matrix only):
    T6(b)          l_T - l_star in C_{n-1}                                        (n >= 2)
    T6(c)          d_m(T) - d_{m-1}(T) >= d_m(star) - d_{m-1}(star) > 0, m = floor(n/2);
                   every maximizing index of d_0..d_{n-2} is at least m             (n >= 3)

Budget, fixed before the run: 5 minutes of wall-clock time for the stored run.  --time-limit
(seconds, default 300) is tested before each order of each part; when it is reached the run stops,
records where, and exits with status 2.  Exit status 1: at least one check failed.

Command of the stored run (from the repository root):

    uv run python experiments/CJ-0001-collins-shor-peak/lower_bound.py --max-rooted 9 --max-merge 9 \
        --max-pairs 10 --max-contract 16 --out experiments/CJ-0001-collins-shor-peak/results/lower-bound.json
"""
import argparse
import hashlib
import json
import subprocess
import sys
import time
from math import comb
from pathlib import Path

from distpoly import layouts, parents_from_layout, peak_indices, run_metadata, scaled_coefficients, star_parents
from rooted_state import WT, det_adj, half_gamma, padd, pmul, pscale, psub, ptrim, state

# Number of rooted trees with n vertices (OEIS A000081), n = 0..12.  Used only to validate the enumeration.
A000081 = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766]


# ---------- polynomials (lists of integers, lowest degree first; the zero polynomial trims to []) ----------
def peq(p, q):
    return ptrim(p) == ptrim(q)


def xpow(p, k):
    """x^k p."""
    return [0] * k + list(p)


def binom_row(k):
    return [comb(k, i) for i in range(k + 1)]


def lam(p, m):
    """[x^m] p - [x^(m-1)] p."""
    return (p[m] if 0 <= m < len(p) else 0) - (p[m - 1] if 0 <= m - 1 < len(p) else 0)


def in_C(p, d):
    """Membership in the cone C_d.  The zero polynomial is in every C_d; degree above d is a failure."""
    p = ptrim(p)
    if not p:
        return True
    if d < 0 or len(p) > d + 1:
        return False
    return min(half_gamma(p, d)) >= 0


# ---------- bookkeeping ----------
class Tally:
    """Number of cases and of failures per named check; the first failing instance of each is kept."""

    def __init__(self):
        self.cases, self.failures, self.first = {}, {}, {}

    def check(self, name, ok, witness=None):
        self.cases[name] = self.cases.get(name, 0) + 1
        self.failures.setdefault(name, 0)
        if not ok:
            self.failures[name] += 1
            if name not in self.first:
                self.first[name] = witness() if callable(witness) else witness
        return bool(ok)

    def total_cases(self):
        return sum(self.cases.values())

    def total_failures(self):
        return sum(self.failures.values())

    def as_dict(self):
        return {
            "checks": {k: {"cases": self.cases[k], "failures": self.failures[k]} for k in self.cases},
            "cases_total": self.total_cases(),
            "failures_total": self.total_failures(),
            "first_failures": self.first,
        }


class Budget:
    def __init__(self, seconds=None):
        self.deadline = None if seconds is None else time.monotonic() + seconds

    def expired(self):
        return self.deadline is not None and time.monotonic() > self.deadline


def _stopped(res, budget, where):
    if budget is not None and budget.expired():
        res["completed"] = False
        res["stopped_before"] = where
        return True
    return False


# ---------- trees ----------
def tree_edges(par):
    return [(par[v], v) for v in range(1, len(par))]


def neighbours(n, edges):
    adjl = [[] for _ in range(n)]
    for a, b in edges:
        adjl[a].append(b)
        adjl[b].append(a)
    return adjl


def rooted_code(adjl, u, parent=-1):
    """Canonical code of the rooted tree: equal codes if and only if the rooted trees are isomorphic."""
    return tuple(sorted(rooted_code(adjl, w, u) for w in adjl[u] if w != parent))


def bfs(adjl, u):
    """Distances from u, the neighbour of each vertex on the way to u, and the vertices in order of visit."""
    delta, up, order = {u: 0}, {u: None}, [u]
    for v in order:
        for w in adjl[v]:
            if w not in delta:
                delta[w], up[w] = delta[v] + 1, v
                order.append(w)
    return delta, up, order


def rooted_trees(a):
    """One (edges, root) per isomorphism class of rooted trees of order a."""
    out = []
    for lay in layouts(a):
        edges = tree_edges(parents_from_layout(lay))
        adjl = neighbours(a, edges)
        seen = set()
        for u in range(a):
            code = rooted_code(adjl, u)
            if code not in seen:
                seen.add(code)
                out.append((edges, u))
    return out


def parents_from_edges(n, edges):
    """A parent array with parent[i] < i (vertices renumbered in order of visit from vertex 0)."""
    _, up, order = bfs(neighbours(n, edges), 0)
    assert len(order) == n
    new = {v: i for i, v in enumerate(order)}
    return [-1] + [new[up[v]] for v in order[1:]]


def d_coefficients(par):
    """[d_0, ..., d_{n-2}] from the distance matrix; None if some 2^k |delta_k| is not divisible by 2^(n-2)."""
    n = len(par)
    s = scaled_coefficients(par)
    if any(c % 2 ** (n - 2) for c in s):
        return None
    return [c >> (n - 2) for c in s]


def ell_distance(par):
    """l_T as a list of n + 1 integers (top coefficients 0 and -4), from the distance matrix; n >= 2."""
    d = d_coefficients(par)
    return None if d is None else d + [0, -4]


def ell_from_R(T):
    """(R(T, 0) + (1+4x) Phi_T)/x for a WT of weight zero (Proposition S23(a)); None if x does not divide."""
    s = ptrim(padd(T.R(), pmul([1, 4], T.phi)))
    if s and s[0] != 0:
        return None
    return s[1:]


# ---------- the state of a rooted tree ----------
def state_E(T, u):
    """Psi, H, G, Omega, R of (T, 0, u) from their definitions, Phi, and E = R - Omega + (1+2x)^2 Psi - 2xG."""
    st = state(T, u)
    s = {k: ptrim(st[k]) for k in ("Psi", "H", "G", "Om", "R")}
    s["Phi"] = ptrim(T.phi)
    s["E"] = ptrim(psub(padd(psub(s["R"], s["Om"]), pmul([1, 4, 4], s["Psi"])), pscale(xpow(s["G"], 1), 2)))
    return s


def rooted_record(edges, a, u):
    """Everything parts A, B and C need about the rooted tree (A, u) and about the planted tree (A^, r)."""
    T = WT(a, edges, [0] * a)
    rec = state_E(T, u)
    adjl = neighbours(a, edges)
    delta, up, _ = bfs(adjl, u)
    L = [[0] * a for _ in range(a)]
    for x, y in edges:
        L[x][y] = L[y][x] = -1
        L[x][x] += 1
        L[y][y] += 1
    av = {}
    for v in range(a):
        if v == u:
            continue
        path, w = set(), v
        while w is not None:
            path.add(w)
            w = up[w]
        keep = [w for w in range(a) if w not in path]
        minor = det_adj([[L[i][k] for k in keep] for i in keep])[0]  # Pi_uv = det M[A - V(path(u, v))]
        av[v] = ptrim(xpow(minor, delta[v] - 1))
    T1 = T.raised(u)
    Q1 = []
    for v in range(a):
        for w in range(v + 1, a):
            Q1 = padd(Q1, pscale(T1.adj[v][w], (delta[v] - delta[w]) ** 2))
    Tp = WT(a + 1, list(edges) + [(u, a)], [0] * (a + 1))
    rec.update(
        edges=[list(e) for e in edges], a=a, u=u, delta=delta, av=av,
        adj_row={v: ptrim(T.adj[u][v]) for v in range(a)},
        Gh=rec["G"][1:], G_divisible=not rec["G"] or rec["G"][0] == 0,
        Phi1=ptrim(T1.phi), R1=ptrim(T1.R()), Q1=ptrim(Q1), planted=state_E(Tp, a),
    )
    return rec


def _w(rec, vertex=None, **polys):
    """A JSON-ready description of a failing rooted tree (called only when a check fails)."""
    return lambda: dict(edges=rec["edges"], root=rec["u"], vertex=vertex, **{k: ptrim(v) for k, v in polys.items()})


def part_A(max_rooted, budget=None):
    """Returns (result, records); records[a] is the list of rooted records of order a."""
    tally, records, by_order = Tally(), {}, {}
    res = {"completed": True}
    for a in range(1, max_rooted + 1):
        if _stopped(res, budget, "order %d" % a):
            break
        records[a] = [rooted_record(edges, a, u) for edges, u in rooted_trees(a)]
        by_order[str(a)] = len(records[a])
        if a < len(A000081):
            tally.check("enumeration_A000081", len(records[a]) == A000081[a], dict(order=a, found=len(records[a])))
        for r in records[a]:
            Psi, H, G, Gh, Om, R, E, P = r["Psi"], r["H"], r["G"], r["Gh"], r["Om"], r["R"], r["E"], r["planted"]
            delta, av = r["delta"], r["av"]
            sum_a, sum_d1, sum_d2 = [], [], []
            for v, p in av.items():
                tally.check("S24_x_av_is_adjugate_entry", peq(xpow(p, 1), r["adj_row"][v]),
                            _w(r, vertex=v, x_av=xpow(p, 1), adj_uv=r["adj_row"][v]))
                sum_a = padd(sum_a, p)
                sum_d1 = padd(sum_d1, pscale(p, delta[v] - 1))
                sum_d2 = padd(sum_d2, pscale(p, delta[v] ** 2))
            tally.check("S33b_H", peq(H, sum_a), _w(r, H=H, sum=sum_a))
            tally.check("S33c_x_divides_G", r["G_divisible"], _w(r, G=G))
            tally.check("S33c_G_over_x", r["G_divisible"] and peq(Gh, sum_d1), _w(r, G=G, sum=sum_d1))
            rhs = padd(r["Q1"], xpow(sum_d2, 2))
            tally.check("S33e_R1", peq(r["R1"], rhs), _w(r, R1=r["R1"], rhs=rhs))
            rhs = psub(r["R1"], pmul([1, 1], padd(Om, xpow(H, 1))))
            tally.check("S34a_E", peq(E, rhs), _w(r, E=E, rhs=rhs))
            # plant: the state of the planted tree, from its definition, against the rules
            rhs = padd(pmul([1, 1], Psi), xpow(H, 1))
            tally.check("S34b_plant_Psi", peq(P["Psi"], rhs), _w(r, planted=P["Psi"], rhs=rhs))
            tally.check("S34b_plant_Psi_is_Phi1", peq(P["Psi"], r["Phi1"]), _w(r, planted=P["Psi"], Phi1=r["Phi1"]))
            rhs = padd(Psi, xpow(H, 1))
            tally.check("S34b_plant_H", peq(P["H"], rhs) and peq(P["H"], r["Phi"]), _w(r, planted=P["H"], rhs=rhs))
            rhs = xpow(padd(xpow(H, 1), G), 1)
            tally.check("S34b_plant_G", peq(P["G"], rhs), _w(r, planted=P["G"], rhs=rhs))
            tally.check("S34b_plant_Omega", peq(P["Om"], r["R1"]), _w(r, planted=P["Om"], R1=r["R1"]))
            rhs = padd(pmul([1, 1], R), xpow(Om, 1))
            tally.check("S19c_plant_R", peq(P["R"], rhs), _w(r, planted=P["R"], rhs=rhs))
            rhs = xpow(padd(padd(E, Om), padd(pscale(G, 2), pmul([0, 3, 2], H))), 1)
            tally.check("S34b_plant_E", peq(P["E"], rhs), _w(r, planted=P["E"], rhs=rhs))
            # cones
            tally.check("cone_Psi_in_C(a-1)", in_C(Psi, a - 1), _w(r, Psi=Psi))
            tally.check("cone_H_in_C(a-2)", in_C(H, a - 2), _w(r, H=H))
            tally.check("cone_G_over_x_in_C(a-1)", in_C(Gh, a - 1), _w(r, G_over_x=Gh))
            tally.check("cone_Omega_in_C(a)", in_C(Om, a), _w(r, Omega=Om))
            tally.check("cone_E_in_C(a+1)", in_C(E, a + 1), _w(r, E=E))
            tally.check("cone_R1_in_C(a+1)", in_C(r["R1"], a + 1), _w(r, R1=r["R1"]))
            tally.check("cone_Q1_in_C(a)", in_C(r["Q1"], a), _w(r, Q1=r["Q1"]))
            for v, p in av.items():
                tally.check("cone_av_in_C(a-2)", in_C(p, a - 2), _w(r, vertex=v, a_v=p))
                tally.check("cone_av_in_C(a+delta-3)", in_C(p, a + delta[v] - 3), _w(r, vertex=v, a_v=p))
            t6a = psub(padd(pmul([1, 4], Psi), Om), pmul([1, 4], binom_row(a - 1)))
            tally.check("T6a_r_minus_star_in_C(a)", in_C(t6a, a), _w(r, difference=t6a))
    res.update(rooted_trees=sum(by_order.values()), rooted_trees_by_order=by_order, **tally.as_dict())
    return res, records


# ---------- part B: merges ----------
def merged_tree(r1, r2):
    """The merge of (A1, u1) and (A2, u2): the two roots identified; root u1."""
    a1, u1, u2 = r1["a"], r1["u"], r2["u"]

    def lab(v):
        return u1 if v == u2 else a1 + v - (1 if v > u2 else 0)

    n = a1 + r2["a"] - 1
    edges = [tuple(e) for e in r1["edges"]] + [(lab(x), lab(y)) for x, y in r2["edges"]]
    return WT(n, edges, [0] * n), u1


def _w2(r1, r2, which=None, **polys):
    return lambda: dict(edges_1=r1["edges"], root_1=r1["u"], edges_2=r2["edges"], root_2=r2["u"], which=which,
                        **{k: ptrim(v) for k, v in polys.items()})


def s35_sides(r1, r2):
    """The two sides of the identity of Proposition S35 for the rooted trees r1, r2."""
    P1, P2 = r1["planted"], r2["planted"]
    lhs = psub(xpow(padd(pmul(P1["H"], P2["Om"]), pmul(P2["H"], P1["Om"])), 1), pscale(pmul(P1["G"], P2["G"]), 2))
    squares = []
    for v, p in r1["av"].items():
        for w, q in r2["av"].items():
            squares = padd(squares, pscale(pmul(p, q), (r1["delta"][v] - r2["delta"][w]) ** 2))
    rhs = padd(padd(xpow(padd(pmul(r1["Psi"], r2["R1"]), pmul(r2["Psi"], r1["R1"])), 1),
                    xpow(padd(pmul(r1["H"], r2["Q1"]), pmul(r2["H"], r1["Q1"])), 2)), xpow(squares, 4))
    return ptrim(lhs), ptrim(rhs)


def part_B(records, max_merge, budget=None):
    tally, by_orders = Tally(), {}
    res = {"completed": True}
    top = max(records) if records else 0
    for a1 in range(1, top + 1):
        if _stopped(res, budget, "first order %d" % a1):
            break
        for a2 in range(a1, top + 1):
            if a1 + a2 - 1 > max_merge:
                continue
            by_orders["%d,%d" % (a1, a2)] = len(records[a1]) * len(records[a2])
            for r1 in records[a1]:
                for r2 in records[a2]:
                    Tm, um = merged_tree(r1, r2)
                    m = state_E(Tm, um)
                    rules = peq(m["Psi"], pmul(r1["Psi"], r2["Psi"])) and all(
                        peq(m[k], padd(pmul(r1[k], r2["Psi"]), pmul(r2[k], r1["Psi"]))) for k in ("H", "G", "Om"))
                    tally.check("S19d_merge_Psi_H_G_Omega", rules, _w2(r1, r2))
                    rhs = padd(padd(pmul(r1["E"], r2["Psi"]), pmul(r2["E"], r1["Psi"])),
                               psub(xpow(padd(pmul(r1["H"], r2["Om"]), pmul(r2["H"], r1["Om"])), 1),
                                    pscale(pmul(r1["G"], r2["G"]), 2)))
                    tally.check("S34c_merge_E", peq(m["E"], rhs), _w2(r1, r2, E=m["E"], rhs=rhs))
                    lhs, rhs = s35_sides(r1, r2)
                    tally.check("S35_identity", lhs == rhs, _w2(r1, r2, lhs=lhs, rhs=rhs))
                    tally.check("S35_left_side_in_C(a1+a2+2)", in_C(lhs, a1 + a2 + 2), _w2(r1, r2, lhs=lhs))
    res.update(pairs=sum(by_orders.values()), pairs_by_orders=by_orders, **tally.as_dict())
    return res


# ---------- part C: the formula of S36 on pairs of rooted trees ----------
def s36_trees(rA, rB):
    """Edge lists of T (A, B and the edge uv) and of T' (u = v identified, one new pendant vertex there)."""
    a, u, v = rA["a"], rA["u"], rB["u"]
    eA = [tuple(e) for e in rA["edges"]]
    eT = eA + [(x + a, y + a) for x, y in rB["edges"]] + [(u, v + a)]
    eTp = eA + [((u if x == v else x + a), (u if y == v else y + a)) for x, y in rB["edges"]] + [(u, v + a)]
    return eT, eTp


def s36_right_side(rA, rB, middle=(0, 2, 5)):
    """H_A E_B + H_B E_A + middle * H_A H_B + 2 G_A G_B / x; `middle` is x(2+5x) in Proposition S36."""
    return ptrim(padd(padd(pmul(rA["H"], rB["E"]), pmul(rB["H"], rA["E"])),
                      padd(pmul(list(middle), pmul(rA["H"], rB["H"])), pscale(xpow(pmul(rA["Gh"], rB["Gh"]), 1), 2))))


def part_C(records, max_pairs, budget=None, middle=(0, 2, 5)):
    """`middle` exists for the negative control of the tests only; the statement has x(2+5x)."""
    tally, by_orders = Tally(), {}
    res = {"completed": True}
    trivial = 0
    top = max(records) if records else 0
    for a in range(1, top + 1):
        if _stopped(res, budget, "first order %d" % a):
            break
        for b in range(a, top + 1):
            n = a + b
            if n > max_pairs:
                continue
            by_orders["%d,%d" % (a, b)] = len(records[a]) * len(records[b])
            for rA in records[a]:
                for rB in records[b]:
                    trivial += a == 1
                    eT, eTp = s36_trees(rA, rB)
                    lT, lTp = ell_distance(parents_from_edges(n, eT)), ell_distance(parents_from_edges(n, eTp))
                    if not tally.check("guard_d_k_integers", lT is not None and lTp is not None, _w2(rA, rB)):
                        continue
                    for name, edges, ell in (("T", eT, lT), ("T'", eTp, lTp)):
                        other = ell_from_R(WT(n, edges, [0] * n))
                        tally.check("S23a_l_from_R", other is not None and peq(other, ell),
                                    _w2(rA, rB, which=name, from_distance_matrix=ell))
                    lhs = ptrim(psub(lT, lTp))
                    rhs = s36_right_side(rA, rB, middle)
                    tally.check("S36_formula", lhs == rhs, _w2(rA, rB, lhs=lhs, rhs=rhs))
                    tally.check("S36_difference_in_C(n-1)", in_C(lhs, n - 1), _w2(rA, rB, lhs=lhs))
    res.update(pairs=sum(by_orders.values()), pairs_with_a_single_vertex_tree=trivial,
               pairs_by_orders=by_orders, **tally.as_dict())
    return res


# ---------- part D: contraction of a non-pendant edge, from the distance matrix ----------
def contracted_parents(par, v):
    """T': the edge (par[v], v) contracted and a pendant vertex added at the merged vertex.

    The children of v become children of par[v]; v itself stays as the new pendant vertex.
    """
    return [par[v] if q == v else q for q in par]


def part_D(max_contract, budget=None):
    tally, rows = Tally(), []
    res = {"completed": True}
    for n in range(4, max_contract + 1):
        if _stopped(res, budget, "order %d" % n):
            break
        t0, m = time.time(), n // 2
        trees = pairs = 0
        for lay in layouts(n):
            par = parents_from_layout(lay)
            trees += 1
            deg = [0] * n
            for v in range(1, n):
                deg[v] += 1
                deg[par[v]] += 1
            d = None
            for v in range(1, n):
                p = par[v]
                if deg[v] < 2 or deg[p] < 2:
                    continue
                pairs += 1
                if d is None:
                    d = d_coefficients(par)
                dp = d_coefficients(contracted_parents(par, v))
                where = dict(order=n, parents=par, edge=[p, v])
                if not tally.check("guard_d_k_integers", d is not None and dp is not None, where):
                    continue
                diff = [x - y for x, y in zip(d, dp)]
                tally.check("S36_difference_in_C(n-1)", in_C(diff, n - 1), lambda: dict(where, difference=diff))
                tally.check("S36_lam_m_nonnegative", lam(diff, m) >= 0, lambda: dict(where, difference=diff))
                tally.check("S36_remark1_linear_coefficient", diff[1] == 2 * (deg[p] - 1) * (deg[v] - 1),
                            lambda: dict(where, difference=diff))
        rows.append(dict(order=n, trees=trees, tree_edge_pairs=pairs, seconds=round(time.time() - t0, 1)))
        print("D", rows[-1], file=sys.stderr, flush=True)
    res.update(trees=sum(r["trees"] for r in rows), tree_edge_pairs=sum(r["tree_edge_pairs"] for r in rows),
               rows=rows, **tally.as_dict())
    return res


# ---------- part E: Theorem T6(b), (c) ----------
def star_closed_form(n):
    """(1+x)^(n-2) [(n-1) + 4(n-2)x - 4x^2], as a list of n + 1 integers."""
    return pmul(binom_row(n - 2), [n - 1, 4 * (n - 2), -4])


def part_E(max_order, budget=None, star=star_closed_form):
    """`star` exists for the negative control of the tests only; the statement has `star_closed_form`."""
    tally, rows = Tally(), []
    res = {"completed": True}
    for n in range(2, max_order + 1):
        if _stopped(res, budget, "order %d" % n):
            break
        t0, m = time.time(), n // 2
        closed = list(star(n))
        from_matrix = ell_distance(star_parents(n))
        tally.check("S23d_star_closed_form", from_matrix is not None and closed == from_matrix,
                    dict(order=n, closed_form=closed, from_distance_matrix=from_matrix))
        base = closed[: n - 1]
        star_gap = lam(base, m) if n >= 3 else None
        if n >= 3:
            tally.check("T6c_star_gap_positive", star_gap > 0, dict(order=n, star_gap=star_gap))
        if n >= 4 and n % 2 == 0:
            tally.check("T6_remark3_star_gap", (m - 1) * (m + 1) * star_gap == comb(2 * m - 2, m - 2) * (2 * m - 1) * (3 * m - 5),
                        dict(order=n, star_gap=star_gap))
        trees = equal_gap = 0
        for lay in layouts(n):
            par = parents_from_layout(lay)
            trees += 1
            d = d_coefficients(par)
            where = dict(order=n, parents=par)
            if not tally.check("guard_d_k_integers_and_d_0", d is not None and d[0] == n - 1, where):
                continue
            diff = [x - y for x, y in zip(d, base)]
            tally.check("T6b_l_minus_star_in_C(n-1)", in_C(diff, n - 1), lambda: dict(where, difference=diff))
            if n >= 3:
                gap = lam(d, m)
                equal_gap += gap == star_gap
                tally.check("T6c_gap_at_least_star", gap >= star_gap, lambda: dict(where, gap=gap, star_gap=star_gap))
                tally.check("T6c_peak_at_least_floor_n_over_2", min(peak_indices(d)) >= m,
                            lambda: dict(where, d=d, peaks=peak_indices(d)))
        rows.append(dict(order=n, trees=trees, star_gap=star_gap, trees_with_gap_equal_to_star=equal_gap,
                         seconds=round(time.time() - t0, 1)))
        print("E", rows[-1], file=sys.stderr, flush=True)
    res.update(trees=sum(r["trees"] for r in rows), rows=rows, **tally.as_dict())
    return res


# ---------- provenance of the source files ----------
def source_fingerprints():
    """SHA-256 of this script and of the two modules it imports, and whether each equals its blob at HEAD.

    Read-only Git commands.  `identical_to_git_revision` is None for a file that HEAD does not contain.
    """
    here = Path(__file__).resolve().parent
    root = here.parents[1]

    def git(*a):
        done = subprocess.run(["git", *a], cwd=root, capture_output=True, text=True)
        return done.stdout.strip() if done.returncode == 0 else None

    out = {}
    for name in ("lower_bound.py", "distpoly.py", "rooted_state.py"):
        path = here / name
        rel = path.relative_to(root).as_posix()
        at_head = git("rev-parse", "--verify", "--quiet", "HEAD:" + rel)
        now = git("hash-object", "--", rel)
        out[rel] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "identical_to_git_revision": None if at_head is None or now is None else at_head == now}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--max-rooted", type=int, default=9, help="largest order of a rooted tree (part A)")
    ap.add_argument("--max-merge", type=int, default=9, help="largest order of a merged tree (part B)")
    ap.add_argument("--max-pairs", type=int, default=10, help="largest total order a + b (part C)")
    ap.add_argument("--max-contract", type=int, default=15, help="largest order of a tree (parts D and E)")
    ap.add_argument("--time-limit", type=float, default=300.0, help="seconds; the run stops there and records where")
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    if args.max_merge > args.max_rooted or args.max_pairs > args.max_rooted + 1:
        ap.error("parts B and C use the rooted trees of part A: need max-merge <= max-rooted and max-pairs <= max-rooted + 1")
    # Revision, state of the tree and file hashes are read before the computation starts.
    meta, sources = run_metadata(), source_fingerprints()
    start = time.time()
    budget = Budget(args.time_limit)
    out = {
        "experiment": "CJ-0001 exact checks of notes/lower-bound.md (S33 to S36, Theorems T5 and T6)",
        "arithmetic": "exact integers (Python integers; python-flint characteristic polynomial of the distance matrix)",
        "scope": "finite checks of identities and cone memberships on the stated ranges; not a proof",
        "run": meta, "sources": sources, "parameters": vars(args),
    }
    out["A"], records = part_A(args.max_rooted, budget)
    out["A"]["seconds"] = round(time.time() - start, 1)
    for key, fn in (("B", lambda: part_B(records, args.max_merge, budget)),
                    ("C", lambda: part_C(records, args.max_pairs, budget)),
                    ("D", lambda: part_D(args.max_contract, budget)),
                    ("E", lambda: part_E(args.max_contract, budget))):
        t0 = time.time()
        out[key] = fn()
        out[key]["seconds"] = round(time.time() - t0, 1)
    parts = ("A", "B", "C", "D", "E")
    out["summary"] = {
        "cases": {k: out[k]["cases_total"] for k in parts},
        "failures": {k: out[k]["failures_total"] for k in parts},
        "cases_total": sum(out[k]["cases_total"] for k in parts),
        "failures_total": sum(out[k]["failures_total"] for k in parts),
        "completed": all(out[k]["completed"] for k in parts),
    }
    out["seconds"] = round(time.time() - start, 1)
    for k in parts:
        extra = {x: out[k][x] for x in ("rooted_trees", "pairs", "trees", "tree_edge_pairs") if x in out[k]}
        print(k, extra, "cases", out[k]["cases_total"], "failures", out[k]["failures_total"],
              "completed", out[k]["completed"], "seconds", out[k]["seconds"], flush=True)
        for name, first in out[k]["first_failures"].items():
            print("  FIRST FAILURE of", name, json.dumps(first), flush=True)
    print("total cases", out["summary"]["cases_total"], "failures", out["summary"]["failures_total"],
          "completed", out["summary"]["completed"], "seconds", out["seconds"], flush=True)
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, indent=1)
            fh.write("\n")
    if out["summary"]["failures_total"]:
        return 1
    return 0 if out["summary"]["completed"] else 2


if __name__ == "__main__":
    sys.exit(main())
