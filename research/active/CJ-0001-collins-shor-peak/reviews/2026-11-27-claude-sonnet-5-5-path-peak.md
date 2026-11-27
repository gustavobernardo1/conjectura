# Independent review — CJ-0001 — `notes/path-peak.md` (Lemma S47, Corollary S48: the peak of the path)

- **Reviewer:** Claude, model `claude-sonnet-5-5`, run as the `adversarial-reviewer` subagent.
- **Date:** 2026-11-27
- **Independence:** fresh subagent context; I received the task and the revision
  but not the author's reasoning trail. The author of the note is
  `claude-opus-5-5`, a different model of the same vendor. I wrote my own scripts (scratchpad, not stored) and did not run the author's `pp2.py`.
- **Revision reviewed:** commit `2037b18c2823900d159efdacf1a68d4619bec0e3`.
  - `research/active/CJ-0001-collins-shor-peak/notes/path-peak.md` SHA-256 `b65a9931ed8497047ab00b834ae40dc37abedeabaeca6a66f3b5024996e78016` (unmodified relative to `2037b18`)
  - for the cross-references: `notes/upper-bound.md` SHA-256 `ad21eeb6…49e0ed`; `results/upper-bound.json` SHA-256 `989be91d…f85de`.
- **Material given to the reviewer:** the note, the statement in `STATE.md`, the result file of the stored experiment.

## Statement as read from the primary source

