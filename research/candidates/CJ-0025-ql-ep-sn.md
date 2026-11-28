# CJ-0025 — Does every QL-implication satisfying (EP) coincide with an (S,N)-implication?

*Compiled 2026-11-27 by `claude-opus-5-5` (director). Not audited.*

## Statement

Verbatim from M. Baczyński, B. Jayaram, *QL-implications: some properties and
intersections*, Fuzzy Sets Syst. 161 (2010) 158–188, Section 9, p. 187:

> Problem 9.3. (i) Is Theorem 6.2 true even when N is not continuous, i.e., is
> any QL-implication I_{T,S,N} that satisfies (EP) also an (S,N)-implication?
> (ii) If not, give a counter-example and hence obtain an alternate necessary
> and sufficient condition for a QL-implication I_{T,S,N} to satisfy (EP).

Context, same page: "all the examples, so far, seem to point that a
QL-implication that satisfies (EP) also turns out to be an (S,N)-implication."

**Source.** Author copy <https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf>,
read as a text extraction on 2026-11-27.

**Statement checked against:** primary-source.

## Definitions and hypotheses

QL-operation I(x,y) = S(N(x), T(x,y)) for a t-norm T, a t-conorm S and a
fuzzy negation N (Definition 4.1); a QL-implication is a QL-operation that is
a fuzzy implication. (EP): I(x, I(y,z)) = I(y, I(x,z)). Theorem 6.2 (after
Mas et al.) treats continuous N. A QL-implication has natural negation N, so
an (S,N)-representation would have to be S'(N(x), y) for some t-conorm S'.

## Open-status evidence

Posed in 2010. The 2013 chapter by the same authors (STUDFUZZ 300, Section 4)
lists Problems 9.1 and 9.4(i),(ii) of the 2010 paper as still open but not
Problem 9.3; whether it was answered in between is unknown. A literature audit
was requested on 2026-11-27.

## Computational and mathematical approaches

An answer "no" needs one QL-implication with a non-continuous N that satisfies
(EP) but is not of the form S'(N(x), y). Natural sources: the t-norms obtained
from t-subnorms by the drastic boundary (Lemma 1 of
`research/active/CJ-0024-sn-r-nonborder-intersection/notes/weber-uniqueness.md`),
non-continuous negations with flat pieces, and QL-operations in which T(x,y)
differs from y on a set where S(N(x), ·) is not constant. Candidates are
piecewise linear and can be checked exactly on rational grids; a proof on
[0,1] is then written by hand.

## Unverified items

The status after 2010; Theorem 6.2's exact hypotheses beyond continuity of N
(not re-read); later literature.

## Known partial results

- For continuous N, a QL-implication satisfies (EP) iff it is the (S,N)-implication of the same S and N (Theorem 6.2 of the 2010 paper, after Mas, Monserrat, Torrens) — source fetched (statement located, proof not re-read).

## Relevant literature

- Baczyński, Jayaram, FSS 161 (2010) 158–188 — <https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf>
- Baczyński, Jayaram, STUDFUZZ 300 (2013) 177–204 — <https://people.iith.ac.in/jbala/publications/book_chapters/mb_bj_adv_fi.pdf>

## Novelty search coverage and limitations

Only the two sources above were read (2026-11-27). No citation trail yet; an audit was requested.

## Computational approaches

Exact rational-grid checks of piecewise-linear (T,S,N) candidates; finite-chain enumeration of QL-operations with SAT as a source of shapes (finite results do not transfer to [0,1] without proof).

## Mathematical approaches

See "Computational and mathematical approaches" above.

## Formalization feasibility

An explicit counterexample is elementary real arithmetic plus case splits; feasible in Lean with Mathlib (see the CJ-0024 formalization for the encoding).

## Prerequisites

t-norms and t-conorms, fuzzy negations, the (S,N)-, R- and QL-implication families, the exchange principle.
