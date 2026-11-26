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

### Literature audit, 2026-11-26 (session 2)

*Literature Auditor subagent (Claude, model `claude-fable-5-2`). "Read" below
means: the PDF was downloaded with the fetch tool and its pages were read as
rendered page images. The fetch tool's own text extraction failed on every PDF,
so nothing below rests on an automatic summary. Page and statement numbers are
those of the versions named. Access details, queries and gaps are in the
matching subsection under "Novelty search coverage and limitations".*

**A. arXiv:1507.02341v3 (Aalipour et al.), read in full (11 pages).**

- p. 3: "The conjecture regarding the location of the peak was disproved by
  Collins [4] who showed that for both stars and paths the sequence
  `d_0(T), …, d_{n−2}(T)` is unimodal, but for paths the peak is at
  approximately `(1 − 1/√5)n` (and at `⌊n/2⌋` for stars)." Footnote 1: "Despite
  use of the term *coefficient* throughout [4], the sequence discussed there is
  `d_k(T)`, not `δ_k(T)`."
- p. 3: "In [4], Conjecture 9 is stated without the floor or ceiling; `⌊n/2⌋`
  is clearly the intended lower bound, since [4, Theorem 1] establishes `⌊n/2⌋`
  as the peak location for a star. An examination of the proof of [4, Theorem 3]
  shows that the ceiling is needed in the upper bound (although the path `P_n`
  may attain either the floor or the ceiling depending on `n`)." So, according
  to this paper, Collins's Theorem 1 is the star and Theorem 3 is the path.
- Section 3, p. 5: "the question of the location of the peak of the unimodal
  sequence of normalized coefficients … remains open"; "Computations on *Sage*
  [10, 11] confirm this conjecture for all trees of order at most 20."
- Peak-location results proved in the paper, complete list: Lemma 3.2 (two
  ratio criteria for a real-rooted polynomial), Theorem 3.3 (peak at most
  `⌈((2−ρ)/(3−ρ)) n⌉` when `T` has at least `ρ·C(n−1,2)` paths of length 2;
  `⌈2n/3⌉` for every tree), Remark 3.4 (for the star the bound is `⌈n/2⌉`),
  Lemma 3.5 (`d_{n−3}/d_{n−2} < nd/3`), Theorem 3.6 (peak at least
  `⌊(n−2)/(1+d)⌋` for diameter `d`). There is no corollary for double stars,
  trees of diameter 3, caterpillars or any other family. The words "double
  star", "caterpillar" and "diameter 3" do not occur.
- Proof of Theorem 3.3, p. 6: "`d_0(T) = n − 1` is given in [9, Theorem 3]"
  (Graham–Pollak) and "the formula `d_1(T) = 2n(n−1) − 2N_{P_3}(T) − 4` follows
  from [7, Theorem 4.1]" (Edelberg–Garey–Graham 1976). This is the project's L2
  (`d_1 = 2n² − 6 − Σ deg²`, since `2N_{P_3} = Σ deg² − 2n + 2`).
- Tie convention: the paper defines "unimodal" (p. 2) but never defines "peak
  location" when two coefficients tie.

**B. arXiv:2206.07561v1 (Abiad, Brimkov, Hayat, Khramova, Koolen, 15 Jun 2022), read in full (19 pages).**

- p. 2: "Little progress on this problem is known. Collins [9] confirmed the
  conjecture for stars, and also showed that for a paths the sequence is
  unimodal with a maximum value at `(1 − 1/√5)n`." The Collins–Shor statement
  is its Conjecture 1.1.
- The paper works with the *un-normalized* coefficients of block graphs (p. 9:
  "we will not use the normalized coefficients to investigate Question 1.2").
- Peak-location results, complete list: Theorem 4.3 (windmill `W(k,t)`,
  `k ≥ 2`, `t ≥ 3`: peak at `kt(t−1)/(2(t+1)) + O(log k)` as `k → ∞`),
  Corollary 4.5 (friendship graph), Theorem 4.6 (`W(2,t)`: peak at `⌊n/2⌋`),
  Theorem 4.7 (barbell `B(t,ℓ)`, `ℓ ∈ {2,3,4,5}`), Corollary 4.8 (lollipop
  `L(t,ℓ)`, `ℓ ∈ {2,…,5}`). None of these graphs is a tree other than in
  degenerate cases, and no result concerns double stars, trees of diameter 3 or
  caterpillars; those words do not occur. No computational verification of the
  tree conjecture is reported.
- The introduction says "As a corollary of our results we obtain Collins'
  result for stars [9]"; no such corollary is stated explicitly in the body of
  v1 (Theorem 4.3 assumes `t ≥ 3`; the star is `W(k,2)`).
- Section 5: Question 5.1 (block graphs: peak between `⌊n/3⌋` and `⌊n/2⌋`?),
  from SageMath experiments on block paths.
- Method relevant to L3 / MD-0003: Theorems 4.6 and 4.7 obtain
  `p_D(x) = (x+1)^{…} · p_B(x)` with `B` the quotient matrix of an equitable
  partition, citing "[16, Theorem 3.3]" (the Hogben–Reinhart survey, item C);
  Remark 4.4 states the same factorisation shape for a general windmill.
- Its reference [1] gives the journal data of the source paper: Electron. J.
  Linear Algebra 34:373–380, 2018.

**C. arXiv:2103.00647 (Hogben, Reinhart, survey), pages 5–12 read (Sections 2.1–3.4); the rest not read.**

