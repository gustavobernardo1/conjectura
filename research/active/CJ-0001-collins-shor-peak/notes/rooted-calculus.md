# CJ-0001 — Conjecture Γ: statements (E″) and (S) are false; the rooted state of a weighted tree; statement (Λ)

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 8. Propositions S19 to S22 have written proofs below;
**none has been reviewed** unless a report under [`../reviews/`](../reviews/)
names this file. Statement (Λ) is a conjecture of this session, supported by
exact finite computation only. Nothing here is a claim of novelty. Conjecture
Γ (MD-0010) remains a conjecture.

What this file does. Session 7 left a plan: prove statement (E) of
[`gamma-components.md`](gamma-components.md) through a stronger statement
(E″) that involves no `R`, and (E″) through a slope statement (S), by an
induction on a family indexed by a multiset of vertices. **(E″) and (S) are
false** (Proposition S21): the plan cannot be completed, whatever the family.
(E) itself is not affected. In its place this file gives (i) a description of
`R(T, ν)` by a *rooted state* with three rules, in which the whole difficulty
is one product `−2G₁G₂` of polynomials with non-negative coefficients
(Proposition S19); (ii) a formula for the increment of `R` when one weight is
raised, at any vertex (Proposition S20); (iii) a statement (Λ) that implies
(E) at every leaf without any hypothesis on the weights, and has no failure
in the range where (E″) and (S) fail (Proposition S22).

Notation: that of [`gamma-components.md`](gamma-components.md). A weighted
tree `(T, ν)` has `j ≥ 1` vertices, vertex set `W`, degrees `k_v`, integer
weights `ν_v ≥ 0` (the zero weight is allowed unless excluded), `N = Σ ν_v`,
`M = M(T, ν) = I + x(L_T + diag ν)`, `Φ = Φ(T, ν) = det M`,
`p_v = 1 + (2 − k_v − ν_v)x`, `π_u = e_uᵀ adj(M) p`,
`R(T, ν) = (N + j − 1)(1 + x)Φ − pᵀ adj(M) p`. `C_d` is the cone of Lemma C;
`C_d · C_e ⊆ C_{d+e}`, and the elements of `C_d` have non-negative
coefficients and degree at most `d`.

## The rooted state

Fix a vertex `u` (the *root*). Let `T_1, …, T_q` be the components of `T − u`
(`q = k_u`), `u_i` the neighbour of `u` in `T_i`,
`Φ_i = Φ(T_i, ν + e_{u_i})`, `P_i = Π_{l ≠ i} Φ_l`. Define

- `Ψ = adj(M)_{uu} = Π_i Φ_i` (`Ψ = 1` if `j = 1`);
- `H = (Φ − Ψ)/x`;
- `G = (1 + 2x)Ψ − π_u`;
- `Ω = Σ_i R(T_i, ν + e_{u_i}) P_i` (`Ω = 0` if `j = 1`).

`H` is a polynomial: `Φ` and `Ψ` have constant term 1. The *rooted state* of
`(T, ν, u)` is `(Ψ, H, G, Ω, R)` together with the number `ν_u`.

Three operations build every rooted weighted tree from single vertices:

- *raise*: add 1 to the weight of the root;
- *plant*: add a new vertex `r` of weight 0 adjacent to `u`, and take `r` as
  the root (the result is written `(T^, ν, r)`);
- *merge*: from `(T_1, ν^1, u_1)` and `(T_2, ν^2, u_2)` on disjoint vertex
  sets, identify `u_1` with `u_2`; the root is the identified vertex and its
  weight is the sum of the two root weights.

Indeed `(T, ν, u)` is the merge of the single vertex of weight `ν_u` with the
planted trees `(T_i^, ν, r_i)`, `i = 1, …, q` (each `T_i` rooted at `u_i`,
with the weight `ν`, not raised).

## Proposition S19 (rules for the rooted state)

**Lemma (★).** For every rooted weighted tree,
`Ψ · R = Φ · [ν_u (1 + x)Ψ + Ω] − π_u²`.

