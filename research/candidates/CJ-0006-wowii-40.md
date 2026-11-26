# CJ-0006 — Written on the Wall II, Conjecture 40

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Verbatim from the WOWII list: "If G is a simple connected graph on more than one vertex, then f(G) ≥ CEIL[(p(G)+b(G)+1)/2]". Definitions, verbatim from wowIIdefs.js: f(G) (forest number) = "The number of vertices of a largest induced forest of the graph."; p(G) (path covering number) = "The minimum number of vertex disjoint paths needed to cover the vertices of the graph."; b(G) (bipartite number) = "The maximum number of vertices of an induced bipartite subgraph of the graph." In LaTeX: $f(G) \ge \lceil (p(G)+b(G)+1)/2 \rceil$.

**Source.** E. DeLaViña, Written on the Wall II (Conjectures of Graffiti.pc), entry 40, dated 5 March 2004; read from the Internet Archive snapshot of 2026-07-23. <https://web.archive.org/web/20260723161800id_/http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html>

**Statement checked against:** primary-source. Read from an archived copy.

## Definitions and hypotheses

G finite, simple, connected, at least 2 vertices. The paths in a path cover are subgraph paths (not required to be induced), pairwise vertex-disjoint, and single vertices count as paths (the last point is stated in the formal-conjectures docstring for conjecture 372, not on the WOWII page). f(G) = n minus the decycling (feedback vertex) number. The ceiling matters: the bound is an integer inequality.

## Known partial results

- Comment on the WOWII page, verbatim: "Mar 6, 2004, DeLaVina: For a connected graph on more than one vertex it is easily shown that f(G) ≥ b(G)/2 + 1. Thus, in the special case that path covering is one, the result follows." So the conjecture holds for traceable graphs (p(G) = 1). — DeLaViña, WOWII list, entry 40 (archived snapshot 2026-07-23) <https://web.archive.org/web/20260723161800id_/http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html> (source fetched)
- The neighbouring entry 41 (f(G) ≥ CEIL[dist_avg(V)*(1+sqrt(p(G)))]) is marked false on the same page, with a 2005 counterexample built from binary stars; so bounds of this family mixing f and p do fail. — DeLaViña, WOWII list, entry 41 <https://web.archive.org/web/20260723161800id_/http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html> (source fetched)

## Relevant literature

- E. DeLaViña, Written on the Wall II (Conjectures of Graffiti.pc), entry 40, dated 5 March 2004; read from the Internet Archive snapshot of 2026-07-23. <https://web.archive.org/web/20260723161800id_/http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html>
- DeLaViña, WOWII list, entry 40 (archived snapshot 2026-07-23) <https://web.archive.org/web/20260723161800id_/http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html>
- DeLaViña, WOWII list, entry 41 <https://web.archive.org/web/20260723161800id_/http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html>

## Open-status evidence

- Most recent source: google-deepmind/formal-conjectures, FormalConjectures/WrittenOnTheWallII/GraphConjecture40.lean on the main branch
- URL: <https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/WrittenOnTheWallII/GraphConjecture40.lean>
- Date: fetched 2026-11-26
- Content: The theorem `conjecture40` is tagged `@[category research open, AMS 5]` with proof `sorry`. The WOWII page (snapshot 2026-07-23) shows status letter 'O' for entry 40. The repository README also lists 40 as open.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- "Written on the Wall II" OR "Graffiti.pc" conjecture 199 OR 84 OR 40 "largest induced tree" OR "induced forest" "Hamiltonian path" proof OR counterexample 2025 2026
- GitHub: full download of FormalConjectures/WrittenOnTheWallII/*.lean, grep for `research open`
- GitHub: README of 1337isnot1337/solved-conjectures

Sources checked:

- google-deepmind/formal-conjectures (main branch)
- DeLaViña WOWII all.html + wowIIdefs.js (Internet Archive snapshot 2026-07-23)
- 1337isnot1337/solved-conjectures README
- one general web search (no hit for conjecture 40)

Limitations: Same as for conjecture 199: no arXiv full-text, MathOverflow or open-PR scan. The WOWII page has not obviously been updated in years, so its 'O' is weak evidence; the Lean tag is the only current signal. One search with no hit does not establish openness.

## Computational approaches

All three invariants are NP-hard in general but trivial for n ≤ 12 by subset enumeration (f and b) and by 'maximum linear forest' search or DP (p(G) = n minus the maximum number of edges in a spanning subgraph that is a disjoint union of paths). Exhaustive check over connected graphs up to n = 10 (geng), then targeted search on graphs with large path covering number (trees with many leaves, graphs with many pendant vertices, blow-ups of stars), since p = 1 is already proved. An ILP/SAT formulation with f, p, b as certified optima is possible for n up to about 20 on structured families. No verified range appears in the sources fetched.

## Mathematical approaches

Induct on the path cover number starting from DeLaViña's p = 1 case; attempt p = 2 next. Use f(G) ≥ α(G)+1 for connected nontrivial G, Gallai–Milgram (p(G) ≤ α(G)) and b(G) ≤ 2α(G) to see where slack is lost; prove the bound for trees and bipartite graphs first (there b = n and f is the forest number of a bipartite graph), then for graphs with a cut vertex via block decomposition.

Scout's tractability assessment: A realistic ladder exists: p = 1 is done, so p = 2, trees, and bipartite graphs are concrete next rungs, and an exhaustive small-case table is cheap. A counterexample is also plausible (entry 41, of the same shape, is false). This is a low-fame conjecture with little literature, so even a modest theorem or a counterexample is a genuine contribution; the risk is that someone in the formal-conjectures community closes it first.

## Formalization feasibility

Already stated in Lean 4 in formal-conjectures (`conjecture40`, using `pathCoverNumber`, `b`, `largestInducedForestSize` from the repository's util library). Mathlib itself has `SimpleGraph.IsAcyclic`, induced subgraphs and colourability, but (not checked in detail) no packaged path-cover or forest-number invariants.

## Prerequisites

Basic graph theory (independent sets, bipartite subgraphs, path covers, Gallai–Milgram), small-graph enumeration with nauty, integer programming or SAT modelling, elementary Lean 4.

## Unverified items

- Gallai–Milgram and the inequalities f ≥ α+1, b ≤ 2α are quoted from memory.
- The convention that single vertices count as paths is taken from the formal-conjectures docstring of conjecture 372, not from DeLaViña's page.
- Computational size estimates are estimates.
- Whether an unmerged PR already resolves it was not checked.
