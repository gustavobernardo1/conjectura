# CJ-0015 — Kalai's 3^d conjecture

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Verbatim from arXiv:2308.02909v3: 'We write $s(P)$ for the number of non-empty faces of $P$ and we denote by $C_{d}=[-1,+1]^{d}$ the $d$-dimensional cube. Conjecture 1 ($3^{d}$ conjecture). Every $d$-dimensional centrally-symmetric polytope $P$ satisfies $s(P)\ \geq\ s(C_{d})\ =\ 3^{d}$.' Here 'A convex polytope $P\subset\mathbb{R}^{d}$ is centrally-symmetric if $-P=P$.' Related open statement in the same paper: 'Conjecture 25. Every $d$-dimensional centrally-symmetric polytope $P$ has at least as many flags as the $d$-dimensional cube, i.e., $\#\mathrm{flags}(P)\ \geq\ \#\mathrm{flags}(C_{d})\ =\ 2^{d}d!$.'

**Source.** G. Kalai, The number of faces of centrally-symmetric polytopes, Graphs Combin. 5 (1989) 389-391; statement quoted from R. Sanyal, M. Winter, arXiv:2308.02909v3 (21 April 2024), Conjecture 1. <https://arxiv.org/abs/2308.02909>

**Statement checked against:** secondary-source. Quoted from a 2024 restatement; the 1989 paper was not accessed.

## Definitions and hypotheses

P is a full-dimensional convex polytope in R^d with -P = P. s(P) counts NON-EMPTY faces including P itself (so the cube has 3^d: sign vectors in {-1,0,+1}^d). Easy to get wrong: (a) the count is of all faces, not facets (the abstract of arXiv:2211.09215 says 'facets', which is a slip); (b) the empty face is excluded and P is included; (c) the conjectured minimisers are the Hanner polytopes (built from segments by products and polar duals), not only the cube and cross-polytope; (d) Kalai's stronger conjectures B and C are FALSE (C fails in d=4; B and C fail in all d >= 5), so strengthened forms should not be assumed; (e) the quantity is combinatorial, so only the face lattice matters and the conjecture is invariant under polar duality.

## Known partial results

- The three Kalai conjectures hold for d <= 3; in dimension 4 conjectures A and B hold while C fails; B and C fail in all dimensions d >= 5. Hence the 3^d conjecture is proved exactly for d <= 4. — R. Sanyal, A. Werner, G. M. Ziegler, 'On Kalai's conjectures concerning centrally symmetric polytopes', arXiv:0708.3661 (Discrete Comput. Geom. 41(2):183-198, 2009) - abstract read via arXiv API <https://arxiv.org/abs/0708.3661> (source fetched)
- True for unconditional polytopes and, more generally, proper locally anti-blocking polytopes, with equality exactly for (generalized) Hanner polytopes (Theorems 3 and 4). Trivially true for zonotopes, with the cube the unique minimiser (Remark 5). — R. Sanyal, M. Winter, arXiv:2308.02909v3 <https://arxiv.org/html/2308.02909v3> (source fetched)
- True if there are d hyperplanes with orthogonal normals such that the polytope is symmetric about all of them (independent proof of the unconditional case). — G. R. Chambers, E. Portnoy, 'A note on Kalai's 3^d Conjecture', arXiv:2211.09215 - abstract read via arXiv API <https://arxiv.org/abs/2211.09215> (source fetched)
- True for Hansen polytopes of split graphs; Hanner polytopes among them correspond to threshold graphs; a family of Hansen polytopes with only 3^d + 16 nonempty faces. — R. Freij, M. Henze, M. W. Schmitt, G. M. Ziegler, 'Face numbers of centrally symmetric polytopes from split graphs', arXiv:1201.5790 - abstract read via arXiv API <https://arxiv.org/abs/1201.5790> (source fetched)
- Related: vol(P) vol((P-P)^polar) <= F(P)/(d!)^2 for any polytope with F(P) flags, implying that the Mahler conjecture implies Kalai's flag conjecture. — M. Winter, 'A relation between Mahler volume and flag number for convex polytopes', arXiv:2610.09990v1 (7 Oct 2026) - abstract read via arXiv API <https://arxiv.org/abs/2610.09990> (source fetched)

