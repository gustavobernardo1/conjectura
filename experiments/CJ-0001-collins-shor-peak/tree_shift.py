"""CJ-0001, session 12: exact checks of notes/path-maximality.md (Lemma S37, Proposition S38, Theorems T7, T8,
Lemma S39) and a falsification attempt on the OPEN statement (PM).

Exact integer arithmetic (Python integers, python-flint characteristic polynomial of the distance matrix,
fractions.Fraction for margins).  No floating point supports a claim; the only floats written are decimal
renderings of exact margins and are labelled exploratory.  Finite checks on the stated ranges, not proofs.

Notation of the note.  l_T = sum_{k<=n-2} d_k x^k - 4 x^n (d_k from the distance matrix, as in lower_bound.py).
The generalized tree shift T -> T' along a path x..y of length k >= 1: the inner vertices of the path have
degree 2, x and y each have a neighbour off the path, and all neighbours of y off the path are moved to x.
K_d = non-negative combinations of x^e (1+x)^(d-2e) (2e < d) and of x^e (2e >= d); C_d = K_d with degree <= d.
The polynomials x^e (1+x)^(d-2e), x^e form a basis of all polynomials (triangular by lowest-degree term), so
membership in K_d is decided from the unique coordinates (`k_coordinates`).

Parts.
  A  (only if sympy imports; not a project dependency: uv run --with sympy==1.14.0)
       det(I - tJ) = (1 - xt)(1 - (1+2x)t + x^2 t^2)^2 for the plant matrix J of the note, and
       Delta_k = c_k (the proof of Lemma S37) for k = 1..12 in free state variables.
  B  Lemma S37 on actual trees: every pair of rooted trees (A,u), (B,v), a, b >= 2, k = 1..K, n = a+b+k-1 <= N_B.
       T_k and T'_k as explicit graphs, l from the distance matrix, states of (A,u), (B,v) from their definitions;
       identity of Lemma S37; each term in K_{n-1} (the indices of Proposition S38); difference in C_{n-1}.
  C  Theorem T7: every tree of order 5..N_C and every generalized tree shift: l_T - l_T' in C_{n-1}.
  D  Theorem T8: every tree of order 4..N_D: l_{P_n} - l_T in C_{n-1}; number of trees with l_T = l_{P_n};
       Lemma S39 constructively for every non-path tree of order <= N_C.
  E  statement (PM), OPEN: for every shift T -> T', pmax(T') <= pmax(T) and pmin(T') <= pmin(T), pmax/pmin the
       largest/smallest index maximizing d_0..d_{n-2}.  (i) exhaustive, orders 5..N_E; (ii) families (double stars,
       brooms, spiders, caterpillars) at orders up to 120; (iii) seeded random Pruefer trees.  A violation is verified
       by an independent method (Faddeev-LeVerrier on a networkx distance matrix) and stops the run.
  F  the path: Collins's closed form d_{n-k}(P_n) = C(n+k-1, 2k-1)(k-1)n/k for n = 3..N_F, against the distance
       matrix for n <= 60; the peak indices against M = n - isqrt(n*n//5) = ceil(n - n/sqrt 5).

Budget, fixed before the run: 10 minutes of wall-clock for the stored run (--time-limit, default 570 s, tested
inside the loops; when reached the part stops and records where; exit status 2).  Exit status 1: a check failed.

Command of the stored run (from the repository root): see the README entry and the `run` block of the result.
"""
import argparse
import hashlib
import json
import random
import subprocess
import sys
import time
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path

import lower_bound as lb
from distpoly import layouts, parents_from_layout, path_parents, run_metadata
from lower_bound import Budget, Tally, d_coefficients, padd, parents_from_edges, pmul, pscale, psub, ptrim, xpow


# ---------- cones ----------
def k_coordinates(p, d):
    """Coordinates of the polynomial p in the basis x^e (1+x)^(d-2e) (2e < d), x^e (2e >= d), e = 0, 1, ..."""
    c = [int(v) for v in ptrim(p)]
    top = max(len(c), d + 1, 1)
    c += [0] * (top - len(c))
    coords = []
    e = 0
    while 2 * e < d:
        g = c[e]
        coords.append(g)
        for i in range(d - 2 * e + 1):
            c[e + i] -= g * comb(d - 2 * e, i)
        e += 1
    coords.extend(c[e:])
    return coords


def in_K(p, d):
    """Membership in K_d (any degree)."""
    return min(k_coordinates(p, d), default=0) >= 0


def in_Cd(p, d):
    """Membership in C_d = K_d with degree <= d."""
    return len(ptrim(p)) <= d + 1 and in_K(p, d)


# ---------- trees ----------
def adjacency(n, edges):
    adjl = [[] for _ in range(n)]
    for a, b in edges:
        adjl[a].append(b)
        adjl[b].append(a)
    return adjl


def d_of(n, edges):
    d = d_coefficients(parents_from_edges(n, edges))
    assert d is not None
    return d


def tree_shifts(adjl):
    """All generalized tree shifts that change the tree, as (x, y, path) with x < y: a path x..y whose inner
    vertices have degree 2 and with a neighbour of x and a neighbour of y off the path."""
    out = []
    for x in range(len(adjl)):
        if len(adjl[x]) < 2:
            continue
        for s in adjl[x]:
            path, prev, cur = [x, s], x, s
            while True:
                if len(adjl[cur]) >= 2 and x < cur:
                    out.append((x, cur, list(path)))
                if len(adjl[cur]) != 2:
                    break
                nxt = adjl[cur][0] if adjl[cur][0] != prev else adjl[cur][1]
                prev, cur = cur, nxt
                path.append(cur)
    return out


