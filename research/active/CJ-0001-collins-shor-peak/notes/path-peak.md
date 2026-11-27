# CJ-0001 — the peak of the path, exactly

Status of this file: written by an AI agent (Claude, model `claude-opus-5-5`)
on 2026-11-27, session 13. Lemma S47 and Corollary S48 have written proofs
below. **Nothing here is an established result**: a statement counts as
reviewed only where a report under [`../reviews/`](../reviews/) names this
file and its revision. Nothing here is a claim of novelty: the location of
the peak of the path up to one is the content of Theorem 3 of K. L. Collins,
Discrete Appl. Math. 25 (1989) 27–35, whose last step is informal (dossier,
"Primary sources read in session 11"); this file gives an exact criterion
and a complete proof.

Kept apart from [`upper-bound.md`](upper-bound.md) because that note is
under review at revision `53421a6` and is left byte-identical to it.

## Notation

`P_n` the path of order `n ≥ 3`; `d_j = d_j(P_n)`, `0 ≤ j ≤ n − 2`, its
normalized coefficients; `x = n − n/√5`, `y = n/√5` (irrational).

**Collins's formula** (Collins 1989, Theorem 3; checked against the distance
matrix for `n ≤ 30` by `experiments/CJ-0001-collins-shor-peak/upper_bound.py`,
part C, and for `n ≤ 14` by the reviewer of `53421a6`):

`d_{n−k} = C(n + k − 1, 2k − 1) (k − 1) n / k`,  `2 ≤ k ≤ n`.

## Lemma S47 (the peak of the path)

For `n ≥ 3` put `h_n(k) = 5k³ + 2k² − 4k − 2 − kn²` and let `k_0(n)` be the
least integer `k ≥ 2` with `h_n(k) > 0`. Then `k_0(n) ≤ n − 1`, and
`d_0, …, d_{n−2}` is strictly increasing up to the index `n − k_0(n)` and
strictly decreasing after it: **the path has the unique maximizing index
`p(P_n) = n − k_0(n)`.** Moreover `p(P_n) ∈ {⌊x⌋, ⌈x⌉}`, and
`p(P_n) = ⌈x⌉` exactly when `h_n(⌊y⌋) > 0`.

*Proof.* For `2 ≤ k ≤ n − 1`, from the formula,
`C(n+k, 2k+1)/C(n+k−1, 2k−1) = (n+k)(n−k)/(2k(2k+1))`, so

`d_{n−k}/d_{n−k−1} = [(k−1)/k]·[(k+1)/k]·2k(2k+1)/((n+k)(n−k)) = 2(k² − 1)(2k + 1)/(k(n² − k²))`,

and `d_{n−k} > d_{n−k−1}` iff `2(k²−1)(2k+1) > k(n² − k²)` iff
`h_n(k) > 0`; likewise with `<` and `=`. Now `h_n(k)/k = 5k² + 2k − 4 − 2/k − n²`
is strictly increasing in real `k > 0`, and `h_n(k) ≠ 0` for every integer
`k ≥ 2` (a zero would make `k` divide 2, so `k = 2`, and
`h_n(2) = 38 − 2n² ≠ 0`). Hence `h_n(k) > 0` exactly for `k ≥ k_0(n)`. And
`k_0(n) ≤ n − 1`: `h_n(n−1) = (n−1)(5(n−1)² − n²) + 2(n−1)² − 4(n−1) − 2`,
positive for `n ≥ 4` (both parts are, as `√5(n−1) > n` and `n − 1 ≥ 3`) and
equal to `20` for `n = 3`. So, reading `k = n − 1, n − 2, …, 2` (indices
`n − k − 1 → n − k` from `0 → 1` upwards), `d` increases strictly while
`k ≥ k_0` and decreases strictly once `k < k_0`; the unique peak is at
`n − k_0`.

