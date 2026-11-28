"""Exact rational checks of Theorems A and B of
research/active/CJ-0024-sn-r-nonborder-intersection/notes/weber-uniqueness.md.

Everything is computed with fractions.Fraction (exact). The residual
sup{t in [0,1] : T(x,t) <= y} is NOT taken from the closed form: it is
bracketed by exact bisection on the sublevel set (an initial segment of [0,1]
because T(x,.) is non-decreasing, which is itself checked on the grid), to
width 2**-BISECT, and the closed form is required to lie in the bracket.

A grid check is evidence for the identities, not a proof of them on [0,1];
the proofs are in the note. Usage:  uv run python check_examples.py
"""
from fractions import Fraction as F
from itertools import product
import sys

BISECT = 60
CS = [F(6, 5), F(3, 2), F(7, 4), F(101, 100), F(199, 100)]


def grid(c, n=40):
    pts = {F(k, n) for k in range(n + 1)}
    extra = {c - 1, (c - 1) / 2, (c - 1 + 1) / 2, 2 - c, c / 2, 1 - F(1, 10**6)}
    pts |= {p for p in extra if 0 <= p <= 1}
    return sorted(pts)


# ---- operations ---------------------------------------------------------
def T_A(c):
    return lambda x, y: min(x, y) if max(x, y) == 1 else max(F(0), x + y - c)


def T_B(c):
    return lambda x, y: min(x, y) if (max(x, y) == 1 or x + y > c) else F(0)


def N_c(c):
    return lambda x: F(0) if x == 1 else min(F(1), c - x)


def S_L(a, b):
    return min(F(1), a + b)


def S_star(c):
    return lambda a, b: max(a, b) if a + b < c else F(1)


def T_M(x, y):
    return min(x, y)


def I_WB(x, y):
    return F(1) if x < 1 else y


# closed forms claimed in the note
def I_A_claim(c):
    return lambda x, y: y if x == 1 else min(F(1), c - x + y)


def I_B_claim(c):
    def f(x, y):
        if x == 1:
            return y
        if x <= y:
            return F(1)
        return max(min(F(1), c - x), y)
    return f


# ---- independent residual bracket ---------------------------------------
def residual_bracket(T, x, y):
    """Return (lo, hi) with lo <= sup{t : T(x,t) <= y} <= hi, hi - lo <= 2**-BISECT."""
    if T(x, F(1)) <= y:
        return F(1), F(1)
    if not T(x, F(0)) <= y:  # cannot happen for a t-norm (T(x,0)=0)
        raise AssertionError("T(x,0) > y")
    lo, hi = F(0), F(1)  # lo in the set, hi not in the set
    for _ in range(BISECT):
        mid = (lo + hi) / 2
        if T(x, mid) <= y:
            lo = mid
        else:
            hi = mid
    return lo, hi


# ---- axiom checks -------------------------------------------------------
def check_tnorm(T, G, neutral=F(1), name=""):
    for x in G:
        assert T(x, neutral) == x and T(neutral, x) == x, (name, "neutral", x)
    for x, y in product(G, repeat=2):
        assert T(x, y) == T(y, x), (name, "comm", x, y)
        assert 0 <= T(x, y) <= 1, (name, "range", x, y)
    for i, x in enumerate(G):
        for y in G:
            for x2 in G[i:]:
                assert T(x, y) <= T(x2, y), (name, "mono", x, x2, y)
    for x, y, z in product(G, repeat=3):
        assert T(T(x, y), z) == T(x, T(y, z)), (name, "assoc", x, y, z)


def check_tconorm(S, G, name=""):
    check_tnorm(S, G, neutral=F(0), name=name)


def check_negation(N, G):
    assert N(F(0)) == 1 and N(F(1)) == 0
    for i, x in enumerate(G):
        for x2 in G[i:]:
            assert N(x) >= N(x2)


def check_implication(I, G, name=""):
    assert I(F(0), F(0)) == 1 and I(F(1), F(1)) == 1 and I(F(1), F(0)) == 0, name
    for i, x in enumerate(G):
        for x2 in G[i:]:
            for y in G:
                assert I(x, y) >= I(x2, y), (name, "I1", x, x2, y)
    for x in G:
        for j, y in enumerate(G):
            for y2 in G[j:]:
                assert I(x, y) <= I(x, y2), (name, "I2", x, y, y2)


def main():
    checked = 0
    for c in CS:
        G = grid(c)
        N = N_c(c)
        check_negation(N, G)
        Sst = S_star(c)
        check_tconorm(lambda a, b: S_L(a, b), G, name="S_L")
        check_tconorm(Sst, G, name=f"S*_{c}")
        for label, T, Iclaim, S in (("A", T_A(c), I_A_claim(c), S_L), ("B", T_B(c), I_B_claim(c), Sst)):
            check_tnorm(T, G, name=f"T{label}_{c}")
            check_implication(Iclaim, G, name=f"I{label}_{c}")
            for x, y in product(G, repeat=2):
                lo, hi = residual_bracket(T, x, y)
                v = Iclaim(x, y)
                assert lo <= v <= hi, (label, c, x, y, lo, hi, v)
                assert v == S(N(x), y), (label, c, "(S,N)", x, y)
                assert v == S(N(x), T_M(x, y)), (label, c, "QL", x, y)
                checked += 1
            # failure of (OP) at (c-1, 0), computed from the bracket alone
            lo, hi = residual_bracket(T, c - 1, F(0))
            assert lo >= 1 - F(1, 2**BISECT) and c - 1 > 0
            # the residual is not identically 1 for x < 1: differs from I_WB
            x0 = c / 2  # in ]c-1, 1[
            lo, hi = residual_bracket(T, x0, F(0))
            assert hi < 1 == I_WB(x0, F(0)), (label, c, lo, hi)
            # boundary discontinuity: T(x,1) = x but T(x, 1 - 2**-40) far below x
            xb = (c - 1) / 2 if label == "B" else x0
            assert T(xb, F(1)) == xb and T(xb, 1 - F(1, 2**40)) < xb - (c - 1) / 4
        # the two families differ
        x, y = 1 - F(1, 1000), F(1, 1000)
        assert I_A_claim(c)(x, y) != I_B_claim(c)(x, y)
        print(f"c = {c}: grid of {len(G)} points: all checks passed", flush=True)
    print(f"residual/(S,N)/QL identities checked at {checked} grid pairs")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    sys.exit(main())
