# CJ-0001 — trees with pendant leaves on a skeleton: an expansion, and an order-independent positivity property

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 5. Lemma S1 and Propositions S2, S3, S4 have written
proofs below; **none has been reviewed**. Property Γ is verified by exact
computation for the 47 trees with 2 to 8 vertices and is a conjecture in
general (registered as MD-0010). Nothing here is a claim of novelty.

This file generalizes [`vertex-principle.md`](vertex-principle.md) from
caterpillars to all trees and replaces its Lemma L3′ (a sketch) by Lemma S1.
Notation: `ℓ_T`, `d_k`, `δ_k` as in [`lemmas.md`](lemmas.md); `C(N, i) = 0`
when `i < 0` or `i > N`.

## Setting

Let `S` be a tree on `s ≥ 2` vertices (the *skeleton*) with vertex set `V`
and distance matrix `P`, and let `c = (c_v)_{v ∈ V}` be non-negative integers.
`S(c)` is the tree obtained by attaching `c_v` pendant leaves at each `v`; its
order is `n = s + Σ c_v`. Every tree with at least two non-leaf vertices is of
this form (take for `S` the tree induced by the non-leaf vertices), and so is
every tree `S(c)` with some `c_v = 0`. Caterpillars are the case where `S` is
a path.

`J` is the all-ones matrix, `1` the all-ones vector, `C = diag(c)`. For
`A ⊆ V`: `a = |A|`, `Ā = V ∖ A`, `1_A` the indicator vector of `A`, `I_A` the
diagonal matrix with diagonal `1_A`, and `c^A = Π_{v ∈ A} c_v`. Put

```
Q(c) = |  P        (P + J) C        |          G(c; x) = det(2xI − Q(c)),
       |  P + J    (P + 2J) C − 2I  |
```

and define `g_0(c), …, g_{2s}(c)` by `−G(c; x)/4^{s−1} = Σ_j g_j(c) x^j`. For a
path this is the matrix of Lemma L3. Each `c_v` occurs only in column `s + v`,
so `G` and every `g_j` are of degree at most 1 in each `c_v`.

## Lemma S1 (the closed form, empty classes included)

**Lemma S1.** If `n ≥ 2s`, then `ℓ_{S(c)}(x) = (x+1)^{n−2s} Σ_j g_j(c) x^j`, that
is, `d_k(S(c)) = Σ_{j=0}^{2s} g_j(c) C(n − 2s, k − j)` for `0 ≤ k ≤ n − 2`.

*Proof.* Let `Z = {v : c_v = 0}` and `s′ = s − |Z|`. Partition the vertices of
`T = S(c)` into the `s` singletons `{v}` and the `s′` non-empty leaf classes.
The sum of the distances from a vertex to the vertices of a class depends only
on the class of the vertex, so the partition is equitable for the distance
matrix `D` of `T`; its quotient matrix `Q′` is `Q(c)` with the rows and columns
`s + v`, `v ∈ Z`, deleted. As in the proof of Lemma L3: the vectors constant on
classes form a `D`-invariant subspace on which `D` acts as `Q′`; its orthogonal
complement is `D`-invariant because `D` is symmetric, is spanned by the vectors
supported on one leaf class with entries summing to zero, and `D` acts on it
as `−2` (two leaves of a class are at distance 2 and have equal distances to
every other vertex). Its dimension is `Σ_{v ∉ Z} (c_v − 1) = n − s − s′`. Hence
`det(2xI − D) = (2x + 2)^{n−s−s′} det(2xI − Q′)`.

For `v ∈ Z`, column `s + v` of `2xI − Q(c)` has the entry `2x + 2` on the
diagonal and `0` elsewhere (the entries `(P_{uv} + 1) c_v` and
`(P_{uv} + 2) c_v` vanish, and the diagonal entry of `Q(c)` is `2c_v − 2 = −2`).
Expanding along these `|Z|` columns, `G(c; x) = (2x + 2)^{|Z|} det(2xI − Q′)`.
Since `n − s − s′ − |Z| = n − 2s ≥ 0`,

`ℓ_T(x) = −2^{−(n−2)} det(2xI − D) = −2^{−(n−2)} (2x+2)^{n−2s} G(c; x) = (x+1)^{n−2s} · (−G(c; x)/4^{s−1})`,

