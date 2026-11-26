# CJ-0001 — Collins–Shor conjecture — investigation state

Last updated: 2026-11-26 (session 5). This file is the current truth about the
investigation and is meant to be sufficient, on its own, for a new agent to
continue. It was compacted in session 5: details that were here are in the
notes it links. Proofs: [`notes/lemmas.md`](notes/lemmas.md) (R1, L1 to L3),
[`notes/double-stars.md`](notes/double-stars.md) (T1),
[`notes/spine3.md`](notes/spine3.md) (T2),
[`notes/diameter4-caterpillars.md`](notes/diameter4-caterpillars.md) (T3),
[`notes/vertex-principle.md`](notes/vertex-principle.md) (L4, Hypothesis V),
[`notes/skeleton-identity.md`](notes/skeleton-identity.md) (S1 to S4,
Property Γ). Obligations in detail: [`notes/obligations.md`](notes/obligations.md).
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
originality is not assessed. What was written in session 5 (S1 to S4,
Property Γ) has been reviewed by no one. The status of every registered
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
| L4 | Vertex principle: a function of degree ≤ 1 in each variable with non-negative mixed second partials attains its minimum over the integer points of a slice `c ≥ λ`, `Σ c = S` at a point with one coordinate above its lower bound. | Proved, not reviewed. Its one-dimensional core is formalized in Lean (see Status). |
| S1 | Skeleton `S` on `s` vertices with `c_v ≥ 0` leaves at `v`, order `n ≥ 2s`: `d_k = Σ_j g_j(c) C(n−2s, k−j)`, `g_j` of degree ≤ 1 in each `c_v`. | Proved, not reviewed; checked against direct determinants. |
| S2 | `det(2xI − Q(c)) = Σ_A c^A (2x+2)^{s−a} (2x)^a det(2x I_Ā − P − 1_A1ᵀ − 11_Aᵀ − (a/2x)J)`. | Proved, not reviewed; checked exactly on the 47 trees with 2 to 8 vertices. |
| S3 | The product of all `c_v` occurs only in `g_{s−1}` and `g_s`, with coefficients `s` and `s + 3`, for every skeleton. | Proved (Graham–Pollak, Graham–Lovász inverse), not reviewed. |
| S4 | If the polynomial `r_A` has a non-negative half-gamma expansion, the coefficient of `c^A` in `d_m − d_{m−1}` is `≥ 0` for every order `n ≥ 2s`. | Proved, not reviewed. |
| Γ, finite | Property Γ holds for the 47 trees with 2 to 8 vertices; hence Hypothesis V for those skeletons and **every** order. | Computer-assisted (S4 and exact expansions), not reviewed. |

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

Not registered: R1, L2, L4 and S1 to S4 are tools or steps (S3 and S4 are the
evidence of MD-0010); E1 reproduces a published verification; Q1, Q2 are
questions.

## Conjectures and hypotheses of this investigation

**Conjecture Γ — open (MD-0010).** For every tree `S` on `s ≥ 2` vertices and
every `A ⊆ V(S)` with `|A| ≥ 2`, the polynomial
`r_A(x) = −2^{2−s} x det(2x I_Ā − P − 1_A1ᵀ − 11_Aᵀ − (|A|/2x)J)` is a
non-negative combination of `x^e (1+x)^{d−2e}` (`2e < d`) and `x^e`
(`d ≤ 2e ≤ 2d`), `d = s − |A| + 1`. Statement and consequences:
[`notes/skeleton-identity.md`](notes/skeleton-identity.md).

- True for `A = V` and every tree (S3: `r_V = s(1+x) + 3x`). Verified exactly
  for every subset of the 47 trees with 2 to 8 vertices.
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
    ⇐ S1 (closed form)                               [proved, unreviewed]
    ⇐ L4 (vertex principle)                          [proved, unreviewed; core in Lean]
    ⇐ S4 + Property Γ for the skeleton S             [Γ: all 47 skeletons with s ≤ 8, computer-assisted;
                                                      conjecture in general (MD-0010); A = V proved (S3)]
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
- Earlier decisions (budget overrun of session 1, widening of O1, deferral of
  the rerun of orders 21 to 23) are in the journal.

## Open obligations

Details and history: [`notes/obligations.md`](notes/obligations.md).

