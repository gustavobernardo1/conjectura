# CJ-0001 — Collins–Shor conjecture — investigation state

Last updated: 2026-11-26 (session 4). This file is the current truth about the
investigation and is meant to be sufficient, on its own, for a new agent to
continue. Proofs are in [`notes/lemmas.md`](notes/lemmas.md),
[`notes/double-stars.md`](notes/double-stars.md),
[`notes/spine3.md`](notes/spine3.md) and
[`notes/diameter4-caterpillars.md`](notes/diameter4-caterpillars.md); the
exploration of a general mechanism is in
[`notes/vertex-principle.md`](notes/vertex-principle.md); computations are
in [`experiments/CJ-0001-collins-shor-peak/`](../../../experiments/CJ-0001-collins-shor-peak/README.md);
the literature record is the dossier
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

Nothing in this file is a claimed result of the project. Novelty of every
observation below is **unknown**, except where it is marked as known or where
a bounded search is recorded in the registry.

Session 2 produced a candidate proof of the conjecture for double stars
(T1 below). The catalogue status stays `active-investigation`: a status is not
promoted in the session that produced the claim, and T1 has not been read by a
mathematician.

An independent AI review of the notes at revision `e34acfc` is in
[`reviews/2026-11-26-claude-fable-5-2.md`](reviews/2026-11-26-claude-fable-5-2.md).
It is a review by the same model family in a fresh context, not a human
review, and the catalogue status of CJ-0001 stays `not-reviewed` because the
notes were edited afterwards. Four registry records carry `ai-reviewed`.
MD-0002, MD-0003 and MD-0004 rest on that review: the statement and proof of
L1 and of L3 are identical to the reviewed revision (compared on 2026-11-26),
and the reviewer recomputed the counterexample to A(i) with its own code.
MD-0006 (T1) rests on a second review, of revision `5e5ef14`:
[`reviews/2026-11-26-claude-fable-5-2-T1.md`](reviews/2026-11-26-claude-fable-5-2-T1.md).
Both are AI reviews by the same model family as the author, in fresh
contexts, and nothing more.

Session 3 produced a candidate proof of the conjecture for the caterpillars
`K(a,b,c)` with `a, b, c ≥ 1` (T2 below, MD-0007), reviewed at revision
`74cb5bb` by a different model (`claude-opus-5-5`, fresh context):
[`reviews/2026-11-26-claude-opus-5-5-T2.md`](reviews/2026-11-26-claude-opus-5-5-T2.md),
no gap found within stated scope. It is an AI review by a model of the same
vendor. The catalogue status is unchanged.

Session 4 produced a candidate proof for the caterpillars `K(a,0,c)` (T3,
MD-0008), reviewed at `d2eb9ac` by `claude-opus-5-5`
([`reviews/2026-11-26-claude-opus-5-5-T3.md`](reviews/2026-11-26-claude-opus-5-5-T3.md),
no gap found within stated scope); an exploration of a mechanism for any
spine length (Lemma L4 and Hypothesis V, MD-0009, a conjecture); and the
first Lean formalization for this problem (the general form of R1). The
formal status of CJ-0001 is `partial`: only that lemma about sequences is
formalized, nothing about trees. By the director's decision of 2026-11-26,
T1, T2 and T3 stay candidate theorems.

## Established results