and the coefficient of `x^k` in `ℓ_T` is `d_k` (Fact 1.1 and Observation 3.1
of arXiv:1507.02341). ∎

## Proposition S2 (expansion over subsets)

**Proposition S2.** `G(c; x) = Σ_{A ⊆ V} c^A γ_A(x)`, where for `x ≠ 0`

`γ_A(x) = (2x + 2)^{s−a} (2x)^a det N_A(x)`, `N_A(x) = 2x I_Ā − P − 1_A 1ᵀ − 1 1_Aᵀ − (a/2x) J`.

*Proof.* Column `s + v` of `2xI − Q(c)` is `c_v u_v + (2x + 2) e_{s+v}`, where
`u_v` has the entries `−(P_{uv} + 1)` in the rows `u ≤ s` and `−(P_{uv} + 2)` in
the rows `s + u`. The determinant is linear in each column, so
`G = Σ_A c^A γ_A` with `γ_A` the determinant in which column `s + v` is `u_v`
for `v ∈ A` and `(2x+2) e_{s+v}` for `v ∉ A`. Expanding along the latter
columns, `γ_A = (2x+2)^{s−a} det M_A` with

```
M_A = |  2xI − P            −(P + J)[V, A]   |
      |  −(P + J)[A, V]     −(P + 2J)[A, A]  |
```

(`X[R, K]` is the submatrix with rows `R` and columns `K`). For each `b ∈ A`
subtract row `b` from row `s + b`: that row becomes `−(2x e_bᵀ + 1ᵀ)` in the
first block and `−1ᵀ` in the second. Then for each `b ∈ A` subtract column `b`
from column `s + b`: the upper part becomes `−(2x e_b + 1)` and the lower part
becomes `2x e_b`. So

```
det M_A = det |  2xI − P             −(2xI + J)[V, A]  |
              |  −(2xI + J)[A, V]    2x I              |
```

For `x ≠ 0` the Schur complement of the lower right block gives
`det M_A = (2x)^a det( 2xI − P − (1/2x) (2xI + J)[V, A] (2xI + J)[A, V] )`, and
`(2xI + J)[V, A] (2xI + J)[A, V] = Σ_{b ∈ A} (2x e_b + 1)(2x e_b + 1)ᵀ = 4x² I_A + 2x (1_A 1ᵀ + 1 1_Aᵀ) + a J`. ∎

`J` has rank one, so `det N_A(x)` is of degree at most 1 in `1/x`, and it is of
degree at most `s − a` in `x`. Hence

`p_A(x) := −γ_A(x)/4^{s−1} = x^{a−1} (1+x)^{s−a} r_A(x)`, with `r_A(x) = −2^{2−s} · x · det N_A(x)` a polynomial of degree at most `d = s − a + 1`.

`p_A` is the coefficient of `c^A` in `Σ_j g_j(c) x^j`, and by Lemma S1

`ℓ_{S(c)}(x) = Σ_{A ⊆ V} c^A x^{a−1} (1+x)^{n−s−a} r_A(x)`.

## Proposition S3 (the top coefficient)

**Proposition S3.** For every tree `S` on `s ≥ 2` vertices,
`r_V(x) = (s + 3)x + s`. Equivalently, the product of all the `c_v` occurs in
`g_{s−1}` with coefficient `s`, in `g_s` with coefficient `s + 3`, and in no
other `g_j`.

*Proof.* `N_V(x) = −(P + αJ)` with `α = 2 + s/(2x)`. By the matrix determinant
lemma `det(P + αJ) = det(P) (1 + α 1ᵀP^{−1}1)`. For the distance matrix of a
tree on `s` vertices, `det P = (−1)^{s−1} (s−1) 2^{s−2}` (Graham–Pollak) and
`P^{−1} = −L/2 + ττᵀ/(2(s−1))` with `L` the Laplacian and `τ_v = 2 − deg(v)`
(Graham–Lovász 1978, Lemma 1, as used for L1 in `lemmas.md`); since `L1 = 0`
and `1ᵀτ = 2s − 2(s−1) = 2`, `1ᵀP^{−1}1 = 2/(s−1)`. So
`det(P + αJ) = (−1)^{s−1} 2^{s−2} (s − 1 + 2α) = (−1)^{s−1} 2^{s−2} (s + 3 + s/x)`,
`det N_V = (−1)^s det(P + αJ) = −2^{s−2} (s + 3 + s/x)`, and
`r_V = −2^{2−s} x det N_V = (s+3)x + s`. Then `p_V = x^{s−1} r_V`. ∎

