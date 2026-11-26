# CJ-0001 — Collins–Shor conjecture on the peak of the distance characteristic polynomial of a tree

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Let $T$ be a tree of order $n \ge 3$ with distance matrix $\mathcal{D}(T)$ (the $(i,j)$ entry is the length of the path from $v_i$ to $v_j$). Let $\delta_k(T)$ be the coefficient of $x^k$ in $\det(\mathcal{D}(T) - xI)$ and, for $0 \le k \le n-2$, let $d_k(T) = 2^{k-(n-2)}\,|\delta_k(T)|$ be the normalized coefficients. Conjecture 1.2 (Collins–Shor), verbatim: "The [normalized] coefficients of the distance characteristic polynomial for any tree $T$ with $n$ vertices are unimodal with peak between $\lfloor n/2 \rfloor$ and $\lceil n - n/\sqrt{5} \rceil$." Unimodality (indeed log-concavity) is Theorem 2.1 of the same paper. The open part is the location: every index $k$ at which $d_0(T),\dots,d_{n-2}(T)$ attains its maximum satisfies $\lfloor n/2 \rfloor \le k \le \lceil n - n/\sqrt{5} \rceil$. (The source does not say how a tie between two maximal coefficients is to be read; the project uses the strong reading 'every maximizing index' and records ties explicitly.)

**Source.** G. Aalipour, A. Abiad, Z. Berikkyzy, L. Hogben, F. H. J. Kenter, J. C.-H. Lin, M. Tait, Proof of a conjecture of Graham and Lovász concerning unimodality of coefficients of the distance characteristic polynomial of a tree, arXiv:1507.02341, Conjecture 1.2 (a search result reports the journal version as Electron. J. Linear Algebra, 2018; not verified from the journal); originally Conjecture 9 of K. L. Collins, On a conjecture of Graham and Lovász about distance matrices, Discrete Appl. Math. 25 (1989) 27-35, attributed there to P. Shor. <https://arxiv.org/abs/1507.02341>

**Statement checked against:** primary-source. The catalogued wording is Conjecture 1.2 of arXiv:1507.02341, compared with the paper's TeX source on 2026-11-26. Collins (1989) was not accessed; according to arXiv:1507.02341 it states the bounds without floor and ceiling.

## Definitions and hypotheses

T is a tree (connected acyclic simple graph) on n vertices; D(T) is the n x n matrix of shortest-path distances. The polynomial is det(D - xI) (sign convention matters only up to absolute values). k ranges over 0..n-2 only (the top coefficients are excluded by the normalization range). The original Graham–Lovász claim that the peak is always at floor(n/2) is FALSE (disproved by Collins: for paths the peak is at about (1 - 1/sqrt(5)) n, for stars at floor(n/2)), so do not target the original form. 'Peak' must be defined carefully when two consecutive coefficients tie; check the primary text for the convention. The tree results do not extend to all graphs: the paper notes the Heawood graph has log-concave but not unimodal coefficients (zeros are involved), so the hypothesis 'tree' is essential. Easy confusion: Collins also made a DIFFERENT conjecture relating the peak of the adjacency characteristic polynomial coefficients of a tree to the peak of the distance one; per a search snippet that one was refuted by Wagner (arXiv:2104.14516). That is not the Collins–Shor interval conjecture stated here.

## Known partial results

