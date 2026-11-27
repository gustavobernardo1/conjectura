# CJ-0001 — Collins–Shor conjecture — investigation state

Last updated: 2026-11-27 (session 12). This file is the current truth about the
investigation and is meant to be sufficient, on its own, for a new agent to
continue. It was compacted in sessions 5, 8 and 9: details are in the notes it
links. **Session 9:** [`notes/wiener-form.md`](notes/wiener-form.md) (S24 to
S26, Theorem T4: the lower bound for odd order; revised once in session 10,
with Lemma K) and
[`notes/leaf-telescoping.md`](notes/leaf-telescoping.md) (S23, S27, statement
(SM)). **Session 10:** [`notes/even-order.md`](notes/even-order.md) (S28 to
S31, statement (SM⁺): the even orders reduced to one polynomial `Ω_T`).
**Session 11:** [`notes/lower-bound.md`](notes/lower-bound.md) (S32 to S36,
Theorems T5 and T6: statement (Γ_c¹), star minimality (SM) and **the lower
bound `⌊n/2⌋` for every tree** — a candidate proof; contraction of an edge);
Collins (1986) and Collins (1989) read (dossier, last section).
**Session 12:** [`notes/path-maximality.md`](notes/path-maximality.md) (S37 to
S39, Theorems T7 and T8: the generalized tree shift lowers `ℓ` in the cone
order, and the path is the coefficientwise maximum — a candidate proof;
statements (PM) and (PX-peak) on the location of the peak, open).
Proofs: [`notes/lemmas.md`](notes/lemmas.md) (R1, L1 to L3),
[`notes/double-stars.md`](notes/double-stars.md) (T1),
[`notes/spine3.md`](notes/spine3.md) (T2),
[`notes/diameter4-caterpillars.md`](notes/diameter4-caterpillars.md) (T3),
[`notes/vertex-principle.md`](notes/vertex-principle.md) (L4, Hypothesis V),
[`notes/skeleton-identity.md`](notes/skeleton-identity.md) (S1 to S4,
Property Γ), [`notes/skeleton-locality.md`](notes/skeleton-locality.md) (S6 to
S10, Lemma C), [`notes/gamma-reduction.md`](notes/gamma-reduction.md) (Lemma F,
S11), [`notes/gamma-components.md`](notes/gamma-components.md) (S12 to S18,
Lemma G), [`notes/rooted-calculus.md`](notes/rooted-calculus.md) (S19 to S22,
statement (Λ)). Failed approaches in detail:
[`notes/dead-ends.md`](notes/dead-ends.md). Obligations in detail:
[`notes/obligations.md`](notes/obligations.md). Computations:
[`experiments/CJ-0001-collins-shor-peak/`](../../../experiments/CJ-0001-collins-shor-peak/README.md).
Literature: the dossier
[`research/candidates/CJ-0001-collins-shor-peak.md`](../../candidates/CJ-0001-collins-shor-peak.md).

## Exact statement

Source: Conjecture 1.2 of Aalipour, Abiad, Berikkyzy, Hogben, Kenter, Lin, Tait,
arXiv:1507.02341 (journal version: Electron. J. Linear Algebra 34:373–380,
2018, according to the reference lists of arXiv:2206.07561 and
arXiv:2407.03309; not checked against the journal), read in the paper's TeX
source on 2026-11-26. Verbatim:

> The [normalized] coefficients of the distance characteristic polynomial for
> any tree `T` with `n` vertices are unimodal with peak between `⌊n/2⌋` and
> `⌈n − n/√5⌉`.

It originates as Conjecture 9 of K. L. Collins, Discrete Appl. Math. 25 (1989)
27–35, attributed there to Peter Shor. Read in session 11; verbatim: "The
coefficients of CPD(T) for any tree T with n vertices are unimodal with peak
between `½n` and `n(1 − 1/√5)`" — no floor, no ceiling. For odd `n` the
literal bound `½n` would contradict Theorem 1 of the same paper (the star
peaks at `½(n−1)`), so the floor is the only consistent reading (dossier).

## Definitions and conventions

- `T`: a tree of order `n ≥ 3`. `D`: its distance matrix. `δ_k`: the coefficient
  of `x^k` in `det(D − xI)`.
- Normalized coefficients: `d_k = 2^{k−(n−2)} |δ_k|`, `0 ≤ k ≤ n−2`. They are
  positive. The code works with the integers `s_k = 2^k |δ_k| = 2^{n−2} d_k`.
- `m = ⌊n/2⌋`, `M = ⌈n − n/√5⌉ = n − ⌊n/√5⌋` (computed exactly as
  `n − isqrt(n² // 5)`).
- **Tie convention.** The source does not say how a tie between two maximal
  coefficients is to be read. The project tests the strong reading: *every*
  maximizing index lies in `[m, M]`. Ties are counted and reported.
- `ρ_k(T) = d_{k+1}(T)/d_k(T)`; `q(T) = d_{m−1}(T)/d_m(T) = 1/ρ_{m−1}(T)`.
- `S_n`: star. `P_n`: path. `S(a,b)`: double star, two adjacent centres with
  `a` and `b` leaves (`n = a + b + 2`).
- Skeleton notation (`S`, `A`, `B = V ∖ A`, `r_A`, `Φ_B`, the cones `C_d`):
  `notes/skeleton-locality.md`. Weighted trees `(T, ν)`, `R(T, ν)`:
  `notes/gamma-components.md`. Rooted state `(Ψ, H, G, Ω, R)`, `F`, `Λ`:
  `notes/rooted-calculus.md`.

Unimodality and log-concavity of `d_0, …, d_{n−2}` are a theorem (Theorem 2.1
of the source). Only the location of the peak is open.

## Status

Mathematical: `active-investigation`. Formal: `partial`. Novelty:
`preliminary-search-completed`. External review: `not-reviewed`.

