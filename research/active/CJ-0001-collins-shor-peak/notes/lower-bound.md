# CJ-0001 — the lower bound `⌊n/2⌋` for every tree: statement (Γ_c¹), star minimality, and contraction of an edge

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 11. Lemma S32, Propositions S33 to S36 and Theorems
T5 and T6 have written proofs below. **Nothing here is an established
result**: a statement of this file counts as reviewed only where a report
under [`../reviews/`](../reviews/) names this file and its revision. Nothing
here is a claim of novelty.

What this file does. Sessions 9 and 10 reduced the lower half of the
Collins–Shor conjecture for trees of even order to statement (Γ_c¹) of
[`leaf-telescoping.md`](leaf-telescoping.md) and left it open. This file
proves it (Theorem T5), by an induction on rooted trees in which the one
negative term of the merge rule of [`rooted-calculus.md`](rooted-calculus.md)
becomes a sum of squares. Consequences (Theorem T6): statement (SM) — the
star is the minimum of `ℓ_T` in the cone order — and

> for every tree `T` of order `n ≥ 3`, `d_{m−1}(T) < d_m(T)` with
> `m = ⌊n/2⌋`: every maximizing index of `d_0, …, d_{n−2}` is at least
> `⌊n/2⌋`.

Proposition S36 is a second result: an explicit formula for the change of
`ℓ_T` when a non-pendant edge is contracted and a pendant vertex is added,
which lies in the same cone.

## Notation and tools

Weighted trees, `M(T, ν) = I + x(L_T + diag ν)`, `Φ(T, ν) = det M`,
`p_v = 1 + (2 − k_v − ν_v)x` (`k_v` the degree), `N = Σ_v ν_v`,
`R(T, ν) = (N + j − 1)(1 + x)Φ − pᵀ adj(M) p` for a tree on `j` vertices: as
in [`gamma-components.md`](gamma-components.md). The rooted state
`(Ψ, H, G, Ω, R)` of `(T, ν, u)`, and the operations *raise*, *plant* and
*merge*: as in [`rooted-calculus.md`](rooted-calculus.md). Throughout this
file **a rooted tree `(A, u)` has weight zero** unless a weight is written;
`a = |A|`, `δ_v = dist(u, v)`, `M = I + xL_A`, `Φ = det M`, and for a vertex
`v ≠ u`

`Π_{uv} := det M[A ∖ V(path(u, v))]`,  `a_v := x^{δ_v − 1} Π_{uv}`.

`M¹ := M + x e_u e_uᵀ = M(A, e_u)`. `ℓ_T`, `d_k`, `λ_μ(f) = [x^μ]f − [x^{μ−1}]f`,
the cones `K_d` and `C_d`: as in [`wiener-form.md`](wiener-form.md).

Results used, with their status at the time of writing:

- **(K2)** `K_{d+1} ⊆ K_d`; `K_d · K_{d′} ⊆ K_{d+d′}`; `(1+x)K_d ⊆ K_{d+1}`;
  `x K_d ⊆ K_{d+2}` (immediate from the definition; `wiener-form.md`).
  Elements of `K_d` have non-negative coefficients.
- **Lemma K** (`wiener-form.md`; audited at `a3e5179`): `Φ(K, ν) ∈ K_j` for a
  tree `K` on `j ≥ 1` vertices and an integer weight `ν ≥ 0`, `ν ≠ 0`; and
  (K3): for a leaf `w` with neighbour `u` and `ν′` the restriction of `ν` to
  `K − w`, `Φ(K, ν) = (1+x)Φ(K − w, ν′) + x det M[K ∖ {w, u}] + ν_w x Φ(K − w, ν′ + e_u)`.
- **Lemma S24** (`wiener-form.md`; reviewed at `b5d9294`, audited at
  `a3e5179`): for an unweighted tree, `adj(M)_{uv} = x^{dist(u,v)} det M[V ∖ V(path)]`.
- **Lemma A(a)** (`wiener-form.md`; formalized in Lean on the cone):
  `λ_μ ≥ 0` on `K_{2μ−1}`.
- **Proposition S19** (`rooted-calculus.md`; reviewed at `59c47f7`): the
  values of the state for one vertex of weight `n` (a), and the rules for
  raise (b), plant (c) and merge (d).
- **Proposition S23** ([`leaf-telescoping.md`](leaf-telescoping.md);
  **(a) to (c) not reviewed**, (d) checked by the reviewer of `b5d9294`):
  `R(T, 0) = xℓ_T − (1+4x)Φ_T` (a); the leaf recursion
  `ℓ_{T⁺} = (1+x)ℓ_T + r_u(T)`, `r_u(T) = (1+4x)Ψ + Ω` for the state of
  `(T, 0, u)` (b); its telescoped form (c); the star (d).
