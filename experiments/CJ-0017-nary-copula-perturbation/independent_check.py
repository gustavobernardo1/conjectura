"""Independent exact check (no code shared with box_search.py) that
C_1(x,y,z) = xyz - (x - xyz)(y - xyz)(z - xyz)  [C = product copula]
(a) satisfies the boundary conditions of a 3-copula, and
(b) has negative volume on B = [3/5,4/5] x [4/5,1] x [4/5,1],
computed as the integral over B of the mixed partial d^3 C_1/dx dy dz,
from the monomial expansion of C_1 (polynomials as dicts of exponents)."""
from fractions import Fraction as F
from collections import defaultdict

def mul(p, q):
    r = defaultdict(F)
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[tuple(a + b for a, b in zip(e1, e2))] += c1 * c2
    return {e: c for e, c in r.items() if c}

def add(p, q, s=1):
    r = defaultdict(F, p)
    for e, c in q.items():
        r[e] += s * c
    return {e: c for e, c in r.items() if c}

X = {(1, 0, 0): F(1)}; Y = {(0, 1, 0): F(1)}; Z = {(0, 0, 1): F(1)}
P = mul(mul(X, Y), Z)                      # xyz
C1 = add(P, mul(mul(add(X, P, -1), add(Y, P, -1)), add(Z, P, -1)), -1)

def ev(p, x, y, z):
    return sum(c * x**e[0] * y**e[1] * z**e[2] for e, c in p.items())

# (a) boundary conditions on a grid of rationals
g = [F(k, 7) for k in range(8)]
for s in g:
    for t in g:
        assert ev(C1, F(0), s, t) == 0 and ev(C1, s, F(0), t) == 0 and ev(C1, s, t, F(0)) == 0
    assert ev(C1, s, F(1), F(1)) == s and ev(C1, F(1), s, F(1)) == s and ev(C1, F(1), F(1), s) == s

# (b) mixed partial, then exact integral over the box
D = {}
for (a, b, c), coef in C1.items():
    if a >= 1 and b >= 1 and c >= 1:
        D[(a - 1, b - 1, c - 1)] = D.get((a - 1, b - 1, c - 1), F(0)) + coef * a * b * c
def integ(k, lo, hi):
    return (hi ** (k + 1) - lo ** (k + 1)) / (k + 1)
box = ((F(3, 5), F(4, 5)), (F(4, 5), F(1)), (F(4, 5), F(1)))
V = sum(coef * integ(a, *box[0]) * integ(b, *box[1]) * integ(c, *box[2]) for (a, b, c), coef in D.items())
print("monomials of C_1:", len(C1))
print("volume of B =", V, "=", float(V))
assert V == F(-23, 1953125)
print("CHECK PASSED: boundary conditions hold; V_{C_1}(B) = -23/5^9 < 0")
