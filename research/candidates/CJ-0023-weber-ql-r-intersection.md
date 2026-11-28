# CJ-0023 — Is the Weber implication the only QL-implication that is also an R-implication from a non-left-continuous t-norm?

*Compiled 2026-11-27 by the problem-scout subagent (model Sonnet 5.5). Not audited.*

## Statement

Verbatim from the primary source (page 202 of the chapter, as read from a downloaded PDF image):

"Problem 4.5. (i) Characterize the non-empty intersection I_{S,N} ∩ I_{QL}.
(ii) Is the Weber implication I_WB the only QL-implication that is also an R-implication obtained from a non-left continuous t-norm? If not, give other examples from the above intersection and hence, characterize the non-empty intersection I_QL ∩ I_T."

The chapter introduces Problems 4.3-4.5 with: "The following problems originally appeared as open in [2] and still remain so" ([2] = the 2008 monograph "Fuzzy Implications", Problem numbers in the monograph not read).

This record concerns part (ii) only (a yes/no existence question; "no" is witnessed by one explicit example).

**Source.** M. Baczyński, B. Jayaram, "Fuzzy Implications: Some Recently Solved Problems", in: Baczyński et al. (eds.), Advances in Fuzzy Implication Functions, STUDFUZZ 300, pp. 177-204, Springer 2013, DOI 10.1007/978-3-642-35677-3_8, Section 4 "Concluding Remarks", Problem 4.5. Read from the author-hosted PDF https://people.iith.ac.in/jbala/publications/book_chapters/mb_bj_adv_fi.pdf (fetched 2026-11-27).

**Statement checked against:** primary-source (the problem list of the chapter). The definitions it relies on (Weber implication, QL-implication, R-implication, non-left-continuous t-norm) are in pages 3-23 and in the 2010 QL paper, which were NOT read in full; see Unverified items.

## Definitions and hypotheses

Standard definitions (to be confirmed from the sources before work starts):
- Fuzzy implication I: [0,1]^2 -> [0,1] with I1 (decreasing in x), I2 (increasing in y), I(0,0)=I(1,1)=1, I(1,0)=0 (read verbatim as Definition 2.1 in the chapter, p. 178).
- QL-operation I(x,y) = S(N(x), T(x,y)) with T a t-norm, S a t-conorm, N a fuzzy negation; QL-implication if it is a fuzzy implication (formula recalled from a search-result summary and the 2010 paper's introduction; not read verbatim).
- R-implication I_T(x,y) = sup{t : T(x,t) <= y} (the chapter's formula (3), not read verbatim). The question allows T not left-continuous, so the supremum need not be attained.
- Weber implication I_WB: definition NOT read in this session (recalled: 1 if x<1, y if x=1; unverified).

## Known partial results

- QL-implications contain all R-implications from left-continuous t-norms that are also (S,N)-implications — Baczyński and Jayaram, FSS 161 (2010) 158-188, abstract — https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf — fetched (abstract and introduction read).
- Continuity of an R-implication forces left-continuity of the t-norm (search-result summary only; not verified) — Baczyński and Jayaram line of work.

## Relevant literature

- Baczyński, Jayaram, "QL-implications: Some properties and intersections", FSS 161 (2010) 158-188, doi:10.1016/j.fss.2008.09.021.
- Baczyński, Jayaram, "(S,N)- and R-implications: a state-of-the-art survey", FSS 159 (2008) 1836-1859 (listed as ref. 3 of the chapter; not read).
- Fernández-Peralta, "A Comprehensive Survey of Fuzzy Implication Functions", arXiv:2503.05702 (read only its abstract, section 4 excerpt; no open problems there).

## Open-status evidence

The 2013 chapter (above) says the problem "still remain[s]" open as of 2013. That is 13 years old. OpenAlex (fetched 2026-11-27) lists four works citing the chapter: the 2015 Springer Handbook chapter "Fuzzy Implications: Past, Present, and Future" (doi:10.1007/978-3-662-43505-2_12), "Order from non-associative operations" (FSS 2023, doi:10.1016/j.fss.2023.02.005), "Representations of the fuzzy implications satisfying the law of left or right contraposition" (FSS 2025, doi:10.1016/j.fss.2025.109580), and a 2021 conference version of the 2023 paper. None was opened, so it is unknown whether any restates or answers the problem. The 2015 chapter is the most likely place for a restatement but is paywalled and was not read.

## Novelty search coverage and limitations

Run on 2026-11-27: two web searches on the Weber implication / QL ∩ R intersection and on QL-operations satisfying I1; OpenAlex citation list of the chapter; the abstract and first two pages of the 2010 QL paper. NOT done: full text of the 2010 QL paper (Section on intersections may already answer part (ii)), the 2008 monograph, the 2015 handbook chapter, Semantic Scholar/Google Scholar trails of the 2010 paper, MathSciNet/zbMATH. A failed search is not evidence that the problem is still open.

## Computational approaches

The question lives on [0,1], but its finite analogue is exact and cheap: on a finite chain {0,...,n} enumerate t-norms (discrete, commutative, associative, increasing, neutral n), t-conorms, negations, and compare the sets of QL-implications and R-implications (with the residual defined as a max over a finite set). The counts for discrete t-norms are known to grow fast (OEIS A367446, A367447 give enumerations of related discrete implication families; not checked here beyond their data lines), so small n (up to about 6 or 7) is feasible. The finite case cannot directly refute the [0,1] statement because left-continuity has no finite analogue; it can suggest the shape of a candidate example (non-left-continuous t-norm with ordinal-sum or drastic-like structure) to be generalised by hand and then verified exactly with piecewise-linear arithmetic on [0,1].

## Mathematical approaches

Work out which non-left-continuous t-norms T give an R-implication I_T that equals S(N(x), T'(x,y)) for some (T', S, N). Start from t-norms that are left-continuous except at a boundary (e.g. non-border-continuous modifications of the nilpotent minimum or of the drastic product) and compute I_T explicitly. A candidate answer "yes, another example exists" is a piecewise-defined function that can be checked exactly.

## Formalization feasibility

Mathlib has no fuzzy-logic library. A statement of a concrete counterexample (explicit t-norm, t-conorm, negation on ℚ ∩ [0,1] or ℝ, equalities of piecewise functions) is formalizable with moderate effort; the sup in the residual needs `sSup` over real sets. Low priority.

## Prerequisites

t-norm theory (ordinal sums, left-continuity, residuals), the QL/R/(S,N) implication families.

## Unverified items

- The definition and formula of the Weber implication, of QL-implications and of R-implications (not read verbatim).
- The meaning of "non-border continuous" (used in Problem 4.2 of the same chapter, not in 4.5(ii)).
- Whether the 2010 QL paper, the 2015 handbook chapter or any later paper answers part (ii).
- Statement numbering in the 2008 monograph.
- Any claim from search-result summaries (marked as such above).
