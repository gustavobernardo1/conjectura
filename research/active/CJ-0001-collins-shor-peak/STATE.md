# CJ-0001 — Collins–Shor conjecture — investigation state

Last updated: 2026-11-26 (session 1, revised after the review of revision `e34acfc`). This file is the current truth about the
investigation and is meant to be sufficient, on its own, for a new agent to
continue. Proofs are in [`notes/lemmas.md`](notes/lemmas.md); computations are
in [`experiments/CJ-0001-collins-shor-peak/`](../../../experiments/CJ-0001-collins-shor-peak/README.md);
the literature record is the dossier
[`research/candidates/CJ-0001-collins-shor-peak.md`](../../candidates/CJ-0001-collins-shor-peak.md).

## Exact statement

Source: Conjecture 1.2 of Aalipour, Abiad, Berikkyzy, Hogben, Kenter, Lin, Tait,
arXiv:1507.02341 (a search result reports the journal version as Electron. J.
Linear Algebra, 2018; not verified), read in the paper's TeX source on
2026-11-26. Verbatim:

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

Mathematical: `active-investigation`. Formal: `not-started`. Novelty:
`preliminary-search-completed`. External review: `not-reviewed`.

Nothing in this file is a claimed result of the project. Novelty of every
observation below is **unknown**, except where it is marked as known.

An independent AI review of the notes at revision `e34acfc` is in
[`reviews/2026-11-26-claude-fable-5-2.md`](reviews/2026-11-26-claude-fable-5-2.md).
It is a review by the same model family in a fresh context, not a human
review, and the catalogue status stays `not-reviewed` because the notes were
edited afterwards.

## Established results

| ID | Statement | Level | Evidence |
| --- | --- | --- | --- |
| E1 | The conjecture (strong reading) holds for all trees of order 3 to 20: 1,346,022 trees, 0 violations. | Verified computationally, exact. Reproduces the claim of the source ("all trees of order at most 20"). | `results/exhaustive-03-20.json` |
| E2 | The conjecture (strong reading) holds for all trees of order 21, 22 and 23: 22,596,335 trees, 0 violations. | Verified computationally, exact. Beyond the range reported in the source. | `results/exhaustive-21-23.json` |
| E3 | In E1 and E2 every tree count equals OEIS A000055, `d_0 = n − 1` on every tree (Graham–Pollak), every sequence is unimodal, and the only tie is one tree of order 13 (maximum at indices 6 and 7, inside the interval). | Verified computationally, exact. | same files |
| E4 | In orders 3 to 23 the peak is always `⌊n/2⌋` or `⌊n/2⌋ + 1`; the star attains the minimum and the path the maximum. | Verified computationally, exact. | same files |
| R1 | The lower bound for `T` is equivalent to `d_{m−1} < d_m`; the upper bound is equivalent to `M ≥ n−2` or `d_{M+1} < d_M`. | Proved here (short; uses log-concavity from the source). AI review of `e34acfc`: no gap found; restated in general form afterwards, not re-reviewed. | `notes/lemmas.md` |
| L1 | `ℓ_T(x) = (n−1) det(I + xL) − x τᵀ adj(I + xL) τ`. | Proved here from two classical facts (Graham–Pollak, cited; the Graham–Lovász inverse formula, quoted from memory and re-derived independently by the reviewer); checked exactly on all trees of order 3 to 9. AI review of `e34acfc`: no gap found. | `notes/lemmas.md`, `tests/test_cj0001_distpoly.py` |
| L2 | `d_1(T) = 2n² − 6 − Σ deg(v)²`; hence `ρ_0(S_n) ≤ ρ_0(T) ≤ ρ_0(P_n)` with equality only for the star and the path. | **Known:** the formula for `d_1` is in the source (proof of Theorem 3.3), as the review pointed out. Re-derived here; checked exactly on all trees of order 3 to 11. AI review of `e34acfc`: no gap found. | `notes/lemmas.md`, tests |
| L3 | Caterpillar with spine length `s` and all `c_i ≥ 1`: `det(xI − D) = (x+2)^{n−2s} det(xI − Q)` for an explicit `2s × 2s` matrix `Q`. | Proved here (equitable partition); every coefficient checked exactly against the direct computation on ten caterpillars. AI review of `e34acfc`: no gap found. | `notes/lemmas.md`, `near_star_families.py` |