*Proof.* It is an identity between polynomials; take `x > 0` real, where `M`
and its principal submatrices are positive definite. Write `M` in block form
with `u` first: the entry `d = 1 + x(k_u + ν_u)`, the column `b` (equal to
`−x` at each `u_i` and `0` elsewhere) and the block `Y = M[W ∖ u]`, which is
block diagonal with blocks `M(T_i, ν + e_{u_i})`. Let `q` be the restriction
of `p` to `W ∖ u`; its restriction to `T_i` is the vector `p` of
`(T_i, ν + e_{u_i})`, as in the proof of S16. Then `det Y = Ψ`,
`Φ = Ψ(d − bᵀY^{−1}b)`, `(M^{−1})_{uu} = Ψ/Φ`, and the row `u` of `M^{−1}`
outside `u` is `−(Ψ/Φ) bᵀY^{−1}`. Hence `π_u = Φ e_uᵀM^{−1}p = Ψ(p_u − bᵀY^{−1}q)`,
and by the formula for the inverse of a block matrix
`pᵀM^{−1}p = qᵀY^{−1}q + (p_u − bᵀY^{−1}q)² Ψ/Φ`. Multiplying by `ΦΨ`:
`Ψ · pᵀadj(M)p = Φ · qᵀadj(Y)q + π_u²`. Now
`qᵀadj(Y)q = Σ_i V(T_i, ν + e_{u_i}) P_i = (N − ν_u + j − 1)(1 + x)Ψ − Ω`,
by the definition of `R(T_i, ·)` and `Σ_i (N_i + j_i − 1) = N − ν_u + j − 1`
(`N_i = ν(T_i) + 1`), as in the proof of S16. Substituting in
`ΨR = (N + j − 1)(1 + x)ΦΨ − Ψ pᵀadj(M)p` gives the claim. For `j = 1`:
`Ψ = 1`, `Ω = 0`, `R = ν(1 + x)(1 + νx) − (1 + (2 − ν)x)²`, which is the value
of `R` for one vertex. ∎

**Proposition S19.**

(a) *One vertex of weight `n`*: `Ψ = 1`, `H = n`, `G = nx`, `Ω = 0`,
`R = (n − 1)(1 + 5x + 4x²) + (n − 1)²x`.

(b) *Raise.* `Ψ` and `Ω` do not change; `H` becomes `H + Ψ`; `G` becomes
`G + xΨ`; and

`Δ_u := R(T, ν + e_u) − R(T, ν) = [(1 + 2x)² + ν_u x(1 + x)]Ψ + x(1 + x)H + xΩ − 2xG`.

(c) *Plant.* `Ψ^ = Φ + xΨ = Φ(T, ν + e_u)`, `H^ = Φ`, `G^ = x(xH + G)`,
`Ω^ = R(T, ν + e_u)`, `R^ = (1 + x)R + x[ν_u (1 + x)Ψ + Ω]`, and the new root
has weight 0.

(d) *Merge.* With the indices 1, 2 for the two trees and `ν_1`, `ν_2` for
their root weights: `Ψ = Ψ_1Ψ_2`; `X = X_1Ψ_2 + X_2Ψ_1` for `X = H, G, Ω`; and

`R = R_1Ψ_2 + R_2Ψ_1 + x(H_1Ω_2 + H_2Ω_1) + x(1 + x)(ν_2 H_1Ψ_2 + ν_1 H_2Ψ_1) + (1 + 2x)²Ψ_1Ψ_2 − 2G_1G_2`.

(e) `Ψ`, `H` and `G` have non-negative coefficients, for every rooted
weighted tree.

*Proof.* (a) `Φ = 1 + nx`, `adj(M) = 1`, `p = 1 + (2 − n)x`; the value of `R`
is in `gamma-components.md`, before S14.

(b) `M` becomes `M + x e_u e_uᵀ` and `p` becomes `p − x e_u`. `Y` and the
components of `T − u` with their weights do not change, so `Ψ` and `Ω` do
not. `Φ` becomes `Φ + xΨ`. By (G1), `adj(M)` becomes `adj(M) + x adj(Y)^ext`,
whose row `u` is that of `adj(M)`; so `π_u` becomes `π_u − xΨ` and `G`
becomes `G + xΨ`. Proposition S16 gives
`Δ_u = (1 + x)Φ + 2xπ_u + [(ν_u + 1)x(1 + x) − x²]Ψ + xΩ`; substituting
`Φ = Ψ + xH` and `π_u = (1 + 2x)Ψ − G`, the coefficient of `Ψ` is
`(1 + x) + 2x(1 + 2x) + (ν_u + 1)x(1 + x) − x² = (1 + 2x)² + ν_u x(1 + x)`.

