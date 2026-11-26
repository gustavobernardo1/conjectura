# CJ-0001 — the Wiener form of the distance polynomial of a tree, and the bound `⌊(n−1)/2⌋` on the peak

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 9, and **revised once in session 10** (same model).
The session-9 text (revision `b5d9294`) had one AI review, which found no gap
and three defects of wording. The revision corrects those three defects,
adds Lemma K (a self-contained proof of the cone memberships, so that the
proof of Theorem T4 no longer depends on Lemma F or Lemma C of the earlier
notes) and adds the section "Prior literature". No statement was changed.
A review counts for this text only if its report under
[`../reviews/`](../reviews/) names the revision that contains it. Theorem T4
is a **candidate**: it has not been read by a mathematician, and nothing here
is a claim of novelty (the searches made are recorded in the dossier).

What this file claims. For every tree `T` of order `n ≥ 3`, with
`μ = ⌊(n−1)/2⌋`, the normalized coefficients of the distance characteristic
polynomial satisfy `d_{μ−1} < d_μ` (Theorem T4). By R1, every maximizing
index is at least `⌊(n−1)/2⌋`. For **odd** `n` this is the lower bound
`⌊n/2⌋` of Conjecture 1.2 of arXiv:1507.02341, in the strong reading of ties.
For **even** `n` it is one less than the conjectured bound, and the
conjectured bound is **not** proved here. The upper bound of the conjecture
is not addressed.

## Notation and what is used

`T` is a tree of order `n` with vertex set `V`, distance matrix `D`,
Laplacian `L`, degrees `k_v`, `τ_v = 2 − k_v`. `M = I + xL`,
`Φ = Φ_T = det M`, `adj = adj(M)`. `t = D1` is the vector of transmissions
(`t_v = Σ_u dist(u, v)`) and `W = ½ 1ᵀD1` the Wiener index.
`ℓ_T(x) = −2^{−(n−2)} det(2xI − D)`; for `n ≥ 2` its coefficients are
`d_0, …, d_{n−2}` (the normalized coefficients), `0` at `x^{n−1}` and `−4` at
`x^n` (the trace of `D` is zero and `det(2xI − D)` is monic in `2x`). That
the coefficient of `x^k` is the normalized coefficient `d_k = 2^{k−(n−2)}|δ_k|`
for `0 ≤ k ≤ n−2` uses the sign `(−1)^{n−1}δ_k > 0` (Fact 1.1 of
arXiv:1507.02341, from Graham–Lovász) and Observation 3.1 of
arXiv:1507.02341, as recorded in [`lemmas.md`](lemmas.md), "Notation".

Used from earlier notes:

- **L1** ([`lemmas.md`](lemmas.md); Graham–Lovász 1978, quoted there):
  `ℓ_T = (n−1)Φ − x τᵀ adj τ`.
- **Lemma F** ([`gamma-reduction.md`](gamma-reduction.md); AI-reviewed): for
  a tree `K` on `j ≥ 1` vertices and an integer weight `ν ≥ 0`, `ν ≠ 0`,
  `Φ(K, ν) := det(I + x(L_K + diag ν)) ∈ C_j`; and the expansion in its proof
  at a leaf `w` with neighbour `u`:
  `det M = (1 + (1+ν_w)x) det M[W∖w] − x² det M[W∖{w,u}]`.
- **R1** ([`lemmas.md`](lemmas.md); formalized in Lean): for a positive
  log-concave sequence, every maximizing index is `≥ j` if and only if
  `a_{j−1} < a_j`. The sequence `d_0, …, d_{n−2}` is positive and log-concave
  (Theorem 2.1 of arXiv:1507.02341).
