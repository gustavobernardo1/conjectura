# CJ-0001 — the polynomials `r_A` depend only on a Laplacian block; Property Γ when the complement of `A` is independent

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 6. Propositions S6 to S10 and Lemma C have written
proofs below. Whether they have been reviewed is recorded under
[`../reviews/`](../reviews/) and in `STATE.md`, not here; a statement without a
review report naming this file is unreviewed. Nothing here is a claim of
novelty. Conjecture Γ (MD-0010) remains a conjecture.

This file continues [`skeleton-identity.md`](skeleton-identity.md) and uses
its notation and its Propositions S2 to S4 without change.

## Setting and notation

`S` is a tree on `s ≥ 2` vertices with vertex set `V`, distance matrix `P` and
Laplacian `L`; `g_v` is the degree of `v` in `S` and `τ_v = 2 − g_v`. For
`A ⊆ V` put `B = V ∖ A`, `a = |A|`, `t = |B| = s − a`, and, as in
`skeleton-identity.md`,

`N_A(x) = 2x I_B − P − 1_A 1ᵀ − 1 1_Aᵀ − (a/2x) J`,  `r_A(x) = −2^{2−s} · x · det N_A(x)`  (`x ≠ 0`),

where `I_B` is the diagonal matrix with diagonal `1_B`. `r_A` is a polynomial
of degree at most `t + 1`: `N_A = N⁰ − (a/2x) 1 1ᵀ` with
`N⁰ = 2x I_B − P − 1_A 1ᵀ − 1 1_Aᵀ`, so `det N_A = det N⁰ − (a/2x) 1ᵀ adj(N⁰) 1`,
and `x` occurs in `N⁰` only in the `t` diagonal positions of `B`, so `det N⁰`
and every cofactor of `N⁰` have degree at most `t`.

Quantities attached to `B` (vectors indexed by `B`, matrices by `B × B`):

- `L_B = L[B, B]`, `τ_B` the restriction of `τ`, `1` the all-ones vector of length `t`;
- `h_w = g_w − 1 ≥ 0`, `H = Σ_{w ∈ B} h_w`;
- `k_w` = the number of neighbours of `w` that lie in `B`; `e_B` = the number
  of edges of `S` with both ends in `B`, so `Σ_{w ∈ B} k_w = 2 e_B`;
- `z = L_B 1 − τ_B`. Since `(L_B 1)_w = g_w − k_w`, `z_w = 2h_w − k_w`;
- `Φ_B(x) = det(I + x L_B)` (for `t = 0`: `Φ_B = 1`, and sums over `B` are empty).

Two classical facts are used, as in Proposition S3: `det P = (−1)^{s−1} (s−1) 2^{s−2}`
(Graham–Pollak) and `P^{−1} = −L/2 + ττᵀ/(2(s−1))` (Graham–Lovász 1978; the
formula was checked by exact computation on small trees by the reviewer of S3,
and has not been compared with the printed paper by the project). They give
`P^{−1} 1 = τ/(s−1)` and `1ᵀP^{−1}1 = 2/(s−1)`, because `L1 = 0` and `1ᵀτ = 2`.

## Proposition S6 (reduction to a matrix of size `t + 1`; locality)

**Proposition S6.** For every tree `S` on `s ≥ 2` vertices, every `A ⊆ V`
and every `x ≠ 0`,

`r_A(x) = (s − 1) · x · det(I_{t+1} − K G)`,

where, in block form with a first coordinate followed by the coordinates of `B`,

```
K = | −β   1ᵀ    |      β = 2 + a/(2x),        G = v vᵀ/(2(s−1)) − (1/2) | 0   0   |      v = | 2   |
    |  1   2x I  |                                                       | 0   L_B |          | τ_B |
```

Consequently `r_A` is determined by the integer `s` and the matrix `L_B` up to
a simultaneous permutation of its rows and columns: by the degrees in `S` of
the vertices outside `A` and the adjacencies among them.