(c) `T^ − r` has the single component `T`, with neighbour `u`: this gives
`Ψ^` and `Ω^`. `Φ(T^, ν) = (1 + x)Φ + xΨ` (Lemma F; Lemma G2 with `n = 0`),
so `H^ = Φ`. By Lemma G2, `adj(M^)_{rr} = Φ + xΨ` and
`adj(M^)_{rv} = x adj(M)_{uv}`; `p_r = 1 + x` and the restriction of the
vector `p` of `T^` to `W` is `p − x e_u`. So
`π_r(T^) = (1 + x)(Φ + xΨ) + x(π_u − xΨ) = (1 + x)Φ + xΨ + xπ_u`, and
`G^ = (1 + 2x)(Φ + xΨ) − (1 + x)Φ − xΨ − xπ_u = xΦ + 2x²Ψ − x[(1 + 2x)Ψ − G] = x(Φ − Ψ) + xG`.
`R^` is Proposition S15 for the leaf `r`.

(d) In the block form of the proof of (★), the merged tree has
`Y = Y_1 ⊕ Y_2`, `b = (b_1, b_2)`, `q = (q_1, q_2)`, and `k_u`, `ν_u` are the
sums. So `Ψ = Ψ_1Ψ_2`, `adj(Y) = Ψ_2 adj(Y_1) ⊕ Ψ_1 adj(Y_2)`, and each of
`β = bᵀadj(Y)b`, `B = bᵀadj(Y)q` satisfies `X = X_1Ψ_2 + X_2Ψ_1`. Since
`xH = Φ − Ψ = x(k_u + ν_u)Ψ − β` and
`G = (1 + 2x − p_u)Ψ + B = x(k_u + ν_u)Ψ + B`, so do `H` and `G`; and `Ω`
does by its definition, the components of `T − u` being those of `T_1 − u_1`
and `T_2 − u_2`. For `R`, put `A_k = ν_k(1 + x)Ψ_k + Ω_k`, so that
`Ψ_kR_k = Φ_kA_k − π_k²` (★), and for the merged tree
`ν_u(1 + x)Ψ + Ω = A_1Ψ_2 + A_2Ψ_1`,
`Φ = Ψ + xH = Φ_1Ψ_2 + Φ_2Ψ_1 − Ψ_1Ψ_2`,
`π_u = (1 + 2x)Ψ − G = π_1Ψ_2 + π_2Ψ_1 − (1 + 2x)Ψ_1Ψ_2`. By (★) for the merged
tree,

`Ψ_1Ψ_2 R = (Φ_1Ψ_2 + Φ_2Ψ_1 − Ψ_1Ψ_2)(A_1Ψ_2 + A_2Ψ_1) − (π_1Ψ_2 + π_2Ψ_1 − (1 + 2x)Ψ_1Ψ_2)²`.

Expanding, `Φ_1A_1Ψ_2² − π_1²Ψ_2² = Ψ_1Ψ_2 · R_1Ψ_2` and likewise for the index
2; every other term contains `Ψ_1Ψ_2`, and after division by `Ψ_1Ψ_2`:

`R = R_1Ψ_2 + R_2Ψ_1 + (Φ_1 − Ψ_1)A_2 + (Φ_2 − Ψ_2)A_1 − 2π_1π_2 + 2(1 + 2x)(π_1Ψ_2 + π_2Ψ_1) − (1 + 2x)²Ψ_1Ψ_2`.

The last three terms are `−2(π_1 − (1 + 2x)Ψ_1)(π_2 − (1 + 2x)Ψ_2) + (1 + 2x)²Ψ_1Ψ_2 = −2G_1G_2 + (1 + 2x)²Ψ_1Ψ_2`,
and `(Φ_1 − Ψ_1)A_2 = xH_1[ν_2(1 + x)Ψ_2 + Ω_2]`.

(e) By induction on the construction: for one vertex the three polynomials
are `1`, `n`, `nx`; (b) and (d) preserve non-negative coefficients; in (c),
`Φ = Ψ + xH`, so `Ψ^`, `H^`, `G^` have non-negative coefficients. ∎