| ID | Statement | Level | Evidence |
| --- | --- | --- | --- |
| E1 | The conjecture (strong reading) holds for all trees of order 3 to 20: 1,346,022 trees, 0 violations. | Verified computationally, exact. Reproduces the claim of the source ("all trees of order at most 20"). | `results/exhaustive-03-20.json` |
| E2 | The conjecture (strong reading) holds for all trees of order 21, 22 and 23: 22,596,335 trees, 0 violations. | Verified computationally, exact. Beyond the range reported in the source. | `results/exhaustive-21-23.json` |
| E3 | In E1 and E2 every tree count equals OEIS A000055, `d_0 = n − 1` on every tree (Graham–Pollak), every sequence is unimodal, and the only tie is one tree of order 13 (maximum at indices 6 and 7, inside the interval). | Verified computationally, exact. | same files |
| E4 | In orders 3 to 23 the peak is always `⌊n/2⌋` or `⌊n/2⌋ + 1`; the star attains the minimum and the path the maximum. | Verified computationally, exact. | same files |
| R1 | The lower bound for `T` is equivalent to `d_{m−1} < d_m`; the upper bound is equivalent to `M ≥ n−2` or `d_{M+1} < d_M`. | Proved here (short; uses log-concavity from the source). AI review of `e34acfc`: no gap found; restated in general form afterwards, not re-reviewed. | `notes/lemmas.md` |
| L1 | `ℓ_T(x) = (n−1) det(I + xL) − x τᵀ adj(I + xL) τ`. | **Known:** a rewriting of Graham–Lovász (1978), eqs. (10)–(12), found by the literature audit of session 2 (the rewriting itself is unreviewed). Derived here from Graham–Pollak and the Graham–Lovász inverse formula (their Lemma 1, p. 66); checked exactly on all trees of order 3 to 9. AI review of `e34acfc`: no gap found. | `notes/lemmas.md`, `tests/test_cj0001_distpoly.py`, dossier |
| L2 | `d_1(T) = 2n² − 6 − Σ deg(v)²`; hence `ρ_0(S_n) ≤ ρ_0(T) ≤ ρ_0(P_n)` with equality only for the star and the path. | **Known:** the formula for `d_1` is in the source (proof of Theorem 3.3), as the review pointed out, and is eq. (6) of Graham–Lovász (1978). Re-derived here; checked exactly on all trees of order 3 to 11. AI review of `e34acfc`: no gap found. | `notes/lemmas.md`, tests |
| L3 | Caterpillar with spine length `s` and all `c_i ≥ 1`: `det(xI − D) = (x+2)^{n−2s} det(xI − Q)` for an explicit `2s × 2s` matrix `Q`. | **Known:** a direct special case of Theorem 3.3 of Hogben–Reinhart, arXiv:2103.00647 (twin partitions), found by the literature audit of session 2. Proved here (equitable partition); every coefficient checked exactly against the direct computation on ten caterpillars. AI review of `e34acfc`: no gap found. | `notes/lemmas.md`, `near_star_families.py`, dossier |
| T1 | Double star `S(a,b)`, `a, b ≥ 1`, `n = a+b+2`, `m = ⌊n/2⌋`: `d_{m−1} < d_m`, and `d_{m+1} < d_m` when `m+1 ≤ n−2`. Hence `m` is the only maximizing index and the conjecture holds for every tree of diameter 3. With `t = ab`: for `n = 2m`, `(m−1)m(m+1)(d_m − d_{m−1}) = C(2m−4, m−2)[3t m(m+1) + 2(2m−1)(2m−3)(3m−5)]`; for `n = 2m+1`, `m(m+1)(m+2)(d_m − d_{m−1}) = C(2m−3, m−1)[10t(m+1)(m+2) + 16m(2m−1)(2m+1)]`. | **Candidate proof**, written in session 2, from L3 with `s = 2` and Theorem 2.1 of the source. Closed forms and inequalities checked exactly on all 10,000 double stars with `a + b ≤ 200`; whole sequences against the direct determinant on 404 of them. AI review of `5e5ef14` (same model family, fresh context): no gap found within stated scope; eight minor discrepancies of presentation. Novelty: no earlier statement found within a bounded search; Collins (1989) not read. | `notes/double-stars.md`, `results/double-stars.json`, `double_stars.py`, tests |
| T2 | Caterpillar `K(a,b,c)`: spine `v_1 v_2 v_3` carrying `a, b, c ≥ 1` leaves, `n = a+b+c+3 ≥ 6`, `m = ⌊n/2⌋`: `d_{m−1} < d_m` and `d_{m+1} < d_m`. Hence `m` is the only maximizing index and the conjecture holds for every caterpillar of diameter 4 whose central vertex carries a leaf. With `u = a+c`, `v = ac`, each of the four differences (two parities, two sides) is a positive factor times `vK(m,u) + R(m,u)` with `K > 0`; the minimum over the family is at `v = u−1` and, by concavity in `u`, at `K(1, n−5, 1)` or `K(1, 1, n−5)`. | **Candidate proof**, written in session 3, from L3 with `s = 3`, Fact 1.1 and Theorem 2.1 of the source. Two steps (the `6 × 6` determinant and the reduction to `vK + R`) are computer-assisted polynomial identities. Identities and inequalities checked exactly on all 2,238,725 such caterpillars with `a+b+c ≤ 300` (from the closed form); whole sequences against the direct determinant on 621. AI review of `74cb5bb` (`claude-opus-5-5`, fresh context): no gap found within stated scope; both computer-assisted steps recomputed with the reviewer's code from distance matrices; eight defects of record and presentation. Novelty: nothing found in a small bounded search. | `notes/spine3.md`, `results/spine3.json`, `spine3.py`, tests |
| T3 | Caterpillar `K(a,0,c)`: spine `v_1 v_2 v_3`, `a, c ≥ 1` leaves at `v_1`, `v_3`, none at `v_2`, `a + c ≥ 3`, `n = a+c+3 ≥ 6`, `m = ⌊n/2⌋`: `d_{m−1} < d_m` and `d_{m+1} < d_m`. Corollary, conditional on T2: for every caterpillar of diameter 4 (`K(a,b,c)` with `a, c ≥ 1`, `b ≥ 0`; `P_5` by direct computation) the only maximizing index is `⌊n/2⌋`. | **Candidate proof**, written in session 4: the formula of Lemma C1 of `spine3.md` stays valid at `b = 0` for `n ≥ 6` (Lemma C1′), the identities of Lemma C2 hold with `u = n−3`, and `K > 0`, `H > 0` there. Relies on the computer-assisted identities of `spine3.md`. Formula against the direct determinant on 402 trees; identities and inequalities on all 89,999 trees with `a+c ≤ 600`. AI review of `d2eb9ac` (`claude-opus-5-5`, fresh context): no gap found within stated scope; six defects of record and presentation. Novelty: nothing found in a small bounded search. | `notes/diameter4-caterpillars.md`, `results/diameter4.json`, `diameter4.py`, tests |
| L4 | Vertex principle: a polynomial of degree at most 1 in each variable whose mixed second partials are non-negative on `x ≥ λ` attains its minimum over the integer points `c ≥ λ` with a given coordinate sum at a point with a single coordinate above its lower bound. | Proved here (short induction; concavity along `e_i − e_k`). Not reviewed. Elementary; novelty not examined. | `notes/vertex-principle.md` |
| R1 (general form), formal | For a positive log-concave sequence `a_0, …, a_r` and `1 ≤ j ≤ r`: every maximizing index is `≥ j` if and only if `a_{j−1} < a_j`. | **Formalized in Lean 4** (four registered theorems, a non-vacuity witness; axioms `propext`, `Classical.choice`, `Quot.sound` only). The comparison of the Lean statement with the written one was made by the formalizing agent and by the session's author, not by an independent reviewer. A lemma about sequences: positivity and log-concavity of the `d_k` are not formalized. | `formalization/Conjectura/Research/CollinsShorPeak/LogConcavePeak.lean`, `formalization/registry.json`, the latest receipt under `verification/receipts/` |

