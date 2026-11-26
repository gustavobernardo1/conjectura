# CJ-0009 — Erdős–Gyárfás conjecture (Erdős Problem 64)

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Docstring of formal-conjectures `Erdos64` (verbatim): "Does every finite graph with minimum degree at least $3$ contain a cycle of length $2^k$ for some $k \geq 2$?" Wikipedia's wording: the conjecture "states that every graph with minimum degree 3 contains a simple cycle whose length is a power of two." Lean form: for every finite simple graph G with G.minDegree ≥ 3 there exist k ≥ 2, a vertex v and a closed walk c at v that is a cycle with c.length = 2^k.

**Source.** Erdős Problem 64; statement read from google-deepmind/formal-conjectures (FormalConjectures/ErdosProblems/64.lean) and from Wikipedia. The original printed source was not accessed. <https://www.erdosproblems.com/64>

**Statement checked against:** secondary-source. erdosproblems.com returned HTTP 403 to the fetch tool; its status and comment thread are unchecked.

## Definitions and hypotheses

Finite simple graphs; minimum degree ≥ 3 (not exactly 3); cycle lengths 4, 8, 16, ... (k ≥ 2; in a simple graph lengths 1 and 2 are impossible anyway). The cycle is a subgraph cycle, not necessarily induced. Per Wikipedia Erdős offered $100 for a proof and $50 for a counterexample.

## Known partial results

- Computer searches (Markström; Royle): any counterexample has at least 17 vertices and any cubic counterexample at least 30 vertices; Markström found four 24-vertex graphs whose only power-of-two cycles have length 16 (one planar). Cubic bipartite counterexamples need at least 30 vertices (Salehi Nowbandegani, Esfandiari 2011). True for 3-connected cubic planar graphs (Heckman, Krakovski 2013), planar claw-free graphs (Daniel, Shauger 2001), some K_{1,m}-free graphs (Shauger 1998). Sudakov–Verstraëte 2008: average degree exponential in the iterated logarithm of n forces a power-of-two cycle. — Wikipedia, "Erdős–Gyárfás conjecture" (most recent reference there: Heckman–Krakovski, Electron. J. Combin., 2013) <https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture> (source fetched)
- Minimal counterexamples: "every regular minimal counterexample must be cubic"; every vertex is adjacent to a vertex of degree 3; "at least 4/7 of the vertices" have degree exactly 3. — Avery Carr, "Every Minimal Counterexample to the Erdős-Gyárfás Conjecture is Predominantly Cubic", arXiv:2605.22844 (13 May 2026), single-author preprint <https://arxiv.org/abs/2605.22844> (source fetched)
- Known from search-result snippets only: Liu–Montgomery (a large enough constant average degree forces a power-of-two cycle); P10-free graphs (Hu, Shen, arXiv:2308.05675); P13-free graphs (Hegde, Sandeep, Shashank, arXiv:2410.22842); diameter 2 and minimum degree ≥ 3 gives a cycle of length 4 or 8 (Carr, arXiv:2508.19302); the AlphaEvolve paper (arXiv:2511.02864) reports experiments on graphs up to 40 vertices without finding a counterexample. — various, via web search snippets <https://arxiv.org/abs/2410.22842> (source not fetched)

## Relevant literature

- Erdős Problem 64; statement read from google-deepmind/formal-conjectures (FormalConjectures/ErdosProblems/64.lean) and from Wikipedia. The original printed source was not accessed. <https://www.erdosproblems.com/64>
- Wikipedia, "Erdős–Gyárfás conjecture" (most recent reference there: Heckman–Krakovski, Electron. J. Combin., 2013) <https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture>
- Avery Carr, "Every Minimal Counterexample to the Erdős-Gyárfás Conjecture is Predominantly Cubic", arXiv:2605.22844 (13 May 2026), single-author preprint <https://arxiv.org/abs/2605.22844>
- various, via web search snippets <https://arxiv.org/abs/2410.22842>