**Remarks.** (1) By (e), `π_u = (1 + 2x)Ψ − G` with `G ≥ 0` coefficientwise:
this is the sign information on the linear form `π_u` that session 7 did not
have. Also `G = x[2Ψ − H + Σ_v adj(M)_{uv}(k_v + 2ν_v − 2)]` (from
`adj(M)(1 + xν) = Φ1`; checked by computation, not used below).
(2) In (d), every term except `−2G_1G_2` is a product of polynomials that are
in cones under the hypotheses of an induction (`R_k`, `Ω_k` by Γ_c for
smaller trees; `Ψ_k` by Lemma F). A proof of Γ_c by induction on the rooted
construction has to absorb exactly this product.
(3) Dividing by `Ψ`: `h = H/Ψ`, `g = G/Ψ`, `o = Ω/Ψ` and `ν_u` are *additive*
under merges, and (★) reads
`R/Ψ = (1 + xh)(ν_u(1 + x) + o) − (1 + 2x − g)²`.

## Proposition S20 (the increment of `R` at a vertex; `Λ`)

For a rooted weighted tree put

`Λ(T, ν, u) = x[(1 − x)Φ + 2xΨ + R(T, ν + e_u) − 2xG]`,

and recall `F(T, ν, u) = (1 + 5x + 3x²)Φ + (x + 4x²)Ψ + 2x²π_u` (session 7).

**Proposition S20.**

(a) `F = (1 + x)²(1 + 4x)Ψ + x(1 + 5x + 3x²)H − 2x²G`.

(b) *At a new leaf.* For the planted tree `(T^, ν, r)`, the increment
`E = R(T^, ν + e_r) − R(T^, ν)` (the polynomial `E` of Corollary S17, with
`T^`, `r`, `T`, `u` in the roles of `T`, `w`, `T′`, `u` there) satisfies

`E = (1 + 2x)² Φ(T, ν + e_u) + Λ(T, ν, u)`
`  = x R(T, ν + e_u) + F(T, ν, u)`
`  = xR + x²Ω + [(1 + x)²(1 + 4x) + x(1 + 2x)² + ν_u x²(1 + x)]Ψ + x(1 + 6x + 4x²)H − 4x²G`.

(c) *At any vertex.* For every weighted tree and every vertex `u`, with
`T_c` the components of `T − u`, each rooted at the neighbour `c` of `u` and
carrying the weight `ν` (not raised), and `P_c = Π_{l ≠ c} Φ(T_l, ν + e_l)`:

`Δ_u = R(T, ν + e_u) − R(T, ν) = [(1 + 2x)² + 2xν_u]Ψ + Σ_c Λ(T_c, ν, c) P_c`.

(d) `Ψ · Λ = x {Φ(T, ν + e_u) [(2 + ν_u(1 + x))Ψ + Ω] − (Ψ − G)² − xΨ²}`.

*Proof.* (a) Substitute `Φ = Ψ + xH`, `π_u = (1 + 2x)Ψ − G`; the coefficient of
`Ψ` is `1 + 6x + 9x² + 4x³ = (1 + x)²(1 + 4x)`.

(b) By S19(b) at the root `r` of `T^` (weight 0) and S19(c):
`E = (1 + 2x)²(Φ + xΨ) + x(1 + x)Φ + xR(T, ν + e_u) − 2x²(Φ − Ψ + G)`, which
is the first line. The second is Corollary S17 (`E = (1 + x)Φ(T^, ν) + xR(T, ν + e_u) + E*`
with `Φ(T^, ν) = (1 + x)Φ + xΨ`). For the third, write
`R(T, ν + e_u) = R + Δ_u` in the first line and use S19(b): the coefficient
of `Ψ` is `(1 + 2x)²(1 + x) + x(1 − x) + 2x² + x(1 + 2x)² + ν_u x²(1 + x)`, and
`(1 + 2x)²(1 + x) + x(1 + x) = (1 + x)²(1 + 4x)`; that of `H` is
`x(1 + 2x)² + x²(1 − x) + x²(1 + x) = x(1 + 6x + 4x²)`; that of `G` is
`−2x² − 2x²`.

