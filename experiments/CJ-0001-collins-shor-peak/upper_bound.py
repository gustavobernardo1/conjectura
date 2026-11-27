"""CJ-0001, session 12: exact finite checks of the ingredients of an upper bound on the peak index of d_0..d_{n-2}
through tr(T) = trace (I+L)^{-1}.

Exact arithmetic only: Python integers, fractions.Fraction, python-flint (integer characteristic polynomials and exact
rational inverses).  Floating point appears in two places and is labelled `exploratory`: the decimal renderings of
exact margins, and part F (eigenvalues of D/2).  The 50-digit comparison of part B2 uses `decimal` and is labelled
`high-precision numeric` (not exact).  Finite checks on the stated ranges, not proofs.

Notation.  T tree on n vertices, L its Laplacian, D its distance matrix, d_k the coefficient of x^k in
l_T(x) = -2^{-(n-2)} det(2xI - D) (0 <= k <= n-2; as in distpoly.py / lower_bound.py).
tr(T) = trace of (I+L)^{-1} = -p'(-1)/p(-1) with p(y) = det(yI - L).

Parts.
  V  validation of the three ways to compute tr (charpoly of L, exact inverse in flint, Fraction Gauss-Jordan that shares
       no code with flint) on every tree of order 1..V_MAX, and of the path value against the continuant formula.
  A  path minimality: every tree of order 2..N_A: tr(T) >= tr(P_n), equality only for the path; minimum of
       tr(T) - tr(P_n) over the non-paths per order.
  B1 tr(P_n) - 2/5 > n/sqrt 5 for n = 1..200, exactly (both sides positive, squares compared in Q).
  B2 tr(P_n) = n/sqrt5 + 2/5 + (2n/sqrt5) r^{2n}/(1 - r^{2n}), r = phi^{-2}, to 50 significant digits, n = 1..60
       (high-precision numeric, `decimal`, not exact).
  C  every maximizing index p of d_0..d_{n-2} satisfies p < n - n/sqrt5 + 3/5, i.e. n sqrt5 < 5(n-p)+3, i.e.
       5 n^2 < (5(n-p)+3)^2 (exact integers): every tree of order 3..N_C, and the path P_n for n = 3..N_PATH from
       Collins's closed form d_{n-k}(P_n) = C(n+k-1, 2k-1)(k-1)n/k, itself compared with the distance matrix for
       n <= 30.  For the path: how many n have the peak equal to ceil(n - n/sqrt5) = n - isqrt(n^2 // 5) and the minimum
       of the fractional part of n - n/sqrt5 in those cases.
  D  pendant-path merging: every rooted tree (X,v), 2 <= |X| <= 8, every 1 <= q <= p, p+q <= 8:
       tr(T(p,q)) > tr(T(p+q,0)) exactly (T(p,q): two pendant paths of p and q new vertices at v).
  E  path inequality c(0) >= c(r) for P_{N+1} (vertices 0..N), c(r) = [(I+L)^-2]_rr / [(I+L)^-1]_rr, 1 <= r <= N-1,
       N = 2..60; equality only at N = 2, r = 1.
  F  EXPLORATORY (floating point): every tree of order 3..N_F: with beta_i = -theta_i for the n-1 negative eigenvalues
       theta_i of D/2, sum 1/(1+beta_i) <= n - tr(T) (tolerance 1e-9), and n - tr(T) <= n - tr(P_n) (exact, from A).
  M  regression of the merge identity: rooted trees (A,u), (B,v) glued at u = v into T; g = [(I+L)^-1]_root,root,
       k = [(I+L)^-2]_root,root, eps = 1/g - 1, kappa = k/g^2:  g_T = 1/(1+eps_A+eps_B) and
       tr(T) = tr(A) + tr(B) - g_T - g_T (eps_B kappa_A g_A + eps_A kappa_B g_B), exactly, on all ordered pairs of
       rooted trees with 1 <= |A|, |B| <= 6 (one rooted tree per isomorphism class; |A| = 1 included).

Budget, fixed before the run: 15 minutes of wall-clock in total (--time-limit, default 780 s, tested inside the loops;
when reached the part stops and records where; exit status 2).  Exit status 1: a check failed.
"""
import argparse
import hashlib
import json
import subprocess
import sys
import time
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
from pathlib import Path