Conjecture 1.2 of arXiv:1507.02341: the normalized coefficients `d_k` of the
distance characteristic polynomial of a tree of order `n` are unimodal with peak
between `⌊n/2⌋` and `⌈n − n/√5⌉`. Normalized coefficients of the path `P_n` are, by
Collins (1989), Theorem 3, `d_{n−k} = C(n+k−1, 2k−1)(k−1)n/k`, `2 ≤ k ≤ n`
(i.e. indices `0 ≤ j = n−k ≤ n−2`). The note claims, taking this formula as given:
(S47) for `n ≥ 3` the peak of `d(P_n)` is unique and equals `n − k_0(n)`, with `k_0` the least integer
`k ≥ 2` with `h_n(k) = 5k³ + 2k² − 4k − 2 − kn² > 0`, `k_0 ≤ n−1`, and it lies in `{⌊x⌋, ⌈x⌉}`, `x = n − n/√5`;
(S48) with `θ = {n/√5}`: `θ ≥ 1/5 ⇒ p = ⌊x⌋`; `θ < 1/10`, `n ≥ 30 ⇒ p = ⌈x⌉`; hence the conjecture's upper bound is attained for infinitely many `n`
(and for those `n` cannot be replaced by the floor).

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | `n ≥ 3`; the formula is a cited theorem (Collins 1989, Thm 3), not proved in the note. I did not read Collins; I verified the formula exactly against the distance matrix for every `n = 3..20` (see Reproduction), and the stored experiment does it to `n ≤ 30`. For `n > 30` the correctness of the path formula rests on Collins's theorem; this is a dependency, not a gap in the note's own argument. |
| Quantifiers | Correct. "Unique maximizing index" is proved (strictness, no ties); "`p ∈ {⌊x⌋, ⌈x⌉}`" and "`p = ⌈x⌉` iff `h_n(⌊y⌋) > 0`" are proved for `n ≥ 6`, and for `n = 3, 4, 5` by direct computation (see D1). |
| Mathematical definitions | `h_n`, `k_0`, `x`, `y`, `θ` well defined. `n − ⌈y⌉ = ⌊x⌋` and `n − ⌊y⌋ = ⌈x⌉` hold since `y` is irrational. |
| Boundary cases | `n = 3`: `h_3(2) = 20 > 0`, `k_0 = 2`, `p = 1 = ⌊1.66⌋`; `n = 4`: `h_4(2) = 6`, `k_0 = 2`, `p = 2 = ⌊2.21⌋`; `n = 5`: `h_5(2) = −12`, `h_5(3) = 64`, `k_0 = 3`, `p = 2 = ⌊2.76⌋`. All agree with the note, and with the exact peaks of `d(P_n)`. `k_0 = n − 1` (peak at index 1) occurs at no `n ≥ 3` in my range; the upper end `k = n − 1` of the ratio identity is nevertheless legitimate (it compares `d_1` with `d_0`). `n = 3`: `h_3(n−1) = 20` as the note says. |
| Ratio identity | Re-derived: `C(n+k,2k+1)/C(n+k−1,2k−1) = (n+k)(n−k)/(2k(2k+1))`, so `d_{n−k}/d_{n−k−1} = [(k−1)/k][(k+1)/k]·2k(2k+1)/((n+k)(n−k)) = 2(k²−1)(2k+1)/(k(n²−k²))`; and `2(k²−1)(2k+1) − k(n²−k²) = 5k³ + 2k² − 4k − 2 − kn² = h_n(k)`. Checked exactly (rational arithmetic) for `n ∈ {3,4,5,6,37,100}`, every `2 ≤ k ≤ n−1`. |
| Monotonicity and no tie | `h_n(k)/k = 5k² + 2k − 4 − 2/k − n²` is strictly increasing on `k > 0` (each term nondecreasing, `5k²` strictly). `h_n(k) = 0` for an integer `k ≥ 2` forces `k \| 2`, so `k = 2` and `h_n(2) = 38 − 2n² = 0`, impossible. Hence the sign of `h_n(k)` on integers `k ≥ 2` is negative up to `k_0 − 1` and positive from `k_0`: strictly increasing then strictly decreasing, the peak unique at `n − k_0`. The orientation (`k` large ↔ small index) is read correctly: `h_n(k) > 0` means `d_{n−k} > d_{n−k−1}`. Verified exactly for `3 ≤ n ≤ 700`: unique maximum, `p = n − k_0`, strict increase up to `p` and strict decrease after. |
| `k_0 ≤ n − 1` | Correct: `h_n(n−1) = (n−1)(5(n−1)² − n²) + 2(n−1)² − 4(n−1) − 2`; for `n ≥ 4` the first part is positive (`√5(n−1) > n` iff `n > 1.8`) and `2k² − 4k − 2 > 0` for `k = n−1 ≥ 3` (value 4 at `k = 3`, increasing); `= 20` at `n = 3`. Checked by computer: `h_n(n−1) > 0` for `n = 3..49` (no exceptions). |
| Location for `n ≥ 6` | Correct. `y = n/√5 ≥ 2.68 > 1 + √2 = 2.414` (`√5(1+√2) ≈ 5.40 < 6`), so `2y − 4 − 2/y > 0` (iff `y² − 2y − 1 > 0`), giving `h_n(⌈y⌉) > 0` and `k_0 ≤ ⌈y⌉`. For the lower end, `k = ⌊y⌋ − 1 < y − 1` and monotonicity of `h/k` give `h/k < 5(y−1)² + 2(y−1) − 4 − 2/(y−1) − 5y² = −8y − 1 − 2/(y−1) < 0` (expansion re-done); so `k_0 ≥ ⌊y⌋`; the case `⌊y⌋ − 1 < 2` is trivial since `k_0 ≥ 2`. `⌊y⌋ ≥ 2` for `n ≥ 6` so `h_n(⌊y⌋)` is in the domain. The criterion `p = ⌈x⌉ iff h_n(⌊y⌋) > 0` follows (if `h_n(⌊y⌋) > 0` then `k_0 ≤ ⌊y⌋`, hence `= ⌊y⌋`). |
| Small cases `n = 3, 4, 5` | Verified directly (above). The note does not restate "`p = ⌈x⌉` iff `h_n(⌊y⌋) > 0`" for these; it is true there (`h_3(1) = −8`, `h_4(1) = −15`, `h_5(2) = −12`, all negative, `p = ⌊x⌋`), though for `n = 3, 4` the value `⌊y⌋ = 1` is outside the domain `k ≥ 2` of `k_0`. See D1. |
| Corollary S48 identity | `h_n(k)/k = 2y(1 − 5θ) + 5θ² − 2θ − 4 − 2/k` with `k = y − θ`: re-expanded, correct. |
| S48(a) | Correct: for `θ ≥ 1/5` the first term is `≤ 0`, `5θ² − 2θ − 4 < 0` on `[0,1)` (convex, endpoint values `−4` and `−1`), `−2/k < 0`, so `h_n(⌊y⌋) < 0`; for `n ≤ 5` by S47 directly. Exact check for `3 ≤ n ≤ 700`: whenever `5n² ≥ (5⌊y⌋+1)²` (equivalent to `θ ≥ 1/5`) the peak is `⌊x⌋`: no exception. |
| S48(b) | Correct: `θ < 1/10` gives `1 − 5θ > 1/2`, first term `> y ≥ 30/√5 = 13.4 > 13`; `5θ² − 2θ − 4 ∈ (−4.15, −4]` on `[0, 0.1)` and `2/k < 0.16`, so `\|…\| < 6`. The threshold `n ≥ 30` is not sharp but sufficient. Exact check for `30 ≤ n ≤ 700` with `θ < 1/10`: peak `= ⌈x⌉`, no exception. |
| S48(c), infinitude | `p = ⌈x⌉` implies `θ < 1/5` by (a) (valid for all `n ≥ 3`), i.e. the fractional part of `x` (`= 1 − θ`) exceeds `4/5`. Infinitely many `n` with `θ < 1/10` by Kronecker/Weyl (`1/√5` irrational), and these `n` can be taken `≥ 30`. Hence the ceiling `⌈x⌉` is attained by the path for infinitely many `n`, and `⌊x⌋` fails for them. Computation: in `3 ≤ n ≤ 700` the ceiling occurs in 135 cases, smallest fractional part of `x` among them `0.8023` (`> 0.8`); the stored experiment gives 393 cases for `n ≤ 2000`, minimum `0.80128`. A caveat on reading: "the upper bound of the conjecture is attained for infinitely many `n`" means the path attains `⌈n − n/√5⌉` as its peak; this is correct and uses that the peak is unique (S47). |
| Consistency with Theorem T9 | Correct. T9 (`upper-bound.md`, reviewed) gives `p ≤ K = ⌈x − 2/5⌉` for every tree. When the path peak is `⌈x⌉`, `{x} > 4/5`, so `{x} − 2/5 > 2/5 > 0` and `K = ⌈x⌉` — no contradiction. When `{x} < 2/5`, `K = ⌊x⌋`, and `θ = 1 − {x} > 3/5 ≥ 1/5`, so by (a) the path has `p = ⌊x⌋`, hence every maximizing index of every tree is `≤ p(P_n)`. The paragraph's hypothesis "θ ≥ 1/5 and moreover `{x} < 2/5`" is redundant (the second implies the first); harmless. The claim "(PX-peak) of MD-0021 for those `n`" is then correct. I checked `p(P_n) ≤ ⌈x − 2/5⌉` with 60-digit decimals for `3 ≤ n ≤ 700`: no violation. |
| Logical implications | Each of S47 → S48 steps follows; S48 uses only S47's criterion and the location result. |
| Dependency assumptions | (i) Collins's closed formula (cited; verified exactly for `n ≤ 20` by me, `n ≤ 30` by the stored experiment, `n ≤ 14` by the earlier reviewer); (ii) T9 of `upper-bound.md` (reviewed, no gap, two reviews of `53421a6` and the recheck at `2037b18`) only for the consistency paragraph, not for S47 or S48. |
| Counterexample attempts | Exact enumeration of the peak of `d(P_n)` from the formula for `3 ≤ n ≤ 700` (below): unique peak, equal to `n − k_0`, in `{⌊x⌋, ⌈x⌉}`; criteria (a), (b) never violated; the ceiling never occurs with fractional part of `x` below `4/5`. No counterexample to any statement. |
| Formalization scope | None (not applicable). The working tree contains an untracked `UpperBoundPeak.lean`; not part of this revision and not reviewed. |
| Novelty coverage | Not assessed. The note says it is not a claim of novelty (Collins 1989, Theorem 3 locates the peak up to one). I made no literature search. Unknown. |
| Unresolved gaps | No mathematical gap. Defects D1 to D4 below. |