(c) `(T, ν, u)` is the merge of the vertex `u` of weight `ν_u` with the
planted trees `(T_c^, ν, r_c)`. By S19(d), applied repeatedly, each of
`X = H, G, Ω` is the sum of the contributions `X_part · Π Ψ_other` of the
parts, and `Ψ` is the product. In S19(b) the vertex contributes
`ν_u[x(1 + x) − 2x²]Ψ` to `x(1 + x)H − 2xG`, which with `ν_u x(1 + x)Ψ` gives
`2xν_uΨ`; a planted tree contributes, by S19(c),
`[x(1 + x)Φ_c + xR(T_c, ν + e_c) − 2x²(Φ_c − Ψ_c + G_c)]P_c = Λ(T_c, ν, c) P_c`
(`Φ_c`, `Ψ_c`, `G_c` those of `(T_c, ν, c)`).

(d) (★) for the weight `ν + e_u`, with S19(b):
`ΨR(T, ν + e_u) = Φ(T, ν + e_u)[(ν_u + 1)(1 + x)Ψ + Ω] − (π_u − xΨ)²`, and
`π_u − xΨ = (1 + x)Ψ − G`. Then
`ΨΛ/x = (1 − x)ΦΨ + 2xΨ² + ΨR(T, ν + e_u) − 2xGΨ`, `Φ = Φ(T, ν + e_u) − xΨ`, and
`−((1 + x)Ψ − G)² − 2xGΨ + 2xΨ² − x(1 − x)Ψ² = −(Ψ − G)² − xΨ²`. ∎

In (b), the third line shows `E` with a single negative term, `−4x²G`, `G`
having non-negative coefficients.

## Proposition S21 ((E″) and (S) are false)

Statement (E″) of session 7: `F(T, ν, u) ∈ C_{j+2}` for every rooted weighted
tree with `ν ≠ 0`. Statement (S): `x[F(T, ν + e_v, u) − 2x³ adj(M(T, ν))_{uv}] ∈ C_{j+3}`
for every weighted tree, all vertices `u, v` and every `ν ≥ 0`.

**Proposition S21.** Let `T` be the star with centre `u` of weight `n_0` and
`q ≥ 1` leaves of weights `n_1, …, n_q`; put `Π = Π_i (1 + n_i)` and
`σ = Σ_i n_i/(1 + n_i)`.

(a) The coefficient of `x^{q+3}` in `F(T, ν, u)` is `Π · (4 + n_0 − σ)`.

(b) The coefficient of `x^{q+4}` in `x[F(T, ν + e_u, u) − 2x³Ψ]` (the
polynomial of (S) for `v = u`) is `Π · (3 + n_0 − σ)`.

(c) Hence **(E″) is false**: `F ∉ C_{q+3}` whenever `σ > 4 + n_0`, for example
for `n_0 = 0` and six leaves of weight 3 (`j = 7`, leading coefficient
`−2048`). **(S) is false**: for `n_0 = 0` and four leaves of weight 4
(`j = 5`, `u = v` the centre) the leading coefficient is `−125`.

*Proof.* The star is the merge of the vertex `u` with the planted single
vertices. By S19(a), (c), a planted vertex of weight `n` has `Ψ = 1 + (n + 1)x`,
`H = 1 + nx`, `G = 2nx²`. By S19(d), `Ψ = Π_i (1 + (n_i + 1)x)`, of degree `q`
with leading coefficient `Π`; `H = n_0Ψ + Σ_i (1 + n_i x) Π_{l ≠ i}(1 + (n_l + 1)x)`,
of degree `q` with leading coefficient `Π(n_0 + σ)`; `G = n_0xΨ + Σ_i 2n_i x² Π_{l ≠ i}(1 + (n_l + 1)x)`,
of degree `q + 1` with leading coefficient `Π(n_0 + 2σ)`. By S20(a) the
coefficient of `x^{q+3}` in `F` is `4Π + 3Π(n_0 + σ) − 2Π(n_0 + 2σ)`: (a).
Raising `n_0` by one and subtracting `2Π` gives (b). A polynomial with a
negative coefficient is in no cone `C_d`: (c); `4^6 (4 − 9/2) = −2048`,
`5^4 (3 − 16/5) = −125`. ∎

