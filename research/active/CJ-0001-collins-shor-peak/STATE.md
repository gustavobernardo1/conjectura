# CJ-0001 — Collins–Shor conjecture — investigation state

Last updated: 2026-11-26 (session 7). This file is the current truth about the
investigation and is meant to be sufficient, on its own, for a new agent to
continue. It was compacted in session 5: details that were here are in the
notes it links. Proofs: [`notes/lemmas.md`](notes/lemmas.md) (R1, L1 to L3),
[`notes/double-stars.md`](notes/double-stars.md) (T1),
[`notes/spine3.md`](notes/spine3.md) (T2),
[`notes/diameter4-caterpillars.md`](notes/diameter4-caterpillars.md) (T3),
[`notes/vertex-principle.md`](notes/vertex-principle.md) (L4, Hypothesis V),
[`notes/skeleton-identity.md`](notes/skeleton-identity.md) (S1 to S4,
Property Γ), [`notes/skeleton-locality.md`](notes/skeleton-locality.md) (S6 to
S10, Lemma C), [`notes/gamma-reduction.md`](notes/gamma-reduction.md) (Lemma F,
S11), [`notes/gamma-components.md`](notes/gamma-components.md) (S12 to S18,
Lemma G). Obligations in detail: [`notes/obligations.md`](notes/obligations.md).
Computations: [`experiments/CJ-0001-collins-shor-peak/`](../../../experiments/CJ-0001-collins-shor-peak/README.md).
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
27–35, attributed there to Peter Shor. According to arXiv:1507.02341, Collins
states it without the floor and the ceiling. Collins's paper has not been read
by the project.

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

Unimodality and log-concavity of `d_0, …, d_{n−2}` are a theorem (Theorem 2.1
of the source). Only the location of the peak is open.

## Status

Mathematical: `active-investigation`. Formal: `partial`. Novelty:
`preliminary-search-completed`. External review: `not-reviewed`.