*Proof.* Let `U` be the `s × t` matrix whose columns are the unit vectors
`e_w`, `w ∈ B`, and `W = [1 | U]`, an `s × (t+1)` matrix. Then `I_B = UUᵀ` and
`1_A = 1 − U1`, so

`N_A = −P + 2x UUᵀ + U1 1ᵀ + 1 (U1)ᵀ − (2 + a/2x) 1 1ᵀ = −P + W K Wᵀ`.

`P` is invertible, so by the identity `det(I − XY) = det(I − YX)`,

`det N_A = det(−P) · det(I_s − P^{−1} W K Wᵀ) = det(−P) · det(I_{t+1} − K WᵀP^{−1}W)`.

Now `Wᵀτ = (1ᵀτ, Uᵀτ) = (2, τ_B) = v`, and `WᵀLW` has the blocks `1ᵀL1 = 0`,
`1ᵀLU = 0`, `UᵀLU = L_B`. Hence `WᵀP^{−1}W = vvᵀ/(2(s−1)) − diag(0, L_B)/2 = G`.
Finally `det(−P) = (−1)^s det P = −(s−1) 2^{s−2}`, so
`r_A = −2^{2−s} x · (−(s−1) 2^{s−2}) · det(I − KG) = (s−1) x det(I − KG)`.

For the last assertion: `a = s − t`, `τ_B` is `2` minus the diagonal of `L_B`,
so `K` and `G` are functions of `s`, `x` and `L_B`; a simultaneous permutation
of `B` conjugates `K` and `G` by the same permutation matrix. ∎

This proves, for every tree and every subset, the observation "Locality" of
`skeleton-identity.md` (stated there for `s ≤ 8` and `|V ∖ A| ≤ 4` from
computation).

Check with `t = 0`: `K = (−β)`, `G = (2/(s−1))`, and
`r_V = (s−1) x (1 + 2β/(s−1)) = x(s − 1 + 4) + s`, which is Proposition S3.

## Proposition S7 (the Laplacian form)

**Proposition S7.** For every tree `S` on `s ≥ 2` vertices and every `A ⊆ V`,
as polynomials in `x`,

`r_A(x) = Φ_B(x) · [a + (s + 3 − 1ᵀτ_B) x] + x · zᵀ adj(I + xL_B) (1 + xτ_B)`    (first form)

`r_A(x) = Φ_B(x) · [a(1 + x) + (3 + 3H − 2e_B) x] − x² · zᵀ adj(I + xL_B) z`    (second form).

In particular `r_A(0) = a`.

*Proof.* Both sides are polynomials, so it is enough to prove the identities
for the infinitely many `x ≠ 0` with `Φ_B(x) ≠ 0`. Fix such an `x` and put
`R = (I + xL_B)^{−1}`, `Λ = diag(0, L_B)`, `σ = s − 1`. By Proposition S6,
`r_A = σx det(E − (Kv)vᵀ/(2σ))` with `E = I + KΛ/2`. Since
`KΛ` has the blocks `0`, `1ᵀL_B` (first row) and `0`, `2xL_B` (other rows),

```
E = | 1   1ᵀL_B/2  |      det E = Φ_B(x),      E^{−1} = | 1   −(1/2) 1ᵀL_B R |
    | 0   I + xL_B |                                    | 0    R             |
```

By the matrix determinant lemma, `det(E − (Kv)vᵀ/(2σ)) = Φ_B · (1 − vᵀE^{−1}Kv/(2σ))`.
`Kv` has first coordinate `−2β + 1ᵀτ_B` and other coordinates `2(1 + xτ_B)`;
so `E^{−1}Kv` has first coordinate `−2β + 1ᵀτ_B − (L_B1)ᵀR(1 + xτ_B)` and other
coordinates `2R(1 + xτ_B)`, and (`L_B` is symmetric)

`vᵀE^{−1}Kv = −4β + 2·1ᵀτ_B − 2 (L_B1 − τ_B)ᵀ R (1 + xτ_B) = −4β + 2·1ᵀτ_B − 2 zᵀR(1 + xτ_B)`.

