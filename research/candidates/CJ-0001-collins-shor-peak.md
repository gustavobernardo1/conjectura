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
