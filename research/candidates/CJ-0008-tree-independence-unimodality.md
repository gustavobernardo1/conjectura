# CJ-0008 — Unimodality of the independence polynomial of trees

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

As quoted in Galvin (arXiv:2502.10654v2) from Alavi–Malde–Schwenk–Erdős, Problem 3: "For trees (or perhaps forests), is the vertex independence sequence unimodal?" Definitions: for a graph G let $i_k(G)$ be the number of independent sets of size k, $0\le k\le \alpha(G)$; the sequence $(i_0,\dots,i_{\alpha(G)})$ (coefficients of the independence polynomial $I(G;x)=\sum_k i_k(G)x^k$) is unimodal if there is m with $i_0\le i_1\le\dots\le i_m\ge i_{m+1}\ge\dots\ge i_{\alpha(G)}$. Conjecture form: the independence polynomial of every tree (resp. forest) is unimodal.

**Source.** Y. Alavi, P. J. Malde, A. J. Schwenk, P. Erdős, The vertex independence sequence of a graph is not constrained, Congr. Numer. 58 (1987) 15-23, Problem 3; quoted via D. Galvin, arXiv:2502.10654. <https://arxiv.org/abs/2502.10654>

**Statement checked against:** secondary-source. Posed as a question in the original; quoted from Galvin's paper. The 1987 paper was not accessed.

## Definitions and hypotheses

Originally a question, not an assertion; Galvin notes it "is often presented in the literature as a conjecture". Tree version and forest version are distinct statements (forest polynomials are products of tree polynomials, and products of unimodal polynomials need not be unimodal). Log-concavity ($i_k^2\ge i_{k-1}i_{k+1}$) is STRONGER and is now known to be FALSE for trees; unimodality is what remains open. Unimodality is false for general graphs and for some well-covered/bipartite classes, so the tree hypothesis is essential.

## Known partial results

- All trees on at most 25 vertices have log-concave (hence unimodal) independent set sequences (Radcliffe, personal communication cited by Galvin). Kadrawi, Levit, Yosef and Mizrachi extended the computation and found exactly two 26-vertex trees that are not log-concave; search snippets of their paper say all 26-vertex trees are still unimodal. — D. Galvin, arXiv:2502.10654v2 (fetched); O. Kadrawi, V. E. Levit, R. Yosef, M. Mizrachi, "The independence polynomial of trees is not always log-concave starting from order 26", arXiv:2305.01784 (snippet only) <https://arxiv.org/html/2502.10654v2> (source fetched)
- Kadrawi and Levit: infinite families of trees with non-log-concave sequences (failure at α(T)-1). Ramos and Sun: PatternBoost found many non-log-concave trees with 27 to 101 vertices. Galvin, Theorem 1.3: trees T_t with α = (1+t)⌊2^{t/16}⌋ where log-concavity breaks at t⌊2^{t/16}⌋+2. Levit–Mandrescu: the sequence of a tree is decreasing from ⌈(2α(T)-1)/3⌉ on. Galvin also says the "status of caterpillars is not known". — D. Galvin, arXiv:2502.10654v2 (revised Jan 2026 per search result) <https://arxiv.org/html/2502.10654v2> (source fetched)
- The two infinite non-log-concave families T_{3,m,n} and T*_{3,m,n} of Kadrawi–Levit–Yosef–Mizrachi are unimodal: "we show that these two infinite families also satisfy the unimodal conjecture". — Grace M. X. Li, "Unimodality of independence polynomials of two family of trees", arXiv:2603.03025 (3 Mar 2026) <https://arxiv.org/abs/2603.03025> (source fetched)

## Relevant literature

- Y. Alavi, P. J. Malde, A. J. Schwenk, P. Erdős, The vertex independence sequence of a graph is not constrained, Congr. Numer. 58 (1987) 15-23, Problem 3; quoted via D. Galvin, arXiv:2502.10654. <https://arxiv.org/abs/2502.10654>
- D. Galvin, arXiv:2502.10654v2 (fetched); O. Kadrawi, V. E. Levit, R. Yosef, M. Mizrachi, "The independence polynomial of trees is not always log-concave starting from order 26", arXiv:2305.01784 (snippet only) <https://arxiv.org/html/2502.10654v2>
- D. Galvin, arXiv:2502.10654v2 (revised Jan 2026 per search result) <https://arxiv.org/html/2502.10654v2>
- Grace M. X. Li, "Unimodality of independence polynomials of two family of trees", arXiv:2603.03025 (3 Mar 2026) <https://arxiv.org/abs/2603.03025>

