"""Exact bounds of the density d1 = d^3 C_1/dxdydz of C_1 = Pi - prod(x_i - Pi), n = 3,
on [0,1]^3, decided with z3's nonlinear real arithmetic (exact; nlsat)."""
from fractions import Fraction as F
import z3
x, y, z = z3.Reals("x y z")
e1, e2, e3 = x + y + z, x*y + y*z + z*x, x*y*z
d1 = 4*e2 - 12*e3*e1 + 27*e3*e3
box = [0 <= x, x <= 1, 0 <= y, y <= 1, 0 <= z, z <= 1]
def check(cond, label):
    s = z3.Solver(); s.set("timeout", 120000); s.add(*box); s.add(cond)
    r = s.check(); print(label, r, s.model() if r == z3.sat else "")
    return r
check(d1 < z3.RealVal("-4/15"), "d1 < -4/15 possible?")
check(d1 <= z3.RealVal("-4/15"), "d1 <= -4/15 attained?")
check(d1 > 3, "d1 > 3 possible?")
check(d1 >= 3, "d1 >= 3 attained?")