Location. For `n ≥ 6` (`y > 1 + √2`, since `√5(1 + √2) < 5.4`):
`k = ⌈y⌉ > y` gives `h_n(k)/k > 5y² + 2y − 4 − 2/y − n² = 2y − 4 − 2/y > 0`,
so `k_0 ≤ ⌈y⌉`; and if `k = ⌊y⌋ − 1 ≥ 2`, then `k < y − 1` and
`h_n(k)/k < 5(y−1)² + 2(y−1) − 4 − 2/(y−1) − n² = −8y − 1 − 2/(y−1) < 0`,
so `k_0 ≥ ⌊y⌋` (trivially also when `⌊y⌋ − 1 < 2`). Hence
`k_0 ∈ {⌊y⌋, ⌈y⌉}` and `p = n − k_0 ∈ {⌊x⌋, ⌈x⌉}` (`n − ⌈y⌉ = ⌊x⌋`,
`n − ⌊y⌋ = ⌈x⌉`), with `p = ⌈x⌉` iff `k_0 = ⌊y⌋` iff `h_n(⌊y⌋) > 0`. For
`n = 3, 4, 5` directly: `k_0 = 2, 2, 3`, `p = 1, 2, 2 = ⌊x⌋`
(`x ≈ 1.66, 2.21, 2.76`). ∎

## Corollary S48 (when the path reaches the ceiling)

Let `θ` be the fractional part of `y = n/√5`. (a) If `θ ≥ 1/5`, then
`p(P_n) = ⌊x⌋`. (b) If `θ < 1/10` and `n ≥ 30`, then `p(P_n) = ⌈x⌉`. (c) In
particular `p(P_n) = ⌈n − n/√5⌉` implies that the fractional part of
`n − n/√5` exceeds `4/5`, and it holds for infinitely many `n`: **the upper
bound `⌈n − n/√5⌉` of the conjecture is attained for infinitely many `n`,
and for those `n` the ceiling cannot be replaced by the floor.**

*Proof.* With `k = ⌊y⌋ = y − θ` (`k ≥ 2` for `n ≥ 5`):
`h_n(k)/k = 2y(1 − 5θ) + 5θ² − 2θ − 4 − 2/k`. (a) If `θ ≥ 1/5` the first
term is `≤ 0` and `5θ² − 2θ − 4 < 0` on `[0, 1)`, so `h_n(⌊y⌋) < 0` and
S47 gives `⌊x⌋` (for `n ≤ 5`, S47 directly). (b) If `θ < 1/10` the first
term exceeds `y ≥ 30/√5 > 13`, while `|5θ² − 2θ − 4 − 2/k| < 6`; so
`h_n(⌊y⌋) > 0`. (c) The fractional part of `x = n − y` is `1 − θ`; and
`θ < 1/10` holds for infinitely many `n`, since `1/√5` is irrational
(Kronecker; even with density `1/10` by Weyl's equidistribution). ∎

Consistency with Theorem T9 of `upper-bound.md`: T9 gives
`p(T) ≤ ⌈x − 2/5⌉` for every tree; when the path is at `⌈x⌉` the fractional
part of `x` exceeds `4/5 > 2/5`, so `⌈x − 2/5⌉ = ⌈x⌉`. When `θ ≥ 1/5`
(fractional part of `x` at most `4/5`) and moreover the fractional part of
`x` is below `2/5`, T9 gives `p(T) ≤ ⌊x⌋ = p(P_n)` for every tree: the path
is peak-maximal for those `n` ((PX-peak) of MD-0021 for those `n`).

## Exact checks

Scratch, session 13 (exact integers, values compared by cross-multiplication;
script `pp2.py` in the session scratchpad, not stored): the maximizing index
of the path from Collins's formula is unique and equals `n − k_0(n)` for
every `3 ≤ n ≤ 2000`, always in `{⌊x⌋, ⌈x⌉}`, with 393 ceiling cases; the
ratio identity holds exactly for `n = 37`, `2 ≤ k ≤ 36`. (A first, slower
scratch run to `n = 3000` was stopped before it finished and is not
counted.) Stored: `upper_bound.py`, part C (the path, `n ≤ 2000`:
393 ceiling cases, smallest fractional part of `x` among them `0.80128`).