## Open-status evidence

- Most recent source: G. M. X. Li, arXiv:2603.03025
- URL: <https://arxiv.org/abs/2603.03025>
- Date: 2026-03-03
- Content: The abstract treats tree unimodality as a standing conjecture and proves it only for two families ("these two infinite families also satisfy the unimodal conjecture"). Neither Li nor Galvin uses the literal word 'open'; Galvin describes "few very general results". A search on 2026-11-26 for a non-unimodal tree or a general proof found none (it also surfaced Levit–Kadrawi, arXiv:2603.17114, on unicyclic graphs, which does not address trees).

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- unimodality independence polynomial of trees conjecture Alavi Malde Schwenk Erdős 2025 2026 verified vertices counterexample
- tree independence polynomial "not unimodal" OR "non-unimodal" counterexample tree 2026 Alavi Malde Schwenk Erdős conjecture disproved OR "remains open"

Sources checked:

- arXiv:2502.10654v2 (HTML, read)
- arXiv:2603.03025 (abstract page)
- two general web searches
- 1337isnot1337/solved-conjectures README (no matching entry)

Limitations: The 1987 primary source was not accessible. No explicit 2026 sentence 'the conjecture is open' was fetched; openness is inferred from 2026 papers that prove special cases. MathOverflow, Wikipedia and OEIS were not checked. Whether anyone has exhaustively checked unimodality beyond 26 vertices is unknown to the scout (the PatternBoost search to 101 vertices was heuristic, for log-concavity).

## Computational approaches

Independence polynomial of a tree by the standard rooted DP (include/exclude root) in O(n^2) integer operations; trees enumerated up to isomorphism by nauty's gentreeg or the Wright–Richmond–Odlyzko–McKay algorithm. Largest exhaustive case in the fetched literature: 26 vertices (unimodal for all; two non-log-concave). Tree counts grow by a factor of about 2.7 per vertex (about 2.8e8 unlabelled trees at n = 26), so 27-30 vertices (up to roughly 1.5e10 trees) is reachable on one desktop with compiled, multithreaded code; that would be a new exhaustive small case. Beyond that: targeted search in the families where log-concavity fails near the mode (spherically symmetric trees, Galvin's T_{m,t,1}, caterpillars and 'brooms'), local search / reinforcement search maximising a unimodality-violation score, and exact big-integer evaluation of parametrised families.

## Mathematical approaches

Prove unimodality for further families: caterpillars (status reported as unknown), spiders, lobsters, spherically symmetric trees, trees of bounded diameter; use real-rootedness where available (claw-free does not apply, but path-like trees), the Levit–Mandrescu tail-decrease result (only the first two thirds of the sequence needs control), ordered log-concavity / 'log-concave except at one index' arguments, and transfer-matrix recursions for periodic families. For a disproof one needs log-concavity to fail before index (2α-1)/3 badly enough to create a valley (Galvin's Question 3.1 asks for breaks at relative position (1-c)α with c > 1/3).

Scout's tractability assessment: Famous and old; the general statement is very unlikely to fall. But it is unusually computation-friendly: extending the exhaustive range past 26 vertices, settling caterpillars or another named family, or answering Galvin's Questions 3.1/3.2 for a new family are realistic. Log-concavity for trees has been 'tried to death' and is now refuted; the active frontier (2023-2026: Kadrawi–Levit, Ramos–Sun, Galvin, Li) is exactly how badly log-concavity can fail while unimodality survives.

## Formalization feasibility

Not checked. To the scout's knowledge Mathlib has `SimpleGraph.IsTree`, independent sets (`IsIndepSet`, `indepNum`) and polynomial unimodality-adjacent notions are thin; an independence polynomial would likely have to be defined. Finite verified instances (specific families or all trees up to a small n) are formalisable by computation.

## Prerequisites

Generating functions and graph polynomials, tree DP, unimodality / log-concavity / real-rootedness techniques (Newton inequalities, interlacing), efficient tree enumeration, big-integer arithmetic.

## Unverified items

- Exact wording and numbering in the 1987 Congressus Numerantium paper (quoted only via Galvin).
- That all 26-vertex trees are unimodal (search-result snippet of arXiv:2305.01784, not fetched).
- Tree counts (about 2.8e8 at n = 26, about 1.5e10 at n = 30) are from memory of OEIS A000055.
- Whether exhaustive unimodality checks beyond 26 vertices already exist.
- The scope of Galvin's remark on caterpillars (unimodality vs log-concavity) should be re-read in context.
- Mathlib coverage statements.
