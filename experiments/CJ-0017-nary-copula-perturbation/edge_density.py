"""Exact density of C_1 = Pi - prod_i (x_i - Pi) along the edge (t, 1, ..., 1),
for n = 2..8: the polynomial in t, its value at chosen rationals, and whether it
takes negative values on [0,1] (exact: by evaluating at a rational point)."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product

def poly_C1(n):
    # monomials as exponent tuples
    P = {tuple([1]*n): F(1)}
    prod_ = {tuple([0]*n): F(1)}
    for i in range(n):
        xi = {tuple(1 if j == i else 0 for j in range(n)): F(1)}
        fac = dict(xi)
        for e, c in P.items():
            fac[e] = fac.get(e, F(0)) - c
        r = defaultdict(F)
        for e1, c1 in prod_.items():
            for e2, c2 in fac.items():
                r[tuple(a + b for a, b in zip(e1, e2))] += c1 * c2
        prod_ = {e: c for e, c in r.items() if c}
    C1 = dict(P)
    for e, c in prod_.items():
        C1[e] = C1.get(e, F(0)) - c
    return {e: c for e, c in C1.items() if c}

def density_edge(n):
    """coefficients (dict power->coef) of d^n C_1/dx_1..dx_n at (t,1,...,1)."""
    out = defaultdict(F)
    for e, c in poly_C1(n).items():
        if all(k >= 1 for k in e):
            coef = c
            for k in e:
                coef *= k
            out[e[0] - 1] += coef
    return {k: v for k, v in out.items() if v}

for n in range(2, 9):
    d = density_edge(n)
    f = lambda t: sum(c * t**k for k, c in d.items())
    best = min((f(F(k, 1000)), F(k, 1000)) for k in range(1001))
    print(f"n={n}: density(t,1,...,1) = " + " + ".join(f"({c})t^{k}" for k, c in sorted(d.items())),
          f"| min over t in (1/1000)Z: {best[0]} at t={best[1]} ({float(best[0]):.5f})", flush=True)
