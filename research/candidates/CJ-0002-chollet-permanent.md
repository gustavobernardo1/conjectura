# CJ-0002 — Chollet's permanent conjecture

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Quoted from Zhang (arXiv:1608.02844, Section 6 'Chollet conjecture is open'): 'Chollet conjecture 1982 [10]. If A >= 0 and B >= 0 are n x n matrices, then per(A \circ B) <= per A per B (16)'. Here (Zhang, Section 2) M_n is the set of n x n complex matrices, 'A >= 0' means A is positive semidefinite (x^*Ax >= 0 for all x in C^n, hence Hermitian), per A = \sum_{\sigma \in S_n} \prod_{t=1}^n a_{t\sigma(t)}, and A \circ B = (a_{ij} b_{ij}) is the Hadamard (entrywise) product. Equivalent form (Zhang, quoting Chollet): 'Chollet showed that the inequality holds if and only if it is true when B = \bar{A}: per(A \circ \bar{A}) <= (per A)^2 (17)'. Real special case posed as Zhang's Question 9: for a real positive semidefinite A = (a_{ij}), does per((a_{ij}^2)) <= (per A)^2 hold?

**Source.** Chollet (1982), as stated in F. Zhang, An update on a few permanent conjectures, arXiv:1608.02844 (2016), Section 6, inequality (16). <https://arxiv.org/abs/1608.02844>

**Statement checked against:** secondary-source. Statement quoted from Zhang's survey; Chollet's 1982 paper was not accessed.

## Definitions and hypotheses

