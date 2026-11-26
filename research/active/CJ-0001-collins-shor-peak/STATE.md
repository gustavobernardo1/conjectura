# CJ-0001 — Collins–Shor conjecture — investigation state

Last updated: 2026-11-26 (session 8). This file is the current truth about the
investigation and is meant to be sufficient, on its own, for a new agent to
continue. It was compacted in sessions 5 and 8: details are in the notes it
links. Proofs: [`notes/lemmas.md`](notes/lemmas.md) (R1, L1 to L3),
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
theorems** (director's decision of 2026-11-26). The status of every
registered contribution is in
[`research/discoveries.json`](../../discoveries.json), not here.

Formal (Lean, `formalization/Conjectura/Research/CollinsShorPeak/`): 14 registered theorems; the latest receipt is under `verification/receipts/`. In Lean: the general form of R1; the discrete core of L4, since session 8 **in any finite number of variables** (`vertex_principle_discrete`: a function on integer points with the exchange inequality `f(c+e_i−e_k) + f(c+e_k−e_i) ≤ 2f(c)` on the slice is, at every point of the slice, at least its value at some vertex `λ + (S−Σλ)e_p`); the cone `C_d` over real polynomials (`HalfGammaCone`) with `C_d·C_e ⊆ C_{d+e}`, `x·C_d ⊆ C_{d+1}`, `x·C_d ⊆ C_{d+2}`, `(1+x)·C_d ⊆ C_{d+1}`, `x(1+x)·C_d ⊆ C_{d+3}`, and Lemma C. **Not formalized:** the step from a multi-affine polynomial with non-negative mixed partials to the exchange inequality (so L4 as written is not formalized); the equality of the inductive cone with the explicit non-negative sums; anything about trees, determinants or `r_A`. The Lean statements were compared with the written ones by the formalizing agent and the author of the session only.

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
| S12, S13 | `r_A = r_V Φ_B − pᵀ adj(I + xL_B) p`; degree `t + 1`, leading coefficient `κ det L_B`, `κ = s + 3 − τ_BᵀL_B^{−1}τ_B ≥ 4` (equality iff `a = 1`; `κ = 4 + 2/(1ᵀP_A^{−1}1)`); **all roots of `r_A` are real and negative**. | Proved; reviewed (`b0a4dbe`). The bound on `κ` and the identity with `P_A` are **implied by Richman–Shokrieh–Wu, arXiv:2411.11488** (session 8 audit; bridging step unreviewed). |
| S14 to S18, G | Component form `r_A = [(1+4x) + e_A(1+x)]Φ_B + Σ_i R(T_i, ν) Π_{l≠i} Φ(T_l, ν)`, so Γ⁺ follows from **Γ_c** (`R(T, ν) ∈ C_{j+1}`, `ν ≠ 0`); the adjugate when a leaf is removed or a weight raised (Lemma G); recurrences for `R` (S15 to S17); Γ_c follows from statement **(E)** by induction on a leaf (S18). | Proved (S18 conditional); reviewed (`b0a4dbe`). |
| S19, S20 | Rooted state `(Ψ, H, G, Ω, R)` of `(T, ν, u)`: `ΨR = Φ[ν_u(1+x)Ψ + Ω] − π_u²` (★); rules for raising the root weight, a new root, and merging two rooted trees — in the merge the only negative term of `R` is `−2G_1G_2`, and `G = (1+2x)Ψ − π_u` has non-negative coefficients; the increment of `R` at any vertex, `Δ_u = [(1+2x)² + 2xν_u]Ψ + Σ_c Λ(T_c, ν, c)P_c`; at a new leaf, `E = (1+2x)²Φ(T, ν+e_u) + Λ = xR(T, ν+e_u) + F`. | Proved; reviewed (`59c47f7`), no gap found. |
| S21 | **(E″) and (S) of session 7 are false.** On the star with centre `u` of weight `n_0` and leaf weights `n_i`: `[x^{q+3}]F = Π(1+n_i)(4 + n_0 − Σ n_i/(1+n_i))`. Smallest failures found: (E″) at 6 vertices (five leaves of weight 4), (S) at 5 vertices (leaf weights 2, 3, 4, 4). | Proved (leading coefficients) and exact computation with an independent checker; reviewed (`59c47f7`), counterexamples confirmed by the reviewer's own code. |
| S22 | If **(Λ)** (`Λ(T, ν, u) ∈ C_{j+2}` for every rooted weighted tree, `ν ≥ 0` arbitrary) holds, then `R` is non-decreasing in every weight at every vertex in the cone order; in particular (E) for every leaf, Γ_c, Γ⁺ and Γ. | Proved (conditional); reviewed (`59c47f7`), no gap found. |

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

Not registered: R1, L2, L4 and S1 to S4 are tools or steps (S3 and S4 are the
evidence of MD-0010); Γ⁺ is an observation on the 47 small trees, recorded
under MD-0012; Γ_c and (E) are stated in MD-0014, and (Λ) in MD-0015, and are
not registered as conjectures of their own; E1 reproduces a published
verification; Q1, Q2 are questions.

## Conjectures and hypotheses of this investigation

**Conjecture Γ — open (MD-0010).** For every tree `S` on `s ≥ 2` vertices and
every `A ⊆ V(S)` with `|A| ≥ 2`, the polynomial
`r_A(x) = −2^{2−s} x det(2x I_Ā − P − 1_A1ᵀ − 11_Aᵀ − (|A|/2x)J)` is a
non-negative combination of `x^e (1+x)^{d−2e}` (`2e < d`) and `x^e`
(`d ≤ 2e ≤ 2d`), `d = s − |A| + 1`. Statement and consequences:
[`notes/skeleton-identity.md`](notes/skeleton-identity.md).

- True for `A = V` (S3), for every `A` whose complement is independent (S10)
  or has at most two vertices (S8, S9), and for every subset of the 47 trees
  with 2 to 8 vertices (exact).
- Every `r_A` has only real negative roots (S13); this does not give the
  expansion.
- It does not depend on the order `n` nor on the leaf numbers. If true for
  `S`: Hypothesis V for `S` and every order (S4), and by L4 the lower half of
  Collins–Shor for the trees `S(c)`, `n ≥ 2s`, is reduced to the trees
  "skeleton plus one star".
- **Chain of sufficient conditions** (each arrow a proved implication; only
  S11 is an equivalence):
  `Γ ⇐ Γ⁺ ⇐ Γ⁺ for A independent (S11) ⇐ Γ_c (S14) ⇐ (E) (S18) ⇐ (Λ) (S22)`.
  - **Γ_c**: `R(T, ν) ∈ C_{j+1}` for every weighted tree, `ν ≠ 0`. Exact for
    all 29,336 weighted trees with `j ≤ 7`, weights 0 to 2; for 11,073 rooted
    stars with heavy leaves and 3,213 rooted random trees (session 8).
  - **(E)**: for every tree all of whose leaves have weight `≥ 1` there is a
    leaf `w` with `E = R(T, ν⁰ + e_w) − R(T, ν⁰) ∈ C_{j+1}`. No failure known
    (17,856 cases of session 7; every counterexample to (E″) and (S)).
  - **(Λ)** (session 8, replaces (E″)): `Λ(T, ν, u) = x[(1−x)Φ + 2xΨ + R(T, ν+e_u) − 2xG] ∈ C_{j+2}`
    for every rooted weighted tree, zero weight included; equivalently
    `E − (1+2x)²Φ(T′, ν+e_u) ∈ C_{j′+2}` at a new leaf. **Open**; no failure
    in 4,395 + 11,085 + 3,269 rooted trees (`results/rooted-state.json`), nor
    in two scratch runs (29,295 rooted stars with up to 7 leaves and weights
    up to 8; 8,198 rooted random trees; not stored).
    The reviewer's own search (stars with equal leaf weights up to about
    30, at most 6 leaves; 2,462 rooted cases) found none either. Brooms,
    spiders, double stars and paths with heavy weights are **untested**
    beyond the random sample.
  - **(E″), (S)**: false (S21). The family indexed by multisets of vertices
    that session 7 proposed is abandoned.