## Open-status evidence

- Most recent source: google-deepmind/formal-conjectures, FormalConjectures/ErdosProblems/64.lean (main branch); Carr, arXiv:2605.22844 (May 2026)
- URL: <https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/64.lean>
- Date: Lean file fetched 2026-11-26; Carr preprint 2026-05-13
- Content: The Lean statement `erdos_64` is tagged `@[category research open, question, AMS 5]`. Carr's May 2026 preprint studies hypothetical minimal counterexamples, which presupposes the conjecture is unresolved. Wikipedia calls it an "unsolved problem in mathematics". A web search for a 2025/2026 proof or counterexample found only partial results.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- Erdős–Gyárfás conjecture cycle length power of two proof OR counterexample 2025 2026

Sources checked:

- Wikipedia article
- arXiv:2605.22844 abstract page
- formal-conjectures ErdosProblems/64.lean
- erdosproblems.com/64 (HTTP 403, NOT read)
- 1337isnot1337/solved-conjectures README (no matching entry)

Limitations: The erdosproblems.com page and its comment thread could not be read (403), so the site's current status flag and any recent comments (including AI attempts) are unchecked. Only one web search was run. The Wikipedia article's references stop at 2013.

## Computational approaches

A counterexample must avoid cycles of lengths 4, 8, 16, ... simultaneously; by Carr it can be taken predominantly cubic. Options: (1) exhaustive generation of cubic graphs of girth ≥ 5 (genreg / snarkhunter / minibaum) beyond Markström's 30-vertex bound, filtering for 8- and 16-cycles: 32 and perhaps 34 vertices look reachable on a desktop because the girth restriction prunes heavily; (2) SAT Modulo Symmetries with lazily added cycle-exclusion clauses for degree sequences allowed by Carr's 4/7 result; (3) extending the general (non-cubic) bound of 17 vertices; (4) heuristic search for graphs whose only power-of-two cycles are long (Markström-type 24-vertex examples) to understand near-counterexamples. Largest verified in fetched sources: ≥ 17 vertices in general, ≥ 30 for cubic and for cubic bipartite.

## Mathematical approaches

Prove the conjecture for further restricted classes (the literature is a ladder of such results: planar claw-free, 3-connected cubic planar, P_k-free for growing k, diameter 2): e.g. P14-free, cubic bipartite with extra structure, Cayley or vertex-transitive cubic graphs, graphs of diameter 3, outerplanar-like or bounded-treewidth cubic graphs; strengthen the structure theory of minimal counterexamples (reducible configurations in the style of Carr and Markström) and feed the reductions back into the computer search.

Scout's tractability assessment: Famous and hard; a full resolution is not a realistic goal and the problem has been attacked by many people and by large AI systems (AlphaEvolve reported no counterexample up to 40 vertices in heuristic search). Realistic contributions: raising the exhaustive cubic bound from 30, a new forbidden-path or diameter class, or new reducible configurations. Include as the 'stretch' problem only.

## Formalization feasibility

Already stated in Lean 4 in formal-conjectures (`Erdos64.erdos_64`) using only Mathlib notions (`SimpleGraph.minDegree`, `Walk.IsCycle`, `Walk.length`). Formalising class-restricted proofs is ordinary but laborious graph theory; certified small-case verification would need a verified checker or SAT proof import.

## Prerequisites

Basic graph theory (cycles, girth, connectivity, planarity), reducibility arguments, orderly generation of cubic graphs, SAT encodings with symmetry breaking.

## Unverified items

- The original printed source and year of the conjecture (Wikipedia says 1995; not checked against Erdős's paper).
- erdosproblems.com/64 status and comments (page not retrievable).
- Liu–Montgomery, Hu–Shen, Hegde–Sandeep–Shashank, Carr's diameter-2 note and the AlphaEvolve remark are from search snippets only.
- Feasibility of 32-34 vertex cubic enumeration is an estimate.
- Carr's preprints are single-author, unrefereed as far as the scout knows.