- Unimodality and log-concavity of |\delta_k(T)| and d_k(T) for every tree (Theorem 2.1); this proves the unimodality half of Graham–Lovász. — Aalipour, Abiad, Berikkyzy, Hogben, Kenter, Lin, Tait, arXiv:1507.02341 <https://arxiv.org/abs/1507.02341> (source fetched)
- Upper bound on peak location: at most ceil(2n/3) for every tree of order n; improves to ceil(((2-rho)/(3-rho)) n) if the tree has at least rho*C(n-1,2) paths of length 2 (Theorem 3.3). Lower bound: at least floor((n-2)/(1+d)) for a tree of diameter d (Theorem 3.6). — Aalipour et al., arXiv:1507.02341 <https://arxiv.org/abs/1507.02341> (source fetched)
- Peak for paths is at about (1 - 1/sqrt(5)) n and for stars at floor(n/2) (Collins), which disproves the original peak claim and motivates the interval. — As reported in arXiv:1507.02341 (Collins's own paper not fetched) <https://arxiv.org/abs/1507.02341> (source fetched)
- Sage computations confirm Conjecture 1.2 for all trees of order at most 20. — Aalipour et al., arXiv:1507.02341 (the ar5iv rendering showed '2020', read as 20) <https://arxiv.org/abs/1507.02341> (source fetched)
- Extension to block graphs: unimodality part proved for block graphs; peak established only for several extremal cases of uniform block graphs with small diameter. — A. Abiad, B. Brimkov, S. Hayat, A. P. Khramova, J. H. Koolen, 'Extending a conjecture of Graham and Lovász on the distance characteristic polynomial', arXiv:2206.07561 (submitted 15 June 2022; abstract page fetched) <https://arxiv.org/abs/2206.07561> (source fetched)

## Relevant literature

- G. Aalipour, A. Abiad, Z. Berikkyzy, L. Hogben, F. H. J. Kenter, J. C.-H. Lin, M. Tait, Proof of a conjecture of Graham and Lovász concerning unimodality of coefficients of the distance characteristic polynomial of a tree, arXiv:1507.02341, Conjecture 1.2 (a search result reports the journal version as Electron. J. Linear Algebra, 2018; not verified from the journal); originally Conjecture 9 of K. L. Collins, On a conjecture of Graham and Lovász about distance matrices, Discrete Appl. Math. 25 (1989) 27-35, attributed there to P. Shor. <https://arxiv.org/abs/1507.02341>
- Aalipour, Abiad, Berikkyzy, Hogben, Kenter, Lin, Tait, arXiv:1507.02341 <https://arxiv.org/abs/1507.02341>
- Aalipour et al., arXiv:1507.02341 <https://arxiv.org/abs/1507.02341>
- As reported in arXiv:1507.02341 (Collins's own paper not fetched) <https://arxiv.org/abs/1507.02341>
- Aalipour et al., arXiv:1507.02341 (the ar5iv rendering showed '2020', read as 20) <https://arxiv.org/abs/1507.02341>
- A. Abiad, B. Brimkov, S. Hayat, A. P. Khramova, J. H. Koolen, 'Extending a conjecture of Graham and Lovász on the distance characteristic polynomial', arXiv:2206.07561 (submitted 15 June 2022; abstract page fetched) <https://arxiv.org/abs/2206.07561>

## Open-status evidence

- Most recent source: Aalipour et al., arXiv:1507.02341 (states that the location of the peak for trees remains open); the 2022 follow-up arXiv:2206.07561 (abstract only fetched) still treats peak location as the unresolved part and settles it only in extremal block-graph cases.
- URL: <https://arxiv.org/abs/2206.07561>
- Date: 2022-06-15 (latest dated source fetched); no 2024–2026 source stating the status was found
- Content: From arXiv:1507.02341 (via fetch tool): 'the question of the location of the peak of the unimodal sequence' of normalized coefficients remains open for trees; about the Collins–Shor conjecture: 'No more results are known about that conjecture.'

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- Graham Lovász conjecture distance characteristic polynomial tree coefficients peak location conjecture open 2024 OR 2025 OR 2026
- Collins Shor conjecture peak location normalized coefficients distance characteristic polynomial tree 2025 OR 2026 proof OR counterexample

Sources checked:

- General web search (2 queries)
- ar5iv rendering of arXiv:1507.02341 (full text)
- arXiv abstract page 2206.07561

Limitations: No direct arXiv listing search, no Google Scholar citation trawl of the 2018 ELA paper, no MathOverflow or Open Problem Garden check. The evidence of openness is 4+ years old; an unsuccessful 2025–2026 search does not establish that nobody has settled it. Forward citations of arXiv:1507.02341 and arXiv:2206.07561 should be checked before investing.

## Computational approaches

Everything is exact integer arithmetic: generate all trees of order n (nauty 'gentreeg' or networkx nonisomorphic_trees), build the integer distance matrix, compute the characteristic polynomial exactly (Berkowitz / fraction-free methods in SymPy, FLINT, Sage), locate the argmax of 2^k |delta_k|. Literature has all trees up to n = 20. Tree counts grow roughly x2.7 per vertex (from memory, OEIS A000055: 823,065 trees at n=20; about 5.6 million at n=22; about 39 million at n=24), so a desktop can plausibly extend exhaustive verification to n around 23–25 and probe extremal families (paths, stars, caterpillars, spiders, brooms, double stars) to n in the hundreds. Also record which trees attain the extreme peak positions to guess a structural extremal statement (is the path always the upper extreme and the star the lower extreme?).

## Mathematical approaches

Graham–Lovász give a combinatorial formula for the coefficients delta_k(T) in terms of counts of certain subforests of T; Aalipour et al. obtain log-concavity through real-rootedness (the distance matrix of a tree has exactly one positive eigenvalue) and get peak bounds from ratio estimates of consecutive coefficients (Newton-type inequalities). Routes for partial progress: (i) sharpen the general upper bound ceil(2n/3) towards n(1 - 1/sqrt(5)) ≈ 0.553 n; (ii) improve the diameter-dependent lower bound towards floor(n/2); (iii) prove the interval for specific classes (caterpillars, spiders, double stars, trees of bounded diameter) using explicit distance-spectrum or recurrence formulas; (iv) monotonicity of the peak under tree transformations (e.g. grafting / Kelmans-type moves from star towards path).

Scout's tractability assessment: Best 'newcomer' target in this list. The headline (full interval for all trees) may be hard, but there is a clearly quantified gap (proved upper bound 2n/3 versus conjectured about 0.553n; proved lower bound depending on diameter versus conjectured n/2), an existing exhaustive bound (n <= 20) that can be pushed, and many natural tree classes where a proof looks feasible. Unimodality itself is done; do not re-prove it. Main risk: thin recent literature means a result could exist that this search missed.

## Formalization feasibility

Not checked in this session. From memory: Mathlib has SimpleGraph.dist, trees (SimpleGraph.IsTree), Matrix.charpoly and Polynomial.coeff, so the statement is expressible after defining the distance matrix (not in Mathlib as far as I recall). Verified small cases (n <= some bound) could be checked by 'decide'/'native_decide'-style computation only for very small n; the exhaustive search itself is better certified outside Lean.

## Prerequisites

Linear algebra (characteristic polynomial, eigenvalue interlacing, inertia), basic graph theory (trees, distance), log-concavity and Newton's inequalities for real-rooted polynomials, exact computation with integer matrices, tree generation tools (nauty/Sage).

## Unverified items

- Exact bibliographic data of the Graham–Lovász 1978 paper (title, volume, pages) and of Collins's paper were not fetched; given from memory / search-result titles.
- That the 2018 journal version appeared in Electronic Journal of Linear Algebra (search snippet only).
- The statement text is the fetch tool's rendering of Conjecture 1.2, not a character-exact quotation; tie-breaking convention for 'peak' not checked.
- Tree counts (OEIS A000055 values) quoted from memory.
- Wagner's 2021 neural-network counterexample (arXiv:2104.14516) concerns a different Collins conjecture according to a search snippet; this should be double-checked against the paper.
- No 2023–2026 paper on the peak location was found, which is not proof that none exists.

## Project notes

- 2026-11-26, coordinating agent (Claude, `claude-fable-5-2`): the TeX source of
  arXiv:1507.02341 was downloaded and the statement of Conjecture 1.2 compared
  with the catalogue entry. The paper notes that Collins's Conjecture 9 is
  stated without floor and ceiling, that `⌊n/2⌋` is "clearly the intended lower
  bound", and that the ceiling is needed in the upper bound; it also records
  that the conjecture appears as Conjecture 2.6 in Aouchiche and Hansen,
  *Distance spectra of graphs: a survey*, Linear Algebra Appl. 458 (2014)
  301–386, with the comment "No more results are known about that conjecture."
- The same source states: "Computations on Sage confirm this conjecture for
  all trees of order at most 20."
- One additional web search on the same day ("distance characteristic
  polynomial" tree coefficients peak location … 2025 OR 2026) returned nothing
  after the 2022 paper arXiv:2206.07561. It also surfaced a 2021 survey,
  arXiv:2103.00647, which has not been read.
- The scout's remark about Wagner (arXiv:2104.14516) concerns a different
  conjecture of Collins and remains unverified.

### Corrections to the scout record above (2026-11-26)

An independent review of revision `e34acfc` pointed out two inconsistencies in
this dossier; the scout's text is left as written and corrected here.

- *Statement.* The item under "Unverified items" saying that the statement text
  is a tool rendering and not character-exact is superseded: the statement in
  the "Statement" section was compared with the TeX source of arXiv:1507.02341
  on 2026-11-26 (first project note above).
- *Quotation.* Under "Open-status evidence", the sentence "No more results are
  known about that conjecture." is attributed to arXiv:1507.02341. It is a
  quotation that arXiv:1507.02341 takes from Aouchiche and Hansen's 2014
  survey. The statement that the peak location "remains open" is the paper's
  own (its Section 3).
- *Journal.* That the paper appeared in Electron. J. Linear Algebra in 2018 is
  reported by a search result and was not verified from the journal.