## Relevant literature

- G. Kalai, The number of faces of centrally-symmetric polytopes, Graphs Combin. 5 (1989) 389-391; statement quoted from R. Sanyal, M. Winter, arXiv:2308.02909v3 (21 April 2024), Conjecture 1. <https://arxiv.org/abs/2308.02909>
- R. Sanyal, A. Werner, G. M. Ziegler, 'On Kalai's conjectures concerning centrally symmetric polytopes', arXiv:0708.3661 (Discrete Comput. Geom. 41(2):183-198, 2009) - abstract read via arXiv API <https://arxiv.org/abs/0708.3661>
- R. Sanyal, M. Winter, arXiv:2308.02909v3 <https://arxiv.org/html/2308.02909v3>
- G. R. Chambers, E. Portnoy, 'A note on Kalai's 3^d Conjecture', arXiv:2211.09215 - abstract read via arXiv API <https://arxiv.org/abs/2211.09215>
- R. Freij, M. Henze, M. W. Schmitt, G. M. Ziegler, 'Face numbers of centrally symmetric polytopes from split graphs', arXiv:1201.5790 - abstract read via arXiv API <https://arxiv.org/abs/1201.5790>
- M. Winter, 'A relation between Mahler volume and flag number for convex polytopes', arXiv:2610.09990v1 (7 Oct 2026) - abstract read via arXiv API <https://arxiv.org/abs/2610.09990>

## Open-status evidence

- Most recent source: Sanyal-Winter arXiv:2308.02909v3 (21 Apr 2024) for the explicit status; arXiv API listing checked 2026-11-26 for anything newer
- URL: <https://arxiv.org/html/2308.02909v3>
- Date: 2024-04-21 (explicit statement); 2026-11-26 (listing)
- Content: 'The conjecture is known to hold in dimensions d <= 4' and 'Like Kalai's 3^d conjecture, Conjecture 25 is widely open'. A date-sorted arXiv API query (all:Kalai AND all:"centrally symmetric") returned as its newest item Winter's Oct 2026 paper, which proves an implication between Mahler's conjecture and the flag conjecture, not the 3^d conjecture; a web search for 2025/2026 proofs or counterexamples found none. Note: the most recent EXPLICIT 'open' statement I fetched is from 2024, not 2025-2026.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- web: Kalai 3^d conjecture centrally symmetric polytopes 2025 OR 2026 proof OR counterexample dimension 5 open
- arXiv API: all:"Kalai" AND all:"centrally symmetric", sortBy=submittedDate desc, 12 results (6 returned)

Sources checked:

- arXiv abs + HTML of 2308.02909v3
- arXiv API listing (abstracts of 0708.3661, 1201.5790, 2211.09215, 2610.09990)
- general web search (Wikipedia page surfaced, not opened)

Limitations: Session date 2026-11-26. About 30 outbound requests in total across all candidates: 13 model-summarised web searches (US-only index), 4 model-summarised page fetches, 13 direct downloads of arXiv abs/HTML pages and arXiv API listings (sorted by submission date). NOT checked: MathOverflow, Open Problem Garden, MathSciNet/zbMATH, Google Scholar citation trails, journal sites, conference proceedings, non-arXiv preprint servers (several 2026 AI-assisted proofs of other conjectures appeared first on preprints.org or GitHub, which this search does not cover). An unsuccessful search does not establish that the problem is open or that a planned partial result is new. The arXiv query was narrow (it requires the words 'Kalai' and 'centrally symmetric'); a paper phrased differently (e.g. '3^d conjecture' with 'centrally-symmetric' hyphenated, or a result on a new polytope class) could be missed. Wikipedia's page on the conjecture was not opened.

