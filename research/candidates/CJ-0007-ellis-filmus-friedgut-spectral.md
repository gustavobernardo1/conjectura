# CJ-0007 — Ellis–Filmus–Friedgut spectral conjectures H and I for Kneser graphs of downsets

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Quoted sentences: Conjecture H: "The weighted Hoffman bound is tight for any downset." Conjecture I: "The inertia bound is tight for any downset." Setting (as reported from the paper; wording of the definitions is a close paraphrase obtained through a summarising fetch, not a verbatim copy): a downset is a family $\mathcal{D}\subseteq 2^{[n]}$ with $A\in\mathcal{D},\ B\subseteq A \Rightarrow B\in\mathcal{D}$. $\mathrm{Kn}(\mathcal{D})$ is the graph on vertex set $\mathcal{D}$ in which two sets are adjacent iff they are disjoint (so $\emptyset$ carries a loop). Weighted Hoffman bound: if $M$ is a real symmetric $V\times V$ matrix with $M(x,y)=0$ whenever $xy\notin E(G)$ and $M\mathbf{1}=\mathbf{1}$, then $\alpha(G)\le \frac{-\lambda_{\min}(M)}{1-\lambda_{\min}(M)}|V(G)|$. Inertia bound: if $M$ is real symmetric with $M(x,y)=0$ whenever $xy\notin E(G)$, then $\alpha(G)\le \#\{\text{nonnegative eigenvalues of } M\}$. 'Tight' is to be read as: for $G=\mathrm{Kn}(\mathcal{D})$ there is an admissible $M$ for which the bound equals the maximum size of an intersecting subfamily of $\mathcal{D}$, which by the (now proved) Chvátal conjecture is the size of the largest star $\max_i |\{A\in\mathcal{D}: i\in A\}|$.

**Source.** D. Ellis, Y. Filmus, E. Friedgut, Chvátal's conjecture: a proof from The Book, arXiv:2609.28404 (v3, 22 October 2026), Section 5, Conjectures H and I. <https://arxiv.org/abs/2609.28404>

**Statement checked against:** not-checked. The two conjecture sentences were quoted through a summarising fetch and the surrounding definitions are a paraphrase. The PDF must be re-read before any work starts.

## Definitions and hypotheses

Quantifier: for EVERY downset D (every n) there EXISTS a matrix M achieving equality. Loops: a footnote says "we allow vertices of G to have loops (the vertex ∅ of Kn(D) has a loop)", and that the weighted Hoffman bound needs at least one loopless vertex; whether nonzero diagonal entries of M are allowed anywhere other than at the looped vertex ∅ must be read off the paper's exact definition (the summary says M(x,y)=0 for non-edges, so the diagonal is forced to 0 at loopless vertices). The paper does not give a one-line definition of 'tight'; the reading above is inferred from context and should be confirmed against the PDF. The two bounds are reported to be incomparable in general. Degenerate downsets (D = {∅}) need separate handling.

## Known partial results

