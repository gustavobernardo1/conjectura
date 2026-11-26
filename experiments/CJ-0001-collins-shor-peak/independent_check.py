"""Independent recomputation of the normalized coefficients, sharing no code with distpoly.py.

Method. For a tree T of order n >= 2 with Laplacian L and tau_i = 2 - deg(i),
Graham and Lovász's formula D^{-1} = -L/2 + tau tau^T / (2(n-1)) together with
det D = (-1)^(n-1) (n-1) 2^(n-2) and the matrix determinant lemma gives

    ell_T(x) := -2^(-(n-2)) det(2xI - D) = (n-1) det(I + xL) - x * tau^T adj(I + xL) tau,

and the coefficient of x^k in ell_T is the normalized coefficient d_k(T) for
0 <= k <= n-2 (the coefficients of x^(n-1) and x^n are 0 and -4).

Here the right-hand side is evaluated with pure-Python exact polynomial
arithmetic over the integers (fraction-free cofactor expansion via the
Faddeev–LeVerrier recursion), from an edge list. No floating point, no flint,
no networkx.
"""

from __future__ import annotations

from fractions import Fraction


def _matmul(a, b):
    n = len(a)
    return [[sum(a[i][t] * b[t][j] for t in range(n)) for j in range(n)] for i in range(n)]


def _det_and_adjugate_of_I_plus_xL(laplacian):
    """Return (coefficients of det(I + xL), adj(I + xL) as a list of coefficient matrices).

    Faddeev–LeVerrier: with M_1 = I, c_{n-1} = -tr(L), M_{k+1} = L M_k + c_{n-k} I,
    c_{n-k} = -tr(L M_k)/k, one has det(tI - L) = sum c_j t^j and
    adj(tI - L) = sum_{k=1}^n t^(n-k) M_k. Substituting t = -1/x and clearing
    powers of x gives det(I + xL) and adj(I + xL).
    """
    n = len(laplacian)
    identity = [[int(i == j) for j in range(n)] for i in range(n)]
    m = [row[:] for row in identity]
    ms = [m]
    char = [Fraction(0)] * (n + 1)  # char[j] = coefficient of t^j in det(tI - L)
    char[n] = Fraction(1)
    for k in range(1, n + 1):
        lm = _matmul(laplacian, m)
        c = Fraction(-sum(lm[i][i] for i in range(n)), k)
        char[n - k] = c
        if k < n:
            m = [[lm[i][j] + (c if i == j else 0) for j in range(n)] for i in range(n)]
            ms.append(m)
    # det(I + xL) = (-x)^n det(tI - L) at t = -1/x  =>  coefficient of x^k is (-1)^k char[n-k].
    det_coeffs = [(-1) ** k * char[n - k] for k in range(n + 1)]
    # adj(I + xL) = (-x)^(n-1) adj(tI - L) at t = -1/x = sum_k (-x)^(k-1) M_k.
    adj_coeffs = [[[(-1) ** (k - 1) * entry for entry in row] for row in ms[k - 1]] for k in range(1, n + 1)]
    return det_coeffs, adj_coeffs


def normalized_coefficients(n: int, edges: list[tuple[int, int]]) -> list[Fraction]:
    """Return [d_0, ..., d_{n-2}] for the tree on vertices 0..n-1 with the given edges."""
    if len(edges) != n - 1:
        raise ValueError("a tree of order n has n - 1 edges")
    laplacian = [[0] * n for _ in range(n)]
    for u, v in edges:
        laplacian[u][u] += 1
        laplacian[v][v] += 1
        laplacian[u][v] -= 1
        laplacian[v][u] -= 1
    tau = [2 - laplacian[i][i] for i in range(n)]
    det_coeffs, adj_coeffs = _det_and_adjugate_of_I_plus_xL(laplacian)
    ell = [Fraction(0)] * (n + 1)
    for k in range(n + 1):
        ell[k] += (n - 1) * det_coeffs[k]
    for k, matrix in enumerate(adj_coeffs):  # x^k term of adj contributes to x^(k+1)
        quadratic = sum(tau[i] * matrix[i][j] * tau[j] for i in range(n) for j in range(n))
        ell[k + 1] -= quadratic
    if ell[n] != -4 or ell[n - 1] != 0:
        raise AssertionError("top coefficients of ell_T must be -4 and 0; the input is not a tree")
    return ell[: n - 1]