Result files are under `experiments/CJ-0001-collins-shor-peak/results/`.

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

**Question Q1 — open.** For balanced caterpillars with a fixed spine length `s`,
exact values at `n = 10³, 10⁴, 10⁵, 10⁶` suggest `n (1 − q) → 6/(2s+3)`
(`1.2000, 0.8571, 0.6667, 0.5455, …` for `s = 1, 2, 3, 4, …`). Numerical
observation from exact values; no proof attempted.

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
       diameter 3 (double stars): reachable through L3 with s = 2  ← next step
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

## Open obligations

1. **Literature audit before any claim.** Not yet read: Collins (1989); Graham
   and Lovász (1978); the body of arXiv:2206.07561 (only its abstract); the
   2021 survey arXiv:2103.00647; the forward citations of arXiv:1507.02341. In
   particular it is unknown whether E2, L1, L3, Hypothesis A(ii) or the
   double-star case are already in the literature. (The formula in L2 is known:
   it is in the source.)
2. **Review.** One AI review (same model family, fresh context) of revision
   `e34acfc` found no gap in R1, L1, L2, L3 within its stated scope. R1 was
   restated afterwards and has not been re-reviewed. No human has reviewed
   anything. The review did not check Collins (1989), Graham–Lovász (1978) or
   novelty.
3. **Independent recomputation of E2.** Orders 21–23 were computed by one
   implementation with internal guards (E3); the independent method was run on
   all trees only up to order 9. An independent rerun on a sample of orders
   21–23, or a second full implementation, would strengthen E2. In addition,
   `results/exhaustive-21-23.json` was produced before the first commit of the
   repository and carries no provenance block; rerunning it at a committed
   revision takes about 34 minutes on the development machine.
4. The inverse formula of Graham and Lovász is quoted from memory in L1.
5. No Lean formalization exists for this problem.

## Remaining obstacles

- Upper half: no proof idea yet for A(ii) beyond `k = 0`. A formula for `d_2`
  in terms of subforest counts (edges, paths of length 2 and 3, claws, pairs of
  disjoint edges) is the natural next case.
- Lower half: the extremal trees are not known. In the data, `n(1 − q)` stays
  bounded for balanced caterpillars of fixed spine length (Q1) and `1 − q` is
  smaller still when the spine grows with `n` (Q2), so crude bounds are
  unlikely to work; an exact treatment of structured families is needed first.

## Next step

**Objective O1.** Prove the lower bound of the Collins–Shor conjecture for
double stars: for all integers `a, b ≥ 1`, with `n = a + b + 2` and
`m = ⌊n/2⌋`, `d_{m−1}(S(a,b)) < d_m(S(a,b))`.

How: by L3 with `s = 2`, `d_k ∝ Σ_{j=0}^{4} g_j(a,b) C(n−4, k−j)` with `g_j`
the coefficients of `−det(2xI − Q)` for the explicit `4 × 4` matrix `Q`.
(1) Compute `g_j(a,b)` symbolically (SymPy is not yet a dependency; add it).
(2) Divide `d_m − d_{m−1}` by a positive binomial factor to get a polynomial in
`(a, b)` for each parity of `n`. (3) Prove positivity, for instance after the
substitution `a = b + t`, `t ≥ 0`. (4) Cross-check the polynomial against the
exact values from `near_star_families.py` for all `a + b ≤ 200`. (5) Request an
independent review (skill `review-claim`).

Before starting O1: carry out obligation 1 for Collins (1989) and
arXiv:2206.07561, to learn whether diameter-3 trees are already covered. With
Collins's theorem on stars, O1 would give the lower bound for all trees of
diameter at most 3, where the general bound of the source gives only
`⌊(n−2)/4⌋`.

Falsification test for O1: the statement itself is already verified exactly
for all double stars of order at most 23 (E1, E2), for all double stars of even
order up to 40, and for balanced double stars of order 10³ to 10⁶
(`results/near-star-families.json`); the symbolic polynomial must reproduce
these exact values before any proof is attempted.

Alternative, if O1 turns out to be known: Hypothesis A(ii) for `k = 1`.

## Sources

- G. Aalipour et al., arXiv:1507.02341 — TeX source read 2026-11-26.
- A. Abiad et al., arXiv:2206.07561 — abstract only.
- OEIS A000055 — tree counts used to validate the enumeration.
- Full list with access notes: the dossier.