- The cone `C_d`: the non-negative combinations of `x^e(1+x)^i` with
  `e + i ≤ d ≤ 2e + i` (the definition of
  [`gamma-reduction.md`](gamma-reduction.md), section "The cones `C_d`",
  which also states the product rule `C_d · C_{d′} ⊆ C_{d+d′}`; it is the form
  in which Lemma F is stated). By Lemma C of
  [`skeleton-locality.md`](skeleton-locality.md) this is the same set as the
  half-gamma form `Σ_{2e<d} ρ_e x^e(1+x)^{d−2e} + Σ_{d≤2e≤2d} σ_e x^e`,
  `ρ_e, σ_e ≥ 0`. **The proof of Theorem T4 uses only the cones `K_d` below**;
  with Lemma K it needs neither Lemma F nor Lemma C. The cones `C_d` appear
  in this note only in the sharper conclusion `Π_{uv} ∈ C_{n−d−1}` of Lemma
  S24, which later notes use.

**The cones `K_d`.** For an integer `d`, let `K_d` be the set of finite
non-negative combinations of the polynomials `x^e(1+x)^i`, `e, i ≥ 0`
integers, `2e + i ≥ d`. Directly from the definitions:

- (K1) `C_d ⊆ K_d` (in either description the generators of `C_d` satisfy
  `2e + i ≥ d`);
- (K2) `K_{d+1} ⊆ K_d`; `K_d · K_{d′} ⊆ K_{d+d′}`; `(1+x) K_d ⊆ K_{d+1}`;
  `x K_d ⊆ K_{d+2}`.

**Lemma K (cone membership without Lemma F).** Let `K` be a tree on `j ≥ 1`
vertices with vertex set `U`, and `ν` an integer weight on `U`, `ν ≥ 0`. Put
`Φ(K, ν) = det(I + x(L_K + diag ν))`. If `ν ≠ 0`, then `Φ(K, ν) ∈ K_j`.

*Proof.* Induction on `j`. For `j = 1`: `Φ = 1 + νx = (1+x) + (ν−1)x` with
`ν ≥ 1`, and `1+x, x ∈ K_1`. Let `j ≥ 2`. A tree with at least two vertices
has at least two leaves, so there is a leaf `w` with `ν` not supported on
`{w}` alone: the restriction `ν′` of `ν` to `U ∖ w` is not zero. Let `u` be
the neighbour of `w`, `N = I + x(L_K + diag ν)`, `A = Φ(K − w, ν′)` and
`Ψ = det N[U ∖ {w, u}]`. Expanding `det N` along the row of `w` (entries
`1 + (1+ν_w)x` on the diagonal and `−x` at `u`):
`det N = (1 + (1+ν_w)x) det N[U ∖ w] − x² Ψ`. The degree of `u` in `K − w` is
one less than in `K`, and no other degree changes, so
`N[U ∖ w] = I + x(L_{K−w} + diag ν′) + x e_u e_uᵀ` and, the determinant being
linear in row `u`, `det N[U ∖ w] = A + xΨ = Φ(K − w, ν′ + e_u)`. Therefore

`Φ(K, ν) = (1+x) A + xΨ + ν_w x Φ(K − w, ν′ + e_u)`.  (K3)

`A ∈ K_{j−1}` by induction (`ν′ ≠ 0`), so `(1+x)A ∈ K_j` by (K2).
`N[U ∖ {w, u}]` is block diagonal over the components `K′` of `K − w − u`,
with blocks `I + x(L_{K′} + diag(ν|_{K′} + e_{a′}))`, `a′` the neighbour of
`u` in `K′` (each component contains exactly one neighbour of `u`); each
block has a non-zero weight, so its determinant is in `K_{|K′|}` by
induction, the product `Ψ` is in `K_{j−2}` by (K2) (`Ψ = 1 ∈ K_0` if
`j = 2`), and `xΨ ∈ K_j`. Finally `Φ(K − w, ν′ + e_u) ∈ K_{j−1}` by
induction, and `x K_{j−1} ⊆ K_{j+1} ⊆ K_j`. ∎

## Lemma S24 (off-diagonal entries of the adjugate)

**Lemma S24.** Let `u, v ∈ V`, `P` the path from `u` to `v` in `T`,
`d = dist(u, v)`, `Q = V ∖ V(P)`. Then