- **R1** ([`lemmas.md`](lemmas.md); formalized in Lean).
- `C_d` is the set of non-negative combinations of `x^e(1+x)^i` with
  `e + i ≤ d ≤ 2e + i` ([`gamma-reduction.md`](gamma-reduction.md)). Hence
  **(K4)**: a polynomial of `K_d` of degree at most `d` is in `C_d`. Indeed
  it is a combination with positive coefficients of generators `x^e(1+x)^i`,
  `2e + i ≥ d`; these have non-negative coefficients, so none has degree
  above `d`, that is `e + i ≤ d`.

## Lemma S32 (off-diagonal entries of the adjugate, with weights)

**Lemma S32.** Let `(K, ν)` be a weighted tree on `j ≥ 1` vertices, `ν ≥ 0`
an integer weight (the zero weight allowed), `M = M(K, ν)`, `v, v′` two
vertices, `P` the path between them, `d = dist(v, v′)`, `Q` the set of
vertices off `P`. Then `adj(M)_{vv′} = x^d det M[Q]`, and `det M[Q] ∈ K_{j−d−1}`.

*Proof.* The proof of Lemma S24 uses of the matrix only that it is symmetric,
positive definite for real `x > 0`, with off-diagonal entries `−x` on the
edges of a tree and `0` elsewhere. `M(K, ν) = I + x(L_K + diag ν)` has these
properties, so that proof gives `adj(M)_{vv′} = x^d det M[Q]`. `M[Q]` is block
diagonal over the components `K′` of `K − V(P)`; each `K′` is joined to `P` by
exactly one edge, with end `a_{K′}` in `K′`, and its block is
`I + x(L_{K′} + diag(ν|_{K′} + e_{a_{K′}}))`, whose weight is not zero. By
Lemma K each block has its determinant in `K_{|K′|}`, and by (K2) the product
is in `K_{j−d−1}` (it is `1 ∈ K_0` if `Q = ∅`). ∎

## Proposition S33 (the state of an unweighted rooted tree)

**Proposition S33.** Let `(A, u)` be a rooted tree of order `a ≥ 1`, with the
state `(Ψ, H, G, Ω, R)` of `(A, 0, u)`.

(a) For `v ≠ u`: `a_v ∈ K_{a+δ_v−3}`. So `a_v ∈ K_{a−2}`, and `a_v ∈ K_{a−1}`
if `δ_v ≥ 2`.

(b) `H = Σ_{v≠u} a_v ∈ K_{a−2}`.

(c) `G = x Σ_{v≠u} (δ_v − 1) a_v`; so `G/x` is a polynomial in `K_{a−1}`.

(d) `Ψ ∈ K_{a−1}`.

(e) `R(A, e_u) = Q¹ + x² Σ_{v≠u} δ_v² a_v`, where
`Q¹ := Σ_{v<v′} (δ_v − δ_{v′})² adj(M¹)_{vv′}` (the sum over unordered pairs of
distinct vertices), and `Q¹ ∈ K_a`.

*Proof.* (a) By Lemma S32 (with `ν = 0`), `Π_{uv} ∈ K_{a−δ_v−1}`; multiply by
`x^{δ_v−1}` and use (K2): `a_v ∈ K_{a−δ_v−1+2(δ_v−1)} = K_{a+δ_v−3}`, and
`K_{a+δ_v−3} ⊆ K_{a−2}` as `δ_v ≥ 1`.

(b) `L1 = 0`, so `M1 = 1` and `adj(M)1 = Φ1`: `Φ = Σ_v adj(M)_{uv}`. By
Lemma S24, `adj(M)_{uv} = x^{δ_v}Π_{uv} = x a_v` for `v ≠ u`, and
`adj(M)_{uu} = Ψ`. So `xH = Φ − Ψ = x Σ_{v≠u} a_v`.

(c) Let `τ_v = 2 − k_v`. *Claim:* `Lδ = τ − 2e_u`. For `v ≠ u`, `v` has one
neighbour at distance `δ_v − 1` from `u` and `k_v − 1` at distance `δ_v + 1`,
so `(Lδ)_v = k_vδ_v − (δ_v − 1) − (k_v − 1)(δ_v + 1) = 2 − k_v`; and
`(Lδ)_u = −k_u = τ_u − 2`. Hence `p = 1 + xτ = 1 + (M − I)δ + 2x e_u`, and,
with `e_uᵀadj(M)1 = Φ`, `e_uᵀadj(M)Mδ = Φδ_u = 0`:

`π_u = e_uᵀadj(M)p = Φ − Σ_v δ_v adj(M)_{uv} + 2xΨ = Φ + 2xΨ − x Σ_{v≠u} δ_v a_v`.

So `G = (1+2x)Ψ − π_u = −(Φ − Ψ) + x Σ δ_v a_v = x Σ_{v≠u} (δ_v − 1) a_v` by
(b). Only vertices with `δ_v ≥ 2` contribute, and for them `a_v ∈ K_{a−1}`
by (a).

(d) `Ψ = adj(M)_{uu} = det M[A ∖ u]`, which is in `K_{a−1}` by Lemma S32 with
`v = v′ = u`.

(e) For `(A, e_u)`: `N = 1`, and `p_v = 1 + xτ_v − x[v = u]`. By the claim in
(c), `xτ = xLδ + 2x e_u`, so `p = 1 + xLδ + x e_u`. As `δ_u = 0`,
`M¹δ = δ + xLδ`, and `M¹1 = 1 + x e_u`. Hence `p = M¹(1 + δ) − δ`, and with
`adj(M¹)M¹ = Φ¹ I` (`Φ¹ = det M¹`):

`pᵀadj(M¹)p = Φ¹ (1+δ)ᵀM¹(1+δ) − 2Φ¹ δᵀ(1+δ) + δᵀadj(M¹)δ`.

`(1+δ)ᵀL(1+δ) = δᵀLδ = Σ_{edges} 1 = a − 1`, because the two ends of an edge
have distances from `u` that differ by exactly one; so
`(1+δ)ᵀM¹(1+δ) = Σ_v (1+δ_v)² + x(a − 1) + x(1 + δ_u)² = Σ_v (1+δ_v)² + xa`.
Therefore `pᵀadj(M¹)p = Φ¹[a(1 + x) − Σ_v δ_v²] + δᵀadj(M¹)δ` and

`R(A, e_u) = a(1+x)Φ¹ − pᵀadj(M¹)p = Φ¹ Σ_v δ_v² − δᵀadj(M¹)δ`.

From `adj(M¹)M¹1 = Φ¹1`: `Σ_{v′} adj(M¹)_{vv′} + x adj(M¹)_{vu} = Φ¹` for every
`v`. Substituting this for `Φ¹` in the coefficient of each `δ_v²`, and using
the symmetry of `adj(M¹)`:

`R(A, e_u) = x Σ_v δ_v² adj(M¹)_{vu} + ½ Σ_{v,v′} (δ_v − δ_{v′})² adj(M¹)_{vv′}`.

The second sum is `Q¹`. By Lemma S32 for `(A, e_u)`,
`adj(M¹)_{vu} = x^{δ_v} det M¹[A ∖ V(path(u, v))]`, and this minor is `Π_{uv}`,
since `M¹` and `M` differ only in the entry `(u, u)`, whose row is deleted.
So `x δ_v² adj(M¹)_{vu} = x² δ_v² a_v`. Finally, for `v ≠ v′` at distance
`d ≥ 1`, Lemma S32 for `(A, e_u)` gives `adj(M¹)_{vv′} ∈ x^d K_{a−d−1} ⊆ K_{a+d−1} ⊆ K_a`. ∎

## Proposition S34 (the polynomial `E`)

For a rooted tree `(A, u)` define

`E = E(A, u) := R − Ω + (1+2x)²Ψ − 2xG`  (the state of `(A, 0, u)`).

**Proposition S34.** (a) `E = R(A, e_u) − (1+x)(Ω + xH)`.

(b) *Plant.* For the planted tree `(A^, r)` (a new vertex `r` adjacent to
`u`, root `r`): `Ψ^ = (1+x)Ψ + xH = Φ(A, e_u)`, `H^ = Ψ + xH = Φ`,
`G^ = x(xH + G)`, `Ω^ = R(A, e_u)`, and

`E^ = x [E + Ω + 2G + x(3 + 2x)H]`.

(c) *Merge.* For the merge of `(A_1, u_1)` and `(A_2, u_2)`:

`E = E_1Ψ_2 + E_2Ψ_1 + x(H_1Ω_2 + H_2Ω_1) − 2G_1G_2`.

(d) *Merge of several.* For the merge of `q ≥ 1` rooted trees with states
indexed by `i`, put `P_i = Π_{l≠i} Ψ_l`, `P_{il} = Π_{t≠i,l} Ψ_t` and
`X_{il} = x(H_iΩ_l + H_lΩ_i) − 2G_iG_l`. Then `Ψ = Π_i Ψ_i`, `X = Σ_i X_iP_i`
for `X = H, G, Ω`, and