Result files are under `experiments/CJ-0001-collins-shor-peak/results/`.

### Global identifiers

Nine findings are registered as contributions in
[`research/discoveries.json`](../../discoveries.json). The local identifiers
keep their meaning. An `MD` identifier establishes identity only: the status of
each record (mathematical, formal, novelty, review) is in the registry and in
[`research/INDEX.md`](../../INDEX.md), not here.

| Local | Global | Type |
| --- | --- | --- |
| E2 (with E1 and the guards E3) | MD-0001 | computational finding |
| L1 | MD-0002 | identity (rediscovered) |
| L3 | MD-0003 | lemma (rediscovered) |
| Refutation of A(i) | MD-0004 | counterexample |
| A(ii) | MD-0005 | conjecture |
| T1 | MD-0006 | theorem |
| T2 | MD-0007 | theorem |
| T3 | MD-0008 | theorem |
| Hypothesis V | MD-0009 | conjecture |

Not registered, and why: E1 alone reproduces a published verification; E4 is a
pattern of small orders that supports MD-0001; R1 is a routine consequence of
log-concavity; L2 is known (its formula is in the source); Q1 is an observed
limit that has not been examined; Q2 is the lower half of the conjecture
itself, not a separate statement. Hypothesis A(i) has no record of its own:
the contribution is its refutation. L4 is an elementary lemma used as a tool; the
corollary of T3 is a consequence of MD-0007, MD-0008 and one direct computation;
the observation on the top coefficient (below) has not been examined enough to
be stated as a conjecture.