from flint import fmpz_mat

import lower_bound as lb
import tree_shift as ts
from distpoly import layouts, parents_from_layout, path_parents, peak_indices, run_metadata, scaled_coefficients
from lower_bound import Budget, Tally, tree_edges


# ---------- exact trace of (I+L)^{-1} ----------
def laplacian_plus_identity(n, edges):
    """Integer matrix I + L of the graph with the given edge list."""
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = 1
    for a, b in edges:
        M[a][a] += 1
        M[b][b] += 1
        M[a][b] -= 1
        M[b][a] -= 1
    return M


def laplacian(n, edges):
    M = laplacian_plus_identity(n, edges)
    for i in range(n):
        M[i][i] -= 1
    return M


def tr_charpoly(n, edges):
    """tr(T) = -p'(-1)/p(-1), p(y) = det(yI - L) (integer characteristic polynomial; exact Fraction)."""
    c = [int(v) for v in fmpz_mat(laplacian(n, edges)).charpoly().coeffs()]
    p = sum(ci * (-1) ** i for i, ci in enumerate(c))
    dp = sum(i * ci * (-1) ** (i - 1) for i, ci in enumerate(c) if i)
    assert p != 0
    return Fraction(-dp, p)


def inverse_entries(n, edges):
    """(I+L)^{-1} as a list of rows of Fractions (flint exact inverse)."""
    Q = fmpz_mat(laplacian_plus_identity(n, edges)).inv()
    return [[Fraction(int(Q[i, j].p), int(Q[i, j].q)) for j in range(n)] for i in range(n)]


def tr_inverse(n, edges):
    Q = inverse_entries(n, edges)
    return sum(Q[i][i] for i in range(n))


