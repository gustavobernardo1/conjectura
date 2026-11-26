# CJ-0003 — Lieb's permanental dominance conjecture

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Quoted from Zhang (arXiv:1608.02844, Section 4): 'Lieb permanent dominance conjecture 1966 [28]. Let H be a subgroup of the symmetric group S_n and let \chi be a character of degree m of H. Then (1/m) \sum_{\sigma \in H} \chi(\sigma) \prod_{i=1}^n a_{i\sigma(i)} <= per A (10) holds for all n x n positive semidefinite Hermitian A.' Here per A = \sum_{\sigma \in S_n} \prod_i a_{i\sigma(i)}; the left side is the normalized generalized matrix function d^H_\chi(A)/\chi(e). Important special case (H = S_n, \chi irreducible): every normalized immanant of a PSD matrix is at most its permanent.

**Source.** E. H. Lieb (1966), as stated in F. Zhang, An update on a few permanent conjectures, arXiv:1608.02844 (2016), Section 4, inequality (10). <https://arxiv.org/abs/1608.02844>

**Statement checked against:** secondary-source. Statement quoted from Zhang's survey; Lieb's 1966 paper was not accessed.

## Definitions and hypotheses

A is complex Hermitian positive semidefinite, n x n; H is ANY subgroup of S_n; \chi is any character of H (not necessarily irreducible) of degree m = \chi(e). For m = 1 this is the Marcus–Minc question. Names are confused in the literature (Zhang's note): some authors call this inequality the 'permanent-on-top' conjecture; the genuinely stronger Soules permanent-on-top (POT) conjecture (per A is the largest eigenvalue of the Schur power matrix) is FALSE (Shchesnovich 2016, a 5x5 rank-2 complex example), so proofs must not go through POT. Zhang's implication diagram: Soules POT implies Lieb per-dom, which implies Marcus per-in-per; POT also implies Bapat–Sunder (false), which implies Chollet.

## Known partial results

- Schur's inequality det A <= d^H_\chi(A)/\chi(e) (the determinantal counterpart, a theorem); Lieb's inequality per A >= per A_11 per A_22; Merris's upper bound (1/m) d^H_\chi(A) <= (\prod_i (A^n)_{ii})^{1/n} <= (1/n) \sum \lambda_i^n. — F. Zhang, arXiv:1608.02844, Sections 2 and 4 <https://arxiv.org/abs/1608.02844> (source fetched)
- Permanent dominance is true for immanants (H = S_n, \chi irreducible) with n <= 13 (Pate). — F. Zhang, arXiv:1608.02844, Section 4 <https://arxiv.org/abs/1608.02844> (source fetched)
- POT conjecture true for n <= 3 (Bapat–Sunder 1986) and false for n = 5 (Shchesnovich 2016); whether a 4x4 POT counterexample exists is Zhang's Question 1. — F. Zhang, arXiv:1608.02844, Section 3 <https://arxiv.org/abs/1608.02844> (source fetched)
- Claimed (single-author, unrefereed): the ordinary irreducible-immanant case for every partition of n <= 15, settling (4,4,3,3) at order 14 and (5,4,3,3), (3^5) at order 15, with exact integer/rational certificates and a Lean 4 kernel-checked 'order-14 bridge'. According to the abstract, Pate had proved order <= 13 and all order-14 partitions except (4,4,3,3). — Yinjie Li, 'Lieb's Permanental Dominance Conjecture for Ordinary Immanants through Order Fifteen', arXiv:2609.13412 (11 September 2026, v1; abstract page fetched) <https://arxiv.org/abs/2609.13412> (source fetched)
- Survey of the conjecture and its relatives ('remains open 56 years later' per search snippet). — I. M. Wanless, 'Lieb's permanental dominance conjecture', arXiv:2202.01867 / EMS Press book chapter (search snippets only) <https://arxiv.org/abs/2202.01867> (source not fetched)
- Titles surfaced but not read: 'The General Subgroup Permanental-Dominance Conjecture in Order Four' (arXiv:2608.21749); 'Some remarks on permanent dominant conjecture' (arXiv:2303.00316). — Search results only <https://arxiv.org/abs/2608.21749> (source not fetched)

## Relevant literature

- E. H. Lieb (1966), as stated in F. Zhang, An update on a few permanent conjectures, arXiv:1608.02844 (2016), Section 4, inequality (10). <https://arxiv.org/abs/1608.02844>
- F. Zhang, arXiv:1608.02844, Sections 2 and 4 <https://arxiv.org/abs/1608.02844>
- F. Zhang, arXiv:1608.02844, Section 4 <https://arxiv.org/abs/1608.02844>
- F. Zhang, arXiv:1608.02844, Section 3 <https://arxiv.org/abs/1608.02844>
- Yinjie Li, 'Lieb's Permanental Dominance Conjecture for Ordinary Immanants through Order Fifteen', arXiv:2609.13412 (11 September 2026, v1; abstract page fetched) <https://arxiv.org/abs/2609.13412>
- I. M. Wanless, 'Lieb's permanental dominance conjecture', arXiv:2202.01867 / EMS Press book chapter (search snippets only) <https://arxiv.org/abs/2202.01867>
- Search results only <https://arxiv.org/abs/2608.21749>

## Open-status evidence

- Most recent source: Yinjie Li, arXiv:2609.13412 (abstract page fetched)
- URL: <https://arxiv.org/abs/2609.13412>
- Date: 2026-09-11
- Content: The abstract claims only the irreducible-immanant case for n <= 15 ('These three cases are settled here') and discusses the limits of its method; nothing is claimed for n >= 16 or for general subgroups H, so the general conjecture is still treated as open. Zhang 2016 section title: 'The permanent dominance conjecture is open'.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- Lieb permanental dominance conjecture 2025 OR 2026 proof OR counterexample OR "still open" immanant

Sources checked:

- General web search (1 dedicated query plus 2 neighbouring permanent-conjecture queries)
- F. Zhang survey arXiv:1608.02844 (PDF pages 1–13 read)
- arXiv abstract page 2609.13412

Limitations: Wanless's survey (the authoritative status reference) was not fetched. The order-four general-subgroup paper (arXiv:2608.21749) was not read, so the smallest open case for general (H, \chi) is not established here. No arXiv listing, MathOverflow or Scholar search.

## Computational approaches

For fixed small n one can enumerate conjugacy classes of subgroups H <= S_n and their irreducible characters (GAP/SymPy/Sage) and test (1/\chi(e)) d^H_\chi(A) <= per A numerically over PSD A (Gram matrices of low-rank complex vectors), then look for exact certificates. Sizes: S_4 has 11 conjugacy classes of subgroups, S_5 has 19, S_6 has 56 (from memory). Immanant case: literature claims n <= 13 (Pate, per Zhang) and n <= 15 (2026 preprint, unrefereed). Useful reduction: it suffices to consider irreducible characters of H, and the Schur power matrix restricted to isotypic subspaces turns each case into an eigenvalue comparison.

## Mathematical approaches

Schur power matrix and its numerical range; Pate's inductive/branching techniques on partitions for immanants; Soules's necessary conditions; character-theoretic positivity (monomial immanant / Stembridge-type conjectures in the totally positive setting are related but different); induced characters from subgroups to S_n (reduces general H to combinations of immanants only when coefficients are nonnegative, which is exactly where difficulty lies).

Scout's tractability assessment: Famous and very hard; included as one of the two 'hard' items because finite cases are exactly checkable and the frontier is concrete (immanants: next unclaimed order is 16 if the 2026 preprint holds; general subgroups: small n). Classical techniques have been pushed hard from the late 1960s to the 1990s (Zhang). Realistic contributions: independent re-verification / Lean checking of claimed finite certificates, exhaustive treatment of all (H, \chi) for n = 4 or 5 (check arXiv:2608.21749 first), and numerical counterexample searches for non-immanant (H, \chi) at n = 5..7 using the rank-deficient complex matrices that broke POT.

## Formalization feasibility

Not checked in this session. From memory: Mathlib has Matrix.permanent, PosSemidef, Equiv.Perm and subgroups; class functions/characters exist only in a basic form (characters of FDRep), and immanants are not defined, so stating the conjecture needs a modest amount of new definitions. The 2026 preprint reports a Lean 4 formalization of one finite certificate (not verified by me).

## Prerequisites

Positive semidefinite matrices, permanents, representation theory of finite groups and of S_n (characters, partitions, branching rule), tensor/Schur power constructions, computer algebra (GAP/Sage).

## Unverified items

- Title/journal of Lieb's 1966 paper (from memory).
- Wanless survey content and the '56 years later' quote (search snippet).
- Correctness of arXiv:2609.13412 (unrefereed; only the abstract was read).
- Contents of arXiv:2608.21749 and arXiv:2303.00316 (titles only).
- Subgroup-class counts for S_4, S_5, S_6 (from memory).
- A search snippet mentioned counterexamples by Drury / Tran Hoang Anh to a 'Conjecture 4' in this line of work; not verified and apparently not a counterexample to Lieb's conjecture itself.
- Mathlib coverage quoted from memory.