Therefore `r_A = xΦ_B [σ + 2β − 1ᵀτ_B] + xΦ_B zᵀR(1 + xτ_B)`. With
`x(σ + 2β) = (s − 1)x + 4x + a` and `Φ_B R = adj(I + xL_B)` this is the first form.

For the second form: `(I + xL_B)1 = 1 + xL_B1`, so `R(1 + xL_B1) = 1`, and
`1 + xτ_B = (1 + xL_B1) − xz`; hence `R(1 + xτ_B) = 1 − xRz` and

`x zᵀ adj(I + xL_B)(1 + xτ_B) = xΦ_B · 1ᵀz − x² zᵀ adj(I + xL_B) z`.

`1ᵀz − 1ᵀτ_B = Σ_B (2h_w − k_w) − Σ_B (1 − h_w) = 3H − 2e_B − t`, and `s − t = a`,
so `a + (s + 3 − 1ᵀτ_B + 1ᵀz) x = a + (a + 3 + 3H − 2e_B) x`. ∎

## Proposition S8 (one vertex missing: objective O5)

**Proposition S8.** Let `S` be a tree on `s ≥ 2` vertices, `w` a vertex of
degree `g`, and `A = V ∖ {w}`. Then

`r_A(x) = (s − 1)(1 + x)² + [(g − 1)s + 2g + 1] x + [(g − 1)(s + 6 − g) + 3] x²`,

and the three coefficients are positive. In particular, for `s ≥ 3`, `r_A` has
a non-negative half-gamma expansion of degree 2.

*Proof.* Here `t = 1`, `a = s − 1`, `L_B = (g)`, `Φ_B = 1 + gx`, the adjugate is
`(1)`, `H = g − 1`, `e_B = 0`, `z = 2(g − 1)`. The second form of S7 gives

`r_A = (1 + gx)[(s − 1) + (s − 1 + 3g)x] − 4(g − 1)² x²`
`    = (s − 1) + (gs + 2g + s − 1) x + (gs + 7g − g² − 4) x²`.

Subtracting `(s − 1)(1 + x)²` leaves `[(g−1)s + 2g + 1] x + [gs + 7g − g² − s − 3] x²`,
and `(g − 1)(s + 6 − g) + 3 = gs + 7g − g² − s − 3`. Since `1 ≤ g ≤ s − 1`:
`s − 1 ≥ 1`, `(g − 1)s + 2g + 1 ≥ 3`, and `s + 6 − g ≥ 7` gives
`(g − 1)(s + 6 − g) + 3 ≥ 3`. The basis of degree 2 is `(1+x)²`, `x`, `x²`. ∎

This is the formula observed in `skeleton-identity.md` on the trees with
`3 ≤ s ≤ 8`.

## Proposition S9 (two vertices missing)

**Proposition S9.** Let `S` be a tree on `s ≥ 3` vertices, `u ≠ w` two
vertices of degrees `g_1, g_2`, `ε = 1` if they are adjacent and `ε = 0`
otherwise, `Σ = g_1 + g_2`, `Π = g_1 g_2`, and `A = V ∖ {u, w}`. Then

`r_A(x) = (s − 2)(1 + x)³ + ρ_1 x(1 + x) + σ_2 x² + σ_3 x³`, with

- `ρ_1 = (s + 1)Σ − 2s + 1 − 2ε`,
- `σ_2 = (s + 6)(Π − ε) − Σ² + (2 + 2ε)Σ − s − 3`,
- `σ_3 = (s + 11 − 2ε)Π − ΣΠ − 4(1 − ε)Σ − (s + 11)ε − s + 2`,

and `ρ_1 ≥ 3`, `σ_2 ≥ 3`, `σ_3 ≥ 3`. So `r_A` has a non-negative half-gamma
expansion of degree 3.