def tr_gauss(n, edges):
    """Trace of (I+L)^{-1} by Gauss-Jordan elimination over Fractions (shares no code with flint)."""
    A = [[Fraction(v) for v in row] + [Fraction(int(i == j)) for j in range(n)]
         for i, row in enumerate(laplacian_plus_identity(n, edges))]
    for c in range(n):
        piv = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        inv = 1 / A[c][c]
        A[c] = [v * inv for v in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return sum(A[i][n + i] for i in range(n))


def path_edges(n):
    return [(i, i + 1) for i in range(n - 1)]


def tr_path_continuant(n):
    """tr(P_n) = sum_i theta_{i-1} theta_{n-i} / theta_n, theta_k the leading k x k minors of I+L (tridiagonal:
    diagonal 2,3,...,3,2 for n >= 2, off-diagonal -1; n = 1: I+L = (1)).  Exact; independent of flint."""
    if n == 1:
        return Fraction(1)
    diag = [2] + [3] * (n - 2) + [2]
    # det of the leading k x k block and of the trailing blocks (by the left-right symmetry they agree), by recurrence
    def minors(diagonal):
        th = [1, diagonal[0]]
        for k in range(2, len(diagonal) + 1):
            th.append(diagonal[k - 1] * th[k - 1] - th[k - 2])
        return th
    lead, trail = minors(diag), minors(diag[::-1])
    # (A^{-1})_{ii} = det(A without row/col i) / det A = lead[i-1] * trail[n-i] / lead[n]   (i = 1..n)
    return sum(Fraction(lead[i - 1] * trail[n - i], lead[n]) for i in range(1, n + 1))


def fstr(q):
    return None if q is None else "%d/%d" % (q.numerator, q.denominator)


def fdec(q):
    """Decimal rendering of an exact Fraction; exploratory (floating point)."""
    return None if q is None else float("%.12g" % (q.numerator / q.denominator))


def max_degree(par):
    deg = [0] * len(par)
    for v in range(1, len(par)):
        deg[v] += 1
        deg[par[v]] += 1
    return max(deg)


# ---------- part V ----------
def part_V(v_max, path_to, budget=None):
    tally, res, rows = Tally(), {"completed": True}, []
    for n in range(1, v_max + 1):
        if budget is not None and budget.expired():
            res["completed"], res["stopped_before"] = False, "order %d" % n
            break
        cnt = 0
        for lay in layouts(n):
            edges = tree_edges(parents_from_layout(lay))
            a, b, c = tr_charpoly(n, edges), tr_inverse(n, edges), tr_gauss(n, edges)
            tally.check("V_three_methods_agree", a == b == c, lambda: dict(n=n, edges=edges))
            cnt += 1
        rows.append(dict(order=n, trees=cnt))
    # by hand, from the Laplacian spectra: P_2 {0,2}: 1 + 1/3; P_3 {0,1,3}: 1 + 1/2 + 1/4; K_{1,3} {0,1,1,4}: 1 + 1/2 + 1/2 + 1/5
    tally.check("V_by_hand_P1", tr_charpoly(1, []) == 1)
    tally.check("V_by_hand_P2", tr_charpoly(2, [(0, 1)]) == Fraction(4, 3))
    tally.check("V_by_hand_P3", tr_charpoly(3, [(0, 1), (1, 2)]) == Fraction(7, 4))
    tally.check("V_by_hand_star_K13", tr_charpoly(4, [(0, 1), (0, 2), (0, 3)]) == Fraction(11, 5))
    for n in range(1, path_to + 1):
        tally.check("V_path_continuant_equals_charpoly", tr_path_continuant(n) == tr_charpoly(n, path_edges(n)), dict(n=n))
    res.update(rows=rows, trees=sum(r["trees"] for r in rows), path_to=path_to, **tally.as_dict())
    return res


# ---------- part B ----------
def part_B1(n_max):
    tally, margins = Tally(), []
    for n in range(1, n_max + 1):
        t = tr_path_continuant(n)
        lhs = t - Fraction(2, 5)
        tally.check("B1_lhs_positive", lhs > 0, dict(n=n))
        # lhs > n/sqrt5 <=> lhs^2 > n^2/5 (both sides positive)
        tally.check("B1_tr_minus_2_5_exceeds_n_over_sqrt5", lhs * lhs > Fraction(n * n, 5), dict(n=n))
        margins.append((n, lhs * lhs - Fraction(n * n, 5)))
    nmin, mmin = min(margins, key=lambda t: t[1])
    return dict(completed=True, n_range="1..%d" % n_max, min_square_margin_exact=fstr(mmin), min_square_margin_at_n=nmin,
                **tally.as_dict())


def part_B2(n_max, digits=50, work=90):
    getcontext().prec = work
    s5 = Decimal(5).sqrt()
    phi = (1 + s5) / 2
    r = 1 / (phi * phi)
    tally, worst = Tally(), Decimal(0)
    for n in range(1, n_max + 1):
        t = tr_path_continuant(n)
        exact = Decimal(t.numerator) / Decimal(t.denominator)
        rn = r ** (2 * n)
        formula = n / s5 + Decimal(2) / 5 + (2 * n / s5) * rn / (1 - rn)
        rel = abs(exact - formula) / exact
        worst = max(worst, rel)
        tally.check("B2_formula_agrees_to_50_significant_digits", rel < Decimal(10) ** (-digits), dict(n=n, rel=str(rel)))
    getcontext().prec = 28
    return dict(completed=True, n_range="1..%d" % n_max, kind="high-precision numeric (decimal, working precision %d digits), not exact" % work,
                significant_digits_required=digits, max_relative_difference="%.3e" % worst, **tally.as_dict())


# ---------- part C ----------
def peak_condition(n, p):
    """p < n - n/sqrt5 + 3/5  <=>  5 n^2 < (5(n-p)+3)^2  (m = n-p >= 2 here, so both sides are positive)."""
    return 5 * n * n < (5 * (n - p) + 3) ** 2


def peak_slack(n, p):
    """(5(n-p)+3)^2 - 5 n^2: a positive integer exactly when the condition holds."""
    return (5 * (n - p) + 3) ** 2 - 5 * n * n


def part_C_path(max_n, matrix_to, budget=None):
    tally, res = Tally(), {"completed": True}
    getcontext().prec = 60
    s5 = Decimal(5).sqrt()
    ceil_cases, floor_cases, other, tied = [], [], [], []
    min_frac, min_frac_n, last = None, None, 2
    min_slack, slack_at = None, None
    for n in range(3, max_n + 1):
        if budget is not None and budget.expired():
            res["completed"], res["stopped_before"] = False, "n=%d" % n
            break
        d = ts.collins_d(n)
        last = n
        if n <= matrix_to:
            tally.check("C_path_closed_form_equals_distance_matrix", d == lb.d_coefficients(path_parents(n)), dict(n=n))
        peaks = peak_indices(d)
        for p in peaks:
            tally.check("C_path_every_peak_below_bound", peak_condition(n, p), dict(n=n, p=p))
            sl = peak_slack(n, p)
            if min_slack is None or sl < min_slack:
                min_slack, slack_at = sl, dict(n=n, p=p)
        if len(peaks) > 1:
            tied.append(n)
        top = max(peaks)
        M = n - isqrt(n * n // 5)  # ceil(n - n/sqrt5)
        if top == M:
            ceil_cases.append(n)
            frac = 1 - (n / s5 - isqrt(n * n // 5))  # fractional part of n - n/sqrt5 (n/sqrt5 irrational)
            if min_frac is None or frac < min_frac:
                min_frac, min_frac_n = frac, n
        elif top == M - 1:
            floor_cases.append(n)
        else:
            other.append(n)
    getcontext().prec = 28
    res.update(n_range="3..%d" % last, matrix_checked_to=min(matrix_to, last),
               n_with_peak_equal_ceil=len(ceil_cases), n_with_peak_equal_floor=len(floor_cases), n_with_peak_neither=other,
               n_with_tied_peak=tied,
               first_ceil_cases=ceil_cases[:40],
               min_fractional_part_when_peak_is_ceil=dict(
                   value="%.15f" % min_frac if min_frac is not None else None, at_n=min_frac_n,
                   kind="high-precision numeric (decimal, 60 digits); the exact claim is `peak < n - n/sqrt5 + 3/5`, "
                        "which for peak = ceil(x) says fractional part > 2/5"),
               min_slack_5n2_exact=dict(value=min_slack, at=slack_at,
                                        meaning="min over n, maximizing p of (5(n-p)+3)^2 - 5n^2, an exact positive integer"),
               **tally.as_dict())
    return res


# ---------- part A and C on all trees ----------
def part_AC(n_a, n_c, budget=None):
    ta, tc = Tally(), Tally()
    resA, resC = {"completed": True}, {"completed": True}
    rowsA, rowsC = [], []
    stop = False
    for n in range(2, max(n_a, n_c) + 1):
        t0 = time.time()
        trP = tr_path_continuant(n)
        trees, paths, nonpaths = 0, 0, 0
        min_diff, min_wit = None, None
        max_p, max_p_wit, min_sl, sl_wit = -1, None, None, None
        for lay in layouts(n):
            if budget is not None and budget.expired():
                for r in (resA, resC):
                    r["completed"], r["stopped_before"] = False, "order %d" % n
                stop = True
                break
            par = parents_from_layout(lay)
            edges = tree_edges(par)
            trees += 1
            is_path = max_degree(par) <= 2
            if n <= n_a:
                t = tr_charpoly(n, edges)
                diff = t - trP
                where = lambda: dict(n=n, edges=edges, tr=fstr(t), tr_path=fstr(trP))
                ta.check("A_tr_at_least_tr_path", diff >= 0, where)
                ta.check("A_equality_only_for_the_path", (diff == 0) == is_path, where)
                if is_path:
                    paths += 1
                    ta.check("A_path_value_matches_continuant", diff == 0, where)
                else:
                    nonpaths += 1
                    if min_diff is None or diff < min_diff:
                        min_diff, min_wit = diff, dict(edges=edges)
            if 3 <= n <= n_c:
                s = scaled_coefficients(par)
                for p in peak_indices(s):
                    tc.check("C_peak_below_n_minus_n_over_sqrt5_plus_3_5", peak_condition(n, p),
                             lambda: dict(n=n, edges=edges, p=p))
                    if p > max_p:
                        max_p, max_p_wit = p, dict(edges=edges)
                    sl = peak_slack(n, p)
                    if min_sl is None or sl < min_sl:
                        min_sl, sl_wit = sl, dict(edges=edges, p=p)
        if n <= n_a:
            rowsA.append(dict(order=n, trees=trees, paths=paths, non_paths=nonpaths,
                              min_tr_minus_tr_path_over_non_paths=dict(exact=fstr(min_diff), decimal_exploratory=fdec(min_diff),
                                                                       witness=min_wit),
                              seconds=round(time.time() - t0, 1)))
            print("A", {k: v for k, v in rowsA[-1].items() if k != "min_tr_minus_tr_path_over_non_paths"}, flush=True,
                  file=sys.stderr)
        if 3 <= n <= n_c:
            rowsC.append(dict(order=n, trees=trees, largest_peak_index=max_p, largest_peak_witness=max_p_wit,
                              min_slack_exact=min_sl, min_slack_witness=sl_wit, bound_n_minus_n_over_sqrt5_plus_3_5_exploratory=
                              round(n - n / 5 ** 0.5 + 0.6, 6)))
        if stop:
            break
    resA.update(rows=rowsA, trees=sum(r["trees"] for r in rowsA), **ta.as_dict())
    resC.update(rows=rowsC, trees=sum(r["trees"] for r in rowsC), **tc.as_dict())
    return resA, resC


# ---------- part D ----------
def glue_paths(a, edges, v, lengths):
    """Edge list of X (order a, root v) with a pendant path of `length` new vertices at v for each length."""
    out, nxt = [tuple(e) for e in edges], a
    for ln in lengths:
        prev = v
        for _ in range(ln):
            out.append((prev, nxt))
            prev, nxt = nxt, nxt + 1
    return nxt, out


def part_D(x_max, total_max, budget=None):
    tally, res = Tally(), {"completed": True}
    cases, rooted, min_margin, wit = 0, 0, None, None
    pairs = [(p, q) for p in range(1, total_max) for q in range(1, p + 1) if p + q <= total_max]
    for a in range(2, x_max + 1):
        for edges, v in lb.rooted_trees(a):
            if budget is not None and budget.expired():
                res["completed"], res["stopped_before"] = False, "|X|=%d" % a
                break
            rooted += 1
            for p, q in pairs:
                n1, e1 = glue_paths(a, edges, v, [p, q])
                n2, e2 = glue_paths(a, edges, v, [p + q])
                assert n1 == n2 == a + p + q and len(e1) == len(e2) == n1 - 1
                t1, t2 = tr_charpoly(n1, e1), tr_charpoly(n2, e2)
                tally.check("D_tr_T(p,q)_exceeds_tr_T(p+q,0)", t1 > t2,
                            lambda: dict(X_edges=[list(e) for e in edges], root=v, p=p, q=q, t1=fstr(t1), t2=fstr(t2)))
                cases += 1
                if min_margin is None or t1 - t2 < min_margin:
                    min_margin, wit = t1 - t2, dict(X_edges=[list(e) for e in edges], root=v, p=p, q=q, X_order=a)
    res.update(X_orders="2..%d" % x_max, p_plus_q_at_most=total_max, pairs_pq=len(pairs), rooted_trees=rooted, cases=cases,
               min_margin=dict(exact=fstr(min_margin), decimal_exploratory=fdec(min_margin), witness=wit), **tally.as_dict())
    return res


# ---------- part E ----------
def part_E(n_max):
    tally = Tally()
    equalities, rows, strict_min = [], [], None
    for N in range(2, n_max + 1):
        n = N + 1
        Q = inverse_entries(n, path_edges(n))
        c = []
        for r in range(n):
            q2 = sum(Q[r][j] * Q[j][r] for j in range(n))  # [(I+L)^{-2}]_{rr}
            c.append(q2 / Q[r][r])
        for r in range(1, N):
            ok = c[0] >= c[r]
            tally.check("E_c0_at_least_c_r", ok, lambda: dict(N=N, r=r, c0=fstr(c[0]), cr=fstr(c[r])))
            if c[0] == c[r]:
                equalities.append((N, r))
            else:
                gap = c[0] - c[r]
                if strict_min is None or gap < strict_min[0]:
                    strict_min = (gap, dict(N=N, r=r))
        rows.append(dict(N=N, r_range="1..%d" % (N - 1)))
    tally.check("E_equality_only_at_N2_r1", equalities == [(2, 1)], dict(equalities=equalities))
    cases = sum(N - 1 for N in range(2, n_max + 1))
    return dict(completed=True, N_range="2..%d" % n_max, pairs=cases, equalities=[list(e) for e in equalities],
                min_strict_gap=dict(exact=fstr(strict_min[0]), decimal_exploratory=fdec(strict_min[0]), at=strict_min[1]),
                **tally.as_dict())


# ---------- part M (merge identity) ----------
def rooted_gk(n, edges, root):
    Q = inverse_entries(n, edges)
    g = Q[root][root]
    k = sum(Q[root][j] * Q[j][root] for j in range(n))
    return g, k


def glue(a, eA, u, b, eB, v):
    """T = (A,u) and (B,v) glued at u = v.  Order a + b - 1."""
    m = {w: a + (w if w < v else w - 1) for w in range(b) if w != v}
    m[v] = u
    return a + b - 1, [tuple(e) for e in eA] + [(m[p], m[q]) for p, q in eB]


def merge_sides(trA, gA, kA, trB, gB, kB):
    epsA, epsB = 1 / gA - 1, 1 / gB - 1
    kapA, kapB = kA / gA ** 2, kB / gB ** 2
    gT = 1 / (1 + epsA + epsB)
    return gT, trA + trB - gT - gT * (epsB * kapA * gA + epsA * kapB * gB)


def part_M(max_size, budget=None, perturb=False):
    """`perturb` (negative control for the tests): flips the sign of the correction term."""
    tally, res = Tally(), {"completed": True}
    data = []
    for a in range(1, max_size + 1):
        for edges, u in lb.rooted_trees(a):
            g, k = rooted_gk(a, edges, u)
            data.append((a, edges, u, tr_charpoly(a, edges), g, k))
    pairs = 0
    for (a, eA, u, trA, gA, kA) in data:
        for (b, eB, v, trB, gB, kB) in data:
            if budget is not None and budget.expired():
                res["completed"], res["stopped_before"] = False, "pair %d" % pairs
                break
            n, eT = glue(a, eA, u, b, eB, v)
            assert len(eT) == n - 1
            trT = tr_charpoly(n, eT)
            gTdirect, _ = rooted_gk(n, eT, u)
            gT, rhs = merge_sides(trA, gA, kA, trB, gB, kB)
            if perturb:
                rhs = trA + trB - gT + gT * (((1 / gB - 1) * (kA / gA ** 2) * gA) + ((1 / gA - 1) * (kB / gB ** 2) * gB))
            where = lambda: dict(A=eA, root_A=u, B=eB, root_B=v, tr_T=fstr(trT), rhs=fstr(rhs))
            tally.check("M_g_T_equals_1_over_1_plus_eps_sum", gTdirect == gT, where)
            tally.check("M_tr_T_identity", trT == rhs, where)
            pairs += 1
        if not res["completed"]:
            break
    res.update(max_size=max_size, rooted_trees=len(data), ordered_pairs=pairs, **tally.as_dict())
    return res


# ---------- part F (exploratory, floating point) ----------
def part_F(n_max, budget=None):
    tally, res, rows = Tally(), {"completed": True}, []
    for n in range(3, n_max + 1):
        if budget is not None and budget.expired():
            res["completed"], res["stopped_before"] = False, "order %d" % n
            break
        trP = tr_path_continuant(n)
        trees, min_gap = 0, None
        for lay in layouts(n):
            par = parents_from_layout(lay)
            edges = tree_edges(par)
            D = lb_distance(par)
            roots = fmpz_mat(D).charpoly().complex_roots()
            theta = []
            for r, mult in roots:
                theta += [float(r.real.mid()) / 2] * mult
            neg = [t for t in theta if t < 0]
            tally.check("F_one_positive_and_n_minus_1_negative_eigenvalues", len(neg) == n - 1 and len(theta) == n,
                        lambda: dict(n=n, edges=edges, theta=theta))
            lhs = sum(1.0 / (1.0 - t) for t in neg)  # beta = -theta, 1/(1+beta)
            t = tr_charpoly(n, edges)
            rhs = n - t.numerator / t.denominator  # exploratory float rendering of the exact n - tr(T)
            gap = rhs - lhs
            tally.check("F_sum_inverse_1_plus_beta_at_most_n_minus_tr", gap >= -1e-9, lambda: dict(n=n, edges=edges, lhs=lhs, rhs=rhs))
            tally.check("F_n_minus_tr_at_most_n_minus_tr_path_exact", n - t <= n - trP, lambda: dict(n=n, edges=edges))
            trees += 1
            if min_gap is None or gap < min_gap[0]:
                min_gap = (gap, edges)
        rows.append(dict(order=n, trees=trees, min_gap_exploratory=min_gap[0], witness=min_gap[1]))
    res.update(kind="EXPLORATORY: floating point (flint complex roots, midpoints), tolerance 1e-9; "
                    "the second inequality is exact", rows=rows, trees=sum(r["trees"] for r in rows), **tally.as_dict())
    return res


def lb_distance(par):
    from distpoly import distance_matrix
    return distance_matrix(par)


# ---------- provenance ----------
def git(*a):
    root = Path(__file__).resolve().parents[2]
    done = subprocess.run(["git", *a], cwd=root, capture_output=True, text=True)
    return done.stdout if done.returncode == 0 else None


def source_fingerprints():
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    out = {}
    for name in ("upper_bound.py", "tree_shift.py", "lower_bound.py", "distpoly.py", "rooted_state.py"):
        path = here / name
        rel = path.relative_to(root).as_posix()
        at_head, now = (git("rev-parse", "--verify", "--quiet", "HEAD:" + rel) or "").strip(), (git("hash-object", "--", rel) or "").strip()
        out[rel] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "identical_to_git_revision": (at_head == now) if at_head and now else None}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--v-max", type=int, default=9, help="part V: trees of order 1..v_max by three methods")
    ap.add_argument("--n-a", type=int, default=20, help="part A: all trees of order 2..n_a")
    ap.add_argument("--n-c", type=int, default=18, help="part C: all trees of order 3..n_c")
    ap.add_argument("--n-path", type=int, default=2000, help="part C: the path, n = 3..n_path")
    ap.add_argument("--n-b1", type=int, default=200)
    ap.add_argument("--n-b2", type=int, default=60)
    ap.add_argument("--x-max", type=int, default=8, help="part D: |X| <= x_max")
    ap.add_argument("--pq-max", type=int, default=8, help="part D: p + q <= pq_max")
    ap.add_argument("--n-e", type=int, default=60, help="part E: N = 2..n_e")
    ap.add_argument("--n-f", type=int, default=14, help="part F (exploratory): trees of order 3..n_f")
    ap.add_argument("--m-size", type=int, default=6, help="part M: |A|, |B| <= m_size")
    ap.add_argument("--time-limit", type=float, default=780.0)
    ap.add_argument("--only", default="VBDEMFAC", help="parts to run (A and C share the sweep over all trees)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    meta, sources = run_metadata(), source_fingerprints()
    status = git("status", "--porcelain")
    meta["dirty_files"] = [ln for ln in (status or "").splitlines()] if status is not None else None
    start = time.time()
    budget = Budget(args.time_limit)
    out = {"experiment": "CJ-0001 exact checks around tr(T) = trace (I+L)^{-1} and the upper bound on the peak index",
           "arithmetic": "exact integers / Fractions / python-flint; part B2 high-precision numeric (decimal); part F exploratory floating point",
           "scope": "finite checks on the stated ranges; not a proof",
           "run": meta, "sources": sources, "parameters": vars(args)}
    parts = {}

    def run(key, fn):
        t0 = time.time()
        parts[key] = fn()
        parts[key]["seconds"] = round(time.time() - t0, 1)
        print(key, "cases", parts[key]["cases_total"], "failures", parts[key]["failures_total"],
              "completed", parts[key]["completed"], "seconds", parts[key]["seconds"], flush=True)

    if "V" in args.only:
        run("V", lambda: part_V(args.v_max, 40, budget))
    if "B" in args.only:
        run("B1", lambda: part_B1(args.n_b1))
        run("B2", lambda: part_B2(args.n_b2))
    if "D" in args.only:
        run("D", lambda: part_D(args.x_max, args.pq_max, budget))
    if "E" in args.only:
        run("E", lambda: part_E(args.n_e))
    if "M" in args.only:
        run("M", lambda: part_M(args.m_size, budget))
    if "C" in args.only:
        run("C_path", lambda: part_C_path(args.n_path, 30, budget))
    if "F" in args.only:
        run("F_exploratory", lambda: part_F(args.n_f, budget))
    if "A" in args.only or "C" in args.only:
        t0 = time.time()
        rA, rC = part_AC(args.n_a if "A" in args.only else 2, args.n_c if "C" in args.only else 2, budget)
        el = round(time.time() - t0, 1)
        if "A" in args.only:
            rA["seconds"] = el
            parts["A"] = rA
        if "C" in args.only:
            rC["seconds"] = el
            parts["C_all_trees"] = rC
        for k in [k for k in ("A", "C_all_trees") if k in parts]:
            print(k, "cases", parts[k]["cases_total"], "failures", parts[k]["failures_total"],
                  "completed", parts[k]["completed"], "seconds", parts[k]["seconds"], flush=True)
    out.update(parts)
    exact_parts = [k for k in parts if k != "F_exploratory"]
    out["summary"] = {
        "cases": {k: parts[k]["cases_total"] for k in parts},
        "failures": {k: parts[k]["failures_total"] for k in parts},
        "failures_of_exact_checks": sum(parts[k]["failures_total"] for k in exact_parts),
        "failures_of_exploratory_checks": parts.get("F_exploratory", {}).get("failures_total", 0),
        "completed": all(p["completed"] for p in parts.values()),
    }
    out["seconds"] = round(time.time() - start, 1)
    for k, p in parts.items():
        for name, first in p["first_failures"].items():
            print("  FIRST FAILURE of", k, name, json.dumps(first)[:600], flush=True)
    print("summary", json.dumps(out["summary"]), "seconds", out["seconds"], flush=True)
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, indent=1)
            fh.write("\n")
    if out["summary"]["failures_of_exact_checks"] or out["summary"]["failures_of_exploratory_checks"]:
        return 1
    return 0 if out["summary"]["completed"] else 2


if __name__ == "__main__":
    sys.exit(main())