`E = Σ_i E_iP_i + Σ_{i<l} X_{il}P_{il}`.

*Proof.* (a) S19(b) with `ν_u = 0`:
`R(A, e_u) = R + (1+2x)²Ψ + x(1+x)H + xΩ − 2xG = E + Ω + x(1+x)H + xΩ`.

(b) The values of `Ψ^`, `H^`, `G^`, `Ω^` are S19(c) (`Φ = Ψ + xH` by the
definition of `H`), and `R^ = (1+x)R + xΩ` (S19(c), `ν_u = 0`). By (a),
`Ω^ = E + (1+x)(Ω + xH)`, and by the definition of `E`,
`R = E + Ω − (1+2x)²Ψ + 2xG`. Then

`E^ = R^ − Ω^ + (1+2x)²Ψ^ − 2xG^`
`   = (1+x)[E + Ω − (1+2x)²Ψ + 2xG] + xΩ − E − (1+x)Ω − x(1+x)H + (1+2x)²[(1+x)Ψ + xH] − 2x²(xH + G)`
`   = xE + xΩ + [2x(1+x) − 2x²]G + [x(1+2x)² − x(1+x) − 2x³]H`,

and `x(1+2x)² − x(1+x) − 2x³ = 3x² + 2x³`.

(c) S19(d) with both root weights zero: `Ψ = Ψ_1Ψ_2`, `X = X_1Ψ_2 + X_2Ψ_1`
for `X = H, G, Ω`, and
`R = R_1Ψ_2 + R_2Ψ_1 + x(H_1Ω_2 + H_2Ω_1) + (1+2x)²Ψ_1Ψ_2 − 2G_1G_2`. Then
`E = R − Ω + (1+2x)²Ψ − 2xG` is
`[R_1 − Ω_1 − 2xG_1]Ψ_2 + [R_2 − Ω_2 − 2xG_2]Ψ_1 + 2(1+2x)²Ψ_1Ψ_2 + x(H_1Ω_2 + H_2Ω_1) − 2G_1G_2`,
and `(1+2x)²Ψ_1Ψ_2` is added once to each bracket.

(d) Induction on `q`; `q = 1` is trivial and `q = 2` is (c). The merge of
`q + 1` trees is the merge of the first `q` (state with index `0`) with the
last. By (c) and the induction hypothesis,
`E = E_0Ψ_{q+1} + E_{q+1}Ψ_0 + x(H_0Ω_{q+1} + H_{q+1}Ω_0) − 2G_0G_{q+1}`, with
`Ψ_0 = Π_{i≤q} Ψ_i` and `X_0 = Σ_{i≤q} X_i Π_{l≤q, l≠i} Ψ_l`; the last three
terms are `Σ_{i≤q} X_{i,q+1} Π_{l≤q, l≠i} Ψ_l`, and `E_0Ψ_{q+1}` supplies the
terms with both indices at most `q`. The rules for `Ψ, H, G, Ω` are the same
induction. ∎

## Proposition S35 (two planted trees: a sum of squares)

**Proposition S35.** Let `(A_1, u_1)`, `(A_2, u_2)` be rooted trees of orders
`a_1, a_2 ≥ 1`, with the quantities of Proposition S33 (`a_v`, `Q¹_i`,
`R¹_i := R(A_i, e_{u_i})`), and let a hat denote the state of the planted
tree `(A_i^, r_i)`. Then

`x(H^_1Ω^_2 + H^_2Ω^_1) − 2G^_1G^_2 = x(Ψ_1R¹_2 + Ψ_2R¹_1) + x²(H_1Q¹_2 + H_2Q¹_1) + x⁴ Σ_{v, v′} (δ_v − δ_{v′})² a_v a_{v′}`,

the last sum over `v ∈ A_1 ∖ u_1` and `v′ ∈ A_2 ∖ u_2`, each distance taken
in its own tree from its own root. Consequently, if `R¹_1 ∈ K_{a_1+1}` and
`R¹_2 ∈ K_{a_2+1}`, the left side is in `K_{a_1+a_2+2}`.

*Proof.* By S34(b), `H^_i = Ψ_i + xH_i`, `Ω^_i = R¹_i`, and
`G^_i = x(xH_i + G_i) = x² J_i` with `J_i := H_i + G_i/x = Σ_v δ_v a_v`
(S33(b), (c)). By S33(e), `R¹_i = Q¹_i + x² W_i` with `W_i := Σ_v δ_v² a_v`.
So

`x H^_1 Ω^_2 = xΨ_1R¹_2 + x² H_1 (Q¹_2 + x² W_2)`,

