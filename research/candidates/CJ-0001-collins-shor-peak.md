# CJ-0001 — Collins–Shor conjecture on the peak of the distance characteristic polynomial of a tree

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Let $T$ be a tree of order $n \ge 3$ with distance matrix $\mathcal{D}(T)$ (the $(i,j)$ entry is the length of the path from $v_i$ to $v_j$). Let $\delta_k(T)$ be the coefficient of $x^k$ in $\det(\mathcal{D}(T) - xI)$ and, for $0 \le k \le n-2$, let $d_k(T) = 2^{k-(n-2)}\,|\delta_k(T)|$ be the normalized coefficients. Conjecture 1.2 (Collins–Shor), verbatim: "The [normalized] coefficients of the distance characteristic polynomial for any tree $T$ with $n$ vertices are unimodal with peak between $\lfloor n/2 \rfloor$ and $\lceil n - n/\sqrt{5} \rceil$." Unimodality (indeed log-concavity) is Theorem 2.1 of the same paper. The open part is the location: every index $k$ at which $d_0(T),\dots,d_{n-2}(T)$ attains its maximum satisfies $\lfloor n/2 \rfloor \le k \le \lceil n - n/\sqrt{5} \rceil$. (The source does not say how a tie between two maximal coefficients is to be read; the project uses the strong reading 'every maximizing index' and records ties explicitly.)

**Source.** G. Aalipour, A. Abiad, Z. Berikkyzy, L. Hogben, F. H. J. Kenter, J. C.-H. Lin, M. Tait, Proof of a conjecture of Graham and Lovász concerning unimodality of coefficients of the distance characteristic polynomial of a tree, arXiv:1507.02341, Conjecture 1.2 (a search result reports the journal version as Electron. J. Linear Algebra, 2018; not verified from the journal); originally Conjecture 9 of K. L. Collins, On a conjecture of Graham and Lovász about distance matrices, Discrete Appl. Math. 25 (1989) 27-35, attributed there to P. Shor. <https://arxiv.org/abs/1507.02341>

**Statement checked against:** primary-source. The catalogued wording is Conjecture 1.2 of arXiv:1507.02341, compared with the paper's TeX source on 2026-11-26. Collins (1989) was not accessible in sessions 1 to 10; according to arXiv:1507.02341 it states the bounds without floor and ceiling. **Session 11:** Collins (1989) was read in full; its Conjecture 9 reads "The coefficients of CPD(T) for any tree T with n vertices are unimodal with peak between ½n and n(1 − 1/√5)", without floor or ceiling, as reported (see the section "Primary sources read in session 11").

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
- K. L. Collins, On a conjecture of Graham and Lovász about distance matrices, Discrete Appl. Math. 25 (1–2) (October 1989) 27–35, DOI `10.1016/0166-218X(89)90044-9` (bibliographic data confirmed from the Crossref record; full text not accessible until session 11, when it was read in full from a copy supplied by the director).
- K. L. Collins, Distance matrices of trees, Ph.D. thesis, MIT, 1986 (advisor R. P. Stanley), <https://dspace.mit.edu/handle/1721.1/77687> (record page read; PDF not accessible until session 11, when a copy supplied by the director was read: pp. 30–47 and 55–61 as page images, the rest through its OCR text layer).
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

## Literature audit 2026-11-26 (session 8): MD-0013 and MD-0014

Auditor: Claude (`claude-fable-5-2`), literature-auditor subagent. Budget set
by the launching session: about 15 minutes and about 40 tool calls (the
environment does not report elapsed time; the work was stopped at 38 tool
calls). Requests made: 8 web searches, 19 fetches (1 returned HTTP 429 and
succeeded on a later retry, 1 returned HTTP 404, 2 returned undecoded PDF
bytes whose first pages were then read as page images). All accesses on
2026-11-26. This is the first search made for the statements of MD-0013
(Propositions S12, S13) and MD-0014 (Proposition S14, Lemma G, Propositions
S15, S16, Corollary S17, Theorem S18), all in
`research/active/CJ-0001-collins-shor-peak/notes/gamma-components.md`. It
builds on the session-7 audit above and does not repeat it.

**Result in one sentence.** A prior source was found that implies part of
MD-0013: the identity `(κ − 4) · 1ᵀadj(P_A)1 = 2 det P_A` (S13(e), item (iv))
is a restatement of Theorems A, 2.4 and 4.4 of Richman–Shokrieh–Wu
(arXiv:2411.11488, item R1 of session 7) once `τ_Bᵀ adj(L_B) τ_B` is expanded
by the all-minors matrix-tree theorem, and with it the bound `κ ≥ 4`, equality
exactly for `|A| = 1` (S13(c), item (ii)) follows from their Theorem 4.6(b),
which gives more; the bridging step is the auditor's own derivation and is
unreviewed. No source read states the third form S12, the real-rootedness of
`r_A` (S13(d)), the component form S14, the recurrences S15 to S17 or the
induction S18. Lemma G1 and the spectral identity S13(b) are classical linear
algebra. The coverage is small and supports no statement of novelty.

### Queries (verbatim)

General web search tool (all in standard mode):

1. `Richman Shokrieh Wu "principal minors of tree distance matrices" det D[S] cof D[S] rooted spanning forests monotonicity`
2. `adjugate rank-one update "adj(A + uv^T)" formula principal submatrix diagonal perturbation "adjugate" multilinear determinant reference`
3. `"Laplacian matching polynomial" tree "principal submatrix" Laplacian weighted tree recurrence pendant vertex Mohammadian real roots "subdivision"`
4. `"sum of entries" inverse of principal submatrix distance matrix tree "Steiner" OR "subtree spanned" cof det ratio "effective resistance" OR "magnitude" tree subset formula Laplacian Schur complement`
5. `"definite pencil" OR "secular equation" real roots det(A + xB) positive definite bordered matrix "rank-one" interlacing polynomial "Φ(x)(a+bx) − x^2" OR "adjugate" quadratic form real-rooted Laplacian principal submatrix tree`
6. `Mohar "On the Laplacian coefficients of acyclic graphs" pendant vertex recurrence Laplacian characteristic polynomial tree "L_v" principal submatrix leaf deletion formula`
7. `tree Laplacian "rooted spanning forests" adjugate "I + xL" quadratic form recurrence leaf removal "vertex weights" OR "Dirichlet" polynomial "gamma-positive" OR "real-rooted" forests two-rooted "doubly rooted"`
8. `"gamma-positivity" OR "γ-positive" "Laplacian" polynomial tree "det(I + xL)" OR "forest polynomial" OR "Laplacian characteristic polynomial" trees non-symmetric expansion "x^i(1+x)" peak location coefficients`

The answers of the search tool are summaries and were used only to locate
sources. For queries 5, 7 and 8 the tool reported that it found nothing on the
specific part of the query (bordered/adjugate quadratic forms; leaf-removal
recurrences for the adjugate; gamma-type expansions of Laplacian polynomials).

arXiv listing search (`arxiv.org/search`, all fields, newest first):

9. `"distance matrix" tree "principal minors" OR "principal submatrix"` — the
   page reports 115 results; the first 49 were returned (listing abstracts
   only). Relevant entries: arXiv:2411.11488 (R1), 2407.01966, 2407.01227,
   2504.05337, 2309.08691, 2404.06684, 2407.03309. No entry among the 49
   concerns a polynomial of the form of `r_A`, nor the inverse of a principal
   submatrix of a tree distance matrix. Results 50 to 115 were not seen.

Citation index (Semantic Scholar API):

10. Citations of arXiv:2411.11488 — 2 papers: arXiv:2606.21902 and
    arXiv:2606.18061 (both opened at abstract level, see below).

### Sources opened, and what was read

**(R1, again) H. Richman, F. Shokrieh, C. Wu, Principal minors of tree
distance matrices, arXiv:2411.11488v2.** Access: HTML rendering through the
fetch tool's text extraction, two passes with questions aimed at Sections 4
and 5 (characters 0 to 100,000, and 55,000 to the end). Statements as returned
by the tool; not read as page images; proofs not read. In addition to the
statements recorded in session 7:

- Section 1.3: `det D[S]/cof D[S]` is called the *normalized principal minor*;
  `cof A = det A · 1ᵀA^{−1}1` for invertible `A`.
- Lemma 3.4: for `|S| ≥ 2`, `D[S]` has one positive and `|S| − 1` negative
  eigenvalues; in particular `det D[S] ≠ 0`.
- Proposition 4.1 and Corollary 4.3:
  `det D[S]/cof D[S] = max { uᵀDu : 1ᵀu = 1, u_v = 0 for v ∉ S }`.
- Theorem D: for non-empty `A ⊆ B ⊆ V`,
  `det D[A]/cof D[A] ≤ det D[B]/cof D[B]`.
- Proposition 4.5: `det D/cof D = ½ Σ_e α_e`.
- **Theorem 4.6** (inequalities not strict): (a)
  `det D[S]/cof D[S] ≤ ½ Σ_{e ∈ E(conv(S, G))} α_e`, `conv(S, G)` the subtree
  spanned by `S`; (b) for `s_0, s_1 ∈ S` joined by the path `γ`,
  `½ Σ_{e ∈ γ} α_e ≤ det D[S]/cof D[S]`.
- Definition 5.1, Proposition 5.2, **Theorem 5.3**: the *equilibrium vector*
  `m(G; S)`, `m_v = Σ_{T ∈ F_1(G;S)} w(T)(2 − outdeg(T, v))`, satisfies
  `1ᵀm = 2 Σ_T w(T)` and `D[S] m = λ 1` with
  `λ = Σ_e α_e Σ_{T ∈ F_1} w(T) − Σ_{F ∈ F_2} w(F)(2 − outdeg(F, ∗))²`.
- Per the tool: the paper does **not** express the ratio through
  `L[S̄]^{−1}` or as a quadratic form `mᵀ adj(L[S̄]) m`, and does not state
  `Σ_F (outdeg(F, ∗) − 2)² = mᵀ adj(L[S̄]) m`. A search summary (query 4) says
  the paper lists the inverse of `D[S]` as an open question; that sentence was
  not located in the text by the auditor.
- References of R1 relevant here (as listed by the tool): [4] R. B. Bapat,
  S. Sivasubramanian, Identities for minors of the Laplacian, resistance and
  distance matrices, Linear Algebra Appl. 435 (2011) 1479–1489, DOI
  `10.1016/j.laa.2011.03.028` (cited for `cof D[S]`); [10] K. Devriendt, Graph
  geometry from effective resistances, Ph.D. thesis, Oxford, 2022; [15]
  Gutiérrez–Lillo, arXiv:2407.01966. **None of the three was opened.**

**(R5) K. Castillo, I. Zaballa, On a formula of Thompson and McEnteggert for
the adjugate matrix, arXiv:2103.13739v1 (25 Mar 2021).** Access: abstract
page, and pages 1–2 of the PDF read as page images. Theorem 2.1, equation (1):
for a matrix `A` over a commutative ring, an eigenvalue `λ_0` and right and
left eigenvectors `v`, `w`, `wᵀv · Adj(λ_0 I − A) = p_A′(λ_0) · v wᵀ`; the
introduction attributes the Hermitian case to Thompson and McEnteggert
("[33, pp. 212–213]"; the reference list was not read, so the bibliographic
entry of [33] is not verified here).

**(R6) J.-C. Wan, Y. Wang, Z.-Y. Wang, Subdivision method in the Laplacian
matching polynomial, arXiv:2410.14112v1 (18 Oct 2024).** Access: HTML
rendering through the fetch tool's extraction; statements as returned by the
tool. Equation (1.4): the *principal Laplacian matching polynomial* of `G`
with respect to an induced subgraph `H`,
`β(G, x)_{[H]} = Σ_{M ∈ M(H)} (−1)^{|M|} Π_{v ∈ V(H) ∖ V(M)} (x − d_G(v))`.
Theorem 1.2 (attributed there to its reference [17]): for `W ⊆ V(G)`,
`α(S_G − W, x) = x^{|E(G)| − |V(G)| + |W|} β(G, x²)_{[G − W]}`, `α` the
matching polynomial and `S_G` the subdivision graph. Theorem 3.1: the zeros of
`β(G, x)_{[H − v]}` interlace those of `β(G, x)_{[H]}`. Reference [20] there:
B. Zhou, I. Gutman, A connection between ordinary and Laplacian spectra of
bipartite graphs, Linear Multilinear Algebra 56 (2008) 305–310. Per the tool:
no pendant-vertex or leaf-removal recurrence, nothing on vertex-weighted
trees, on the adjugate or on quadratic forms `pᵀ adj(·) p`, nothing on
expansions in `x^i(1+x)^j`; Mohar is not cited.

**(R7) B. Mohar, On the Laplacian coefficients of acyclic graphs, preprint
version (Univ. of Ljubljana Preprint series 44 (2006), no. 1023; the journal
version is cited elsewhere as Linear Algebra Appl. 422 (2007), not opened).**
Access: `https://users.fmf.uni-lj.si/mohar/Reprints/2007/BM07_LAA422_Mohar_LaplacianCoefficient.pdf`,
pages 1–4 of the PDF (cover, and pp. 1–3 of the text) read as page images.
Content read: equation (1), the Zhou–Gutman identity `c_k(T) = m_k(S(T))` for
acyclic `T`; the transformations `π` (merging two pendant paths) and `σ`;
Proposition 2.1; Theorem 2.2 (`c_k(T) ≤ c_k(T′) − Σ_d n_d C(n−3−d, k−1−d)`).
On the pages read there is no recurrence for `det(λI − L)` or its adjugate
under removal of a leaf, no principal submatrix of `L`, no vertex weights.
The rest of the paper was not read.