- **What the application needs is weaker (Γ_w)**: S4 uses `r_A` only through
  `([x^c] − [x^{c−1}])(1+x)^L r_A ≥ 0`, `L ≥ d − 1`, `c = ⌈(L+d)/2⌉`. That
  cone is strictly larger than `C_d` (`1 + x + x²`), but it is not known to
  be closed under products, which every proof so far uses.
- Not covered by Γ: trees with fewer leaves than non-leaf vertices; the trees
  "skeleton plus one star" themselves (positive in all computed cases); the
  upper half.

**Hypothesis V — open in general (MD-0009).** The mixed second partials of
`D_n` are non-negative for caterpillars with any number `s` of spine vertices.
A consequence of Γ for path skeletons: computer-assisted for `s ≤ 8` and
every order. The analogue for `d_m − d_{m+1}` is false from `s = 4`.

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
Collins–Shor, lower half  (⇔ d_{m−1} < d_m, by R1 [Lean])
  trees S(c) with at least as many leaves as non-leaf vertices (n ≥ 2s):
    ⇐ S1 (closed form)                               [proved, AI-reviewed]
    ⇐ L4 (vertex principle)                          [proved, AI-reviewed; Lean: see Status]
    ⇐ S4 [AI-reviewed] + Property Γ for the skeleton S [conjecture in general (MD-0010)]
        (S4 needs only Γ_w, strictly weaker than Γ)   [observation, session 8]
        Γ for A with V∖A independent or |V∖A| ≤ 2     [proved for every tree, AI-reviewed (MD-0011)]
        Γ ⇐ Γ⁺ ⇐ Γ⁺ for A independent                 [S11 (MD-0012)]
        Γ⁺ ⇐ Γ_c (one weighted tree)                  [S14 (MD-0014)]
        Γ_c ⇐ (E): raising a leaf weight 0 → 1         [S18 (MD-0014); (E) OPEN]
        (E) ⇐ (Λ)                                      [S22 (MD-0015); (Λ) OPEN, exact on the ranges above]
        (E) ⇐ (E″) ⇐ (S)                               [(E″), (S) FALSE: S21 (MD-0015)]
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

