"""Saved without change from the scratch directory of session 12 (claude-opus-5-5, 2026-11-26), where it ran:
    uv run --with sympy==1.14.0 python tree_shift_symbolic.py   ->  "F - closed form = 0", sympy 1.14.0.
Draft: no README entry and no test yet (journal, session 12). Proof context: notes/path-maximality.md, Lemma S37.
"""
"""Session 12 (scratch): the closed form of the generalized-tree-shift difference, for EVERY path length k,
as an identity of rational generating functions in t (exact, sympy).

State of a rooted tree (zero weights): s = (Psi, H, G, Omega, E)  (notes/lower-bound.md, S33, S34).
plant is linear: s' = P s (S19(c), S34(b)); merge is bilinear (S19(d), S34(c)); x*l = E + Om + 2xG + x(1+4x)H - 4x^2 Psi.
T_k = merge(plant^k(A), B),  T'_k = merge(merge(A, B), plant^k(point)).
Claim: sum_{k>=0} x(l_{T_k} - l_{T'_k}) t^k equals the generating function of the closed form below."""
import sympy as sp

x, t = sp.symbols("x t")
A = sp.symbols("PA HA GA OA EA")
B = sp.symbols("PB HB GB OB EB")

P = sp.Matrix([
    [1 + x, x, 0, 0, 0],            # Psi' = (1+x)Psi + xH
    [1, x, 0, 0, 0],                # H'   = Psi + xH
    [0, x**2, x, 0, 0],             # G'   = x^2 H + xG
    [0, x * (1 + x), 0, 1 + x, 1],  # Om'  = E + (1+x)Om + x(1+x)H
    [0, x**2 * (3 + 2 * x), 2 * x, x, x],  # E' = xE + xOm + 2xG + x^2(3+2x)H
])


def merge(s, u):
    P1, H1, G1, O1, E1 = s
    P2, H2, G2, O2, E2 = u
    return (P1 * P2, H1 * P2 + H2 * P1, G1 * P2 + G2 * P1, O1 * P2 + O2 * P1,
            E1 * P2 + E2 * P1 + x * (H1 * O2 + H2 * O1) - 2 * G1 * G2)


def xl(s):
    Ps, H, G, O, E = s
    return E + O + 2 * x * G + x * (1 + 4 * x) * H - 4 * x**2 * Ps


# sum_k P^k t^k = (I - tP)^{-1}; merge and xl are (bi)linear, so they commute with the summation.
R = (sp.eye(5) - t * P).inv()
SA = tuple(sp.simplify(v) for v in (R * sp.Matrix(A)))
SP = tuple(sp.simplify(v) for v in (R * sp.Matrix([1, 0, 0, 0, 0])))
F = xl(merge(SA, B)) - xl(merge(merge(A, B), SP))

# closed form: a_j = det of the j x j tridiagonal matrix (1+2x on the diagonal, -x beside it);
# sum_j a_j t^j = 1/Q,  Q = 1 - (1+2x)t + x^2 t^2.
Q = 1 - (1 + 2 * x) * t + x**2 * t**2
Agf = 1 / Q
g_a_km1 = t * Agf                                   # sum_{k>=1} a_{k-1} t^k
g_gam = t * Agf / (1 - x * t)                       # sum_{k>=1} gamma_k t^k,  gamma_k = sum_{i<k} x^i a_{k-1-i}
g_gam_km1 = t * g_gam                               # sum_{k>=1} gamma_{k-1} t^k
g_rho = x * t**2 / (1 - x * t)**2 * sp.diff(t * Agf, t)   # rho_k = x sum_{i+j=k-2} (i+1) x^i (j+1) a_j
PA, HA, GA, OA, EA = A
PB, HB, GB, OB, EB = B
Gcl = (x * g_a_km1 * (HA * EB + EA * HB) + 2 * g_gam * GA * GB + 2 * x**2 * g_gam_km1 * (HA * GB + GA * HB)
       + x**2 * (2 * (1 + x) * g_gam + 3 * x * g_a_km1 + g_rho) * HA * HB)

diff = sp.simplify(sp.together(F - Gcl))
print("F - closed form =", diff)
assert diff == 0

# the sequences used in the closed form agree with their definitions (first terms)
def a(j):
    if j < 0:
        return sp.Integer(0)
    M = sp.Matrix(j, j, lambda r, c: 1 + 2 * x if r == c else (-x if abs(r - c) == 1 else 0))
    return sp.expand(M.det()) if j else sp.Integer(1)

ser = sp.series(Agf, t, 0, 8).removeO()
assert all(sp.expand(ser.coeff(t, j) - a(j)) == 0 for j in range(8))
ser = sp.series(g_rho, t, 0, 9).removeO()
for k in range(1, 9):
    direct = x * sum((i + 1) * (k - 1 - i) * x**i * a(k - 2 - i) for i in range(k - 1))
    assert sp.expand(ser.coeff(t, k) - direct) == 0
print("generating functions of a_j and rho_k agree with their definitions up to t^8")
print("sympy", sp.__version__)
