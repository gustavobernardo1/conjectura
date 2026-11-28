# CJ-0038 — Amalgamation property for commutative (and integral) cancellative semilinear residuated lattices

*Compiled 2026-11-27 by the problem-scout subagent (model claude-sonnet-5-5). Not audited. The statements below come from a summarising fetch of the ar5iv rendering and are not verified verbatim.*

## Statement

Fussner and Santschi, "Amalgamation in Semilinear Residuated Lattices", arXiv:2407.21613 (submitted 31 July 2024; published Studia Logica 2025, DOI 10.1007/s11225-025-10206-9 per OpenAlex). As reported by the fetch of https://ar5iv.labs.arxiv.org/html/2407.21613:

- Question 6.9 (cited from [24], Problem 6): "Does the variety of commutative cancellative semilinear residuated lattices have the amalgamation property?"
- Question 6.10 (cited from [24], Problem 2): "Does the variety of integral cancellative semilinear residuated lattices have the amalgamation property?"

The introduction reportedly says the remaining open problems are "confined to the vicinity of cancellative semilinear residuated lattices". Appendix A, Table 1 marks both with "?".

**Source.** arXiv:2407.21613, Questions 6.9 and 6.10. Reference [24] was not identified.

**Statement checked against:** secondary-source (summarised fetch of the ar5iv rendering).

## Definitions and hypotheses

Semilinear: subdirect product of chains. Cancellative: x*z = y*z implies x = y (and the left version). AP: every V-formation of members of the variety embeds in a common member. A negative answer is settled by ONE explicit V-formation (A, B, C with embeddings of A into B and C) that has no amalgam in the variety. Note: related negative results in the same area: the variety of all semilinear cancellative residuated lattices (non-commutative) fails AP (Gil-Ferez, Ledda, Tsinakis, via a web-search summary; not fetched); commutative semilinear residuated lattices fail AP (Fussner-Santschi abstract). Both questions are therefore about the commutative and the integral cancellative subvarieties.

## Known partial results

- Fussner, Santschi, arXiv:2407.21613: survey; commutative semilinear RL fail AP; open problems concentrated in the cancellative case. (abstract fetched)
- Giustarini, Ugolini, arXiv:2408.17400 (v3, 19 Dec 2025): "we solve in the negative several longstanding open problems in the literature about the amalgamation property (AP)", covering semilinear integral RLs, MTL-algebras and related classes; the page did not say what remains open. (abstract fetched)
- Jipsen, Santschi, arXiv:2504.16111 (v2 20 March 2026): residuated lattices do not have AP. (abstract fetched)

## Relevant literature

- https://arxiv.org/abs/2407.21613, https://arxiv.org/abs/2408.17400, https://arxiv.org/abs/2504.16111

## Open-status evidence

Fussner-Santschi (2024, published 2025) mark both as open. OpenAlex (2026-11-27) lists 11 papers citing the published version, none with a title indicating cancellative semilinear AP; titles only, so none was read. Giustarini-Ugolini (v3 December 2025) may have settled one of the two; its page did not say. This is the main risk: check Section 1 of 2408.17400 and the 2025 citing papers "Interpolation in Hajek's basic logic" and "Interpolation and Amalgamation" first.

## Novelty search coverage and limitations

2026-11-27: about eight fetches (arXiv abstracts, ar5iv, OpenAlex citation list) and two web searches. Not checked: full text of 2408.17400, 2504.16111 and 2310.14953, zbMATH, Semantic Scholar, reference [24] of Fussner-Santschi (the source of the problems), any 2026 citing paper's content.

## Computational approaches

Cancellative chains are infinite, so finite enumeration is not available. Exact work is possible with finitely presented examples: e.g. subalgebras of ordered abelian groups with explicit negative cones (Z-lex products), checking a candidate V-formation by exact integer arithmetic. A search for non-amalgamable V-formations among small-rank lattice-ordered-group-like chains is possible but not routine.

## Mathematical approaches

Adapt the blockwise-gluing and V-formation arguments of 2408.17400 and the weakly abelian l-group failure of AP to the commutative cancellative setting; or prove AP via a known amalgamation of abelian l-groups plus a Galatos-Tsinakis style equivalence between integral residuated lattices and l-groups with nuclei. Tractability is low: specialists have worked on these questions.

## Formalization feasibility

Mathlib lacks residuated lattices and V-formations. Only an explicit finite-presentation counterexample over integers would be formalizable; unlikely soon. Low.

## Prerequisites

Universal algebra (amalgamation, V-formations), residuated lattices, lattice-ordered groups.

## Unverified items

The exact wording of Questions 6.9 and 6.10, the identity of reference [24], whether either was settled after 2024, and whether the "cancellative commutative" and "integral cancellative" varieties are as defined above (definitions not captured).