*Proof.* `t = 2`, `a = s − 2`, `L_B` has diagonal `g_1, g_2` and off-diagonal
entries `−ε`; `Φ_B = 1 + Σx + (Π − ε)x²` (using `ε² = ε`);
`adj(I + xL_B)` has diagonal `1 + g_2x, 1 + g_1x` and off-diagonal entries `εx`;
`H = Σ − 2`, `e_B = ε`, `z_i = 2g_i − c` with `c = 2 + ε`. The second form of
S7 reads

`r_A = [1 + Σx + (Π − ε)x²] · [(s − 2) + (s − 5 + 3Σ − 2ε)x] − x² [z_1² + z_2² + (z_1²g_2 + z_2²g_1 + 2ε z_1z_2) x]`.

With `c² = 4 + 5ε`, `εc = 3ε`, `εc² = 9ε`:
`z_1² + z_2² = 4Σ² − 8Π − (8 + 4ε)Σ + 8 + 10ε` and
`z_1²g_2 + z_2²g_1 + 2ε z_1z_2 = 4ΠΣ − 8cΠ + c²Σ + 2ε(4Π − 2cΣ + c²) = 4ΠΣ − 16Π + (4 − 7ε)Σ + 18ε`.
The coefficients `c_0, …, c_3` of `r_A` are therefore

- `c_0 = s − 2`,
- `c_1 = (s + 1)Σ + s − 5 − 2ε`,
- `c_2 = (s + 3 + 2ε)Σ − Σ² + (s + 6)Π − 8 − (s + 8)ε`,
- `c_3 = (s + 11 − 2ε)Π − ΣΠ − 4(1 − ε)Σ − (s + 11)ε`,

and the expansion in the basis `(1+x)³, x(1+x), x², x³` has `ρ_0 = c_0`,
`ρ_1 = c_1 − 3c_0`, `σ_2 = c_2 − 3c_0 − ρ_1`, `σ_3 = c_3 − c_0`, which are the
stated values.

Signs. The edges incident with `u` or `w` are `Σ − ε` distinct edges of a
tree with `s − 1` edges, so `Σ ≤ s − 1 + ε`; `g_i ≥ 1` gives `Σ ≥ 2` and
`Π ≥ Σ − 1` (from `(g_1 − 1)(g_2 − 1) ≥ 0`); and if `ε = 1` then `Σ ≥ 3`,
because `s ≥ 3` and `S` is connected.

*Case `ε = 0`* (`2 ≤ Σ ≤ s − 1`). `ρ_1 = (s+1)Σ − 2s + 1 ≥ 3`.
`σ_2 = (s + 6)(Π − 1) + 3 − Σ(Σ − 2) ≥ (Σ + 7)(Σ − 2) + 3 − Σ(Σ − 2) = 7(Σ − 2) + 3 ≥ 3`,
using `Π − 1 ≥ Σ − 2 ≥ 0` and `s + 6 ≥ Σ + 7`.
`σ_3 = (s + 11 − Σ)(Π − 1) + 13 − 5Σ ≥ 12(Σ − 2) + 13 − 5Σ = 7Σ − 11 ≥ 3`,
using `s + 11 − Σ ≥ 12`.

*Case `ε = 1`* (`3 ≤ Σ ≤ s`). `ρ_1 = (s+1)Σ − 2s − 1 ≥ s + 2 ≥ 5`.
`σ_2 = (s + 6)(Π − 2) + 3 − Σ(Σ − 4) ≥ (Σ + 6)(Σ − 3) + 3 − Σ(Σ − 4) = 7Σ − 15 ≥ 6`,
using `Π − 2 ≥ Σ − 3 ≥ 0` and `s + 6 ≥ Σ + 6`.
`σ_3 = (s + 9 − Σ)Π − 2s − 9`; with `s = Σ + j`, `j ≥ 0`:
`σ_3 = (9 + j)Π − 2Σ − 2j − 9 ≥ (9 + j)(Σ − 1) − 2Σ − 2j − 9 = 7Σ − 18 + j(Σ − 3) ≥ 3`.

Finally `ρ_0 = s − 2 ≥ 1`. ∎

## Lemma C (the cone of Property Γ)