## Conjectures and hypotheses of this investigation

**Hypothesis A(ii) — open.** For every tree `T` of order `n` and every
`0 ≤ k ≤ min(p_n, n−3)`, where `p_n` is the largest maximizing index of the
path: `ρ_k(T) ≤ ρ_k(P_n)`. (`ρ_k` is defined for `k ≤ n−3`; when `p_n = n−2`,
which happens at `n = 4`, the upper bound on the peak is vacuous.)

- Evidence: holds for all 1,346,021 trees of order 4 to 20 (exact), and for
  10,000 pseudo-random trees of orders 24, 30, 40, 60, 90 from five random
  models (exact arithmetic, seed 20261126).
  `results/ratio-extremality-04-17.json`, `-18-20.json`, `-sampled.json`.
- Proved for `k = 0` (L2).
- Consequence, if true (for `p_n ≤ n−3`): at `k = p_n`, `ρ_{p_n}(T) ≤ ρ_{p_n}(P_n) < 1`, so by R1
  the peak of `T` is at most the peak of the path. Together with Collins's
  theorem on paths (as reported in the source: the path's peak is the floor or
  the ceiling of `n − n/√5`) this would give the upper half of the conjecture.
- The index range matters: the path does not maximize `ρ_k` at every index.
  The set of indices at which it does is recorded for each order in the result
  files (`indices_where_path_maximises_rho`).

**Hypothesis V — open (MD-0009).** For a caterpillar with `s` spine vertices
and leaf numbers `c = (c_1, …, c_s)`, and a fixed order `n ≥ 2s`, let
`D_n(c) = Σ_j g_j(c)[C(n−2s, m−j) − C(n−2s, m−1−j)]`, which is multi-affine in
`c` and equals `d_m − d_{m−1}` on the slice `Σ c_i = n − s`. Hypothesis:
`∂²D_n/∂c_i∂c_k ≥ 0` for all `i < k` whenever `c_1, c_s ≥ 1` and the inner
`c_j ≥ 0`. Exact statement, evidence and consequences:
[`notes/vertex-principle.md`](notes/vertex-principle.md).

- Evidence: a sufficient certificate holds for every pair, `2 ≤ s ≤ 8`, every
  order from `2s` to 200 (`results/mixed-partials.json`). True for `s = 2`
  (from T1) and, by a computer-assisted identity checked by
  `mixed_partials_s3.py` and not reviewed, for `s = 3` and every order.
- Consequence, if true for a given `s` (by L4, and given the extension of L3
  to empty leaf classes): the lower inequality `d_{m−1} < d_m` for all
  caterpillars with `s` spine vertices and at least `s` leaves follows from
  its validity on the trees obtained from the path `P_{s+2}` by attaching all
  remaining leaves to one inner vertex — at most `⌈s/2⌉` one-parameter
  families. In the range computed all these are positive and the minimum is
  at the middle vertex.
- For `s = 3` this reproduces the lower inequalities of T2 and T3.
- The analogous statement for the upper difference `d_m − d_{m+1}` is false
  from `s = 4` on, and for `s ≥ 6` some of those trees have `d_{m+1} ≥ d_m`.
- Observation, uniform in `s` (exact for `2 ≤ s ≤ 8`): the product
  `c_1 ⋯ c_s` occurs only in `g_{s−1}` and `g_s`, with coefficients `s` and
  `s + 3`; then its coefficient in `D_n` is `3·C(2k,k)/(k+1)` for even order
  and `(2s+6)·C(2k+1,k+1)/(k+2)` for odd order, `k = m − s`. Not proved for
  general `s`.