`adj(M)_{uv} = x^d · Π_{uv}`,  `Π_{uv} := det M[Q] = Π_K Φ(K, e_{a_K})`,

the product over the components `K` of `T − V(P)`, where `a_K` is the unique
vertex of `K` adjacent to `P` (`Π_{uv} = 1` if `Q = ∅`). Consequently
`Π_{uv} ∈ C_{n−d−1} ⊆ K_{n−d−1}`.

*Proof.* Both sides are polynomials in `x`; it is enough to prove the
identity for real `x > 0`, where `M` and its principal submatrices are
positive definite. Since `T` is a tree, each component `K` of `T − V(P)` is
joined to `P` by exactly one edge (two edges would close a cycle); call its
end in `K` `a_K`. The degree in `T` of a vertex `w ∈ K` is its degree in `K`
plus `1` if `w = a_K`, so `M[Q]` is block diagonal with blocks
`I + x(L_K + diag e_{a_K})`: this is the product formula for `det M[Q]`.

Write `P = (p_0 = u, p_1, …, p_d = v)`. In `M[P, Q] M[Q]^{−1} M[Q, P]` the
entry `(p_i, p_j)` is `x² Σ_K [a_K ∼ p_i][a_K ∼ p_j] (M[K]^{−1})_{a_K a_K}`,
which vanishes for `i ≠ j` because `a_K` has only one neighbour on `P`. So
the Schur complement `S = M[P] − M[P, Q] M[Q]^{−1} M[Q, P]` differs from
`M[P]` only on the diagonal. Two vertices `p_i, p_j` of `P` are adjacent in
`T` only if `|i − j| = 1` (again because `T` has no cycle), so `S` is
tridiagonal with the entries `−x` next to the diagonal. By the Schur
complement formulas, `det M = det M[Q] · det S` and `(M^{−1})[P, P] = S^{−1}`.
The cofactor of `S` that gives `(S^{−1})_{0d}` is `(−1)^d` times the
determinant of `S` with row `d` and column `0` deleted; that matrix (rows
`0, …, d−1`, columns `1, …, d`) is lower triangular with `−x` on its
diagonal, so the cofactor is `(−1)^d (−x)^d = x^d`. Hence
`(M^{−1})_{uv} = x^d / det S` and `adj(M)_{uv} = det M · x^d / det S = x^d det M[Q]`.
(For `d = 0` this is the definition of the adjugate.)

Each factor `Φ(K, e_{a_K})` is in `K_{|K|}` by Lemma K, and the product is in
`K_{n−d−1}` by (K2); this is all that Propositions S25, S26 and Theorem T4
use. (The sharper statement: each factor is in `C_{|K|}` by Lemma F, and the
product is in `C_{n−d−1}` by the product rule for the cones `C_d` stated in
`gamma-reduction.md`, section "The cones `C_d`".) ∎

## Proposition S25 (the Wiener form)

**Proposition S25.** For every tree `T` of order `n ≥ 2`,

`n² ℓ_T(x) = 4 (W − n x) Φ(x) + Σ_{u<v} (t_u − t_v)² x^{dist(u,v)−1} Π_{uv}(x)`,

the sum over the unordered pairs of distinct vertices.

*Proof.* For a vertex `c` let `δ_c` be the vector of distances from `c`
(column `c` of `D`). For `v ≠ c` with `r = dist(c, v)`: `v` has one neighbour
at distance `r − 1` and `k_v − 1` at distance `r + 1`, so
`(Lδ_c)_v = k_v r − (r − 1) − (k_v − 1)(r + 1) = 2 − k_v`; and
`(Lδ_c)_c = −k_c`. Hence

`L δ_c = τ − 2e_c`,  and summing over `c`:  `L t = nτ − 2·1`.  (1)

Also `δ_cᵀ L δ_c = Σ_{ab ∈ E} (δ_c(a) − δ_c(b))² = n − 1`, and by (1)
`δ_cᵀ L δ_c = δ_cᵀτ − 2δ_c(c) = δ_cᵀτ`; so `δ_cᵀτ = n − 1` for every `c`, that
is `tᵀτ = n(n−1)`. With `1ᵀt = 2W` and (1):