**Smaller failures (exact computation).** The leading coefficient is not the
only obstruction. For `n_0 = 0` and five leaves of weight 4 (`j = 6`,
`σ = 4`): `F = 1 + 36x + 554x² + 4744x³ + 24505x⁴ + 76600x⁵ + 134500x⁶ + 102500x⁷`
has degree 7 and its expansion of degree 8 ends with the coefficient `−1`;
this is the only failure of (E″) among all weighted trees with `j ≤ 6` and
weights 0 to 4. (S) fails first at `j = 5` (the star with leaf weights
`2, 3, 4, 4`, centre of weight 0, `u = v` the centre; 31 failures at `j = 5`,
7,194 at `j = 6`, weights 0 to 4, also on trees that are not stars and with
`u ≠ v`). Counts: `results/slope-family.json`; the counterexamples are
confirmed by a checker that shares no code with the search
(`slope_family_verify.py`).

**What this refutes and what it does not.** The range of session 7 (`j ≤ 5`,
weights 0 to 2; `j ≤ 4`, weights up to 4) contains no failure, which is why
the statements were proposed. The induction of session 7 — (E) through (E″),
(E″) through (S), (S) through a family indexed by a multiset of vertices —
is abandoned: its first two members are false. **(E), Γ_c and Conjecture Γ
are not affected**: in every counterexample above, `E`, `R` and `Λ` are in
their cones (for five leaves of weight 4, `E` has leading coefficient
`112500` and is in `C_8`). The reason is visible in S20(b): `E = xR(T, ν + e_u) + F`,
and for the star the leading coefficient of `xR(T, ν + e_u)` exceeds the
deficit of `F`. A proof of (E) cannot discard `R(T, ν + e_u)`.

## Statement (Λ) and Proposition S22

> **(Λ)** For every tree `T` on `j ≥ 1` vertices, every vertex `u` and every
> integer weight `ν ≥ 0` (the zero weight included):
> `Λ(T, ν, u) = x[(1 − x)Φ + 2xΨ + R(T, ν + e_u) − 2xG] ∈ C_{j+2}`.

By S20(b), `Λ = E − (1 + 2x)²Φ(T, ν + e_u)`: (Λ) says that the increment of
`R` at a new leaf exceeds `(1 + 2x)²Φ(T, ν + e_u)` in the cone order. It keeps
`R(T, ν + e_u)`, which (E″) had discarded.

**Proposition S22.** Suppose (Λ) holds for every rooted weighted tree with
fewer than `j` vertices. Then for every weighted tree `(T, ν)` on `j`
vertices, `ν ≥ 0` arbitrary, and **every vertex** `u`:
`R(T, ν + e_u) − R(T, ν) ∈ C_{j+1}`. In particular, if (Λ) holds, then (E)
holds for every leaf and every weight, and so do Γ_c, Γ⁺ and Conjecture Γ.

*Proof.* In S20(c), `Ψ = Π_l Φ(T_l, ν + e_l) ∈ C_{j−1}` by Lemma F (every
weight `ν + e_l` is non-zero; `Ψ = 1 ∈ C_0` if `j = 1`);
`(1 + 2x)² = (1 + x)² + 2x(1 + x) + x² ∈ C_2` and `x ∈ C_2`; so the first term
is in `C_{j+1}`. `Λ(T_c, ν, c) ∈ C_{j_c+2}` by hypothesis and
`P_c ∈ C_{j−1−j_c}` by Lemma F, so each product is in `C_{j+1}`. (E) is the
case of a leaf `u` with `ν_u = 0`; then Theorem S18 and its corollary give
Γ_c, and S14 gives Γ⁺ and Γ. ∎

So the cone order makes `R` non-decreasing in every weight, at every vertex,
if (Λ) holds — a statement that session 7 had only at leaves and as a
hypothesis. (Λ) is sufficient; it is not shown to be necessary for Γ_c.

**Evidence for (Λ)** (exact; `rooted_state.py`, `results/rooted-state.json`;
the counts are in the result file and in the journal entry of session 8): no
failure among all rooted weighted trees with `j ≤ 5` and weights 0 to 2; all
rooted stars with at most 6 leaves and weights up to 5 (centre weights 0, 1,
3), which contain the counterexamples to (E″) and (S); and random trees with
up to 9 vertices and weights up to 20. On the same ranges the increment
`R(T, ν + e_u) − R(T, ν)` is in `C_{j+1}` at every vertex (`ν ≠ 0`) and Γ_c
holds. This is finite evidence, not a proof.

