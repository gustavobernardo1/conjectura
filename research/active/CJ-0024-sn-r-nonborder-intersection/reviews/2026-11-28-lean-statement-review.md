# Independent review — CJ-0024 — Lean statements of Theorems A and B vs. the note

- **Reviewer:** claude-sonnet-5-5 (Claude Code subagent `adversarial-reviewer`)
- **Date:** 2026-11-28
- **Independence:** fresh context; the reviewer received only the file paths and
  the task, not the authors' reasoning. Different model from the authors
  (`claude-opus-5-5`). The reviewer read the Lean source and the note
  line by line and recomputed the witnesses by hand. **Lean was not built or
  run by the reviewer** (instructed not to; a verification run was in progress).
  Whether the file compiles and the axioms are clean rests on the receipts
  (`verification/receipts/…`), which this review did not re-check; the latest
  receipt present in the tree is `20261128T030452Z-232840d982-dirty-passed.json`,
  made on a dirty tree at a different commit than the one reviewed.
- **Revision reviewed:** commit `f5de051aade0fc854b8274e4ae708aef024864be`
  (branch `research`; working tree had unrelated uncommitted changes to STATE.md,
  catalogue.json, discoveries.json, an exploration note; none of the reviewed
  files was modified).
  - `formalization/Conjectura/Research/WeberUniqueness.lean`
    SHA-256 `dabcb41312b9f7d7ec777257fbeba62a9e1a248409974b932742c1b93c1a3e30` (889 lines)
  - `research/active/CJ-0024-sn-r-nonborder-intersection/notes/weber-uniqueness.md`
    SHA-256 `48686378da728f0260db61f813714c5be0cfc09239f897988f643d0af337753d` (294 lines; header says revision 2)
  - the 25 entries of `formalization/registry.json` with `catalogue_id` `CJ-0024`.
- **Scope:** statement comparison only (does the Lean statement say what the
  note's item says). Not a re-review of the mathematics of the note (done
  separately), not a build.

## Statement as read from the primary source (note, §2, §3, Lemma 4)

For real `c` with `1 < c < 2`: `N_c`, `T_c`, `I_c = residual(T_c)`, `S_L`,
`T_M`, `I_WB` as in the note; Theorem A items 1–6; Theorem B with `T'_c`,
`S*_c`, `J_c`, items 1–5; Lemma 4: T t-norm, T(x,·) left-continuous at 1 for
every x, I_T(x,y)=1 implies x ≤ y. All objects live on `[0,1]` / `[0,1]²`.

## Checks on the definitions' bodies

- `IsTNorm`: values in `[0,1]` for arguments in `[0,1]` (yes, `mem`), commutativity,
  associativity, `T x 1 = x`, monotone in the first variable, all quantified over
  `Icc 0 1`. Second-variable monotonicity follows from commutativity
  (`IsTNorm.mono_right`, read and correct). In `assoc`, `T x y` is in `[0,1]`
  by `mem`, so the inner application stays in the checked domain: no hidden
  use of values outside `[0,1]`. Faithful. Every genuine t-norm on `[0,1]` extends
  to ℝ×ℝ, so quantifying over ℝ → ℝ → ℝ loses nothing.
- `IsTConorm`: same with `S x 0 = x`. `IsFuzzyNegation`: values in `[0,1]`,
  antitone on `[0,1]`, `N 0 = 1`, `N 1 = 0`. Faithful to §2.
- `residual T x y = sSup {t | t ∈ Icc 0 1 ∧ T x t ≤ y}`. For a t-norm and
  `x, y ∈ [0,1]` the set contains `0` (`T x 0 = 0 ≤ y`, `IsTNorm.zero_right`)
  and is bounded above by `1`, so the real `sSup` is the true supremum; no junk
  value (`sSup ∅ = 0`, unbounded `= 0`) can occur on the domain of the theorems.
  Moreover `residual_Tc`, `residual_Tc'` do not use that remark: they compute the
  sSup explicitly (`csSup_Icc`, `csSup_Ico`, `IsGreatest.csSup_eq`). In
  `le_of_residual_eq_one` only non-emptiness is used (`exists_lt_of_lt_csSup`);
  were the set unbounded the junk value would be `0 ≠ 1`, so the hypothesis
  could not hold vacuously via junk. OK.