### Defects (none is a gap in S47 or S48)

- **D1 (statement vs. proof).** S47 asserts "`p(P_n) = ⌈x⌉` exactly when `h_n(⌊y⌋) > 0`" for all `n ≥ 3`; the proof covers it for `n ≥ 6`, and
  for `n = 3, 4, 5` only gives the values `p`. For `n = 3, 4` `⌊y⌋ = 1` is outside the range `k ≥ 2` on which `h_n` was introduced.
  True (the values are `−8, −15, −12`) but not written; either restrict the "exactly when" to `n ≥ 6` or add the values.
- **D2 (stale sentence).** The introduction says `upper-bound.md` "is under review at revision `53421a6` and is left byte-identical to it". At `2037b18` that file is revision 1
  (changed since; `path-peak.md` is cited from it); the sentence is false at this revision and should say that the file is separate for historical reasons or be removed.
- **D3 (stored check of the formula).** The stored experiment checks Collins's formula against the distance matrix only for `n ≤ 30` (and the note's "Exact checks" says the author's `pp2.py` is scratch, not stored, which is honest); the part of the
  statement for `31 ≤ n ≤ 2000` is supported by the stored experiment only through the formula, and for all `n` only through Collins's theorem. The note says so (Notation), but the final sentence of "Exact checks" could state the dependency.