- 2026-11-26. CJ-0001 selected first. Strong reading of ties.
- 2026-11-26 (director). MD-0006 to MD-0008 stay candidate theorems until
  their validity and originality are adequately assessed; an AI review is not
  that assessment. Every description of T2 states `a, b, c ≥ 1`.
  Formalization accompanies the investigation. The session budget of 60
  minutes is binding, review and verification included.
- 2026-11-26 (director, session 5). Priority: a general mechanism, not
  further fixed-spine theorems.
- 2026-11-26 (sessions 3 to 7). Reviews by a model other than the author's.
  A note is left byte-identical to the revision that was reviewed; its
  defects are corrected in one revision that is then rechecked; new results
  go in a new note. Γ⁺, Γ_c and (E) are not registered as conjectures of
  their own.
- 2026-11-26 (director, sessions 7 and 8). The classifications of MD-0011 to
  MD-0014 are approved as they stand. Verified commits may be pushed to
  `research` only.
- 2026-11-26 (session 8). (Λ) is stated inside MD-0015 and not registered as
  a conjecture of its own, like Γ_c and (E). MD-0013 is not split: its items
  (ii) (bound) and (iv) are recorded as implied by Richman–Shokrieh–Wu in its
  novelty search; splitting it is a decision for the director.
- Earlier decisions (budget overrun of session 1, widening of O1, deferral of
  the rerun of orders 21 to 23, the notes of sessions 5 and 6) are in the
  journal.

## Open obligations

Details and history: [`notes/obligations.md`](notes/obligations.md) (the
full text of items 1 to 8 as of session 7 is there).