Nothing in this file is an established result of the project. Every statement
below marked "reviewed" had one AI review of one revision by a fresh context
(named in the registry); none has been read by a mathematician, and
originality is not established for any of them. T1, T2, T3 are **candidate
theorems** (director's decision of 2026-11-26), and so is **T4** (session 9:
`d_{μ−1} < d_μ`, `μ = ⌊(n−1)/2⌋`, for every tree — the conjectured lower
bound for odd order, one less for even order), and so are **T5 and T6**
(session 11: `d_{m−1} < d_m`, `m = ⌊n/2⌋`, for every tree — the conjectured
lower bound for every order; its reviews are listed in obligation 11), and so are **T7 and T8**
(session 12: the path is the coefficientwise maximum; obligation 12). The
status of every registered contribution is in
[`research/discoveries.json`](../../discoveries.json), not here.

Formal (Lean, `formalization/Conjectura/Research/CollinsShorPeak/`): 21 registered theorems for this problem; the latest receipt is under `verification/receipts/`. **Session 10** (`WienerCone.lean`): the cones `K_d` (`WienerCone`) with (K1), (K2), and Lemma A of `wiener-form.md` on the cone, strict part included — nothing about trees, `Φ`, S24 to S26 or T4. In Lean before that: the general form of R1; the discrete core of L4, since session 8 **in any finite number of variables** (`vertex_principle_discrete`: a function on integer points with the exchange inequality `f(c+e_i−e_k) + f(c+e_k−e_i) ≤ 2f(c)` on the slice is, at every point of the slice, at least its value at some vertex `λ + (S−Σλ)e_p`); the cone `C_d` over real polynomials (`HalfGammaCone`) with `C_d·C_e ⊆ C_{d+e}`, `x·C_d ⊆ C_{d+1}`, `x·C_d ⊆ C_{d+2}`, `(1+x)·C_d ⊆ C_{d+1}`, `x(1+x)·C_d ⊆ C_{d+3}`, and Lemma C. **Not formalized:** the step from a multi-affine polynomial with non-negative mixed partials to the exchange inequality (so L4 as written is not formalized); the equality of the inductive cone with the explicit non-negative sums; anything about trees, determinants or `r_A`. The Lean statements were compared with the written ones by the formalizing agent and the author of the session only.

## Established results

"Level" says what kind of evidence exists; "reviewed" always means an AI
review of one revision, named in the registry.