Nothing in this file is an established result of the project. T1, T2 and T3
are **candidate theorems** (director's decision of 2026-11-26): each has a
written proof and one AI review by a fresh context that found no gap within
its stated scope, none has been read by a mathematician, and their
originality is not assessed. The same holds for what was written in
sessions 5 and 6 and reviewed in session 6 (S1 to S4; S6 to S10 and Lemma C;
Lemma F, F′ and S11): one AI review each by a fresh context of `claude-opus-5-5`, no
human reader. Session 7: Lemma L4, Corollary S5 and the computation of
Property Γ for the 47 small trees each had one AI review of `9499572` (no gap
found within stated scope), and the statements of session 7 (S12 to S18,
Lemma G) one AI review of `b0a4dbe` (no gap found within stated scope;
three defects of wording). The status of every registered
contribution is in [`research/discoveries.json`](../../discoveries.json), not
here.

Formal: the general form of R1 and the discrete core of L4 (concavity on an integer interval; the exchange step for two coordinates) are proved in Lean (`formalization/Conjectura/Research/CollinsShorPeak/`, six registered theorems; the latest receipt is under `verification/receipts/`). They are statements about sequences and about functions on integer points; nothing about trees is formalized, and the Lean statements were compared with the written ones by the formalizing agent and the session's author only.

## Established results

"Level" says what kind of evidence exists; "reviewed" always means an AI
review of one revision, named in the registry.

| ID | Statement | Level |
| --- | --- | --- |
| E1, E2 | The conjecture (every maximizing index in `[m, M]`) holds for all trees of order 3 to 23: 23,942,357 trees, 0 violations. Orders 21 to 23 are beyond the published range. | Exact computation; orders 21 to 23 by one implementation, without a provenance block (obligation 4). |
| E3, E4 | In those orders: one tie (order 13, indices 6 and 7); the peak is always `⌊n/2⌋` or `⌊n/2⌋ + 1`; the star attains the minimum, the path the maximum. | Exact computation. |
| R1 | Lower bound ⇔ `d_{m−1} < d_m`; upper bound ⇔ `M ≥ n−2` or `d_{M+1} < d_M`. General form: for a positive log-concave sequence, every maximizing index is `≥ j` iff `a_{j−1} < a_j`. | Proved; general form reviewed twice and **formalized in Lean**. |
| L1, L2, L3 | The Laplacian formula for `ℓ_T`; `d_1 = 2n² − 6 − Σ deg²`; the quotient-matrix formula for caterpillars. | **Known** (Graham–Lovász 1978; the source; Hogben–Reinhart). Tools. |
| T1 | Double star `S(a,b)`, `a, b ≥ 1`: `m` is the only maximizing index. | Candidate proof, reviewed. Its closed formula (Lemma D1) is **in print**: Xue–Liu–Jia 2016, Lemma 2.3; do Nascimento 2018, Prop. 3.2.1. No peak statement found. |
| T2 | Caterpillar `K(a,b,c)`, `a, b, c ≥ 1`: `m` is the only maximizing index. | Candidate proof (two computer-assisted identities), reviewed. The balanced case of its formula is in do Nascimento 2018, Prop. 3.2.9. |
| T3 | Caterpillar `K(a,0,c)`, `a, c ≥ 1`, `a + c ≥ 3`: `m` is the only maximizing index. With T2 and `P_5`: every caterpillar of diameter 4. | Candidate proof, reviewed. Its formula is in do Nascimento 2018, Prop. 3.2.6. |
| L4 | Vertex principle: a function of degree ≤ 1 in each variable with non-negative mixed second partials attains its minimum over the integer points of a slice `c ≥ λ`, `Σ c = S` at a point with one coordinate above its lower bound. | Proved; AI review of `9499572`, no gap found (the reviewer adds that it holds at real points of the slice too). Its one-dimensional core is formalized in Lean (see Status). |
| S1 | Skeleton `S` on `s` vertices with `c_v ≥ 0` leaves at `v`, order `n ≥ 2s`: `d_k = Σ_j g_j(c) C(n−2s, k−j)`, `g_j` of degree ≤ 1 in each `c_v`. | Proved; AI review of `1bb2bbe`, no gap found. The factor `(λ+2)^{p−q}` is in print (Collins 1993, Cor. 7). |
| S2 | `det(2xI − Q(c)) = Σ_A c^A (2x+2)^{s−a} (2x)^a det(2x I_Ā − P − 1_A1ᵀ − 11_Aᵀ − (a/2x)J)`. | Proved; AI review of `1bb2bbe`, no gap found; checked exactly on the 47 trees with 2 to 8 vertices. |
| S3 | The product of all `c_v` occurs only in `g_{s−1}` and `g_s`, with coefficients `s` and `s + 3`, for every skeleton. | Proved (Graham–Pollak, Graham–Lovász inverse); AI review of `1bb2bbe`, no gap found. |
| S4 | If the polynomial `r_A` has a non-negative half-gamma expansion, the coefficient of `c^A` in `d_m − d_{m−1}` is `≥ 0` for every order `n ≥ 2s`. | Proved; AI review of `1bb2bbe`, no gap found. |
| S6, S7 | `r_A = (s−1) x det(I − KG)` with matrices of size `|Ā| + 1`; `r_A = Φ_B [a(1+x) + (3 + 3H − 2e_B)x] − x² zᵀ adj(I + xL_B) z`, `B = Ā`, `Φ_B = det(I + xL_B)`. So `r_A` depends only on `s` and `L[Ā, Ā]` (locality, for every tree and subset). | Proved; AI review of `1805bca`, no gap found; checked exactly on the 47 trees (7,820 subsets). |
| S8, S9 | Closed forms of `r_A` for one and for two missing vertices, with positive half-gamma coefficients: the requirement of Γ for `|Ā| ≤ 2`, every tree. | Proved; AI review of `1805bca`, no gap found. |
| C | A non-negative combination of `x^e(1+x)^j`, `e + j ≤ d`, `2e + j ≥ d` (the cone `C_d`), has a non-negative half-gamma expansion of degree `d`. | Proved; AI review of `1805bca`, no gap found. |
| S10 | If `Ā` is a non-empty independent set: an explicit decomposition of `r_A` in `C_{t+1}`, using `a − H ≥ 1`. **The requirement of Γ holds for every tree and every `A` with independent complement.** | Proved; AI review of `1805bca`, no gap found. |
| F, F′ | `det(I + x(L_T + diag ν)) ∈ C_j` for a tree on `j` vertices and integer `ν ≥ 0`, `ν ≠ 0`; hence `Φ_B ∈ C_t` and the positive term of S7 is in `C_{t+1}` whenever `1 ≤ |A| ≤ s − 1`. | Proved; AI review of `5622d19` (no gap in this statement), recheck of the revision `7acd425`. |
| S11 | Contracting the components of `S[A]`: `r_A^S = r_{A′}^{S′} + (a − a′)(1+x)Φ_B`. So Γ⁺ (Γ with `|A| ≥ 1`) for all trees follows from its case `A` independent. | Proved; AI review of `5622d19` (no gap in this statement), recheck of the revision `7acd425`. |
| S5 | Conditional on Property Γ for `S`: Hypothesis V for `S` and, by L4, `d_m − d_{m−1} ≥ min_p D_n((n−s)e_p)` for every `S(c)` of order `n ≥ 2s`. | Proved; AI review of `9499572`, no gap found. It gives no positivity by itself. |
| Γ, finite | Property Γ holds for the 47 trees with 2 to 8 vertices; hence (S4) Hypothesis V for those skeletons and every order `n ≥ 2s`. | Computer-assisted; AI review of `9499572` with an independent recomputation from the definition (7,448 pairs), no gap found. |
| S12 | `r_A = r_V Φ_B − pᵀ adj(I + xL_B) p`, `p = 1 + xτ_B`, `r_V = s + (s+3)x` (third form). | Proved; AI review of `b0a4dbe`, no gap found. |
| S13 | For `1 ≤ a ≤ s − 1`: `zᵀ adj(I + xL_B) z = Σ y_i² Π_{l≠i}(1 + λ_l x)` (director's identity; non-negative coefficients); `r_A` has degree `t + 1`, leading coefficient `κ det L_B`, `κ = s + 3 − τ_BᵀL_B^{−1}τ_B ≥ 4` (equality iff `a = 1`; `κ = 4 + 2/(1ᵀP_A^{−1}1)`); **all roots of `r_A` are real and negative**. | Proved; AI review of `b0a4dbe`, no gap found; exact check on the 47 trees (7,726 subsets). |
| S14 | Component form: `r_A = [(1+4x) + e_A(1+x)]Φ_B + Σ_i R(T_i, ν) Π_{l≠i} Φ(T_l, ν)`, `R(T, ν) = (N + j − 1)(1+x)Φ − pᵀadj(M)p`. So Γ⁺ follows from **Γ_c**: `R(T, ν) ∈ C_{j+1}` for every weighted tree. | Proved; AI review of `b0a4dbe`, no gap found. |
| G, S15 to S17 | The adjugate of `I + x(L_T + diag ν)` when a leaf is removed and when a weight is raised; `R(T, ν) = (1+x)R(T−w, ν) + x[ν_u(1+x)Ψ + Σ R_i P_i]` for a leaf of weight 0; `R(T, ν) = R(T, ν⁰) + nE + n(n−1)xΦ(T−w, ν+e_u)` for a leaf of weight `n`. | Proved; AI review of `b0a4dbe`, no gap found; exact check on 111,768 leaves (G) and 17,856 leaves (S17). |
| S18 | Induction on a leaf: under Γ_c for smaller trees, `R(T, ν) ∈ C_{j+1}` if the leaf has weight 0, or if `E = R(T, ν⁰+e_w) − R(T, ν⁰) ∈ C_{j+1}`. So Γ_c follows from statement (E). | Proved (conditional); AI review of `b0a4dbe`, no gap found. |

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

Not registered: R1, L2, L4 and S1 to S4 are tools or steps (S3 and S4 are the
evidence of MD-0010); Γ⁺ (the extension of Γ to `|A| = 1`) is an observation on
the 47 small trees, recorded under MD-0012; Γ_c and (E) are stated in MD-0014
and not registered as conjectures of their own; E1 reproduces a published
verification; Q1, Q2 are questions.

## Conjectures and hypotheses of this investigation

**Conjecture Γ — open (MD-0010).** For every tree `S` on `s ≥ 2` vertices and
every `A ⊆ V(S)` with `|A| ≥ 2`, the polynomial
`r_A(x) = −2^{2−s} x det(2x I_Ā − P − 1_A1ᵀ − 11_Aᵀ − (|A|/2x)J)` is a
non-negative combination of `x^e (1+x)^{d−2e}` (`2e < d`) and `x^e`
(`d ≤ 2e ≤ 2d`), `d = s − |A| + 1`. Statement and consequences:
[`notes/skeleton-identity.md`](notes/skeleton-identity.md).

- True for `A = V` and every tree (S3: `r_V = s(1+x) + 3x`). Verified exactly
  for every subset of the 47 trees with 2 to 8 vertices.
- **Session 6 (MD-0011): true for every tree and every `A` whose complement
  is independent (S10) or has at most two vertices (S8, S9).** For a star
  skeleton this covers every `A` containing the centre.
- **Session 6 (MD-0012): reduced to `A` independent**, provided the statement
  is extended to `|A| = 1` (Γ⁺; exact on the 47 trees, 325 subsets with one
  element). Remaining case: `A` independent and at least one edge inside
  `V ∖ A`. In the form of S7 the positive term is always in `C_{t+1}` (F′);
  the conjecture is about absorbing `−x² zᵀ adj(I + xL_B) z`, and S10 shows
  that the absorption uses a tree inequality (`a − H ≥ 1`), not only algebra.
- **Session 7 (MD-0013, MD-0014).** Every `r_A` has only real negative roots
  (so positive, log-concave coefficients); this does not give the expansion.
  Γ⁺ follows from **Γ_c** (one weighted tree: `R(T, ν) ∈ C_{j+1}`), exact for
  all 29,336 weighted trees with `j ≤ 7`, weights 0 to 2. Γ_c follows, by
  induction on a leaf, from **(E)**: for every tree all of whose leaves have
  weight `≥ 1` there is a leaf `w` with
  `E = R(T, ν⁰ + e_w) − R(T, ν⁰) ∈ C_{j+1}` (`ν⁰`: `ν` with `ν_w = 0`). The
  step for a leaf of weight 0 is proved. `E ∈ C_{j+1}` in all 17,856 cases
  computed (`j ≤ 6`, weights 0 to 2; every admissible leaf).
- It does not depend on the order `n` nor on the leaf numbers.
- If true for `S`: Hypothesis V for `S` and every order (S4), and by L4, for
  every tree `S(c)` with `n ≥ 2s`,
  `d_m − d_{m−1} ≥ min_p D_n((n−s) e_p)` — the lower half of the conjecture
  is reduced to the trees "skeleton plus one star".
- Not covered: trees with fewer leaves than non-leaf vertices; the trees
  "skeleton plus one star" themselves (positive in all computed cases, orders
  up to 100); the upper half.

**Hypothesis V — open in general (MD-0009).** The mixed second partials of
`D_n` are non-negative for caterpillars with any number `s` of spine vertices.
Now a consequence of Γ for path skeletons: computer-assisted for `s ≤ 8` and
every order (unreviewed). The analogue for `d_m − d_{m+1}` is false from
`s = 4`.

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

**Hypothesis A(i) — refuted.** *Statement:* `ρ_k(T) ≥ ρ_k(S_n)` for every tree
`T` of order `n` and every `0 ≤ k ≤ ⌊n/2⌋ − 1`. *Motivation:* it holds for all
522,956 trees of order 4 to 19, and at `k = ⌊n/2⌋ − 1` it would have given the
lower half of the conjecture from Collins's theorem on stars.
*Refutation:* at order 20 it fails for exactly 10 trees, all at the last index
`k = 9` and all close to the star: the nine double stars `S(a, 18−a)`,
`1 ≤ a ≤ 9`, and the spider with two legs of length 2 and fifteen of length 1.
Explicit counterexample: the double star `S(9,9)`,

`q(S(9,9)) = 10255/10791 ≈ 0.950329 > q(S_20) = 94/99 ≈ 0.949495`,

confirmed by two implementations that share no code
(`test_refutation_of_star_minimality_at_order_20_by_both_methods`). Double stars were
compared with the star for every order from 6 to 41: some double star has a
larger `q` than the star at every even order from 20 to 40 and at every odd
order from 29 to 41, and at no other order in that range. All these values of
`q` stay below 1, so the Collins–Shor conjecture itself is not affected.

*What this teaches:* at those orders the star is not the extremal tree for the
lower bound, so a proof of the lower bound cannot go through comparison with
the star at the critical index. Do not retry star-comparison at `k = ⌊n/2⌋ − 1`.
Whether star-minimality holds for `k ≤ ⌊n/2⌋ − 2` at larger orders is untested.

*How it was found:* the pattern was perfect on every tree up to order 17; the
falsification test on sampled trees of order 24 and above broke it within
minutes.

**Session 7 — three dead ends for Γ.** (1) *Roots.* `r_A` is real-rooted
(S13), but real negative roots do not imply membership in `C_d`
(`1 + 5x/2 + x²/2`); pairing roots `μ_i μ_{d+1−i} ≥ 1` cannot work for long
paths (the smallest eigenvalue of `L_B` tends to 0; not computed). (2)
*Darroch's theorem on the mode* applied to `(1+x)^K r_A`: the index needed by
S4 is the upper central one, where a symmetric polynomial has equality, so a
bound on the mean decides nothing (for `A = V` the mean is below the index and
the inequality still holds); real roots with mean equal to half the degree are
not enough (`(1+0.6x)²(1+3x)(1+x)²`, hand computation). (3) *Termwise
absorption in S17.* The part `E* = 2x²π′ + (3x+2x²)Φ′ + 3x²Ψ` of `E` is not in
the cone by itself (star with three leaves of weights 2, 2, 3 and centre of
weight 0: leading coefficient `−6`); a proof of (E) must use
`xR(T′, ν+e_u)` or `(1+x)Φ(T, ν⁰)`.

## Counterexamples and observations

- No counterexample to the Collins–Shor conjecture was found.
- For odd `n` the lower-bound margin is wide; for even `n` it tends to 0.
- For `10 ≤ n ≤ 19` the star minimizes `ρ_k` exactly for `k ≤ ⌊n/2⌋ − 1`.
- The relative margin `1 − d_{m−1}/d_m` behaves like a constant over `n` in
  every family examined (double stars: about `1/n` for even and `3/n` for odd
  order; `K(a,b,c)`: `≈ 0.0024` at order 302). Not proved; which shape
  minimizes it at a given order was not analysed.
- In every case computed, the tree "skeleton plus one star" with the smallest
  `d_m − d_{m−1}` has the star at a vertex of large degree or central
  position; no rule was extracted.

## Dependency map

```
Collins–Shor, lower half  (⇔ d_{m−1} < d_m, by R1 [Lean])
  trees S(c) with at least as many leaves as non-leaf vertices (n ≥ 2s):
    ⇐ S1 (closed form)                               [proved, AI-reviewed]
    ⇐ L4 (vertex principle)                          [proved, AI-reviewed; core in Lean]
    ⇐ S4 [AI-reviewed] + Property Γ for the skeleton S [conjecture in general (MD-0010)]
        Γ for A with V∖A independent or |V∖A| ≤ 2     [proved for every tree, AI-reviewed (MD-0011)]
        Γ⁺ ⇐ Γ⁺ for A independent                     [S11 (MD-0012)]
        Γ⁺ ⇐ Γ_c (one weighted tree)                  [S14 (MD-0014)]
        Γ_c ⇐ (E): raising a leaf weight 0 → 1         [S18 (MD-0014); (E) OPEN, exact for j ≤ 6, weights ≤ 2]
        Γ for A independent, an edge inside V∖A       [OPEN; all 47 skeletons with s ≤ 8 by computation]
    ⇐ d_{m−1} < d_m for "skeleton plus one star"     [OPEN in general; s ≤ 3 paths done (T1 to T3)]
  trees with fewer leaves than non-leaf vertices     [OPEN; no approach]
  special cases with complete candidate proofs, both halves, peak exactly m:
    diameter 3: T1;  caterpillars of diameter 4: T2, T3, P_5;  stars: Collins 1989 (not read)

Collins–Shor, upper half
  ⇐ R1
  ⇐ Hypothesis A(ii) at k = p_n                      [OPEN; k = 0 proved (L2)]
  ⇐ Collins 1989: peak of P_n ≤ ⌈n − n/√5⌉           [cited via arXiv:1507.02341; not read]
  no mechanism from the skeleton expansion           [Property Γ says nothing about it]
```

## Decisions

- 2026-11-26. CJ-0001 selected first (highest score; statement readable from
  the primary source; exact, cheap computations). Strong reading of ties.
- 2026-11-26 (director). MD-0006, MD-0007 and MD-0008 stay candidate theorems
  until their validity and originality are adequately assessed; an AI review
  is not that assessment. Every description of T2 states `a, b, c ≥ 1`.
  Formalization accompanies the investigation (`autoresearch.md`, step 9).
  The session budget of 60 minutes is binding, review and verification
  included (session 5 onwards).
- 2026-11-26 (director, session 5). Priority: a general mechanism (Hypothesis
  V and beyond), not further fixed-spine theorems; O4 is a tool.
- 2026-11-26 (sessions 3, 4). T3 is a separate record, so that the statement
  of MD-0007 stays fixed. Reviews by a model other than the author's. Notes
  are left unchanged after a review; corrections are made in one revision
  that is then rechecked.
- 2026-11-26 (session 5). Conjecture Γ is registered as the general statement;
  S1 to S4 are its supporting lemmas and are not registered separately. No
  adversarial review was run in session 5: the budget went to the mathematics,
  the literature audit and the formalization.
- 2026-11-26 (session 6). The results of the session are written in two new
  notes, so that `notes/skeleton-identity.md` and then
  `notes/skeleton-locality.md` stay byte-identical to the revisions that were
  reviewed; the defects listed by the reviews are left for one revision per
  file, followed by a recheck. MD-0011 and MD-0012 are registered as
  candidates (`candidate-proof`); nothing was promoted. The statement of
  MD-0010 is unchanged; Γ⁺ is not registered as a conjecture of its own.
- 2026-11-26 (director, session 7). The classifications of MD-0011 and
  MD-0012 are approved as they stand; verified commits may be pushed to
  `research` only; the automatic CI trigger works. (Session 7.) Their novelty
  field moved from `unknown` to `preliminary-search-completed` after the
  first audit, which is not a claim of originality. S12 to S18 are written
  in a new note; Γ_c and (E) are not registered as separate conjectures.
- Earlier decisions (budget overrun of session 1, widening of O1, deferral of
  the rerun of orders 21 to 23) are in the journal.

## Open obligations

Details and history: [`notes/obligations.md`](notes/obligations.md).

1. **Literature.** Session 5 found the closed formulas of T1 and T3, and the
   balanced case of T2, in print (see Sources); T1 to T3 must cite them, and
   Lemma D1 is to be recorded as known. Session 6 read Collins 1993 in the
   author's manuscript (no peak statement, no subset expansion; only the
   balanced double star, with a formula that fails as printed there — see the
   dossier) and thesis pages 14 to 38 (nothing on the peak). L3 and S1 must
   cite Collins 1993, Corollary 7. Still unread: the Discrete Appl. Math. 2019
   paper (the publisher refused automated access; a person can probably open
   it: DOI `10.1016/j.dam.2018.10.018`), the published version of Collins
   1993, Collins 1989, thesis pages 1–3, 6–11, 50–77, Graham–Lovász
   pp. 68–79; no search of MathSciNet, zbMATH, Google Scholar. Session 7: a
   first audit for MD-0011 and MD-0012 found no identical statement and
   three sources to cite — Bapat–Kirkland–Neumann 2005, Thm 2.4 (**the
   determinant behind S3 is in print**: `det(D + xJ)` for weighted trees) and
   Thm 2.1; Richman–Shokrieh–Wu, arXiv:2411.11488, Thms A and 4.4 (principal
   minors of `D` through a Laplacian minor on the complement). Unread and
   most likely to contain Lemma F: matching polynomials of forests, Laplacian
   coefficients of trees (Mohar 2007, Zhou–Gutman, arXiv:2410.14112),
   Chebotarev–Shamis. **No search at all for MD-0013 and MD-0014.**
2. **T1, T2, T3: one revision of the three notes** (citations of the published
   formulas; defects E3 to E5 of the review of T3; the last wording changes of
   T1 and T2, which no one but the author has checked), followed by one
   recheck. A human reader, or a different vendor's model, before any
   promotion.
3. **Reviews of sessions 5 and 6.** S1 to S4 (`1bb2bbe`), S6 to S10 with
   Lemma C (`1805bca`), Lemma F, F′ and S11 (`5622d19`; one paragraph of the note had a gap, repaired and rechecked at `7acd425`): AI reviews, no gap found; reports under
   `reviews/`. Owed: (a) one revision of `notes/skeleton-identity.md` for the
   four defects of its review (the degree bound of `r_A` needs its one-line
   cofactor argument; `γ_A` at `x = 0`; `M_A` used for two matrices; `p_∅`),
   and one of `notes/skeleton-locality.md` (the count 1,011 should be 1,010
   for S9 as stated; "Property Γ" used for one subset; the remark "has to use
   the tree"; a redundant proviso), each followed by a recheck
   (`notes/gamma-reduction.md` was already revised and rechecked; two trivial
   defects of wording remain in it); (b) L4, S5 and
   the Γ computation were reviewed in session 7 (no gap); their defects are
   owed one revision: `vertex-principle.md` (L3′ is superseded by S1; "V(s)
   not proved for any s ≥ 4" is stale), `skeleton-identity.md` (S1 was checked
   with zero leaf numbers only for `s ≤ 5`; "orders up to 100" has no
   committed evidence; "at least two non-leaf vertices"; stale review status),
   the result file's provenance, test coverage (`s ≤ 5` only); (b′) S12 to
   S18 were reviewed at `b0a4dbe` (no gap); `notes/gamma-components.md` is
   left byte-identical to that revision and is owed one revision for three
   defects of wording ("two elementary facts" lists three; statement (E)
   must say "there is a leaf `w`" and quantify `ν`; the opening paragraph
   calls a sufficient condition a reduction and a family of polynomials "one
   polynomial") and for the observation (E″) below, then a recheck; (c) a human reader, or a model of another vendor,
   before any promotion; (d) the two classical formulas (Graham–Pollak,
   Graham–Lovász inverse) have not been compared with the printed papers.
4. **E2** (orders 21 to 23): independent recomputation, about 34 minutes,
   needs the director's approval of the budget. MD-0001 stays `partial-result`.
5. Comparison of the code with Table II of Graham–Lovász (cheap, not done).
6. The audit's identifications of L1 and L3 as known, and the two specialised
   statements of R1 about `M`, are unreviewed.
7. **Formalization.** In Lean: the general form of R1 and the one-dimensional
   core of L4. An independent comparison of the Lean statements with the
   written ones is owed. Next: L4 in `s` variables; Proposition S4 (binomial
   inequalities only).
8. `spine3.py` and `results/spine3.json` still say "spine length 3" in their
   description strings (the result file is evidence and is not edited).
9. This file is above its target of 400 lines since session 7: compact it
   (the dead ends and the details of O7 belong in a note), and add a
   regression test for `component_form.py` (none exists).

## Remaining obstacles

- Γ is now reduced to (E) (session 7), which is open: in
  `E = (1+x)Φ(T, ν⁰) + xR(T′, ν+e_u) + E*` the linear form
  `π′ = e_uᵀ adj(M(T′, ν)) p` inside `E*` has no sign, and `E*` alone can leave
  the cone. S16 expresses `2xπ′` as a difference of values of `R`.
- Conjecture Γ is proved only when `V ∖ A` is independent or has at most two
  vertices. When `V ∖ A` contains edges, `Φ_B` and `adj(I + xL_B)` are sums
  over rooted spanning forests of `S[B]`, and the termwise weight count of
  S10 fails (a vertex of `B` with no neighbour in `A` gives a factor of
  weight 0 when it is an isolated root); S9 with adjacent vertices was done by
  explicit inequalities, not by a grouping that generalizes.
- Even with Γ, the trees "skeleton plus one star" must be handled, uniformly
  in the skeleton; and trees with few leaves are out of reach of the closed
  form.
- The upper half has no mechanism: A(ii) is unproved beyond `k = 0`, and the
  expansion over subsets does not control the coefficients with `|A| ≤ 1`.

## Next step

**Objective O7.** Prove statement (E) of `notes/gamma-components.md` through
the stronger statement **(E″)**, which involves no `R`. Since
`E = x R(T′, ν + e_u) + [(1+x)Φ(T, ν⁰) + E*]` and `Φ(T, ν⁰) = (1+x)Φ′ + xΨ`,
(E) follows (under the induction hypothesis of S18) from

> (E″) for every tree `T′` on `j′ ≥ 1` vertices, every vertex `u` and every
> integer weight `ν ≥ 0`, `ν ≠ 0`:
> `F(T′, ν, u) := (1 + 5x + 3x²)Φ′ + (x + 4x²)Ψ + 2x²π′ ∈ C_{j′+2}`,

`Φ′ = Φ(T′, ν)`, `Ψ = adj(M(T′, ν))_{uu}`, `π′ = e_uᵀ adj(M(T′, ν)) p`.
(E″) is an observation of session 7: exact for the 17,856 rooted cases with
`j′ ≤ 5`, weights 0 to 2 (`component_form.py`, field
`part3_E_minus_xR_not_in_cone`), and in a trial with weights up to 4 and
`j′ ≤ 4` (31,460 cases, not stored). It is not in the note and not reviewed.

What session 7 found about (E″), **on paper and in a scratch computation
only** (all weighted rooted trees with at most 5 vertices, weights 0 to 2,
every root and every leaf `w ≠ u`: 10,089 cases, 0 failures; script not
stored, nothing written up or reviewed). For a leaf `w ≠ u` of `T` with
neighbour `v` and weight `n`, `m = 1 + (1+n)x`, `θ = x(1+nx)`, by Lemma G2:

- `v ≠ u`: `F(T, ν, u) = m F(T − w, ν, u) + θ F(T_c, ν + e_{v_c}, u) Π_{l≠c} Φ_l − 4n x⁴ adj(M(T − w, ν))_{uv}`
  (`T_c` the component of `T − w − v` containing `u`);
- `v = u`: `F(T, ν, u) = m F(T − w, ν, u) + [x + (5+n)x² + (3+5n)x³ − n x⁴] Ψ_u(T − w)`;
- `F` is affine in `n`, with slope
  `x [F(T − w, ν + e_v, u) − 2x³ adj(M(T − w, ν))_{uv}]`;
- `F(T, ν, u) ∈ C_{j+2}` held in every case, **also for `ν = 0`**, and so did
  the slope.

So for `n = 0` every term is in the cone under the induction hypothesis
(`x(1 + 5x + 3x²) ∈ C_4`), and **(E″) — hence (E), Γ_c, Γ⁺ and Conjecture Γ —
would follow from the slope statement**

> (S) for every tree `T` on `j ≥ 1` vertices, all vertices `u, v` and every
> integer weight `ν ≥ 0`:
> `x [F(T, ν + e_v, u) − 2x³ adj(M(T, ν))_{uv}] ∈ C_{j+3}`,

with (E″) stated for all `ν ≥ 0`, zero included. `adj(M)_{uv}` is
`x^{dist(u,v)}` times the product of the polynomials `Φ` of the components
off the path from `u` to `v`. First step of the next session: put these
identities and (S) into `component_form.py` (weights up to 4, `j ≤ 6`), then
attack (S) by the same leaf removal. The expression in (S) is again affine in
the weight of a leaf `w ≠ u`; its slope subtracts two adjugate entries, so
the induction needs a family indexed by a multiset of vertices `v`, and
leaves that belong to the multiset have weight at least 1 — that is where the
session stopped.

Cheap exact computations that remain: Γ_c for `j = 8`; (E) and (E″) with
weights up to 6; the trees "skeleton plus one star" as polynomials in `m`.

Owed first by default: obligations 1 to 3.

## Sources

- G. Aalipour et al., arXiv:1507.02341 — read in full (TeX source; twice by reviewers).
- R. L. Graham, L. Lovász, Adv. Math. 29 (1978) 60–88 — pp. 60–67, 80–86 read.
- L. Hogben, C. Reinhart, arXiv:2103.00647 — pp. 5–12 read.
- A. Abiad et al., arXiv:2206.07561; R. Jana et al., arXiv:2407.03309 — read in full.
- J. Xue, R. Liu, H. Jia, Filomat 30:6 (2016) 1559–1565 — read in full (session 5): Lemma 2.3, the distance characteristic polynomial of the double star.
- J. S. do Nascimento, D.Sc. thesis, COPPE/UFRJ 2018 — pp. vi–ix, 4–5, 12–49, 78–79 read (sessions 5 and 6): Props. 3.2.1, 3.2.6, 3.2.9; Section 3.1 (multiplicity of −2, number of distinct eigenvalues).
- J. S. do Nascimento, R. R. Del-Vecchio, M. A. A. de Freitas, Discrete Appl. Math. 266 (2019) 141–152 — not read (not accessible in session 6; DOI `10.1016/j.dam.2018.10.018`).
- K. L. Collins, Factoring distance matrix polynomials, Discrete Math. 122 (1993) 103–112 — read in full in the author's manuscript (9 pages, supplied by the director, kept outside the repository; session 6); the published version not seen.
- K. L. Collins, Discrete Appl. Math. 25 (1989) 27–35 — not accessible; second-hand only.
- R. Bapat, S. J. Kirkland, M. Neumann, Linear Algebra Appl. 401 (2005) 193–209 — read in full by the auditor (session 7): Thm 2.1, Thm 2.4.
- H. Richman, F. Shokrieh, C. Wu, arXiv:2411.11488v2 — read by text extraction, proofs not read (session 7).
- R. Merris, J. Graph Theory 14 (1990) 365–369 — read in full by the auditor (session 7).
- Full list with access notes: the dossier.