and the left side is
`x(Ψ_1R¹_2 + Ψ_2R¹_1) + x²(H_1Q¹_2 + H_2Q¹_1) + x⁴ [H_1W_2 + H_2W_1 − 2J_1J_2]`.
With `H_i = Σ a_v`, `J_i = Σ δ_v a_v`, `W_i = Σ δ_v² a_v`, the bracket is
`Σ_{v,v′} a_v a_{v′} (δ_{v′}² + δ_v² − 2δ_vδ_{v′})`.

For the cone: `Ψ_i ∈ K_{a_i−1}` (S33(d)), so
`xΨ_1R¹_2 ∈ K_{2+(a_1−1)+(a_2+1)}`; `H_1 ∈ K_{a_1−2}` and `Q¹_2 ∈ K_{a_2}`
(S33(b), (e)), so `x²H_1Q¹_2 ∈ K_{4+(a_1−2)+a_2}`; and `a_v ∈ K_{a_1−2}`,
`a_{v′} ∈ K_{a_2−2}` (S33(a)), so `x⁴a_va_{v′} ∈ K_{8+a_1+a_2−4} ⊆ K_{a_1+a_2+2}`.
(If `a_i = 1`, then `H_i = G_i = 0`, the sums over `A_i ∖ u_i` are empty, and
the statement holds with the same proof.) ∎

## Theorem T5 (statement (Γ_c¹))

**Theorem T5.** For every rooted tree `(A, u)` of order `a ≥ 1`, with the
state of `(A, 0, u)`:

(i) `Ω ∈ K_a`;  (ii) `E ∈ K_{a+1}`;  (iii) `R(A, e_u) ∈ K_{a+1}`.

Moreover `R(A, e_u) ∈ C_{a+1}`: this is statement (Γ_c¹) of
`leaf-telescoping.md`.

*Proof.* (iii) follows from (i) and (ii): by S34(a),
`R(A, e_u) = E + (1+x)Ω + x(1+x)H`, with `(1+x)Ω ∈ K_{a+1}` and
`x(1+x)H ∈ K_{(a−2)+3}` (S33(b), (K2)).

(i) and (ii) by induction on `a`. For `a = 1`: `Ψ = 1`, `H = G = Ω = 0` and
`R = −(1+2x)²` (S19(a) with `n = 0`), so `E = 0`.

Let `a ≥ 2`. Let `c_1, …, c_q` (`q ≥ 1`) be the neighbours of `u`, `A_i` the
component of `A − u` that contains `c_i`, `a_i = |A_i|`; `Σ_i a_i = a − 1`.
The statements (i) to (iii) hold for each `(A_i, c_i)` by induction, and
`(A, u)` is the merge of the planted trees `(A_i^, r_i)`.

(i) By the definition of `Ω`, `Ω = Σ_i R(A_i, e_{c_i}) Π_{l≠i} Φ(A_l, e_{c_l})`.
`R(A_i, e_{c_i}) ∈ K_{a_i+1}` by (iii) for `(A_i, c_i)` and `Φ(A_l, e_{c_l}) ∈ K_{a_l}`
by Lemma K; so each term is in `K_{1+Σ_l a_l} = K_a`.

(ii) By S34(d) applied to the planted trees,
`E = Σ_i E^_iP_i + Σ_{i<l} X_{il}P_{il}`, where `P_i` and `P_{il}` are products
of the polynomials `Ψ^_t = Φ(A_t, e_{c_t}) ∈ K_{a_t}` (S34(b), Lemma K) and
`X_{il} = x(H^_iΩ^_l + H^_lΩ^_i) − 2G^_iG^_l`.

*The terms `E^_iP_i`.* By S34(b), `E^_i = x[E_i + Ω_i + 2G_i + x(3+2x)H_i]`,
with the state of `(A_i, 0, c_i)`. By induction `E_i ∈ K_{a_i+1}` and
`Ω_i ∈ K_{a_i}`; by S33, `G_i/x ∈ K_{a_i−1}` and `H_i ∈ K_{a_i−2}`. With (K2):
`xE_i ∈ K_{a_i+3}`, `xΩ_i ∈ K_{a_i+2}`, `2xG_i = 2x²(G_i/x) ∈ K_{a_i+3}`,
`x²H_i ∈ K_{a_i+2}`, `x³H_i ∈ K_{a_i+4}`. All these are in `K_{a_i+2}`, so
`E^_i ∈ K_{a_i+2}` and `E^_iP_i ∈ K_{a_i+2+Σ_{l≠i} a_l} = K_{a+1}`.