1. **Literature.** T1 to T3 must cite the published formulas; L3 and S1 must
   cite Collins 1993, Cor. 7; S3 must cite Bapat–Kirkland–Neumann 2005,
   Thm 2.4. **Session 8:** MD-0013 items (ii) (bound) and (iv) must cite
   Richman–Shokrieh–Wu, arXiv:2411.11488 (Thms A, 2.4, 4.4, 4.6) — the
   auditor's bridging step is unreviewed, and that paper was read by text
   extraction only; S13(d) has a shorter proof by a definite pencil (auditor's
   remark, unreviewed); Lemma G1 is classical; `Φ(T, ν)` is the principal
   Laplacian matching polynomial of arXiv:2410.14112. Still unread: the
   sources listed in the dossier's two audit sections; no search of
   MathSciNet, zbMATH, Google Scholar. No search for MD-0015.
2. **T1, T2, T3: one revision of the three notes**, then one recheck. A human
   reader, or a different vendor's model, before any promotion.
3. **Revisions owed after reviews** (each followed by a recheck):
   `skeleton-identity.md`, `skeleton-locality.md`, `vertex-principle.md`,
   `gamma-components.md` (three defects of wording), two trivial defects in
   `gamma-reduction.md`, `rooted-calculus.md` (seven defects of wording
   listed by its review: degrees in the proof of S21 when all weights are 0;
   "strictly larger" for Γ_w argued only for `d ≥ 2`; Remark 2 ignores parts
   of zero weight; two sentences after S21; the result files were produced
   on a dirty tree at `9069d88`; (★) and S20(d) checked by an unstored
   script), the result file's provenance and
   test coverage of `skeleton_structure.py`. A human reader, or a model of
   another vendor, before any promotion. The two classical formulas
   (Graham–Pollak, Graham–Lovász inverse) have not been compared with the
   printed papers.
4. **E2** (orders 21 to 23): independent recomputation, about 34 minutes,
   needs the director's approval of the budget. MD-0001 stays `partial-result`.
5. Comparison of the code with Table II of Graham–Lovász (cheap, not done).
6. The audit's identifications of L1 and L3 as known, and the two specialised
   statements of R1 about `M`, are unreviewed.
7. **Formalization.** Done: see Status. Owed: an independent
   comparison of all the registered Lean statements with the written ones;
   the bridge from multi-affine polynomials to the exchange inequality (L4
   as written); the inductive cone against explicit non-negative sums, and a
   non-membership example. Next: Proposition S4 (binomial inequalities for
   the generators of `C_d`), then Lemma F.
8. `spine3.py` and `results/spine3.json` still say "spine length 3" in their
   description strings (the result file is evidence and is not edited).

## Remaining obstacles

- Γ is reduced to (E), and (E) to (Λ); both are open. In every form the
  obstruction is the same: one negative term built from
  `G = (1+2x)Ψ − π_u ≥ 0` — `−4x²G` in `E` (S20(b)), `−2G_1G_2` in the merge
  rule (S19(d)), `−(1−g)²` in `Λ/(xΨ)` (S20(d)) — to be absorbed by `R`,
  which grows quadratically in the weights but is negative at `ν = 0`.
- Even with Γ, the trees "skeleton plus one star" must be handled, uniformly
  in the skeleton; and trees with few leaves are out of reach of the closed
  form.
- The upper half has no mechanism: A(ii) is unproved beyond `k = 0`.

## Next step

**Objective O8.** Prove statement (Λ) of
[`notes/rooted-calculus.md`](notes/rooted-calculus.md), or find a
counterexample. Start from the recursion over the branches at `u`
(`rooted-calculus.md`, "Where the difficulty is"):

`Λ(T, ν, u) = x[R(T, ν) + (1−x)Φ − 2xG + ((1+2x)² + 2x(1+ν_u))Ψ] + x Σ_c Λ(T_c, ν, c) P_c`.