**Question Q1 — open.** For balanced caterpillars with a fixed spine length `s`,
exact values at `n = 10³, 10⁴, 10⁵, 10⁶` suggest `n (1 − q) → 6/(2s+3)`
(`1.2000, 0.8571, 0.6667, 0.5455, …` for `s = 1, 2, 3, 4, …`). Numerical
observation from exact values; no proof attempted. For `s = 1` and `s = 2` the
closed forms of T1 and of the star make the limit a routine computation, which
has not been written out.

**Question Q2 — open, and it is the lower half of the conjecture for even n.**
Is `q(T) < 1` for every tree of even order? The closest trees found are
balanced caterpillars whose spine length grows slowly with `n`:

| `n` | closest balanced caterpillar | `1 − q` |
| ---: | --- | ---: |
| 100 | spine 3 | 8.45 × 10⁻³ |
| 1,000 | spine 7 | 5.10 × 10⁻⁴ |
| 10,000 | spine 15 | 2.65 × 10⁻⁵ |
| 100,000 | spine 33 | 1.29 × 10⁻⁶ |

All margins are positive (exact comparison), but they shrink faster than `1/n`.
Only balanced caterpillars with spine length up to 80 were examined at these
orders (`results/near-star-families.json`).

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
- Counterexample to Hypothesis A(i): see above.
- For odd `n` the lower-bound margin is wide (for the star,
  `q ≈ 0.83` at `n = 17`); for even `n` it tends to 0. The even case is the
  delicate one.
- For `10 ≤ n ≤ 19` the set of indices at which the star minimizes `ρ_k` over
  all trees is exactly `{0, …, ⌊n/2⌋ − 1}`.
- Caterpillars of diameter 4 with no leaf at the centre, `K(a,0,c)`: now T3.
- Among the `K(a,b,c)` of even order with `a+b+c ≤ 300`, the smallest relative
  margin `1 − d_{m−1}/d_m` recorded by `spine3.py` is `≈ 0.002386` at
  `K(59,180,60)` (order 302). The reviewer of T2 saw `≈ 0.00275` at
  `K(109,1,108)` (order 221). Which shape minimizes the relative margin at a
  given order was not analysed; it is not the same question as the minimum of
  `vK + R` in T2.

## Dependency map

```
Collins–Shor, upper half
  ⇐ R1 (proved here, unreviewed)
  ⇐ Hypothesis A(ii) at k = p_n            [OPEN; k = 0 proved (L2)]
  ⇐ Collins 1989: peak of P_n ≤ ⌈n − n/√5⌉  [cited via arXiv:1507.02341; paper not read]

Collins–Shor, lower half
  ⇐ R1
  ⇐ d_{m−1}(T) < d_m(T) for every tree      [OPEN; no reduction known]
       odd n:  wide margin in all data
       even n: margin → 0 along near-star caterpillars (Q2)
       diameter ≤ 2 (stars): Collins 1989, Theorem 1 [cited via arXiv:1507.02341]
       diameter 3 (double stars): T1 [candidate proof; both halves; ⇐ L3, Theorem 2.1 of the source]
       diameter 4, caterpillars K(a,b,c) with a, b, c ≥ 1: T2 [candidate proof; both halves;
            computer-assisted; ⇐ L3, Fact 1.1 and Theorem 2.1 of the source]
       diameter 4, caterpillars K(a,0,c), a + c ≥ 3: T3 [candidate proof; both halves;
            ⇐ Lemmas C1, C2 of spine3.md at b = 0]; P_5 by direct computation
       diameter 4, not caterpillars: open; unbounded number of twin classes
       caterpillars with s spine vertices and at least s leaves, lower half only:
            ⇐ L4 (proved here, unreviewed)
            ⇐ Hypothesis V(s)                       [OPEN; s = 2 from T1; s = 3 computer-assisted,
                                                     unreviewed; certificate for s ≤ 8, n ≤ 200]
            ⇐ L3 with empty inner classes           [written out for s = 3 only]
            ⇐ positivity on ⌈s/2⌉ one-parameter families   [s ≤ 3 done; s = 4 ← next step (O4)]
  R1, general form: formalized in Lean (LogConcavePeak.lean)
```