def apply_shift(edges, adjl, x, y, path):
    """Edge list of T': the neighbours of y off the path are moved to x."""
    moved = {w for w in adjl[y] if w != path[-2]}
    out = []
    for a, b in edges:
        if a == y and b in moved:
            out.append((x, b))
        elif b == y and a in moved:
            out.append((a, x))
        else:
            out.append((a, b))
    return out


def leaves(adjl):
    return sum(len(a) == 1 for a in adjl)


def peaks(d):
    top = max(d)
    idx = [i for i, c in enumerate(d) if c == top]
    return idx[0], idx[-1], top


def pm_margins(dT, dTp):
    """For a pair T, T': (pmax(T') <= pmax(T), pmin(T') <= pmin(T), margin1, margin2), margins exact Fractions or None.
    With p = pmax(T): margin1 = (max_{j<=p} d_j(T') - max_{j>p} d_j(T')) / max d(T')  (> 0 iff pmax(T') <= p);
    with q = pmin(T): margin2 = same at q (>= 0 iff pmin(T') <= q)."""
    lo, hi, _ = peaks(dT)
    lo2, hi2, top2 = peaks(dTp)
    out = []
    for p in (hi, lo):
        after = dTp[p + 1:]
        out.append(Fraction(max(dTp[: p + 1]) - max(after), top2) if after else None)
    return hi2 <= hi, lo2 <= lo, out[0], out[1]


