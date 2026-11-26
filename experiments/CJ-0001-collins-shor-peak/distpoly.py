"""Exact normalized coefficients of the distance characteristic polynomial of a tree.

Notation follows Aalipour et al., arXiv:1507.02341. For a tree T of order n
with distance matrix D, let delta_k be the coefficient of x^k in det(D - xI).
The normalized coefficients are

    d_k(T) = 2^(k-(n-2)) * |delta_k(T)|,      0 <= k <= n-2.

All functions here work with the integers

    s_k(T) = 2^k * |delta_k(T)| = 2^(n-2) * d_k(T),

which have the same order relations as the d_k. Everything is exact integer
arithmetic (python-flint for the characteristic polynomial); no floating point
is used anywhere in this module.
"""

from __future__ import annotations

from math import isqrt

from flint import fmpz_mat
from networkx.generators.nonisomorphic_trees import _next_rooted_tree, _next_tree

# Number of unlabelled trees of order n (OEIS A000055), n = 0..25. Used only
# to validate the enumeration; quoted from the OEIS entry.
A000055 = [1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741, 19320, 48629,
           123867, 317955, 823065, 2144505, 5623756, 14828074, 39299897, 104636890]


def layouts(order: int):
    """Yield one level sequence per isomorphism class of trees of the given order.

    A level sequence lists the depths of the vertices in depth-first preorder
    (root at depth 0). The successor functions are those of networkx (the
    Wright–Richmond–Odlyzko–McKay algorithm); the enumeration is validated in
    the test suite against OEIS A000055 and by an independent canonical form.
    """
    if order < 1:
        return
    if order == 1:
        yield [0]
        return
    layout = list(range(order // 2 + 1)) + list(range(1, (order + 1) // 2))
    while layout is not None:
        layout = _next_tree(layout)
        if layout is not None:
            yield list(layout)
            layout = _next_rooted_tree(layout)


def parents_from_layout(layout) -> list[int]:
    """Parent of each vertex (root has parent -1); always ``parent[i] < i``."""
    base = layout[0]
    last_at_depth: dict[int, int] = {}
    parents = []
    for vertex, depth in enumerate(layout):
        depth -= base
        parents.append(last_at_depth[depth - 1] if depth > 0 else -1)
        last_at_depth[depth] = vertex
    return parents


def distance_matrix(parents: list[int]) -> list[list[int]]:
    """Distance matrix of the tree given by a parent array with ``parent[i] < i``."""
    rows: list[list[int]] = [[0]]
    for vertex in range(1, len(parents)):
        via_parent = rows[parents[vertex]]
        new_row = [via_parent[other] + 1 for other in range(vertex)]
        for other in range(vertex):
            rows[other].append(new_row[other])
        new_row.append(0)
        rows.append(new_row)
    return rows


def scaled_coefficients(parents: list[int]) -> list[int]:
    """Return [s_0, ..., s_{n-2}] with s_k = 2^k |delta_k(T)| (exact integers)."""
    n = len(parents)
    charpoly = fmpz_mat(distance_matrix(parents)).charpoly()  # det(xI - D)
    return [abs(int(charpoly[k])) << k for k in range(n - 1)]


def peak_indices(sequence: list[int]) -> list[int]:
    """All indices at which the sequence attains its maximum."""
    top = max(sequence)
    return [index for index, value in enumerate(sequence) if value == top]


def conjectured_interval(n: int) -> tuple[int, int]:
    """(floor(n/2), ceil(n - n/sqrt(5))) computed in exact integer arithmetic.

    n/sqrt(5) is irrational for n >= 1, so ceil(n - n/sqrt(5)) = n - floor(n/sqrt(5)),
    and floor(n/sqrt(5)) = floor(sqrt(n^2/5)) = isqrt(n^2 // 5).
    """
    return n // 2, n - isqrt(n * n // 5)


def path_parents(n: int) -> list[int]:
    return [-1] + list(range(n - 1))


def star_parents(n: int) -> list[int]:
    return [-1] + [0] * (n - 1)