This proves, for every `s` and every skeleton, the pattern observed for paths
with `s ≤ 8` in `vertex-principle.md`. The two values of the coefficient of
`c^V` in `d_m − d_{m−1}` computed there follow.

## Proposition S4 (a positivity property that does not depend on the order)

Fix `S` and `n ≥ 2s`, `m = ⌊n/2⌋`, and let
`D_n(c) = Σ_j g_j(c) [C(n−2s, m−j) − C(n−2s, m−1−j)]`, which is of degree at
most 1 in each `c_v` and equals `d_m − d_{m−1}` of `S(c)` when `Σ c_v = n − s`
(Lemma S1). Its coefficient of `c^A` is

`β_A(n) = ([x^m] − [x^{m−1}]) (1+x)^{n−2s} p_A(x) = ([x^m] − [x^{m−1}]) x^{a−1} (1+x)^{n−s−a} r_A(x)`.

**Definition (Property Γ).** A polynomial `r` of degree at most `d` has a
*non-negative half-gamma expansion of degree `d`* if

`r(x) = Σ_{0 ≤ e, 2e < d} ρ_e x^e (1+x)^{d−2e} + Σ_{d ≤ 2e ≤ 2d} σ_e x^e` with all `ρ_e ≥ 0` and `σ_e ≥ 0`.

(The polynomials `x^e (1+x)^{d−2e}`, `2e < d`, and `x^e`, `d ≤ 2e ≤ 2d`, form a
basis of the polynomials of degree at most `d`, so the expansion is unique and
is computed from the lowest degree upwards.) The skeleton `S` *has
Property Γ* if for every `A ⊆ V` with `|A| ≥ 2` the polynomial `r_A` has a
non-negative half-gamma expansion of degree `d = s − |A| + 1`.

**Proposition S4.** If `r_A` has a non-negative half-gamma expansion of degree
`d = s − a + 1`, then `β_A(n) ≥ 0` for every `n ≥ 2s`.

*Proof.* For integers `L ≥ 0` and `r` with `2r ≤ L + 1`:
`C(L, r) ≥ C(L, r−1)` (if `r ≤ 0` the right side is `0`; if `r ≥ 1` then
`r ≤ L` and `C(L, r)/C(L, r−1) = (L − r + 1)/r ≥ 1`). A term `x^e (1+x)^j` of
`r_A` contributes to `β_A(n)` the amount `C(L, r) − C(L, r−1)` with
`L = n − s − a + j ≥ 0` and `r = m − a + 1 − e`. Since `2m ≤ n`,
`2r ≤ n − 2a + 2 − 2e`, and `L + 1 = n − s − a + j + 1`; so `2r ≤ L + 1` holds as
soon as `2e + j ≥ s − a + 1 = d`. For the terms of the first kind
`2e + (d − 2e) = d`, and for those of the second kind `j = 0` and `2e ≥ d`. ∎

**Corollary S5 (conditional on Property Γ for `S`).** If `S` has Property Γ,
then for every order `n ≥ 2s`: every coefficient `β_A(n)` with `|A| ≥ 2` is
non-negative; hence `∂²D_n/∂c_u∂c_v = Σ_{A ∋ u, v} β_A(n) c^{A ∖ {u,v}} ≥ 0` for
all `u ≠ v` and all real `c ≥ 0` (Hypothesis V for `S`, for every order); and
by Lemma L4 of `vertex-principle.md` (with lower bounds `0` and sum `n − s`),
for every tree `S(c)` of order `n`,

`d_m − d_{m−1} ≥ min_{p ∈ V} D_n((n − s) e_p)`,

the minimum over the trees obtained from `S` by attaching all `n − s` leaves
at one vertex.

By Proposition S3, `r_V = s(1 + x) + 3x`: the case `A = V` of Property Γ holds
for every tree.

## What is verified, and what is conjectured

