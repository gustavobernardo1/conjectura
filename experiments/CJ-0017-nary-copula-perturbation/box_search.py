"""Exploratory-then-exact search for a box of negative C_1-volume, where
C_1 = C - prod_i (x_i - C) and C = Pi (product copula), in dimension n.
All volumes are computed exactly with fractions.Fraction."""
from fractions import Fraction as F
from itertools import product
import sys

def C1_pi(x):
    c = F(1)
    for t in x:
        c *= t
    p = F(1)
    for t in x:
        p *= (t - c)
    return c - p

def volume(f, lo, hi):
    n = len(lo)
    v = F(0)
    for eps in product((0, 1), repeat=n):
        pt = [hi[i] if eps[i] else lo[i] for i in range(n)]
        sign = (-1) ** (n - sum(eps))
        v += sign * f(pt)
    return v

def main(n, den=20):
    best = None
    grid = [F(k, den) for k in range(den + 1)]
    for lo in product(range(den), repeat=n):
        lo_ = [grid[k] for k in lo]
        hi_ = [grid[k + 1] for k in lo]
        v = volume(C1_pi, lo_, hi_)
        if best is None or v < best[0]:
            best = (v, lo_, hi_)
    return best

if __name__ == "__main__":
    for n in (2, 3, 4):
        den = {2: 40, 3: 20, 4: 10}[n]
        v, lo, hi = main(n, den)
        print(n, "min cell volume", v, float(v), "box", [str(t) for t in lo], [str(t) for t in hi], flush=True)