- **D4 (redundant hypothesis).** In the consistency paragraph, "`θ ≥ 1/5` and moreover `{x} < 2/5`" — the first is implied by the second.

## Reproduction

Scratch, session scratchpad (`pp.py`, `r.py`), run with `uv run --project d:/conjectura python -u …`; python-flint for exact integer characteristic polynomials, `fractions.Fraction`, `decimal` (60 digits) for `K`.

1. Collins's formula vs. the distance matrix: for `n = 3..20`, the characteristic polynomial of the exact distance matrix `|i − j|` of `P_n`, normalized as `−2^{−(n−2)} det(2xI − D)`, has top coefficients `d_n = −4`, `d_{n−1} = 0` and `d_{n−k} = C(n+k−1,2k−1)(k−1)n/k` for every `2 ≤ k ≤ n`: all equal (exact). Output "Collins formula matches distance matrix n=3..20".
2. For every `3 ≤ n ≤ 700` (the run was set to 3000 first, killed for slowness; the output line "ok to 3000" printed by my script is a mislabelled message, the range was `3..700`): unique maximum of `d_0..d_{n−2}` (exact); `k_0(n) ≤ n − 1`; `p = n − k_0`; strict monotonicity on both sides; `p ∈ {⌊x⌋, ⌈x⌉}`; `p = ⌈x⌉` iff `h_n(⌊y⌋) > 0`; S48(a) and (b) (exactly via `5n² ≥ (5⌊y⌋+1)²` and `100n² < 5(10⌊y⌋+1)²`); `p ≤ ⌈x − 2/5⌉`; fractional part of `x` above `0.8` whenever `p = ⌈x⌉`. All assertions passed; 135 ceiling cases, minimum fractional part `0.80234`.
3. Ratio identity exactly for `n ∈ {3,4,5,6,37,100}` and all `2 ≤ k ≤ n−1`: passed.
4. Small cases `h_3(2) = 20`, `h_4(2) = 6`, `h_4(3) = 91`, `h_5(2) = −12`, `h_5(3) = 64`: as in the note.
5. The stored result `results/upper-bound.json` (not re-run), part `C_path`: 393 ceiling cases for `3..2000`, no tied peak, `matrix_checked_to: 30`, minimum fractional part `0.801276…` at `n = 1436`; consistent with the note's figures.

## Verdict

`no gap found within stated scope`

Scope: Lemma S47 and Corollary S48 of `notes/path-peak.md` at `2037b18`, **assuming Collins's closed formula** for `d_{n−k}(P_n)` (cited from Collins 1989, Theorem 3; verified here for `n ≤ 20` against the distance matrix, not read at the source), the ratio identity, the monotonicity and no-tie argument, `k_0 ≤ n − 1`, the location for `n ≥ 6` and the small cases, both parts of S48 and the infinitude claim, and the consistency paragraph with T9 (taking T9 as stated). It does not cover Collins's theorem itself for `n > 30`, the novelty of the statement (unknown, not searched), formalization (none), or any claim about trees other than the path except through T9. Defects D1 to D4 do not affect correctness but should be corrected in a later revision, after which this review no longer applies to that revision. One AI review, by a model of the same vendor as the author; not human review.