**Lemma C.** Let `d ≥ 0` and let `e, j ≥ 0` be integers with `e + j ≤ d` and
`2e + j ≥ d`. Then `x^e (1 + x)^j` has a non-negative half-gamma expansion of
degree `d`. Hence so has every non-negative combination of such polynomials.

*Proof.* Induction on `j`. If `j = 0`, then `d ≤ 2e ≤ 2d` and `x^e` is a basis
element of the second kind. Let `j ≥ 1`. If `2e + j = d`, then `2e < d` and
`x^e(1+x)^{d−2e}` is a basis element of the first kind. If `2e + j > d`, write
`x^e(1+x)^j = x^e(1+x)^{j−1} + x^{e+1}(1+x)^{j−1}`; the pairs `(e, j−1)` and
`(e+1, j−1)` satisfy both conditions (`2e + j − 1 ≥ d`; `e + 1 + j − 1 ≤ d`),
and the induction hypothesis applies to each. The last sentence follows from
the uniqueness of the expansion. ∎

Call a polynomial of this form (a non-negative combination of `x^e(1+x)^j`
with `e + j ≤ d`, `2e + j ≥ d`) *of weight at least `d`*. The weight condition
is additive: a product of polynomials of weights at least `d_1` and `d_2`,
taken term by term, has weight at least `d_1 + d_2`, provided the degree
condition holds for the terms of the product (it does in the use below, where
every product has degree at most `d`).

## Proposition S10 (Property Γ when the complement of `A` is independent)

**Proposition S10.** Let `S` be a tree on `s ≥ 2` vertices and `A ⊆ V` such
that `B = V ∖ A` is non-empty and independent in `S` (no two vertices of `B`
are adjacent). Put `Φ_B = Π_{w ∈ B} (1 + g_w x)` and
`Φ_w = Π_{u ∈ B, u ≠ w} (1 + g_u x)`. Then `a − H ≥ 1` and

`r_A(x) = (a − H)(1 + x) Φ_B + 3x Φ_B + Σ_{w ∈ B} [h_w (1 + x)² + 3h_w x(1 + x) + h_w² x] Φ_w`,

and `r_A` has a non-negative half-gamma expansion of degree `t + 1`.

Together with Proposition S3 (`B = ∅`): **Property Γ holds for every tree and
every subset `A` whose complement is an independent set.**

*Proof.* `L_B` is the diagonal matrix of the `g_w`, so `Φ_B` is the stated
product, `adj(I + xL_B)` is diagonal with entries `Φ_w`, `e_B = 0` and
`z_w = 2h_w`. The second form of S7 gives

`r_A = aΦ_B(1 + x) + 3xΦ_B + 3HxΦ_B − 4x² Σ_w h_w² Φ_w`.

Since `Φ_B = (1 + g_w x)Φ_w = ((1 + x) + h_w x)Φ_w` for each `w`:

- `3HxΦ_B = Σ_w 3h_w x Φ_B = Σ_w [3h_w x(1 + x) + 3h_w² x²] Φ_w`;
- `aΦ_B(1 + x) = (a − H)(1 + x)Φ_B + Σ_w h_w (1 + x)Φ_B = (a − H)(1 + x)Φ_B + Σ_w [h_w (1 + x)² + h_w² x(1 + x)] Φ_w`.

Adding, the coefficient of `Φ_w` is
`h_w(1+x)² + 3h_w x(1+x) + h_w² [x(1+x) + 3x² − 4x²] = h_w(1+x)² + 3h_w x(1+x) + h_w² x`,
which is the stated identity.

`a − H ≥ 1`: `B` is independent, so the `Σ_{w ∈ B} g_w` edges incident with
`B` are distinct and each joins `B` to `A`. They form a forest on at most
`t + a` vertices, with at least one vertex, so `Σ_B g_w ≤ t + a − 1`, that is
`H = Σ_B g_w − t ≤ a − 1`.

