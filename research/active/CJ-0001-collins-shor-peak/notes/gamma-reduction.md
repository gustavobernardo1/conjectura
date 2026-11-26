# CJ-0001 — Conjecture Γ: the positive part has the required weight, and a reduction to independent `A`

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 6, after
[`skeleton-locality.md`](skeleton-locality.md) had been committed and sent to
review. Lemma F, Corollary F′ and Proposition S11 have written proofs below;
**none has been reviewed** unless a report under [`../reviews/`](../reviews/)
names this file. They use Proposition S7 and Lemma C of
`skeleton-locality.md`. Nothing here is a claim of novelty, and Conjecture Γ
(MD-0010) remains a conjecture.

Revision history. First version: commit `5622d19`, reviewed by
`claude-opus-5-5` ([`../reviews/2026-11-26-claude-opus-5-5-F-S11.md`](../reviews/2026-11-26-claude-opus-5-5-F-S11.md)):
no gap in the cones, Lemma F, Corollary F′ and Proposition S11; a gap in the
paragraph "What this gives" (the case `A = V` was not accounted for). This
version (same day, session 6) changes: that paragraph (the case `A = V` is
Proposition S3); "strong induction" in Lemma F and a remark that integrality
is needed; the order of the argument that `S′` is a tree; the section on
computation (what the script computes and does not test). No statement or
proof step of Lemma F, Corollary F′ or Proposition S11 was changed.

Notation: that of `skeleton-locality.md` (`S`, `A`, `B = V ∖ A`, `a`, `t`,
`g_w`, `h_w`, `H`, `k_w`, `e_B`, `z`, `L_B`, `Φ_B`).

## The cones `C_d`

For an integer `d ≥ 0` let `C_d` be the set of non-negative combinations of
the polynomials `x^e (1 + x)^i` with integers `e, i ≥ 0`, `e + i ≤ d` and
`2e + i ≥ d`. By Lemma C every element of `C_d` has a non-negative half-gamma
expansion of degree `d`. Directly from the two conditions:

- `C_{d_1} · C_{d_2} ⊆ C_{d_1 + d_2}` (exponents add);
- `x · C_d ⊆ C_{d+2}` and `x² · C_d ⊆ C_{d+2}`;
- `1 ∈ C_0`; `(1 + x) + νx ∈ C_1` for every real `ν ≥ 0`; `α(1 + x) + βx ∈ C_1`
  for `α, β ≥ 0`.

## Lemma F (weight of the forest polynomial)

**Lemma F.** Let `T` be a tree on `j ≥ 1` vertices with vertex set `W` and
Laplacian `L_T`, and let `ν : W → {0, 1, 2, …}` be not identically zero. Then

`Φ(T, ν) := det(I + x (L_T + diag(ν))) ∈ C_j`.

*Proof.* Strong induction on `j` (the statement is used below for trees with
`j − 1` vertices and with at most `j − 2` vertices). For `j = 1`,
`Φ = 1 + νx = (1 + x) + (ν − 1)x` with `ν ≥ 1`, which is in `C_1`.

Let `j ≥ 2`. `T` has at least two leaves. Choose a leaf `w` such that `ν` is
not identically zero on `W ∖ {w}`: if `ν` vanishes outside one leaf, take
another leaf. Let `u` be the neighbour of `w` and `M = I + x(L_T + diag(ν))`.
Row `w` of `M` has the entries `M_ww = 1 + (1 + ν_w)x` and `M_wu = −x`, and
zeros elsewhere; `M` is symmetric. Expanding along row `w` and then along
column `w`,

`det M = (1 + (1 + ν_w)x) · det M[W ∖ w] − x² · Ψ`,  `Ψ := det M[W ∖ {w, u}]`

(`M[R]` is the principal submatrix on `R`). In `T − w` the degree of `u` is
one less than in `T`, and the other degrees are unchanged, so
`M[W ∖ w] = X + x e_u e_uᵀ` with `X = I + x(L_{T−w} + diag(ν))`, and
`X[W ∖ {w, u}] = M[W ∖ {w, u}]`. By linearity of the determinant in row `u`,
`det M[W ∖ w] = Φ(T − w, ν) + xΨ`. Hence