| ID | Statement | Level |
| --- | --- | --- |
| E1, E2 | The conjecture (every maximizing index in `[m, M]`) holds for all trees of order 3 to 23: 23,942,357 trees, 0 violations. Orders 21 to 23 are beyond the published range. | Exact computation; orders 21 to 23 by one implementation, without a provenance block (obligation 4). |
| E3, E4 | In those orders: one tie (order 13, indices 6 and 7); the peak is always `⌊n/2⌋` or `⌊n/2⌋ + 1`; the star attains the minimum, the path the maximum. | Exact computation. |
| R1 | Lower bound ⇔ `d_{m−1} < d_m`; upper bound ⇔ `M ≥ n−2` or `d_{M+1} < d_M`. General form: for a positive log-concave sequence, every maximizing index is `≥ j` iff `a_{j−1} < a_j`. | Proved; general form reviewed twice and **formalized in Lean**. |
| L1, L2, L3 | The Laplacian formula for `ℓ_T`; `d_1 = 2n² − 6 − Σ deg²`; the quotient-matrix formula for caterpillars. | **Known** (Graham–Lovász 1978; the source; Hogben–Reinhart). Tools. |
| T1 | Double star `S(a,b)`, `a, b ≥ 1`: `m` is the only maximizing index. | Candidate proof, reviewed. Its closed formula is **in print** (Xue–Liu–Jia 2016, Lemma 2.3; do Nascimento 2018, Prop. 3.2.1). No peak statement found. |
| T2 | Caterpillar `K(a,b,c)`, `a, b, c ≥ 1`: `m` is the only maximizing index. | Candidate proof (two computer-assisted identities), reviewed. Balanced case of its formula: do Nascimento 2018, Prop. 3.2.9. |
| T3 | Caterpillar `K(a,0,c)`, `a, c ≥ 1`, `a + c ≥ 3`: `m` is the only maximizing index. With T2 and `P_5`: every caterpillar of diameter 4. | Candidate proof, reviewed. Its formula: do Nascimento 2018, Prop. 3.2.6. |
| L4 | Vertex principle: a function of degree ≤ 1 in each variable with non-negative mixed second partials attains its minimum over the integer points of a slice `c ≥ λ`, `Σ c = S` at a point with at most one coordinate above its lower bound. | Proved; reviewed (`9499572`). Lean: see Status. |
| S1 to S4 | Skeleton `S` with `c_v ≥ 0` leaves at `v`, `n ≥ 2s`: `d_k = Σ_j g_j(c) C(n−2s, k−j)`, `g_j` of degree ≤ 1 in each `c_v` (S1); the expansion of `det(2xI − Q(c))` over subsets `A` (S2); `r_V = s(1+x) + 3x` (S3); if `r_A` has a non-negative half-gamma expansion, the coefficient of `c^A` in `d_m − d_{m−1}` is `≥ 0` for every `n ≥ 2s` (S4). | Proved; reviewed (`1bb2bbe`). |
| S5 | Conditional on Property Γ for `S`: Hypothesis V for `S` and, by L4, `d_m − d_{m−1} ≥ min_p D_n((n−s)e_p)` for every `S(c)` of order `n ≥ 2s`. | Proved; reviewed (`9499572`). No positivity by itself. |
| Γ, finite | Property Γ holds for the 47 trees with 2 to 8 vertices; hence (S4) Hypothesis V for those skeletons and every order `n ≥ 2s`. | Computer-assisted; reviewed with an independent recomputation (`9499572`). |
| S6 to S10, C | `r_A` depends only on `s` and `L[Ā, Ā]` (two Laplacian forms, S6, S7); closed forms for `|Ā| ≤ 2` (S8, S9); the cone `C_d` lies in the half-gamma cone (Lemma C); **Γ holds for every tree and every `A` with independent complement** (S10). | Proved; reviewed (`1805bca`). |
| F, F′, S11 | `det(I + x(L_T + diag ν)) ∈ C_j` for integer `ν ≥ 0`, `ν ≠ 0`; contracting the components of `S[A]`: Γ⁺ (Γ with `|A| ≥ 1`) for all trees follows from its case `A` independent. | Proved; reviewed (`5622d19`, recheck of `7acd425`). |
| S12, S13 | `r_A = r_V Φ_B − pᵀ adj(I + xL_B) p`; degree `t + 1`, leading coefficient `κ det L_B`, `κ = s + 3 − τ_BᵀL_B^{−1}τ_B ≥ 4` (equality iff `a = 1`; `κ = 4 + 2/(1ᵀP_A^{−1}1)`); **all roots of `r_A` are real and negative**. | Proved; reviewed (`b0a4dbe`). **Known consequences of prior literature:** `κ ≥ 4` with its equality case and the identity with `P_A` (Richman–Shokrieh–Wu, arXiv:2411.11488; bridging step unreviewed); `L_B` positive definite (standard). **Potentially original** (no source found within the session-8 coverage; originality not established): the form S12, the degree and leading coefficient, the real roots. Item by item: MD-0013, `limitations`. |
| S14 to S18, G | Component form `r_A = [(1+4x) + e_A(1+x)]Φ_B + Σ_i R(T_i, ν) Π_{l≠i} Φ(T_l, ν)`, so Γ⁺ follows from **Γ_c** (`R(T, ν) ∈ C_{j+1}`, `ν ≠ 0`); the adjugate when a leaf is removed or a weight raised (Lemma G); recurrences for `R` (S15 to S17); Γ_c follows from statement **(E)** by induction on a leaf (S18). | Proved (S18 conditional); reviewed (`b0a4dbe`). |
| S19, S20 | Rooted state `(Ψ, H, G, Ω, R)` of `(T, ν, u)`: `ΨR = Φ[ν_u(1+x)Ψ + Ω] − π_u²` (★); rules for raising the root weight, a new root, and merging two rooted trees — in the merge the only negative term of `R` is `−2G_1G_2`, and `G = (1+2x)Ψ − π_u` has non-negative coefficients; the increment of `R` at any vertex, `Δ_u = [(1+2x)² + 2xν_u]Ψ + Σ_c Λ(T_c, ν, c)P_c`; at a new leaf, `E = (1+2x)²Φ(T, ν+e_u) + Λ = xR(T, ν+e_u) + F`. | Proved; reviewed (`59c47f7`), no gap found. |
| S21 | **(E″) and (S) of session 7 are false.** On the star with centre `u` of weight `n_0` and leaf weights `n_i`: `[x^{q+3}]F = Π(1+n_i)(4 + n_0 − Σ n_i/(1+n_i))`. Smallest failures found: (E″) at 6 vertices (five leaves of weight 4), (S) at 5 vertices (leaf weights 2, 3, 4, 4). | Proved (leading coefficients) and exact computation with an independent checker; reviewed (`59c47f7`), counterexamples confirmed by the reviewer's own code. |
| S22 | If **(Λ)** (`Λ(T, ν, u) ∈ C_{j+2}` for every rooted weighted tree, `ν ≥ 0` arbitrary) holds, then `R` is non-decreasing in every weight at every vertex in the cone order; in particular (E) for every leaf, Γ_c, Γ⁺ and Γ. | Proved (conditional); reviewed (`59c47f7`), no gap found. |
| S24, S25, S26 | For every tree: `adj(I+xL)_{uv} = x^{dist(u,v)} Π_{uv}`, `Π_{uv} = det (I+xL)[V ∖ path(u,v)] ∈ C_{n−d−1}` (S24); **the Wiener form** `n² ℓ_T = 4(W − nx)Φ + Σ_{u<v} (t_u − t_v)² x^{dist(u,v)−1} Π_{uv}`, `t = D1`, `W` the Wiener index, `Φ = det(I+xL)` (S25); `Φ ∈ K_{n−1}` (S26). `K_d`: non-negative combinations of `x^e(1+x)^i`, `2e + i ≥ d`. | Proved; reviewed (`b5d9294`), no gap found. Exact on all trees of order ≤ 12 (`results/wiener-form.json`). |
| **T4** | **For every tree of order `n ≥ 3`: `d_{μ−1} < d_μ`, `μ = ⌊(n−1)/2⌋`; every maximizing index is `≥ ⌊(n−1)/2⌋`. For odd `n` this is the lower bound `⌊n/2⌋` of the conjecture; for even `n` it is one less.** Proof: in S25 the pair terms are in `K_{n−2}`, where `[x^μ] − [x^{μ−1}] ≥ 0`, and `(W − nx)Φ` is handled with `W ≥ (n−1)² ≥ 3n`. | Candidate proof; **two AI reviews, no gap found**: `b5d9294`, and a complete audit of the revised note at `a3e5179` (every step and L1, L2, R1 re-proved by hand; five defects of citation and wording, obligation 9). Since `a3e5179` the proof needs neither Lemma F nor Lemma C (Lemma K). Lean: Lemma A and the cones only. Checked on all trees of order ≤ 19. Literature (session 10): S24 and `Lt = nτ − 2·1` are **known**; no source found for S25 or T4 within a thin coverage. |
| S28, S29, S30 | **Rooted form** (S28): for any root `c`, `ℓ_T = Σ_e Π_e + 4 Σ_{v≠c} δ_v x^{δ_v} Π_{cv} − 4xΨ_c + Σ_{dist ≥ 2} (δ_u − δ_v)² x^{dist−1} Π_{uv}`. **Leaf polynomial** (S29): an explicit formula with non-negative coefficients for `r_c(T) = ℓ_{T+leaf at c} − (1+x)ℓ_T`. **Remainder** (S30): `ℓ_T = (1+4x)Θ_T − 4x(1+x)^{n−1} + Ω_T`, `xΘ_T = Φ − (1+x)^{n−1}`; `Ω_T ≥ 0` coefficientwise, `= Σ_k (1+x)^{n−1−k} Ω_{u_k}(T_k)` for every construction, in `K_{n−1}` up to its deep-edge terms; **for even `n = 2m ≥ 4`: `d_m − d_{m−1} ≥ (n−1)(3m−5)/(m+1)·Cat_{m−1} + λ_m(Ω_T)`**, equality for the star. | Proved; **not reviewed**. Exact on all rooted trees of order ≤ 9 (S28, S29) and all trees of order ≤ 15 (`results/even-order.json`). |
| S31 | The right side of inequality (3) of `wiener-form.md` (the Wiener form without the pairs at distance ≥ 2) is **negative** for the spider with 49 legs of length 2 and one pendant vertex (`n = 100`), positive for that family up to `n = 98` and for all trees of even order ≤ 14. The conjectured inequality holds on those trees. | Exact computation, two implementations. Not reviewed. |
| S23 | `R(T, 0) = xℓ_T − (1+4x)Φ_T`; **leaf recursion** `ℓ_{T+leaf at u} = (1+x)ℓ_T + r_u(T)`, `r_u = (1+4x)Ψ_u + Ω_u` (the polynomial `r_{{u}}`); telescoped: `ℓ_T = −4x(1+x)^{n−1} + Σ_k (1+x)^{n−1−k} r_{u_k}(T_k)` along any construction leaf by leaf; `ℓ_{S_n} = (1+x)^{n−2}[(n−1) + 4(n−2)x − 4x²]`. | Proved; (d) checked by the reviewer of `b5d9294`; (a) to (c): see obligation 11. Exact on all rooted trees of order ≤ 11. **Literature (session 11):** (d) is **known** (Collins 1989, Theorem 1); a leaf recursion in terms of minors of `D − λI` is Theorem 4 of Collins's thesis (1986) — a precursor to be cited; the form with `1 + x`, the Laplacian remainder and its positivity are not there. |
| S32 to S35, **T5** | For a rooted tree `(A, u)` of order `a`, weight zero, `δ` the distances from `u`, `a_v = x^{δ_v−1}Π_{uv}`: `H = Σ a_v`, `G = xΣ(δ_v−1)a_v`, `R(A, e_u) = Q¹ + x²Σδ_v²a_v` with `Q¹ ∈ K_a` (S33); `E := R − Ω + (1+2x)²Ψ − 2xG = R(A, e_u) − (1+x)(Ω + xH)`, with the plant rule `E^ = x[E + Ω + 2G + x(3+2x)H]` and the merge rule `E = E_1Ψ_2 + E_2Ψ_1 + x(H_1Ω_2 + H_2Ω_1) − 2G_1G_2` (S34); for two planted trees the last two terms equal `x(Ψ_1R¹_2 + Ψ_2R¹_1) + x²(H_1Q¹_2 + H_2Q¹_1) + x⁴Σ(δ_v − δ_{v′})²a_va_{v′}` (S35). **T5: `Ω ∈ K_a`, `E ∈ K_{a+1}`, `R(A, e_u) ∈ C_{a+1}` for every rooted tree — statement (Γ_c¹).** | Candidate proof (induction on rooted trees); reviews: obligation 11. Exact on all rooted trees of order ≤ 9 and (Γ_c¹) to order 11. |
| **T6** | **For every tree: `r_u(T) − (1+4x)(1+x)^{n−1} ∈ K_n`; (SM) `ℓ_T − ℓ_{S_n} ∈ C_{n−1}` (so `d_k(T) ≥ d_k(S_n)` for every `k`); and for `n ≥ 3`, `m = ⌊n/2⌋`: `d_m − d_{m−1} ≥` that of the star `> 0` — every maximizing index is `≥ ⌊n/2⌋`, the lower half of the conjecture.** Uses T5, S23(c), Lemma A, R1. | Candidate proof; reviews: obligation 11. (SM) exact on all trees of order ≤ 20; the conjecture itself on orders ≤ 23 (E1, E2). |
| S36 | **Contraction.** `uv` a non-pendant edge, `(A, u)`, `(B, v)` the two sides, `T′` = `A` and `B` glued at `u = v` plus a pendant vertex there: `ℓ_T − ℓ_{T′} = H_AE_B + H_BE_A + x(2+5x)H_AH_B + 2G_AG_B/x ∈ C_{n−1}`; so every `d_k` and `d_m − d_{m−1}` decrease (weakly) under the operation. A second proof of (SM). | Candidate proof; reviews: obligation 11. Formula exact on 1,064 pairs; membership on all trees of order 4 to 16 and all non-pendant edges (220,181). |
| S37 to S39, **T7, T8** | **Generalized tree shift** (`A`, `B` joined by a path of length `k` → glued, with a pendant path of length `k`; `a, b ≥ 2`): `ℓ_{T_k} − ℓ_{T′_k}` has an explicit formula (S37: four terms, coefficients built from the tridiagonal determinants `a_j`) and lies in `C_{n−1}` (T7). Every tree but the path is the result of a shift that removes one leaf (S39). **T8: `ℓ_{P_n} − ℓ_T ∈ C_{n−1}` for every tree** — with T6(b), `d_k(S_n) ≤ d_k(T) ≤ d_k(P_n)` for every `k`, and the increments `d_μ − d_{μ−1}` ordered the same way for `μ ≤ ⌊n/2⌋`; equality with the path only for the path. **Coefficientwise only: nothing about the peak index.** | Candidate proof (session 12); one AI review of `8b03309`, no gap found (`claude-opus-5-5`, the author's model; independent by context only); S37 uses a finite exact identity (sympy). Exact: `results/tree-shift.json` (T7 on all shifts of order ≤ 15, T8 on all trees of order ≤ 17). |
| S27 | (SM) implies `d_m − d_{m−1} ≥` that of the star `> 0`, `m = ⌊n/2⌋`, for every tree; `Φ(B, e_c) − (1+x)^j ∈ C_j`; (Γ_c¹) ⇒ `r_u(T) − (1+4x)(1+x)^{n−1} ∈ C_n` ⇒ (SM). | Proved (conditional); (a), (b) and the algebra of (c) checked by the reviewer of `b5d9294`, which is not a review of the note. |

### Global identifiers

Statuses are in the registry and in [`research/INDEX.md`](../../INDEX.md).

| Local | Global | Type |
| --- | --- | --- |
| E2 (with E1, E3) | MD-0001 | computational finding |
| L1 | MD-0002 | identity (rediscovered) |
| L3 | MD-0003 | lemma (rediscovered) |
| Refutation of A(i) | MD-0004 | counterexample |
| A(ii) | MD-0005 | conjecture |
| T1, T2, T3 | MD-0006, MD-0007, MD-0008 | theorems (candidates) |
| Hypothesis V | MD-0009 | conjecture |
| Conjecture Γ | MD-0010 | conjecture |
| S6 to S10, Lemma C | MD-0011 | theorem (candidate) |
| Lemma F, F′, S11 | MD-0012 | structural result (candidate) |
| S12, S13 | MD-0013 | structural result (candidate) |
| S14, Lemma G, S15 to S18 | MD-0014 | structural result (candidate) |
| (★), S19 to S22, refutation of (E″) and (S) | MD-0015 | structural result (candidate) |
| S24 to S26, T4 | MD-0016 | theorem (candidate) |
| (SM), with S23 and S27 as evidence; (SM⁺) | MD-0017 | conjecture |
| S28 to S30, with S31 | MD-0018 | structural result (candidate) |
| T5, T6, S36 (with S32 to S35) | MD-0019 | theorem (candidate) |
| S37 to S39, T7, T8 | MD-0020 | theorem (candidate) |
| (PM), (PX-peak) | MD-0021 | conjecture |

Not registered: R1, L2, L4 and S1 to S4 are tools or steps (S3 and S4 are the
evidence of MD-0010); Γ⁺ is an observation on the 47 small trees, recorded
under MD-0012; Γ_c and (E) are stated in MD-0014, and (Λ) in MD-0015, and are
not registered as conjectures of their own; E1 reproduces a published
verification; Q1, Q2 are questions.

## Conjectures and hypotheses of this investigation

**Statement (SM), star minimality (MD-0017, session 9) — candidate proof
since session 11 (Theorem T6(b), MD-0019).** For every tree of order
`n ≥ 3`: `ℓ_T − ℓ_{S_n} ∈ C_{n−1}`. Exact for all 1,346,023 trees of order 3
to 20 (equality only for the star). It implies the lower bound `⌊n/2⌋` for
**every** tree, and it follows from **(Γ_c¹)**: `R(B, e_c) ∈ C_{j+1}` for
every rooted tree, which is Theorem T5. **(SM⁺)** (session 10): `Ω_T ∈ C_{n−1}`
for every tree; it follows from T5(i) and the formula of S30 (unreviewed).
**(CM)** (session 11): the same cone order is respected by the contraction
of any non-pendant edge (S36). Still open, and no longer needed for the
lower half: Γ_c for general weights, (E), (Λ), Conjecture Γ.

**Three kinds of extremality** (session 12; `path-maximality.md`, last
sections). (1) *Coefficientwise*: `d_k(S_n) ≤ d_k(T) ≤ d_k(P_n)` — T6(b) and
T8, candidate proofs. (2) *Increments below the middle*: the same order for
`d_μ − d_{μ−1}`, `μ ≤ ⌊n/2⌋`; the cone reaches no further. (3) *Peak
location*: the star is peak-minimal (every tree has `p_min ≥ ⌊n/2⌋ = p_max(S_n)`;
this is T6(c), the lower half); whether the path is peak-maximal is open,
and (1) does not imply it (termwise domination does not order maximizing
indices).

**(PX-peak) and (PM) — open (MD-0021, session 12).** (PX-peak):
`p_max(T) ≤ p_max(P_n)` for every tree. (PM): for every generalized shift,
`p_max(T′_k) ≤ p_max(T_k)`. Proved: (PM) ⇒ (PX-peak) (S39 and induction on
the leaves); (PX-peak) and `p_max(P_n) ≤ ⌈n − n/√5⌉` ⇒ the upper half. The
path bound is the informal last step of Collins's Theorem 3; exact for
`n ≤ 2000` (the path's maximizing index is unique and equals
`⌈n − n/√5⌉` for 393 values of `n`, `⌊n − n/√5⌋` for 1,605). Evidence for
(PM), exact (`results/tree-shift.json`, part E): every shift of every tree of
order 5 to 15; 10,812 shifts of families of orders 20 to 150; 4,000 random
shifts of random trees of orders 30 to 100; no violation; smallest relative
margin about 0.0014 (order 120). Scratch, not stored: double brooms shifted
to brooms up to order 300, no violation, margin about `c/n`, `c` between 0.3
and 0.7. Ratio dominance `d_{j+1}(T′)/d_j(T′) ≤ d_{j+1}(T)/d_j(T)` fails even
at `j = p_max(T_k)` (2,292 of 95,248 shifts of orders 4 to 14, the smallest
`S(2,2) → S_6`; the reviewer of `8b03309`), so (PM) needs another mechanism.

**Conjecture Γ (MD-0010) and Hypothesis V (MD-0009) — open; no longer on
the route to the lower half.** Γ: for every tree `S` and every `A ⊆ V(S)`,
`|A| ≥ 2`, the polynomial `r_A` is in the half-gamma cone `C_{s−|A|+1}`.
Proved for `A = V`, for `A` with independent complement or complement of at
most two vertices, and (exactly) for the 47 trees with 2 to 8 vertices; all
roots of `r_A` are real. Chain `Γ ⇐ Γ⁺ ⇐ Γ_c ⇐ (E) ⇐ (Λ)`; (E″), (S) false.
V: non-negative mixed partials of `D_n` for caterpillars. Full text as of
session 10: [`notes/gamma-chain.md`](notes/gamma-chain.md), last section.

**Hypothesis A(ii) — open (MD-0005).** For every tree `T` of order `n` and
every `0 ≤ k ≤ min(p_n, n−3)`, `p_n` the largest maximizing index of the path:
`ρ_k(T) ≤ ρ_k(P_n)`. Exact for all trees of order 4 to 20 and 10,000 sampled
trees of orders 24 to 90; proved for `k = 0` (L2). With Collins's theorem on
paths it would give the upper half. The path does not maximize `ρ_k` at every
index.

**Questions Q1, Q2 — open.** Q1: for balanced caterpillars with fixed spine
length `s`, `n(1 − q) → 6/(2s+3)` (observed at `n = 10³ … 10⁶`). Q2: is
`q(T) < 1` for every tree of even order (the lower half)? The smallest margins
found are on balanced caterpillars whose spine grows slowly with `n`
(`1 − q ≈ 1.3 × 10⁻⁶` at `n = 10⁵`, spine 33); `results/near-star-families.json`.

## Failed approaches and refuted hypotheses

Full text of each: [`notes/dead-ends.md`](notes/dead-ends.md).

- **Hypothesis A(i) — refuted (MD-0004).** `ρ_k(T) ≥ ρ_k(S_n)` for
  `k ≤ ⌊n/2⌋ − 1` holds for all trees of order 4 to 19 and fails at order 20
  (`S(9,9)`: `q = 10255/10791 > 94/99`). Do not retry star-comparison at
  `k = ⌊n/2⌋ − 1`.
- **Inequality (3) of `wiener-form.md` — refuted as a route (S31, session
  10).** Dropping the pairs at distance ≥ 2 from the Wiener form loses the
  even case: negative at `n = 100` on spiders with legs of length 2. The
  cone statement `4(W − 3n)Θ_T − 16n(1+x)^{n−2} − Σ_e (n − 2n_e)² Π_e ∈ C_{n−2}`
  (which would imply (3) > 0) holds for all trees of order 7 to 15 and fails
  on the same spiders from about `n = 30` (scratch, not stored). **Test
  even-order statements on spiders with many legs of length 2 at `n ≥ 100`.**
- **Roots of `r_A`** (session 7): real-rootedness does not give the cone
  (`1 + 5x/2 + x²/2`); pairing roots cannot work for long paths.
- **Darroch's theorem** on the mode (session 7): the index needed is the upper
  central one, where a bound on the mean decides nothing.
- **Termwise absorption in S17** (session 7): `E*` alone leaves the cone.
- **(E″) and (S)** (proposed in session 7, **refuted in session 8**, S21):
  `F = E − xR(T′, ν+e_u)` is not in `C_{j′+2}` for stars with many heavy
  leaves, so a proof of (E) cannot discard `R(T′, ν+e_u)`; the slope
  statement (S) fails already at 5 vertices. The session-7 range (`j ≤ 5`,
  weights ≤ 2) contained no failure: **test auxiliary cone statements on
  stars with heavy leaves (weights ≥ 4) before building on them.**

## Counterexamples and observations

- No counterexample to the Collins–Shor conjecture was found.
- For odd `n` the lower-bound margin is wide; for even `n` it tends to 0.
- For `10 ≤ n ≤ 19` the star minimizes `ρ_k` exactly for `k ≤ ⌊n/2⌋ − 1`.
- The relative margin `1 − d_{m−1}/d_m` behaves like a constant over `n` in
  every family examined (double stars: about `1/n` for even and `3/n` for odd
  order; `K(a,b,c)`: `≈ 0.0024` at order 302). Not proved.
- In every case computed, the tree "skeleton plus one star" with the smallest
  `d_m − d_{m−1}` has the star at a vertex of large degree or central
  position; no rule was extracted.
- `Ω` has non-negative coefficients in all 4,395 rooted weighted trees
  computed (not proved; it would follow from Γ_c).

## Dependency map

```
Collins–Shor, lower half  (⇔ d_{m−1} < d_m, m = ⌊n/2⌋, by R1 [Lean])
  ODD ORDER, every tree:  T4  ⇐ S25 (Wiener form) ⇐ L1, S24 ⇐ Lemma F   [candidate proof, session 9 (MD-0016)]
  EVERY ORDER, every tree: T6(c)                                          [candidate proof, session 11 (MD-0019)]
    ⇐ (SM): ℓ_T − ℓ_{S_n} ∈ C_{n−1}   (T6(b); also from S36)              [candidate proof]
    ⇐ S23(c) (telescoped leaf recursion) + T6(a) ⇐ T5(i): Ω ∈ K_a          [S23(a)–(c): see obligation 11]
    ⇐ T5: (Γ_c¹), by induction on rooted trees                            [candidate proof]
        ⇐ S19 (plant, merge rules) [AI-reviewed, MD-0015], S33 to S35, Lemma K, Lemma S24
    ⇐ the star: d_{m−1}(S_n) < d_m(S_n)                                   [KNOWN: Collins 1989, Theorem 1]
    ⇐ R1 [Lean], Lemma A(a) [Lean on the cone], log-concavity [Theorem 2.1 of the source]
  routes that are not needed any more: S30(d) and (SM⁺) (now consequences of T5); Γ_c, (E), (Λ) [OPEN];
    inequality (3) of wiener-form.md                                     [FALSE in general: S31]
  the route of sessions 4 to 8 (S1, L4, S4, Property Γ, "skeleton plus one star"; leafy trees only):
    superseded for the lower half; verbatim in notes/gamma-chain.md, last section.
  special cases with complete candidate proofs, both halves, peak exactly m:
    diameter 3: T1;  caterpillars of diameter 4: T2, T3, P_5;  stars: Collins 1989, Theorem 1

Collins–Shor, upper half
  ⇐ R1
  ⇐ (PX-peak) + p_max(P_n) ≤ ⌈n − n/√5⌉               [(PX-peak) OPEN (MD-0021); path bound exact for n ≤ 2000]
      ⇐ (PM) + Lemma S39                             [(PM) OPEN; S39 candidate proof (MD-0020)]
  coefficientwise path maximality T8                 [candidate proof; does NOT locate the peak]
  ⇐ Hypothesis A(ii) at k = p_n                      [OPEN; k = 0 proved (L2)]
  ⇐ Collins 1989, Theorem 3: d_{n−k}(P_n) = C(n+k−1, 2k−1)(k−1)n/k; peak of P_n at ⌊n − n/√5⌋ or ⌈n − n/√5⌉
                                                     [read in session 11; the last step of its proof is informal]
  no mechanism from the skeleton expansion           [Property Γ says nothing about it]
```

## Decisions

- Sessions 1 to 8 (verbatim in [`notes/obligations.md`](notes/obligations.md),
  last section). Still in force: strong reading of ties; T1 to T3 stay
  candidate theorems (director); every description of T2 states
  `a, b, c ≥ 1`; formalization accompanies the investigation; reviews by a
  model other than the author's; a note is left byte-identical to the
  revision that was reviewed, its defects go into one revision that is then
  rechecked, new results go in a new note; Γ⁺, Γ_c, (E), (Λ) are not
  registered as conjectures of their own; MD-0013 is not split.
- 2026-11-26 (director, session 9). The AI investigator allocates effort by
  its own judgment; earlier directions are revisable. MD-0013 keeps its
  identifier and review; its items are classified as known or potentially
  original in the record. The current classifications are approved; verified
  commits may be pushed to `research` only.
- 2026-11-26 (session 9). Direction changed: the lower half is attacked for
  the whole tree (Wiener form, leaf recursion), not through Γ, L4 and
  "skeleton plus one star". O8 ((Λ)) is deferred, not abandoned: (Λ) still
  implies (Γ_c¹). (SM) is registered as a conjecture of its own (MD-0017)
  because it implies the lower half for every tree; (Γ_c¹) is not.
- 2026-11-26 (director, session 10). MD-0016 is to receive independent
  validation and an originality assessment before promotion; CJ-0001 keeps
  its status until the validation requirements are met; the director's
  preliminary reading with GPT-6.2 (no apparent gap) is not a proof audit.
  Verified commits may be pushed to `research` only.
- 2026-11-26 (session 10). `wiener-form.md` had its one revision (`a3e5179`)
  and is left byte-identical to it; the five defects found by the audit of
  that revision go into one further revision. (SM⁺) is recorded under
  MD-0017, not registered. S28 to S31 are one record (MD-0018).
- 2026-11-26 (director, session 11). Session budget 120 minutes, with
  checkpoints (harness commit `759d93f`); this replaces the 60 minutes of the
  decision above. For the current phase the project relies on independent AI
  reviews, adversarial verification, exact computation and Lean; **human
  specialist consultation is deferred until there is a mature manuscript**
  (this replaces "a human reader, or a different vendor's model, before any
  promotion" as the next step of obligations 2, 3 and 9; the requirement of
  section 4 of `AGENTS.md` for promotion is unchanged). Verified commits may
  be pushed to `research` for research contributions.
- 2026-11-26 (session 11). T5, T6 and S36 are one record (MD-0019); MD-0017
  keeps its identifier and its statement (the conjecture (SM)), now with a
  candidate proof. The lower half is treated as a candidate proof to be
  consolidated into one self-contained manuscript before promotion.
- Earlier decisions (budget overrun of session 1, widening of O1, deferral of
  the rerun of orders 21 to 23, the notes of sessions 5 and 6) are in the
  journal.

## Open obligations

Details and history: [`notes/obligations.md`](notes/obligations.md) (the
full text of items 1 to 8 as of session 7 is there).

1 to 8 (unchanged in session 11; full text:
   [`notes/obligations.md`](notes/obligations.md), last section). In short:
   1 literature and citations owed (T1 to T3, L3, S1, S3, MD-0013; unread
   sources; no MathSciNet, zbMATH, Google Scholar); 2 one revision and one
   recheck of the notes of T1 to T3; 3 revisions owed after reviews
   (`skeleton-identity.md`, `skeleton-locality.md`, `vertex-principle.md`,
   `gamma-components.md`, `gamma-reduction.md`, `rooted-calculus.md`); 4 E2,
   orders 21 to 23: independent recomputation (about 34 minutes; needs the
   director's approval); 5 comparison with Table II of Graham–Lovász; 6 the
   identifications of L1 and L3 as known are unreviewed; 7 formalization
   (independent comparison of the Lean statements; L4 as written; the
   inductive cone against explicit sums; next: S4, Lemma F); 8 description
   strings of `spine3.py`.
9. **T4 (MD-0016), before any promotion.** Done: two AI reviews (same
   vendor), no gap; a first literature audit; Lean for Lemma A and `K_d`.
   Owed: (a) one revision of `wiener-form.md` for the audit's defects D1 to
   D5 (S26 and the tools list still cite Lemma F; `W = Σ_e n_e(n − n_e)`
   uncited; L1 at `n = 2`; the `C`-clause of S24; "strong induction"), then
   a recheck, then drop the dependency on MD-0012; (b) **a human reader or a
   model of another vendor** — the director's GPT-6.2 reading is not a
   recorded audit; (c) literature: Collins 1989 and Collins's thesis were
   **read in session 11** (neither contains S25 or T4; the thesis has a leaf
   formula, Theorem 4, to be cited for S23 and S29, and a formula for two
   graphs joined at a vertex, Theorem 7, to be cited for S19(d); S23(d) is
   Collins 1989, Theorem 1). Still unread: Graham–Lovász pp. 72–88, Merris
   1990, Moon 1995; MathSciNet, zbMATH, Google Scholar not searched; the
   auditor's two bridging steps (S24, identity (1)) are unreviewed; (d) a
   result package. `leaf-telescoping.md` (S23, S27) is **unreviewed**.
10. **Session 10.** `even-order.md` (S28 to S31, MD-0018) is **unreviewed**
   and has no literature search. The Lean statements of `WienerCone.lean`
   were compared with the note by the formalizing agent and the author only.
11. **Session 11: T5, T6, S36 (MD-0019), before any promotion.** Done: two
   independent AI reviews of `lower-bound.md` at `74d65b0`, both **no gap
   found** — `claude-opus-5-5` (every step by hand, S23(a) to (c) included;
   its own code on all 205,002 trees of order 3 to 18 and on extreme
   families) and `claude-fable-5-2` in a fresh context (the author's model,
   so independent by context only; a machine re-derivation from the
   definitions on 7,813 rooted trees of order ≤ 12, 18,048 pairs, weighted
   trees, all trees of order ≤ 18); the stored computation `lower_bound.py`
   (1,040,693 checks, 0 failures); Collins (1986, 1989) read. Owed:
   (a) **one revision of `lower-bound.md`**, then a recheck, for the defects
   the two reports list (none is a gap): the section "Exact checks" cites a
   script that did not exist at the reviewed revision and gives "778 pairs"
   where the described set has 1,064, and "1,064 pairs" for S36 of which 486
   are outside its hypothesis; the proof of S32 is by reference to that of
   S24 and should be written out; Remark 1 of S36 asserts `E ≡ 0 (mod x²)`
   without argument; notation used twice (`E` is not the `E` of S17 and S20;
   `a`, `a_v`, `a_i`; `Q`, `Q¹`; `X`, `X_{il}`; `n` for a weight in "S19(a)
   with `n = 0`"); in `leaf-telescoping.md`, S23(a) uses L1 at `n = 2` while
   `lemmas.md` states it for `n ≥ 3` (true at `n = 2`; a citation defect).
   The note is left byte-identical to `74d65b0` until that revision.
   (b) **One self-contained manuscript of the lower half**, from the
   Graham–Lovász inverse to T6(c) (L1, Lemma K, S24, S19 with zero weights,
   S23, S33 to S35, T5, T6), then a complete audit of that one document; a
   model of another vendor when one is available (human consultation is
   deferred by the director's decision of session 11). S19 was re-derived by
   neither reviewer of this session (they relied on the review of `59c47f7`
   and on exact checks). (c) Literature: see the audit of session 11 in the
   dossier, and the limits it states. (d) A result package. (e) The Lean
   statements of `LowerBoundCone.lean`, if registered, were compared with
   the note by the formalizing agent and the author only.

12. **Session 12: T7, T8 (MD-0020).** Done: one AI review of
   `path-maximality.md` at `8b03309` (`claude-opus-5-5`, the author's model;
   no gap); the stored computation `tree_shift.py` (`results/tree-shift.json`,
   0 failures). Owed: one revision of the note for the review's defects D1 to
   D8 (the cited code for `Δ_k = c_k` is the wrong scratch script — the check
   is now part A of `tree_shift.py`; notation `a_j`, `ρ_k`, `C(t)`, `Q`, `T_0`;
   a self-contradictory sentence in the equality remark; the star's unique
   peak cited to S23(d) instead of Collins 1989; two negative claims stated
   beyond their support; the path bound attributed to Collins's theorem
   rather than to its informal last step; the header's dependency list), then
   a recheck; a reviewer of another model when one is available; a
   literature search aimed at distance-matrix versions of Csikvári's
   results; it depends on MD-0019 and MD-0015, which are candidates.

## Remaining obstacles

- **Lower half.** No mathematical obstacle is known: T6 is a candidate proof
  for every tree. What remains is validation (obligation 11) and one
  self-contained write-up. How the difficulty of session 10 (the deep-edge
  terms, one level short) was avoided: they are never separated from
  `R(A_l, e_{c_l})` except where an extra factor `x` is available (Remark
  after T5 in `lower-bound.md`).
- **Upper half.** Reduced to (PM) (MD-0021), with no proof mechanism: the
  cone order controls only `μ ≤ n/2`, and ratio dominance fails at the
  relevant index. What a proof must show is a sign: with `p = p_max(T_k)`,
  `λ_{p+1}(ℓ_{T′_k}) = λ_{p+1}(ℓ_{T_k}) − λ_{p+1}(ℓ_{T_k} − ℓ_{T′_k}) < 0`, where
  the second term is given by S37. A(ii) is unproved beyond `k = 0`.
- Γ_c for general weights, (E), (Λ), Conjecture Γ: open, and now of interest
  only for themselves (the weighted statements), not for Collins–Shor.

## Next step

**Owed first.** (a) Obligation 11: the one revision of
`notes/lower-bound.md` for the defects listed there, and its recheck; then
`manuscripts/CJ-0001-lower-bound/`, one self-contained proof of T6(c) from the
Graham–Lovász inverse (L1, Lemma K, S24, S19 for zero weights, S23, S33 to
S35, T5, T6) for a complete audit. (b) Obligation 12: the one revision of
`notes/path-maximality.md` for the defects D1 to D8 of its review, and its
recheck.

**Objective O11 (the upper half) through (PM) (MD-0021).** First action
(exploration, cheap, exact): for the shifts of order ≤ 14 where ratio
dominance fails at `p = p_max(T_k)`, split `λ_{p+1}(ℓ_{T_k} − ℓ_{T′_k})` into the
four terms of S37 and see which one is negative and how it compares with
`λ_{p+1}(ℓ_{T_k})`; look for an inequality between `λ_{p+1}` of the terms
`a_{k−1}(H_AE_B + E_AH_B)` and `λ_{p+1}(ℓ_{T_k})` that a proof could use. Keep
testing (PM) on families before building on it (spiders with legs of mixed
lengths and caterpillars near the star at orders ≥ 200).

Upper cone, floating-point LP of session 11 (exploratory, not a
certificate): for every tree of order 5 to 14 the part of `ℓ_T` of degree
`≤ n − 2` is a non-negative combination of `x^e(1+x)^i` with `2e + i ≤ 2M + 1`
(on which `λ_{M+1} ≤ 0`), with no margin for two near-stars at order 14.

Also open and cheap: obligations 5 and 8; the rerun of orders 21 to 23
(obligation 4) needs the director's approval of its budget.

## Sources

- G. Aalipour et al., arXiv:1507.02341 — read in full (TeX source; twice by reviewers).
- K. L. Collins, Discrete Appl. Math. 25 (1989) 27–35 — read in full (session 11). K. L. Collins, Distance matrices of trees, thesis, MIT 1986 — read (pp. 30–47, 55–61 as page images, the rest through OCR; session 11). Details: the dossier, section "Primary sources read in session 11".
- Every other source, with what was read of each: [`notes/obligations.md`](notes/obligations.md), last section, and the dossier. None was added in session 9. Session 10: what its audit read is in the dossier, section "Audit for session 10".