*The terms `X_{il}P_{il}`.* By (iii) for `(A_i, c_i)` and `(A_l, c_l)` and
Proposition S35, `X_{il} ∈ K_{a_i+a_l+2}`; so
`X_{il}P_{il} ∈ K_{a_i+a_l+2+Σ_{t≠i,l} a_t} = K_{a+1}`.

*The cone `C_{a+1}`.* `R(A, e_u) = a(1+x)Φ¹ − pᵀadj(M¹)p` has degree at most
`a + 1` (`Φ¹` has degree at most `a`, the entries of `adj(M¹)` at most
`a − 1`, those of `p` at most 1). By (iii) and (K4), `R(A, e_u) ∈ C_{a+1}`. ∎

**Remark (where the difficulty went).** In the merge rule the negative term
is `−2G_1G_2`. For two planted trees it is `−2x⁴J_1J_2`, with `J = Σ δ_v a_v`
a first moment of the distances from the root; `H = Σ a_v` is the moment of
order zero, and the part `x²Σ δ_v² a_v` of `R(A, e_u)` is the second. The
three combine into `Σ (δ_v − δ_{v′})² a_v a_{v′}`. What is left of `R(A_l, e_{c_l})`
after its second moment is taken out is `Q¹_l`, which is one level lower
(`K_{a_l}` instead of `K_{a_l+1}`); it is multiplied by `x²H_i`, which has a
factor `x` more than the term `xΨ_i` that multiplies the whole of
`R(A_l, e_{c_l})`. That extra factor is why the induction closes for planted
trees, and Proposition S34(d) reduces every merge to planted trees.

## Theorem T6 (star minimality and the lower bound)

For a tree `T` and a vertex `u`, `r_u(T) = (1+4x)Ψ + Ω` with the state of
`(T, 0, u)` (this is the definition in `leaf-telescoping.md`).

**Theorem T6.** (a) For every tree `T` of order `n ≥ 1` and every vertex `u`:
`r_u(T) − (1+4x)(1+x)^{n−1} ∈ K_n`.

(b) **(SM).** For every tree `T` of order `n ≥ 2`: `ℓ_T − ℓ_{S_n} ∈ K_{n−1}`,
and `ℓ_T − ℓ_{S_n} ∈ C_{n−1}`. In particular `d_k(T) ≥ d_k(S_n)` for every
`0 ≤ k ≤ n − 2`.

(c) For every tree `T` of order `n ≥ 3`, with `m = ⌊n/2⌋`:

`d_m(T) − d_{m−1}(T) ≥ d_m(S_n) − d_{m−1}(S_n) > 0`,

and every maximizing index of the sequence `d_0(T), …, d_{n−2}(T)` is at
least `⌊n/2⌋`.

*Proof.* (a) *Claim:* for a rooted tree `(B, c)` on `j ≥ 1` vertices,
`Φ(B, e_c) − (1+x)^j ∈ K_j`. For `j = 1` the difference is `0`. For `j ≥ 2`
take a leaf `w ≠ c` with neighbour `y`; by (K3) with `ν = e_c`, `ν_w = 0`:
`Φ(B, e_c) = (1+x)Φ(B − w, e_c) + x det M(B, e_c)[B ∖ {w, y}]`, so
`Φ(B, e_c) − (1+x)^j = (1+x)[Φ(B − w, e_c) − (1+x)^{j−1}] + x det M(B, e_c)[B ∖ {w, y}]`.
The first term is in `K_j` by induction and (K2). The minor is the minor
off the path `(w, y)` of Lemma S32, so it is in `K_{j−2}`, and `x K_{j−2} ⊆ K_j`.

Now `Ψ = Π_i Φ(T_i, e_{u_i})` over the components `T_i` of `T − u`
(`Σ |T_i| = n − 1`). Writing each factor as `(1+x)^{|T_i|} + b_i` with
`b_i ∈ K_{|T_i|}` and expanding, `Ψ − (1+x)^{n−1}` is a sum of products with
one factor from each `K_{|T_i|}`, hence in `K_{n−1}`. As `1 + 4x = (1+x) + 3x`,
`(1+4x)[Ψ − (1+x)^{n−1}] ∈ K_n` by (K2). And `Ω ∈ K_n` by Theorem T5(i).

(b) Build `T` one pendant vertex at a time, `T_1 ⊂ … ⊂ T_n = T`, `T_{k+1}`
being `T_k` with a pendant vertex at `u_k`. By S23(c),
`ℓ_T = −4x(1+x)^{n−1} + Σ_{k=1}^{n−1} (1+x)^{n−1−k} r_{u_k}(T_k)`. For the star
built from its centre the same formula holds with
`r_{u_k}(T_k) = (1+4x)(1+x)^{k−1}` (proof of S23(d)). Subtracting,