`tᵀ L t = n tᵀτ − 2·1ᵀt = n²(n−1) − 4W`.  (2)

Take real `x > 0` and `G = M^{−1}`. `M1 = 1`, so `G1 = 1`; `G` is symmetric
and commutes with `L`; and `xLG = I − G`. By (1), `τ = (Lt + 2·1)/n`, so

`n² x τᵀGτ = x tᵀLGLt + 4x 1ᵀGLt + 4x 1ᵀG1`.

Here `1ᵀGLt = 1ᵀLt = 0`, `1ᵀG1 = n`, and
`x tᵀLGLt = tᵀ(I − G)Lt = tᵀLt − tᵀGLt = tᵀLt − (tᵀt − tᵀGt)/x`. With (2):

`n² x τᵀGτ = n²(n−1) − 4W − (tᵀt − tᵀGt)/x + 4nx`.

By L1, `ℓ_T/Φ = (n−1) − x τᵀGτ`, hence

`n² ℓ_T/Φ = 4W − 4nx + (tᵀt − tᵀGt)/x`.

Since `G` is symmetric with row sums `1`,
`tᵀt − tᵀGt = ½ Σ_{u,v} G_{uv}(t_u − t_v)² = Σ_{u<v} G_{uv}(t_u − t_v)²`.
Multiplying by `Φ` and using `ΦG_{uv} = adj_{uv} = x^{dist(u,v)} Π_{uv}`
(Lemma S24) gives the identity for every `x > 0`, hence as polynomials. ∎

**Remarks.** (1) The only term with a negative coefficient is `−4nxΦ`.
(2) For an edge `uv` whose removal leaves components of orders `n_e` and
`n − n_e`, `(t_u − t_v)² = (n − 2n_e)²`, and `W = Σ_e n_e(n − n_e)`; the
constant terms give `4W + Σ_e (n − 2n_e)² = n²(n−1)`. (3) For the star:
`W = (n−1)²`, `Φ = (1+x)^{n−2}(1+nx)`, the only pairs with `t_u ≠ t_v` are
the `n − 1` edges, with `Π = (1+x)^{n−2}`, and the formula gives
`ℓ = (1+x)^{n−2}[(n−1) + 4(n−2)x − 4x²]`.

## Proposition S26 (`Φ_T` is in the cone)

**Proposition S26.** For every tree `T` of order `n ≥ 1`,
`Φ_T = det(I + xL) ∈ K_{n−1}`, and `Φ_T(0) = 1`.

*Proof.* Induction on `n`; `Φ = 1 ∈ K_0` for `n = 1`. Let `n ≥ 2`, `w` a leaf
with neighbour `u`, `T′ = T − w`. The expansion in the proof of Lemma F with
`ν = 0` reads `Φ_T = (1+x) det M[V∖w] − x²Ψ`, `Ψ = det M[V∖{w,u}]`, and
`M[V∖w] = (I + xL_{T′}) + x e_u e_uᵀ`, so `det M[V∖w] = Φ_{T′} + xΨ` (the
determinant is linear in row `u`). Hence `Φ_T = (1+x)Φ_{T′} + xΨ`. `Ψ` is the
polynomial `Π_{uu}` of Lemma S24 for the tree `T′` (the case `d = 0`), so
`Ψ ∈ K_{n−2}`. By induction and (K2), `(1+x)Φ_{T′} ∈ K_{n−1}` and
`xΨ ∈ K_n ⊆ K_{n−1}`. ∎

## Theorem T4 (the peak is at least `⌊(n−1)/2⌋`)

For an integer `μ ≥ 1` and a polynomial `f` put
`λ_μ(f) = [x^μ] f − [x^{μ−1}] f`. Binomial coefficients `C(i, k)` are `0` for
`k < 0` or `k > i`.

**Lemma A.** Let `μ ≥ 1`, `g = x^e(1+x)^i`, `a = μ − e`.

