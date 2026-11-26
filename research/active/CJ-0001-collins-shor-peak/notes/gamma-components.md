# CJ-0001 — Conjecture Γ: real roots of `r_A`, the component form, and recurrences for the adjugate

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 7. Propositions S12 to S17, Lemma G and Theorem S18
have written proofs below; **none has been reviewed** unless a report under
[`../reviews/`](../reviews/) names this file. The spectral identity of
Proposition S13(b) was supplied by the project director (G. B. Brito) in the
instructions for this session; its consequences (c) to (e) were drawn by the
agent. Nothing here is a claim of novelty. Conjecture Γ (MD-0010) remains a
conjecture; what this file adds is a structural fact (all roots of `r_A` are
real and negative), a reduction of Γ to a statement about one weighted tree,
and an induction that closes except for one explicit polynomial.

Notation: that of [`skeleton-locality.md`](skeleton-locality.md) and
[`gamma-reduction.md`](gamma-reduction.md) (`S`, `A`, `B = V ∖ A`, `a`, `t`,
`g_w`, `τ`, `z`, `L_B`, `Φ_B`, the cones `C_d`). Throughout,
`M = I + xL_B` and `p = 1 + xτ_B`, the vector with entries
`p_w = 1 + (2 − g_w)x`, `w ∈ B`.

Two elementary facts about the cones, used repeatedly (both read off the
conditions `e + i ≤ d`, `2e + i ≥ d`): `x · C_d ⊆ C_{d+1}` and
`x · C_d ⊆ C_{d+2}`; `x(1 + x) · C_d ⊆ C_{d+3}`.

## Proposition S12 (third form of `r_A`)

**Proposition S12.** For every tree `S` on `s ≥ 2` vertices and every
`A ⊆ V`,

`r_A(x) = r_V(x) · Φ_B(x) − pᵀ adj(I + xL_B) p`,  `r_V = s + (s + 3)x`.

*Proof.* By the first form of Proposition S7,
`r_A = Φ_B [a + (s + 3 − 1ᵀτ_B)x] + x zᵀ adj(M) p`. Since `z = L_B 1 − τ_B`,
`xz = (1 + xL_B 1) − (1 + xτ_B) = M1 − p`. `M` is symmetric and
`M adj(M) = Φ_B I`, so `x zᵀ adj(M) p = Φ_B 1ᵀp − pᵀ adj(M) p`, and
`1ᵀp = t + x 1ᵀτ_B`. Adding, the bracket becomes `a + t + (s + 3)x`, and
`a + t = s`. ∎

## Proposition S13 (spectral form; the roots of `r_A`)

**Proposition S13.** Let `S` be a tree on `s ≥ 2` vertices and `A ⊆ V` with
`1 ≤ a ≤ s − 1`.

(a) `L_B` is positive definite.

