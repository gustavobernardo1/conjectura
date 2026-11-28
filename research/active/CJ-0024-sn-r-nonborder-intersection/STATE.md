# CJ-0024 — (S,N)- and QL-implications among residuals of non-border-continuous t-norms — investigation state

Last updated: 2026-11-27 (session 1, about 23:50). This file is the current truth about the
investigation and must be sufficient, on its own, for a new agent to continue.
The investigation also covers CJ-0023 (same construction answers both).

## Exact statement

- **CJ-0024** = Problem 4.2 of Baczyński–Jayaram, *Fuzzy Implications: Some
  Recently Solved Problems*, STUDFUZZ 300 (2013) 177–204, p. 202: "(i) Is
  there a fuzzy implication I, other than the Weber implication I_WB, which is
  both an (S,N)-implication and an R-implication which is obtained from a
  non-border continuous t-norm and cannot be obtained as the residual of any
  other left-continuous t-norm? (ii) If the answer to the above question is in
  the affirmative, characterize the above non-empty intersection." Monograph
  form (Problem 4.8.1 of STUDFUZZ 231, 2008, quoted in the chapter, §3.1.3):
  "is the following equality true I_{S,N} ∩ (I_T \ I_{T*}) = {I_WB}?"
- **CJ-0023** = Problem 4.5(ii) of the same chapter = Problem 9.4(ii) of
  Baczyński–Jayaram, FSS 161 (2010) 158–188: "Is the Weber implication I_WB
  the only QL-implication that is also an R-implication obtained from a
  non-left continuous t-norm? If not, give other examples from the above
  intersection and hence, characterize the non-empty intersection I_QL ∩ I_T."

## Definitions and conventions