## Decisions

- 2026-11-26. Selected as the first investigation: highest score in the ranking
  (80.2), with the second (79.2) and third (78.1) within the noise of the
  model; chosen also because its statement could be read from the primary
  source the same day and its computations are exact and cheap.
- 2026-11-26. Strong reading of ties adopted (see conventions).
- 2026-11-26. The computation budget of 30 minutes was exceeded (about 41
  minutes of recorded computation) to let the order-23 run finish. This was the
  agent's decision, taken without prior approval by the director; it is
  recorded in the journal for the director's review.
- 2026-11-26 (session 2). Objective O1 was widened during the session from the
  lower inequality to the exact location of the peak, because the second
  inequality costs only a sign argument once the coefficients are explicit.
- 2026-11-26 (session 2). L1 and L3 are recorded as rediscovered (registry
  records MD-0002 and MD-0003) on the strength of the literature audit. They
  remain tools of the investigation and are not results of the project.
- 2026-11-26 (session 2). The rerun of orders 21 to 23 was deferred: it needs
  about 34 minutes of computation and the director's approval.
- 2026-11-26 (director). MD-0006 (T1) and MD-0007 (T2) stay candidate theorems
  until their mathematical validity and their originality have been
  adequately assessed; an AI review is not that assessment. The presentation
  defects found by the two reviews are to be corrected, with the provenance
  of the reviews preserved. Every description of T2 states the condition
  `a, b, c ≥ 1`. Lean formalization is to accompany the investigation
  progressively (`autoresearch.md`, step 9).
- 2026-11-26 (session 4). O3 was recorded as a separate theorem (T3, MD-0008)
  with its own notes, not as a change to T2: the statement of MD-0007 stays
  fixed and its review stays bound to it. The first Lean target was the
  general form of R1, because every result of the investigation uses it and
  its statement is stable. The formal status of CJ-0001 was set to `partial`.
- 2026-11-26 (session 3). The open obligations were deferred in favour of O2
  (recorded in the journal). T2 was reviewed by a model other than the
  author's (`claude-opus-5-5`). `notes/spine3.md` was at first left unchanged
  after the review; it and `notes/double-stars.md` were then revised in
  presentation at the director's request (obligations 2 and 8).

## Open obligations

1. **Literature.** The audit of session 2 is in the dossier. Still unread:
   Collins (1989) and her 1986 thesis (publisher and repositories refused
   automated access; everything said about them is second-hand); Graham–Lovász
   pp. 68–79 and 87–88; do Nascimento, Del-Vecchio and de Freitas (2019), "The
   distance matrix of caterpillar", which bears on L3 and possibly on T1; the
   journal versions; MathSciNet, zbMATH, Google Scholar and MathOverflow were
   not searched. For MD-0004 and MD-0005 only one query was made.
2. **Review of T1.** AI review of `5e5ef14` (same model family, fresh context):
   no gap found within stated scope; eight minor discrepancies of
   presentation. No mathematician has read it. Before T1 is promoted it needs
   a human reader or a review by a different model, and the reading of
   Collins (1989). The defects (a) to (g) listed by the review were corrected
   in `notes/double-stars.md` on 2026-11-26 (its *Revision history* says
   what changed); no statement, formula or step of the proof was changed. The
   review was made on the earlier text. A recheck of that revision (`1c38662`)
   by `claude-opus-5-5`,
   [`reviews/2026-11-26-claude-opus-5-5-recheck-T1-T2.md`](reviews/2026-11-26-claude-opus-5-5-recheck-T1-T2.md),
   found no change to the mathematics and that the first verdict still
   applies; the loose sentences it found were corrected in a second revision,
   which no one but the author has checked.
3. **Review of the audit's identifications.** That L1 is a rewriting of
   Graham–Lovász (10)–(12), and that L3 is a special case of Hogben–Reinhart
   Theorem 3.3, are the auditor's own short computations, unreviewed. They only
   lower what the project claims.
