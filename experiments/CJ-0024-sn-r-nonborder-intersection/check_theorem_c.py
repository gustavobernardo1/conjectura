"""Exact rational checks of Theorem C of
research/active/CJ-0024-sn-r-nonborder-intersection/notes/rescaled-tnorms.md.

For each base t-norm T0 (left-continuous, strong natural negation N0), each
increasing bijection psi : [0,1] -> [0,a] and each a, the script builds T, S, N
as in the note and checks on a rational grid, in exact arithmetic:
  - t-norm axioms of T, t-conorm axioms of S, negation axioms of N;
  - the residual of T, bracketed by exact bisection on the sublevel set
    (independent of any closed form), equals S(N(x), y) and S(N(x), min(x,y));
  - a <= e: the residual equals the Weber implication on the grid;
  - a > e: I_T(x,0) = 1 at x = psi^-1(N0(a)) > 0, I_T(x,0) < 1 somewhere,
    T(x,t) = 0 for t < 1 near 1 while T(x,1) = x.
Grid evidence supports, and does not prove, the identities on [0,1].
Usage:  uv run python check_theorem_c.py
"""
from fractions import Fraction as F
from itertools import product

ONE, ZERO = F(1), F(0)
BISECT = 50


# ---- base t-norms with strong natural negations ---------------------------
def NC(u):
    return 1 - u


def N3(u):  # piecewise-linear strong negation, fixed point 1/3
    return 1 - 2 * u if u <= F(1, 3) else (1 - u) / 2


def nilmin(N):
    return lambda u, v: min(u, v) if v > N(u) else ZERO


BASES = {
    "Lukasiewicz": (lambda u, v: max(ZERO, u + v - 1), NC, F(1, 2)),
    "nilpotent-min": (nilmin(NC), NC, F(1, 2)),
    "nilmin-N3": (nilmin(N3), N3, F(1, 3)),
}


def dual(T0, N0):
    return lambda p, q: N0(T0(N0(p), N0(q)))


# ---- rescalings ------------------------------------------------------------
def lin(a):
    return (lambda x: a * x), (lambda s: s / a)


def pwl(a):  # a * g, g(x) = 2x on [0,1/4], 1/2 + (2/3)(x - 1/4) on [1/4,1]
    g = lambda x: 2 * x if x <= F(1, 4) else F(1, 2) + F(2, 3) * (x - F(1, 4))
    gi = lambda s: s / 2 if s <= F(1, 2) else F(1, 4) + F(3, 2) * (s - F(1, 2))
    return (lambda x: a * g(x)), (lambda s: gi(s / a))


def build(T0, N0, a, psi, psii):
    S0 = dual(T0, N0)

    def T(x, y):
        if max(x, y) == 1:
            return min(x, y)
        return psii(T0(psi(x), psi(y)))

    def N(x):
        return ZERO if x == 1 else psii(min(a, N0(psi(x))))

    def S(p, q):
        return psii(min(a, S0(psi(p), psi(q))))

    return T, S, N


def residual_bracket(T, x, y):
    if T(x, ONE) <= y:
        return ONE, ONE
    lo, hi = ZERO, ONE
    for _ in range(BISECT):
        mid = (lo + hi) / 2
        if T(x, mid) <= y:
            lo = mid
        else:
            hi = mid
    return lo, hi


def check_assoc_comm_mono(op, G, neutral, name):
    for x in G:
        assert op(x, neutral) == x, (name, "neutral", x)
    for x, y in product(G, repeat=2):
        assert op(x, y) == op(y, x), (name, "comm", x, y)
        assert 0 <= op(x, y) <= 1, (name, "range")
    for i, x in enumerate(G):
        for x2 in G[i:]:
            for y in G:
                assert op(x, y) <= op(x2, y), (name, "mono", x, x2, y)
    for x, y, z in product(G, repeat=3):
        assert op(op(x, y), z) == op(x, op(y, z)), (name, "assoc", x, y, z)


def main():
    n = 24
    configs = 0
    for bname, (T0, N0, e) in BASES.items():
        avals = [e - F(1, 10), e, (e + 1) / 2, e + F(1, 10), F(9, 10)]
        for a in avals:
            for pname, mk in (("linear", lin), ("pwl", pwl)):
                psi, psii = mk(a)
                T, S, N = build(T0, N0, a, psi, psii)
                G = sorted({F(k, n) for k in range(n + 1)}
                           | {p for p in (psii(N0(a)) if N0(a) <= a else None,
                                          psii(N0(a)) / 2 if N0(a) <= a else None,
                                          psii((N0(a) + a) / 2) if N0(a) < a else None) if p is not None})
                name = f"{bname}, a={a}, psi={pname}"
                assert N(ZERO) == 1 and N(ONE) == 0
                for i, x in enumerate(G):
                    for x2 in G[i:]:
                        assert N(x) >= N(x2), (name, "N mono")
                check_assoc_comm_mono(T, G, ONE, "T " + name)
                check_assoc_comm_mono(S, G, ZERO, "S " + name)
                for x, y in product(G, repeat=2):
                    lo, hi = residual_bracket(T, x, y)
                    v = S(N(x), y)
                    assert lo <= v <= hi, (name, x, y, lo, hi, v)
                    assert v == S(N(x), min(x, y)), (name, "QL", x, y)
                    if a <= e:
                        assert v == (ONE if x < 1 else y), (name, "Weber", x, y)
                if a > e:
                    x0 = psii(N0(a))
                    assert 0 < x0 < 1
                    for x in (x0, x0 / 2):
                        lo, hi = residual_bracket(T, x, ZERO)
                        assert lo >= 1 - F(1, 2**BISECT), (name, "OP", x)
                        assert T(x, 1 - F(1, 2**30)) == 0 and T(x, ONE) == x > 0
                    x1 = psii((N0(a) + a) / 2)
                    lo, hi = residual_bracket(T, x1, ZERO)
                    assert hi < 1, (name, "not Weber")
                configs += 1
                print(f"ok: {name} ({len(G)} grid points)", flush=True)
    print(f"ALL CHECKS PASSED for {configs} configurations")


if __name__ == "__main__":
    main()