**Where the difficulty is.** By S20(d) and Remark 3, with `D = Φ(T, ν + e_u)/Ψ = 1 + x + xh`:
`Λ/(xΨ) = D[2 + ν_u(1 + x) + o] − (1 − g)² − x`, where `h`, `g`, `o` are sums
over the branches at `u`. The negative part is quadratic in `g`, as in
S19(d). (Λ) is not proved, and no induction for it is written. By S20(c),

`Λ(T, ν, u) = x[R(T, ν) + (1 − x)Φ − 2xG + ((1 + 2x)² + 2x(1 + ν_u))Ψ] + x Σ_c Λ(T_c, ν, c) P_c`,

so under (Λ) for the branches the terms to absorb are `−x²Φ` and `−2x²G`,
and the term that must absorb them, `xR(T, ν)`, is itself outside the cone
when `ν = 0` (for one vertex, `R = −(1 + 2x)²`). Whether the first bracket
alone is in `C_{j+1}` was not tested.

## The chain from (S) to Conjecture Γ, and what is actually needed

```
Conjecture Γ (MD-0010): r_A ∈ C_{s−a+1}, |A| ≥ 2
  ⇐ Γ⁺ (the same for |A| ≥ 1)                        [adds |A| = 1]
  ⇐ Γ⁺ for A independent                             [S11, an equivalence]
  ⇐ Γ_c: R(T, ν) ∈ C_{j+1}, ν ≠ 0                    [S14; discards (1+4x)Φ_B + e_A(1+x)Φ_B]
  ⇐ (E): the increment of R at one leaf, for trees   [S18; induction on j]
         whose leaves all have weight ≥ 1
  ⇐ (Λ)                                              [S22; no hypothesis on ν, every leaf]   OPEN
  ⇐ (E″)   FALSE (S21)        ⇐ (S)   FALSE (S21)
```

Each arrow is a sufficient condition; only S11 is known to be an
equivalence. What the application needs is weaker than Γ. Proposition S4
uses `r_A` only through the numbers
`β_A(n) = ([x^c] − [x^{c−1}]) (1 + x)^L r_A`, `L = n − s − a ≥ d − 1`,
`c = ⌈(L + d)/2⌉`, `d = s − a + 1` (from the formula for `β_A(n)` in
`skeleton-identity.md`: the index is `m − a + 1 = ⌊(L + d + 1)/2⌋`). Call
**Γ_w** the statement `β_A(n) ≥ 0` for all `n ≥ 2s` and `|A| ≥ 2`. Γ implies
Γ_w (S4), and the cone of polynomials `f` of degree at most `d` with
`([x^c] − [x^{c−1}])(1 + x)^L f ≥ 0` for all `L ≥ d − 1` is strictly larger
than `C_d`: it contains every palindromic unimodal polynomial of degree `d`
with non-negative coefficients (its product with `(1 + x)^L` is palindromic
and unimodal), for example `1 + x + x² = (1 + x)² − x ∉ C_2`. Γ_w is the
exact requirement of S4 and S5; it is not easier as it stands, because every
proof so far uses that the cones `C_d` are closed under products
(`Φ_B` is a product over components), and no such property is known for the
larger cone.

## Verification by computation

`experiments/CJ-0001-collins-shor-peak/rooted_state.py` (exact integers),
result file `results/rooted-state.json`: S19(b), (c), (d), (e), Remark 1,
S20(b), (c) as identities on every rooted weighted tree of the range; S21(a)
on stars; the cone memberships (E″), (S), (Λ), monotonicity and Γ_c with
their first failures. Lemma (★) and S20(d) were checked on the 750 rooted
weighted trees with `j ≤ 4`, weights 0 to 2, by a script that is not stored.
`slope_family.py`, `slope_family_extension.py`, `slope_family_verify.py`
(computational experimenter, separate context): the identities of session 7
for `F`, the failures of (E″) and (S) for `j ≤ 6`, weights 0 to 4, and their
independent confirmation.