`Φ(T, ν) = (1 + (1 + ν_w)x) · Φ(T − w, ν) + x (1 + ν_w x) · Ψ`.

`T − w` is a tree on `j − 1` vertices on which `ν` is not identically zero, so
`Φ(T − w, ν) ∈ C_{j−1}` by induction; `1 + (1 + ν_w)x = (1 + x) + ν_w x ∈ C_1`;
the first product is in `C_j`.

`T − w − u` is a forest whose components `T_1, …, T_q` (`q ≥ 0`) each contain
exactly one neighbour `u_i` of `u`, because `T` is a tree. The degree in `T`
of a vertex `v` of `T_i` is its degree in `T_i`, plus one if `v = u_i`. So
`M[W ∖ {w, u}]` is block diagonal with blocks `I + x(L_{T_i} + diag(ν + e_{u_i}))`,
and `Ψ = Π_i Φ(T_i, ν + e_{u_i})`. Each weight `ν + e_{u_i}` is integral and
not identically zero on `T_i`, and `|T_i| < j`, so by induction
`Ψ ∈ C_{j−2}` (for `q = 0`: `Ψ = 1 ∈ C_0` and `j = 2`). Then `xΨ ∈ C_j` and
`ν_w x² Ψ ∈ C_j`. ∎

Integrality is used in the base case (`ν ≥ 1` at a single vertex) and cannot
be dropped: for the path on two vertices with `ν = (1/2, 0)`,
`Φ = (1 + 3x/2)(1 + x) − x² = 1 + 5x/2 + x²/2 = (1+x)² + x/2 − x²/2`, which is
not in `C_2` (example found by the reviewer of the first version).

**Corollary F′.** Let `S` be a tree on `s ≥ 2` vertices and `A ⊆ V` with
`1 ≤ a ≤ s − 1`. Then `Φ_B ∈ C_t`, the integer `3 + 3H − 2e_B` is at least 3,
and

`Φ_B · [a(1 + x) + (3 + 3H − 2e_B) x] ∈ C_{t+1}`.

So in the second form of Proposition S7 the first term always has a
non-negative half-gamma expansion of degree `t + 1`; Conjecture Γ is about
absorbing `−x² zᵀ adj(I + xL_B) z` into it.

*Proof.* Let `T_1, …, T_c` be the components of the forest `S[B]` (`c ≥ 1`)
and `ν_w = g_w − k_w` the number of neighbours of `w` in `A`. Then `L_B` is
block diagonal with blocks `L_{T_i} + diag(ν)`. Since `S` is connected and
`A ≠ ∅`, each `T_i` has a vertex with a neighbour in `A`, so `ν` is not
identically zero on `T_i`; by Lemma F and the product rule,
`Φ_B = Π_i Φ(T_i, ν) ∈ C_t`. Next `Σ_B g_w = 2e_B + Σ_B ν_w`, `e_B = t − c`
and `Σ_B ν_w ≥ c`, so
`3 + 3H − 2e_B = 3 + 3Σ_B ν_w + 4e_B − 3t = 3 + t − 4c + 3Σ_B ν_w ≥ 3 + t − c ≥ 3`.
The bracket is in `C_1`, and the product in `C_{t+1}`. ∎

## Proposition S11 (reduction to independent `A`)

**Proposition S11.** Let `S` be a tree on `s ≥ 2` vertices and `A ⊆ V` with
`1 ≤ a ≤ s − 1`. Let `S′` be obtained from `S` by contracting each connected
component of `S[A]` to a single vertex, and let `A′` be the set of the `a′`
contracted vertices. Then `S′` is a tree on `a′ + t ≥ 2` vertices, `A′` is
independent in `S′`, its complement in `S′` is `B`, and

`r_A^S(x) = r_{A′}^{S′}(x) + (a − a′)(1 + x) Φ_B(x)`,  with `(1 + x)Φ_B ∈ C_{t+1}`.