4. **Independent recomputation of E2.** Orders 21–23 were computed by one
   implementation with internal guards (E3); the independent method was run on
   all trees only up to order 9. `results/exhaustive-21-23.json` was produced
   before the first commit and carries no provenance block; rerunning it at a
   committed revision takes about 34 minutes and needs the director's approval
   of the budget. MD-0001 stays `partial-result` until then.
5. **A published data set to compare with.** Table II of Graham–Lovász (1978,
   pp. 85–86) lists the normalized coefficients of all trees on at most eight
   vertices. The project's code has not been compared with it.
6. R1 was restated after the review of `e34acfc`. Its general form was since
   reconstructed in both directions by the review of T1 (`5e5ef14`), and the
   direction used by T2 by the review of T2; the two specialised statements
   of R1 about `M` have not been re-reviewed, and the header of
   `notes/lemmas.md` still says "has not been re-reviewed" (the file is left
   unchanged because two reviews pin its hash).
7. **Formalization.** Only the general form of R1 is formalized (session 4).
   Its statement was compared with the written one by the formalizing agent
   and by the session's author; an independent comparison is owed before the
   formal status is relied on. Next targets, in order of usefulness: Lemma L4
   (independent of trees); the polynomial inequalities of Step 3 of T2 and T3.
8. **Review of T2.** AI review of `74cb5bb` by `claude-opus-5-5`: no gap found
   within stated scope. No mathematician has read it, and no literature
   auditor searched for this statement (do Nascimento, Del-Vecchio and de
   Freitas 2019 on caterpillars is the first thing to read). The review
   listed eight defects of record and presentation. D1 and D2 (no registry
   record and no result file at the reviewed revision) were met by `1ef55b8`.
   D3 to D7 were corrected in `notes/spine3.md` on 2026-11-26 (its *Revision
   history* says what changed); no statement, formula or step of the proof
   was changed, and the review was made on the earlier text. D8 concerns the
   brief given to the reviewer, which misquoted the title of
   arXiv:1507.02341. The commit subject of `74cb5bb` says "every spine-3
   caterpillar", which is broader than T2 (`a, b, c ≥ 1`); the history is not
   rewritten. The recheck of `1c38662` named under obligation 2 found no
   change to the mathematics of T2 and that the first verdict still applies;
   it found three wrong sentences in the revision, corrected in a second
   revision that no one but the author has checked. Still open from it:
   `spine3.py` and `results/spine3.json` keep the words "spine length 3" in
   their description strings (the result file is evidence and is not
   edited).

9. **Review of T3.** AI review of `d2eb9ac` by `claude-opus-5-5`: no gap found
   within stated scope. No mathematician has read it; no literature auditor
   searched for the statement. `notes/diameter4-caterpillars.md` is unchanged
   since the review. Defects it listed, to be corrected in one revision that
   then needs a recheck: (E3) the notes call "Lemma C1" the determinant
   identity, which is a step inside its proof, and call the identities of
   Lemma C2 "between polynomials in `m, a, c`" although `c_0`, `e_0` and the
   `d_k` are not polynomials in `m`; (E4) the description of the caterpillars
   of diameter 4 in the corollary is asserted without argument and
   "caterpillar" is not defined in the notes; (E5) Step 3(ii) writes `R` for
   `R(m, n−3)`; (E6) no script or test re-derives Lemma C2 at `b = 0` (the
   reviewer did). E1 and E2 (no registry record and no result file at the
   reviewed revision) are met by the commit that follows the review.
10. **The exploration is unreviewed.** Lemma L4, the `s = 3` identities of
    `notes/vertex-principle.md` and the extension of L3 to empty leaf classes
    for general `s` (a sketch) have been checked by no one but their author.
    Nothing that depends on them may be promoted.

## Remaining obstacles

- Upper half: no proof idea yet for A(ii) beyond `k = 0`. A formula for every
  `δ_k` in terms of subforest counts exists (Graham–Lovász 1978, Theorem at
  eq. (42), p. 81, with coefficients for `k ≤ 5` in their Table III, not read);
  it is the natural tool for `k = 1`.
