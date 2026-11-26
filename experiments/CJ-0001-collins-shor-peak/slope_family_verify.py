"""CJ-0001, objective O7: independent checker for the failures reported by
slope_family.py and slope_family_extension.py.

This file shares no code with slope_family.py, slope_family_extension.py or
component_form.py, and uses a different method. It imports only the standard
library.

Method (exact rational arithmetic, fractions.Fraction):

- A weighted tree (T, nu) is given by its number of vertices j, its edges on
  the vertices 0..j-1 and the list nu. The hypotheses are checked first: the
  edges form a tree (j - 1 distinct edges between distinct vertices, connected),
  every nu_v is an integer >= 0, and the named vertices exist.
- For an integer t >= 1, M(t) = I + t (L_T + diag nu) is a rational matrix.
  det M(t) and M(t)^(-1) are obtained by Gauss-Jordan elimination, and
  adj(M(t)) = det M(t) * M(t)^(-1). (M(t) is positive definite for t > 0; the
  elimination asserts that it meets no zero pivot.)
- A polynomial Q(x) of degree <= D defined from Phi, adj(M) and p is evaluated
  at t = 1, ..., D + 2 from the definition and recovered by Lagrange
  interpolation through these D + 2 points; the coefficient of x^(D+1) must
  come out as 0 (asserted), and every coefficient must be an integer
  (asserted). The degree bounds are those of the definitions: Phi has degree
  <= j, the entries of adj(M) degree <= j - 1, p_v degree <= 1.
- Membership in the cone C_d: the d + 1 polynomials b_e = x^e (1+x)^(d-2e)
  (2e < d) and b_e = x^e (d <= 2e <= 2d) are written as the columns of a
  (d+1) x (d+1) rational matrix, the system "sum_e c_e b_e = Q" is solved by
  Gauss-Jordan elimination (the matrix is found to be invertible, so the
  expansion is unique), the solution is substituted back and compared with Q,
  and Q is in C_d exactly when every c_e >= 0. In addition the checker reports
  whether Q has a negative coefficient, which by itself excludes Q from every
  C_d (each b_e has non-negative coefficients).

Definitions checked (notes/gamma-components.md and STATE.md, objective O7):
  p_v = 1 + (2 - k_v - nu_v) x,  pi_u = e_u^T adj(M) p,
  F(T, nu, u) = (1 + 5x + 3x^2) Phi + (x + 4x^2) adj(M)_uu + 2 x^2 pi_u,
  S(T, nu, u, v) = x [F(T, nu + e_v, u) - 2 x^3 adj(M(T, nu))_uv],
  R(T, nu) = (N + j - 1)(1 + x) Phi - p^T adj(M) p,  N = sum of nu,
  E(T, nu, w) = R(T, nu0 + e_w) - R(T, nu0), nu0 = nu with nu_w replaced by 0.
Statements: (S) S(T, nu, u, v) in C_{j+3} for all nu >= 0; (E'') F(T, nu, u) in
C_{j+2} for nu >= 0, nu != 0; (E) E(T, nu, w) in C_{j+1} when j >= 2, w is a
leaf of T and every leaf of T has weight >= 1.

Command:

    uv run python experiments/CJ-0001-collins-shor-peak/slope_family_verify.py --out experiments/CJ-0001-collins-shor-peak/results/slope-family-verify.json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


# ---------- hypotheses ----------
def is_tree(j, edges):
    if not isinstance(j, int) or j < 1 or len(edges) != j - 1:
        return False
    seen = set()
    parent = list(range(j))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for edge in edges:
        if len(edge) != 2:
            return False
        a, b = edge
        if not (isinstance(a, int) and isinstance(b, int) and 0 <= a < j and 0 <= b < j and a != b):
            return False
        if frozenset((a, b)) in seen:
            return False
        seen.add(frozenset((a, b)))
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return len({find(a) for a in range(j)}) == 1


def is_weight(j, nu):
    return len(nu) == j and all(isinstance(value, int) and not isinstance(value, bool) and value >= 0 for value in nu)


def degrees(j, edges):
    out = [0] * j
    for a, b in edges:
        out[a] += 1
        out[b] += 1
    return out


# ---------- rational linear algebra ----------
def gauss_jordan(matrix, rhs):
    """Solve matrix * X = rhs (rhs a list of columns as a matrix); returns (det, X). Asserts invertibility."""
    n = len(matrix)
    a = [[Fraction(value) for value in row] + [Fraction(value) for value in extra] for row, extra in zip(matrix, rhs)]
    det = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        assert pivot is not None, "singular matrix"
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        det *= a[col][col]
        inv = 1 / a[col][col]
        a[col] = [value * inv for value in a[col]]
        for r in range(n):
            if r != col and a[r][col] != 0:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[col])]
    return det, [row[n:] for row in a]


def det_and_adjugate_at(j, edges, nu, t):
    """det and adjugate of M(t) = I + t (L_T + diag nu) at the rational point t."""
    deg = degrees(j, edges)
    m = [[Fraction(0)] * j for _ in range(j)]
    for v in range(j):
        m[v][v] = 1 + t * (deg[v] + nu[v])
    for a, b in edges:
        m[a][b] -= t
        m[b][a] -= t
    identity = [[1 if r == c else 0 for c in range(j)] for r in range(j)]
    det, inverse = gauss_jordan(m, identity)
    return det, [[det * value for value in row] for row in inverse]


def interpolate(function, degree):
    """Integer coefficients (lowest first) of the polynomial of degree <= `degree` with the given values."""
    points = [Fraction(t) for t in range(1, degree + 3)]
    values = [function(t) for t in points]
    size = len(points)
    vandermonde = [[t**k for k in range(size)] for t in points]
    _, solution = gauss_jordan(vandermonde, [[value] for value in values])
    coeffs = [row[0] for row in solution]
    assert coeffs[-1] == 0, "degree bound violated"
    assert all(c.denominator == 1 for c in coeffs), "non-integer coefficient"
    out = [int(c) for c in coeffs[:-1]]
    while out and out[-1] == 0:
        out.pop()
    return out


# ---------- the quantities, from their definitions ----------
def f_value_at(j, edges, nu, u, t):
    deg = degrees(j, edges)
    det, adj = det_and_adjugate_at(j, edges, nu, t)
    pi = sum(adj[u][b] * (1 + (2 - deg[b] - nu[b]) * t) for b in range(j))
    return (1 + 5 * t + 3 * t * t) * det + (t + 4 * t * t) * adj[u][u] + 2 * t * t * pi


def f_polynomial(j, edges, nu, u):
    return interpolate(lambda t: f_value_at(j, edges, nu, u, t), j + 2)


def s_polynomial(j, edges, nu, u, v):
    raised = list(nu)
    raised[v] += 1

    def value(t):
        _, adj = det_and_adjugate_at(j, edges, nu, t)
        return t * (f_value_at(j, edges, raised, u, t) - 2 * t**3 * adj[u][v])

    return interpolate(value, j + 3)


def r_value_at(j, edges, nu, t):
    deg = degrees(j, edges)
    det, adj = det_and_adjugate_at(j, edges, nu, t)
    p = [1 + (2 - deg[b] - nu[b]) * t for b in range(j)]
    quadratic = sum(p[a] * adj[a][b] * p[b] for a in range(j) for b in range(j))
    return (sum(nu) + j - 1) * (1 + t) * det - quadratic


def e_polynomial(j, edges, nu, w):
    low = list(nu)
    low[w] = 0
    high = list(low)
    high[w] = 1
    return interpolate(lambda t: r_value_at(j, edges, high, t) - r_value_at(j, edges, low, t), j + 1)


# ---------- the cone C_d ----------
def binomial_row(n):
    row = [1]
    for _ in range(n):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return row


def cone_expansion(poly, d):
    """The unique c with sum_e c_e b_e = poly (as integers when they are), or None if deg poly > d."""
    if len(poly) > d + 1:
        return None
    target = list(poly) + [0] * (d + 1 - len(poly))
    basis = []
    for e in range(d + 1):
        column = [0] * (d + 1)
        if 2 * e < d:
            for i, c in enumerate(binomial_row(d - 2 * e)):
                column[e + i] = c
        else:
            column[e] = 1
        basis.append(column)
    matrix = [[basis[e][row] for e in range(d + 1)] for row in range(d + 1)]
    _, solution = gauss_jordan(matrix, [[value] for value in target])
    c = [row[0] for row in solution]
    back = [sum(c[e] * basis[e][row] for e in range(d + 1)) for row in range(d + 1)]
    assert back == target
    return c


def cone_report(poly, d):
    c = cone_expansion(poly, d)
    if c is None:
        return dict(degree=d, in_cone=False, reason="degree exceeds d", expansion=None,
                    negative_positions=[], has_negative_coefficient=any(v < 0 for v in poly))
    return dict(
        degree=d, in_cone=all(v >= 0 for v in c),
        expansion=[int(v) if v.denominator == 1 else str(v) for v in c],
        negative_positions=[e for e, v in enumerate(c) if v < 0],
        has_negative_coefficient=any(v < 0 for v in poly),
    )


# ---------- instances ----------
def check_s_instance(inst):
    """A claimed failure of (S): hypotheses, then S(T, nu, u, v) not in C_{j+3}."""
    j, edges, nu, u, v = inst["order"], inst["edges"], inst["nu"], inst["u"], inst["v"]
    hyp = is_tree(j, edges) and is_weight(j, nu) and u in range(j) and v in range(j)
    out = dict(kind="S", order=j, edges=edges, nu=nu, u=u, v=v, hypotheses_hold=hyp)
    if hyp:
        poly = s_polynomial(j, edges, nu, u, v)
        out["S"] = poly
        out["agrees_with_reported_polynomial"] = poly == inst["S"]
        out["cone"] = cone_report(poly, j + 3)
        out["violation_confirmed"] = not out["cone"]["in_cone"]
    return out


def check_f_instance(inst):
    """A claimed failure of (E''): hypotheses (nu != 0 included), then F(T, nu, u) not in C_{j+2}."""
    j, edges, nu, u = inst["order"], inst["edges"], inst["nu"], inst["u"]
    hyp = is_tree(j, edges) and is_weight(j, nu) and u in range(j)
    out = dict(kind="E''", order=j, edges=edges, nu=nu, u=u, hypotheses_hold=hyp, nu_nonzero=hyp and any(nu))
    if hyp:
        poly = f_polynomial(j, edges, nu, u)
        out["F"] = poly
        out["agrees_with_reported_polynomial"] = poly == inst["F"]
        out["cone"] = cone_report(poly, j + 2)
        out["violation_confirmed"] = bool(any(nu)) and not out["cone"]["in_cone"]
    return out


def check_e_instance(inst):
    """A reported value of E(T, nu, w) for statement (E): hypotheses, the polynomial, membership in C_{j+1}."""
    j, edges, nu, w = inst["order"], inst["edges"], inst["nu"], inst["w"]
    hyp = is_tree(j, edges) and is_weight(j, nu) and w in range(j) and j >= 2
    if hyp:
        deg = degrees(j, edges)
        hyp = deg[w] == 1 and all(nu[x] >= 1 for x in range(j) if deg[x] == 1)
    out = dict(kind="E", order=j, edges=edges, nu=nu, w=w, hypotheses_hold=hyp)
    if hyp:
        poly = e_polynomial(j, edges, nu, w)
        out["E"] = poly
        out["agrees_with_reported_polynomial"] = poly == inst["E"]
        out["cone"] = cone_report(poly, j + 1)
        out["agrees_with_reported_membership"] = out["cone"]["in_cone"] == inst["in_cone"]
    return out


def git(*a):
    try:
        return subprocess.run(["git", *a], capture_output=True, text=True, check=True, cwd=HERE).stdout.strip()
    except Exception:  # noqa: BLE001
        return "unavailable"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--result", default=str(HERE / "results" / "slope-family.json"))
    ap.add_argument("--extension", default=str(HERE / "results" / "slope-family-extension.json"))
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    start = time.time()
    with open(args.result, encoding="utf-8") as fh:
        result = json.load(fh)
    s_instances = list(result["S"]["failure_examples"])
    smallest = result["S"].get("smallest_failure")
    if smallest is not None and smallest not in s_instances:
        s_instances.append(smallest)
    f_instances = list(result["E2"]["failure_examples"])
    e_instances = []
    if args.extension and Path(args.extension).exists():
        with open(args.extension, encoding="utf-8") as fh:
            extension = json.load(fh)
        for item in extension["instances"]:
            if item.get("E2_failure") is not None:
                f_instances.append(item["E2_failure"])
            if item.get("E_value") is not None:
                e_instances.append(item["E_value"])
        for item in extension.get("E_at_stored_E2_failures", []):
            if item.get("E_value") is not None:
                e_instances.append(item["E_value"])
    else:
        args.extension = None
    checked = dict(
        S=[check_s_instance(inst) for inst in s_instances],
        E2=[check_f_instance(inst) for inst in f_instances],
        E=[check_e_instance(inst) for inst in e_instances],
    )
    summary = dict(
        S_instances=len(checked["S"]),
        S_confirmed=sum(1 for c in checked["S"]
                        if c["hypotheses_hold"] and c["violation_confirmed"] and c["agrees_with_reported_polynomial"]),
        E2_instances=len(checked["E2"]),
        E2_confirmed=sum(1 for c in checked["E2"]
                         if c["hypotheses_hold"] and c["violation_confirmed"] and c["agrees_with_reported_polynomial"]),
        E_instances=len(checked["E"]),
        E_agreeing=sum(1 for c in checked["E"]
                       if c["hypotheses_hold"] and c["agrees_with_reported_polynomial"]
                       and c["agrees_with_reported_membership"]),
        E_in_cone=sum(1 for c in checked["E"] if c["hypotheses_hold"] and c["cone"]["in_cone"]),
    )
    res = dict(summary=summary, checked=checked)
    res["provenance"] = dict(
        command=" ".join(sys.argv if argv is None else ["slope_family_verify.py", *argv]),
        revision=git("rev-parse", "HEAD"), dirty_tree=bool(git("status", "--porcelain")),
        python=sys.version.split()[0], seconds=round(time.time() - start, 1), arguments=vars(args),
    )
    text = json.dumps(res, indent=1)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    print(text)
    ok = (summary["S_confirmed"] == summary["S_instances"] and summary["E2_confirmed"] == summary["E2_instances"]
          and summary["E_agreeing"] == summary["E_instances"])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