Consequently, if `r_{A′}^{S′}` has a non-negative half-gamma expansion of
degree `t + 1`, then so has `r_A^S`.

*Proof.* `S[A]` is a forest with `a′` components and `a − a′` edges. A vertex
`w ∈ B` cannot have two neighbours in the same component of `S[A]` (that
would close a cycle in `S`), so the contraction creates no parallel edges:
`S′` is a simple graph, the degree of `w` in `S′` is `g_w`, and the
adjacencies inside `B` are unchanged. `S′` is connected and has
`s − (a − a′)` vertices and `s − 1 − (a − a′)` edges, so it is a tree. Two
contracted vertices are not adjacent, since an edge between two components of
`S[A]` would be an edge of `S[A]`. Hence the matrix `L_B` is the
same for `(S, A)` and `(S′, A′)`, and with it `Φ_B`, `H`, `e_B`, `z` and
`adj(I + xL_B)`. In the second form of Proposition S7 only the factor `a` of
`a(1 + x)` differs, which gives the identity. `(1 + x)Φ_B ∈ C_1 · C_t` by
Corollary F′, and the last assertion follows from Lemma C and the uniqueness
of the expansion (the sum of two non-negative expansions of degree `t + 1` is
the expansion of the sum). ∎

**What this gives.** Let *Property Γ⁺* be Property Γ with the condition
`|A| ≥ 2` replaced by `|A| ≥ 1`: for every `A ⊆ V` with `|A| ≥ 1`, `r_A` has a
non-negative half-gamma expansion of degree `s − |A| + 1`. Γ⁺ for all trees
implies Conjecture Γ. In the other direction, three cases:

- `A = V`: the requirement holds for every tree by Proposition S3
  (`r_V = s(1 + x) + 3x`). This case is not covered by S11, which needs
  `a ≤ s − 1`, and `V` is not independent.
- `1 ≤ |A| ≤ s − 1` and `A` independent: this is the hypothesis below.
- `1 ≤ |A| ≤ s − 1` and `A` not independent: by S11 the requirement for
  `(S, A)` follows from the requirement for `(S′, A′)`, where `A′` is
  independent and `1 ≤ |A′| ≤ s′ − 1`.

So **Γ⁺ for all trees follows from Proposition S3 together with Γ⁺ for the
pairs `(S, A)` with `A` independent** (for such a pair
`a = Σ_B ν_w − c + 1`, the smallest value that the forest `S[B]` and the
numbers `ν_w` allow). The extension to `|A| = 1` is needed because a
connected `A` contracts to one vertex. By Proposition S10 the pairs with `B`
independent are done; what remains is: `A` independent and `S[B]` containing
at least one edge.

## Observations from exact computation (not proved)

`experiments/CJ-0001-collins-shor-peak/gamma_pieces.py`, result file
`results/gamma-pieces.json`: for the 47 trees with 2 to 8 vertices and the
7726 subsets with `1 ≤ |A| ≤ s − 1`. The script does not compute `r_A` from
its definition: it computes `r_A` as the second form of Proposition S7, so
what it reports about `r_A` rests on S7 (which `locality_check.py` compares
with the definition on the same trees). It tests `Φ_B` only for the weights
`ν` that arise from a pair `(S, A)`, not Lemma F for arbitrary weights.

- `Φ_B` has a non-negative half-gamma expansion of degree `t`, and the first
  term of S7 one of degree `t + 1`, in every case (consistent with
  Corollary F′);
- **Γ⁺ holds: `r_A` has a non-negative half-gamma expansion of degree `t + 1`
  also for the 325 subsets with `|A| = 1`**, which Conjecture Γ as registered
  does not include;
- the polynomial `zᵀ adj(I + xL_B) z` has non-negative coefficients in every
  case (the entries of `z` can be negative: `z_w = −1` for a leaf of `S` whose
  neighbour is in `B`).

These are finite observations on skeletons with at most 8 vertices.
