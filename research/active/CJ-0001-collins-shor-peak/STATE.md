# CJ-0001 — Collins–Shor conjecture — investigation state

Last updated: 2026-11-27 (session 15). This file is the current truth about the
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
Collins (1986) and Collins (1989) read (dossier, section "Primary sources read in session 11").
**Session 12:** [`notes/path-maximality.md`](notes/path-maximality.md) (S37 to
S39, Theorems T7 and T8: the generalized tree shift lowers `ℓ` in the cone
order, and the path is the coefficientwise maximum — a candidate proof;
statements (PM) and (PX-peak) on the location of the peak, open).
**Session 13:** [`notes/upper-bound.md`](notes/upper-bound.md) (S40 to S46,
T9, T10: **the upper bound for every tree**, a spectral route; the path
minimizes `tr(I + L)^{−1}`) and [`notes/path-peak.md`](notes/path-peak.md)
(S47, S48: the exact peak of the path). **Session 14:** the manuscript
[`manuscripts/CJ-0001-collins-shor/main.tex`](../../../manuscripts/CJ-0001-collins-shor/main.tex)
(both halves, self-contained; obligation 14); CJ-0001 `candidate-proof`
(director). **Session 15:** the review of revision 2 by an OpenAI model
through Codex (no gap; six findings, all accepted); revisions 3 and 4
(obligation 15); T10 is a consequence of Andriantiana–Misanantenaina–Wagner
(MD-0023 `previously-resolved`; the merging lemma S45 is MD-0025); a proof
of Collins's formula ([`notes/path-formula.md`](notes/path-formula.md),
MD-0026).
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