(a) If `2e + i ≥ 2μ − 1`, then `λ_μ(g) ≥ 0`.

(b) If `2e + i ≥ 2μ` and `W, n` are positive reals with `W ≥ 3n`, then
`λ_μ((W − nx) g) ≥ 0`, with strict inequality if `a ≥ 1`.

*Proof.* `[x^μ] g = C(i, a)`, `[x^{μ−1}] g = [x^μ](xg) = C(i, a−1)`,
`[x^{μ−1}](xg) = C(i, a−2)`.

(a) If `a ≤ 0`, `λ_μ(g) = C(i, a) ≥ 0`. If `a ≥ 1`, then `i ≥ 2a − 1 ≥ a`, so
`C(i, a) = C(i, a−1)(i − a + 1)/a` and
`λ_μ(g) = C(i, a−1)(i − 2a + 1)/a ≥ 0`.

(b) `λ_μ((W − nx)g) = W[C(i, a) − C(i, a−1)] − n[C(i, a−1) − C(i, a−2)]`. If
`a ≤ 0` this is `W C(i, a) ≥ 0`. Let `a ≥ 1`; then `i ≥ 2a`, `C(i, a−1) > 0`,
`C(i, a) = C(i, a−1)(i − a + 1)/a` and
`C(i, a−2) = C(i, a−1)(a − 1)/(i − a + 2)` (also for `a = 1`). With
`s = i − 2a + 1 ≥ 1`, so that `i − a + 2 = a + s + 1`:

`λ_μ((W − nx)g) = C(i, a−1) [W s/a − n(s + 2)/(a + s + 1)] = C(i, a−1) [W s(a + s + 1) − n a(s + 2)] / (a(a + s + 1))`.

Since `W ≥ 3n`: `W s(a+s+1) ≥ 3n s(a+s+1) = n(3sa + 3s² + 3s) > n(sa + 2a)`,
because `2sa ≥ 2a` and `3s² + 3s > 0`. ∎

**Theorem T4.** Let `T` be a tree of order `n ≥ 3` and `μ = ⌊(n−1)/2⌋`. Then
`d_{μ−1}(T) < d_μ(T)`. Consequently every index at which `d_0, …, d_{n−2}`
attains its maximum is at least `⌊(n−1)/2⌋`.

*Proof.* `1 ≤ μ ≤ n − 2`, so `d_μ − d_{μ−1} = λ_μ(ℓ_T)`.

*Orders 3 and 4* (`μ = 1`). By L2 (`lemmas.md`), `d_0 = n − 1` and
`d_1 = 2n² − 6 − Σ_v k_v²`. For `n = 3`: `d_1 = 6 > 2`. For `n = 4`:
`Σ k_v² ≤ 12`, so `d_1 ≥ 14 > 3`.

*Orders `n ≥ 5`.* `W = Σ_e n_e(n − n_e) ≥ (n−1)(n−1) ≥ 3n` (each of the
`n − 1` edges separates `n_e ≥ 1` vertices from `n − n_e ≥ 1`, and
`n_e(n − n_e) ≥ n − 1`; `(n−1)² ≥ 3n` for `n ≥ 5`). Note `2μ ≤ n − 1` and
`2μ − 1 ≤ n − 2`. By Proposition S25 and linearity of `λ_μ`,

`n² (d_μ − d_{μ−1}) = 4 λ_μ((W − nx)Φ) + Σ_{u<v} (t_u − t_v)² λ_μ(x^{d−1} Π_{uv})`,  `d = dist(u, v)`.

*The pair terms are non-negative.* `Π_{uv} ∈ K_{n−d−1}` (Lemma S24), so
`x^{d−1}Π_{uv}` is a non-negative combination of polynomials
`x^{e+d−1}(1+x)^i` with `2e + i ≥ n − d − 1`, for which
`2(e + d − 1) + i ≥ n + d − 3 ≥ n − 2 ≥ 2μ − 1`. Lemma A(a) applies to each.