# ---------- independent method (used only to verify a violation, and in the tests) ----------
def leverrier_charpoly(D):
    """Coefficients c_0..c_n of det(xI - D) by Faddeev-LeVerrier in Fractions (shares no code with flint)."""
    n = len(D)
    Dm = [[Fraction(v) for v in row] for row in D]
    M = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    coeffs = [Fraction(1)]
    for k in range(1, n + 1):
        AM = [[sum(Dm[i][t] * M[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        ck = -sum(AM[i][i] for i in range(n)) / k
        coeffs.append(ck)
        M = [[AM[i][j] + (ck if i == j else 0) for j in range(n)] for i in range(n)]
    return list(reversed(coeffs))  # c_0 .. c_n


def independent_d(n, edges):
    """[d_0..d_{n-2}] by Faddeev-LeVerrier on a breadth-first distance matrix (networkx-free)."""
    adjl = adjacency(n, edges)
    D = []
    for s in range(n):
        dist, order = {s: 0}, [s]
        for v in order:
            for w in adjl[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    order.append(w)
        D.append([dist[t] for t in range(n)])
    c = leverrier_charpoly(D)
    out = []
    for k in range(n - 1):
        v = abs(c[k]) * 2 ** k / 2 ** (n - 2)
        assert v.denominator == 1
        out.append(int(v))
    return out


# ---------- the sequences of Lemma S37 ----------
def a_seq(m):
    a = [[1], [1, 2]]
    for j in range(2, m + 1):
        a.append(psub(pmul([1, 2], a[j - 1]), xpow(a[j - 2], 2)))
    return a


def gamma_k(a, k):
    out = []
    for i in range(k):
        out = padd(out, xpow(a[k - 1 - i], i))
    return ptrim(out)


def rho_k(a, k):
    out = []
    for i in range(k - 1):
        out = padd(out, pscale(xpow(a[k - 2 - i], i), (i + 1) * (k - 1 - i)))
    return ptrim(xpow(out, 1))


def s37_terms(rA, rB, k, a, scales=(1, 1, 1, 1)):
    """The four terms of the right side of Lemma S37 (and the three pieces of the last), as polynomials.
    `scales` multiplies the four terms; it exists for the negative controls only (the statement has 1,1,1,1)."""
    HA, HB, EA, EB, GA, GB = rA["H"], rB["H"], rA["E"], rB["E"], rA["Gh"], rB["Gh"]
    g, g1, ak = gamma_k(a, k), (gamma_k(a, k - 1) if k >= 2 else []), a[k - 1]
    t1 = pmul(ak, padd(pmul(HA, EB), pmul(EA, HB)))
    t2 = pscale(xpow(pmul(g, pmul(GA, GB)), 1), 2)
    t3 = pscale(xpow(pmul(g1, padd(pmul(HA, GB), pmul(GA, HB))), 2), 2)
    HH = pmul(HA, HB)
    p41 = pscale(xpow(pmul(padd([1], [0, 1]), pmul(g, HH)), 1), 2)
    p42 = pscale(xpow(pmul(ak, HH), 2), 3)
    p43 = xpow(pmul(rho_k(a, k), HH), 1)
    t4 = padd(padd(p41, p42), p43)
    terms = [pscale(t, s) for t, s in zip((t1, t2, t3, t4), scales)]
    return terms, (p41, p42, p43)


# ---------- part A (sympy) ----------
def part_A(k_max=12):
    try:
        import sympy as sp
    except ImportError:
        msg = "skipped: sympy is not importable (not a project dependency; run with uv run --with sympy==1.14.0)"
        print("A", msg, file=sys.stderr, flush=True)
        return {"skipped": True, "reason": msg, "completed": True, "cases_total": 0, "failures_total": 0,
                "checks": {}, "first_failures": {}}
    tally = Tally()
    x, t = sp.symbols("x t")
    J = sp.Matrix([
        [1 + x, x, 0, 0, 0],
        [1, x, 0, 0, 0],
        [0, x**2, x, 0, 0],
        [0, x * (1 + x), 0, 1 + x, 1],
        [0, x**2 * (3 + 2 * x), 2 * x, x, x]])
    Q = 1 - (1 + 2 * x) * t + x**2 * t**2
    det = sp.expand((sp.eye(5) - t * J).det() - (1 - x * t) * Q**2)
    tally.check("A_det_factorization", det == 0, {"difference": str(det)})

    def plant(s):
        P, H, G, O, E = s
        return ((1 + x) * P + x * H, P + x * H, x * (x * H + G), E + (1 + x) * (O + x * H),
                x * (E + O + 2 * G + x * (3 + 2 * x) * H))

    def merge(s, u):
        P1, H1, G1, O1, E1 = s
        P2, H2, G2, O2, E2 = u
        return (P1 * P2, H1 * P2 + H2 * P1, G1 * P2 + G2 * P1, O1 * P2 + O2 * P1,
                E1 * P2 + E2 * P1 + x * (H1 * O2 + H2 * O1) - 2 * G1 * G2)

    def xl(s):
        P, H, G, O, E = s
        return E + O + 2 * x * G + x * (1 + 4 * x) * H - 4 * x**2 * P

    av = [sp.Integer(1), 1 + 2 * x]
    for _ in range(k_max + 2):
        av.append(sp.expand((1 + 2 * x) * av[-1] - x**2 * av[-2]))
    a = lambda j: av[j] if j >= 0 else sp.Integer(0)
    gam = lambda k: sp.expand(sum(x**i * a(k - 1 - i) for i in range(k)))
    A = sp.symbols("PA HA GA OA EA")
    B = sp.symbols("PB HB GB OB EB")
    _, HA, GA, _, EA = A
    _, HB, GB, _, EB = B
    sA, path = A, (sp.Integer(1), 0, 0, 0, 0)
    for k in range(1, k_max + 1):
        sA, path = plant(sA), plant(path)
        lhs = sp.expand(xl(merge(sA, B)) - xl(merge(merge(A, B), path)))
        rho = x * sum((i + 1) * (k - 1 - i) * x**i * a(k - 2 - i) for i in range(k - 1))
        # c_k = x times the right side of Lemma S37, with G-hat = G/x
        rhs = (x * a(k - 1) * (HA * EB + EA * HB) + 2 * gam(k) * GA * GB + 2 * x**2 * gam(k - 1) * (HA * GB + GA * HB)
               + x**2 * (2 * (1 + x) * gam(k) + 3 * x * a(k - 1) + rho) * HA * HB)
        tally.check("A_Delta_k_equals_c_k", sp.expand(lhs - rhs) == 0, {"k": k})
    res = {"skipped": False, "completed": True, "sympy": sp.__version__, "k_max": k_max, **tally.as_dict()}
    return res


# ---------- part B ----------
def build_Tk(rA, rB, k):
    a, b = rA["a"], rB["a"]
    u, v = rA["u"], a + rB["u"]
    edges = [tuple(e) for e in rA["edges"]] + [(p + a, q + a) for p, q in rB["edges"]]
    chain = [u] + list(range(a + b, a + b + k - 1)) + [v]
    edges += list(zip(chain, chain[1:]))
    return edges


def build_Tk_prime(rA, rB, k):
    a, b, u, v = rA["a"], rB["a"], rA["u"], rB["u"]
    m = {w: a + (w if w < v else w - 1) for w in range(b) if w != v}
    m[v] = u
    edges = [tuple(e) for e in rA["edges"]] + [(m[p], m[q]) for p, q in rB["edges"]]
    chain = [u] + list(range(a + b - 1, a + b - 1 + k))
    edges += list(zip(chain, chain[1:]))
    return edges


def part_B(max_order, k_max, budget=None, scales=(1, 1, 1, 1)):
    """`scales` exists for the negative control of the tests only."""
    tally, rows = Tally(), []
    res = {"completed": True}
    a_pol = a_seq(k_max + 2)
    # the sequence a_j against the determinant of the j x j tridiagonal matrix (evaluated at x = 0..j+1)
    from flint import fmpz_mat
    for j in range(0, k_max + 2):
        ok = True
        for x0 in range(0, j + 2):
            val = sum(c * x0**i for i, c in enumerate(a_pol[j]))
            if j:
                M = fmpz_mat(j, j, [(1 + 2 * x0) if r == c else (-x0 if abs(r - c) == 1 else 0)
                                    for r in range(j) for c in range(j)])
                ok &= int(M.det()) == val
            else:
                ok &= val == 1
        tally.check("a_j_is_tridiagonal_determinant", ok, {"j": j})
    top = max_order - 2
    records = {a: [lb.rooted_record(e, a, u) for e, u in lb.rooted_trees(a)] for a in range(2, top + 1)}
    for k in range(1, k_max + 1):
        t0, pairs = time.time(), 0
        for a in range(2, top + 1):
            for b in range(a, top + 1):
                n = a + b + k - 1
                if n > max_order:
                    continue
                if budget is not None and budget.expired():
                    res["completed"], res["stopped_before"] = False, "k=%d, a=%d, b=%d" % (k, a, b)
                    break
                for rA in records[a]:
                    for rB in records[b]:
                        pairs += 1
                        eT, eTp = build_Tk(rA, rB, k), build_Tk_prime(rA, rB, k)
                        ok_graph = len(eT) == n - 1 == len(eTp)
                        tally.check("guard_graphs_have_n_minus_1_edges", ok_graph, dict(a=a, b=b, k=k))
                        lT, lTp = d_of(n, eT) + [0, -4], d_of(n, eTp) + [0, -4]
                        lhs = ptrim(psub(lT, lTp))
                        terms, (p41, p42, p43) = s37_terms(rA, rB, k, a_pol, scales)
                        rhs = ptrim(padd(padd(terms[0], terms[1]), padd(terms[2], terms[3])))
                        where = lambda: dict(edges_A=rA["edges"], root_A=rA["u"], edges_B=rB["edges"], root_B=rB["u"],
                                             k=k, lhs=lhs, rhs=rhs)
                        tally.check("S37_identity", lhs == rhs, where)
                        names = ("S38_term1_in_K(n-1)", "S38_term2_in_K(n)", "S38_term3_in_K(n)", "S38_term4_in_K(n-1)")
                        for nm, term, d in zip(names, terms, (n - 1, n, n, n - 1)):
                            tally.check(nm, in_K(term, d), where)
                        for nm, piece, d in (("S38_term4a_in_K(n-1)", p41, n - 1), ("S38_term4b_in_K(n)", p42, n),
                                             ("S38_term4c_in_K(n-1)", p43, n - 1)):
                            tally.check(nm, in_K(piece, d), where)
                        tally.check("T7_difference_in_C(n-1)", in_Cd(lhs, n - 1), where)
                        tally.check("cone_test_agrees_with_lower_bound_in_C", in_Cd(lhs, n - 1) == lb.in_C(lhs, n - 1), where)
        rows.append(dict(k=k, pairs=pairs, seconds=round(time.time() - t0, 1)))
        print("B", rows[-1], file=sys.stderr, flush=True)
        if not res["completed"]:
            break
    res.update(rooted_orders="2..%d" % top, rows=rows, pairs=sum(r["pairs"] for r in rows), **tally.as_dict())
    return res


# ---------- parts C and E(i): sweep over all trees and all shifts ----------
class PM:
    """Tally of statement (PM) with the minimum margins and the violations."""

    def __init__(self):
        self.tally, self.min1, self.min2, self.w1, self.w2, self.violations = Tally(), None, None, None, None, []

    def add(self, name, n, edgesT, edgesTp, k, dT, dTp):
        okmax, okmin, m1, m2 = pm_margins(dT, dTp)
        info = lambda: dict(n=n, edges_T=[list(e) for e in edgesT], edges_Tprime=[list(e) for e in edgesTp], k=k,
                            peaks_T=sorted({peaks(dT)[0], peaks(dT)[1]}), peaks_Tprime=sorted({peaks(dTp)[0], peaks(dTp)[1]}),
                            d_T=dT, d_Tprime=dTp)
        self.tally.check(name + "_pmax_not_larger", okmax, info)
        self.tally.check(name + "_pmin_not_larger", okmin, info)
        if not (okmax and okmin):
            self.violations.append(info())
        if m1 is not None and (self.min1 is None or m1 < self.min1):
            self.min1, self.w1 = m1, dict(n=n, edges_T=[list(e) for e in edgesT], k=k)
        if m2 is not None and (self.min2 is None or m2 < self.min2):
            self.min2, self.w2 = m2, dict(n=n, edges_T=[list(e) for e in edgesT], k=k)

    def margins(self):
        f = lambda q: None if q is None else dict(exact="%d/%d" % (q.numerator, q.denominator),
                                                   decimal_exploratory=round(float(q), 12))
        return {"margin1_min_pmax": f(self.min1), "witness1": self.w1, "margin2_min_pmin": f(self.min2), "witness2": self.w2}


def verify_violation(n, edgesT, edgesTp):
    """Independent confirmation (Faddeev-LeVerrier) of the d-sequences of both trees of a violation."""
    return dict(independent_d_T=independent_d(n, edgesT), independent_d_Tprime=independent_d(n, edgesTp),
                agree=independent_d(n, edgesT) == d_of(n, edgesT) and independent_d(n, edgesTp) == d_of(n, edgesTp))


def part_CE1(max_c, max_e, budget=None):
    tc, pm = Tally(), PM()
    resC, resE, rowsC, rowsE = {"completed": True}, {"completed": True}, [], []
    stop = False
    for n in range(5, max(max_c, max_e) + 1):
        t0, trees, shifts = time.time(), 0, 0
        for lay in layouts(n):
            if budget is not None and budget.expired():
                for r in (resC, resE):
                    r["completed"], r["stopped_before"] = False, "order %d" % n
                stop = True
                break
            par = parents_from_layout(lay)
            edges = lb.tree_edges(par)
            adjl = adjacency(n, edges)
            dT = d_of(n, edges)
            lT = dT + [0, -4]
            trees += 1
            for x, y, path in tree_shifts(adjl):
                shifts += 1
                k = len(path) - 1
                edgesp = apply_shift(edges, adjl, x, y, path)
                dTp = d_of(n, edgesp)
                if n <= max_c:
                    diff = ptrim(psub(lT, dTp + [0, -4]))
                    where = lambda: dict(n=n, edges_T=[list(e) for e in edges], edges_Tprime=[list(e) for e in edgesp], k=k,
                                         difference=diff)
                    tc.check("T7_difference_in_C(n-1)", in_Cd(diff, n - 1), where)
                    tc.check("T7_difference_in_K(n-1)", in_K(diff, n - 1), where)
                    tc.check("T7_coefficientwise_nonnegative", all(c >= 0 for c in diff), where)
                if n <= max_e:
                    pm.add("PM_exhaustive", n, edges, edgesp, k, dT, dTp)
                    if pm.violations:
                        stop = True
                        break
            if stop:
                break
        row = dict(order=n, trees=trees, shifts=shifts, seconds=round(time.time() - t0, 1))
        if n <= max_c:
            rowsC.append(row)
        if n <= max_e:
            rowsE.append(row)
        print("C/E1", row, file=sys.stderr, flush=True)
        if stop:
            break
    resC.update(rows=rowsC, trees=sum(r["trees"] for r in rowsC), shifts=sum(r["shifts"] for r in rowsC), **tc.as_dict())
    resE.update(rows=rowsE, trees=sum(r["trees"] for r in rowsE), shifts=sum(r["shifts"] for r in rowsE),
                **pm.tally.as_dict(), **pm.margins())
    if pm.violations:
        resE["violations"] = pm.violations[:5]
        resE["independent_verification"] = verify_violation(pm.violations[0]["n"], [tuple(e) for e in pm.violations[0]["edges_T"]],
                                                              [tuple(e) for e in pm.violations[0]["edges_Tprime"]])
        resE["stopped_on_violation"] = True
    return resC, resE, pm


# ---------- part D ----------
def s39_preimage(n, edges):
    """The recipe of the proof of Lemma S39 for a tree that is not a path.  Returns the data of the preimage."""
    adjl = adjacency(n, edges)
    w = next(v for v in range(n) if len(adjl[v]) == 1)
    path, prev, cur = [w], w, adjl[w][0]
    while len(adjl[cur]) == 2:
        path.append(cur)
        prev, cur = cur, (adjl[cur][0] if adjl[cur][0] != prev else adjl[cur][1])
    z = cur  # first vertex of degree >= 3 (exists: the tree is not a path)
    assert len(adjl[z]) >= 3
    k = len(path)  # path z - ... - w has k edges
    off = [v for v in adjl[z] if v != path[-1]]
    out = []
    for split in (1, len(off) // 2):
        n2 = off[split:]
        # T_k(A,B): the neighbours in N_2 of z are moved to w (the far end of the pendant path)
        e2 = [(w, b) if (a == z and b in n2) else ((a, w) if (b == z and a in n2) else (a, b)) for a, b in edges]
        out.append((z, w, k, off[:split], n2, e2))
    return out


def part_D(max_d, max_c, budget=None):
    import networkx as nx
    tally, rows, res = Tally(), [], {"completed": True}
    for n in range(4, max_d + 1):
        if budget is not None and budget.expired():
            res["completed"], res["stopped_before"] = False, "order %d" % n
            break
        t0, trees, equal = time.time(), 0, 0
        dP = d_coefficients(path_parents(n))
        lP = dP + [0, -4]
        for lay in layouts(n):
            par = parents_from_layout(lay)
            edges = lb.tree_edges(par)
            d = d_of(n, edges)
            trees += 1
            diff = ptrim(psub(lP, d + [0, -4]))
            where = lambda: dict(n=n, edges=[list(e) for e in edges], difference=diff)
            tally.check("T8_path_minus_tree_in_C(n-1)", in_Cd(diff, n - 1), where)
            is_path = max(len(a) for a in adjacency(n, edges)) <= 2
            equal += d == dP
            tally.check("T8_equality_only_for_the_path", (d == dP) == is_path, where)
            tally.check("T8_reversed_difference_not_in_C_unless_equal", in_Cd([-c for c in diff], n - 1) == (not diff), where)
            if n <= max_c and not is_path:
                adjl = adjacency(n, edges)
                for z, w, k, n1, n2, e2 in s39_preimage(n, edges):
                    ok = len(e2) == n - 1 and nx.is_tree(nx.Graph(e2))
                    adj2 = adjacency(n, e2)
                    sh = {(x, y): (p) for x, y, p in tree_shifts(adj2)}
                    key = (min(z, w), max(z, w))
                    ok = ok and key in sh and len(sh[key]) - 1 == k
                    ok = ok and leaves(adj2) == leaves(adjl) - 1
                    if ok:
                        zw = sh[key] if key[0] == z else sh[key][::-1]  # the path from z to w
                        back = apply_shift(e2, adj2, z, w, zw)
                        ok = nx.is_isomorphic(nx.Graph(back), nx.Graph(edges))
                    # a, b >= 2: sizes of A and B
                    def comp_size(group):
                        seen, stack = {z}, list(group)
                        seen.update(group)
                        while stack:
                            v = stack.pop()
                            for q in adjl[v]:
                                if q not in seen:
                                    seen.add(q)
                                    stack.append(q)
                        return len(seen)
                    sa = comp_size(n1)
                    tally.check("S39_preimage_valid", ok, lambda: dict(n=n, edges=[list(e) for e in edges], z=z, w=w, k=k))
                    tally.check("S39_a_and_b_at_least_2", len(n1) >= 1 and len(n2) >= 1 and sa >= 2,
                                lambda: dict(n=n, edges=[list(e) for e in edges], z=z, w=w))
        rows.append(dict(order=n, trees=trees, trees_with_l_equal_to_path=equal, seconds=round(time.time() - t0, 1)))
        print("D", rows[-1], file=sys.stderr, flush=True)
    res.update(rows=rows, trees=sum(r["trees"] for r in rows),
               trees_with_l_equal_to_path=sum(r["trees_with_l_equal_to_path"] for r in rows), **tally.as_dict())
    return res


# ---------- part E(ii), (iii): larger trees ----------
def double_star(a, b):
    return 2 + a + b, [(0, 1)] + [(0, 2 + i) for i in range(a)] + [(1, 2 + a + i) for i in range(b)]


def broom(n, s):
    L = n - s
    return n, [(i, i + 1) for i in range(L - 1)] + [(L - 1, L + i) for i in range(s)]


def spider(legs):
    edges, nxt = [], 1
    for ln in legs:
        prev = 0
        for _ in range(ln):
            edges.append((prev, nxt))
            prev, nxt = nxt, nxt + 1
    return nxt, edges


def caterpillar(spine, counts):
    edges = [(i, i + 1) for i in range(spine - 1)]
    nxt = spine
    for i, c in enumerate(counts):
        for _ in range(c):
            edges.append((i, nxt))
            nxt += 1
    return nxt, edges


def distribute(total, parts, weights=None):
    base, rem = divmod(total, parts)
    return [base + (1 if i < rem else 0) for i in range(parts)]


def families(n):
    """(family, name, (order, edges)) for the families of E(ii) at order n."""
    out = []
    m = n - 2
    for a in sorted({1, 2, 3, m // 4, m // 2 - 1, m // 2}):
        if 1 <= a <= m - 1:
            out.append(("double_star", "S(%d,%d)" % (a, m - a), double_star(a, m - a)))
    for s in sorted({3, 5, n // 4, n // 2, (2 * n) // 3}):
        if 2 <= s <= n - 2:
            out.append(("broom", "broom(n=%d,leaves=%d)" % (n, s), broom(n, s)))
    legs2 = [2] * ((n - 1) // 2) + ([1] if (n - 1) % 2 else [])
    out.append(("spider", "legs of length 2 (+1)", spider(legs2)))
    mixed, rest, i = [], n - 1, 0
    while rest > 0:
        ln = min([1, 2, 3][i % 3], rest)
        mixed.append(ln)
        rest -= ln
        i += 1
    out.append(("spider", "legs 1,2,3 cycling", spider(mixed)))
    out.append(("spider", "legs of length 3 (+rest)", spider([3] * ((n - 1) // 3) + ([(n - 1) % 3] if (n - 1) % 3 else []))))
    out.append(("spider", "2*k legs of length 2 and one long leg", spider([2] * (n // 4) + [n - 1 - 2 * (n // 4)])))
    out.append(("spider", "three balanced legs", spider(distribute(n - 1, 3))))
    for sp in sorted({n // 4, n // 3, n // 2}):
        lv = n - sp
        out.append(("caterpillar", "spine %d balanced leaves" % sp, caterpillar(sp, distribute(lv, sp))))
        end = [0] * sp
        end[0], end[-1] = lv - lv // 2, lv // 2
        out.append(("caterpillar", "spine %d leaves at the two ends" % sp, caterpillar(sp, end)))
        one = [0] * sp
        one[0] = lv
        out.append(("caterpillar", "spine %d all leaves at one end" % sp, caterpillar(sp, one)))
        tri = [1 + (i * 2 * (lv - sp)) // (sp * (sp - 1)) if sp > 1 else 0 for i in range(sp)]
        if sum(tri) <= lv:
            tri[-1] += lv - sum(tri)
            out.append(("caterpillar", "spine %d increasing leaf counts" % sp, caterpillar(sp, tri)))
    return out


def prufer_tree(n, rng):
    seq = [rng.randrange(n) for _ in range(n - 2)]
    deg = [1] * n
    for v in seq:
        deg[v] += 1
    edges = []
    for v in seq:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, v))
        deg[leaf] -= 1
        deg[v] -= 1
    u, w = [i for i in range(n) if deg[i] == 1]
    edges.append((u, w))
    return edges


def sample_pm(pm, name, n, edges, nsample, rng):
    adjl = adjacency(n, edges)
    dT = d_of(n, edges)
    allsh = tree_shifts(adjl)
    chosen = allsh if len(allsh) <= nsample else rng.sample(allsh, nsample)
    for x, y, path in chosen:
        edgesp = apply_shift(edges, adjl, x, y, path)
        pm.add(name, n, edges, edgesp, len(path) - 1, dT, d_of(n, edgesp))
        if pm.violations:
            break
    return len(allsh), len(chosen)


def part_E2(orders, sample_small, sample_big, big_from, seed, budget=None):
    pm, rng, rows, res = PM(), random.Random(seed), [], {"completed": True}
    for n in orders:
        if budget is not None and budget.expired():
            res["completed"], res["stopped_before"] = False, "order %d" % n
            break
        t0, nt, nsh_all, nsh = time.time(), 0, 0, 0
        ns = sample_small if n <= big_from else sample_big
        per_family = {}
        for fam, nm, (nn, edges) in families(n):
            assert nn == n and len(edges) == n - 1, (fam, nm, nn, n)
            a_all, a_used = sample_pm(pm, "PM_family", n, edges, ns, rng)
            nt += 1
            nsh_all += a_all
            nsh += a_used
            f = per_family.setdefault(fam, [0, 0, 0])
            f[0] += 1
            f[1] += a_all
            f[2] += a_used
            if pm.violations or (budget is not None and budget.expired()):
                break
        rows.append(dict(order=n, trees=nt, shifts_available=nsh_all, shifts_tested=nsh, sample_cap=ns,
                         per_family={k: dict(trees=v[0], shifts_available=v[1], shifts_tested=v[2]) for k, v in per_family.items()},
                         seconds=round(time.time() - t0, 1)))
        print("E2", {k: v for k, v in rows[-1].items() if k != "per_family"}, file=sys.stderr, flush=True)
        if pm.violations:
            break
    res.update(rows=rows, trees=sum(r["trees"] for r in rows), shifts_tested=sum(r["shifts_tested"] for r in rows),
               **pm.tally.as_dict(), **pm.margins())
    if pm.violations:
        v = pm.violations[0]
        res["violations"] = pm.violations[:5]
        res["independent_verification"] = verify_violation(v["n"], [tuple(e) for e in v["edges_T"]], [tuple(e) for e in v["edges_Tprime"]])
        res["stopped_on_violation"] = True
    return res


def part_E3(n_trees, shifts_each, lo, hi, seed, budget=None):
    pm, rng, res, used = PM(), random.Random(seed), {"completed": True}, 0
    sizes, nt = [], 0
    for i in range(n_trees):
        if budget is not None and budget.expired():
            res["completed"], res["stopped_before"] = False, "tree %d" % i
            break
        n = rng.randint(lo, hi)
        edges = prufer_tree(n, rng)
        _, u = sample_pm(pm, "PM_random", n, edges, shifts_each, rng)
        used += u
        nt += 1
        sizes.append(n)
        if pm.violations:
            break
    res.update(trees=nt, shifts_tested=used, orders=dict(min=min(sizes, default=None), max=max(sizes, default=None)),
               seed=seed, **pm.tally.as_dict(), **pm.margins())
    if pm.violations:
        v = pm.violations[0]
        res["violations"] = pm.violations[:5]
        res["independent_verification"] = verify_violation(v["n"], [tuple(e) for e in v["edges_T"]], [tuple(e) for e in v["edges_Tprime"]])
        res["stopped_on_violation"] = True
    return res


# ---------- part F: the path ----------
def collins_d(n):
    """[d_0, ..., d_{n-2}] from d_{n-k} = C(n+k-1, 2k-1)(k-1)n/k, 2 <= k <= n (exact; divisibility checked)."""
    d = [0] * (n - 1)
    B = comb(n + 1, 3)  # k = 2
    for k in range(2, n + 1):
        num = B * (k - 1) * n
        assert num % k == 0
        d[n - k] = num // k
        if k < n:
            B = B * (n + k) * (n - k) // ((2 * k) * (2 * k + 1))
    return d


def part_F(max_n, matrix_to, budget=None):
    tally, res = Tally(), {"completed": True}
    hi_is, lo_is = {"ceil": [], "floor": [], "neither": []}, {"ceil": [], "floor": [], "neither": []}
    tied, bad_hi, bad_lo = [], [], []
    last = 2
    for n in range(3, max_n + 1):
        if budget is not None and budget.expired():
            res["completed"], res["stopped_before"] = False, "n=%d" % n
            break
        d = collins_d(n)
        last = n
        if n <= matrix_to:
            tally.check("F_closed_form_equals_distance_matrix", d == d_coefficients(path_parents(n)), dict(n=n))
        lo, hi, _ = peaks(d)
        M = n - isqrt(n * n // 5)
        for idx, store in ((hi, hi_is), (lo, lo_is)):
            store["ceil" if idx == M else "floor" if idx == M - 1 else "neither"].append(n)
        tally.check("F_pmax_at_most_M", hi <= M, dict(n=n, pmax=hi, M=M))
        tally.check("F_pmin_at_least_M_minus_1", lo >= M - 1, dict(n=n, pmin=lo, M=M))
        if lo != hi:
            tied.append((n, lo, hi))

    def compress(v):
        return v if len(v) <= 400 else dict(count=len(v), first=v[:40], last=v[-10:], note="list truncated")

    res.update(n_range="3..%d" % last, matrix_checked_to=min(matrix_to, last),
               pmax_equals=dict(ceil_M=len(hi_is["ceil"]), floor_M_minus_1=len(hi_is["floor"]), neither=hi_is["neither"]),
               pmin_equals=dict(ceil_M=len(lo_is["ceil"]), floor_M_minus_1=len(lo_is["floor"]), neither=lo_is["neither"]),
               n_with_pmax_equal_floor=compress(hi_is["floor"]), n_with_pmin_equal_floor=compress(lo_is["floor"]),
               n_with_pmax_equal_ceil_up_to_60=[n for n in hi_is["ceil"] if n <= 60],
               n_with_pmax_floor_up_to_60=[n for n in hi_is["floor"] if n <= 60],
               n_with_tied_peak=compress([list(t) for t in tied]), **tally.as_dict())
    return res


# ---------- provenance ----------
def source_fingerprints():
    here = Path(__file__).resolve().parent
    root = here.parents[1]

    def git(*a):
        done = subprocess.run(["git", *a], cwd=root, capture_output=True, text=True)
        return done.stdout.strip() if done.returncode == 0 else None

    out = {}
    for name in ("tree_shift.py", "lower_bound.py", "distpoly.py", "rooted_state.py"):
        path = here / name
        rel = path.relative_to(root).as_posix()
        at_head, now = git("rev-parse", "--verify", "--quiet", "HEAD:" + rel), git("hash-object", "--", rel)
        out[rel] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "identical_to_git_revision": None if at_head is None or now is None else at_head == now}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--k-max", type=int, default=6, help="largest path length k (part B)")
    ap.add_argument("--n-b", type=int, default=11, help="largest order n = a+b+k-1 (part B)")
    ap.add_argument("--n-c", type=int, default=15, help="largest tree order in part C and in S39 (part D)")
    ap.add_argument("--n-d", type=int, default=17, help="largest tree order in part D (T8)")
    ap.add_argument("--n-e", type=int, default=15, help="largest tree order in E(i), exhaustive")
    ap.add_argument("--e-orders", default="20,30,45,60,80,100,120,150", help="orders of the families of E(ii)")
    ap.add_argument("--e-sample", type=int, default=200, help="shifts per family tree when the order is <= --e-big-from")
    ap.add_argument("--e-sample-big", type=int, default=50, help="shifts per family tree above --e-big-from")
    ap.add_argument("--e-big-from", type=int, default=60)
    ap.add_argument("--e-random-trees", type=int, default=200, help="E(iii): number of random Pruefer trees")
    ap.add_argument("--e-random-shifts", type=int, default=20)
    ap.add_argument("--e-random-orders", default="30,100", help="E(iii): orders drawn uniformly in lo..hi")
    ap.add_argument("--n-f", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20261127)
    ap.add_argument("--time-limit", type=float, default=570.0)
    ap.add_argument("--only", default="ABCDEF", help="parts to run, e.g. BF")
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    meta, sources = run_metadata(), source_fingerprints()
    start = time.time()
    budget = Budget(args.time_limit)
    out = {"experiment": "CJ-0001 exact checks of notes/path-maximality.md (S37, S38, T7, T8, S39) and a falsification "
                         "attempt on the open statement (PM)",
           "arithmetic": "exact integers (python-flint charpoly of the distance matrix), Fractions for margins",
           "scope": "finite checks on the stated ranges; not a proof.  Part E is evidence about an OPEN statement.",
           "run": meta, "sources": sources, "parameters": vars(args)}
    parts = {}
    t0 = time.time()
    if "A" in args.only:
        parts["A"] = part_A()
        parts["A"]["seconds"] = round(time.time() - t0, 1)
    if "B" in args.only:
        t0 = time.time()
        parts["B"] = part_B(args.n_b, args.k_max, budget)
        parts["B"]["seconds"] = round(time.time() - t0, 1)
    if "C" in args.only or "E" in args.only:
        t0 = time.time()
        rc, re1, _ = part_CE1(args.n_c if "C" in args.only else 4, args.n_e if "E" in args.only else 4, budget)
        el = round(time.time() - t0, 1)
        if "C" in args.only:
            rc["seconds"] = el
            parts["C"] = rc
        if "E" in args.only:
            re1["seconds"] = el
            parts["E_i_exhaustive"] = re1
    if "D" in args.only:
        t0 = time.time()
        parts["D"] = part_D(args.n_d, args.n_c, budget)
        parts["D"]["seconds"] = round(time.time() - t0, 1)
    if "E" in args.only and not parts.get("E_i_exhaustive", {}).get("stopped_on_violation"):
        t0 = time.time()
        orders = [int(v) for v in args.e_orders.split(",") if v]
        parts["E_ii_families"] = part_E2(orders, args.e_sample, args.e_sample_big, args.e_big_from, args.seed, budget)
        parts["E_ii_families"]["seconds"] = round(time.time() - t0, 1)
        t0 = time.time()
        lo, hi = [int(v) for v in args.e_random_orders.split(",")]
        parts["E_iii_random"] = part_E3(args.e_random_trees, args.e_random_shifts, lo, hi, args.seed + 1, budget)
        parts["E_iii_random"]["seconds"] = round(time.time() - t0, 1)
    if "F" in args.only:
        t0 = time.time()
        parts["F"] = part_F(args.n_f, 60, budget)
        parts["F"]["seconds"] = round(time.time() - t0, 1)
    out.update(parts)
    # E parts are reported apart from the checks of S37..S39 / T7 / T8: a violation of (PM) is a finding, not a failure of those.
    proved = [k for k in parts if not k.startswith("E_")]
    out["summary"] = {
        "cases": {k: parts[k]["cases_total"] for k in parts},
        "failures": {k: parts[k]["failures_total"] for k in parts},
        "failures_of_checked_statements": sum(parts[k]["failures_total"] for k in proved),
        "pm_violations_found": sum(len(parts[k].get("violations", [])) for k in parts if k.startswith("E_")),
        "completed": all(p["completed"] for p in parts.values()),
        "part_A_skipped": bool(parts.get("A", {}).get("skipped")),
    }
    out["seconds"] = round(time.time() - start, 1)
    for k, p in parts.items():
        print(k, "cases", p["cases_total"], "failures", p["failures_total"], "completed", p["completed"], "seconds", p["seconds"], flush=True)
        for name, first in p["first_failures"].items():
            print("  FIRST FAILURE of", name, json.dumps(first)[:600], flush=True)
    print("summary", json.dumps(out["summary"]), "seconds", out["seconds"], flush=True)
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, indent=1)
            fh.write("\n")
    if out["summary"]["failures_of_checked_statements"] or out["summary"]["pm_violations_found"]:
        return 1
    return 0 if out["summary"]["completed"] else 2


if __name__ == "__main__":
    sys.exit(main())
