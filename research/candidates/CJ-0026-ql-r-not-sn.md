# CJ-0026 — Is every QL-implication that is an R-implication also an (S,N)-implication?

*Compiled 2026-11-27 by `claude-opus-5-5` (director). Not audited.*

## Statement

Verbatim from M. Baczyński, B. Jayaram, *QL-implications: some properties and
intersections*, Fuzzy Sets Syst. 161 (2010) 158–188, Section 9, p. 187:

> Problem 9.4. […] (iii) Prove or disprove by giving an example:
> (I_QL ∩ I_T) \ I_{S,N} = ∅.

Context: "it is not yet clear if there is a QL-implication which can be
represented as an R-implication of some non-left-continuous t-norm, but which
is not an (S,N)-implication."

**Source.** Author copy <https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf>,
read as a text extraction on 2026-11-27. **Statement checked against:**
primary-source.

## Definitions and hypotheses

I_QL: QL-implications (Definition 4.1); I_T: R-implications of arbitrary
t-norms (sup formula, no continuity); I_{S,N}: (S,N)-implications. By the
paper's Theorem 7.2 the R-implications of left-continuous t-norms that are
QL-implications are (S,N)-implications, so an example needs a
non-left-continuous t-norm.

## Open-status evidence

Posed in 2010; not in the 2013 chapter's list of still-open problems. Status
after 2010 unknown; audit requested 2026-11-27.

## Approaches

Every member of (I_QL ∩ I_T) found so far by the project (the families I_c,
J_c of CJ-0024) is an (S,N)-implication. A negative answer needs a residual of
a non-left-continuous t-norm, written as S(N(x), T'(x,y)), that violates (EP)
or is not of the form S'(N(x), y). Scan the drastic-boundary t-norms (Lemma 1
of the CJ-0024 note) with other t-subnorms.

## Unverified items

Status after 2010; later literature.

## Known partial results

- Theorem 7.2 of the 2010 paper: a QL-implication that is the residual of a left-continuous t-norm is an (S,N)-implication (statement located in the fetched source; proof not re-read).
- The examples I_c, J_c of CJ-0024 lie in I_QL ∩ I_T ∩ I_{S,N} (candidate, not reviewed).

## Relevant literature

- Baczyński, Jayaram, FSS 161 (2010) 158–188 — <https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf>

## Novelty search coverage and limitations

Only the 2010 paper and the 2013 chapter were read (2026-11-27). Audit requested.

## Computational approaches

Exact grid checks of the residuals of drastic-boundary t-norms built from parametrised t-subnorms; test (EP) and the (S,N) form S'(N(x), y).

## Mathematical approaches

See "Approaches" above.

## Formalization feasibility

As for CJ-0025.

## Prerequisites

As for CJ-0025.

## Director's notes, 2026-11-27 (session 1 of CJ-0024)

Local analysis with S = S_L and N(x) = c − x on ]c−1, 1[ (as in CJ-0024):
writing I(x,y) = min(1, c − x + T'(x,y)), the R-implication condition becomes
commutativity of the recovered t-norm, i.e. φ(x,s) = φ(s + c − x, s) where
φ(x,s) = inf{y : T'(x,y) ≥ s}; the (S,N) condition becomes the contrapositive
symmetry I(x,y) = I(c − y, c − x) on the region where I < 1. T' = T_M
satisfies both; T_P and ordinal sums of T_L with min fail the first. No
T' satisfying the first and failing the second was found; it is possible
that the answer to Problem 9.4(iii) is "the set is empty" (a theorem to
prove, not a counterexample). Not pursued further in this session.