*The main term is positive.* By Proposition S26 and (K2),
`Φ ∈ K_{n−1} ⊆ K_{2μ}`: `Φ = Σ_g c_g g` with `c_g ≥ 0` and `g = x^e(1+x)^i`,
`2e + i ≥ 2μ`. By Lemma A(b), `λ_μ((W − nx)g) ≥ 0` for each `g`. Since
`Φ(0) = 1`, some `g` with `e = 0` has `c_g > 0`; for it `a = μ ≥ 1`, and the
inequality is strict. So `λ_μ((W − nx)Φ) > 0`.

Hence `d_μ − d_{μ−1} > 0`. The last sentence of the theorem is R1, the
sequence being positive and log-concave. ∎

**Corollary (odd order).** For every tree of odd order `n ≥ 3`, every
maximizing index of the normalized coefficients is at least `⌊n/2⌋`: the
lower bound of Conjecture 1.2 of arXiv:1507.02341 holds for trees of odd
order, in the strong reading of ties. (For odd `n`, `⌊(n−1)/2⌋ = ⌊n/2⌋`.)

**What is not proved.** For even `n = 2m` the theorem gives `d_{m−2} < d_{m−1}`
(peak at least `m − 1`); the conjecture asks for `d_{m−1} < d_m`. The same
decomposition with `λ_m` gives, for even `n ≥ 6`,

`n² (d_m − d_{m−1}) ≥ λ_m( 4(W − nx)Φ + Σ_{e = uv ∈ E} (n − 2n_e)² Π_{uv} )`,  (3)

because for `d ≥ 2` the pair terms are in `K_{n+d−3} ⊆ K_{n−1} = K_{2m−1}`
and Lemma A(a) applies. The edge polynomials `Π_{uv}` are only in `K_{n−2}`,
on which `λ_m` can be negative (`λ_m((1+x)^{n−2}) < 0`), and for the star the
right side of (3) is the whole of `n²(d_m − d_{m−1})`. Whether the right side
of (3) is positive for every tree of even order is open; see
[`leaf-telescoping.md`](leaf-telescoping.md) for a conjecture that implies
it. The upper bound `⌈n − n/√5⌉` is not touched by this argument.

## Prior literature (audit of session 10; originality not established)

Recorded in the dossier, section "Audit for session 10". In short, and with
the limits stated there (one bounded search; several sources seen only
through machine summaries; the two bridging steps below were written by the
auditor and are not independently reviewed):

- The first equality of **Lemma S24** is a known consequence of the path
  expansion of a cofactor (Maybee, Olesky, van den Driessche, Wiener, SIAM J.
  Matrix Anal. Appl. 10 (1989) 500–519, read only as quoted in
  Chebotarev–Shamis, arXiv:math/0602575, eq. (4)): in a tree there is one
  path from `u` to `v`. It is not a result of the project.
- **Identity (1)** (`Lt = nτ − 2·1`) follows from the Graham–Lovász formula
  for `D^{−1}` (Adv. Math. 29 (1978), Lemma 1) on multiplying by `D`. It is
  not a result of the project.
- **Proposition S25** and **Theorem T4**: no source found within that
  coverage. This is not a claim of novelty.

## Verification by computation

`experiments/CJ-0001-collins-shor-peak/wiener_form.py` (exact integers),
result file `results/wiener-form.json`. For every tree of order 2 to the
bound in the result file: Proposition S25 with `ℓ_T` taken from the
characteristic polynomial of the distance matrix (python-flint), not from
L1; Lemma S24 entry by entry (the adjugate from Faddeev–LeVerrier against
the product over the components off the path); the cone memberships of
`Φ` and `Π_{uv}`; the sign of every pair term and of the main term in the
proof of T4; the decomposition of `n²(d_μ − d_{μ−1})`; `W ≥ (n−1)²`. The
inequality `d_{μ−1} < d_μ` alone is also checked from the distance matrix for
larger orders. The counts are in the result file and in the journal entry of
session 9. These checks support the identities on the range computed; the
theorem rests on the written proof.