## Computational approaches

s(P) is a face-lattice invariant, so exact computation is integer arithmetic. Feasible on a desktop: (1) exhaustive enumeration of combinatorial types of centrally symmetric d-polytopes with few vertices or facets for d = 5, 6 (e.g. cs polytopes with 2d+2 or 2d+4 vertices via Gale-diagram or oriented-matroid enumeration; cs 0/1-type or lattice polytopes in a small box; Hansen polytopes of all graphs on few vertices; cs 2-level polytopes) and computing f-vectors with polymake/Normaliz/SageMath; (2) search for polytopes with small s(P) - 3^d (the known near-miss family has excess 16), by local moves (stacking/truncating symmetric pairs, products, duals, free sums); (3) LP/IP over known linear relations on flag f-vectors of cs polytopes to test whether known inequalities already force s >= 3^5 (this is how d = 4 was handled, with additional arguments). Largest case settled: all cs polytopes for d <= 4. A search summary reported that all cs 2-level polytopes up to dimension 7 satisfy the conjecture (not verified by me).

## Mathematical approaches

f-vector / flag-vector inequalities for centrally symmetric polytopes (cs analogues of the g-theorem, toric h-vector, rigidity); the 'special points' / concave-function argument of Sanyal-Winter modelled on Saint-Raymond's proof of Mahler's conjecture for unconditional bodies; induction on dimension through central hyperplane sections and projections; structure of Hanner polytopes (cographs); connections to the Mahler volume and flag conjecture.

Scout's tractability assessment: A proof for d = 5 looks hard: the d = 4 proof needed strong f-vector theory and the stronger conjectures that might have given an inductive handle are false. But the problem is unusually friendly to partial results: every new natural class (as in 2012, 2022, 2023) has been publishable, and counterexample searches are cheap and exact. Realistic outcomes: (a) verified exhaustive results such as 'all cs 5-polytopes with at most 2d+k vertices (or facets) satisfy s(P) >= 243', with an explicit list of those achieving small excess; (b) proof for a new class (e.g. Hansen polytopes of a wider graph family, cs polytopes with a large symmetry group, cs simplicial/simple polytopes in d = 5 where known h-vector inequalities may suffice); (c) classification of polytopes with s(P) = 3^d + small excess in low dimension. Tried to death: unconditional/coordinate-symmetric cases (now done, with equality characterisation) and attempts via Kalai's conjectures B and C (false).

## Formalization feasibility

Not checked in this session. From memory (unverified): Mathlib has convex hulls, extreme points and exposed faces of convex sets but, as far as I know, no developed theory of polytope face lattices or f-vectors, so even stating 'number of non-empty faces of a polytope' needs groundwork (define a face as an exposed face of the convex hull of a finite set, prove finiteness). A purely combinatorial restatement is not available, since realisability matters. Formalising proofs for d <= 2 or 3, or the zonotope case, would be a reasonable but nontrivial project.

## Prerequisites

Convex polytopes (faces, face lattices, polarity, products and free sums, f-vectors, Euler and Dehn-Sommerville relations); Hanner polytopes; software such as polymake/SageMath/Normaliz; some oriented-matroid or Gale-duality background for enumeration.

## Unverified items

- Kalai's original 1989 wording (paper not fetched; statement taken from Sanyal-Winter).
- The claim that all centrally symmetric 2-level polytopes up to dimension 7 satisfy the conjecture (seen only in a search-engine summary of arXiv:1703.01943, not fetched).
- Whether simplicial/simple cs 5-polytopes are already covered by known inequalities (my suggestion, not checked).
- No explicit 2025-2026 source saying 'the 3^d conjecture is open for d >= 5' was fetched; the status rests on a 2024 paper plus the absence of later claims in the searches listed.
- Publication venue of arXiv:2308.02909 (acknowledgements mention a reviewer; journal not confirmed).