- Lower half: the extremal trees are not known. For double stars the margin
  `1 − q` is exactly computable (T1); numerically it is of order `1/n` (not
  proved). In the data `1 − q` is
  smaller still when the spine of a balanced caterpillar grows with `n` (Q2),
  so the method of T1 must be made uniform in the spine length to say anything
  about the trees that come closest to violating the bound.
- What T2 teaches about the dependence on the spine length: from `s = 2` to
  `s = 3` the number of binomial terms grows from 5 to 7, the differences stay
  affine in the product of the outer leaf numbers, and positivity is no longer
  term by term: it needs a boundary reduction and concavity. The polynomials
  were found by machine; nothing in the proof of T2 is uniform in `s`.
- The method of T1 to T3 works for a fixed number of twin classes. Trees of
  diameter 4 are not all caterpillars and have an unbounded number of classes.
- Hypothesis V with L4 would make the lower half, for each fixed spine length,
  a finite list of polynomial inequalities in `m`; it is still not uniform in
  the spine length, it says nothing about caterpillars with fewer leaves than
  spine vertices, and it does not apply to the upper half. The one statement
  with the same form for every `s` is the observation on the top coefficient.

## Next step

**Objective O4.** Four spine vertices. For the caterpillars with spine
`v_1 v_2 v_3 v_4` and leaf numbers `c_1, c_4 ≥ 1`, `c_2, c_3 ≥ 0`, of order
`n ≥ 8`: (1) write the six mixed partials `∂²D_n/∂c_i∂c_k` as polynomials in
`m` and the two remaining variables, for each parity, and decide whether they
are non-negative for every `m ≥ 4` (Hypothesis V for `s = 4`); (2) write
`D_n` at the vertices of the slice — `(n−5, 0, 0, 1)` and `(1, n−6, 0, 1)` and
their mirror images — as polynomials in `m` and decide their sign.

How: generalize `mixed_partials_s3.py`. The `g_j` for `s = 4` come from
`mixed_partials.multiaffine_g(4)` (16 coefficients each); the scaled binomials
need the recurrences for `C(n − 8, ·)` around `m − 4` up to distance 5. Write
out Lemma L3 with empty inner classes for `s = 4` (two inner classes) as in
Lemma C1′ of `notes/diameter4-caterpillars.md`. If (1) and (2) hold, Lemma L4
gives `d_{m−1} < d_m` for every caterpillar of diameter 5 with at least four
leaves; the upper inequality needs a separate argument and, for diameter 5,
the peak is expected to be `⌊n/2⌋` or `⌊n/2⌋ + 1`.

Falsification test for O4: `results/mixed-partials.json` has no failure of the
certificate and no non-positive vertex for `s = 4` up to order 200; before any
proof, extend that run to order 2000 for `s = 4` alone.

With it, or before it if cheaper: prove that the product `c_1 ⋯ c_s` occurs in
the `g_j` only with the coefficients `s` (in `g_{s−1}`) and `s + 3` (in `g_s`),
from the structure of the determinant; this is the first statement that would
be uniform in the spine length.

Owed first by default (obligations 8 to 10): one revision of the three sets of
notes with a recheck; an independent review of Lemma L4 and of the `s = 3`
identities; a literature audit for T2 and T3 (do Nascimento, Del-Vecchio and de
Freitas 2019 first).

Alternatives: Hypothesis A(ii) for `k = 1`, using the Graham–Lovász subforest
formula; obligation 5 (comparison with Table II), which is cheap.

## Sources

- G. Aalipour et al., arXiv:1507.02341 — TeX source read 2026-11-26.
- A. Abiad et al., arXiv:2206.07561 — read in full by the literature audit of session 2.
- R. L. Graham, L. Lovász, Adv. Math. 29 (1978) 60–88 — pp. 60–67 and 80–86 read by the audit.
- L. Hogben, C. Reinhart, arXiv:2103.00647 — pp. 5–12 read by the audit.
- R. Jana, I. Mahato, S. Sivasubramanian, arXiv:2407.03309 — read in full by the audit.
- K. L. Collins, Discrete Appl. Math. 25 (1989) 27–35 — not accessible; second-hand only.
- OEIS A000055 — tree counts used to validate the enumeration.
- Full list with access notes: the dossier.