**Computer-assisted (exact; `skeleton_structure.py`, result file
`results/skeleton-structure.json`).** For every tree `S` with `2 ≤ s ≤ 8`
vertices (47 trees, one per isomorphism class):

- Lemma S1 against the direct `n × n` determinant on small leaf numbers, zeros
  included;
- Proposition S2, as an identity between polynomials in `x`, for every subset;
- Proposition S3;
- **Property Γ, for every subset with at least two elements.**

With Proposition S4 this gives Hypothesis V for all orders for each of these
47 skeletons — in particular for the path skeletons with `s ≤ 8`, that is,
Hypothesis V of `vertex-principle.md` (MD-0009) for `s ≤ 8` and every order,
on the larger domain `c ≥ 0`. This rests on the interpolated polynomials
`g_j` and on Proposition S4, and has not been reviewed.

**Conjecture Γ (MD-0010).** Every tree on at least two vertices has
Property Γ.

Under Conjecture Γ and Lemma L4, for every tree with at least as many leaves
as non-leaf vertices the lower inequality `d_{m−1} < d_m` would follow from the
same inequality for the trees "skeleton plus one star". Those are not treated
here in general; in the range computed (orders up to 100) all of them satisfy
it.

## Two observations (exact on the trees computed; not proved)

**One vertex missing.** For `A = V ∖ {w}`, `w` of degree `g` in `S` (`d = 2`),
on every tree with `3 ≤ s ≤ 8`:

`r_A(x) = (s − 1)(1 + x)² + [(g − 1)s + 2g + 1] x + [(g − 1)(s + 6 − g) + 3] x²`.

It depends on `S` only through `s` and `g`, and all three coefficients are
positive (`g ≤ s − 1`). A proof should follow from
`P^{−1} = −L/2 + ττᵀ/(2(s−1))` as in Proposition S3 (objective O5 of
`STATE.md`); it has not been written.

**Locality.** For every tree with `s ≤ 8` and every `A` with
`2 ≤ |A|`, `|V ∖ A| ≤ 4`, the polynomial `r_A` depends only on `s` and on the
principal submatrix `L[Ā, Ā]` of the Laplacian of `S` (the degrees in `S` of
the vertices outside `A` and the adjacencies among them), up to simultaneous
permutation. If this holds in general, Conjecture Γ is a statement about a
forest with prescribed vertex degrees and one integer `s`, not about the whole
skeleton. It is what the formula `P^{−1} = −L/2 + ττᵀ/(2(s−1))` suggests, and
it has not been proved.

## Remarks

**Why this is the mechanism behind T1, T2, T3.** In T1 the coefficient of `ab`
is the top coefficient (Proposition S3 with `s = 2`). In T2 and T3 the three
mixed partials of `vertex-principle.md` are sums of the `β_A` with `|A| ≥ 2`
for the path on three vertices. Property Γ replaces the explicit polynomials
in `m` by one finite, order-independent statement per subset.

**A reformulation that may lead to a proof.** With
`M_A = P + 1_A 1ᵀ + 1 1_Aᵀ + (a/2x) J`, `det N_A = (−1)^s det(M_A) det(I − 2x (M_A^{−1})[Ā, Ā])`.
`M_A` is a perturbation of rank at most 2 of `P`, and `P^{−1} = −L/2 + ττᵀ/(2(s−1))`,
so `(M_A^{−1})[Ā, Ā]` is `−L[Ā, Ā]/2` plus a matrix of small rank, and
`det(I + xL[Ā, Ā])` is a generating function of rooted forests with
non-negative coefficients. Whether the half-gamma expansion of `r_A` can be
read off such a forest expansion has not been examined; this was not derived
carefully and is recorded as a direction, not as a result.

**The upper bound.** Nothing here applies to it. The argument of
Proposition S4 is specific to the index `⌊n/2⌋`, where the binomial terms of
the first kind are centred. The conjectured upper bound concerns the index
`⌈n − n/√5⌉`, and it involves all the coefficients `β_A`, including those with
`|A| ≤ 1`, which Property Γ does not control. No mechanism for it was found in
this session.

**Scope.** Trees with fewer leaves than non-leaf vertices (`n < 2s`) are
outside Lemma S1. The trees "skeleton plus one star" are not handled in
general. Property Γ for a given skeleton is a finite computation, but the
number of skeletons is infinite.
