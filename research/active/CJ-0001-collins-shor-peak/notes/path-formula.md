# A direct proof of Collins's formula for the path (session 15)

Status: candidate proof, written in session 15 (2026-11-27) by Claude,
model `claude-opus-5-5`; not reviewed when written (its review: journal of
session 15). Exact check: `experiments/CJ-0001-collins-shor-peak/path_formula_check.py`.

**Purpose.** Section 11 of the manuscript (`manuscripts/CJ-0001-collins-shor/main.tex`,
the exact peak of the path and the sharpness of the upper bound) rests on
Collins's formula (C), cited from K. L. Collins, Discrete Appl. Math. 25
(1989) 27–35, Theorem 3, and checked against the distance matrix only for
small `n`. The proof below derives (C) from tools the manuscript already
proves or cites (its Lemma 2.1 and Lemma L1 (the Laplacian form), and the
path cofactor formula Lemma 4.3), plus the Cauchy–Binet formula.

## Statement

Let `P_n` be the path on vertices `1, …, n` (`n ≥ 2`), `L` its Laplacian,
`d_j = d_j(P_n)` the normalized coefficients. Then for `2 ≤ k ≤ n`

    d_{n−k}(P_n) = C(n+k−1, 2k−1) · (k−1) n / k.          (C)

## Proof

Put `M = I + xL`, `Φ_n = det M`, `A_n = det M[V ∖ {1}]`.

**Step 1 (the Laplacian form for the path).** By Lemma L1,
`ℓ_{P_n} = (n−1)Φ_n − x τᵀ adj(M) τ` with `τ_v = 2 − deg v`, so `τ = e_1 + e_n`.
By symmetry of the path, `adj(M)_{nn} = adj(M)_{11} = A_n`; by the path
cofactor formula (Lemma 4.3 of the manuscript), `adj(M)_{1n} = x^{n−1} det M[∅] = x^{n−1}`.
Hence

    ℓ_{P_n} = (n−1)Φ_n − 2x A_n − 2x^n,

and for `0 ≤ j ≤ n−2`, `d_j = [x^j]ℓ_{P_n} = (n−1)[x^j]Φ_n − 2[x^{j−1}]A_n`.

**Step 2 (forest expansions).** Let `B` be an oriented vertex–edge incidence
matrix of a tree `T` (`n × (n−1)`), so that `L = BBᵀ`. For `W ⊆ V` let `B_W`
be the rows of `B` indexed by `W`. Then `M[W] = I + x B_W B_Wᵀ` and, by
`det(I + XY) = det(I + YX)` and the Cauchy–Binet formula,

    det M[W] = det(I_{n−1} + x B_Wᵀ B_W) = Σ_{S ⊆ E} x^{|S|} det(B_W[·, S]ᵀ B_W[·, S])
             = Σ_{S ⊆ E} x^{|S|} Σ_{R ⊆ W, |R| = |S|} det(B[R, S])².

For a set `S` of edges (a spanning forest of `T` with components
`C_1, …, C_r`, `r = n − |S|`, isolated vertices included), every edge of `S`
has both ends in one component, so after ordering rows and columns by
components the square matrix `B[R, S]` is block-diagonal with blocks
`B[R ∩ C_i, S ∩ E(C_i)]` of size `|R ∩ C_i| × (|C_i| − 1)`. It is nonsingular
exactly when every block is square and nonsingular, i.e. when `R` omits
exactly one vertex of each component (if some block has fewer rows than
columns, another has more rows than columns, and the matrix is singular);
then each block is the incidence matrix of a tree with one row removed,
whose determinant is `±1`. Hence

    Φ = det M      = Σ_S x^{|S|} Π_i |C_i|,
    det M[V ∖ {u}] = Σ_S x^{|S|} Π_{i : u ∉ C_i} |C_i|

(in the second, `R` must omit `u` itself from the component containing `u`).

**Step 3 (the path).** For `P_n` the spanning forests with `r` components are
in bijection with the compositions `(c_1, …, c_r)` of `n` (the component
sizes from vertex 1 to vertex `n`), with `|S| = n − r`. So

    [x^{n−r}] Φ_n = Σ_{c_1+…+c_r = n} c_1 c_2 ⋯ c_r = [z^n] (z/(1−z)²)^r = C(n+r−1, 2r−1),
    [x^{n−r}] A_n = Σ_{c_1+…+c_r = n} c_2 ⋯ c_r = [z^n] (z/(1−z)) (z/(1−z)²)^{r−1} = C(n+r−2, 2r−2),

using `Σ_{c ≥ 1} c z^c = z/(1−z)²`, `Σ_{c ≥ 1} z^c = z/(1−z)` and
`[z^m](1−z)^{−a} = C(m+a−1, a−1)`.

**Step 4.** With `j = n − k`, `2 ≤ k ≤ n`: `[x^{n−k}]Φ_n = C(n+k−1, 2k−1)` (Step
3, `r = k`) and `[x^{n−k−1}]A_n = C(n+k−1, 2k)` (Step 3, `r = k+1`; for `k = n`
both sides are 0). Since `C(n+k−1, 2k) = C(n+k−1, 2k−1)(n−k)/(2k)`,

    d_{n−k} = C(n+k−1, 2k−1) [(n−1) − (n−k)/k] = C(n+k−1, 2k−1) (k−1) n / k.   ∎

## Remarks

- Step 2 is the matrix-forest theorem for `det(I + xL)` and its principal
  minors (classical; proved here so that nothing beyond Cauchy–Binet is
  cited). Steps 1–4 use no property of `P_n` beyond its forests being
  compositions and the cofactor formula.
- The same computation gives, for every tree, `[x^j]Φ = Σ` over spanning
  forests with `j` edges of the product of the component sizes (the known
  forest expansion of Laplacian coefficients).
- Collins's own proof goes through his thesis; this one is independent of it.
  Novelty of the proof: not searched.

## Exact check

`path_formula_check.py`: for every `n` in the stated range, `Φ_n`, `A_n` and
`ℓ_{P_n}` by exact determinants and interpolation; the coefficient formulas of
Step 3; the identity of Step 1; (C) against the distance matrix; and the two
composition sums by brute force for `n ≤ 12`. Result:
`results/path-formula-check.json`.