- Chvátal's conjecture itself (every downset has a maximum-size intersecting family which is a star) is now a theorem: proved by Chang, Liu and Liu as a corollary of a sharp correlation inequality, with a second, short spectral proof in the Ellis–Filmus–Friedgut paper; Kleitman's stronger conjecture is proved as well. — F. Chang, H. Liu, M. Liu, "A proof of Chvátal's conjecture via a sharp correlation inequality", arXiv:2609.19123 (2026) [citation taken from the reference list of arXiv:2609.28404; not fetched itself]; Ellis–Filmus–Friedgut arXiv:2609.28404 <https://arxiv.org/abs/2609.28404> (source fetched)
- Numerical evidence only: the authors "checked whether they were tight on thousands of downsets D, both structured and random" and "both bounds worked on every family that we tested"; the new proofs "do not seem to produce a matrix certifying a tight bound in either case". No special case of H or I is proved in the paper; no range of n is given. — Ellis–Filmus–Friedgut, arXiv:2609.28404v3, Section 5 <https://arxiv.org/html/2609.28404v3> (source fetched)
- A natural strengthening of H (replace the weighted Hoffman bound by the fractional independence number) is false: for D = {A ⊆ [7] : |A| ≤ 3} the maximum intersecting family has size 22 while the fractional independence number is 22.75. Also Theorem 3: the projection packing number equals the largest star for every downset, and it is bounded above by the inertia and theta bounds. — Ellis–Filmus–Friedgut, arXiv:2609.28404v3 <https://arxiv.org/html/2609.28404v3> (source fetched)
- For general graphs the inertia bound is not always tight (Sinkovic's first example; Kwan–Wigderson, "The inertia bound is far from tight", arXiv:2312.04925). These concern arbitrary graphs, not Kneser graphs of downsets. — M. Kwan, Y. Wigderson, arXiv:2312.04925 (known from search-result snippet only) <https://arxiv.org/abs/2312.04925> (source not fetched)

## Relevant literature

- D. Ellis, Y. Filmus, E. Friedgut, Chvátal's conjecture: a proof from The Book, arXiv:2609.28404 (v3, 22 October 2026), Section 5, Conjectures H and I. <https://arxiv.org/abs/2609.28404>
- F. Chang, H. Liu, M. Liu, "A proof of Chvátal's conjecture via a sharp correlation inequality", arXiv:2609.19123 (2026) [citation taken from the reference list of arXiv:2609.28404; not fetched itself]; Ellis–Filmus–Friedgut arXiv:2609.28404 <https://arxiv.org/abs/2609.28404>
- Ellis–Filmus–Friedgut, arXiv:2609.28404v3, Section 5 <https://arxiv.org/html/2609.28404v3>
- Ellis–Filmus–Friedgut, arXiv:2609.28404v3 <https://arxiv.org/html/2609.28404v3>
- M. Kwan, Y. Wigderson, arXiv:2312.04925 (known from search-result snippet only) <https://arxiv.org/abs/2312.04925>

## Open-status evidence

- Most recent source: Ellis–Filmus–Friedgut, arXiv:2609.28404 v3
- URL: <https://arxiv.org/abs/2609.28404>
- Date: 2026-10-22 (v3)
- Content: The conjectures are stated as new open conjectures in Section 5, supported only by experiments on "thousands of downsets". A web search on 2026-11-26 for a proof or counterexample returned only the source paper.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- "weighted Hoffman bound" OR "inertia bound" downset Kneser graph Chvátal "Conjecture H" OR "spectral Chvátal" Ellis Filmus Friedgut proof OR counterexample
- Chvátal's conjecture intersecting family downset "still open" 2025 arXiv

Sources checked:

- arXiv abstract page and HTML v3 of 2609.28404
- two general web searches
- 1337isnot1337/solved-conjectures README (no matching entry)

Limitations: The conjectures are two months old; follow-up preprints may not be indexed yet. arXiv listing/citation search (papers citing 2609.28404 or 2609.19123), MathOverflow and the authors' pages were not checked. The Chang–Liu–Liu paper and Keevash's paper on Kahn's flow conjecture (arXiv 2609.23595, seen only in a snippet) were not read and may already contain or imply a certifying matrix. Statement details were obtained through a summarising fetch and must be re-read from the PDF before any formal work.

## Computational approaches

Conjecture H is decidable per downset by semidefinite programming (scout's own analysis): the best weighted Hoffman bound is obtained by maximising λ_min(M) over the affine space {M symmetric, supported on edges of Kn(D), M1 = 1}, i.e. maximise t subject to M - tI ⪰ 0; SDP duality then gives either a certifying matrix or a dual certificate of non-tightness, both of which can be rounded to exact rational/algebraic certificates. Matrix size is |D| ≤ 2^n: n ≤ 6 gives at most 64x64, n = 8 gives 256x256, easy for a desktop SDP solver. Exhaustive enumeration of all downsets up to isomorphism is feasible for n ≤ 6 (inequivalent monotone Boolean functions: 210 for n = 5, 16,353 for n = 6) and by sampling for n = 7, 8. A systematic exhaustive table for n ≤ 6 with exact certificates would go beyond the 'thousands of examples' reported. Conjecture I is harder to refute computationally (non-convex existence question; a counterexample needs a proof that no admissible M has only s nonnegative eigenvalues), but certifying matrices can be searched for numerically and then verified exactly (Sturm sequences / exact inertia via LDL^T over Q).

## Mathematical approaches

Prove H or I for structured downsets where symmetry reduces M to a small quotient: the full cube 2^[n] (the complement-pairing matrix certifies tightness), downsets generated by a single set or by a few maximal sets, the truncated cubes {A : |A| ≤ k} (Johnson-scheme / Erdős–Ko–Rado spectral methods; note the paper's n = 7, k = 3 example shows fractional relaxations are not enough), products and joins of downsets (does tightness tensorise?), and compressed (left-shifted) downsets. Try to extract an explicit certifying matrix from the Chang–Liu–Liu or Ellis–Filmus–Friedgut proof for these classes; look for patterns in SDP-optimal matrices on small cases and guess a closed form.

Scout's tractability assessment: Best 'new and fresh' target found: stated two months ago by strong authors who explicitly say they have only numerical evidence and no certifying matrices. A newcomer can realistically (a) produce the first exhaustive small-n verification with exact certificates, (b) prove one or two structured families, or (c) find a counterexample to H by SDP (the fractional variant already fails at n = 7). Risks: the authors or their circle may settle it quickly; the exact normalisation (loops, diagonal) must be read carefully from the PDF.

## Formalization feasibility

Not checked in detail. Mathlib has finite set families (`Finset`, `IsLowerSet`), real symmetric/Hermitian matrices with eigenvalues (`Matrix.IsHermitian.eigenvalues`) and positive semidefiniteness; it does not, as far as the scout knows, contain the Hoffman or inertia bounds. Individual small instances (a given downset and an explicit rational matrix M) reduce to checking positive semidefiniteness of an explicit rational matrix, which is formalisable via an explicit LDL^T / Cholesky certificate.

## Prerequisites

Linear algebra (eigenvalue interlacing, positive semidefinite matrices), the Hoffman ratio bound and Cvetković inertia bound, Erdős–Ko–Rado and intersecting families, basics of semidefinite programming and duality, representation theory of the Johnson scheme for the symmetric cases.

## Unverified items

- Exact wording of the definitions surrounding Conjectures H and I (obtained via a summarising fetch); the meaning of 'tight' is inferred, not quoted.
- arXiv:2609.19123 (Chang–Liu–Liu) was not fetched; its citation comes from the Ellis–Filmus–Friedgut reference list.
- Counts of inequivalent downsets (210 for n = 5, 16,353 for n = 6) are from memory (OEIS A003182), not fetched.
- The SDP reformulation and the claim that the full cube is certified by the complement-pairing matrix are the scout's own unverified analysis.
- Kwan–Wigderson / Sinkovic results known only from search snippets.