- `Tc c x y = if max x y = 1 then min x y else max 0 (x+y−c)`: on `[0,1]²`,
  `max x y = 1` iff not both `< 1`, so this is the note's two-case definition.
  `Nc`, `SL`, `Ic`, `weberImp` match the note on `[0,1]` (`weberImp x y = if x<1 then 1 else y`).
  `Tc' c x y = if max x y = 1 ∨ c < x+y then min x y else 0`, `Sstar c a b =
  if a+b<c then max a b else 1`: match Theorem B. `Jc c x y = if x=1 then y else
  if x ≤ y then 1 else max (min 1 (c−x)) y`: on `[0,1]²` equal to the note's
  three cases (overlap only at `(1,1)`, both give 1). I recomputed that the
  note's `J_c(1,y)=y`, `J_c=1` for `x≤y` agree at `(1,1)`. Match.
- `ContinuousWithinAt (T x) (Icc 0 1) 1`: `1` is the right endpoint of the set,
  so this is exactly continuity from the left at `1` of `T(x,·)` on `[0,1]`.
  Adequate encoding. Its negation `¬ContinuousWithinAt …` is the right negation.
- "Border-continuous": see finding F1 below.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | `1 < c < 2` kept as `hc1 hc2` everywhere (unused in some). Lean statements with fewer hypotheses than the note (`Ic_eq_SL_Nc`: any real `c`, any real `x`) are stronger. `le_of_residual_eq_one` assumes continuity only at the given `x` (note: for every `x`) – stronger. No vacuous hypothesis found; `IsTNorm`, `IsFuzzyNegation` are inhabited (`min_isTNorm`, `Tc_isTNorm`, `Nc_isFuzzyNegation`). |
| Quantifiers | All "for all x,y" of the note are over `[0,1]` in Lean; the note's "for all x, y" means `[0,1]²` (domain of the operations). "I ≠ I'" is encoded as `∃ x y ∈ [0,1]` with values differing: the correct negation of equality as functions on `[0,1]²`. "Not the residual of any LC t-norm" is `∀ T' …, ∃ x y ∈ [0,1], residual T' x y ≠ residual (Tc c) x y`; with `residual_Tc` this is the same as `I_c ≠ I_T'`. |
| Mathematical definitions | Match (see above). Residual sSup well behaved on the domain. |
| Boundary cases | `(1,1)` of `J_c` consistent. `x = 1` branches of `I_c`, `J_c`, `N_c` consistent with the note. Witnesses recomputed by hand: `Ic_ne_weberImp` x=c/2 (needs c/2 > c−1 iff c<2, ok); `Jc_ne_Ic` x=(2+c)/4, y=(2−c)/4: y<x, J=(3c−2)/4, I_c=c/2, differ iff c≠2, ok; `Ic_ne_Ic`, `Jc_ne_Jc` witness x=max(c,c')/2, y=0, value c−x vs c'−x, differ, ok. `residual_*_violates_OP` at x=c−1∈(0,1), y=0, ok. |
| Intermediate lemmas | Each of the 25 registered theorems is compared in the table below. |
| Logical implications | `residual_ne_of_leftContinuous` / `residual_Tc'_ne_of_leftContinuous`: the proof takes `residual T' (c−1) 0`, rewrites the other side to `1`, and applies `le_of_residual_eq_one`, giving `c−1 ≤ 0`, contradicting `c>1`. Direction confirmed: the Lean hypothesis (`T'(x,·)` left-continuous at 1 for each `x ∈ [0,1]`, nothing else) is implied by left-continuity of the t-norm in either/both variables, so the Lean theorem is at least as strong as the note's item 5 / B4. |
| Dependency assumptions | None beyond Mathlib (no project axioms found). Scan below. |
| Counterexample attempts | Tried to make a statement vacuous or false: junk `sSup` (excluded above), `y` outside `[0,1]` (excluded by hypotheses), `T'` weird outside `[0,1]` (irrelevant: `ContinuousWithinAt` restricted to `Icc`, residual uses only `[0,1]` arguments), `x` with `T' x` constant etc. None succeeded. |
| Formalization scope | See "Not formalized" below. |
| Novelty coverage | Not assessed (out of scope). |
| Unresolved gaps | F1, F2, F3, F4 below; none of them makes a registered Lean statement mismatch the corresponding note sentence, but F2 and F3 limit what the 25 theorems establish about the note's *prose* claims. |

### Detailed findings

- **F1 (interpretation, not a mismatch).** `Tc_not_borderContinuous` formalizes
  "not border-continuous" as `¬ContinuousWithinAt (uncurry (Tc c)) ([0,1]×[0,1]) (x,1)`
  for `0<x<1`, i.e. joint discontinuity at a border point of the square as a
  function on the whole square. This is exactly the reading fixed in the note's
  §2 (and the header of the Lean file). It is the only non-degenerate reading:
  the restriction of any t-norm to the set `[0,1]²\]0,1[²` is automatically
  continuous (values `T(x,1)=x`, `T(1,y)=y`, `T(x,0)=T(0,y)=0`), so
  "continuous on the border set" read as a restriction would make every t-norm
  border-continuous. Reviewer judgement: the reading is correct for the problem
  (Baczyński–Jayaram's border continuity is joint continuity at border points);
  this review did not consult the source chapter again. The registered statement
  is the "form proved in the note" (existence of a border discontinuity at every
  `(x,1)`, `0<x<1`), which is stronger than the bare existential "not
  border-continuous". For Theorem B the range is `0 < x ≤ c−1`, matching the
  note's proof of B1.
- **F2 (not formalized: fuzzy-implication property).** No registered theorem
  states that `I_c` or `J_c` is a fuzzy implication (Definition 2.1:
  monotonicity in both variables, `I(0,0)=I(1,1)=1`, `I(1,0)=0`). The note's
  "I_c is an (S,N)-implication" is covered only as the identity
  `I_c = S_L(N_c(·),·)` plus `IsTConorm SL` and `IsFuzzyNegation (Nc c)`; the
  note's "I_c is a QL-implication" (a QL-operation that is a fuzzy implication)
  is covered only as the identity with `T_M`, plus `min_isTNorm`, which is a
  helper in the file and is **not registered**. Consequently the Lean side does
  not establish "I_c / J_c is an (S,N)-implication / QL-implication" in the
  sense of the definitions of §2, though these hold mathematically
  (note's proof cites 2010 paper Thm 5.10; mathematically I(0,0)=1 etc. are
  immediate). The Lean header states this limitation honestly.
- **F3 (not formalized: Corollary, Lemmas 1–3, `I_c ∈ I_T \ I_T*`).** The Corollary
  (answer to Problems 4.2(i), 4.5(ii), cardinality "continuum many") is not
  formalized: Lean gives pairwise distinctness only for `I_c ≠ I_c'`, `J_c ≠ J_c'`
  (the continuum count would need injectivity of `c ↦ I_c` on `(1,2)` and the
  cardinality of `(1,2)`, i.e. `Ic_ne_Ic` plus a short Mathlib step). That
  "`I_c` is the residual of a t-norm that is non-border-continuous" holds is
  covered by `residual_Tc` + `Tc_not_borderContinuous`; "and of no
  left-continuous t-norm" by `residual_ne_of_leftContinuous`. Lemmas 1–3 are
  not stated in general form (their content is proved for `T_c`, `T'_c` only);
  not a mismatch since the Lean file declares so.
- **F4 (minor, bookkeeping).** (a) `Ic_eq_SL_Nc_min` and the `Jc` analogue need
  `T_M = min` to be a t-norm to read as "QL-operation"; that fact is in
  `min_isTNorm`, unregistered. (b) `hypotheses_nonvacuous` is not itself a
  registered theorem; it is referenced as the `nonvacuity` witness of every
  entry. It witnesses satisfiability of `1<c<2`, `c≠c'`, `0<x≤c−1`, the t-norm
  and pointwise left-continuity hypotheses (with `T = min`) and the hypotheses of
  `le_of_residual_eq_one` at `x=y=0`. It does not exhibit a *non-trivial*
  application of the conclusion (x=y gives `x ≤ y` trivially), but non-vacuity
  only requires jointly satisfiable hypotheses. Adequate. (c) Registry
  `source_statement` fields cite "commit bf6015c" for revision 2 of the note;
  the file hashes recorded above are those at `f5de051`; this review did not
  check that the note's text at `bf6015c` equals the text at `f5de051`
  (the note's header says revision 2; `git diff` was not run).

## Table: Lean name | note item | verdict | remark

| Lean name | Note item | Match | Remark |
| --- | --- | --- | --- |
| `Tc_isTNorm` | A1, first clause | match | `IsTNorm (Tc c)`, `1<c<2`. |
| `Tc_not_leftContinuous` | A1, "not left-continuous" | match (stronger than ∃) | `∀ 0<x<1`, `¬ContinuousWithinAt (Tc c x) [0,1] 1`; right negation of left-continuity at 1 in the 2nd variable (equiv. in the 1st by commutativity). |
| `Tc_not_borderContinuous` | A1, "not border-continuous" | match, under the note's joint-continuity reading (F1) | discontinuity of `uncurry Tc` within `[0,1]²` at `(x,1)`, `0<x<1`; derived from the previous by composition. |
| `residual_Tc` | A2 | match | on `[0,1]²`; `Ic` body equals note's `I_c`. |
| `SL_isTConorm` | A3, S_L is a t-conorm | match | |
| `Nc_isFuzzyNegation` | §3, N_c negation | match | |
| `Ic_eq_SL_Nc` | A3 identity | stronger | `∀ c x`, `y∈[0,1]`; `(S,N)`-implication status needs F2. |
| `Ic_eq_SL_Nc_min` | A4 identity | match | QL status needs fuzzy-implication property (F2) and `min_isTNorm` (unregistered). |
| `residual_Tc_violates_OP` | A5, first sentence | match | states `0<c−1`, `c−1≤1`, `residual (Tc c)(c−1) 0 = 1` (via residual, not `Ic`; link by `residual_Tc`). |
| `le_of_residual_eq_one` | Lemma 4 | stronger | continuity only at the given `x`; hypotheses `x,y∈[0,1]`, `IsTNorm T`. |
| `residual_ne_of_leftContinuous` | A5, second sentence | match / stronger | hypothesis weaker than left-continuity of `T'`; conclusion: residuals differ somewhere on `[0,1]²`; correct direction. |
| `Ic_ne_weberImp` | A6, first clause | match | |
| `Ic_ne_Ic` | A6, second clause | match | |
| `Tc'_isTNorm` | B1, first clause | match | |
| `Tc'_not_leftContinuous` | B1 | match (as in the note's proof) | range `0<x≤c−1`. |
| `Tc'_not_borderContinuous` | B1 | match under same reading as F1 | range `0<x≤c−1`. |
| `Sstar_isTConorm` | B1, last clause | match | |
| `residual_Tc'` | B2 | match | `Jc` body = note's three cases on `[0,1]²`. |
| `Jc_eq_Sstar_Nc` | B3, first identity | match | `x,y∈[0,1]`; (S,N) status needs F2. |
| `Jc_eq_Sstar_Nc_min` | B3, second identity | match | QL status needs F2 and `min_isTNorm`. |
| `residual_Tc'_violates_OP` | B4, first clause | match | |
| `residual_Tc'_ne_of_leftContinuous` | B4, second clause | match / stronger | as for `residual_ne_of_leftContinuous`. |
| `Jc_ne_weberImp` | B5, first | match | |
| `Jc_ne_Ic` | B5, second | match | witness recomputed (see Boundary cases). |
| `Jc_ne_Jc` | B5, third | match | |

25 registry entries for CJ-0024 were found and all are in the table
(count of the registry entries done by script: 25).

## Source scan (`grep` over the Lean file)

Pattern `sorry|admit|axiom|native_decide|unsafe|set_option|macro|notation|attribute`:
**no match**. No `private` declaration affects any statement (`max_aux`,
`lt_one_of_mem_ne`, `min_aux` are private helpers only). Imports are
`Mathlib.Topology.Instances.Real.Lemmas`, `Mathlib.Tactic.Linarith`,
`Mathlib.Tactic.Positivity`. (The scan is textual; the axiom audit of the
transitive closure is the job of `scripts/verify_lean.py`, not re-run here.)

## Reproduction

- `git rev-parse HEAD`, `sha256sum` of the two files (values above), Python
  script listing the registry entries with `catalogue_id == "CJ-0024"` (25).
- Hand calculation of the witnesses of `Ic_ne_weberImp`, `Ic_ne_Ic`,
  `Jc_ne_Ic`, `Jc_ne_weberImp`, `Jc_ne_Jc`, `residual_*_violates_OP`, and of the
  proof skeleton of `le_of_residual_eq_one` (the contradiction with
  `|T x s − x| < x − y` against `T x s ≤ y`). Lean build **not** run.

## Verdict

**statements match** — within the scope below. The 25 registered Lean theorems
say what the corresponding items of Theorems A and B and Lemma 4 of
`weber-uniqueness.md` (revision 2) say, or are at least as strong, under the
encoding stated in the file header and registry; the definitions' bodies agree
with the note on `[0,1]`; the continuity encodings and negations are right;
`residual_ne_of_leftContinuous` has a weaker hypothesis than left-continuity,
so is stronger; the `sSup` is never a junk value on the theorems' domains.

Qualifications that must travel with the verdict: (i) the "border-continuous"
statements are correct only under the note's joint-continuity reading (F1),
which I judge the right one; (ii) the Lean side does **not** establish that
`I_c`, `J_c` are fuzzy implications, hence not that they are (S,N)-/QL-
implications in the sense of the definitions, nor the Corollary or Lemmas 1–3
in general form (F2, F3); `min_isTNorm` is not registered (F4); (iii) this
review did not run Lean and did not check the receipt; it covers statement
fidelity at commit `f5de051` only, not novelty, not the correctness of the
note's prose proofs, and not the claim that the registry statement fingerprints
are current. It does not support marking the formal status of the *whole*
CJ-0024 claim (Corollary included) `complete`; it supports it for the 25
theorems as listed.