1. The first bracket `Λ⁰ := R(T, ν) + (1−x)Φ − 2xG + ((1+2x)² + 2x(1+ν_u))Ψ`
   was tested in a scratch run of session 8 (not stored): `xΛ⁰ ∈ C_{j+2}`
   failed in 8 of the 4,395 rooted weighted trees with `j ≤ 5`, weights 0 to
   2, and in 7 of 18,009 rooted stars with at most 5 leaves and weights up to
   8 — **in every failing case `ν = 0`** (smallest: the path on 2 vertices,
   `xΛ⁰ = x + 3x²`). So on that range (Λ) splits into two statements:
   **(Λ⁰)** `xΛ⁰ ∈ C_{j+2}` for every rooted weighted tree with `ν ≠ 0`, which
   contains no `Λ` and no `Ω`; and (Λ) for trees with zero weights, a family
   with no parameters besides the rooted tree. First action: add the check
   of (Λ⁰) next to `B3` in `cone_checks` of `rooted_state.py`, store the
   run, and test it on stars, brooms, spiders and double stars with weights
   up to 50.
2. Then expand `Λ⁰` with the merge rule S19(d) for `R` over the branches at
   `u`: the cross terms are `−2G_cG_{c′}` between two branches. Look for the
   inequality between `G_c` and `(R_c, Ω_c, Φ_c)` of one branch that absorbs
   them (on stars: `G^ = 2nx²`, `Ω^ = n(1+5x+4x²) + n²x` for a leaf of weight
   `n`; the cross term `8n n′x⁴` must come from the terms `n²x`).
3. Search wider for a counterexample to (Λ) before investing in a proof:
   weights up to 50 on stars, brooms, spiders and double stars with up to 12
   vertices (minutes of exact computation).

Cheap exact computations that remain: Γ_c for `j = 8`; the trees "skeleton
plus one star" as polynomials in `m`.

Owed first by default: obligations 1 to 3.

## Sources

- G. Aalipour et al., arXiv:1507.02341 — read in full (TeX source; twice by reviewers).
- R. L. Graham, L. Lovász, Adv. Math. 29 (1978) 60–88 — pp. 60–67, 80–86 read.
- L. Hogben, C. Reinhart, arXiv:2103.00647 — pp. 5–12 read.
- A. Abiad et al., arXiv:2206.07561; R. Jana et al., arXiv:2407.03309 — read in full.
- J. Xue, R. Liu, H. Jia, Filomat 30:6 (2016) 1559–1565 — read in full: Lemma 2.3.
- J. S. do Nascimento, D.Sc. thesis, COPPE/UFRJ 2018 — pp. vi–ix, 4–5, 12–49, 78–79 read: Props. 3.2.1, 3.2.6, 3.2.9; Section 3.1.
- J. S. do Nascimento, R. R. Del-Vecchio, M. A. A. de Freitas, Discrete Appl. Math. 266 (2019) 141–152 — not read (DOI `10.1016/j.dam.2018.10.018`).
- K. L. Collins, Discrete Math. 122 (1993) 103–112 — read in full in the author's manuscript (supplied by the director, kept outside the repository); the published version not seen.
- K. L. Collins, Discrete Appl. Math. 25 (1989) 27–35 — not accessible; second-hand only.
- R. Bapat, S. J. Kirkland, M. Neumann, Linear Algebra Appl. 401 (2005) 193–209 — read in full by the auditor: Thm 2.1, Thm 2.4.
- H. Richman, F. Shokrieh, C. Wu, arXiv:2411.11488v2 — read by text extraction, proofs not read (sessions 7 and 8): Thms A, 2.4, 4.4, 4.6, D.
- R. Merris, J. Graph Theory 14 (1990) 365–369 — read in full by the auditor.
- Wan, Wang, Wang (surnames as given by the auditor), arXiv:2410.14112 — read by text extraction (session 8): eq. (1.4), Thms 1.2, 3.1.
- K. Castillo, I. Zaballa, arXiv:2103.13739 — pp. 1–2 read by the auditor (session 8): Thm 2.1.
- Full list with access notes: the dossier.