**(R8) Wikipedia, "Matrix determinant lemma"** (fetch tool's extraction):
`det(A + uvᵀ) = det A + vᵀ adj(A) u`, valid whether or not `A` is invertible;
references listed there: D. A. Harville, *Matrix Algebra From a Statistician's
Perspective*, Springer, 1997; J. Ding, A. Zhou, Eigenvalues of rank-one
updated matrices with some applications, Appl. Math. Lett. 20 (2007)
1223–1226 (neither opened). **Wikipedia, "Dodgson condensation"**: the
Desnanot–Jacobi identity
`det(M) det(M_{1,k}^{1,k}) = det(M_1^1) det(M_k^k) − det(M_1^k) det(M_k^1)`;
references listed there include Bressoud, *Proofs and Confirmations* (1999),
and Zeilberger, Electron. J. Combin. (1997) (not opened). **Wikipedia,
"Adjugate matrix"**: per the tool it states no rank-one update formula for the
adjugate and no Jacobi complementary-minor identity.

**Abstract pages only (nothing claimed about the papers' contents):**

- Á. Gutiérrez, A. Lillo, Principal minors of the distance matrix of a tree,
  arXiv:2407.01966 (2 Jul 2024): a combinatorial proof of a formula for
  `det D[S]` generalizing Graham–Pollak (tool's summary of the abstract).
- G. Wang, Principal minors of effective-resistance matrices and local
  resistance radii, arXiv:2606.18061 (v1 16 Jun 2026, v2 22 Jun 2026). As
  summarized by the tool: for a connected weighted graph with resistance
  matrix `R` and non-empty `S`, `cof R[S] = (−2)^{|S|−1} κ_G(S)/τ(G)` and
  `det R[S]/cof R[S] = (2/|S|) tr Q + ½ qᵀKq` after Kron reduction to `S`
  (`K` the reduced Laplacian, `Q = K⁺`, `q = diag Q`); the ratio is the
  maximum of `uᵀR[S]u` over `1ᵀu = 1`; monotonicity in `S`, a one-point update
  formula. The formula is reproduced from the tool's rendering and **was not
  verified against the paper**. For a tree `R = D`, so this concerns the same
  quantity `2/(1ᵀP_A^{−1}1)` as S13(e), through the Kron reduction onto `A`
  rather than through `L_B^{−1}` on the complement.
- H. Richman, F. Shokrieh, C. Wu, On determinants of resistance matrices,
  arXiv:2606.21902 (20 Jun 2026; the citation index gives DOI
  `10.1016/j.laa.2026.10.003`, not verified): an identity for the determinant
  of the resistance matrix of a graph through spanning trees and forests,
  generalizing Graham–Pollak, using "Bapat's expression" of that determinant.
- P. Chebotarev, E. Shamis, Matrix-forest theorems, arXiv:math/0602575
  (manuscript of 1994–1997): the `(i, j)` cofactor of `I + L(G)` is the number
  of spanning rooted forests in which `i` and `j` lie in the same tree rooted
  at `i`; `det(I + L)` counts all spanning rooted forests.
- R. Balaji, R. B. Bapat, S. Goel, On resistance matrices of weighted balanced
  digraphs, arXiv:2111.02051: the abstract quotes a formula for the inverse of
  the resistance matrix through the Laplacian and a vector `τ`, without
  attribution.
- P. N. Choudhury, A. Khare, arXiv:1903.11566, ar5iv rendering, first 100,000
  of 197,657 characters through the tool: Theorem A (minors of `D_T + xJ`
  depend only on edge data), Theorem B (inverse of the full matrix), Remark
  2.5 (`cof/det = eᵀD^{−1}e`). Per the tool: no inverse of a submatrix, no
  one-variable polynomial or real-rootedness statement, no
  `(2 − deg)ᵀ L[B]^{−1} (2 − deg)`. The second half was not read.

**Search-result snippets only, not opened:** Y. Liu, W. Yan (as named by the
search tool), Appl. Math. Comput. 457 (2023), weighted enumeration of rooted
forests and `det[L + diag(x_1, …, x_n)]`; Wan–Wang–Mohammadian, On the
location of zeros of the Laplacian matching polynomials of graphs,
arXiv:2103.10580; arXiv:2310.00360; a 2025 Open Mathematics paper
(`10.1515/math-2025-0185`); arXiv:1912.03101; arXiv:2501.12055
(bi-gamma-positivity of `1/k`-Eulerian polynomials); arXiv:2504.05337
(recurrences for determinants of tree distance matrices); arXiv:2404.06684
(Doust–Weston: determinant, `M`-constant and cofactor sum for subsets of
weighted Hamming cubes); a statement attributed to Doust and Wolf that the sum
of the entries of `D^{−1}` of an unweighted tree on `n + 1` points is `2/n`;
sources on definite matrix pencils (Manchester eprint 826; a Georgia Tech
preprint).

### Findings per item

**(a) S13(e), item (iv) of MD-0013: `(κ − 4) · 1ᵀadj(P_A)1 = 2 det P_A`.**
*An implying statement was found: R1, Theorems A, 2.4 and 4.4, together with
the all-minors matrix-tree theorem.* Derivation (the auditor's, unreviewed;
it assumes that `outdeg(F, ∗)` in R1 is the number of edges leaving the
floating component). For unit lengths, Theorems A and 4.4 give

`2 det D[A]/cof D[A] = (s − 1) − Σ_{F ∈ F_2(S; A)} (2 − outdeg(F, ∗))² / κ(S; A)`,
`κ(S; A) = det L_B` (Theorem 2.4).

For `v, w ∈ B`, `adj(L_B)_{vw}` is the number of spanning forests with
`|A| + 1` components in which every component but one contains exactly one
vertex of `A` and the remaining one contains `v` and `w` (all-minors
matrix-tree theorem): these are the forests of `F_2(S; A)` whose floating
component contains `v` and `w`. So
`τ_Bᵀ adj(L_B) τ_B = Σ_F (Σ_{v ∈ ∗(F)} (2 − g_v))² = Σ_F (2 − outdeg(F, ∗))²`,
since the degrees over a connected set `C` add up to `2(|C| − 1) + outdeg(C)`.
Hence `2 det P_A/cof P_A = s − 1 − τ_Bᵀ L_B^{−1} τ_B = κ − 4`, which is
S13(e). Checked by hand on two examples (the path on 3 vertices with `A` its
two ends: both sides 2; the star `K_{1,3}` with `A` two leaves:
`τ_Bᵀ adj(L_B) τ_B = 2 = Σ_F (2 − outdeg)²`, `det L_B = 2`, `κ = 6`). The
vector `ω` of the project's proof (`P_A ω = (κ − 4)1`, `1ᵀω = 2`) is, up to
the factor `det L_B`, the equilibrium vector of R1 (Definition 5.1, Theorem
5.3). Relation: **S13(e) is R1's Theorem A in the notation `L_B^{−1}`; the
form with the quadratic form `τ_Bᵀ L_B^{−1} τ_B` was not found stated, but it
is a direct translation.** arXiv:2606.18061 (abstract only) gives a further
closed form of the same ratio for resistance matrices.

**(b) S13(c), item (ii) of MD-0013: degree, leading coefficient, `κ ≥ 4` with
equality if and only if `|A| = 1`.** The degree and the leading coefficient
`κ det L_B` are specific to `r_A` and were not found. *The bound is implied by
(a) and R1, Theorem 4.6(b):* for `|A| ≥ 2` and `u, v ∈ A`,
`κ − 4 = 2 det P_A/cof P_A ≥ dist(u, v) ≥ 1`; for `|A| = 1`, `det D[A] = 0`
in Theorem A gives `κ = 4`. R1 gives more than S13(c):
`max_{u,v ∈ A} dist(u, v) ≤ κ − 4 ≤ |E(conv(A))|` (Theorem 4.6) and `κ` is
non-decreasing in `A` (Theorem D). This agrees with the computed minimum
`κ − 4 = 1` over `|A| ≥ 2` in `component-form.json`. The project's proof (a
variational argument on `B`) is different from R1's (optimization on `A`).

**(c) S12, item (i) of MD-0013 (third form), and S13(d), item (iii) (all
roots of `r_A` real and negative).** *Not found within this coverage.* No
source read or seen in a snippet considers `r_A` or a polynomial
`(linear) · det(I + xL_B) − pᵀ adj(I + xL_B) p`. The technique of S13(d)
(partial fractions of a rational function with positive residues, one zero
between consecutive poles) is the standard secular-equation argument for a
bordered or rank-one modified symmetric matrix; no source for it was opened in
this audit. Auditor's remark (unreviewed, a derivation and not a literature
finding): S12 says `r_A = det(A_0 + x A_1)` with the symmetric
`(t+1) × (t+1)` matrices `A_0 = [[I, 1], [1ᵀ, s]]` and
`A_1 = [[L_B, τ_B], [τ_Bᵀ, s + 3]]` (Schur complement of the block
`I + xL_B`). `A_0` is positive definite because `s − t = a ≥ 1`, and `A_1` is
positive definite because `L_B` is and its Schur complement is `κ > 0`. For a
positive definite `A_0` and a symmetric `A_1`,
`det(A_0 + xA_1) = det(A_0) Π_i (1 + θ_i x)` with `θ_i` the eigenvalues of
`A_0^{−1/2} A_1 A_0^{−1/2}`, which is the textbook fact on definite pencils.
So S13(d) follows from S12, S13(a) and `κ > 0` in one line, and S13(d) should
be regarded as an application of a classical fact to a formula (S12) that was
not found. Consistency check by hand on the path with 3 vertices, `A` its two
ends: `det(A_0 + xA_1) = (1 + 2x)(3 + 6x) − 1 = 2 + 12x + 12x²`, with
`r_A(0) = a = 2` and leading coefficient `κ det L_B = 12`.

**(d) S13(b) (the spectral identity for `zᵀ adj(I + xL_B) z`).** *Classical.*
It is the spectral decomposition of the adjugate of a symmetric matrix,
`adj(I + xL) = Σ_i Π_{l ≠ i}(1 + λ_l x) u_i u_iᵀ`; its value at
`x = −1/λ_i` for a simple eigenvalue is the Thompson–McEnteggert formula (R5,
Theorem 2.1, equation (1), read). The record already attributes the identity
to the director and does not present it as new.

**(e) Lemma G.** (G1), `adj(Z + c e_u e_uᵀ) = adj(Z) + c · adj(Z[u deleted])^ext`:
*classical; no source stating it in this form was found.* It holds for every
square matrix over a commutative ring, because each cofactor is an affine
function of the entry `z_uu` whose coefficient is the corresponding cofactor
of the matrix with row and column `u` removed (cofactor expansion; auditor's
remark, elementary). The determinant case is the matrix determinant lemma in
adjugate form (R8). The identity
`ψ adj(Z)_{vv′} − α_v α_{v′} = det(Z) adj(Y_0)_{vv′}` used in the note's proof
is, for `v = v′`, the Desnanot–Jacobi identity (R8) after a permutation of
indices, and in general Jacobi's theorem on the minors of the adjugate; for
the latter no opened source is available (Horn–Johnson, *Matrix Analysis*, is
the usual reference; not consulted, section number not verified). (G2), the
adjugate of `M(T, ν)` in terms of `T − w`: *not found*; it is a Schur
complement computation combined with (G1). Its determinant part is the
recurrence of Lemma F (MD-0012).

**(f) S14 (component form), S15, S16, S17 (recurrences for `R(T, ν)`), S18
(conditional induction) — MD-0014.** *Not found within this coverage.* The
polynomial `R(T, ν) = (N + j − 1)(1 + x)Φ − pᵀ adj(M) p` is defined in terms
of the project's `r_A`, for which no prior source is known, so a prior
statement in these terms is unlikely to be found by keyword search; an
equivalent statement in other terms cannot be excluded. Related published
material, none of which contains the statements:

- `Φ(T, ν)`, up to the substitution `x → −1/x`, is the characteristic
  polynomial of a principal submatrix of the Laplacian of a tree, which for a
  forest is the principal Laplacian matching polynomial of R6, equation (1.4)
  (auditor's identification: for an acyclic induced subgraph the permutation
  expansion of the determinant has only fixed points and transpositions). R6,
  Theorem 1.2, then gives `det(I + xL_B) = Σ_k m_k(S_S − A) x^k`, the matching
  generating polynomial of the subdivision graph of `S` with the vertices of
  `A` deleted. This is the published form of the "lead not followed" of the
  session-7 audit, item (b); it concerns MD-0012 and is background for
  MD-0014. R6, Theorem 3.1 (interlacing under vertex deletion) is the
  published counterpart of the real-rootedness of `Φ`.
- The cofactors of `I + L` count rooted spanning forests (Chebotarev–Shamis,
  abstract), so `pᵀ adj(I + xL_B) p` has a forest expansion; R1's sums over
  forests with a floating component are of this kind. No source read gives a
  recurrence for such a quadratic form at a leaf.
- Mohar (R7, pp. 1–3) and R6 contain no leaf-removal recurrence for the
  determinant or the adjugate on the parts read.
- Nothing was found on gamma-type or half-gamma expansions of Laplacian-type
  polynomials (query 8; the surveys of Athanasiadis and Brändén were again not
  read).

### Not searched or not accessible

- MathSciNet, zbMATH, Google Scholar: not available to the tool; not searched.
  MathOverflow, OEIS, erdosproblems.com: not searched. Formal libraries
  (Mathlib, formal-conjectures): not searched.
- Books: Horn–Johnson, *Matrix Analysis*; Bapat, *Graphs and Matrices*;
  Fiedler, *Matrices and Graphs in Geometry*; Parlett, *The Symmetric
  Eigenvalue Problem*; Godsil, *Algebraic Combinatorics*. None consulted. In
  particular no textbook source was opened for the definite-pencil fact, for
  the secular equation, or for Jacobi's theorem on minors of the adjugate.
- Not read although located: the proofs of R1 and its definition of
  `outdeg(F, ∗)` as page images; Bapat–Sivasubramanian (2011); Devriendt's
  thesis (2022) and the literature on resistance curvature and resistance
  radius; arXiv:2606.18061 and arXiv:2606.21902 beyond their abstracts;
  Gutiérrez–Lillo beyond the abstract; the second half of Choudhury–Khare;
  R6 as page images; R7 after page 3 and the journal version; the reference
  list of R5 (Thompson–McEnteggert's bibliographic entry); Liu–Yan (2023);
  Wan–Wang–Mohammadian; Zhou–Gutman (2008); Chebotarev–Shamis beyond the
  abstract; the surveys on gamma-positivity; results 50 to 115 of query 9.
- Not searched at all: Leinster's magnitude of metric spaces (for a tree the
  quantity `1ᵀP_A^{−1}1` is not the magnitude, which uses `e^{−d}`, but the
  literature may treat the limit); Fiedler's simplex geometry of resistance
  matrices; Graham–Hoffman–Hosoya; Steiner-distance literature beyond the
  listing titles of query 9; papers citing Bapat–Kirkland–Neumann (2005) or
  Bapat–Sivasubramanian (2011).
- Languages: English only.
- The citation list of R1 has two entries in the index used; a second index
  was not consulted.

### Recommendation for the registry (the auditor did not edit it)

- MD-0013: as the record stands (items (i) to (iv) together), novelty
  `preliminary-search-completed`, with the prior result recorded in the
  record: item (iv) and the bound of item (ii) are implied by R1 (Theorems A,
  2.4, 4.4 and 4.6(b)) through the derivation of item (a) above, which should
  be reviewed. If the record is split, the part "item (iv) and `κ ≥ 4` with
  its equality case" should carry `prior-resolution-identified` (source: R1)
  once that derivation is reviewed, and the part "third form, degree and
  leading coefficient, real negative roots" `preliminary-search-completed`.
  The record should also cite the classical basis of item (iii).
- MD-0014: novelty `preliminary-search-completed`. Nothing identical or
  implying was found; (G1) is classical; the literature on Laplacian matching
  polynomials and forest polynomials was only sampled.

Neither record supports `no-prior-resolution-found`: the databases and books
most likely to contain these facts were not searched. An unsuccessful search
does not establish originality.

## Audit for session 9 (2026-11-26): leaf recursion and star minimality

Auditor: literature-auditor subagent, model `claude-fable-5-2`. Budget stated
by the director: 9 minutes of wall-clock time and about 25 tool calls. Used: 24
tool calls (9 web searches, 9 page fetches of which 5 returned nothing
readable, 3 reads of this dossier, 2 edits, 1 hand-back). Wall-clock time was
not measured by the auditor. This is a FIRST prior-art search for the two
session-9 items below. It is shallow. Novelty of both items stays `unknown`.

Items searched for (statements as given to the auditor, not re-derived):

- (S23) Leaf recursion: `l_{T+}(x) = (1+x) l_T(x) + r_u(T)(x)` when a pendant
  vertex is attached at `u`, with `r_u(T) = (1+4x) Ψ + Ω`; equivalently a
  formula for `det(D_{T+} − 2xI)` minus a `(2+2x)`-multiple of
  `det(D_T − 2xI)`.
- (SM) Conjecture "star minimality in a cone order": `l_T − l_{K_{1,n−1}}` is a
  non-negative combination of `x^e (1+x)^{n−1−2e}` (`2e < n−1`) and `x^e`
  (`n−1 ≤ 2e ≤ 2n−2`). Weaker consequence: `d_k(T) ≥ d_k(star)` for every `k`.

### Queries (verbatim, general web search tool, standard mode)

1. `"distance characteristic polynomial" tree "pendant vertex" recursion coefficients`
2. `coefficients "distance characteristic polynomial" trees star minimizes path maximizes each coefficient extremal`
3. `Collins Shor conjecture distance matrix tree coefficients unimodal peak arXiv 2024 2025 2026`
4. `gamma-positivity distance characteristic polynomial tree OR "Laplacian polynomial" tree gamma-positive`
5. `"distance characteristic polynomial" tree coefficients "star" minimum "path" maximum "among all trees" coefficient ordering`
6. `"peak location" "distance characteristic polynomial" trees lower bound "n/2" 2025`
7. `"distance matrix" tree "pendant vertex" OR "pendent vertex" "characteristic polynomial" recurrence "D - " determinant leaf added Edelberg Garey Graham "On the distance matrix of a tree"`
8. `"generalized tree shift" OR "Kelmans transformation" "distance characteristic polynomial" OR "distance matrix" tree coefficients star minimal path maximal`
9. `Laplacian coefficients of trees star minimal path maximal Zhou Gutman Mohar "Laplacian coefficients of acyclic graphs" every coefficient`

Each query returned about ten links and a machine-written summary. Only the
summaries and link titles were seen; they are "snippets" below and are not
quotations from the papers.

### URLs fetched and what was actually read

| URL | Outcome |
| --- | --- |
| `https://arxiv.org/search/?query=%22distance+characteristic+polynomial%22&searchtype=all&abstracts=hide&order=-announced_date_first&size=50` | Read (listing page, through the fetch tool's extraction). "Showing 1–5 of 5 results": 2206.07561 (15 Jun 2022), 1903.04575, 1811.03061, 1507.02341, 1505.07651. No entry later than June 2022. |
| `https://api.semanticscholar.org/graph/v1/paper/arXiv:1507.02341/citations?fields=title,year,externalIds&limit=100` | Read. 5 citing papers: arXiv:2407.03309 (DOI `10.1007/s40314-025-03163-5`), arXiv:2206.07561 (DOI `10.1016/j.laa.2023.03.027`), arXiv:2104.14516, arXiv:2103.00647, arXiv:1812.05734. Same five as in sessions 2 and 5. |
| `https://arxiv.org/abs/2407.03309` | Abstract page read through the fetch tool's paraphrase (not verbatim). One version, 3 July 2024. Per that paraphrase the abstract does not mention a `⌊n/2⌋` lower bound, stars, or a coefficientwise comparison of trees. |
| `https://arxiv.org/abs/2206.07561` | Abstract page read through the fetch tool's paraphrase. One version, 15 June 2022. Peak established "for several extremal cases of uniform block graphs with small diameter"; no lower bound on the peak, no pendant-vertex recursion mentioned in the abstract. |
| `https://arxiv.org/pdf/2407.03309` | Fetched; the tool returned undecoded PDF bytes. NOT read in this session. (Session 2 records a full reading; not re-verified here.) |
| `https://arxiv.org/pdf/2206.07561` | Fetched; undecoded PDF bytes; only the outline was legible (section 4.2 "Peak location"). NOT read in this session. (Session 2 records a full reading; not re-verified here.) |
| `https://mathweb.ucsd.edu/~ronspubs/78_12_matrix_polynomials.pdf` (Graham–Lovász 1978) | Fetched; scanned page images without a text layer. NOT read. |
| `https://core.ac.uk/download/10129286.pdf` | HTTP 403 (as in session 2). NOT read. |
| `https://arxiv.org/a/search/?query=...` | HTTP 404 (malformed URL, auditor's error); replaced by the first row. |

### Findings per item (within this coverage only)

**(a) Recursion for the distance characteristic polynomial under adding a
pendant vertex.** No statement of such a recursion was read. The closest lead
is unread: the summary of query 1 attributes to the document at
`core.ac.uk/download/10129286.pdf` (described by the search tool as a thesis;
session 2 recorded it, also from a search result, as Collins's thesis) the
remark that the contribution of a leaf can be isolated and that, since a tree
can be decomposed by removing one leaf at a time, the characteristic polynomial
can be built up this way, "although time consuming". The document returned
HTTP 403, so its identity, the exact formula (if any) and whether it coincides
with (S23) are all unverified. **This is an open obligation of the audit: (S23)
may be a known recursion in that document.** Other leads, snippets only:
Choudhury–Khare, arXiv:1903.11566 (minors of the distance matrix under deleting
pendant nodes and adding pendant trees; the first half was read in session 8,
not for this question); an unattributed snippet about adding a pendant vertex
`n+1` with edge weight `α_n` in a weighted tree (source link not identified;
candidates in the result list were arXiv:1810.06182 and Bapat–Kirkland–Neumann).
Graham–Lovász (1978) and Edelberg–Garey–Graham (1976) were not read.

**(b) Star minimal or path maximal for each coefficient of the distance
characteristic polynomial.** Nothing found: queries 2, 5 and 8 returned no
source stating a coefficientwise extremal result for the distance
characteristic polynomial of trees. Related classical results for other
polynomials, snippets only, none opened: Zhou–Gutman (extreme values of every
Laplacian coefficient among `n`-vertex trees attained by the path and the star,
as reported in the snippet of Ilić, arXiv:1104.4280); Mohar, "On the Laplacian
coefficients of acyclic graphs" (title used in the query; not returned);
Csikvári's generalized tree shift poset, "On a poset of trees" I and II (the
shift moves adjacency and Laplacian characteristic polynomial coefficients
monotonically; path and star are the extreme elements); arXiv:1912.03101 and
arXiv:2307.15979 (immanantal and generalized matrix polynomials of tree
Laplacians along the same poset; titles and snippet only); arXiv:2306.05155
(the shift increases the distance spectral radius of complements of trees;
snippet only). The search summary of query 8 states that it did not find
whether monotonicity along the generalized tree shift holds for the distance
polynomial coefficients. Auditor's remark, not checked: the classical Laplacian
results concern `det(I + xL)` alone; `l_T` subtracts `x τᵀ adj(I + xL) τ`, so
they do not by themselves give `d_k(T) ≥ d_k(star)`. Whether that inequality
follows from the Graham–Lovász subforest formula was not examined.

**(c) Progress on the lower half (peak `≥ ⌊n/2⌋`).** Nothing new found. The
arXiv listing search for the phrase "distance characteristic polynomial"
returns five entries, the latest dated 15 June 2022; the citation index lists
the same five papers citing arXiv:1507.02341 as in sessions 2 and 5. Snippets
of queries 2, 3, 5 and 6 repeat what the dossier already records from
arXiv:1507.02341 (upper bound `⌈2n/3⌉`, a diameter-dependent lower bound of
order `n/(d+1)`, and the sentence that `⌊n/2⌋` is "clearly the intended lower
bound" because Collins's Theorem 1 gives `⌊n/2⌋` as the peak of the star);
these were not re-read this session. No paper dated 2025 or 2026 on the
question surfaced. The listing search matches metadata only: it does not return
arXiv:2407.03309, which shows that a paper phrased differently would be missed.

**(d) Gamma-positivity or half-gamma expansions for distance or Laplacian
polynomials of trees.** Nothing found (queries 4 and 8). Returned, titles and
snippets only, none opened: González D'León, arXiv:1505.06676 (gamma
coefficients of the tree Eulerian polynomial, a different polynomial);
Athanasiadis's survey, arXiv:1711.05983; arXiv:2604.18824, "Symmetric and
unimodal independence polynomials of trees" (title only); arXiv:1912.03101
(above). No source expanding a distance or Laplacian polynomial of a tree in
the basis `x^e (1+x)^{m−2e}` was seen.

### Not searched or not accessible

- MathSciNet, zbMATH, Google Scholar: not available to the tool; not searched.
- MathOverflow, OEIS, erdosproblems.com, Open Problem Garden: not searched.
  Formal libraries (Mathlib, formal-conjectures): not searched.
- Not read although located: the document at `core.ac.uk/download/10129286.pdf`
  (403; the most important gap for (a)); Graham–Lovász (1978) (scan);
  Edelberg–Garey–Graham (1976); Collins's 1989 paper beyond what session 6
  records; Zhou–Gutman (2008); Mohar (2007); Csikvári's two papers; Ilić,
  arXiv:1104.4280; arXiv:1912.03101; arXiv:2307.15979; arXiv:2306.05155;
  arXiv:2604.18824; the gamma-positivity surveys; the journal versions of
  arXiv:2206.07561 and arXiv:2407.03309.
- Not done: citing-paper lists of arXiv:2206.07561 and arXiv:2407.03309; a
  second citation index; arXiv listing searches with other phrasings ("distance
  matrix" with "tree" and "coefficients"; "Graham" with "Lovász" and "peak");
  any search on resistance or Steiner distance analogues of (S23); books
  (Bapat, *Graphs and Matrices*; Brouwer–Haemers; Cvetković–Doob–Sachs).
- Languages: English only.

### Recommendation for the registry (the auditor did not edit it)

Any record created for (S23) or (SM) should carry novelty `unknown` or at most
`preliminary-search-completed`, with the unread Collins-thesis lead recorded as
an open obligation for (S23). Nothing here supports
`no-prior-resolution-found`. An unsuccessful search does not establish
originality.

## Audit for session 10 (2026-11-26): originality of MD-0016 (Wiener form, peak at least ⌊(n−1)/2⌋)

Auditor: literature-auditor subagent, model `claude-fable-5-2`. Budget stated
by the director: 12 minutes of wall-clock time and at most 35 tool calls. Used:
35 tool calls (7 web searches; 18 page fetches, of which 5 returned HTTP 403 or
429 or a redirect notice and 4 returned undecoded PDF bytes that were then read
as page images from the saved copy; 8 local reads, 5 of them of those saved
PDFs; 1 edit of this dossier; 1 hand-back). Wall-clock time was not measured by
the auditor. The search stopped because the call budget was spent, not because
the leads were exhausted. Novelty of MD-0016 is not established by this audit.

The statements audited are those of
`research/active/CJ-0001-collins-shor-peak/notes/wiener-form.md` (read in
full): Lemma S24, identity (1) in the proof of Proposition S25, Proposition S25
and Theorem T4. Notation as there: `T` a tree on `n` vertices, `L` its
Laplacian, `D` its distance matrix, `M = I + xL`, `Φ = det M`,
`τ_v = 2 − deg v`, `t = D1`, `W` the Wiener index. The queries of the session-9
audit were not repeated.

### Items

- (a) Lemma S24: `adj(I + xL)_{uv} = x^{dist(u,v)} det (I + xL)[V ∖ path(u,v)]`.
- (b) `L t = nτ − 2·1`, equivalently `LD + 2I = τ1ᵀ`.
- (c) Proposition S25 (the Wiener form):
  `n² l_T(x) = 4(W − nx)Φ(x) + Σ_{u<v} (t_u − t_v)² x^{dist(u,v)−1} Π_{uv}(x)`.
- (d) Theorem T4: `d_{μ−1} < d_μ` for `μ = ⌊(n−1)/2⌋` and every tree of order
  `n ≥ 3` (peak at least `⌊(n−1)/2⌋`).
- (e) The unread document at `core.ac.uk/download/10129286.pdf`.

### Queries (verbatim, general web search tool, standard mode)

1. `"matrix forest theorem" (I + L)^{-1} tree entries "path" off-diagonal entry product forests Chebotarev Shamis "spanning rooted forests" tree accessibility`
2. `Graham Lovász distance matrix tree inverse "LD" "2I" identity Laplacian "τ" "D^{-1} = -L/2 + ττ^T/(2(n-1))" Bapat "Graphs and Matrices" "LD + 2I"`
3. `"distance characteristic polynomial" tree "Wiener index" "Laplacian" formula "transmission" determinant identity "det(I + xL)" OR "Laplacian characteristic polynomial" Graham Lovász subforest`
4. `Graham Lovász conjecture distance characteristic polynomial tree coefficients peak "lower bound" "n/2" proof 2025 OR 2026 arXiv unimodal peak location trees`
5. `Collins thesis "distance matrices of trees" MIT 1986 characteristic polynomial leaf "one leaf at a time" dspace`
6. `tree "distance matrix" "characteristic polynomial" identity "Wiener index" "(I + xL)" OR "resolvent of the Laplacian" OR "forest matrix" "transmission" "(t_u - t_v)^2" OR "Tr(u) - Tr(v)" Graham Lovász coefficients formula`
7. `thesis OR dissertation "Graham" "Lovász" conjecture "distance characteristic polynomial" tree unimodal peak "lower bound" Nascimento OR "peak location" "every tree" coefficients "⌊n/2⌋"`

Each query returned about ten links and a machine-written summary. Text taken
from those summaries is called a "snippet" below and is not a quotation from a
paper.

### URLs fetched and what was actually read

"Page images" means that the fetch tool saved the PDF and the auditor read the
named pages as images, directly. "Tool summary" means that the auditor saw only
the fetch tool's machine-written answer about the page, not the page itself.

| URL | Outcome |
| --- | --- |
| `https://arxiv.org/pdf/math/0602575` (Chebotarev, Shamis, "Matrix-Forest Theorems", arXiv:math/0602575v2) | Page images, pages 1 to 11 of 11 (the whole paper). |
| `https://mathweb.ucsd.edu/~ronspubs/78_12_matrix_polynomials.pdf` (Graham, Lovász, "Distance matrix polynomials of trees", Adv. Math. 29 (1978) 60–88) | Page images of the scan, journal pages 60 to 71. Pages 72 to 88 NOT read. |
| `https://www.math.ucdavis.edu/~saito/data/distmat/bapat-kirkland-neumann-distmat-lap.pdf` (Bapat, Kirkland, Neumann, "On distance matrices and Laplacians", Linear Algebra Appl. 401 (2005) 193–209) | Page images, journal pages 193 to 198. Pages 199 to 209 NOT read. |
| `https://math.ucdavis.edu/~saito/data/distmat/aouchiche-hansen_dist-spec-graphs-survey.pdf` (Aouchiche, Hansen, "Distance spectra of graphs: A survey", Linear Algebra Appl. 458 (2014) 301–386) | Page images, journal pages 301 to 308. Pages 309 to 386 NOT read. |
| `https://ar5iv.labs.arxiv.org/abs/2206.07561` (full text of arXiv:2206.07561) | Tool summary of the full text. |
| `https://arxiv.org/abs/2206.07561` | Tool summary of the abstract page (the tool declined to reproduce the abstract verbatim). Authors: Abiad, Brimkov, Hayat, Khramova, Koolen. One version, 15 June 2022. |
| `https://arxiv.org/html/2407.03309` (full text of arXiv:2407.03309) | Tool summary of the full text; the tool reported that parts (the path subsection, the bi-star result) were not in the text it was given. |
| `https://arxiv.org/abs/2407.03309` | Tool summary of the abstract page. Authors: Jana, Mahato, Sivasubramanian. 3 July 2024. |
| `https://arxiv.org/html/2411.11488` (Richman, Shokrieh, Wu, "Principal minors of tree distance matrices", arXiv:2411.11488v2, stamp 10 Dec 2025) | Tool summary of the first 100000 of 108982 characters; the last 8982 (reference list, per the tool) not read. |
| `https://api.semanticscholar.org/graph/v1/paper/arXiv:2206.07561/citations?fields=title,year,externalIds&limit=100` | Read (tool's listing): 8 citing papers, titles only. |
| `https://api.semanticscholar.org/graph/v1/paper/arXiv:2407.03309/citations?fields=title,year,externalIds&limit=100` | Read: empty list. |
| `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/0166-218X(89)90044-9/citations?fields=title,year,externalIds&limit=200` (Collins 1989) | Read (tool's listing): 14 citing papers in total; the 6 dated 2019 or later were listed by title. |
| `https://dspace.mit.edu/handle/1721.1/77687` | Tool summary of the record page: "Distance matrices of trees", Karen L. Collins, Ph.D. thesis, MIT Department of Mathematics, 1986, advisor Richard P. Stanley; "Bibliography: leaf 56"; one file `15748263-MIT.pdf` (2.26 MB). No abstract or table of contents on the record page. |
| `https://dspace.mit.edu/bitstreams/ffd29595-5770-4d22-936c-16bab6d1daf5/download` | HTTP 429 (Retry-After 900). NOT read. |
| `https://core.ac.uk/outputs/10129286`, `https://core.ac.uk/reader/10129286`, `https://core.ac.uk/download/10129286.pdf` | HTTP 403, all three. NOT read. |
| `https://ar5iv.org/abs/2206.07561` | Redirect notice only; replaced by the `ar5iv.labs.arxiv.org` row. |

### Findings per item (within this coverage only)

**(a) Lemma S24 — known consequence of Maybee–Olesky–van den Driessche–Wiener
(1989), as quoted in Chebotarev–Shamis, via a one-path specialization
(bridging step — unreviewed).** Read directly in arXiv:math/0602575v2:

- Theorem 5 and Theorem 6 (p. 5): for a weighted multigraph `G` and
  `W = I + L(G)`, `det W` is the total weight of the spanning rooted forests of
  `G`, and the cofactor `W^{ij}` is the total weight of the spanning rooted
  forests in which `i` and `j` belong to the same tree rooted at `i`. Theorem 7:
  `(W^{−1})_{ij}` is the quotient of the two. The weight of a forest is the
  product of the weights of its edges, so taking every edge weight equal to `x`
  gives `I + xL`. The paper states that Theorems 3 and 4 (the directed
  versions) can be derived from Chaiken's all-minors theorem (its reference
  [2], SIAM J. Alg. Disc. Meth. 3 (1982) 319–329, NOT opened).
- Equation (4) (p. 8), attributed there to "a theorem by Maybee (see [16])",
  [16] being Maybee, Olesky, van den Driessche, Wiener, "Matrices, digraphs,
  and determinants", SIAM J. Matrix Anal. Appl. 10 (1989) 500–519 (NOT opened):
  for any `n × n` matrix `U` and `i ≠ j`, the cofactor `U^{ij}` equals the sum,
  over the paths `P_k` from `i` to `j` in the weighted digraph of `U` (arc
  weights `−u_{ij}`), of the weight of `P_k` times `det U_{−ψ_k}`, where `ψ_k`
  is the vertex set of `P_k` and `U_{−ψ}` is `U` with those rows and columns
  deleted.

Bridging step, written by the auditor and not reviewed: for `U = I + xL` of a
tree the off-diagonal entries are `−x` on the edges, the digraph has one path
from `u` to `v`, of weight `x^{dist(u,v)}`, and (4) reads
`adj(I + xL)_{uv} = x^{dist(u,v)} det (I + xL)[V ∖ V(P)]`, which is the first
equality of Lemma S24. No source was found that states this tree
specialization in these words. The remaining parts of Lemma S24 (the product
over the components off the path, and the membership in the cone `C_{n−d−1}`)
rest on the project's Lemma F and cones; no source was searched for them. Not
opened: Chebotarev–Shamis, Automat. Remote Control 58 (1997) 1505–1514
(arXiv:math/0602070), which is reference [4] of the paper read; Chaiken (1982);
Maybee et al. (1989); Moon, "On the adjoint of a matrix associated with trees",
Lin. Multilin. Alg. 39 (1995) 191–194 (reference [20] there; by its title a
possible direct source, title only).

**(b) `L t = nτ − 2·1`, `LD + 2I = τ1ᵀ` — known consequence of Graham–Lovász
(1978), Lemma 1, via a two-line step (bridging step — unreviewed).** Read
directly:

- Graham–Lovász (1978), Lemma 1, p. 66: the entries of `D^{−1}` for a tree, in
  terms of the degrees and the adjacency matrix. Some minus signs are faint in
  the scan; the same formula is legible in Aouchiche–Hansen (2014), Theorem 2.8,
  p. 308 ("See [63]", their [63] being Graham–Lovász):
  `(D^{−1})_{ij} = (2 − d_i)(2 − d_j)/(2(n−1)) + (−d_i/2 if i = j, a_{ij}/2 if i ≠ j)`,
  and, on the same page, in matrix form `D^{−1} = −½L + δδᵀ/(2(n−1))` with
  `δ_i = 2 − d_i`.
- Bapat–Kirkland–Neumann (2005), Theorem 2.1, p. 195: the weighted version
  `D^{−1} = −½L + δδᵀ/(2 Σ α_i)`, attributed in the unweighted case to Graham
  and Lovász; and in its proof, p. 196: `Dδ = σ_{n−1} 1` (for unit weights,
  `Dτ = (n−1)1`).

Bridging step (auditor, unreviewed): multiplying `D^{−1} = −½L + ττᵀ/(2(n−1))`
on the right by `D` and using `τᵀD = (n−1)1ᵀ` gives `I = −½LD + ½τ1ᵀ`, that is
`LD + 2I = τ1ᵀ`; applied to `1` it gives `Lt = nτ − 2·1`, and column `c` gives
`Lδ_c = τ − 2e_c`. The relation `tᵀτ = n(n−1)` used in the proof of S25 follows
from `Dτ = (n−1)1`. The identity in the exact form `LD + 2I = τ1ᵀ` was NOT
seen in any page read; the summary of query 2 reports that it found no source
stating it. The auditor recalls it as a lemma of Bapat's book *Graphs and
Matrices* (chapter on the distance matrix of a tree); the book was not opened,
so this recollection is unverified and must not be cited as read.

**(c) Proposition S25, the Wiener form — no source found within this coverage
(originality NOT established).** No formula expressing the distance
characteristic polynomial of a tree through `det(I + xL)`, the Wiener index and
squared differences of transmissions was seen. What was read, and how close it
comes:

- Graham–Lovász (1978), pp. 64–67, read directly: formula (7), the coefficients
  as `Σ_F A_F^{(k)} N_F(T)` over forests; and (10)–(13): the bordered
  `(n+1) × (n+1)` matrix `D′(λ)` with corner `−(n−1)`, border `2 − d_i`,
  diagonal `−2λ − d_i` and off-diagonal `a_{ij}` (that is, `−(2λI + L)` bordered
  by `τ`), with Fact 4 `det D′(λ) = −(n−1) 2^n det(D^{−1} − λI)` and
  `δ_k(T) = ¼ δ′_{n−k}(T)`. This is the place where the Laplacian pencil enters;
  it is the source of the project's L1. Neither the Wiener index nor the
  transmissions appear on pp. 60–71. Pages 72–88 were not read.
- Aouchiche–Hansen (2014), pp. 301–308, read directly: Theorem 2.4
  (Edelberg–Garey–Graham: the signs, `a_{n−2} = (−1)^{n−1} Σ_{i<j} d_{ij}²`,
  `a_0` to `a_3` as subtree counts), Theorem 2.5 (Graham–Lovász subforest
  form), Theorems 2.8 and 2.9 (the inverse). The Wiener index and the
  transmission are defined on p. 304; in the pages read they are not connected
  to the distance characteristic polynomial of a tree. The rest of the survey
  (78 pages, including the sections on transmission-regular graphs) was not
  read.
- Richman–Shokrieh–Wu, arXiv:2411.11488v2 (tool summary only; found through
  query 6): Theorem C gives the coefficient of `λ^{n−k}` of `det(D − λI)` as
  `(−1)^{n−1} 2^{k−2}` times `(n−1) Σ_{F ∈ F_k} π(F) − Σ_{F ∈ F_{k+1}} π(F) Σ_j (outdeg(C_j) − 2)²/|V(C_j)|`,
  over spanning forests with `k` and `k+1` components, `π(F)` the product of
  the component orders. Per the tool: no Wiener index, no transmissions, no
  `det(I + xL)`, nothing on unimodality or the peak. Auditor's remark, not
  checked beyond this line: since `Σ_{v ∈ C} (2 − deg v) = 2 − outdeg(C)` for a
  component `C` of a spanning forest of a tree, Theorem C reads as the
  forest-by-forest expansion of L1, `(n−1)Φ − x τᵀ adj(I + xL) τ`. It is the
  closest published formula found, and it is a different formula: S25 is
  obtained from L1 by the substitution `τ = (Lt + 2·1)/n`, which that paper (per
  the tool summary) does not make. If the project cites L1, this preprint
  should be cited next to Graham–Lovász.

Assessment of what the originality of (c) amounts to, for whoever classifies
the record: the proof of S25 in the note is a short computation from L1
(Graham–Lovász), identity (b) (a consequence of the Graham–Lovász inverse) and
(a) (a consequence of the path expansion of a cofactor). If the identity is
unpublished, what would be new is the form, not a new ingredient. Snippets
only, not opened, and possible places for a formula of this kind: Merris, "The
distance spectrum of a tree" (J. Graph Theory, 1990; a PDF was located at
`math.ucdavis.edu/~saito/data/distmat/merris-distspect-tree.pdf`); the
Merris/McKay formula for the Wiener index of a tree through the Laplacian
eigenvalues (arXiv:1304.0873 and a 2003 paper, snippets); arXiv:1609.06911
("On the Wiener index, distance cospectrality and transmission regular
graphs"); arXiv:2008.06068 ("Bilinear matrix equation characterizes Laplacian
and distance matrices of weighted trees"). Not opened at all:
Edelberg–Garey–Graham (1976); Collins (1989) and her thesis; Bapat's book; the
Bapat–Sivasubramanian papers; Zhou–Trinajstić; the literature on the distance
Laplacian `Diag(t) − D`.

**(d) Theorem T4 — no source found within this coverage (originality NOT
established).** No statement that the peak of the normalized coefficients is at
least `⌊(n−1)/2⌋`, or at least `⌊n/2⌋` for odd `n`, for every tree was seen.

- Aouchiche–Hansen (2014), p. 307, read directly: after Conjecture 2.6 ("The
  coefficients of the distance characteristic polynomial of any tree `T` with
  `n` vertices are unimodal with peak between `n/2` and `(1 − 1/√5)n`",
  attributed to Collins): "No more results are known about that conjecture."
  This describes the state in 2014, before arXiv:1507.02341.
- arXiv:2206.07561 (tool summary of the ar5iv full text; journal version DOI
  `10.1016/j.laa.2023.03.027` per the citation index, not opened). On trees,
  the tool quotes "Little progress on this problem is known" and reports:
  Collins for stars and paths; Conjecture 1.1, the peak between `⌊n/2⌋` and
  `⌈(1 − 1/√5)n⌉`; Aalipour et al. for unimodality and log-concavity. Its own
  peak results concern block graphs: Theorem 4.3 (windmill graphs, asymptotic),
  Corollary 4.5 (friendship graphs, `3k/4 + O(log k)`), Theorem 4.6 (a
  universal vertex joined to two copies of `K_t`: peak at `⌊n/2⌋`), Theorem 4.7
  (barbell graphs), Corollary 4.8 (lollipop graphs, `⌊(n−1)/2⌋`). Open there:
  Question 5.1, whether the coefficients of every block graph on `n` vertices
  are unimodal with peak between `⌊n/3⌋` and `⌊n/2⌋`. No peak-location result
  for general trees, and no formula through the Laplacian, the Wiener index or
  transmissions, per the tool.
- arXiv:2407.03309 (tool summary of the arXiv HTML full text; journal version
  DOI `10.1007/s40314-025-03163-5`, not opened). It concerns two other
  matrices of a tree: Theorem 3, for the Min-4PC matrix, peak index `t` with
  `⌊(n−2)/3⌋ ≤ t ≤ ⌈(n+1)/3⌉`, with unimodality and log-concavity; Theorem 5,
  unimodality and log-concavity for the 2-Steiner distance matrix; Theorem 18,
  the star for the 2-Steiner matrix, `⌊(n−2)/2⌋ ≤ t ≤ ⌈n/2⌉`; a conjecture on
  the peak for the path (value not in the text the tool was given). Per the
  tool it proves nothing about the peak of the ordinary distance matrix and
  says only that bounds for it are known.
- Citation indexes (Semantic Scholar, titles only). Citing arXiv:2206.07561:
  8 papers, of which only arXiv:2407.03309 concerns this question by its title;
  the others are arXiv:2309.08691 ("The additive-multiplicative distance matrix
  of a graph, and a novel third invariant") and six papers on unrelated
  subjects. Citing arXiv:2407.03309: none listed. Citing Collins (1989): 14 in
  total; the six dated 2019 or later are arXiv:2407.03309, arXiv:2306.07956,
  arXiv:2207.03343 (two papers on Monte Carlo search for refuting conjectures,
  not opened), arXiv:2206.07561, arXiv:2104.14516 and arXiv:2103.00647. The
  eight older ones were not listed by the tool. Together with session 9
  (citations of arXiv:1507.02341), no paper citing any of the four concerns the
  peak of trees other than those already in this dossier.
- Queries 4 and 7 returned no paper dated 2025 or 2026 and no thesis; nothing
  under the name Nascimento. Their summaries repeat what this dossier already
  records from arXiv:1507.02341 (upper and lower bounds on the peak, the remark
  that `⌊n/2⌋` is the intended lower bound); that paper was not re-read in this
  session, and the comparison of T4 with its lower bound should be made against
  the reading recorded earlier in this dossier.

**(e) The document at `core.ac.uk/download/10129286.pdf` — NOT read; the
obligation of session 9 stays open.** The three core.ac.uk addresses returned
HTTP 403. Query 5 lists that address in the result list for Karen L. Collins's
thesis, and the DSpace@MIT record `1721.1/77687` (tool summary) confirms that
such a thesis exists: "Distance matrices of trees", Ph.D., MIT, 1986, advisor
Richard P. Stanley, bibliography on leaf 56. That the core.ac.uk document is
this thesis rests on the search result list only. The summary of query 5 says
that the thesis has "a section on the actual contribution of a leaf" and a
section on cospectral trees (snippet; not verified). The full text on DSpace
returned HTTP 429 with a retry delay of 900 seconds. Whether the thesis
contains a leaf-by-leaf recursion for the distance polynomial of a tree, and
whether it coincides with (S23), is therefore still unknown. Next access path
to try: the DSpace bitstream address in the table above.

### What would threaten the originality of (c) or (d)

- For (c): nothing read states it. The identity is a few lines from known
  ingredients, so a statement of it may exist in a place this audit did not
  reach (Merris 1990, Collins's thesis and 1989 paper, Bapat's book, pages
  72–88 of Graham–Lovász, the distance-Laplacian literature), none of which
  was read.
- For (d): nothing read states it or a stronger bound for all trees. The
  sources that would be expected to mention such a bound (the two follow-up
  papers and the 2014 survey) report no general result of this kind, on the
  evidence of tool summaries for the two papers and of a direct reading for the
  survey. A paper that does not cite arXiv:1507.02341, arXiv:2206.07561 or
  Collins (1989), or one newer than the citation index, would have been missed.

### Not searched or not accessible

- MathSciNet, zbMATH, Google Scholar: not available to the tool; not searched.
- MathOverflow, OEIS, erdosproblems.com, Open Problem Garden: not searched.
  Formal libraries (Mathlib, formal-conjectures): not searched.
- Located and not read: Collins's thesis (403 on core.ac.uk, 429 on DSpace);
  Graham–Lovász (1978) pp. 72–88, which include the statement of the
  conjecture; Bapat–Kirkland–Neumann (2005) pp. 199–209; Aouchiche–Hansen
  (2014) pp. 309–386; Merris (1990); Chaiken (1982); Maybee et al. (1989);
  Moon (1995); Chebotarev–Shamis (1997); Collins (1989); Edelberg–Garey–Graham
  (1976); Bapat, *Graphs and Matrices*; arXiv:2309.08691; arXiv:2306.07956;
  arXiv:2207.03343; arXiv:1609.06911; arXiv:2008.06068; arXiv:1304.0873; the
  journal versions of arXiv:2206.07561 and arXiv:2407.03309; the last 8982
  characters of arXiv:2411.11488.
- Read only through the fetch tool's summary, not by the auditor:
  arXiv:2206.07561, arXiv:2407.03309, arXiv:2411.11488, the DSpace record and
  the citation listings. Theorem numbers and quotations from those three papers
  in this section come from the summaries and should be checked against the
  papers before they are cited.
- Not done: the citing-paper list of arXiv:2411.11488 and of Graham–Lovász
  (1978); a second citation index; arXiv listing searches; any search in a
  language other than English; any search for the cone memberships used in the
  proof of T4 (Proposition S26, Lemma A) or for Laplacian-coefficient
  inequalities of the same shape.

### Recommendation for the registry (the auditor did not edit it)

For MD-0016, novelty at most `preliminary-search-completed`. Lemma S24 and
identity (1) should be presented as known facts with the citations above (after
the two bridging steps are reviewed), not as contributions. For Proposition S25
and Theorem T4 nothing here supports `no-prior-resolution-found`: the reference
databases were not searched and several of the most likely sources were not
read. An unsuccessful search does not establish originality.

## Primary sources read in session 11 (2026-11-26): Collins (1986) and Collins (1989)

Reader: the main session (Claude, model `claude-fable-5-2`), not a separate
auditor. The two documents had been refused to automated access in sessions 2
to 10; the director supplied them as local files for this session. They are
not in the repository.

| Document | File supplied | SHA-256 | What was read, and how |
| --- | --- | --- | --- |
| K. L. Collins, On a conjecture of Graham and Lovász about distance matrices, Discrete Appl. Math. 25 (1989) 27–35 | `1-s2.0-0166218X89900449-main.pdf`, 9 pages | `377d4ed79989013acbbc58ecd3d84c8569c464a0d6d4e0c391db63ab9fc7b5ed` | All nine pages, as page images (and the text layer). |
| K. L. Collins, Distance matrices of trees, Ph.D. thesis, MIT, May 1986 (supervisor R. P. Stanley) | `15748263-MIT.pdf`, 61 leaves, a scanned typescript | `bd07fb27fca80653608a8d01543e9ef3b6b9ab8c4764dcbaf924d51f6b2ade5c` | Page images: pp. 30–47 and 55–61 (the end of Section I with Theorem 2 and its examples, all of Sections II and III, the conjectures, the references, the list of notation, the conclusion). Text layer only (an OCR of the typescript, in which prose is legible and most displayed formulas are not): pp. 1–29 (front matter, Section 0, the proof of Theorems 1 and 2) and pp. 48–54 (Section IV). |

Limit of this reading: the displayed formulas of the proof of Theorem 2
(pp. 13–29) and of Section IV were not read reliably. Their statements
(Theorems 1, 2, 10 to 13, Lemmas 1 to 9) were. Exact checks of what was read
(scratch of session 11, exact arithmetic, a script `collins_check.py` that is
not stored in the repository): the star formula and the path formula of the
1989 paper against the distance matrix for orders 3 to 30; Table 1, row
`n = 9`; Theorem 4 of the thesis with leaf weight 1, and the dictionary
below, on the 142 pairs (tree of order 1 to 7, vertex). All agree.

### Collins (1989): contents

- Normalization (p. 29): `d_k = (−1)^{n−1} δ_k / 2^{n−k−2}`, `δ_k` the
  coefficient of `λ^k`. It is the `d_k` of the project.
- The Graham–Lovász conjecture as Collins states it (p. 29): "the sequence
  `d_1, d_2, …, d_{n−2}` is unimodal, with peak at `k = ½n`. This is true for
  stars, but not for paths. It is not known whether the sequence is unimodal
  (with varying peaks) for general trees."
- **Theorem 1** (p. 29): "The coefficients of CPD(S) where S is a star on n
  vertices are unimodal with peak at `⌊½n⌋`." Its proof gives (p. 30)
  `d_k = (n−k−1)(C(n−1, k) + 4 C(n−1, k−1))` and ends "the peak of
  unimodality occurs at `k = ½n`" for even `n` and "at `½(n−1)`" for odd `n`.
- **Theorem 3** (p. 30): "The coefficients of CPD(P) where P is a path on n
  vertices are unimodal with peak at `n(1 − 1/√5)`." The proof takes from the
  thesis the description of the coefficient of `λ^{n−k}` as a sum of
  principal minors, evaluates it by the theorem of Graham, Hoffman and Hosoya
  (Lemma 5), and obtains (p. 31) `d_{n−k} = C(n+k−1, 2k−1)(k−1) n/k`. The sign
  of `d_{n−k−1} − d_{n−k}` is that of `kn² − 5k³ − 2k² + 4k + 2`, which
  vanishes for `n/√5 < k + 1 < n/√5 + 1`; the proof ends (p. 33): "There must
  be some integer in this range, say `n/√5 < M < n/√5 + 1`, and `M` will be
  the peak of the unimodal sequence unless `M` is too close to `n/√5 + 1`. In
  that case, the peak of the sequence will be `M − 1`." In the index of `d`
  this places the peak of the path at `n − ⌈n/√5⌉ = ⌊n − n/√5⌋` or at
  `⌈n − n/√5⌉`. The last step is informal; the theorem as stated says only
  "peak at `n(1 − 1/√5)`".
- Table 1 (p. 34): the values `d_k` of the paths of order 2 to 9.
- Theorem 8: the analogous statement for the adjacency polynomial of a path.
- **Conjecture 9 (Peter Shor)**, p. 35, verbatim: "The coefficients of CPD(T)
  for any tree T with n vertices are unimodal with peak between `½n` and
  `n(1 − 1/√5)`." There is no floor and no ceiling, as arXiv:1507.02341 says.
- Conjecture 10 (p. 35; suggested by the referee, footnote 2): the relative
  position of the peak is the same for the adjacency polynomial.
- Nothing else about general trees. The paper has no formula in terms of the
  Laplacian, no Wiener index or transmission, no recursion on a leaf, and no
  bound on the peak of a general tree.

**On the wording of the conjecture.** For odd `n` the number `½n` is not an
integer, and the literal reading "peak `≥ n/2`" would mean peak `≥ (n+1)/2`.
That is false for the star by Theorem 1 of the same paper (peak at
`½(n−1)`). So the floor in the lower bound of arXiv:1507.02341 is the only
reading of Conjecture 9 consistent with its source; the ceiling in the upper
bound is consistent with the proof of Theorem 3. The catalogued statement
(Conjecture 1.2 of arXiv:1507.02341) is unchanged.

### Collins (1986): contents

Numbering as in the body of the thesis (its table of contents numbers the
theorems of Section III differently).

- Section I (pp. 12–31). Theorem 1 is the theorem of Graham and Lovász on
  the coefficients as counts of subforests; Theorem 2 is its extension to
  trees with weighted edges, proved by generalizing their proof (Lemma 5: the
  inverse of the weighted distance matrix; Lemma 6: the weighted determinant,
  from Graham–Hoffman–Hosoya). Examples (p. 31):
  `d_0 = (−1)^{n−1}2^{n−2}(n−1)`; `d_1 = (−1)^{n−1}2^{n−3}(4N_1 + 2N_2 + 4N_3 − 4)`
  (`N_1` pairs of disjoint edges, `N_2` paths with two edges, `N_3` edges);
  and for edge weights `x_i`,
  `δ_1 = (−1)^{n−1}2^{n−3} Π x_i {2(Σ x_i)(Σ 1/x_i) − Σ_i (d_i − 2)²}`.
- **Section II, "Isolation of a leaf" (pp. 32–38).** Its first sentence: "If
  we could isolate the contribution of a leaf of T to CP(Δ(T)), then we
  could inductively build up CP(Δ(T)) by peeling off one leaf of T at a
  time." Theorem 3: with the weight `x_1` of a leaf edge set to zero,
  `CP(Δ(T)) = −2λ CP(Δ(T_1)) − λ² CP(Δ(G_2))`, `T_1` the tree without the
  leaf and `G_2` the graph whose distance matrix is the principal submatrix
  without the leaf and its neighbour. **Theorem 4** (p. 34), with
  `S = (Δ(T) − λI)(1,1)` (the leaf deleted; `v_2` its neighbour, `M(i,j)` the
  matrix without row `i` and column `j`):
  `CP(Δ(T)) = −2λ det(S) − λ² det(S(2,2)) − 2x_1 [det(S) + λ Σ_j (−1)^{2+j} det(S(2,j))] − x_1² cof(S)`,
  and "From this we see exactly the contribution of `x_1`." Collins adds that
  the determinants in it "are no longer the determinants of subtrees of T,
  but instead can only be expressed in terms of the minors of D(T)". Theorem
  5 applies it to decide when two trees that differ by the position of one
  leaf are cospectral. There is no further use of Theorem 4.
- Section III (pp. 39–47). Theorem 6 is the theorem of Graham, Hoffman and
  Hosoya. **Theorem 7** (p. 40) is a formula for `CP(Δ(G))` when `G` is two
  graphs joined at a vertex, in terms of determinants and cofactors of
  `D(G_i) − λI` and of the matrices `M*`; it is stated without proof ("not
  enlightening"), and the printed formula has what looks like a misprint in
  one index. Theorem 8 (p. 41) is the coefficient of the path used in the
  1989 paper. Remark (p. 42): the coefficient of `λ` is
  `(−1)^{n−1}2^{n−3} Σ_v (−deg(v)² + deg(v)(n+3) − 4)`. Theorem 9: a formula
  for the coefficient of `λ` of a weighted tree.
- Section IV (pp. 48–54): factors of the characteristic polynomial coming
  from automorphisms; the full binary tree.
- Conjectures (p. 55). Conjecture 1: "The sequence `(1/2^{n−2})|d_0(T)|`,
  `(1/2^{n−3})|d_1(T)|`, … is unimodal, with the peak occuring at
  `(1/2^{n−⌊n/2⌋−2})|d_{⌊n/2⌋}(T)|` (due to R. L. Graham)." The others
  concern cospectrality, automorphisms and rational roots. The conjecture of
  Shor is not in the thesis.

### Comparison with the statements of the project

| Project item | What the two sources contain | Assessment |
| --- | --- | --- |
| Statement of CJ-0001 | Conjecture 9 of the 1989 paper, without floor or ceiling. | Source of the conjecture now read first-hand. The catalogued statement is unchanged. |
| S23(d): `ℓ_{S_n} = (1+x)^{n−2}[(n−1) + 4(n−2)x − 4x²]` and `d_{m−1}(S_n) < d_m(S_n)` | 1989, Theorem 1 and the formula in its proof. The two formulas agree: `(n−k−1)C(n−1,k) = (n−1)C(n−2,k)` and `(n−k−1)C(n−1,k−1) = (n−2)C(n−2,k−1) − C(n−2,k−2)`. | **Known** (Collins 1989). To be cited wherever the star is used, including Theorem T6(c). |
| L2: `d_1 = 2n² − 6 − Σ deg²` | Thesis, p. 31 and Remark p. 42 (each equal to L2 after `Σ deg = 2n − 2`). | **Known**, as already recorded (Graham–Lovász; the source). |
| S23(b), (c): the leaf recursion `ℓ_{T⁺} = (1+x)ℓ_T + r_u(T)` and its telescoped form | Thesis, Theorem 4: a recursion on a leaf for the same polynomial, in terms of minors of `D(T) − λI`. With leaf weight 1 and `λ = 2x`, exact dictionary (`n′` the order of `T`, `S = D(T) − 2xI`): `r_u(T) = xℓ_T + (−1)^{n′−1}2^{1−n′}[4x² adj(S)_{uu} + 4x(adj(S)1)_u + 1ᵀadj(S)1]`. | **A precursor exists and must be cited.** The idea of isolating a leaf and building the polynomial leaf by leaf, and an exact formula for it, are due to Collins (1986). Not in the thesis: the splitting with the factor `1 + x`; the remainder written through Laplacian minors (`Ψ_u`, `Ω_u`); that the remainder has non-negative coefficients (S29); the telescoped sum; any cone statement; any use for the peak. S23(b) is to be described as a Laplacian form of a known kind of identity, not as a new recursion. Passing from Theorem 4 to S23(b) needs the Graham–Lovász inverse and the computation of S15; it was not done by hand here, only checked exactly. |
| S19(d): the merge rule of the rooted state | Thesis, Theorem 7: a formula for two graphs joined at a vertex, in the language of the distance matrix, without proof. | **A precursor of the same kind**, to be cited for MD-0015. The printed formula was not verified (its notation is not recoverable with certainty from the scan). |
| S24 to S26, Theorem T4 (Wiener form; peak `≥ ⌊(n−1)/2⌋`) | Nothing. Neither source has the Wiener index, the transmissions, the minors off a path, or any bound on the peak of a general tree. | No prior statement in these two sources. They were named in session 10 as the first sources to read; this removes that specific doubt and no other. |
| Cones `C_d`, `K_d`; S28 to S30; Theorems T5, T6 and Proposition S36 of session 11 (statement (Γ_c¹), star minimality `ℓ_T − ℓ_{S_n} ∈ C_{n−1}`, the bound `⌊n/2⌋` for every tree, contraction of an edge) | Nothing. The only statements about the place of the peak are Theorem 1 (star), Theorem 3 (path) and the conjectures. | No prior statement in these two sources. |
| Hypothesis A(ii) and the upper half | 1989, Theorem 3 with the closed formula of the path. | The path is now first-hand: `d_{n−k}(P_n) = C(n+k−1, 2k−1)(k−1)n/k`. The last step of the proof is informal, so the exact peak of `P_n` should be taken from the formula, not from the sentence. |

### What this reading does and does not establish

- It establishes what these two documents contain, within the limit stated
  above (the formulas of pp. 13–29 and 48–54 of the thesis were read through
  OCR only).
- It does not establish originality of anything. Still not searched:
  MathSciNet, zbMATH, Google Scholar; still not read: Graham–Lovász (1978)
  pp. 72–88, Merris (1990), Moon (1995), Collins (1993) beyond the manuscript
  read in session 6, and the papers citing Collins (1989), which were seen by
  title only. When this section was written no search had been made for the
  statements of session 11 (Theorems T5 and T6, Proposition S36); the audit
  in the next section made a first one.

### Recommendation for the registry

Novelty stays `preliminary-search-completed` for MD-0016 and for the record
of session 11. S23(d) is recorded as known (Collins 1989). The records that
contain S23 (MD-0017) and S19 (MD-0015) name Theorems 4 and 7 of the thesis
as prior related work.

## Audit for session 11 (2026-11-26): the lower bound for every tree, star minimality, contraction of an edge

Auditor: literature-auditor subagent, model `claude-fable-5-2`. Budget stated
by the director: about 15 minutes of wall-clock time and at most 30 web
requests (searches and fetches together). Used: 30 web requests (11 web
searches; 19 page fetches, of which 3 returned HTTP 400 or 503 and 2 returned
undecoded PDF bytes that were then read as page images from the saved copy),
plus local reads and one edit of this dossier. Wall-clock time was not measured
by the auditor. **The search stopped because the budget of web requests was
spent, not because the leads were exhausted.** This is the FIRST prior-art
search for the statements of session 11. Novelty of all of them is not
established by this audit.

The statements audited are those of
`research/active/CJ-0001-collins-shor-peak/notes/lower-bound.md` (Theorem T5,
Theorem T6 and Proposition S36 read; their proofs were not checked, as
instructed). The queries of the audits for sessions 9 and 10 were not repeated
verbatim.

### Items

- (a) Theorem T6(c): for every tree of order `n ≥ 3`,
  `d_{⌊n/2⌋−1} < d_{⌊n/2⌋}` (peak at least `⌊n/2⌋`, the lower half of the
  Collins–Shor conjecture); more generally, any proof, claim or refutation of
  the conjecture or of one of its halves since 2015.
- (b) Theorem T6(b): `d_k(T) ≥ d_k(S_n)` for every `k` (the star minimizes
  every normalized coefficient), in the stronger form
  `ℓ_T − ℓ_{S_n} ∈ C_{n−1}`; or the path as maximizer; any extremal-tree result
  for the coefficients of the distance characteristic polynomial.
- (c) Proposition S36, the inequality: `d_k(T) ≥ d_k(T′)` when `T′` is obtained
  from `T` by contracting a non-pendant edge and attaching a pendant vertex at
  the contracted vertex.
- (d) Proposition S36, the formula
  `ℓ_T − ℓ_{T′} = H_A E_B + H_B E_A + x(2+5x) H_A H_B + 2 G_A G_B / x`; or any
  gamma-positivity or half-gamma expansion for distance characteristic
  polynomials of trees.

### Queries (verbatim, general web search tool, standard mode)

1. `"distance characteristic polynomial" tree coefficients peak "Collins" "Shor" conjecture proof OR proved OR "lower bound" 2025 OR 2026`
2. `"distance matrix" tree "characteristic polynomial" coefficients "generalized tree shift" OR "Kelmans transformation" OR "KC-transformation" OR "π-transform" monotone decrease`
3. `Csikvári "On a poset of trees" generalized tree shift theorem "characteristic polynomial" coefficients "Laplacian" star path extremal statement`
4. `Mohar "On the Laplacian coefficients of acyclic graphs" π transformation σ transformation theorem "Laplacian coefficients" decrease star path`
5. `"distance matrix" trees "coefficients" "characteristic polynomial" "star" minimal "path" maximal "edge contraction" OR "contracting an edge" OR "pendant" transformation coefficientwise`
6. `Csikvári "On a poset of trees II" abstract "generalized tree shift" "distance" OR "Wiener" "characteristic polynomial" Journal of Graph Theory 2013`
7. `"distance spectral radius" trees transformation "star" minimum "path" maximum "edge" contraction OR "grafting" Stevanović Ilić OR "Ruzieh" "Powers" distance matrix tree characteristic polynomial coefficients comparison`
8. `"distance matrix" tree "characteristic polynomial" "gamma-positive" OR "γ-positive" OR "gamma-positivity" OR "(1+x)^" expansion coefficients unimodal "Graham" "Lovász"`
9. `mathoverflow "distance matrix" tree "characteristic polynomial" coefficients unimodal peak "Graham" "Lovász" OR "Collins" conjecture`
10. `"formal-conjectures" OR "Mathlib" "distance matrix" tree "Graham" "Lovász" unimodal coefficients Lean formalization`
11. `"distance matrix" tree "characteristic polynomial" coefficients monotone "GTS" OR "tree shift" OR "poset on trees" Sivasubramanian OR Nagar OR Csikvári "Graham" "Lovász"`

Each query returned about ten links and a machine-written summary. Text taken
from those summaries is called a "snippet" below and is not a quotation from a
paper. **Warning about two snippets.** The summaries of queries 9 and 11 say
that Theorem 2.1 of arXiv:1507.02341 "places the peak between ⌊n/2⌋ and
⌈n − n/√5⌉" and that the Collins–Shor statement "is the one that gets proved
in its bounds". These are machine-written conflations of the conjecture with
the theorem. They contradict the earlier readings recorded in this dossier
(Theorem 2.1 there is the log-concavity theorem; the peak location is left
open) and the abstract page fetched in this session, which per the tool says
nothing about the location of the peak. They are not evidence of a prior
proof. The summary of query 10 places the statement on "page 83 of Graham and
Lovász's paper" and attributes it there to Collins and Shor, which is
impossible for a 1978 paper; also disregarded.

### URLs fetched and what was actually read

"Page images" means that the fetch tool saved the PDF and the auditor read the
named pages as images, directly. "Tool summary" means that the auditor saw only
the fetch tool's machine-written answer about the page, not the page itself.

| URL | Outcome |
| --- | --- |
| `https://users.fmf.uni-lj.si/mohar/Reprints/2007/BM07_LAA422_Mohar_LaplacianCoefficient.pdf` (B. Mohar, "On the Laplacian coefficients of acyclic graphs"; the file is the preprint, Univ. of Ljubljana Preprint series Vol. 44 (2006), 1023, dated 20 November 2006) | Page images, all 8 pages (cover and pp. 1–7: the whole preprint). The journal version (Linear Algebra Appl. 422 (2007) 736–741, reference as given in Csikvári's bibliography) was NOT opened; the theorem numbers below are those of the preprint. |
| `http://real.mtak.hu/14003/1/poset_treesIIV2.pdf` (P. Csikvári, "On a poset of trees II", author's accepted version, 21 pages; journal: J. Graph Theory 74 (2013) 81–103, DOI `10.1002/jgt.21693`, per the repository record) | Page images, pp. 1–11 and 19–21 (abstract, Sections 1 to 6, Section 7 up to the proof of Lemma 7.6, the end of Section 9, Sections 10 and 11, the references). Pages 12–18 (the rest of Section 7, Sections 8 and 9: Laplacian eigenvalues, independence polynomial, edge cover polynomial) NOT read. |
| `https://real.mtak.hu/14003/` | Tool summary of the repository record (bibliographic data; no abstract on the page). |
| `https://arxiv.org/html/2405.09027v2` (C. Ding, "Csikvári's poset and Tutte polynomial") | Tool summary of the full text. |
| `https://arxiv.org/abs/1711.09787` (M. K. Nagar, "Eigenvalue monotonicity of q-Laplacians of trees along a poset"; Linear Algebra Appl. 571 (2019) 110–131 per the page) | Tool summary of the abstract page. |
| `https://arxiv.org/abs/2306.05155` (I. Mahato, M. R. Kannan, "A note on the distance and distance signless Laplacian spectral radius of complements of trees"; one version, 8 June 2023) | Tool summary of the abstract page. |
| `https://arxiv.org/abs/1507.02341v3` | Tool summary of the abstract page: v1 9 July 2015, v2 14 July 2015, v3 20 April 2017; per the tool the abstract states unimodality and log-concavity and "does not state where the peak lies". |
| `https://arxiv.org/search/?query=%22distance+matrix%22+tree+coefficients+unimodal+peak&searchtype=all&abstracts=show&order=-announced_date_first&size=50` | Tool listing: "Showing 1–1 of 1 results": arXiv:2407.03309. |
| `https://arxiv.org/search/?query=%22Graham%22+%22Lov%C3%A1sz%22+distance+tree+polynomial+coefficients&searchtype=all&abstracts=show&order=-announced_date_first&size=50` | Tool listing: "Showing 1–3 of 3 results": arXiv:2411.11488, 2206.07561, 1507.02341. |
| `https://arxiv.org/search/?query=%22distance+matrix%22+tree+%22characteristic+polynomial%22+coefficients&searchtype=all&abstracts=show&order=-announced_date_first&size=50` | Tool listing: "Showing 1–2 of 2 results": arXiv:2411.11488, 2407.03309. |
| `https://arxiv.org/search/?query=%22generalized+tree+shift%22&searchtype=all&abstracts=show&order=-announced_date_first&size=50` | Tool listing: "Showing 1–5 of 5 results": arXiv:2610.17078 ("Sustainable trees", Bencs, van Dijk, Guo, 12 October 2026; adjacency spectral radius only, per the tool), 2306.05155, 1912.03101, 1711.09787, 1710.02416. |
| `https://arxiv.org/search/?query=%22GTS+poset%22+OR+%22Csikv%C3%A1ri+poset%22+OR+%22poset+of+trees%22&searchtype=all&abstracts=show&order=-announced_date_first&size=50` | Tool listing: "Showing 1–8 of 8 results"; per the tool none of the eight abstracts mentions a distance matrix, a distance polynomial or a distance spectral radius (relevant entries: arXiv:2405.09027, 1912.03101, 1710.02416; the other five are on unrelated subjects). |
| `https://api.semanticscholar.org/graph/v1/paper/arXiv:1507.02341/citations?fields=title,year,externalIds&limit=100` | Tool listing: 5 citing papers, the same five as in sessions 2, 5 and 9. |
| `https://api.openalex.org/works?search=Proof%20of%20a%20conjecture%20of%20Graham%20and%20Lov%C3%A1sz%20concerning%20unimodality%20of%20coefficients%20of%20the%20distance%20characteristic%20polynomial%20of%20a%20tree&select=id,doi,title,publication_year,cited_by_count&per-page=5` | Tool listing: the paper is OpenAlex `W1528479167`, DOI `10.13001/1081-3810.3493`, year 2018, cited-by count 8. |
| `https://api.openalex.org/works?filter=cites:W1528479167&select=id,doi,title,publication_year&per-page=50` | Tool listing (a second citation index, used for the first time in this dossier): `meta.count` 7. The five papers above, with arXiv:2206.07561 counted twice (preprint and journal), and one more: "Discrete Mathematics Days 2022" (DOI `10.22429/euc2022.016`, a proceedings volume; NOT opened). |
| `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/jgt.21693/citations?fields=title,year,externalIds&limit=200` (papers citing Csikvári, "On a poset of trees II") | Tool listing: 24 citing papers, titles only. Two have "distance" in the title: arXiv:2306.05155 and "The 2-Steiner distance matrix of a tree" (2022, DOI `10.1016/j.laa.2022.09.007`; NOT opened). None has "Graham", "unimodal", "Wiener" or "transmission" in the title. |
| `https://api.openalex.org/works?filter=cites:doi:10.1002/jgt.22244&per-page=100&select=title,publication_year,doi,id` | HTTP 400. The DOI was the auditor's guess and is wrong (the paper is in Electron. J. Linear Algebra, not J. Graph Theory); replaced by the two OpenAlex rows above. |
| `https://emis.dsd.sztaki.hu/journals/ELA/ela-articles/articles/vol20_pp168-179.pdf` and `https://emis.dsd.sztaki.hu/journals/ELA/ela-articles/abstracts/abs_vol20_pp168-179.pdf` (by the snippet of query 7: Stevanović, Ilić, on the distance spectral radius of trees, Electron. J. Linear Algebra 20, pp. 168–179) | HTTP 503, both. NOT read. |

### Findings per item (within this coverage only)

**(a) The lower bound `⌊n/2⌋` for every tree; either half of the conjecture —
nothing found within this coverage (originality NOT established).** No paper,
preprint, thesis or talk was found that proves, claims or refutes the
Collins–Shor conjecture or one of its halves for all trees or for a large class
of trees.

- Three arXiv listing searches with new phrasings return only papers already
  in this dossier (arXiv:1507.02341, 2206.07561, 2407.03309, 2411.11488); the
  latest is 2411.11488 (v2 of 10 December 2025), which per session 10 does not
  concern the peak.
- Two citation indexes for arXiv:1507.02341: Semantic Scholar lists the same
  five citing papers as before; OpenAlex lists seven records, which are those
  five (one counted twice) and the proceedings volume "Discrete Mathematics
  Days 2022" (not opened; by its date it would at most contain an abstract
  related to arXiv:2206.07561 — a guess, not checked).
- Queries 1, 5, 8, 9 and 11 returned no source dated 2025 or 2026 on the
  question. Their summaries restate the open status as of arXiv:1507.02341 and
  arXiv:2407.03309. See the warning above about the two conflating snippets.
- Statement T6(c) for the star alone is Collins (1989), Theorem 1 (read
  first-hand in session 11, section above); T6(c) for odd `n` coincides with
  the project's own Theorem T4 (session 10 audit).

**(b) Star minimality for every coefficient — nothing found for the distance
characteristic polynomial; exact analogues exist for the Laplacian and the
adjacency polynomial (found closely related prior work).** No source was found
stating that the star minimizes, or the path maximizes, every coefficient (or
every normalized coefficient) of the distance characteristic polynomial among
trees of order `n`, in any order (coefficientwise or in a cone). Related work,
read directly unless marked otherwise:

- Zhou–Gutman, as stated in Mohar's preprint, equation (2), p. 2:
  `c_k(S_n) ≤ c_k(T) ≤ c_k(P_n)`, `0 ≤ k ≤ n`, "for all trees `T` of order
  `n`", where `Λ(G, λ) = Σ_k (−1)^k c_k λ^{n−k}` is the Laplacian
  characteristic polynomial; it rests on their identity (1),
  `c_k(T) = m_k(S(T))` (`k`-matchings of the subdivision graph). Mohar's
  reference [10] for it is "to appear in Lin. Multilin. Algebra"; Csikvári's
  reference [2] gives Linear Multilinear Algebra 56 (2008) 305–310. The
  Zhou–Gutman paper itself was NOT opened.
- Csikvári II, Corollary 7.4 (p. 10): `a_k(P_n) ≥ a_k(T) ≥ a_k(S_n)` for any
  tree `T` on `n` vertices and `k = 1, …, n−1`, with
  `L(G, x) = Σ_k (−1)^{n−k} a_k(G) x^k`; Remark 7.5: "All parts of Corollary
  7.4 are known", the coefficient statement conjectured by Gutman–Pavlović
  (Bull. Acad. Serbe Sci. Arts 127 (2003) 31–40) and proved by Zhou–Gutman, "A
  different proof was given by B. Mohar [20] using graph transformations."
- Distance spectral radius (a different invariant: the largest root, not the
  coefficients), snippet of query 7 only: among trees of order `n` the star
  has the minimum and the path the maximum distance spectral radius
  (attributed in the snippet to Stevanović–Ilić and to Subhi–Powers), proved
  with "a transformation that strictly increases the distance spectral radius
  of a tree". The paper returned HTTP 503 and was not read.
- Auditor's remark, not checked: the project's `Φ_T = det(I + xL)` has the
  Laplacian coefficients `c_k(T)` as its coefficients, so `Φ_T − Φ_{S_n} ≥ 0`
  coefficientwise is the Zhou–Gutman theorem. `ℓ_T` is not `Φ_T` (L1 subtracts
  `x τᵀ adj(I + xL) τ`), so T6(b) does not follow from it by anything read
  here; but any write-up of T6(b) should present it as the distance analogue
  of the Zhou–Gutman–Mohar–Csikvári theorem and cite those papers.

**(c) Monotonicity under contracting a non-pendant edge and adding a pendant
vertex — the OPERATION is known under several names (found prior work on the
operation); its effect on the coefficients of the distance characteristic
polynomial was not found (nothing found within this coverage).**

*Identification of the operation.* Csikvári II, Definition 2.1 (p. 3),
verbatim: "Let `T` be a tree and `x` and `y` be vertices such that all the
interior points of the path `xPy` (if they exist) have degree 2 in `T`. The
generalized tree shift (GTS) of `T` is the tree `T′` obtained from `T` as
follows: let `z` be the neighbor of `y` lying on the path `xPy`, let us erase
all the edges between `y` and `N(y)∖{z}` and add the edges between `x` and
`N(y)∖{z}`." And: "if `x` or `y` is a leaf in `T` then `T′ ≅ T`, otherwise the
number of leaves in `T′` is the number of leaves in `T` plus one. In this
latter case we call the generalized tree shift proper." Bridging step, written
by the auditor and unreviewed: for adjacent `x, y` (a path with `k = 2`
vertices, `z = x`) the shift moves every neighbour of `y` other than `x` to
`x` and leaves `y` as a leaf at `x`; that is the tree obtained by contracting
the edge `xy` and attaching one pendant vertex at the contracted vertex, and
it is proper exactly when `xy` is a non-pendant edge. **So the operation of
Proposition S36 is the proper generalized tree shift of Csikvári with `k = 2`.**
Section 10 of the same paper (pp. 19–20, read directly) names its relatives:

- "The σ-transformation is the generalized tree shift when `H_2` is a star and
  `k = 2` (so the path has no interior vertices)"; "the inverse of
  π-transformation is nothing else than the generalized tree shift when `H_2`
  itself is a path." So, among Mohar's two operations, the one that S36
  generalizes is **σ, not π** (the task description named π).
- J.-M. Guo's transformation "separating an edge" (his reference [12]: Linear
  Algebra Appl. 433 (2010) 1148–1153, NOT opened) "is the generalized tree
  shift applied to adjacent vertices `x, y`" — that is, exactly the operation
  of S36, defined there for every graph.
- "Originally, the author developed the generalized tree shift to overcome a
  certain weakness of the Kelmans transformation." Auditor's recollection, not
  read in any source this session: for adjacent vertices of a tree the Kelmans
  transformation coincides with the `k = 2` shift. Unverified.
- Mohar's preprint, Section 3 (p. 4–5), read directly: for `u_0` of degree
  `p + 1` whose neighbours `u_1, …, u_p` are leaves and whose remaining
  neighbour is `v_0`, `T′ = σ(T, u_0)` is formed "by removing the edges
  `u_0u_1, … u_0u_p` from `T` and adding `p` new pendant edges
  `v_0v_1, … v_0v_p` incident with `v_0`"; Proposition 3.1: "every tree can be
  transformed into a star by a sequence of σ-transformations." This is the
  scheme of Remark 2 after S36 (repeat the operation until the star).

*Known monotonicity theorems for this operation, other matrices* (all read
directly):

- Mohar, Theorem 3.2 (preprint p. 5): for `T′ = σ(T, u_0)`, with `n_d` the
  number of vertices of `T − u_0` at distance `d` from `u_0`,
  `c_k(T) ≥ c_k(T′) + Σ_{d=2}^{k} n_d p C(n−2−d, k−d)` for `2 ≤ k ≤ n−2`, and
  `c_k(T) = c_k(T′)` for `k ∈ {0, 1, n−1, n}`. Theorem 2.2 (p. 3): for a
  π-transform `T′ = π(T, u_0, P, Q)`, with `n_d` the number of vertices of
  `T − P − Q` at distance `d` from `u_0`,
  `c_k(T) ≤ c_k(T′) − Σ_{d=1}^{k−1} n_d C(n−3−d, k−1−d)` for `2 ≤ k ≤ n−2`,
  with the same equalities. Theorem 4.1 (p. 6), using `c_{n−2}(T) = W(T)`:
  `W(T′) − W(T) = pq(n−p−q)` for π (`p = |P| − 1`, `q = |Q| − 1`) and
  `W(T) − W(T″) = r(n−r−1)` for σ (`r = deg_T(u_0) − 1`).
- Csikvári II, Theorem 6.1 (p. 8): "The generalized tree shift decreases the
  coefficients of the characteristic polynomial in absolute value, i.e., if
  the tree `T′` is obtained from the tree `T` by some generalized tree shift
  then `φ(T, x) ≫ φ(T′, x)`" (adjacency matrix; `≫` is the coefficientwise
  comparison of absolute values, p. 3). Theorem 7.3 (p. 10): "The generalized
  tree shift decreases the coefficients of the Laplacian polynomial in
  absolute value, i.e., if `T′` is obtained from `T` by a generalized tree
  shift then `L(T, x) ≫ L(T′, x)` or in other words `a_k(T) ≥ a_k(T′)` for
  `k = 1, …, n−1`. Furthermore, `θ(T′) ≥ θ(T)` and `a(T′) ≥ a(T)`." Theorem
  3.1 (p. 5): "The generalized tree shift increases the spectral radius of the
  tree." Theorem 2.5 (p. 4, attributed to Csikvári's first paper, Combinatorica
  30 (2010) 125–137, NOT opened): "Every tree different from the path is the
  image of some proper generalized tree shift, i.e., the only minimal element
  of the poset is the path."
- The table of Section 11 (p. 20) lists ten parameters monotone along the
  shift (adjacency and Laplacian eigenvalues and coefficients, closed walks
  and walks of fixed length, algebraic connectivity, independence polynomial,
  edge cover polynomial). **No parameter of the distance matrix is in the
  table**, and in the pages read the distance matrix does not occur (the
  Wiener index is mentioned once, in the introduction, as an example of star
  and path extremality; the `D(G)` of that paper is the degree matrix).

*For the distance matrix*, what was found is about spectral radii, not about
coefficients, and through tool summaries or snippets only:

- arXiv:2306.05155 (abstract, tool summary): the generalized tree shift does
  not decrease the distance spectral radius, the distance signless Laplacian
  spectral radius and the `D_α`-spectral radius of **complements of trees**.
  Snippet of query 7: Lin and Drury on the Kelmans transformation and the
  distance spectral radius of complements of trees (not opened).
- arXiv:1711.09787 (abstract, tool summary): eigenvalue monotonicity of
  `q`-Laplacians of trees along the poset, with corollaries for "exponential
  distance matrices of trees" (a different matrix).
- Stevanović–Ilić (snippet only; HTTP 503): a transformation increasing the
  distance spectral radius of a tree.
- "The 2-Steiner distance matrix of a tree" (2022) cites Csikvári II (title
  seen in the citation list only). **Unread lead**: it may contain a
  monotonicity statement along the shift for a distance-type matrix.

No statement that the coefficients of the distance characteristic polynomial
of a tree are monotone under this operation, under the general shift, or under
Mohar's σ or π, was found.

**(d) An explicit formula for `ℓ_T − ℓ_{T′}`; gamma-positivity — nothing found
for the distance characteristic polynomial; product formulas of the same kind
exist for the adjacency and Laplacian polynomials (found closely related prior
work).** Read directly in Csikvári II:

- Theorem 5.1 ("General lemma", pp. 6–8): if graph polynomials `f` and `g`
  satisfy
  `f(M_1 : M_2) = c_1 f(M_1) f(M_2) + c_2 f(M_1) g(M_2|u_2) + c_2 g(M_1|u_1) f(M_2) + c_3 g(M_1|u_1) g(M_2|u_2)`
  for the graph `M_1 : M_2` obtained by identifying `u_1` with `u_2`
  (`c_1, c_2, c_3` rational functions of `x`) and
  `c_2 f(K_2) + c_3 g(K_2|1) ≠ 0`, then
  `f(T) − f(T′) = c_4 (c_2 f(P_k) + c_3 g(P_k|1)) (c_2 f(H_1) + c_3 g(H_1|1)) (c_2 f(H_2) + c_3 g(H_2|k))`
  with `c_4 = (g(P_3|1) − g(P_3|2)) / (c_2 f(K_2) + c_3 g(K_2|1))²`.
- Lemma 6.4 (p. 8), adjacency:
  `φ(T, x) − φ(T′, x) = φ(P_{k−2}, x)(φ(H_1, x) − xφ(H_1 − {1}, x))(φ(H_2, x) − xφ(H_2 − {1}, x))`.
- Lemma 7.6 (p. 10), Laplacian:
  `L(T, x) − L(T′, x) = (1/x) L(P_{k−1}, x)(L(H_1, x) − xL(H_1|1, x))(L(H_2, x) − xL(H_2|k, x))`,
  from the 1-sum formula of Lemma 7.7.

Auditor's remark, not checked: the General Lemma needs a 1-sum recursion in
one polynomial `f` and one auxiliary polynomial `g`. The project's merge rule
(S19(d)) carries a state with five components, and the formula of S36 is a sum
of four products, not one product; so S36 is not an instance of Theorem 5.1 as
stated. The method of S36 (difference of two 1-sum expansions, then a
positivity argument on the factors) is the method of Csikvári's Section 4, and
should be described as such. For Collins's unproved 1-sum formula for the
distance polynomial (thesis, Theorem 7) see the section above.

Gamma-positivity: query 8 returned nothing on an expansion of a distance
characteristic polynomial of a tree in a basis `x^e (1+x)^i`, as in the audit
for session 9.

### What would threaten the originality of the session-11 statements

- **The operation of S36 is not new** and must not be presented as such: it is
  the proper generalized tree shift with `k = 2` (Csikvári 2010, 2013), Guo's
  "separating an edge" (2010), and a generalization of Mohar's σ (2007). The
  proof scheme "each step lowers the polynomial and every tree reaches the
  star" is Mohar's and Csikvári's. What was not found is the result for the
  distance characteristic polynomial.
- For (b) and (c): a statement may exist in a place this audit did not reach —
  the 2-Steiner paper that cites Csikvári II, "On a poset of trees revisited"
  (2021, title only), Csikvári's first paper, Guo (2010), the
  distance-spectral-radius literature on trees (Stevanović–Ilić and its citing
  papers), and the journals of mathematical chemistry, where extremal results
  for tree invariants are common and which the general web search covers
  poorly.
- For (a): the same limits as in the audits for sessions 9 and 10. A paper
  that cites none of arXiv:1507.02341, arXiv:2206.07561 and Collins (1989), or
  one that neither arXiv's metadata search nor the two citation indexes list,
  would have been missed.
- A question this audit raises and does not answer: whether the monotonicity
  of S36 extends to the generalized tree shift with `k ≥ 3`. With Csikvári's
  Theorem 2.5 that would make the path the coefficientwise maximum. No source
  was found for or against it; nothing is claimed here.

### Not searched or not accessible

- MathSciNet, zbMATH, Google Scholar: not available to the tool; not searched.
- MathOverflow: one general web query naming it (query 9), which returned no
  MathOverflow page; no search on the site itself. OEIS, erdosproblems.com,
  Open Problem Garden: not searched.
- Formal libraries: one general web query (query 10), which returned nothing
  about Lean, Mathlib or formal-conjectures; the repositories themselves were
  not searched.
- Located and not read: Csikvári, "On a poset of trees" (Combinatorica 30
  (2010) 125–137); Csikvári II, pp. 12–18; the journal version of Mohar
  (2007); Zhou–Gutman (2008); Gutman–Pavlović (2003); Guo (2010);
  Stevanović–Ilić (HTTP 503) and Subhi–Powers; Lin–Drury; "The 2-Steiner
  distance matrix of a tree" (2022); "On a poset of trees revisited" (2021);
  "Graph Polynomials and Graph Transformations in Algebraic Graph Theory"
  (2011, title only); "Discrete Mathematics Days 2022"; arXiv:2610.17078 and
  arXiv:2610.34114 (a title on the minimum distance spectral radius of trees
  with given maximum degree, in the result list of query 7) beyond a title or
  a tool summary; Ilić, arXiv:1104.4280.
- Read only through the fetch tool's summary, not by the auditor:
  arXiv:2405.09027, the abstract pages of arXiv:1711.09787, 2306.05155 and
  1507.02341, the arXiv listings and the citation listings. Statements
  attributed to them above should be checked against the papers before they
  are cited. Statements attributed to Mohar's preprint and to Csikvári II
  (pp. 1–11, 19–21) were read by the auditor on the page images.
- Not done: citing-paper lists of Mohar (2007), of Csikvári's first paper, of
  Zhou–Gutman and of Stevanović–Ilić; any search for the Kelmans
  transformation literature proper; any search for the intermediate statements
  (Lemma S32, Propositions S33 to S35, the polynomial `E`, statement (Γ_c¹));
  theses and talks beyond what queries 1 and 9 would surface; any language
  other than English.

### Recommendation for the registry (the auditor did not edit it)

For the record or records of session 11 (Theorems T5 and T6, Proposition S36):
novelty at most `preliminary-search-completed`. Nothing here supports
`no-prior-resolution-found`: the reference databases were not searched and
several of the most likely sources were not read. The record should name as
prior related work, with the statements quoted above: Collins (1989), Theorem
1, for the star; Zhou–Gutman (2008), Mohar (2007), Theorems 2.2 and 3.2, and
Csikvári (2013), Theorems 6.1 and 7.3 with Lemmas 6.4 and 7.6, for the
Laplacian and adjacency analogues of T6(b) and S36; Csikvári (2010, 2013),
Guo (2010) and Mohar (2007) for the operation itself. The operation of S36
should be called by its published name (generalized tree shift with `k = 2`).
An unsuccessful search does not establish originality.