`ℓ_T − ℓ_{S_n} = Σ_{k=1}^{n−1} (1+x)^{n−1−k} [r_{u_k}(T_k) − (1+4x)(1+x)^{k−1}]`,

and by (a) for the tree `T_k` of order `k` each bracket is in `K_k`, so each
term is in `K_{n−1}`. The coefficients of `x^n` and `x^{n−1}` are the same in
`ℓ_T` and `ℓ_{S_n}` (`−4` and `0`), so the difference has degree at most
`n − 2` and is in `C_{n−1}` by (K4). Elements of `K_{n−1}` have non-negative
coefficients, which is the last assertion.

(c) `2m − 1 ≤ n − 1`, so `K_{n−1} ⊆ K_{2m−1}` and `λ_m(ℓ_T − ℓ_{S_n}) ≥ 0` by
(b) and Lemma A(a). As `n ≥ 3`, `1 ≤ m ≤ n − 2`, so `λ_m(ℓ_T) = d_m(T) − d_{m−1}(T)`
and the same for the star; `d_m(S_n) − d_{m−1}(S_n) > 0` is S23(d). The last
assertion is R1 (the sequence is positive and log-concave by Theorem 2.1 of
arXiv:1507.02341). ∎

**Remarks.** 1. For odd `n` the bound `⌊n/2⌋` of (c) is that of Theorem T4
(`wiener-form.md`), by a different proof; for even `n` it is one more than
T4 gives, and it is the lower bound of the Collins–Shor conjecture.

2. By the same argument, the polynomial `Ω_T` of
[`even-order.md`](even-order.md) (Proposition S30:
`Ω_T = Σ_k (1+x)^{n−1−k} Ω_{u_k}(T_k)`, a formula that is **not reviewed**) is
in `K_{n−1}` by Theorem T5(i); this is statement (SM⁺) in the cone `K`.

3. The star's value, from the proof of S23(d): for `n = 2m ≥ 4`,
`d_m(S_n) − d_{m−1}(S_n) = C(2m−2, m−2)(2m−1)(3m−5)/((m−1)(m+1))`, which is
`(n−1)(3m−5)/(m+1)·Cat_{m−1}`, the constant of Proposition S30(d). The
inequality (c) is an equality for the star.

## Proposition S36 (contracting an edge)

Let `T` be a tree of order `n` and `uv` a **non-pendant** edge. Let `A` and
`B` be the components of `T − uv` that contain `u` and `v`, of orders
`a, b ≥ 2` (`a + b = n`). Let `T′` be the tree of order `n` obtained from `A`
and `B` by identifying `u` with `v` and attaching one new pendant vertex at
the identified vertex. (`T′` has one leaf more than `T`; repeating the
operation leads from any tree to the star.)

**Proposition S36.** With the states of `(A, 0, u)` and `(B, 0, v)` and
`E_A = E(A, u)`, `E_B = E(B, v)`:

`ℓ_T − ℓ_{T′} = H_A E_B + H_B E_A + x(2 + 5x) H_A H_B + 2 G_A G_B / x`.

Each term is in `K_{n−1}`, and `ℓ_T − ℓ_{T′} ∈ C_{n−1}`. In particular
`d_k(T) ≥ d_k(T′)` for every `0 ≤ k ≤ n − 2`, and
`d_m(T) − d_{m−1}(T) ≥ d_m(T′) − d_{m−1}(T′)` for `m = ⌊n/2⌋`.

*Proof.* Write `Ψ, H, G, Ω, R, E` for `(A, u)`, with `Φ = Ψ + xH`, and
`ψ, h, g, ω, ρ, ε` for `(B, v)`.

*The tree `T′`.* Let `Z` be the merge of `(A, u)` and `(B, v)`, with root `z`.
By S19(d): `Ψ_Z = Ψψ`, `Ω_Z = Ωψ + ωΨ`, `Φ_Z = Ψψ + x(Hψ + hΨ)`,
`R_Z = Rψ + ρΨ + x(Hω + hΩ) + (1+2x)²Ψψ − 2Gg`. By S23(a), (b):
`xℓ_Z = R_Z + (1+4x)Φ_Z` and `ℓ_{T′} = (1+x)ℓ_Z + (1+4x)Ψ_Z + Ω_Z`.

