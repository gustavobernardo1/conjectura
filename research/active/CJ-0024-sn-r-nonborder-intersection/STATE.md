# CJ-0024 — (S,N)- and QL-implications among residuals of non-border-continuous t-norms — investigation state

Last updated: 2026-11-27 (session 1). This file is the current truth about the
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
| A | For 1 < c < 2, T_c (max(0, x+y−c) inside, min on the lines x = 1, y = 1) is a non-border-continuous t-norm with residual I_c = min(1, c−x+y) (x < 1), y (x = 1); I_c = S_L(N_c(x), y) = S_L(N_c(x), min(x,y)); I_c(c−1, 0) = 1, so I_c is not the residual of any left-continuous t-norm; I_c ≠ I_WB. | candidate proof (note §4); exact rational grid check passed | [`notes/weber-uniqueness.md`](notes/weber-uniqueness.md) Theorem A; `experiments/CJ-0024-sn-r-nonborder-intersection/check_examples.py` |
| B | Same for T'_c (min if x+y > c, else 0, inside; min on the lines), residual J_c, t-conorm S*_c (max if a+b < c, else 1). | candidate proof; exact grid check passed | note Theorem B; same script |
| L1–L4 | Drastic-boundary lemma, residual lemma, threshold-minimum associativity, (OP)-type property of residuals of left-continuous t-norms. | candidate proof | note §4 |

## Conjectures and hypotheses of this investigation

- The intersection I_{S,N} ∩ (I_T \ I_{T*}) is large; a characterisation may
  run through t-norms obtained from t-subnorms by the drastic boundary (open,
  no evidence beyond the two families).

## Failed approaches and refuted hypotheses

None yet.

## Counterexamples and observations

- I_c and J_c share the natural negation N_c but differ: two (S,N)-representations
  with the same non-continuous negation and different t-conorms.

## Dependency map

Corollary (answers to 4.2(i), 4.8.1, first question of 4.5(ii)) ← Theorems A,
B ← Lemmas 1–4. Nothing external except the definitions.

## Decisions

- 2026-11-27 (director, via the session mission): CJ-0001 paused; this
  investigation opened in the fuzzy-mathematics campaign.

## Open obligations

1. Independent adversarial review of revision 1 of the note (running in
   session 1; report due in `reviews/`).
2. Literature audit: has any of the problems been answered after 2013, or do
   the examples appear in the literature (running; report due in
   `research/candidates/CJ-0024-sn-r-nonborder-intersection-audit.md`).
3. Lean formalization of Theorem A (running in session 1, file
   `formalization/Conjectura/Research/WeberUniqueness.lean`).

## Remaining obstacles

None for the existence answers. The characterisation parts are open.

## Next step

Read the review and the audit; correct the note in a revision 2 if needed;
then attempt CJ-0026 (Problem 9.4(iii) of the 2010 paper) with the
drastic-boundary construction.

## Sources

- <https://people.iith.ac.in/jbala/publications/book_chapters/mb_bj_adv_fi.pdf> (read 2026-11-27)
- <https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf> (read 2026-11-27)