Mathematical: `candidate-proof` (since session 14, by the director's approval of 2026-11-27, which does not authorize `proved`). Formal: `partial`. Novelty:
`preliminary-search-completed`. External review: `not-reviewed`.

Nothing in this file is an established result of the project. "Reviewed"
means AI review of one revision in a fresh context (named in the registry);
no mathematician has read any of it, and originality is not established.
Candidate theorems (director, 2026-11-26, and later sessions): T1, T2, T3;
T4 (the lower bound for odd order); T5, T6 (the lower bound for every order;
obligation 11); T7, T8 (coefficientwise path maximality; obligation 12); T9
(the upper bound; obligation 13). T10 is a consequence of a published
theorem (session 15). **Both halves of the conjecture have candidate
proofs**, written as one manuscript reviewed by AI models of two vendors;
neither is established. The status of every registered contribution is in
[`research/discoveries.json`](../../discoveries.json), not here.

Formal (Lean, `formalization/Conjectura/Research/CollinsShorPeak/`): 31 registered theorems for this problem (count of session 14; the figure 21 written here earlier was out of date); the latest receipt is under `verification/receipts/` (session 14: `20261127T213151Z-8cbc0151bc-passed.json`, clean tree). **Session 14** (`StarShape.lean`): the binomial statement of Lemma 7.5 of the manuscript (the star's coefficients increase strictly up to `⌊n/2⌋` and decrease strictly after it), both parts, by a different route from the written proof (a polynomial identity and positivity); not the identification of those coefficients with `d_k(S_n)`. **Session 10** (`WienerCone.lean`): the cones `K_d` (`WienerCone`) with (K1), (K2), and Lemma A of `wiener-form.md` on the cone, strict part included — nothing about trees, `Φ`, S24 to S26 or T4. In Lean before that: the general form of R1; the discrete core of L4, since session 8 **in any finite number of variables** (`vertex_principle_discrete`: a function on integer points with the exchange inequality `f(c+e_i−e_k) + f(c+e_k−e_i) ≤ 2f(c)` on the slice is, at every point of the slice, at least its value at some vertex `λ + (S−Σλ)e_p`); the cone `C_d` over real polynomials (`HalfGammaCone`) with `C_d·C_e ⊆ C_{d+e}`, `x·C_d ⊆ C_{d+1}`, `x·C_d ⊆ C_{d+2}`, `(1+x)·C_d ⊆ C_{d+1}`, `x(1+x)·C_d ⊆ C_{d+3}`, and Lemma C. **Not formalized:** the step from a multi-affine polynomial with non-negative mixed partials to the exchange inequality (so L4 as written is not formalized); the equality of the inductive cone with the explicit non-negative sums; anything about trees, determinants or `r_A`. The Lean statements were compared with the written ones by the formalizing agent and the author of the session only.

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
| S40 to S46, **T9, T10** | **Spectral route to the upper half.** `ℓ_T = 4(α − x)q(x)`, `q = Π(x + β_i)` over the negative eigenvalues `−β_i` of `D/2` (S40); if `q_{k+1} < q_k` then `d` is strictly decreasing from `k` on (S41); `μ_q = Σ 1/(1+β_i) ≤ n − tr(I+L)^{−1}` (S42, interlacing); gluing formula for the trace (S43); the path seen from one vertex, closed forms in `cosh` (S44); merging two pendant paths lowers `tr(I+L)^{−1}` (S45); **T10: the path minimizes `tr(I+L)^{−1}` among trees**; `tr(I+L_{P_n})^{−1} = n/√5 + 2/5 + (2n/√5)r^{2n}/(1−r^{2n})` (S46); with Darroch's rule, **T9: every maximizing index is `≤ ⌈n − n/√5 − 2/5⌉ ≤ ⌈n − n/√5⌉`, for every tree of order `n ≥ 3`.** | Candidate proof (session 13); **two independent AI reviews of `53421a6`, no gap found**: `claude-opus-5-5` (fresh context, the author's model) and `claude-sonnet-5-5` (a different model, same vendor); every step re-derived by both; their own exact code on all trees of order ≤ 17 and ≤ 16. Revision 1 (`2037b18`) repairs their defects of wording; its recheck: obligation 13. Uses only classical results (Graham–Lovász, Weyl, Newton, Darroch 1964, Merris 1990), none of MD-0015 to MD-0021. **T10 is a consequence of Andriantiana–Misanantenaina–Wagner (2020), Theorem 4.4** through the subdivision (session 15: confirmed by the external reviewer of revision 2, proved in Remark 9.6 of revision 3, checked exactly); MD-0023 is `previously-resolved`, the proof by merging (S45) is independent and is MD-0025. Exact: `results/upper-bound.json`, `results/amw-reduction-check.json`. |
| S47, S48 | **The peak of the path, exactly**: unique, at `n − k_0(n)`, `k_0` the least `k ≥ 2` with `5k³ + 2k² − 4k − 2 > kn²`; always `⌊x⌋` or `⌈x⌉` (`x = n − n/√5`), the ceiling only if the fractional part of `n/√5` is below `1/5`, and whenever it is below `1/10` (`n ≥ 30`), so for infinitely many `n`. Completes the informal last step of Collins's Theorem 3. | Candidate proof (session 13), from Collins's closed formula; not reviewed (obligation 13). Criterion exact for `n ≤ 2000` (scratch). |
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
| S40 to S42, S46, T9 | MD-0022 | theorem (candidate) |
| T10 with S46 | MD-0023 | theorem (previously resolved: AMW 2020; session 15) |
| S47, S48 | MD-0024 | theorem (candidate) |
| S45 (with S43, S44) | MD-0025 | lemma (candidate; session 15) |
| proof of Collins's formula (`path-formula.md`; Lemma 11.3) | MD-0026 | proof (candidate; session 15) |

Not registered: R1, L2, L4 and S1 to S4 are tools or steps (S3 and S4 are the
evidence of MD-0010); Γ⁺ is an observation on the 47 small trees, recorded
under MD-0012; Γ_c and (E) are stated in MD-0014, and (Λ) in MD-0015, and are
not registered as conjectures of their own; E1 reproduces a published
verification; Q1, Q2 are questions.

## Conjectures and hypotheses of this investigation

Full text as of session 14: [`notes/obligations.md`](notes/obligations.md),
section "Text moved from `STATE.md` in session 15".

- **(SM), star minimality (MD-0017):** `ℓ_T − ℓ_{S_n} ∈ C_{n−1}` for every
  tree; candidate proof since session 11 (T6(b), MD-0019; also from S36).
  (SM⁺) and (CM) are variants (moved text).
- **Extremality:** coefficientwise `d_k(S_n) ≤ d_k(T) ≤ d_k(P_n)` (T6(b), T8,
  candidate proofs); the star is peak-minimal (T6(c), the lower half);
  peak-maximality of the path is (PX-peak) below. Termwise domination does
  not order maximizing indices.

**(PX-peak) and (PM) — open (MD-0021); not needed for the upper half.**
(PX-peak): `p_max(T) ≤ p_max(P_n)` for every tree of order `n`. By T9 it
holds for every `n` with `p(P_n) = ⌈ξ − 2/5⌉`, `ξ = n − n/√5`: the `n` with
fractional part of `ξ` below `2/5`, and the `n` with `p(P_n) = ⌈ξ⌉` (for
instance `n = 9`; finding 2 of the review of revision 2). Open for the
others: 806 of the `n` in `[3, 2000]` are not reached by the argument
(`amw_reduction_check.py`, part D); the 11 of them with `n ≤ 23` are settled
by the exhaustive computation (the path has the largest peak index in every
order ≤ 23), so 795 are open, the smallest 25 (defect D1 of the recheck of
revision 3). A sharper mode–mean inequality
for `q` would be one approach; it is not known to be necessary. (PM) (every
generalized shift lowers `p_max`) implies (PX-peak) (S39); its exact evidence
and the failure of ratio dominance: `notes/obligations.md`, section "Text
moved from `STATE.md` in session 15".

- **Open, and on the route to neither half:** Conjecture Γ (MD-0010),
  Hypothesis V (MD-0009), Hypothesis A(ii) (MD-0005; ratio comparison with
  the path, exact to order 20, proved for `k = 0`), Questions Q1, Q2 (margins
  of balanced caterpillars). Statements and evidence: the moved text and
  [`notes/gamma-chain.md`](notes/gamma-chain.md).

## Failed approaches and refuted hypotheses

Full text: [`notes/dead-ends.md`](notes/dead-ends.md); the summary as of
session 14 is in the moved text. The lessons still in force:

- **A(i) refuted at order 20** (MD-0004; `S(9,9)`): do not retry the star
  comparison of ratios at `k = ⌊n/2⌋ − 1`.
- **Inequality (3) of `wiener-form.md` fails at `n = 100`** (S31): test
  even-order statements on spiders with many legs of length 2 at `n ≥ 100`.
- **(E″) and (S) refuted** (S21): test auxiliary cone statements on stars
  with heavy leaves (weights ≥ 4) before building on them.
- Session 7: real roots of `r_A` do not give the cone; Darroch's rule
  applied to `r_A` decides nothing at the upper central index (the spectral
  route of session 13 applies it to `q` instead); termwise absorption in S17
  leaves the cone.

## Counterexamples and observations

- No counterexample to the Collins–Shor conjecture was found (orders 3 to
  23); one tie (order 13, value 189972). Margins and other observations:
  the moved text.

## Dependency map

As written in the manuscript (revision 3); the map as of session 14, with the
routes no longer needed, is in `notes/obligations.md`, section "Text moved
from `STATE.md` in session 15".

```
Collins–Shor, lower half: every maximizing index ≥ ⌊n/2⌋        [candidate proof; MD-0019]
  ⇐ (SM): ℓ_T − ℓ_{S_n} ∈ K_{n−1} (Thm 7.3(b); T6(b))  + Lemma A (cone increments) [Lean on the cone]
      ⇐ telescoped leaf recursion (Cor. 5.3; S23) + T6(a) ⇐ T5 (Thm 7.1): Ω ∈ K_a, E ∈ K_{a+1}, R_1 ∈ K_{a+1}
          ⇐ Lemma 5.1, Prop. 5.2 (root weights only), Props. 6.1–6.3 (S33–S35), Lemma K, Lemma S24
  ⇐ the star rises strictly up to ⌊n/2⌋ and falls after it (Lemma 7.5) [Lean: StarShape.lean, binomial part]
  (no log-concavity, no Collins 1989 Thm 1 since revision 2; odd order also by T4, MD-0016)

Collins–Shor, upper half: every maximizing index ≤ ⌈n − n/√5 − 2/5⌉   [candidate proof; MD-0022]
  ⇐ S41 (peak of d ≤ mode of q) [Lean] ⇐ S40 (ℓ_T = 4(α − x)q) ⇐ Graham–Lovász, Weyl, Newton
  ⇐ Darroch's rule [KNOWN, 1964] applied to q
  ⇐ S42: μ_q ≤ n − tr(I+L)^{−1} [interlacing; KNOWN in substance: Merris 1990]
  ⇐ T10: tr(I+L_T)^{−1} ≥ tr(I+L_{P_n})^{−1} [KNOWN: AMW 2020, Thm 4.4, via the subdivision (MD-0023)]
      independent proof: S45 (MD-0025) ⇐ S43 (gluing), S43′, S44 (cosh forms; convexity of x/(φ^{2x}+1) on [3, ∞))
  ⇐ S46: tr(I+L_{P_n})^{−1} > n/√5 + 2/5 [Fourier series; also AMW Lemma 4.2]
Attainment: the star (Lemma 7.5); the path for infinitely many n (S47, S48; MD-0024)
  ⇐ Collins's formula: Collins 1989, Thm 3, and Lemma 11.3 (MD-0026: Laplacian form, Lemma 4.3, Cauchy–Binet)
Special cases with separate candidate proofs, peak exactly m: T1 (diameter 3), T2, T3, P_5 (diameter 4)
```

## Decisions

In force (full text of every decision, sessions 1 to 11:
[`notes/obligations.md`](notes/obligations.md), section "Text moved from
`STATE.md` in session 13"): the strong reading of ties; T1 to T3 stay
candidate theorems; formalization accompanies the investigation; reviews by a
model other than the author's where available; a reviewed note stays
byte-identical, its defects go into one revision that is rechecked, new
results go into a new note; the AI investigator allocates effort by its own
judgment (director, session 9); CJ-0001 keeps its status until the
validation requirements are met (director, session 10); 120-minute sessions
with checkpoints, independent AI review, exact computation and Lean for the
current phase, human consultation deferred until there is a mature
manuscript (director, session 11); verified commits may be pushed to
`research` only; the lower half is to be consolidated into one manuscript
before promotion (session 11).

- 2026-11-27 (session 13). T9 with S40–S42, S46 is MD-0022; T10 is MD-0023;
  S47, S48 are MD-0024. (Session 14, director: CJ-0001 is `candidate-proof`,
  which does not authorize `proved`.)
- 2026-11-27 (session 15). MD-0023 reduced to its statement proper (T10 and
  the value S46) and set `previously-resolved` / `prior-resolution-identified`
  (AMW 2020), following the precedent of MD-0002 and MD-0003; the merging
  lemma S45, the part of its proof that is not in AMW, is MD-0025. The
  reviewed revision 2 of the manuscript is kept byte-identical in
  `manuscripts/CJ-0001-collins-shor/versions/r2/`; any substantial
  simplification goes into a later revision, never over a reviewed one.
  CJ-0001's `external_review` is left at `not-reviewed`: setting it to
  `ai-reviewed` is the director's decision (skill `review-claim`, step 5).

## Open obligations

Details and history: [`notes/obligations.md`](notes/obligations.md) (the
full text of items 1 to 8 as of session 7 is there).

1 to 8 (unchanged in session 11; full text:
   [`notes/obligations.md`](notes/obligations.md), section "Text moved from
   `STATE.md` in session 11"). In short:
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
Items 9 to 14 as of session 14, in full: `notes/obligations.md`, section
"Text moved from `STATE.md` in session 15". In short:
9. **T4 (MD-0016):** one revision of `wiener-form.md` (audit defects D1 to
   D5) and a recheck; `leaf-telescoping.md` (S23, S27) never reviewed on its
   own; Moon 1995 unread.
10. `even-order.md` (MD-0018) unreviewed, no literature search;
   `WienerCone.lean` compared by its author only.
11. **T5, T6, S36 (MD-0019):** done: two reviews of `74d65b0`, revision 1
   rechecked, the self-contained manuscript (obligation 14). Owed: a result
   package; `LowerBoundCone.lean` compared by its author only; S36 is in no
   manuscript.
12. **T7, T8 (MD-0020):** one review of `8b03309`; one revision (defects D1 to
   D8) and a recheck owed; literature on distance versions of Csikvári's
   results.
13. **T9, T10 (MD-0022, MD-0023), S47, S48 (MD-0024):** done: two reviews of
   `notes/upper-bound.md`, revision 1 rechecked, a first review of
   `notes/path-peak.md`, Lean for S41, the manuscript (obligation 14). Owed:
   the defects of those reviews in one later revision of each note; Darroch
   (1964) not read in the original (still not accessible in session 15);
   a result package; Lean beyond S41. The draft
   `manuscripts/CJ-0001-upper-bound/main.tex` is superseded.
14. **The manuscript** (`manuscripts/CJ-0001-collins-shor/`; versions,
   hashes and reviews in its `README.md`). Revision 1 `8df6bea`: two reviews
   (Anthropic), no gap. Revision 2 `87c3c8c`: Lemma 7.5 added; recheck
   (`claude-sonnet-5-5`), no gap; **review of the whole document by an
   OpenAI model through Codex** (session 15), no gap found within its scope,
   six findings. The count "1,346,023" in `notes/leaf-telescoping.md` is a
   slip for 1,346,022 (left in the note, corrected in the manuscript).
15. **Session 15.** Revision 3 (`f695cbd`) corrects the six findings (record
   and assessment: `reviews/2026-11-27-codex-gpt-astra-6-manuscript-r2.md`);
   recheck (`claude-opus-5-5`, fresh context): no gap, eight minor defects.
   Revision 4 (`4b02146`) corrects them and adds Lemma 11.3 (Collins's
   formula proved; MD-0026, its note reviewed by `claude-sonnet-5-5`, no
   gap); recheck of revision 4: journal of session 15. Revisions 2 and 3
   frozen in `manuscripts/CJ-0001-collins-shor/versions/`. Owed: human
   reading (deferred by the director); a result package once the director
   judges the manuscript mature; MathSciNet and zbMATH (not accessible); the
   journal versions of AMW and Collins (1989) were not compared with the
   versions read; novelty of MD-0026 not searched.

## Remaining obstacles

- **Lower half.** No mathematical obstacle is known: T6 is a candidate proof
  for every tree; what remains is validation (obligations 11, 14, 15). The
  difficulty of session 10 (the deep-edge terms, one level short) is avoided
  by never separating them from `R(A_l, e_{c_l})` except where an extra
  factor `x` is available (Remark after T5 in `lower-bound.md`).
- **Upper half.** No mathematical obstacle is known: T9 is a candidate proof
  for every tree, and its extremal step T10 is now also a consequence of a
  published theorem; what remains is validation (obligations 13 to 15).
- Open, and not needed for Collins–Shor: (PX-peak) for 795 of the `n ≤ 2000`
  (see above); Γ_c for general weights, (E), (Λ), Conjecture Γ.

## Next step

**Session 15:** revision 4 of the manuscript (`4b02146`) is the current text.
It corrects the six findings of the review of revision 2 by an OpenAI model
through Codex (the first review by a model of another vendor; no gap found)
and the eight defects of the recheck of revision 3, and proves Collins's
formula (Lemma 11.3). Its own recheck is in the journal of session 15. The
next steps are validation, not discovery:
(a) a decision by the director on `external_review` of CJ-0001 and on when
the manuscript is mature enough for a result package and for human reading
(both deferred by the director); (b) a recheck of any later revision; a
second whole-document review by another vendor's model, of revision 4,
would add independence (revision 2 is the only one read by such a model);
(c) literature still owed: MathSciNet and zbMATH, Darroch (1964) and the
journal versions of AMW and Collins (1989) (not accessible to the session-15
auditor), a search for MD-0026; (d) optional, only after (a): a substantial
simplification of the manuscript (for instance citing AMW for T10 and
dropping Lemmas 9.1–9.4) as a new revision, keeping the reviewed revisions
intact; (e) open mathematics: (PX-peak) for the 795 orders `24 ≤ n ≤ 2000`
(and beyond) with `p(P_n) = ⌊ξ⌋` and fractional part of `ξ` above `2/5`.

The items of session 12 under "Next step" (the route through (PM), the upper
cone LP) are in `notes/obligations.md`, section "Text moved from `STATE.md`
in session 13". Also open and cheap: obligations 5 and 8; the rerun of
orders 21 to 23 (obligation 4) needs the director's approval of its budget.

## Sources

- G. Aalipour et al., arXiv:1507.02341 — read in full (TeX source; twice by reviewers).
- K. L. Collins, Discrete Appl. Math. 25 (1989) 27–35 — read in full (session 11). K. L. Collins, Distance matrices of trees, thesis, MIT 1986 — read (pp. 30–47, 55–61 as page images, the rest through OCR; session 11). Details: the dossier, section "Primary sources read in session 11".
- Session 15: Andriantiana–Razanajatovo Misanantenaina–Wagner, arXiv:1903.09825 v1, pp. 8–17; Graham–Lovász (1978) p. 83 and Graham–Pollak (1971) pp. 2509–2511 in scans (dossier, "Audit for session 15").
- Every other source, with what was read of each: [`notes/obligations.md`](notes/obligations.md), sections "Sources read" and "Text moved from `STATE.md` in session 11", and the dossier. Session 10: what its audit read is in the dossier, section "Audit for session 10".