1. **Literature.** Session 5 found the closed formulas of T1 and T3, and the
   balanced case of T2, in print (see Sources); T1 to T3 must cite them, and
   Lemma D1 is to be recorded as known. Still unread: Collins 1989 and 1993
   ("Factoring distance matrix polynomials", which treats double stars —
   first priority), the Discrete Appl. Math. 2019 paper of do Nascimento,
   Del-Vecchio and de Freitas, pages 16 to 37 and 50 to 77 of the 2018 thesis,
   Graham–Lovász pp. 68–79; no search of MathSciNet, zbMATH, Google Scholar.
2. **T1, T2, T3: one revision of the three notes** (citations of the published
   formulas; defects E3 to E5 of the review of T3; the last wording changes of
   T1 and T2, which no one but the author has checked), followed by one
   recheck. A human reader, or a different vendor's model, before any
   promotion.
3. **Session 5 is unreviewed**: S1 to S4, the Γ computation, and L4. An
   independent review of `notes/skeleton-identity.md` and of
   `skeleton_structure.py` comes before anything is built on them.
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

## Remaining obstacles

- Conjecture Γ has no proof and no conceptual explanation beyond `A = V`. The
  reformulation through `P^{−1} = −L/2 + ττᵀ/(2(s−1))` and forest
  polynomials (remark in `notes/skeleton-identity.md`) is a direction, not a
  result.
- Even with Γ, the trees "skeleton plus one star" must be handled, uniformly
  in the skeleton; and trees with few leaves are out of reach of the closed
  form.
- The upper half has no mechanism: A(ii) is unproved beyond `k = 0`, and the
  expansion over subsets does not control the coefficients with `|A| ≤ 1`.

## Next step

**Objective O5.** Property Γ for subsets missing one vertex. For a tree `S`
on `s` vertices, a vertex `w` and `A = V ∖ {w}` (`d = 2`): compute
`r_A(x) = ρ_0 (1+x)² + σ_1 x + σ_2 x²` in closed form and decide whether
`ρ_0, σ_1, σ_2 ≥ 0` for every tree.

How: `r_A = −2^{2−s} x det(2x e_w e_wᵀ − M)`, `M = P + 1_A1ᵀ + 11_Aᵀ + ((s−1)/2x)J`,
so `det = det(−M) + 2x det(−M[V∖w])`. `M` is `P` plus a matrix of rank at most
2 in the span of `1` and `e_w`; with `P^{−1} = −L/2 + ττᵀ/(2(s−1))`
everything reduces to `(P^{−1})_{ww} = −deg(w)/2 + τ_w²/(2(s−1))`,
`P^{−1}1 = τ/(s−1)` and `det P`. The expected outcome is a formula in `s`
and `deg(w)` only; compare it with the expansions stored by
`skeleton_structure.py` (extend its output to print `(ρ, σ)` for these
subsets) before writing any proof. If the formula is non-negative, this is the
second layer of Γ proved for all trees, and it shows what the induction on
`|Ā|` would have to carry.

Falsification test: the stored expansions for the 47 trees with 2 to 8 vertices — the closed form
must reproduce every one of them.

In parallel, as cheap exact computations: the trees "skeleton plus one star"
as polynomials in `m` for the 47 skeletons (a finite check that would give the
lower half for every tree with at most 8 non-leaf vertices and at least 16
vertices, given Γ and L4); extend Γ to `s = 9, 10`.

Owed first by default: obligations 1 to 3.

## Sources

- G. Aalipour et al., arXiv:1507.02341 — read in full (TeX source; twice by reviewers).
- R. L. Graham, L. Lovász, Adv. Math. 29 (1978) 60–88 — pp. 60–67, 80–86 read.
- L. Hogben, C. Reinhart, arXiv:2103.00647 — pp. 5–12 read.
- A. Abiad et al., arXiv:2206.07561; R. Jana et al., arXiv:2407.03309 — read in full.
- J. Xue, R. Liu, H. Jia, Filomat 30:6 (2016) 1559–1565 — read in full (session 5): Lemma 2.3, the distance characteristic polynomial of the double star.
- J. S. do Nascimento, D.Sc. thesis, COPPE/UFRJ 2018 — pp. vi–ix, 4–5, 12–15, 38–49, 78–79 read (session 5): Props. 3.2.1, 3.2.6, 3.2.9.
- J. S. do Nascimento, R. R. Del-Vecchio, M. A. A. de Freitas, Discrete Appl. Math. 266 (2019) 141–152 — not read.
- K. L. Collins, Discrete Appl. Math. 25 (1989) 27–35 and Discrete Math. 122 (1993) 103–112 — not accessible; second-hand only.
- Full list with access notes: the dossier.