A and B are complex Hermitian positive semidefinite of the same size n (n >= 2 in Zhang's survey). The inequality is the reverse-direction permanental analogue of Oppenheim's determinant inequality det(A \circ B) >= det A det B. It is strictly weaker than the Bapat–Sunder conjecture per(A \circ B) <= per A * b_11...b_nn, which is FALSE (Drury 2016: complex 7x7 rank-2 correlation matrices; a real 16x16 example also reported), so approaches via Bapat–Sunder or permanent-on-top are dead. Drury's 7x7 example does not violate Chollet (Zhang: per(A \circ \bar A) = 6185/128 < 45^2). Complex and real cases differ in difficulty; state which one is being attacked. The reduction to B = conj(A) (not B = A) is essential in the complex case.

## Known partial results

- True for 2x2 and 3x3 matrices (Gregorac and Hentzel 1987, elementary; also follows from Bapat–Sunder 1986 results for n <= 3). — As reported in F. Zhang, arXiv:1608.02844, Section 6 <https://arxiv.org/abs/1608.02844> (source fetched)
- Equivalence with the case B = conj(A), i.e. per(A \circ \bar A) <= (per A)^2 (Chollet), via Cauchy–Schwarz. — As reported in F. Zhang, arXiv:1608.02844, Section 6 <https://arxiv.org/abs/1608.02844> (source fetched)
- Stronger Bapat–Sunder conjecture and permanent-on-top conjecture are false (Drury 2016; Shchesnovich 2016), so Chollet 'stands out' as the surviving statement in that chain. — F. Zhang, arXiv:1608.02844, Sections 3 and 5 <https://arxiv.org/abs/1608.02844> (source fetched)
- Real 4x4 case proved (Hutchinson, Special Matrices, 2021). — Search-result snippet (DOAJ listing of Special Matrices, Jan 2021); paper not fetched <https://doaj.org/article/e017fa3f8f3c403d8cdb939d7a8fd906> (source not fetched)
- Complex 4x4 case claimed: 'Chollet's permanent conjecture for 4x4 matrices'. — arXiv:2211.02839 (title and claim from search results; attributed to Rodtes in the snippet; not fetched) <https://arxiv.org/abs/2211.02839> (source not fetched)
- Structural classes: a stronger inequality for a broad class of matrices with bipartite support; a 'one-point sum' operation on PSD matrices preserving Chollet's inequality under conditions; for graph Laplacians this is vertex coalescence, giving larger graph families satisfying the inequality. — P. Pant, R. Singh, 'Structural Classes for Chollet's Permanent Conjecture', arXiv:2604.24192 (v1 27 April 2026, v3 21 November 2026; abstract page fetched) <https://arxiv.org/abs/2604.24192> (source fetched)
- Unrefereed preprint claims the conjecture for complex Hermitian PSD matrices through order six; a second preprint treats per(C \circ C) <= per(C)^2 for real correlation matrices with computer certificates; an arXiv paper gives 'Quantitative Chollet inequalities for matrices of rank at most four'. — preprints.org 202608.2196 and 202608.1346 (fetch returned HTTP 403; search snippets only); arXiv:2609.37461 (title from search results only) <https://www.preprints.org/manuscript/202608.2196> (source not fetched)

## Relevant literature

- Chollet (1982), as stated in F. Zhang, An update on a few permanent conjectures, arXiv:1608.02844 (2016), Section 6, inequality (16). <https://arxiv.org/abs/1608.02844>
- As reported in F. Zhang, arXiv:1608.02844, Section 6 <https://arxiv.org/abs/1608.02844>
- F. Zhang, arXiv:1608.02844, Sections 3 and 5 <https://arxiv.org/abs/1608.02844>
- Search-result snippet (DOAJ listing of Special Matrices, Jan 2021); paper not fetched <https://doaj.org/article/e017fa3f8f3c403d8cdb939d7a8fd906>
- arXiv:2211.02839 (title and claim from search results; attributed to Rodtes in the snippet; not fetched) <https://arxiv.org/abs/2211.02839>
- P. Pant, R. Singh, 'Structural Classes for Chollet's Permanent Conjecture', arXiv:2604.24192 (v1 27 April 2026, v3 21 November 2026; abstract page fetched) <https://arxiv.org/abs/2604.24192>
- preprints.org 202608.2196 and 202608.1346 (fetch returned HTTP 403; search snippets only); arXiv:2609.37461 (title from search results only) <https://www.preprints.org/manuscript/202608.2196>

## Open-status evidence

- Most recent source: P. Pant, R. Singh, arXiv:2604.24192, v3 dated 21 November 2026 (abstract page fetched)
- URL: <https://arxiv.org/abs/2604.24192>
- Date: 2026-11-21
- Content: Abstract still presents the statement as Chollet's 1982 conjecture and says: 'In this paper, we study natural structural classes for which the conjecture holds.' No source found claims a general proof or a counterexample. Zhang 2016 section title: 'Chollet conjecture is open'.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- Chollet conjecture permanent Hadamard product positive semidefinite per(A∘B) ≤ per(A)per(B) counterexample OR proof 2024 OR 2025 OR 2026
- Lieb permanental dominance conjecture 2025 OR 2026 proof OR counterexample OR "still open" immanant
- Pate conjecture permanent positive semidefinite "per(J_k ⊗ M)" OR "Liang-So-Zhang" OR "per(A ⊗ B)" (per A)^m (per B)^n tensor product conjecture 2025 OR 2026 proof OR counterexample

Sources checked:

- General web search (3 queries touching permanent conjectures)
- F. Zhang survey arXiv:1608.02844 (PDF pages 1–13 read)
- arXiv abstract page 2604.24192
- preprints.org 202608.2196 (attempted, HTTP 403)

Limitations: 2026 has seen a burst of (apparently AI-assisted, unrefereed) preprints on this exact conjecture; I could not read the order-<=6 preprint, so the true frontier (n = 5, 6 or 7) is uncertain. No arXiv listing search, MathOverflow, or Scholar check. The Wanless/Cheon open-problem updates were not consulted.

## Computational approaches

Exact permanents by Ryser/Glynn in rational or Gaussian-rational arithmetic are trivial for n <= 12. Counterexample search: maximize per(A \circ \bar A)/(per A)^2 over complex correlation matrices, parametrized as Gram matrices of r unit vectors in C^r (low rank r = 2, 3 first, since all known counterexamples to the neighbouring Bapat–Sunder/POT conjectures are rank-deficient and complex), n = 5..10, using gradient ascent with many restarts and structured families (tight frames, roots-of-unity constructions like Drury's). Proof side for small n: sum-of-squares / Positivstellensatz certificates in the Gram-vector coordinates, exact rational verification. Literature frontier: n <= 3 classical; n = 4 real published (and complex claimed); n <= 6 claimed in an unrefereed 2026 preprint (unverified).

## Mathematical approaches

Reduction to B = conj(A) and to correlation matrices; Schur power matrix / symmetric tensor power representation of the permanent (per A = <A^{\otimes n} sym, sym>); Lieb/Marcus-type inequalities; expansions along rank-one decompositions (permanent of a Gram matrix as a squared norm of a symmetric tensor product v_1 ∨ ... ∨ v_n); structural classes (bipartite support, graph Laplacians, one-point sums as in Pant–Singh); low-rank cases; perturbation near the identity and near rank-one matrices.

Scout's tractability assessment: The full conjecture is old and hard, but it is NOT attacked 'to death' classically, and the April–November 2026 Pant–Singh paper shows that new structural classes (graph Laplacians, bipartite support) are accessible to elementary arguments, so a newcomer can plausibly add a class (e.g. Laplacians of further graph families, circulant or low-rank PSD matrices) or run a serious low-rank complex counterexample search. Caveat: small-n cases are currently crowded with unrefereed computer-assisted preprints; avoid duplicating n <= 6 without first reading those.

## Formalization feasibility

Not checked in this session. From memory: Mathlib has Matrix.permanent, Matrix.PosSemidef and the Hadamard product (Matrix.hadamard), so the statement itself should be a one-line Lean 4 definition; small fixed-n cases reduce to polynomial inequalities that could be certified with SOS + 'polyrith'/'nlinarith'-style tactics, though size grows fast.

## Prerequisites

Positive semidefinite matrices and Gram representations, permanents and Ryser's formula, Hadamard and Kronecker products, Schur product theorem, Oppenheim's inequality, basic multilinear algebra (symmetric tensors), numerical optimization, sum-of-squares certificates.

## Unverified items

- Title/journal of Chollet's 1982 paper (from memory).
- Hutchinson 2021 (real 4x4) and arXiv:2211.02839 (complex 4x4): search snippets only, not fetched; authorship of 2211.02839 as given by the snippet.
- preprints.org 202608.2196 (orders <= 6) and 202608.1346: could not be fetched (HTTP 403); correctness and exact claims unknown.
- arXiv:2609.37461: title only.
- Mathlib API names quoted from memory.