Weights. `Φ_B = Π_w ((1+x) + h_w x)` expands into the terms
`h^C x^{|C|}(1+x)^{t−|C|}`, `C ⊆ B`, with non-negative coefficients; each has
degree `t` and `2|C| + (t − |C|) ≥ t`. Likewise `Φ_w` is a non-negative
combination of terms `x^i(1+x)^{t−1−i}`. Hence, with `d = t + 1`:
`(1+x)Φ_B` consists of terms `x^i(1+x)^{t+1−i}` (degree `t+1`, `2e + j = t + 1 + i`);
`xΦ_B` of terms `x^{i+1}(1+x)^{t−i}` (degree `t+1`, `2e + j = t + 2 + i`);
`(1+x)²Φ_w` of terms `x^i(1+x)^{t+1−i}`; `x(1+x)Φ_w` of terms `x^{i+1}(1+x)^{t−i}`;
and `xΦ_w` of terms `x^{i+1}(1+x)^{t−1−i}` (degree `t`, `2e + j = t + 1 + i`).
All satisfy `e + j ≤ d` and `2e + j ≥ d`, and all coefficients (`a − H`, `3`,
`h_w`, `3h_w`, `h_w²`, and those of the expansions) are non-negative. By
Lemma C, `r_A` has a non-negative half-gamma expansion of degree `d = t + 1`. ∎

Remark. The identity of S10 is not a positivity statement about polynomials
in free variables `h_w`: the second form of S7 contains `−4h_w² x² Φ_w`, and
only `3h_w² x² Φ_w` is available from `3HxΦ_B`. The remaining `−h_w² x² Φ_w`
is absorbed by `aΦ_B(1+x)`, at the price of the coefficient `a − H`, whose
sign is a property of trees (`H ≤ a − 1`). A proof of Conjecture Γ has to use
the tree in this way.

## What S6 to S10 give for Conjecture Γ

- **Proved by hand, for every tree** (subject to review): Property Γ for all
  `A` with `|V ∖ A| ≤ 2` (S3, S8, S9) and for all `A` whose complement is
  independent (S3, S10). For a star skeleton with centre `z`, every `A ∋ z`
  is covered.
- **Reformulation (exact, by S7 and Lemma C).** Conjecture Γ is implied by:
  for every tree `S` and every `A` with `|A| ≥ 2`, the polynomial

  `Φ_B [a(1 + x) + (3 + 3H − 2e_B) x] − x² zᵀ adj(I + xL_B) z`

  is of weight at least `t + 1`. It depends on `S` only through `s` and the
  induced forest `S[B]` with the degrees `g_w` (S6).
- **Not done.** When `B` contains edges, `Φ_B` and `adj(I + xL_B)` are
  generating functions of rooted spanning forests of `S[B]` (all-minors
  matrix-tree theorem; not rederived here), in which a root `w` carries the
  factor `1 + (g_w − k_w)x`. A vertex of `B` with no neighbour in `A`
  contributes a factor of weight 0 when it is an isolated root, so the
  termwise weight count of S10 fails and the terms must be grouped. S9 with
  `ε = 1` is the smallest case; it was proved by explicit inequalities, not by
  a grouping that generalizes. No induction on `|B|` was found.

## Verification by computation

`experiments/CJ-0001-collins-shor-peak/locality_check.py` (written in session
6, sharing no code with `skeleton_structure.py`; exact rationals) compares,
for the 47 trees with 2 to 8 vertices and all 7820 subsets `A`, the definition
of `r_A` with S6, with both forms of S7, with S8 (325 cases), S9 (1011 cases)
and the identity of S10 (2263 cases), at 14 positive rational points (more
than the degree `t + 1 ≤ 9`). Result file:
`experiments/CJ-0001-collins-shor-peak/results/locality-check.json` — zero
failures; the smallest value of `a − H` over the independent complements is
`1`; the smallest values of `(ρ_0, ρ_1, σ_2, σ_3)` in S9 over the subsets with
`|A| ≥ 2` are `(2, 3, 3, 3)`. The computation checks the identities on these
trees; the inequalities for all trees rest on the written proofs.
