# CJ-0024 — A second implication that is both an (S,N)- and an R-implication from a non-border-continuous t-norm?

*Compiled 2026-11-27 by the problem-scout subagent (model Sonnet 5.5). Not audited.*

## Statement

Verbatim from the primary source (page 202 of the chapter, read from a downloaded PDF image):

"Problem 4.2. (i) Is there a fuzzy implication I, other than the Weber implication I_WB, which is both an (S,N)-implication and an R-implication which is obtained from a non-border continuous t-norm and cannot be obtained as the residual of any left-continuous t-norm?
(ii) If the answer to the above question is in the affirmative, characterize the above non-empty intersection."

Context in the same chapter: "Once again, as stated before, the above problem is also related to the following question regarding the intersection of (S,N)- and R-implications which still remains open:" (the sentence introduces Problem 4.2, after Problem 4.1: "Give a necessary condition on a non-border continuous t-norm T for the corresponding I_T to satisfy (EP).").

**Source.** M. Baczyński, B. Jayaram, "Fuzzy Implications: Some Recently Solved Problems", Advances in Fuzzy Implication Functions, STUDFUZZ 300, pp. 177-204, Springer 2013, DOI 10.1007/978-3-642-35677-3_8, Section 4, Problem 4.2. Author-hosted PDF https://people.iith.ac.in/jbala/publications/book_chapters/mb_bj_adv_fi.pdf (fetched 2026-11-27).

**Statement checked against:** primary-source, but the key terms ("non-border continuous t-norm", Weber implication) were defined on pages not read.

## Definitions and hypotheses

Fuzzy implication: Definition 2.1 of the chapter (I1, I2, I(0,0)=I(1,1)=1, I(1,0)=0), read verbatim. (S,N)-implication I(x,y)=S(N(x),y) (recalled, not read). R-implication: residual of a t-norm (the chapter's (3), not read). "Non-border continuous": not defined in the pages read; border continuity presumably concerns continuity of T on the boundary of the unit square (UNVERIFIED). The task is existential: one explicit I, with (S,N) representation and R-representation from a non-border-continuous t-norm that is not an I_T of any left-continuous T.

## Known partial results

- Jayaram, Baczyński, Mesiar, "R-implications and the exchange principle: the case of border continuous t-norms", FSS (listed as ref. 21 of the chapter as "submitted"; publication status not verified) and EUSFLAT 2011 conference paper (ref. 20).
- Related results on the intersection of (S,N)- and R-implications for continuous cases: Baczyński and Jayaram, FSS 159 (2008) 1836-1859 (ref. 3, not read).

## Relevant literature

- Baczyński, Jayaram, Fuzzy Implications, STUDFUZZ 231, Springer 2008 (cited as the source of the original problems; not read).
- Fernández-Peralta, Massanet, Mesiarová-Zemánková, Mir, FSS 441 (2022) 1-32, doi:10.1016/j.fss.2021.06.009 (abstract read via a secondary page): on (S,N)-implications with non-continuous negations; relevant because non-continuous N is the setting where such intersections occur.

## Open-status evidence

Same as CJ-0023: the 2013 chapter says the problem "still remains open". OpenAlex (fetched 2026-11-27) lists four citing works (2015 handbook chapter; FSS 2023 "Order from non-associative operations"; FSS 2025 "Representations of the fuzzy implications satisfying the law of left or right contraposition"; a 2021 conference paper); none opened. Open status after 2013 is unverified. Evidence is old.

## Novelty search coverage and limitations

Two web searches, one OpenAlex citation query, 2026-11-27. Not read: monograph, 2015 handbook chapter, the EUSFLAT 2011 and FSS papers on R-implications and the exchange principle, Fernández-Peralta et al. 2022 full text. Unknown whether the question has since been answered; a failed search does not establish openness.

## Computational approaches

Finite-chain analogue: enumerate discrete t-norms, t-conorms and negations on {0,...,n}, list the (S,N)-implications and R-implications and their intersection, then look for patterns that a [0,1] example could generalise. A [0,1] counterexample would be an explicit pair (T,I) checked symbolically. The search is conditional on pinning down "non-border continuous" first.

## Mathematical approaches

Use the characterization of R-implications from arbitrary t-norms (Jayaram, Baczyński, Mesiar) and compute I_T for non-border-continuous T built from ordinal sums with a discontinuity at the border; test whether I_T has the form S(N(x),y), which forces I_T(x,0) = N(x) and I_T(1,y)=y.

## Formalization feasibility

As for CJ-0023: no fuzzy-logic library in Mathlib; a concrete example would be a statement about explicit real functions.

## Prerequisites

t-norm theory, residuals, the exchange principle, (S,N)-implications.

## Unverified items

- Definition of "non-border continuous t-norm" and of the Weber implication.
- Whether the question has been answered after 2013.
- Publication status of refs. 20 and 21 of the chapter.
- The relation to CJ-0023 (both rely on the Weber implication being the known example).