- Section 2.2 restates the conjecture (Conjecture 2.10) and Collins's result
  (Theorem 2.9: "For both stars and paths the sequence … is unimodal, but for
  paths the peak is at approximately `(1 − 1/√5)n` (for stars it is at
  `⌊n/2⌋`)"), then Theorem 2.12 (the two bounds of item A). It reports nothing
  further on peak location for trees. It dates Collins's disproof "in 1985".
- Theorem 3.1(1): twins `v_k, v_{k+i}` (`i = 1,…,r−1`) give the eigenvalue `−2`
  (independent twins) or `−1` (adjacent twins) of `D(G)` with multiplicity at
  least `r − 1`.
- Theorem 3.3, verbatim apart from typography: "Let `X = (X_1, …, X_p)` be a
  partition of the vertices of `G` with `n_1 ≤ ⋯ ≤ n_p` and let `k` be the least
  index such that `n_k ≥ 2`. Suppose that `v, u ∈ X_j` implies `v = u` or `v`
  and `u` are twins. For `j = k, …, m`, let `λ_j` denote the eigenvalue `λ`
  specified in Theorem 3.1 for `D*` and the type of twin in `X_j`. Let `B`
  denote the quotient matrix of `D*` for `X`. Then
  `spec(D*) = {λ_k^{(n_k−1)}, …, λ_p^{(n_p−1)}} ∪ spec(B)` (as multisets)."
  (The index `m` is as printed.)
- **Consequence for L3 / MD-0003.** For a caterpillar with spine `v_1…v_s` and
  `c_i ≥ 1` leaves at `v_i`, take the `s` singletons `{v_i}` and the `s` leaf
  classes (each a set of independent twins). Theorem 3.3 gives
  `spec(D) = {(−2)^{(Σ(c_i−1))}} ∪ spec(B)` with `Σ(c_i − 1) = n − 2s` and `B`
  of size `2s × 2s`, that is, `det(xI − D) = (x+2)^{n−2s} det(xI − B)`. L3 is
  therefore a direct special case of a published general theorem. The explicit
  matrix for caterpillars was not seen in any source read. (This specialisation
  is the auditor's own two-line check, not a quotation.)

**D. Graham and Lovász, Adv. Math. 29 (1978) 60–88, pages 60–67 and 80–86 read (scan on R. L. Graham's publication page); pages 68–79 and 87–88 not read.**

- Inverse formula: **Lemma 1, p. 66**: "`D^{-1} = (d*_{ij})` is given by
  `d*_{ij} = (2 − d_i)(2 − d_j)/(2(n − 1)) + { −d_i/2 if i = j; a_{ij}/2 if i ≠ j }`",
  with `d_i` the degree of `v_i` and `(a_{ij})` the adjacency matrix. In the scan
  the minus signs inside `(2 − d_i)(2 − d_j)` and in front of `d_i/2` are not
  legible; they are fixed by Fact 3 (p. 65) and by the matrix in eq. (10), whose
  diagonal entries are `−2λ − d_i`. In matrix form this is
  `D^{-1} = −L/2 + ττᵀ/(2(n−1))`, `τ_v = 2 − deg(v)`: the formula quoted from
  memory in L1 is confirmed, with this location.
- Characteristic polynomial through the Laplacian: **eq. (10)** defines the
  `(n+1) × (n+1)` bordered matrix `D'(λ)` with corner `−(n−1)`, border
  `2 − d_i`, diagonal `−2λ − d_i` and off-diagonal `a_{ij}` (that is,
  `[[−(n−1), τᵀ], [τ, −2λI − L]]`); **Fact 4, eq. (11)**:
  `det D'(λ) = −(n−1) 2^n Δ*_T(λ)` where `Δ*_T(λ) = det(D^{-1} − λI)`;
  **eq. (12)**: `Δ_T(λ) = (−λ)^n (det D) Δ*_T(λ^{-1}) = −(n−1) 2^{n−2} λ^n Δ*_T(λ^{-1})`;
  **eq. (13)**: `δ_k(T) = −(n−1) 2^{n−2} δ*_{n−k}(T) = ¼ δ'_{n−k}(T)`.
- **Consequence for L1 / MD-0002.** Expanding the bordered determinant,
  `det D'(μ) = −(n−1) det(−2μI − L) − τᵀ adj(−2μI − L) τ`; with (11), (12) and
  `λ = 2x`, `μ = 1/(2x)` one gets
  `det(D − 2xI) = (−1)^{n+1} 2^{n−2} [(n−1) det(I + xL) − x τᵀ adj(I + xL) τ]`,
  which is exactly the identity of L1 / MD-0002. The identity is thus a
  rewriting of Graham–Lovász (10)–(12). (The three-line rewriting is the
  auditor's computation and has not been reviewed; the displayed equations
  (10)–(13) are in the paper.)
- p. 63, eq. (6): `δ_1(T) = (−1)^{n−1} 2^{n−3} (4N_{2P_1}(T) + 2N_{P_2}(T) + 4N_{P_1}(T) − 4)`,
  which equals the `d_1` formula of item A (so L2's formula goes back to
  Edelberg–Garey–Graham and to this paper).
- p. 81, Theorem, eq. (42), and Theorem′: every `δ_k(T)` is
  `(−1)^{n−1} 2^{n−k−2}` times an explicit linear combination of the counts
  `N_F(T)` of subforests `F` with `k+1`, `k` and `k−1` edges. Table III
  (pp. 87–88, not read) lists the coefficients `A_F^{(k)}` for `k ≤ 5`. A
  subforest formula for `d_2` (the "natural next case" in `STATE.md`) is
  therefore already available from this theorem.
- p. 83, the original statement: "It appears that in fact for each tree `T`,
  the quantities `(−1)^{n−1} δ_k(T)/2^{n−k−2}` are *unimodal* with the maximum
  value occurring for `k = [n/2]`. We see no way to prove this, however."
- Table II (pp. 85–86) lists the normalized coefficients of all trees on at
  most eight vertices; it is an independent published data set against which
  the project's code can be compared (not done in this audit).

**E. arXiv:2407.03309v1 (Jana, Mahato, Sivasubramanian, 3 Jul 2024), "Unimodality and peak location of the characteristic polynomials of two distance matrices of trees", read in full (19 pages). New to this dossier.**

- It concerns two *other* matrices of a tree (the Min-4PC matrix and the
  2-Steiner distance matrix), with un-normalized coefficients. Theorem 3: peak
  of the Min-4PC polynomial of any tree in `[⌊(n−2)/3⌋, ⌈(n+1)/3⌉]`.
  Theorems 18 and 20: peak for the 2-Steiner matrix of the star and of the
  "bi-star" `S_{1,n−3}`; Theorem 28 and Conjecture 29: the path.
- For the ordinary distance matrix it only recalls the literature (p. 1: the
  unimodality part "was proved by Aalipour et. al. … and the peak location was
  disproved by Collins"). It contains no result on the Collins–Shor interval
  and no computational verification of it. Its bi-star result is not about `D`.

**F. Collins (1989) — not read.** See the access record below. Everything said
about its Theorem 1, Theorem 3 and Conjecture 9 is second-hand (items A, B, C).

**Answers within this coverage.**

1. *Double stars, diameter ≤ 3, caterpillars.* In the sources read (A, B, E in
   full; C and D in part) the only families for which the peak of the distance
   polynomial of a tree is located are stars and paths (Collins, as cited), and
   the only general bounds are Theorems 3.3 and 3.6 of item A. For a double
   star Theorem 3.6 gives `⌊(n−2)/4⌋`. No statement of the lower bound
   `peak ≥ ⌊n/2⌋` for double stars, for trees of diameter 3 or for caterpillars
   was found. This does not establish that none exists: Collins (1989) and her
   1986 thesis were not read, and several citing papers were seen by title only.
2. *Exhaustive verification.* The only published verification found is "all
   trees of order at most 20" (item A, Section 3). Items B, C (pages read) and E
   report none. Reference [10] of item A (J. C.-H. Lin's Sage worksheet,
   `TreePeak.pdf`) was not accessed.
3. *Prior sources for project findings.* L1 / MD-0002: Graham–Lovász 1978,
   Lemma 1 and eqs. (10)–(13). L2: Graham–Lovász eq. (6) and item A. L3 /
   MD-0003: special case of Hogben–Reinhart Theorem 3.3. For the ratio
   comparisons (refutation of A(i), Hypothesis A(ii); MD-0004, MD-0005) no
   source was found in one quick search; that search is far too thin to support
   any statement about novelty.

## Relevant literature

Added by the literature audit of 2026-11-26 (session 2):

- R. L. Graham, L. Lovász, Distance matrix polynomials of trees, Adv. Math. 29 (1978) 60–88. Scan: <https://mathweb.ucsd.edu/~ronspubs/78_12_matrix_polynomials.pdf> (pp. 60–67, 80–86 read). DOI `10.1016/0001-8708(78)90005-1` resolves to an Elsevier record; the landing page was not readable.
- K. L. Collins, On a conjecture of Graham and Lovász about distance matrices, Discrete Appl. Math. 25 (1–2) (October 1989) 27–35, DOI `10.1016/0166-218X(89)90044-9` (bibliographic data confirmed from the Crossref record; full text not accessed).
- K. L. Collins, Distance matrices of trees, Ph.D. thesis, MIT, 1986 (advisor R. P. Stanley), <https://dspace.mit.edu/handle/1721.1/77687> (record page read; PDF not accessed).
- L. Hogben, C. Reinhart, Spectra of variants of distance matrices of graphs and digraphs: a survey, arXiv:2103.00647; cited in arXiv:2206.07561 as La Matematica 1 (2022) 186–224 (pp. 5–12 read).
- R. Jana, I. Mahato, S. Sivasubramanian, Unimodality and peak location of the characteristic polynomials of two distance matrices of trees, arXiv:2407.03309 (read in full); a citation index lists it in Computational and Applied Mathematics, DOI `10.1007/s40314-025-03163-5` (not verified).
- arXiv:2206.07561 is cited in arXiv:2407.03309 as Linear Algebra Appl., DOI `10.1016/j.laa.2023.03.027` (journal version not read).
- J. S. do Nascimento, R. R. Del-Vecchio, M. A. A. de Freitas, The distance matrix of caterpillar, Discrete Appl. Math. 266 (2019) 141–152 — multiplicity of `−2` as a distance eigenvalue of caterpillars (search-result abstract only; **not read**). Relevant to L3 / MD-0003.
- M. Edelberg, M. R. Garey, R. L. Graham, On the distance matrix of a tree, Discrete Math. 14 (1976) 23–39 (not read; a scan is listed at <https://mathweb.ucsd.edu/~ronspubs/76_04_distance_matrix.pdf>).

Scout's original list:


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

### Literature audit, 2026-11-26 (session 2)

- Latest dated source read in full that describes the status: arXiv:2407.03309v1
  (3 July 2024), p. 1, which describes the peak-location question for the
  distance matrix only by recalling Collins's disproof of the original
  Graham–Lovász location, and proves nothing about the Collins–Shor interval.
- arXiv:2206.07561v1 (15 June 2022), p. 2: "Little progress on this problem is
  known."
- A citation index (Semantic Scholar API, queried 2026-11-26) lists 5 papers
  citing arXiv:1507.02341 and 14 citing Collins (1989); none of the titles
  announces a resolution of the Collins–Shor conjecture. Titles only were seen
  for most of them (list under "Novelty search coverage and limitations").
- Coverage statement: within the sources listed in this audit, no proof or
  refutation of the conjecture, and no proof of either half for a family other
  than stars and paths, was found. The coverage excludes Collins (1989) itself,
  MathSciNet, zbMATH, Google Scholar, MathOverflow and non-English literature.

## Novelty search coverage and limitations

Queries run:

- Graham Lovász conjecture distance characteristic polynomial tree coefficients peak location conjecture open 2024 OR 2025 OR 2026
- Collins Shor conjecture peak location normalized coefficients distance characteristic polynomial tree 2025 OR 2026 proof OR counterexample

Sources checked:

- General web search (2 queries)
- ar5iv rendering of arXiv:1507.02341 (full text)
- arXiv abstract page 2206.07561

Limitations: No direct arXiv listing search, no Google Scholar citation trawl of the 2018 ELA paper, no MathOverflow or Open Problem Garden check. The evidence of openness is 4+ years old; an unsuccessful 2025–2026 search does not establish that nobody has settled it. Forward citations of arXiv:1507.02341 and arXiv:2206.07561 should be checked before investing.

### Literature audit, 2026-11-26 (session 2)

Budget: about 25 minutes and about 30 web requests; 30 were made (21 fetches,
listed below, and 9 searches). The last fetch was refused by the server.

URLs fetched (all on 2026-11-26):

| URL | Result |
| --- | --- |
| `https://arxiv.org/pdf/2206.07561` | PDF (v1) downloaded; all 19 pages read |
| `https://arxiv.org/pdf/1507.02341` | PDF (v3) downloaded; all 11 pages read |
| `https://arxiv.org/pdf/2407.03309` | PDF (v1) downloaded; all 19 pages read |
| `https://arxiv.org/pdf/2103.00647` | PDF downloaded; pages 5–12 read only |
| `https://mathweb.ucsd.edu/~ronspubs/` | index read (first 100,000 characters) |
| `https://mathweb.ucsd.edu/~ronspubs/78_12_matrix_polynomials.pdf` | scan downloaded; pp. 60–67 and 80–86 read |
| `https://mathweb.ucsd.edu/~ronspubs/78_05_distance_matrix_polynomials.pdf` | 404 (guessed file name) |
| `https://doi.org/10.1016/0166-218X(89)90044-9` | redirect to `linkinghub.elsevier.com/retrieve/pii/0166218X89900449` |
| `https://linkinghub.elsevier.com/retrieve/pii/0166218X89900449` | page body "Redirecting" only |
| `https://www.sciencedirect.com/science/article/pii/0166218X89900449` | 403 |
| `https://api.elsevier.com/content/article/PII:0166218X89900449?httpAccept=text/plain` | 400 |
| `https://api.crossref.org/works/10.1016/0166-218X(89)90044-9` | metadata read (title, author, DAM 25(1–2), Oct 1989, 27–35; Elsevier open-access user licence dated 2013-07-17) |
| `https://doi.org/10.1016/0001-8708(78)90005-1` | redirect to `linkinghub.elsevier.com/retrieve/pii/0001870878900051` |
| `https://linkinghub.elsevier.com/retrieve/pii/0001870878900051` | page body "Redirecting" only |
| `https://api.semanticscholar.org/graph/v1/paper/arXiv:1507.02341/citations?…` | 5 citing papers listed |
| `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/0166-218X(89)90044-9/citations?…` | 14 citing papers listed |
| `https://api.core.ac.uk/v3/search/works?q=doi:…` | 403 |
| `https://core.ac.uk/search?q=…` | 403 |
| `https://core.ac.uk/download/10129286.pdf` (Collins's thesis, per a search result) | 403 |
| `https://dspace.mit.edu/handle/1721.1/77687` | record page read (title, author, 1986, advisor) |
| `https://dspace.mit.edu/bitstreams/ffd29595-5770-4d22-936c-16bab6d1daf5/download` | 429 (retry after 900 s) |

Citing papers returned by the citation index, seen by title only unless marked:
arXiv:2407.03309 (read); arXiv:2206.07561 (read); arXiv:2103.00647 (read in
part); arXiv:2104.14516 (Wagner, Constructions in combinatorics via neural
networks); arXiv:2306.07956 (Adaptive Monte Carlo search for conjecture
refutation in graph theory); arXiv:2207.03343 (Refutation of spectral graph
theory conjectures with Monte Carlo search); arXiv:1812.05734 (Graphs that are
cospectral for the distance Laplacian); arXiv:1304.0873 (On the two conjectures
of the Wiener index); Aouchiche–Hansen, Distance spectra of graphs: a survey;
"Factoring distance matrix polynomials", Discrete Math. 1993,
DOI `10.1016/0012-365X(93)90289-6`; "Spectral properties of distance matrix of
graphs" (2012); Merris-type surveys "Laplacian matrices of graphs" (1989, 1994).
The index is not complete (Crossref reports 9 citations of Collins's paper, the
index 14).

Search queries run (general web search tool):

1. `Collins "On a conjecture of Graham and Lovász about distance matrices" Discrete Applied Mathematics 1989 pdf`
2. `"distance characteristic polynomial" tree normalized coefficients peak location Collins Shor conjecture double star OR caterpillar OR "diameter" 2023 OR 2024 OR 2025 OR 2026`
3. `"On a conjecture of Graham and Lovász about distance matrices" Collins core.ac.uk OR sciencedirect open archive`
4. `"Graham" "Lovász" distance characteristic polynomial tree coefficients "peak" Collins Shor conjecture proof OR progress OR "double star" OR "bounded diameter" arXiv 2025`
5. `"distance characteristic polynomial" caterpillar "quotient matrix" OR "equitable partition" distance spectrum caterpillar tree pendant twins eigenvalue -2`
6. `Nascimento Del-Vecchio de Freitas "The distance matrix of caterpillar" distance eigenvalue -2 multiplicity characteristic polynomial`
7. `distance characteristic polynomial tree coefficients ratio consecutive coefficients extremal star path "normalized coefficients" comparison all trees maximized by path minimized by star`
8. `Karen L. Collins Wesleyan "distance matrices" "Graham and Lovász" conjecture 1989 pdf "coefficients" path star "Shor"`
9. `Karen Collins "Distance matrices of trees" thesis MIT 1986 dspace`

(Queries 2 and 4 were issued in the search tool's "extended" mode.)

Not accessed, and why it matters:

- **Collins (1989), full text.** ScienceDirect and the Elsevier API refused the
  tool. The exact wording of Conjecture 9 and of Theorems 1 and 3 is still
  known only through arXiv:1507.02341. Whether the paper treats any family
  besides stars and paths is known only from three secondary descriptions,
  which all mention stars and paths only.
- **Collins's 1986 MIT thesis** (61 leaves): record found, PDF refused (403 at
  CORE, 429 at DSpace). It may contain more than the paper.
- Graham–Lovász 1978, pp. 68–79 and 87–88 (including Table III).
- Edelberg–Garey–Graham 1976; Aouchiche–Hansen 2014; the journal versions of
  arXiv:1507.02341, 2206.07561 and 2407.03309; Nascimento–Del-Vecchio–de
  Freitas 2019; J. C.-H. Lin's Sage worksheet; arXiv:2104.14516, 2207.03343,
  2306.07956 (the claim that they concern a different conjecture of Collins
  remains unverified); the rest of arXiv:2103.00647.
- No search of MathSciNet, zbMATH, Google Scholar, MathOverflow, the arXiv
  listing interface, OEIS, or any formal-mathematics library was made in this
  session.

An unsuccessful search establishes nothing about novelty. In particular the
search for prior appearances of ratio comparisons with the star or the path
(MD-0004, MD-0005) consisted of one query (number 7). It returned only a
snippet stating a star-minimal / path-maximal ordering for coefficients of the
*Laplacian* characteristic polynomial of trees (attributed to Gutman and
Pavlović, at `emis.univie.ac.at/journals/BSANU/28/r2003_4.pdf`; not opened).

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

### Literature audit, 2026-11-26 (session 2): status of the items above

- *Bibliographic data of Graham–Lovász 1978 and Collins 1989*: now confirmed
  (the first from the title page of the scan, the second from the Crossref
  record of DOI `10.1016/0166-218X(89)90044-9`).
- *Journal version of arXiv:1507.02341*: given as Electron. J. Linear Algebra
  34:373–380, 2018 in the reference lists of arXiv:2206.07561 and
  arXiv:2407.03309. Still not checked against the journal itself.
- *Date of Collins's disproof*: the Hogben–Reinhart survey says "in 1985"; the
  thesis record is dated 1986 and the paper 1989. Unresolved, and immaterial to
  the statement.
- *Tie convention*: still not specified by any source read.
- *Wagner (arXiv:2104.14516)*: still unverified; the paper was not read.
- *Collins's Conjecture 9, Theorem 1, Theorem 3*: still second-hand.
- *Formalization*: no search of Mathlib, formal-conjectures or other libraries
  was made in this audit; the "Formalization feasibility" section remains
  unchecked.

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

## Literature audit 2026-11-26 (session 5)

Auditor: Claude (`claude-fable-5-2`), literature-auditor subagent. Budget set by
the director's session: 12 minutes and at most 14 web requests. Used: 12 web
requests (6 searches, 6 fetches; 2 of the fetches failed). Wall-clock time is
not reported by the environment; the work was stopped at an estimated 12
minutes, with the budget of requests not exhausted. All accesses on 2026-11-26.

**No prior proof or refutation of the Collins–Shor conjecture, and no prior
statement locating the peak of the normalized coefficients for double stars or
caterpillars, was found within the coverage below. Closed formulas for the
distance characteristic polynomials of double stars, of the trees K(a,0,c) and
of the balanced caterpillars K(t,t,t) were found in prior work** (first two
items under "Sources"). The project's results on these families must cite them
for the formulas. The coverage is small; see "Not searched or not accessible".

### Search queries (verbatim, general web search tool, standard mode)

1. `Nascimento Del-Vecchio de Freitas "The distance matrix of caterpillar"`
2. `"distance characteristic polynomial" coefficients peak "double star" OR caterpillar OR broom tree Graham Lovász Collins unimodal 2024 OR 2025 OR 2026`
3. `"The distance matrix of caterpillar" Discrete Applied Mathematics OR "Proceeding Series" OR arXiv distance eigenvalue -2 multiplicity caterpillar Nascimento`
4. `distance characteristic polynomial tree pendant twins "quotient matrix" OR "equitable partition" "number of pendant vertices" distance spectrum double star caterpillar closed formula`
5. `Collins "On a conjecture of Graham and Lovász about distance matrices" 1989 star path coefficients peak "Shor" theorem summary`
6. `distance matrix tree "pendant vertices" twins distance characteristic polynomial "multilinear" OR "multiaffine" OR "linear in" number of leaves quotient matrix "distance spectrum" caterpillar OR "double broom" OR "double star" formula`

### URLs fetched

| URL | Result |
| --- | --- |
| `https://pep.ufrj.br/index.php/en/academic-information/doutorado/2018/683--605/file` | 404 |
| `https://web1.pmf.ni.ac.rs/filomat-content/2016/30-6/30-6-16-1282.pdf` | PDF downloaded; all 7 pages read |
| `https://pantheon.ufrj.br/handle/11422/12254` | record page read (title, author, date, bitstream link) |
| `https://pantheon.ufrj.br/bitstreams/e3cd68d7-684c-4218-93af-e6cb1caae541/download` | PDF of the thesis downloaded; pages listed below read |
| `https://api.semanticscholar.org/graph/v1/paper/arXiv:1507.02341/citations?fields=title,year,externalIds,authors&limit=100` | 5 citing papers, the same 5 as in the session 2 audit |
| `https://api.semanticscholar.org/graph/v1/paper/arXiv:2407.03309/citations?fields=title,year,externalIds,authors&limit=100` | 429, nothing retrieved |

### Sources and what they contain

**(S1) J. Xue, R. Liu, H. Jia, On the distance spectrum of trees, Filomat 30:6
(2016) 1559–1565, DOI `10.2298/FIL1606559X`. Read in full (7 pages).**

- Definition (p. 1560): the double star S(a,b) is two stars K_{1,a} and K_{1,b}
  with an edge joining their centres, a, b ≥ 1, a + b = n − 2. This is the
  project's S(a,b).
- Lemma 2.3 (p. 1560, proof on p. 1561): with P_D(λ) = det(λI − D(G)),
  `P_D(λ) = (λ+2)^{n−4} [λ⁴ − (2a+2b−4)λ³ − (9a+9b+5ab−3)λ² − (12a+12b+4ab+4)λ − (4a+4b+4)]`.
  The proof writes D in four blocks (two centres, two classes of leaves) and
  reduces det(λI − D) to (λ+2)^{a+b−2} times a 4 × 4 determinant, which is the
  characteristic determinant of the quotient matrix of that partition (the
  paper does not use the words "quotient" or "equitable").
- Theorems 3.2 and 3.5: P_n and S(a,b) are determined by their distance
  spectra. On p. 1562 the balanced case is factored:
  `(λ+2)^{n'−4} [λ² + (c+3)λ + 2][λ² − (5c−1)λ − (4c+2)]` for S(c,c).
- The paper contains nothing on the sequence of coefficients, on normalized
  coefficients, on unimodality or a peak, and cites neither Graham–Lovász nor
  Collins (reference list, p. 1565, read).

**(S2) J. S. do Nascimento, Um estudo sobre a matriz distância de grafos
(A study about the distance matrix of graph), D.Sc. thesis, COPPE/UFRJ, April
2018; advisors M. A. A. de Freitas and R. R. Del-Vecchio; in Portuguese;
<https://pantheon.ufrj.br/handle/11422/12254>. Read in part: thesis pages
vi–ix (abstracts, contents, list of figures), 4–5, 12–15, 38–49, 78–79
(bibliography). Not read: pages 1–3, 6–11, 16–37, 50–77.**

- Definition 3.1.1 (p. 13): the caterpillar C(p), p = (p_1, …, p_{d−1}),
  p_1, p_{d−1} ≥ 1, p_i ≥ 0, is the path P_{d−1} with p_i pendant leaves at its
  i-th vertex; diameter d, order n = p_1 + … + p_{d−1} + d − 1. The "double
  broom" V(t,s,d) is the case p_1 = t, p_{d−1} = s, all other p_i = 0. So
  V(t,s,3) is the project's S(t,s), V(t,s,4) is the project's K(t,0,s), and
  C(a,b,c) is the project's K(a,b,c).
- Theorem 2.1.4 (p. 5, cited from Brouwer–Haemers): for an equitable partition
  of a square matrix, the non-zero eigenvalues of the quotient matrix belong to
  the spectrum of the matrix. This is the tool used throughout Section 3.2.
- Theorem 2.3.11 (p. 12), attributed to Collins, "Factoring distance matrix
  polynomials", Discrete Math. 122 (1993) 103–112: for a tree with n_1 leaves
  and n_1' quasi-pendant vertices, −2 is a distance eigenvalue of multiplicity
  at least n_1 − n_1'.
- Theorem 3.1.5 (p. 15): for V(t,s,d), d ≥ 3, the multiplicity of −2 is n − d
  if d ≡ 2 (mod 6) and n − d − 1 otherwise.
- Proposition 3.2.1 (pp. 39–40): for V(t,s,3), n = t + s + 2, the 4 × 4
  reduced matrix M is written out and its characteristic polynomial is
  `p(λ) = λ⁴ − 2(n−4)λ³ − (5ts+9n−21)λ² − (4ts+12n−20)λ − 4n + 4`;
  the statement of the proposition itself is a list of intervals for the
  eigenvalues. This agrees with Lemma 2.3 of (S1) after a + b = n − 2. The
  thesis does not cite (S1) (bibliography read).
- Corollary 3.2.2 and the text around it (pp. 40–41): the thesis says that
  Collins (the 1993 paper) stated a factorization of the distance
  characteristic polynomial of V(t,t,3), namely
  `(λ+2)^{n−4}(λ+1)(λ+t)(λ² − (5t−1)λ − 9t)`, says that it is wrong (example
  V(3,3,3)), and replaces it by Proposition 3.2.3:
  `(λ+2)^{n−4}(λ² + (t+3)λ + 2)(λ² − (5t−1)λ − 4t − 2)`, n = 2t + 2 (the same
  factorization as on p. 1562 of (S1)). Whether Collins's paper says what the
  thesis reports was not checked: Collins (1993) was not accessed.
- Proposition 3.2.6 (pp. 44–45): for V(t,s,4), n = t + s + 3, the distance
  eigenvalues other than −2 are the roots of
  `p(λ) = λ⁵ − (2n−10)λ⁴ − (12ts+18n−52)λ³ − (24ts+44n−104)λ² − (8ts+36n−68)λ − 8n + 8`,
  the characteristic polynomial of an explicit 5 × 5 reduced matrix D*; −2 has
  multiplicity n − 5.
- Proposition 3.2.7 (pp. 45–46): for V(t,t,4), t > 1, the reduced polynomial
  factors as `(λ² + (2t+4)λ + 4)(λ³ − 6tλ² − (12t+6)λ − 4t − 4)`.
- Proposition 3.2.9 (pp. 47–49): for C(t,t,t), t ≥ 1, the 6 × 6 reduced matrix
  is written out and its characteristic polynomial is
  `(λ² + (2t+4)λ + 4) · q_2(λ)`,
  `q_2(λ) = λ⁴ − (8t−2)λ³ − (6t²+33t+6)λ² − (6t²+40t+16)λ − 12t − 8`; −2 has
  multiplicity 3t − 3.
- Section 3.2 treats, for diameter 4, only V(t,s,4) and C(t,t,t) (stated on
  p. 39). No formula for C(a,b,c) with three independent parameters appears on
  the pages read.
- On the pages read there is no statement about the sequence of coefficients,
  normalized coefficients, unimodality or a peak. Graham–Lovász 1978 is item
  [2] of the bibliography; Collins (1989) and arXiv:1507.02341 are not in the
  bibliography (pp. 78–79 read; the Aalipour et al. item listed is "On the
  distance spectra of graphs", Linear Algebra Appl. 497 (2016)). The stated aim
  (abstract, p. vii) is the multiplicity of distance eigenvalues and the number
  of distinct distance eigenvalues. Since pages 16–37 were not read, this is
  not a statement about the whole thesis.

**(S3) J. S. do Nascimento, R. R. Del-Vecchio, M. A. A. de Freitas, The
distance matrix of caterpillar, Discrete Appl. Math. 266 (2019) 141–152. Not
read.** Bibliographic data and a one-sentence description (multiplicity of −2
and number of distinct distance eigenvalues of caterpillars) come from a
library-catalogue record shown in a search result
(`katalog.lib.cas.cz/KNAV/EdsRecord/edsair,…`, not opened). No arXiv or
proceedings version was found by queries 1 and 3. The first author's initials
are J. S., not C. M. That the paper corresponds to Chapter 3 of (S2) is an
inference from the common title subject, author and advisors; it was not
verified.

**(S4) Collins (1989).** Not accessed (query 5 returned only the secondary
sources already recorded in the session 2 audit). No new information.

**(S5) Citation index.** Semantic Scholar still lists 5 papers citing
arXiv:1507.02341, the same as in session 2. The list for arXiv:2407.03309 could
not be retrieved (429).

**Search-result snippets, not opened:** R. Merris, The distance spectrum of a
tree (J. Graph Theory 14 (1990) 365–369; a scan is at
`math.ucdavis.edu/~saito/data/distmat/merris-distspect-tree.pdf`): multiplicity
of a distance eigenvalue of a tree is at most the number of pendant vertices.
"On the spectra of reduced distance matrix of the generalized Bethe trees"
(Iranian J. Math. Chem.), arXiv:2112.10375 (graphs with three distinct distance
eigenvalues), arXiv:1907.02851 (graft transformations, distance (signless)
Laplacian). None was read.

### Auditor's consistency checks (by hand, not machine-verified)

- The quartics of (S1) Lemma 2.3 and (S2) Proposition 3.2.1 coincide. At
  a = b = 1 both give λ⁴ − 20λ² − 32λ − 12, whose constant term and λ²
  coefficient agree with det D(P_4) = −12 and Σ_{i<j} d_{ij}² = 20.
- (S2) Proposition 3.2.6 at t = s = 1 gives λ⁵ − 50λ³ − 140λ² − 120λ − 32;
  the constant term and the λ³ coefficient agree with det D(P_5) = 32 and
  Σ_{i<j} d_{ij}² = 50. The other coefficients were not checked.
- In the quartic of (S1) the coefficient of ab is −5λ² − 4λ. With λ = 2x,
  negated and divided by 4^{s−1} = 4, this is 5x² + 2x = (s+3)x^s + s x^{s−1}
  for s = 2. In (S2) Proposition 3.2.9 the coefficient of t³ in the product is
  −12λ³ − 12λ²; with λ = 2x, negated and divided by 16, this is 6x³ + 3x², the
  value of (s+3)x^s + s x^{s−1} for s = 3. So the published formulas are
  consistent with the project's identity for s = 2 and, on the diagonal
  a = b = c, for s = 3. Neither source states the identity, isolates that
  coefficient, or treats general s.
- The published reduced polynomials have coefficients of degree at most 1 in
  each of the two leaf counts ((S1) Lemma 2.3; (S2) Propositions 3.2.1 and
  3.2.6). Neither source remarks on this or states it as a general property.

### Per-statement conclusions (within this coverage only)

| Project statement | Conclusion |
| --- | --- |
| MD-0006 (T1): peak of every double star at ⌊n/2⌋, unique | **Closely related prior work identified.** The distance characteristic polynomial of S(a,b) is in Xue–Liu–Jia 2016, Lemma 2.3, and in Nascimento 2018, Proposition 3.2.1; per the thesis, Collins (1993) also treats the balanced double star (not verified). None of the sources read states anything about the coefficients' maximum. The closed formula is prior art and must be cited; a prior statement of the peak was not found. |
| MD-0007 (T2): peak of K(a,b,c), a, b, c ≥ 1, at ⌊n/2⌋, unique | **Closely related prior work identified.** Nascimento 2018, Proposition 3.2.9, gives the reduced matrix and the factored polynomial for the balanced case C(t,t,t) only. No formula for three independent parameters and no peak statement was found. |
| MD-0008 (T3): peak of K(a,0,c) at ⌊n/2⌋, unique | **Closely related prior work identified.** Nascimento 2018, Proposition 3.2.6, gives the reduced 5 × 5 matrix and the quintic for V(t,s,4) = K(t,0,s) for all t, s. No peak statement was found. |
| MD-0009 (Hypothesis V, a conjecture of the project) | **Nothing found within this coverage.** |
| Framework: normalized coefficients as binomial coefficients times a polynomial of degree ≤ 1 in each c_v | **Closely related prior work identified** for the method only: reduction of the distance matrix of a tree with pendant twins to the quotient matrix of the twin partition ((S1) proof of Lemma 2.3; (S2) Theorem 2.1.4 and Section 3.2; Hogben–Reinhart, already recorded). The general multi-affine statement and the binomial form of the normalized coefficients: nothing found within this coverage. |
| Framework: reduction of the lower bound to trees with all extra leaves at one vertex | **Nothing found within this coverage.** |
| Framework: coefficient of ∏ c_v in −det(2xI − Q)/4^{s−1} equals (s+3)x^s + s x^{s−1} | **Nothing found within this coverage.** The cases s = 2 and (diagonal) s = 3 can be read off the published formulas, as checked by hand above; the identity is not stated in the sources read. |

None of these conclusions establishes novelty. "Nothing found" means nothing
in six web queries and the pages listed.

### Not searched or not accessible

- **Nascimento–Del-Vecchio–de Freitas, Discrete Appl. Math. 266 (2019)
  141–152**: not read (no open copy located; ScienceDirect was not tried again
  after the refusals of session 2). It may contain results that the thesis does
  not, including formulas for more general caterpillars.
- **Thesis (S2), pages 1–3, 6–11, 16–37, 50–77**: not read. Pages 16–37 contain
  the general results on caterpillars (Theorems 3.1.11 and 3.1.16 on the
  multiplicity of −2 and the number of distinct eigenvalues are cited on
  pp. 44 and 48 but were not read).
- **Collins, Factoring distance matrix polynomials, Discrete Math. 122 (1993)
  103–112** (DOI `10.1016/0012-365X(93)90289-6` per the session 2 list): not
  accessed. According to (S2) it treats double stars and the eigenvalue −2. It
  is by the author of the conjecture and is the most likely place, among the
  items now known, for a prior statement about coefficients of double stars.
  **This is the main open item of the audit.**
- **Collins (1989)** and **Collins's 1986 thesis**: still not accessed.
- Papers citing arXiv:2206.07561, arXiv:2407.03309, Collins (1989), Collins
  (1993), Xue–Liu–Jia (2016) or the DAM 2019 paper: not listed (one request
  failed with 429; the others were not made).
- Journal versions of arXiv:2407.03309 and arXiv:2206.07561; Merris (1990);
  Edelberg–Garey–Graham (1976); Aouchiche–Hansen (2014): not read.
- MathSciNet, zbMATH, Google Scholar, MathOverflow, the arXiv listing
  interface, OEIS, erdosproblems.com: not searched.
- Mathlib, formal-conjectures and other formal libraries: not searched;
  the formalization question (item 5 of the auditor's task) was not addressed
  in this session.
- Non-English literature other than the one Portuguese thesis; literature on
  the distance Laplacian or distance signless Laplacian of caterpillars;
  literature on "trees with many pendant vertices" as a named family: no
  dedicated query.

## Literature audit 2026-11-26 (session 6)

Two readers: the session's main context for Collins (model
`claude-fable-5-2`), and a separate literature-auditor context (same model)
for the thesis and the 2019 paper. Nothing below establishes novelty.

### Collins, "Factoring distance matrix polynomials" — read in full, in the author's manuscript

- **What was read.** A PDF supplied by the director from outside the
  repository (not copied into it, not committed): 9 pages, typeset
  manuscript, title "Factoring Distance Matrix Polynomials", author Karen L.
  Collins, Dept. of Mathematics, Wesleyan University; abstract, Theorems 1 to
  3, Corollaries 4 to 7, Theorem 8, Lemma 9, Remarks 10 to 12, an open
  question attributed to L. Butler, 15 references. All nine pages were read as
  page images.
- **Identification.** Title, author and subject agree with K. L. Collins,
  Discrete Math. 122 (1993) 103–112. The file carries no journal header, page
  numbers 1 to 9 (not 103 to 112), and cites Merris's paper on the distance
  spectrum of a tree as a preprint: it is the author's manuscript, not the
  published version. Whether the two texts agree was not checked, and the
  published version has not been seen.
- **Content.** (i) Theorem 1: if `AW ⊆ W` and `B` is the matrix of `A` on a
  basis of `W`, then `det(B − λI)` divides `det(A − λI)`. Theorem 2: the
  vertex orbits of a graph give a factor of the distance characteristic
  polynomial `CPD(G) = det(D(G) − λI)` ("the orbit factor") — the quotient
  matrix of the orbit partition. (ii) Theorem 3: a vertex-centred automorphism
  gives a further factor. (iii) "Corollary 4. Let T be a tree, and z a vertex
  with k ≥ 2 leaf neighbors. Then −2 is an eigenvalue of CPD(T) at least k − 1
  times." "Corollary 7. Let T be a tree, p be the number of leaves of T, and q
  be the number of vertices that are adjacent to a leaf. Then −2 occurs as an
  eigenvalue of D(T) at least p − q times." (described as a minor improvement
  of a theorem of Merris). (iv) "Corollary 5. Let S_n be the star with n + 1
  vertices. Then CPD(S_n) = (−1)^{n+1}(λ² − 2(n−1)λ − n)(λ + 2)^{n−1}."
  (v) "Corollary 6. Let 2S_n be the tree with 2(n + 1) vertices in which there
  are two vertices of degree n + 1 and 2n vertices of degree 1. Then
  CPD(2S_n) = (−1)^{2(n+1)}(λ + 2)^{2(n−1)}(λ + n)(λ + 1)(λ² − (5n − 1)λ − 9n)."
  (vi) Theorem 8 and the pages after it: the factorization of `CPD` of the
  full `k`-ary tree `F_{r,k}` through linear recurrences; Remark 12, the
  analogue for the adjacency matrix.
- **Corollary 6 as printed in the manuscript does not agree with direct
  computation.** `2S_n` is the balanced double star `S(n, n)`. The product
  printed has the sum of its roots equal to `−2` for every `n`, whereas the
  trace of a distance matrix is 0; for `n = 1` (the path `P_4`) it reads
  `(λ + 1)²(λ² − 4λ − 9)`, and `det(D(P_4) − λI) = λ⁴ − 20λ² − 32λ − 12`.
  Exact computation for `n = 1, …, 6`
  (`experiments/CJ-0001-collins-shor-peak/locality_check.py`, result file
  `results/locality-check.json`): the printed formula fails in all six cases,
  and `det(D − λI) = (λ + 2)^{2(n−1)} (λ² + (n + 3)λ + 2)(λ² − (5n − 1)λ − 4n − 2)`
  holds in all six. The reading of the printed formula was made from a page
  image by one reader; the published version may differ. The project's Lemma
  D1 (double stars) is not affected, and it agrees with Xue–Liu–Jia 2016,
  Lemma 2.3, as recorded in session 5.
- **What it does not contain.** No statement about the coefficients of the
  distance characteristic polynomial, their normalization, unimodality or the
  location of their maximum, for any family; no general double star (only the
  balanced one); no caterpillar; no expansion in the numbers of pendant
  leaves; no determinant of the form `det(P + αJ)`.
- **Bearing on the project.** Corollary 7 is the published source of the
  factor `(λ + 2)^{p−q}` used in Lemma L3 and Lemma S1 (there with its exact
  cofactor, the quotient determinant); Theorems 1 and 2 are the divisor
  principle for an invariant subspace. Both are to be cited where L3 and S1
  are stated. The description "treats double stars" of the session 5 audit
  (taken from the thesis) is to be read as "the balanced double star, with a
  formula that does not check as printed in the manuscript".

### do Nascimento, thesis (COPPE/UFRJ, 2018) — thesis pages 14 to 38 read

Route: `https://pantheon.ufrj.br/bitstreams/e3cd68d7-684c-4218-93af-e6cb1caae541/download`
(the fetch tool saved the PDF outside the repository; read as page images;
PDF page = thesis page + 10). Statements, definitions, examples and
connecting text read on every page from 14 to 38; proofs read in full for
Lemma 3.1.4, Theorem 3.1.5, Corollary 3.1.7, Theorem 3.1.11, Lemma 3.1.15,
Corollary 3.1.17, Theorems 3.1.19 and 3.1.23; the proofs of Theorems 3.1.9,
3.1.16 and 3.1.18 skimmed. With session 5, pages 12 to 49 are now covered;
pages 1–3, 6–11 and 50–77 remain unread.

- Section 3.1 is about the multiplicity of `−2` and the number of distinct
  distance eigenvalues: Theorem 3.1.5 (double brooms `V(t,s,d)`:
  `m_D(−2) = n − d` if `d ≡ 2 mod 6`, `n − d − 1` otherwise); Theorem 3.1.9
  and Theorem 3.1.11 (caterpillars `C(p)` with an inner pendant vertex:
  `m_D(−2) = n − d − n_1' + 1`, `n_1'` the number of quasi-pendant vertices);
  Theorems 3.1.16 and 3.1.18 (the eigenvalues other than `−2` are simple);
  Corollary 3.1.17 and Theorem 3.1.19 (number of distinct eigenvalues);
  Conjecture 3.1.22 (a lower bound on that number for trees). On p. 15 the
  bound `m_D(−2) ≥ n_1 − n_1'` is attributed to Collins.
- **No statement on these pages** about the coefficients of the distance
  characteristic polynomial, their maximum, or unimodality; the polynomial is
  not written down in Section 3.1. No expansion over subsets of spine
  vertices, no multi-affine statement in the leaf numbers, no `det(P + αJ)`.
- Nearest material: the block form of `D` for a caterpillar and the reduction
  of twin rows of `D + 2I` (pp. 16, 26–27; a rank statement at `λ = −2`);
  Lemma 3.1.15 (p. 28: an eigenvector for an eigenvalue other than `−2` is
  constant on pendant twins); the inverse `D^{−1}` of `C(p)` from the
  Graham–Lovász formula (p. 33).
- Defects noticed by the auditor in the thesis, not checked by computation:
  the base case of the induction of Theorem 3.1.9 quotes a floating-point
  spectrum of `C(1,1,1)` from software; a misprint of the multiplicity in the
  proof of Theorem 3.1.19.
- The quotations were transcribed from page images in Portuguese by the
  auditor and are in the session's journal entry.

### do Nascimento, de Freitas, Del-Vecchio, Discrete Appl. Math. 266 (2019) 141–152 — not read

Full text not accessed; the abstract was not read verbatim. Bibliographic
record from Crossref: DOI `10.1016/j.dam.2018.10.018`, 11 references (as
summarised by the fetch tool: Aalipour et al. 2016, Atik 2016, Brouwer 2011,
Collins 1993, Graham 1978, Graham–Pollak 1971, Merris 1990, Rojo 2010, Ruzieh
1990, Zhou 2011, and a Sage code). Failures: `sciencedirect.com` article and
PDF pages, HTTP 403; `core.ac.uk` search, HTTP 403; a library catalogue,
bot protection; Semantic Scholar search, HTTP 429. No preprint was located by
two web queries. OpenAlex reports the article as "bronze" open access, so a
person can probably open the publisher page in a browser. A paraphrase of the
abstract (Semantic Scholar, through the fetch tool) says the paper concerns
the multiplicity of `−2` and the number of distinct distance eigenvalues of
caterpillars, which is the subject of Section 3.1 of the thesis; that the
paper corresponds to that section remains an inference.

Queries of this session (general web search, standard mode):
`"The distance matrix of caterpillar" Nascimento Del-Vecchio Freitas Discrete Applied Mathematics 2019`;
`"distance matrix of caterpillar" Nascimento Del-Vecchio Freitas pdf OR researchgate OR semanticscholar "D-eigenvalue" caterpillar -2 multiplicity`.

### Per-statement conclusions after session 6 (within the coverage of sessions 2, 5 and 6 only)

| Project statement | Conclusion |
| --- | --- |
| MD-0006, MD-0007, MD-0008 (peak at ⌊n/2⌋ for double stars and caterpillars of diameter 4) | No peak statement in Collins's manuscript nor on thesis pages 12–49. The closed formulas remain prior art (session 5). Not read: the DAM 2019 paper, Collins 1989, the published version of Collins 1993. |
| Expansion over subsets (S2) and the multi-affine closed form (S1) | Not found. The factor `(λ + 2)^{p−q}` and the divisor principle are in Collins's manuscript (Corollary 7, Theorems 1 and 2). |
| `r_V = (s + 3)x + s` (S3) | Not found. |
| Lemma L3 / MD-0003 (already recorded as known) | Further prior art: Collins, Corollary 7; thesis, Theorems 3.1.5 and 3.1.11. |

### Still not searched or not accessible after session 6

The DAM 2019 paper; the published version of Collins 1993; Collins 1989 and
her 1986 thesis; thesis pages 1–3, 6–11, 50–77; Graham–Lovász pp. 68–79;
papers citing any of these; MathSciNet, zbMATH, Google Scholar, MathOverflow.
For the statements written in session 6 (the reduction of `r_A` to a Laplacian
block, Property Γ for independent complements) no search was made at all.

## Literature audit 2026-11-26 (session 7): MD-0011 and MD-0012

Auditor: Claude (`claude-fable-5-2`), literature-auditor subagent. Budget set
by the launching session: 20 minutes of wall-clock time (the environment does
not report elapsed time; the work was stopped at an estimated 18 minutes).
Requests made: 14 web searches, 15 fetches (3 of them returned only undecoded
PDF bytes, which were then read as page images; 1 returned an empty list). All
accesses on 2026-11-26. This is the first search made for the statements of
MD-0011 (Propositions S6 to S10, Lemma C) and MD-0012 (Lemma F, Corollary F′,
Proposition S11).

**Result in one sentence.** No source read states S6, S7, S8, S9, S10, Lemma C,
Lemma F, Corollary F′ or S11, and no proof or refutation of the Collins–Shor
conjecture was found; three published results that are close to parts of the
argument were identified and must be cited (items R1 to R3 below), one of which
(R2, Theorem 2.4) is the determinant `det(D + xJ)` that an earlier audit
recorded as "not found" for Proposition S3. The coverage is small and does not
support any statement of novelty.

### Queries (verbatim)

General web search tool (S = standard mode, E = extended mode):

1. (S) `distance characteristic polynomial tree pendant vertices Laplacian principal submatrix formula "distance matrix" "Graham" "Lovász" inverse low-rank update determinant`
2. (S) `"det(I + x L)" OR "det(I+xL)" OR "det(I + tL)" rooted spanning forests tree Laplacian principal submatrix polynomial "gamma-positive" OR "real-rooted" OR "interlacing"`
3. (E) `"distance characteristic polynomial" trees coefficients peak location Collins Shor conjecture arXiv 2025 OR 2026 unimodal "normalized coefficients"`
4. (S) `polynomial nonnegative expansion basis "x^i(1+x)^{d-2i}" beyond symmetric "gamma-positivity" non-palindromic "alternatingly increasing" "symmetric decomposition" Brändén Solus`
5. (S) `distance spectrum "corona" OR "thorn" tree "T∘K_1" OR "pendant vertices attached" distance characteristic polynomial in terms of Laplacian spectrum of the tree`
6. (S) `Chebotarev Shamis "matrix-forest theorem" det(I + τL) forests polynomial coefficients tree weighted roots "Dirichlet" OR "grounded" Laplacian tree characteristic polynomial coefficients combinatorial "gamma" positivity`
7. (S) `Laplacian characteristic polynomial of a tree "pendant vertex" recurrence "principal submatrix" deletion leaf recursion "L_v(T)" characteristic polynomial coefficients forests "Kelmans" tree`
8. (E) `arXiv 2025 distance matrix tree characteristic polynomial coefficients "Graham" "Lovász" peak "caterpillar" OR "double star" OR "starlike" OR "broom" unimodal location of the peak`
9. (E) `"rooted spanning forests" tree polynomial "principal submatrix" Laplacian tree "det(I + x" OR "det(xI + L" weights vertices "non-negative" expansion "(1+x)" basis forests tree gamma-vector`
10. (S) `Indulal Stevanović "distance spectrum of corona and cluster of two graphs" tree pendant vertices distance characteristic polynomial corona G∘K_1 Laplacian`
11. (S) `"Laplacian coefficients" trees matchings "subdivision" Zhou Gutman Mohar "principal submatrix" of Laplacian of a tree characteristic polynomial "matching polynomial" rooted forests`
12. (S) `tree "distance matrix" contracting subtree OR "contraction" pendant vertices "quotient matrix" determinant identity "Laplacian" principal submatrix "matrix determinant lemma" Graham Lovász inverse perturbation "rank one" bordered distance matrix tree`
13. (S) `mathoverflow polynomial "nonnegative combination" "x^i(1+x)^j" cone closed under multiplication peak binomial "gamma-nonnegative" non-symmetric generalization "left-heavy" OR "right-heavy" OR "top-heavy" gamma expansion`
14. (S) `"grounded Laplacian" OR "Dirichlet Laplacian" tree characteristic polynomial coefficients "gamma-positive" OR "γ-positive" OR "unimodal" det(I + x L) principal submatrix tree Laplacian "rooted forests" polynomial inequality coefficients`

The search tool reported for several of these that it had dropped operators or
quoted phrases; its answers are summaries and were used only to locate sources.

arXiv listing search (`arxiv.org/search`, all fields, newest first, 50 per page):

15. `"distance characteristic polynomial"` — 5 results: arXiv:2206.07561,
    1903.04575, 1811.03061, 1507.02341, 1505.07651. None later than 2022.
16. `"Graham and Lovász" distance` — 8 results: arXiv:2604.26385 (On a
    conjecture of distance spectral extremal problems, 29 Apr 2026),
    2604.12404 (Steklov eigenvalues on trees, 14 Apr 2026), 2504.11706
    (distance ideals, 15 Apr 2025), 2411.11488, 2206.07561, 2205.02133,
    1507.02341, 1303.4517. Titles and listing abstracts only, except
    2411.11488 (item R1). As reported by the fetch tool, none of the listing
    abstracts concerns the location of the peak for trees. arXiv:2407.03309 is
    not returned by either query, so these two queries do not find every
    relevant paper.

Citation index (Semantic Scholar API):

17. Citations of arXiv:1507.02341 — the same 5 papers as in sessions 2 and 5.
18. Citations of arXiv:2206.07561 — 8 papers; the only ones on distance
    matrices are arXiv:2407.03309 (already read) and arXiv:2309.08691
    (Choudhury–Khare, "The additive-multiplicative distance matrix of a graph,
    and a novel third invariant", title only).
19. Citations of arXiv:2407.03309 — the API returned an empty list.

### Sources opened, and what was read

**(R1) H. Richman, F. Shokrieh, C. Wu, Principal minors of tree distance
matrices, arXiv:2411.11488 (v1 18 Nov 2024, v2 10 Dec 2025; no journal
reference on the abstract page).** Access: abstract page, and the HTML
rendering of v2 through the fetch tool's text extraction (characters 0 to
100,000 of 108,982 in two passes, and 60,000 to the end in a third). The
statements below are as returned by that tool when asked for exact quotation;
they were **not** read as page images, and the proofs were not read.

- Theorem A: for a tree `G` with `n` vertices and a non-empty `S ⊆ V`,
  `det D[S] = (−1)^{|S|−1} 2^{|S|−2} ( (n−1) κ(G;S) − Σ_{F ∈ F_2(G;S)} (outdeg(F,∗) − 2)² )`,
  with `κ(G;S)` the number of `S`-rooted spanning forests and `F_2(G;S)` the
  set of `(S,∗)`-rooted spanning forests (one extra "floating" component).
- Theorem 2.4 (all-minors matrix-tree theorem): `κ(G;S)` is, up to the edge
  weights, `det L[S̄]`, the principal minor of the Laplacian on the complement.
- Theorem 4.4: `cof D[S] = (−2)^{|S|−1} κ(G;S)` (`cof` = sum of all cofactors).
- Theorem B: the version with edge lengths. Theorem C: a formula for the
  coefficients `δ_{n−k}` of `det(D − λI)` as sums over spanning forests with
  `k` and `k + 1` components. Theorem D: monotonicity of `det D[A]/cof D[A]`.
- Per the tool's listing of all numbered statements: nothing on pendant
  vertices as a family, on a quotient matrix, on `det(D[S] + ·)` with a
  rank-two term, on unimodality, real-rootedness, gamma-positivity or the
  location of the peak. The Graham–Lovász inverse is not a numbered statement.

**(R2) R. Bapat, S. J. Kirkland, M. Neumann, On distance matrices and
Laplacians, Linear Algebra Appl. 401 (2005) 193–209, DOI
`10.1016/j.laa.2004.05.011` (DOI as printed on the first page).** Access: scan
at `https://www.math.ucdavis.edu/~saito/data/distmat/bapat-kirkland-neumann-distmat-lap.pdf`;
all 17 pages read as page images (statements read; proofs of Sections 3 and 5
skimmed).

- Theorem 2.1 (p. 195): for a weighted tree with edge weights `α_i`,
  `D^{−1} = −L/2 + δδᵀ/(2 Σ α_i)`, `δ_i = 2 − d_i`, `L` the Laplacian for the
  reciprocal weights. This is the weighted form of the Graham–Lovász inverse
  used in S3 and S6.
- Theorem 2.3 (p. 197) and **Theorem 2.4 (p. 199)**: for a weighted tree on
  `n` vertices and every real `x`,
  `det(D + xJ) = (−1)^{n−1} 2^{n−2} (Π α_i)(2x + Σ α_i)`; inertia `(1, 0, n−1)`.
  For unit weights this is `det(D + xJ) = (−1)^{n−1} 2^{n−2} (2x + n − 1)`,
  which is the determinant computed in the proof of Proposition S3
  (`det(P + αJ) = (−1)^{s−1} 2^{s−2} (s − 1 + 2α)`).
- Lemma 4.1 (p. 203): `LD = δ1ᵀ − 2I`, `QᵀDQ = −2I`,
  `(D^{−1} − L)^{−1} = D/3 + (Σ α_i / 3) J`. Theorems 4.5 and 4.6: entrywise
  positivity of `(D^{−1} − L̃)^{−1}` for the Laplacian `L̃` of any connected
  weighted graph.
- The paper contains no characteristic polynomial of `D`, no principal
  submatrix of `L`, no pendant-vertex family, no quotient matrix, and no
  polynomial positivity statement.

**(R3) R. Merris, The distance spectrum of a tree, J. Graph Theory 14 (1990)
365–369.** Access: scan at
`https://math.ucdavis.edu/~saito/data/distmat/merris-distspect-tree.pdf`; all
5 pages read as page images. Content: Lemma `QᵀDQ = −2I_m` (`Q` the
vertex–edge incidence matrix; attributed to Graham–Lovász, Graham–Pollak and
W. Watkins); Theorem: the eigenvalues of `−2K^{−1}`, `K = QᵀQ = 2I + A(T*)`,
interlace those of `D`; "the characteristic polynomial of `DL(T)` is
`x(x + 2)^{n−1}`"; Corollary 1 (multiplicity of a distance eigenvalue at most
the number `p` of pendant vertices); Corollary 2 (`−2` has multiplicity at
least `p − q − 1`); Corollaries 3 and 4 (bounds from the algebraic
connectivity; "`I_p` is a principal submatrix of `L(T)`" is used for
interlacing). No formula for `det(D − λI)` through `L` or a block of `L`, no
statement on coefficients.

**(R4) P. Brändén, L. Solus, Symmetric decompositions and real-rootedness,
arXiv:1808.04141v3 (12 Jan 2020).** Access: PDF, pages 1 to 4 read as page
images; the rest not read. Definitions (p. 1): `p = p_0 + … + p_d x^d` is
*alternatingly increasing* if `0 ≤ p_0 ≤ p_d ≤ p_1 ≤ p_{d−1} ≤ … ≤ p_{⌊(d+1)/2⌋}`;
every `p` of degree at most `d` is uniquely `p = a + xb` with `a` symmetric
with respect to `d` and `b` with respect to `d − 1` (Lemma 2.1, p. 2, with
`a = (p − x I_d(p))/(1 − x)`, `b = (I_d(p) − p)/(1 − x)`); `p` is
alternatingly increasing if and only if `a` and `b` are unimodal with
non-negative coefficients. On the pages read there is no basis consisting of
`x^e(1+x)^{d−2e}` (`2e < d`) together with the monomials `x^e`
(`d ≤ 2e ≤ 2d`), and no cone of the form `C_d`.

**Abstract pages only (nothing claimed about the papers' contents):**
arXiv:1903.11566 (P. N. Choudhury, A. Khare, Distance matrices of a tree: two
more invariants, and in a unified framework; Eur. J. Combin. 115 (2024)
103787 per the abstract page): minors of generalized tree distance matrices
after deleting pendant nodes, a closed form for `D^{−1}` extending
Graham–Lovász, and `cof(D)`. arXiv:1711.05983 (C. A. Athanasiadis,
Gamma-positivity in combinatorics and geometry): the abstract describes
gamma-positivity as a property of polynomials with symmetric coefficients.

**Search-result snippets only, not opened:** Chebotarev–Shamis, Matrix-forest
theorems (arXiv:math/0602575); O. Knill, Counting rooted forests in a network
(arXiv:1307.3810: `det(1 + kL)` counts rooted edge-`k`-coloured spanning
forests); F. R. K. Chung, a combinatorial Laplacian with vertex weights
(Dirichlet eigenvalues and rooted forests); O. Bernardi and coauthor, Directed
rooted forests in higher dimension (arXiv:1512.07757); P. Biane and coauthor,
Laplacian matrices and spanning trees of tree graphs (arXiv:1505.04806);
B. Mohar, On the Laplacian coefficients of acyclic graphs (LAA 422, 2007);
the Zhou–Gutman identity `c_k(T) = m_k(S(T))` (Laplacian coefficients of a
forest are the matching numbers of its subdivision), seen only as quoted in
other papers' snippets; arXiv:2410.14112 (Subdivision method in the Laplacian
matching polynomial); arXiv:1104.4280, 1105.5838 (ordering trees by Laplacian
coefficients); arXiv:1306.4649 (Laplacian characteristic polynomials of
caterpillars by recursive formulas); arXiv:1912.03101; arXiv:2102.00899 and
arXiv:2302.00754 (bi-gamma-positivity: `a` and `b` of the symmetric
decomposition both gamma-positive — definition taken from the search tool's
summary); G. Indulal, D. Stevanović, The distance spectrum of corona and
cluster of two graphs, AKCE Int. J. Graphs Comb. 12 (2015) 186–192 (per the
catalogue snippet it assumes `G` distance regular); arXiv:1810.06182 (squared
distance matrix of a weighted tree); the Springer page of the journal version
of arXiv:2407.03309.

### Findings per item

**(a) `r_A` through the Laplacian block `L_B` (S6, S7; S8, S9, S10 as
consequences).** *Identical statement: not found within this coverage.*
Related prior results, to be cited:

- The two ingredients are published: the inverse formula (Graham–Lovász 1978,
  Lemma 1, recorded in session 2; weighted form in R2, Theorem 2.1) and the
  rank-one case `det(D + xJ)` (R2, Theorem 2.4).
- R1 is the nearest structural analogue. Its Theorem A writes a principal
  minor of `D` as "(a linear factor) × (a principal minor of `L` on the
  complement) − (a quadratic correction summed over forests with a floating
  component)", and its Theorem 4.4 gives `cof D[S]`, hence
  `det(D[S] + cJ) = det D[S] + c · cof D[S]` for every `c`. The second form of
  S7, `Φ_B · [linear] − x² zᵀ adj(I + xL_B) z`, has the same shape. The
  difference: the coefficient of `(2x)^{|C|}` in `det N_A`, `C ⊆ B`, is the
  principal minor on `V ∖ C` of `−(P + 1_A 1ᵀ + 1 1_Aᵀ + (a/2x) J)`, which
  contains the rank-two term `1_A 1ᵀ + 1 1_Aᵀ`; for `A = V` it is absorbed in
  `J` and S3 follows from R2 Theorem 2.4 (or R1 Theorems A and 4.4 with
  `S = V`), but for `A ≠ V` it is not covered by `det D[S]` and `cof D[S]`
  alone. (This comparison is the auditor's own and has not been reviewed.)
  Relation: **related technique and a parallel result for a different
  matrix; neither a special case nor a generalization was established.**
- No formula for the distance characteristic polynomial of a tree with
  pendant vertices, or of a corona/thorn/cluster construction on a tree, in
  terms of the Laplacian of the skeleton was found (queries 1, 5, 10, 12).
  The one corona paper located (Indulal–Stevanović) was not opened.
- Correction to the session 6 table: the row "`r_V = (s + 3)x + s` (S3): Not
  found" should now read "the determinant `det(P + αJ)` on which S3 rests is
  R2, Theorem 2.4; the statement `r_V = (s+3)x + s` itself was not found".

**(b) Lemma F (`det(I + x(L_T + diag ν)) ∈ C_j`), Corollary F′, and the leaf
recurrence.** *Not found within this coverage.* What was located concerns the
combinatorial meaning of the polynomial, not its position in a cone: the
matrix-forest theorem and its coloured/weighted versions (Chebotarev–Shamis,
Knill, Chung; snippets only) and the all-minors matrix-tree theorem (R1,
Theorem 2.4). No source read or seen in a snippet states a gamma-type,
half-gamma or `x^e(1+x)^i` expansion of `det(I + xM)` for a principal
submatrix `M` of a tree Laplacian, nor the recurrence
`Φ(T, ν) = (1 + (1 + ν_w)x) Φ(T − w, ν) + x(1 + ν_w x) Ψ`. A lead that was
not followed: `L_B = NNᵀ` with `N` the rows `B` of the incidence matrix, so
by Cauchy–Binet `Φ_B` is the matching generating polynomial of the bipartite
forest on `B` and the edges of `S` meeting `B` (auditor's remark, unreviewed;
it is the principal-submatrix analogue of the Zhou–Gutman identity, which was
seen only in snippets). The literature on matching polynomials of forests and
on Laplacian coefficients of trees (Mohar; Zhou–Gutman; the 2024 "subdivision
method" paper) is therefore the place where Lemma F or its recurrence could
already exist, and **none of it was read**.

**(c) Lemma C and the cones `C_d`.** *The half-gamma basis and the cones
`C_d` were not found under any name within this coverage.* Standard notions
located: gamma-positivity (symmetric polynomials only, per the abstract of
Athanasiadis's survey); the symmetric decomposition `p = a + xb` and the
alternatingly increasing property (R4, pp. 1–2); bi-gamma-positivity (snippet
only). The notion of the project is different from bi-gamma-positivity:
`x²` has a non-negative half-gamma expansion of degree 2, while its symmetric
decomposition with respect to `d = 2` is `a = −x`, `b = 1 + x`, so `a` has a
negative coefficient (auditor's check by hand with the formulas of R4,
Lemma 2.1). No statement of a product-closed cone of this kind was found; that
products of gamma-positive polynomials are gamma-positive is commonly used,
but no source stating it was opened in this audit. Lemma C is elementary and
may well be folklore; the search (queries 4 and 13, four pages of one paper)
cannot decide that.

**(d) Proposition S11 (contraction of the components of `S[A]` changes `r_A`
by `(a − a′)(1 + x)Φ_B`).** *Not found within this coverage.* One query
(number 12) addressed it; it returned only the general literature on tree
distance matrices (R1, R2, Choudhury–Khare, Graham–Lovász). The statement is
specific to the project's polynomials `r_A`, for which no prior source is
known, so a prior statement in these terms is unlikely to be found by keyword
search; an equivalent statement in other terms cannot be excluded.

**(e) Location of the peak for trees, 2023 onwards.** *No new result on the
Collins–Shor interval was found.* Beyond arXiv:2407.03309 (already recorded),
the only new item on the distance characteristic polynomial of trees since
2023 is R1 (coefficients as forest sums, Theorem C; nothing on the peak,
within what was read of it). The arXiv listing queries 15 and 16 and the
citation lists 17 to 19 show no paper announcing a proof, a refutation or a
family result. The three 2025–2026 listing entries of query 16 were judged
from titles and listing abstracts only.

### Not searched or not accessible

- MathSciNet, zbMATH, Google Scholar: not available to the tool; not searched.
  MathOverflow: one general web query naming it (number 13), no site search.
  OEIS, erdosproblems.com: not searched (no integer sequence was extracted
  from Lemma F or S7).
- Books: Bapat, *Graphs and Matrices* (chapters on the distance matrix of a
  tree and on the Laplacian); Brouwer–Haemers; Cvetković–Doob–Sachs; Godsil,
  *Algebraic Combinatorics* (matching polynomials). None consulted.
- Not read although located: R1 beyond the tool's extraction (proofs, and the
  last 8,982 characters only in the third pass); R4 after page 4; the
  Choudhury–Khare papers; Athanasiadis's survey; every item under "snippets
  only", in particular the matching-polynomial and Laplacian-coefficient
  literature relevant to Lemma F; Indulal–Stevanović 2015; arXiv:2604.26385,
  2604.12404, 2504.11706.
- Still unread from earlier audits: Collins (1989) and her thesis; the
  published version of Collins (1993); the DAM 2019 paper; Graham–Lovász
  pp. 68–79; Edelberg–Garey–Graham (1976); Aouchiche–Hansen (2014).
- Languages: English only in this session. No search in Chinese, Russian
  (Kelmans, Chebotarev–Shamis originals) or Portuguese.
- Formal libraries (Mathlib, formal-conjectures): not searched.
- The citation list of arXiv:2407.03309 came back empty, which is a failure
  of the index, not evidence that the paper is uncited. Papers citing R1, R2
  or Merris (1990) were not listed.

### Recommendation for the registry (the auditor did not edit it)

- MD-0011: novelty `preliminary-search-completed`. A first search exists and
  found no identical statement, but it found close prior results (R1, R2 and
  Graham–Lovász) and left the most relevant databases and books unsearched.
  The record should cite R2 (Theorems 2.1, 2.4) and R1 (Theorems A, 4.4).
- MD-0012: novelty `preliminary-search-completed`. Nothing found, but the
  literature in which Lemma F would most plausibly appear (matching
  polynomials of forests, Laplacian coefficients, forest polynomials) was
  identified and not read.

Neither search supports `no-prior-resolution-found`. An unsuccessful search
does not establish originality.