*The tree `T`.* `T` is the merge of the planted tree `(A^, r)` with `(B, v)`.
By S19(c), (b): `Ψ^ = (1+x)Ψ + xH`, `H^ = Ψ + xH`, `G^ = x(xH + G)`,
`R^ = (1+x)R + xΩ`, `Ω^ = R(A, e_u) = R + (1+2x)²Ψ + x(1+x)H + xΩ − 2xG`. By
S19(d): `Φ_T = Ψ^ψ + x(H^ψ + hΨ^)` and
`R_T = R^ψ + ρΨ^ + x(H^ω + hΩ^) + (1+2x)²Ψ^ψ − 2G^g`; and `xℓ_T = R_T + (1+4x)Φ_T`.

*The difference.* `x(ℓ_T − ℓ_{T′}) = [R_T − (1+x)R_Z] + (1+4x)[Φ_T − (1+x)Φ_Z − xΨψ] − x(Ωψ + ωΨ)`.
Substituting:

`Φ_T = (1+2x)Ψψ + x(1+x)(Hψ + hΨ) + x²Hh`, so `Φ_T − (1+x)Φ_Z − xΨψ = x²Hh`;

`R_T − (1+x)R_Z = xΩψ + xρH + x(Ψ − H)ω + xh[R + (1+2x)²Ψ + x(1+x)H − Ω − 2xG] + x(1+2x)²Hψ − 2x²Hg + 2Gg`

(the terms `(1+x)Rψ`, `(1+x)ρΨ`, `(1+x)(1+2x)²Ψψ` cancel; `x(Ψ + xH)ω − x(1+x)Hω = x(Ψ − H)ω`;
`xhΩ^ − x(1+x)hΩ` gives the bracket; `−2G^g + 2(1+x)Gg = −2x²Hg + 2Gg`).
Adding, the terms `xΩψ` and `xΨω` cancel against `−x(Ωψ + ωΨ)`, and

`x(ℓ_T − ℓ_{T′}) = xH[ρ − ω + (1+2x)²ψ − 2xg] + xh[R − Ω + (1+2x)²Ψ − 2xG] + x²(1+x)Hh + (1+4x)x²Hh + 2Gg`
`              = xHε + xhE + x²(2 + 5x)Hh + 2Gg`.

`G` and `g` are divisible by `x` (S33(c)); divide by `x`.

*The cone.* By S33 and Theorem T5: `H ∈ K_{a−2}`, `ε ∈ K_{b+1}`, so
`Hε ∈ K_{n−1}`, and likewise `hE`. `x(2+5x) = 2x(1+x) + 3x²`, so
`x(2+5x)Hh ∈ K_{3+(a−2)+(b−2)} = K_{n−1}`. `2Gg/x = 2x(G/x)(g/x) ∈ K_{2+(a−1)+(b−1)} = K_n ⊆ K_{n−1}`.
The difference has degree at most `n − 2` (the coefficients of `x^n` and
`x^{n−1}` of `ℓ` do not depend on the tree), so it is in `C_{n−1}` by (K4).
The inequalities follow from the non-negativity of the coefficients and from
Lemma A(a), as in Theorem T6(c). ∎

**Remarks.** 1. The coefficient of `x` in the formula is `2 k_A(u) k_B(v)`
(the constant terms of `H_A` and `H_B` are the degrees of the roots, and the
other three terms are divisible by `x²`); this agrees with
`d_1 = 2n² − 6 − Σ_v k_v²` (L2).

2. S36 gives a second proof of (SM) that does not use the telescoped formula
S23(c): each step `T → T′` lowers `ℓ` in the cone order and the star is the
only tree without a non-pendant edge.

## Exact checks

Scratch computations of session 11, exact integer arithmetic; the stored
version is `experiments/CJ-0001-collins-shor-peak/lower_bound.py` (see its
entry in the experiments README for the command and the result file).

- Every rooted tree of order 1 to 9 (486 rooted trees): S33(b), (c), (e);
  S34(a), (b) and the other plant rules; the cone memberships of S33 and of
  Theorem T5 in the cones `C` (`Ψ ∈ C_{a−1}`, `H ∈ C_{a−2}`, `G/x ∈ C_{a−1}`,
  `Ω ∈ C_a`, `E ∈ C_{a+1}`, `R(A, e_u) ∈ C_{a+1}`, `Q¹ ∈ C_a`, `a_v ∈ C_{a−2}`).
  No failure.
- Every pair of rooted trees whose merge has order at most 9 (778 pairs):
  S34(c) and the identity of S35. No failure.
- S36: the formula on 1,064 pairs of rooted trees (total order at most 10);
  `ℓ_T − ℓ_{T′} ∈ C_{n−1}` for every tree of order 4 to 16 and every
  non-pendant edge (220,181 pairs). No failure.

These are finite checks of identities and of memberships; the proofs above
do not depend on them.