(b) (Director's identity.) Let `λ_1, …, λ_t > 0` be the eigenvalues of `L_B`,
`U` an orthogonal matrix with `L_B = U diag(λ) Uᵀ`, and `y = Uᵀz`. Then

`zᵀ adj(I + xL_B) z = Σ_i y_i² Π_{l ≠ i} (1 + λ_l x)`,

a polynomial with non-negative coefficients.

(c) Put `κ = s + 3 − τ_Bᵀ L_B^{−1} τ_B`. Then `r_A` has degree exactly `t + 1`
and leading coefficient `κ · det L_B`, and **`κ ≥ 4`, with equality if and
only if `a = 1`**.

(d) **All `t + 1` roots of `r_A` are real and negative.** Hence every
coefficient of `r_A` is positive, and the coefficients form a log-concave
sequence.

(e) If `a ≥ 2` and `P_A` is the distance matrix of `S` restricted to `A`,
then `(κ − 4) · 1ᵀ adj(P_A) 1 = 2 det P_A`; that is, `κ = 4 + 2/(1ᵀP_A^{−1}1)`
whenever `P_A` is invertible and `1ᵀP_A^{−1}1 ≠ 0`.

*Proof.* (a) For a real vector `f` on `B`, extended by `0` on `A`,
`fᵀL_B f = fᵀLf = Σ_{uv ∈ E(S)} (f_u − f_v)²`. If this is `0`, `f` is constant
on the connected graph `S` and vanishes on `A ≠ ∅`, so `f = 0`.

(b) For an orthogonal `U`, `adj(U) = det(U) Uᵀ` and `adj(XY) = adj(Y) adj(X)`,
so `adj(I + xL_B) = adj(U diag(1 + λ_i x) Uᵀ) = det(U)² U adj(diag(1 + λ_i x)) Uᵀ`,
and the adjugate of a diagonal matrix is the diagonal matrix of the
complementary products. The identity holds for every real `x`, hence as
polynomials. The coefficients are non-negative because `λ_l ≥ 0`. (This
proves the observation recorded in `gamma-reduction.md` on the 47 small
trees: `zᵀ adj(I + xL_B) z` has non-negative coefficients, for every tree and
every `A`; for `A = ∅` the same argument applies with `λ_l ≥ 0`.)

(c) In Proposition S12, `Φ_B` has degree `t` and leading coefficient
`det L_B > 0`, and `adj(I + xL_B)` has entries of degree at most `t − 1`, the
coefficient of `x^{t−1}` being `adj(L_B) = det(L_B) L_B^{−1}` (because
`adj(I + xL_B) = x^{t−1} adj(L_B + x^{−1}I)` for `x ≠ 0`). So the coefficient
of `x^{t+1}` in `r_A` is `(s + 3) det L_B − τ_Bᵀ adj(L_B) τ_B = κ det L_B`.

Bound. Since `L_B` is positive definite,
`τ_Bᵀ L_B^{−1} τ_B = max_f [2 τ_Bᵀf − fᵀL_B f]` over real vectors `f` on `B`,
with the maximum attained only at `f = L_B^{−1}τ_B`. Fix `r ∈ A`, root `S` at
`r`, extend `f` by `0` on `A`, and for `u ≠ r` put `δ_u = f_u − f_{u′}`, `u′`
the parent of `u`. Then `fᵀL_B f = Σ_{u ≠ r} δ_u²` and `f_v` is the sum of
`δ_u` over the vertices `u ≠ r` on the path from `r` to `v`, so
`Σ_v τ_v f_v = Σ_{u ≠ r} δ_u τ(D_u)`, where `D_u` is the set formed by `u` and
its descendants and `τ(D_u) = Σ_{v ∈ D_u} (2 − g_v)`. The degrees of the
vertices of `D_u` add up to `2(|D_u| − 1) + 1` (the edges inside `D_u`, twice,
and the edge from `u` to its parent), so `τ(D_u) = 1`. As `f = 0` on `A`,
`τ_Bᵀf = Σ_{u ≠ r} δ_u`, and

`2 τ_Bᵀf − fᵀL_B f = Σ_{u ≠ r} (2δ_u − δ_u²) ≤ s − 1`,

with equality only if every `δ_u = 1`, that is `f_v = dist(v, r)` for all `v`;
this `f` vanishes on `A` only if `A = {r}`. Hence `τ_Bᵀ L_B^{−1} τ_B ≤ s − 1`,
with equality if and only if `a = 1`, which is the claim.

(d) By the second form of S7 and (b), with `β = 3 + 3H − 2e_B`,

`r_A = Φ_B [a + (a + β)x] − x² Σ_i y_i² Φ_B/(1 + λ_i x)`.

Let `μ_1 < … < μ_q` be the distinct eigenvalues, `c_l` the sum of the `y_i²`
with `λ_i = μ_l`, `Π = {l : c_l > 0}`, `D = Π_{l ∈ Π} (1 + μ_l x)` and
`E_0 = Φ_B/D`, a polynomial of degree `t − |Π|` whose roots are real and
negative. Then `r_A = E_0 · N` with
`N = D [a + (a + β)x] − x² Σ_{l ∈ Π} c_l D/(1 + μ_l x)`, a polynomial of degree
at most `|Π| + 1`. Using `x²/(1 + μx) = x/μ − 1/μ² + 1/(μ²(1 + μx))`,

`N/D = ρ(x) := a + C + κ′x − Σ_{l ∈ Π} (c_l/μ_l²)/(1 + μ_l x)`,  `C = Σ_{l ∈ Π} c_l/μ_l²`,  `κ′ = a + β − Σ_l c_l/μ_l = a + β − zᵀL_B^{−1}z`.

Comparing leading coefficients of `r_A` in this form and in (c):
`κ′ = κ`. (Directly: `β = 3 + t + 1ᵀL_B1 − 2·1ᵀτ_B` by the computation at the
end of the proof of S7, and `zᵀL_B^{−1}z = 1ᵀL_B1 − 2·1ᵀτ_B + τ_BᵀL_B^{−1}τ_B`.)
So `ρ′(x) = κ + Σ_{l ∈ Π} c_l/(μ_l (1 + μ_l x)²) > 0` wherever `ρ` is defined:
`ρ` is strictly increasing on each interval between consecutive poles
`−1/μ_l`. At each pole `ρ → +∞` from the left and `ρ → −∞` from the right;
`ρ(x) → −∞` as `x → −∞` (because `κ > 0`); and `ρ(0) = a > 0`. If `Π ≠ ∅`,
`ρ` therefore has exactly one zero in each of the `|Π| − 1` bounded intervals
between poles, one to the left of all poles, and one between the largest pole
and `0`: `|Π| + 1` distinct negative zeros, all of them zeros of `N = Dρ`.
If `Π = ∅`, `N = a + κx` has the root `−a/κ < 0`. In both cases `N` has
`|Π| + 1` negative roots and degree at most `|Π| + 1`, so these are all its
roots, and `r_A = E_0 N` has `t + 1` real negative roots counted with
multiplicity. A polynomial with positive leading coefficient and only
negative roots is a product of factors `c(x + ξ)`, `ξ > 0`, so its
coefficients are positive; log-concavity is Newton's inequality for
polynomials with real roots.

(e) From `P^{−1} = −L/2 + ττᵀ/(2(s−1))` and `P^{−1}1 = τ/(s−1)` (so
`Pτ = (s−1)1`): multiplying the first identity by `P` on the right gives
`LP = τ1ᵀ − 2I`. Take the rows `B` and a column `v ∈ A`:
`L_B P[B, v] + L[B, A] P[A, v] = τ_B`. With `f = L_B^{−1}τ_B` and
`Θ = −L_B^{−1}L[B, A]`: `f = P[B, v] − Θ P[A, v]`. Then
`τ_Bᵀf = τ_BᵀP[B, v] − (Θᵀτ_B)ᵀP[A, v] = (s − 1) − ωᵀP[A, v]`, with
`ω = τ_A + Θᵀτ_B` (using `τᵀP e_v = s − 1`). So `κ − 4 = ωᵀ P_A e_v` for every
`v ∈ A`, that is `P_A ω = (κ − 4)1`. Since `L1 = 0`, `L[B, A]1 = −L_B1` and
`Θ1 = 1`, so `1ᵀω = 1ᵀτ_A + 1ᵀτ_B = 2`. Multiplying `P_A ω = (κ − 4)1` on the
left by `1ᵀadj(P_A)` gives `2 det P_A = (κ − 4) 1ᵀadj(P_A)1`. ∎

**What S13 does not give.** Real negative roots do not imply a non-negative
half-gamma expansion: `1 + 5x/2 + x²/2` has two negative roots and is not in
`C_2` (the example of the review of Lemma F). The cone is not described by
the roots alone. Two attempts to use the roots are recorded in the journal of
session 7 as failed: pairing the roots, and Darroch's theorem on the mode.

## Proposition S14 (the component form)

For a tree `T` on `j ≥ 1` vertices with vertex set `W`, Laplacian `L_T`,
degrees `k_v`, and a weight `ν : W → {0, 1, 2, …}`, put `N = Σ_v ν_v`,
`g_v = k_v + ν_v`, `M(T, ν) = I + x(L_T + diag ν)`,
`Φ(T, ν) = det M(T, ν)` (as in Lemma F), `p_v = 1 + (2 − g_v)x`, and

`V(T, ν) = pᵀ adj(M(T, ν)) p`,  `R(T, ν) = (N + j − 1)(1 + x) Φ(T, ν) − V(T, ν)`.

Equivalently (the computation of S12 read backwards, with `z_v = g_v + ν_v − 2`,
`1ᵀz = 2N − 2`, `1ᵀτ = 2 − N`):
`R(T, ν) = Φ [(N − 1)(1 + x) + (j − 4 + 3N)x] − x² zᵀ adj(M) z`.
For `j = 1`: `R = (ν − 1)[(1 + x)² + 3x(1 + x) + (ν − 1)x]`, which is in `C_2`
when `ν ≥ 1` (the bracket of Proposition S10).

**Proposition S14.** Let `S` be a tree on `s ≥ 2` vertices, `A ⊆ V` with
`1 ≤ a ≤ s − 1`, `T_1, …, T_c` the components of `S[B]`, `ν_w` the number of
neighbours of `w ∈ B` in `A`, and `e_A` the number of edges of `S[A]`. Then

`r_A = [(1 + 4x) + e_A (1 + x)] Φ_B + Σ_i R(T_i, ν) Π_{l ≠ i} Φ(T_l, ν)`.

Consequently, **if `R(T, ν) ∈ C_{j+1}` for every tree `T` on `j` vertices and
every integer weight `ν ≥ 0`, `ν ≠ 0` (call this statement Γ_c), then
Property Γ⁺ holds for every tree, and so does Conjecture Γ.**

*Proof.* `L_B` is block diagonal with blocks `L_{T_i} + diag ν`, so
`Φ_B = Π_i Φ(T_i, ν)`, `adj(M)` is block diagonal with blocks
`adj(M(T_i, ν)) Π_{l ≠ i} Φ(T_l, ν)`, and the restriction of `p` to `T_i` is
the vector `p` of `(T_i, ν)`, because the degree of `w` in `S` is `k_w + ν_w`.
Hence `pᵀadj(M)p = Σ_i V(T_i, ν) Π_{l ≠ i} Φ(T_l, ν)`. The `s − 1` edges of `S`
are the `e_A` edges inside `A`, the `Σ_i (t_i − 1)` edges inside `B` and the
`Σ_i N_i` edges between them, so `s − 1 = e_A + Σ_i (N_i + t_i − 1)` and
`r_V = (1 + 4x) + e_A(1 + x) + Σ_i (N_i + t_i − 1)(1 + x)`. Substituting in
S12 and using `Φ_B = Φ(T_i, ν) Π_{l ≠ i} Φ(T_l, ν)` for each `i` gives the
identity. For the consequence: `ν ≠ 0` on each `T_i` (Corollary F′), so
`Φ(T_l, ν) ∈ C_{t_l}` by Lemma F; `(1 + 4x) + e_A(1 + x) ∈ C_1`; each term is
in `C_{t+1}`, and Lemma C applies. The case `A = V` is Proposition S3. ∎

Proposition S11 is the dependence on `e_A` in this identity. Γ_c is a
sufficient condition; it is not shown to be equivalent to Γ⁺.

## Lemma G (the adjugate under two elementary operations)

`adj(Y)^ext` denotes the adjugate of a principal submatrix, extended by zero
rows and columns to the index set of the larger matrix.

**Lemma G.** Let `(T, ν)` be a weighted tree, `M = M(T, ν)`.

(G1) *Raising one weight.* For a vertex `w`, with `Y_w = M[W ∖ w]`:
`adj(M + x e_w e_wᵀ) = adj(M) + x · adj(Y_w)^ext`.

(G2) *Removing a leaf.* Let `j ≥ 2`, `w` a leaf with neighbour `u`,
`n = ν_w`, `W′ = W ∖ w`, `X = M(T − w, ν)`, `Y = X[W′ ∖ u] = M[W ∖ {w, u}]`,
`m = 1 + (1 + n)x`, `θ = x(1 + nx)`. Then, for `v, v′ ∈ W′`,

- `adj(M)_{ww} = det X + x det Y`,
- `adj(M)_{wv} = adj(M)_{vw} = x · adj(X)_{uv}`,
- `adj(M)_{vv′} = m · adj(X)_{vv′} + θ · (adj(Y)^ext)_{vv′}`.

*Proof.* All statements are identities between polynomials in `x`; it is
enough to prove them for real `x > 0`, where `M`, `X`, `Y`, `Y_w` and the
matrices below are positive definite (identity plus `x` times a positive
semidefinite matrix), hence invertible.

*A rank-one update.* Let `Z` be symmetric positive definite, `e = e_u` a unit
vector, `Y_0 = Z` with row and column `u` deleted, `ψ = det Y_0 = adj(Z)_{uu}`,
`α = adj(Z)e`, and `c ≥ 0`. By the Sherman–Morrison formula and the matrix
determinant lemma, `det(Z + ceeᵀ) = det Z + cψ` and
`adj(Z + ceeᵀ) = (det Z + cψ)Z^{−1} − c det(Z) Z^{−1}eeᵀZ^{−1} = adj(Z) + c[ψ adj(Z) − ααᵀ]/det Z`.
The inverse of a principal submatrix is a Schur complement of the inverse:
for `v, v′ ≠ u`, `(Y_0^{−1})_{vv′} = (Z^{−1})_{vv′} − (Z^{−1})_{vu}(Z^{−1})_{uv′}/(Z^{−1})_{uu}`;
multiplying by `det(Z) · ψ = det(Z)² (Z^{−1})_{uu}` gives
`ψ adj(Z)_{vv′} − α_v α_{v′} = det(Z) adj(Y_0)_{vv′}`, and the left side
vanishes if `v = u` or `v′ = u`. Therefore

`adj(Z + c e_u e_uᵀ) = adj(Z) + c · adj(Y_0)^ext`.  (∗)

(G1) is (∗) with `Z = M`, `c = x`.

(G2) In block form with `w` first, `M` has the entry `m`, the off-diagonal
block `−x e_uᵀ`, and the block `M[W′] = X + x e_u e_uᵀ`. The Schur complement
of the entry `m` is `S_0 = X + (x − x²/m) e_u e_uᵀ = X + (θ/m) e_u e_uᵀ`, and
`det M = m det S_0`, `(M^{−1})[W′, W′] = S_0^{−1}`,
`(M^{−1})_{wv} = (x/m)(S_0^{−1})_{uv}`. So `adj(M)[W′, W′] = m · adj(S_0)`, and
by (∗) with `c = θ/m`, `adj(S_0) = adj(X) + (θ/m) adj(Y)^ext`: the third
statement. `adj(M)_{wv} = x (adj S_0)_{uv} = x adj(X)_{uv}`, because row `u`
of `adj(Y)^ext` is zero: the second. `adj(M)_{ww} = det M[W′] = det X + x det Y`
by (∗) for determinants: the first. ∎

## Propositions S15, S16 and Corollary S17 (recurrences for `R`)

Notation for a vertex `w` of `T`: `T_1, …, T_q` are the components of `T − w`,
`w_i` the neighbour of `w` in `T_i`, `Φ_i = Φ(T_i, ν + e_{w_i})`,
`R_i = R(T_i, ν + e_{w_i})`, `P_i = Π_{l ≠ i} Φ_l`, `Ψ_w = Π_i Φ_i = adj(M)_{ww}`,
and `π_w(T, ν) = e_wᵀ adj(M(T, ν)) p`.

**Proposition S16 (raising a weight).** For every weighted tree `(T, ν)` and
every vertex `w`,

`R(T, ν + e_w) = R(T, ν) + (1 + x)Φ(T, ν) + 2x π_w(T, ν) + [(ν_w + 1)x(1 + x) − x²] Ψ_w + x Σ_i R_i P_i`.

*Proof.* Passing from `ν` to `ν + e_w` replaces `M` by `M + x e_w e_wᵀ`, `p` by
`p − x e_w`, `N` by `N + 1`, and `Φ` by `Φ + xΨ_w`. By (G1),
`V(T, ν + e_w) = (p − xe_w)ᵀ[adj(M) + x adj(Y_w)^ext](p − xe_w) = V − 2xπ_w + x²Ψ_w + x Σ_i V_i P_i`,
where `V_i = V(T_i, ν + e_{w_i})`: `Y_w` is block diagonal with blocks
`M(T_i, ν + e_{w_i})`, the restriction of `p` to `T_i` is the vector `p` of
`(T_i, ν + e_{w_i})` (the numbers `g_v` agree), and row and column `w` of
`adj(Y_w)^ext` vanish. With `V_i = (N_i + j_i − 1)(1 + x)Φ_i − R_i`,
`N_i = ν(T_i) + 1`, and `Σ_i (N_i + j_i − 1) = N − ν_w + j − 1`:

`R(T, ν + e_w) − R(T, ν) = (1 + x)Φ + (N + j)x(1 + x)Ψ_w + 2xπ_w − x²Ψ_w − x(1 + x)(N + j − 1 − ν_w)Ψ_w + x Σ_i R_i P_i`. ∎

**Proposition S15 (removing a leaf of weight zero).** Let `j ≥ 2`, `w` a leaf
of `T` with neighbour `u` and `ν_w = 0`, `T′ = T − w`, and let `T_i`, `u_i`,
`Φ_i`, `R_i`, `P_i` be as above for the vertex `u` of `T′` (weights
`ν + e_{u_i}`), `Ψ = Π_i Φ_i`. Then

`R(T, ν) = (1 + x) R(T′, ν) + x [ν_u (1 + x) Ψ + Σ_i R_i P_i]`.

*Proof.* Here `m = 1 + x`, `θ = x`, `p_w = 1 + x`. Let `p′` be the vector `p`
of `(T′, ν)`; the restriction of `p` to `W′` is `p′ − x e_u` (the degree of `u`
is one larger in `T`), and its restriction to `T_i` is the vector `p` of
`(T_i, ν + e_{u_i})`. With `Φ′ = Φ(T′, ν)`, `V′ = V(T′, ν)`,
`π′ = e_uᵀadj(X)p′`, `adj(X)_{uu} = Ψ`, Lemma G2 gives

`V(T, ν) = (1+x)²(Φ′ + xΨ) + 2(1+x)x(π′ − xΨ) + (1+x)(V′ − 2xπ′ + x²Ψ) + x Σ_i V_i P_i = (1+x)²Φ′ + (1+x)V′ + x(1+x)Ψ + x Σ_i V_i P_i`;

the terms in `π′` cancel. With `Φ(T, ν) = (1+x)Φ′ + xΨ` (Lemma F),

`R(T, ν) − (1+x)R(T′, ν) = (N + j − 2) x(1+x)Ψ − x Σ_i V_i P_i`,

and `Σ_i V_i P_i = (N + j − 2 − ν_u)(1+x)Ψ − Σ_i R_i P_i`, because
`Σ_i (N_i + j_i − 1) = (N − ν_u + q) + (j − 2) − q`. ∎

**Corollary S17 (a leaf of weight `n`).** Let `j ≥ 2`, `w` a leaf of `T` with
neighbour `u`, `n = ν_w`, `ν⁰` the weight `ν` with `ν_w` replaced by `0`,
`T′ = T − w`, `Φ′ = Φ(T′, ν)`, `Ψ = adj(M(T′, ν))_{uu}`, `π′ = π_u(T′, ν)`,
`Φ′₊ = Φ(T′, ν + e_u) = Φ′ + xΨ`. Then

`R(T, ν) = R(T, ν⁰) + n · E + n(n − 1) · x Φ′₊`,

`E = (1 + x)Φ(T, ν⁰) + x R(T′, ν + e_u) + E*`,  `E* = 2x²π′ + (3x + 2x²)Φ′ + 3x²Ψ`,

and `E = R(T, ν⁰ + e_w) − R(T, ν⁰)`.

*Proof.* Apply S16 at the leaf `w` to the weights `ν⁰ + k e_w`,
`k = 0, …, n − 1`. `T − w` has the single component `T′`, so
`Ψ_w = Φ′₊` and `Σ_i R_i P_i = R(T′, ν + e_u)`, for every `k`.
`Φ(T, ν⁰ + ke_w) = Φ(T, ν⁰) + kxΦ′₊`. By Lemma G2,
`π_w(T, ν⁰ + ke_w) = Φ′₊ (1 + (1 − k)x) + x(π′ − xΨ)`. The increment is

`(1+x)Φ(T, ν⁰) + x R(T′, ν + e_u) + 2x²π′ − 2x³Ψ + xΦ′₊ [k(1+x) + 2 + 2(1−k)x + (k+1)(1+x) − x]`,

and the bracket is `(2k + 3) + 2x`. Since `xΦ′₊(3 + 2x) = (3x + 2x²)Φ′ + (3x² + 2x³)Ψ`,
the increment is `E + 2k · xΦ′₊`; summing over `k` gives the formula. ∎

## Theorem S18 (the induction, and what is missing)

**Theorem S18.** Let `j ≥ 2` and suppose `R(T″, μ) ∈ C_{j″+1}` for every tree
`T″` on `j″ < j` vertices and every integer weight `μ ≥ 0`, `μ ≠ 0`. Let `T`
be a tree on `j` vertices, `ν ≥ 0` an integer weight, and `w` a leaf of `T`
such that `ν` is not identically zero on `T − w`. Then, in the notation of
Corollary S17:

1. `R(T, ν⁰) ∈ C_{j+1}` and `xΦ′₊ ∈ C_{j+1}`;
2. `(1 + x)Φ(T, ν⁰) ∈ C_{j+1}` and `x R(T′, ν + e_u) ∈ C_{j+1}`;
3. consequently `R(T, ν) ∈ C_{j+1}` **if `ν_w = 0`**, and for `ν_w ≥ 1`
   **if `E ∈ C_{j+1}`**.

*Proof.* `R(T, ν⁰)` is given by Proposition S15: `R(T′, ν) ∈ C_j` by
hypothesis (`ν ≠ 0` on `T′`), so `(1+x)R(T′, ν) ∈ C_{j+1}`. `Ψ = Π_i Φ_i ∈ C_{j−2}`
by Lemma F (each weight `ν + e_{u_i}` is non-zero), so `x(1+x)Ψ ∈ C_{j+1}`.
`R_i P_i ∈ C_{j_i+1} · C_{j−2−j_i} = C_{j−1}` by hypothesis and Lemma F, so
`x R_i P_i ∈ C_{j+1}`. `Φ′₊ ∈ C_{j−1}` by Lemma F, so `xΦ′₊ ∈ C_{j+1}`.
`Φ(T, ν⁰) ∈ C_j` by Lemma F (`ν⁰ ≠ 0`), and `R(T′, ν + e_u) ∈ C_j` by
hypothesis, so `x R(T′, ν + e_u) ∈ C_{j+1}`. Statement 3 follows from
Corollary S17. ∎

**Corollary (reduction of Γ_c).** Every tree with at least two vertices has a
leaf `w` with `ν ≠ 0` on `T − w` (if `ν` vanishes outside one leaf, take
another leaf), and if some leaf has weight `0` it can be taken with weight
`0`. So, by induction on `j` from the case `j = 1`: **Γ_c — hence Γ⁺ and
Conjecture Γ — follows from the statement**

> (E) for every tree `T` on `j ≥ 2` vertices in which every leaf has weight at
> least 1, and one leaf `w` of `T`: `E = R(T, ν⁰ + e_w) − R(T, ν⁰) ∈ C_{j+1}`.

In words: in the cone order, `R` does not decrease when the weight of a leaf
goes from `0` to `1`. In `E`, the terms `(1+x)Φ(T, ν⁰)` and `xR(T′, ν + e_u)`
are in `C_{j+1}` (under the induction hypothesis); the open part is the
absorption of `E* = 2x²π′ + (3x + 2x²)Φ′ + 3x²Ψ`.

**`E*` alone is not in the cone.** For `T′` the star with centre `u` and three
leaves, `ν_u = 0` and leaf weights `2, 2, 3`:
`E* = 3x + 46x² + 260x³ + 642x⁴ + 583x⁵ − 6x⁶`, with a negative leading
coefficient (`component_form.py`, field `part3_estar_examples`). So a proof
of (E) has to use `xR(T′, ν + e_u)` or `(1+x)Φ(T, ν⁰)`; the linear form
`π′ = π_u(T′, ν)` has no sign.

A useful identity for that: by S16 applied to `(T′, ν)` at `u`,

`2xπ′ = R(T′, ν + e_u) − R(T′, ν) − (1 + x)Φ′ − [(ν_u + 1)x(1 + x) − x²]Ψ − x Σ_i R_i P_i`,

so `π′` is itself a difference of values of `R`.

## Verification by computation

`experiments/CJ-0001-collins-shor-peak/component_form.py` (exact integers;
Faddeev–LeVerrier for `det` and `adj`; Sturm sequences for the roots), result
file `results/component-form.json`. It computes `r_A` from the second form of
S7 (compared with the definition by `locality_check.py`, not here).

- Part 1, the 47 trees with 2 to 8 vertices, 7,726 subsets with
  `1 ≤ a ≤ s − 1`: S13(c), (d), (e) and, for `e_A = 0`, the identity of S14 —
  zero failures; the smallest value of `κ − 4` over the subsets with `a ≥ 2`
  is `1`.
- Part 2, all weighted trees with `j ≤ 7` and weights in `{0, 1, 2}`:
  `R(T, ν) ∈ C_{j+1}` in every case (Γ_c on this range); Lemma G2 entry by
  entry; `R(T, ν) − (1 + (1+ν_w)x) R(T − w, ν) ∈ C_{j+1}` for every admissible
  leaf.
- Part 3, `j ≤ 6`: the equivalence of the two expressions of `R`; Corollary
  S17 as an identity; `R(T, ν⁰) ∈ C_{j+1}`; `E ∈ C_{j+1}` in every case;
  `E* ∉ C_{j+1}` in some cases.

The counts are in the result file and in the journal entry of session 7.
These are finite checks: they support the identities on the range computed
and are evidence, not proof, for Γ_c and (E).