As in the sources; collected in §2 of
[`notes/weber-uniqueness.md`](notes/weber-uniqueness.md). R-implication:
I_T(x,y) = sup{t ∈ [0,1] : T(x,t) ≤ y}, any t-norm. Border-continuous:
continuous on [0,1]² \ ]0,1[². QL-operation: S(N(x), T(x,y)).

## Status

CJ-0024 and CJ-0023: mathematical `candidate-counterexample`, formal
`not-started`, novelty `unknown`, external review `not-reviewed` (catalogue).

## Established results

| ID | Statement | Level | Evidence |
| --- | --- | --- | --- |
| C | Theorem C (`notes/rescaled-tnorms.md`): any left-continuous T₀ with strong natural negation (fixed point e), rescaled into [0,a] by an increasing bijection ψ and closed by the drastic boundary, has residual = S(N(x),y) = S(N(x),min(x,y)) (truncated N₀-dual S, truncated N₀); a ≤ e gives I_WB; e < a < 1 gives (OP) failure, non-border-continuity, ≠ I_WB. A and B are the cases T_L, T_nM. MD-0029. | candidate proof; exact grid check (30 configurations) passed; review running | `notes/rescaled-tnorms.md`; `check_theorem_c.py` |
| A | For 1 < c < 2, T_c (max(0, x+y−c) inside, min on the lines x = 1, y = 1) is a non-border-continuous t-norm with residual I_c = min(1, c−x+y) (x < 1), y (x = 1); I_c = S_L(N_c(x), y) = S_L(N_c(x), min(x,y)); I_c(c−1, 0) = 1, so I_c is not the residual of any left-continuous t-norm; I_c ≠ I_WB. | candidate proof (note §4, revision 2); exact grid check passed; review 1 (Opus, gaps G1–G5 in side claims only), recheck of revision 2 (Sonnet): no gap found; Lean: see obligations | MD-0027; [`notes/weber-uniqueness.md`](notes/weber-uniqueness.md) Theorem A; `experiments/CJ-0024-sn-r-nonborder-intersection/check_examples.py` |
| B | Same for T'_c (min if x+y > c, else 0, inside; min on the lines), residual J_c, t-conorm S*_c (max if a+b < c, else 1). | as for A | MD-0028; note Theorem B; same script |
| L1–L4 | Drastic-boundary lemma, residual lemma, threshold-minimum associativity, (OP)-type property of residuals of left-continuous t-norms. | candidate proof | note §4 |

## Conjectures and hypotheses of this investigation

- The intersection I_{S,N} ∩ (I_T \ I_{T*}) is large; a characterisation may
  run through t-norms obtained from t-subnorms by the drastic boundary (open,
  no evidence beyond the two families).

## Failed approaches and refuted hypotheses

None yet.

## Counterexamples and observations

- Printed Theorem 6.5 of the 2008 survey (= Theorem 5.14 of the 2010 paper),
  "for a right-continuous t-conorm S and a t-norm T", is contradicted by
  I_WB = I_{S_M,N_D2} = I_{T_D} (the survey's own Remark 6.4(i), printed just
  before it, which says left-continuity of T "is very important") and by
  J_c = I_{S*_c,N_c}. Almost certainly a missing hypothesis (T
  left-continuous), not a discovery. Recorded in note revision 2, §5.
- Observation (proved in one line, not registered): in a QL-implication
  S(N(x),T(x,y)), N(x₁) = N(x₂) implies I(x₁,·) = I(x₂,·) (I1 gives ≥,
  monotonicity of S and T gives ≤). So a residual whose natural negation is
  constant on an interval on which I_T(x,·) varies is not QL (e.g. the T_Z of
  EUSFLAT 2011, Example 4.4).
- Toward CJ-0026 (Problem 9.4(iii) of 2010): I(x,y) = min(1, N_c(x) + xy)
  (x < 1), y (x = 1) is a QL-implication (T_P, S_L, N_c) for c ≥ 5/4 and is
  not an (S,N)-implication (the would-be t-conorm p + (c−p)y is not
  symmetric); it is not an R-implication either (recovering T from it breaks
  commutativity; argument sketched, not written). Toward CJ-0025 (Problem
  9.3(i)): with S_L and N_c, (EP) at z = 0 forces T(x,c−y) + y = T(y,c−x) + x,
  which T_M satisfies and T_L, T_P do not; no counterexample found.

- I_c and J_c share the natural negation N_c but differ: two (S,N)-representations
  with the same non-continuous negation and different t-conorms.

## Dependency map

Corollary (answers to 4.2(i), 4.8.1, first question of 4.5(ii)) ← Theorems A,
B ← Lemmas 1–4. Nothing external except the definitions.

## Decisions

- 2026-11-27 (director, via the session mission): CJ-0001 paused; this
  investigation opened in the fuzzy-mathematics campaign.

## Open obligations

1. Done: review of revision 1 (`reviews/2026-11-27-review-1.md`, gaps
   G1–G5), revision 2 (`notes/weber-uniqueness.md`; revision 1 in
   `notes/versions/`), recheck of revision 2 by a different model
   (`reviews/2026-11-27-recheck-r2.md`, claude-sonnet-5-5): no gap found
   within stated scope. Per skill `review-claim` step 5 the director may now
   set `external_review` of CJ-0024/CJ-0023 to `ai-reviewed`; not done by
   the session. No human has read the proof.
2. Done: literature audit (`research/candidates/CJ-0024-sn-r-nonborder-intersection-audit.md`).
   Still owed: the 2015 handbook chapter (doi:10.1007/978-3-662-43505-2_12)
   and the 2008 monograph, which were not accessible; zbMATH/MathSciNet.
3. Lean formalization of Theorems A and B (session 1, file
   `formalization/Conjectura/Research/WeberUniqueness.lean`): see the journal
   for its outcome; the comparison of the Lean statements with the written
   ones needs an independent check before `formal: complete`.
4. Review of Theorem C (`notes/rescaled-tnorms.md`): running at the end of
   session 1; see `reviews/`.
5. Manuscript draft `manuscripts/CJ-0024-weber-uniqueness/main.tex` (4 pages)
   not yet reviewed as a whole; a result package under `results/` is for a
   later session (no promotion in the session that produced the claim).

## Remaining obstacles

None for the existence answers. The characterisation parts are open.

## Next step

Read the review of Theorem C in `reviews/` and correct `notes/rescaled-tnorms.md`
in a revision 2 if it found gaps; then have the manuscript
`manuscripts/CJ-0024-weber-uniqueness/main.tex` reviewed as a whole and, after
the director's decision on `external_review`, assemble the result package.
Mathematics next: CJ-0026 (Problem 9.4(iii) of the 2010 paper), using the
observations above.

## Sources

- <https://people.iith.ac.in/jbala/publications/book_chapters/mb_bj_adv_fi.pdf> (read 2026-11-27)
- <https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf> (read 2026-11-27)
