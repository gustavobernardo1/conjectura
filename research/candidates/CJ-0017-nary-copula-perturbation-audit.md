# CJ-0017 — Literature audit: Mesiar's Problem 4.1 (n-ary perturbation C − ∏(x_i − C))

*Audit run 2026-11-27 by the literature-auditor subagent (model claude-opus-5-5).
Budget: about 20 web operations and about 15 minutes. 21 web operations were used (list below).
This file records only sources that were opened, and says for each one whether the full text
or only an abstract, metadata or a search-engine snippet was seen.*

## Verdict

**No answer found within this coverage.** Within the sources listed below, no work
answers either question of Problem 4.1 for n ≥ 3. None restates the problem as open, and none
shows that C_1 fails to be a copula for the product copula in dimension n ≥ 3. The coverage is
narrow: two citation indexes (titles and summarised abstracts only), one forward-citation list
of the bivariate perturbation paper (titles only), four full texts (the primary source, two
perturbation papers and one Markov-chain paper) and several search-engine queries. Three
leads that may be relevant could not be opened (section 4). They must be checked before the
open status of the n ≥ 3 case is relied on. This verdict does not establish that any result of
the project is new.

## 1. Primary source: wording and number confirmed

- R. Mesiar, A. Stupňanová, "Open problems from the 12th International Conference on Fuzzy Set
  Theory and Its Applications", Fuzzy Sets and Systems 261 (2015) 112–123,
  doi:10.1016/j.fss.2014.07.012. Author copy:
  http://library.utia.cas.cz/separaty/2019/E/mesiar-0506948.pdf (accessed 2026-11-27). The
  copy uses the journal layout, and pages 112–117 were read as page images.
- Section 4, "Constructions of copulas", p. 114. Definition 4.1 (n ≥ 2 fixed; n-increasing
  through the volume V_C([x,y]) = Σ_{ε∈{−1,1}^n} C(z^(ε)) ∏ ε_i ≥ 0; boundary conditions
  (C2)). The dossier `CJ-0017-nary-copula-perturbation.md` transcribes it correctly.
- **Problem 4.1 (Mesiar)**, p. 114, matches the dossier: "Let C : [0,1]^n → [0,1] be an n-ary
  copula. Define C_1 : [0,1]^n → [0,1] by C_1(x_1,…,x_n) = C(x_1,…,x_n) − ∏_{i=1}^n (x_i −
  C(x_1,…,x_n)). (2) Is the function C_1 n-increasing, i.e., is it an n-copula? If in general
  not, characterize all n-copulas C such that C_1 is an n-copula, too."
- Context in the source, p. 114. Equation (1) is the bivariate family of [38]:
  C_λ(x,y) = C(x,y) + λ(x − C(x,y))(y − C(x,y)), λ ∈ [0,1], C ≠ Min. The text then says: "Our
  first open problem concerns the possibility of extending the construction (1) to higher
  dimension." After the problem: "Observe that if, for a given n-copula C, C_1 given by (2) is
  n-copula, then also C_λ … = C(x_1,…,x_n) − λ ∏_{i=1}^n (x_i − C(x_1,…,x_n)) is an n-copula."
- Problem 4.2 (Mesiar), p. 115, is a different bivariate problem: C^(λ) = C/(1 + λ − λC*).

### Statement remark (auditor's hand calculation, not checked by any program, not a literature finding)

Equation (2) has a minus sign, and equation (1) has a plus sign with λ ∈ [0,1]. For n = 2,
equation (2) therefore gives λ = −1 in (1), not λ = 1. Read literally, Definition 4.1 allows
n = 2. Take C = W, W(x,y) = max(x + y − 1, 0). For x + y < 1, C_1(x,y) = 0 − x·y = −xy < 0. For
example, V_{C_1}([0,1/2]^2) = C_1(1/2,1/2) = −1/4. So under the literal reading, the first
question already has the answer "no" at n = 2, and the stated codomain [0,1] fails. The
substantive content is then the characterisation, together with the case n ≥ 3, where the
project's product-copula example applies.

This is a reading of the source, not a correction of it. Whether the authors meant the sign
to depend on n is not stated on pp. 114–115. Under rule 3 of AGENTS.md, the project should
record which reading it works on.

## 2. Citing works of the 2015 paper

- **OpenAlex.** W-id W2036212222. Query:
  https://api.openalex.org/works?filter=cites:W2036212222&per-page=100 (accessed 2026-11-27),
  32 works.
  - Copula-related titles: "A Collection of Two-Dimensional Copulas Based on an Original
    Parametric Ratio Scheme" (Symmetry 2023), "On the Ratio-Type Family of Copulas"
    (Mathematics 2024) and "A Characterization of a Subclass of Separate Ratio-Type Copulas"
    (2025). All three are bivariate by title. They plausibly relate to Problem 4.2, but this
    was not checked.
  - The other titles concern fuzzy implications, seminormed fuzzy integrals (Problems
    9.x), fuzzy partitions (Holčapek's problem), effect algebras, t-subnorms and applications.
  - No title concerns n-ary copulas or perturbations in dimension n ≥ 3.
- **Semantic Scholar.**
  https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.fss.2014.07.012/citations?fields=title,year,abstract&limit=100
  (accessed 2026-11-27), 30 works. Titles and abstracts were screened through the fetch tool's
  summariser, not read in full.
  - Works not in the OpenAlex list: "Mutually exchangeable fuzzy implications" (2015), "An
    answer to an open problem on seminormed fuzzy integral" (2015, Problem 9.3), and
    **"Solution to an open problem about a transformation on the space of copulas"** (2014).
    Its abstract: "We solve a recent open problem about a new transformation mapping the set
    of copulas into itself."
  - No abstract in the list mentions n-dimensional perturbations or Problem 4.1.
- **"Solution to an open problem about a transformation on the space of copulas".** F. Durante,
  J. Fernández-Sánchez, W. Trutschnig, Dependence Modeling 2(1) (2014) 1–8,
  doi:10.2478/demo-2014-0005. Only the abstract was seen, at
  https://ideas.repec.org/a/vrs/demode/v2y2014i1p8n5.html (accessed 2026-11-27). The abstract
  does not say which open problem is solved or in which dimension. **Not resolved by this
  audit.** It is more likely Problem 4.2 or another bivariate transformation, but that is a
  guess and is not recorded as a finding.

## 3. Perturbation-of-copulas literature

- **Forward citations of Mesiar–Komorníková–Komorník, "Perturbation of bivariate copulas".**
  Fuzzy Sets Syst. 268 (2015) 127–140, doi:10.1016/j.fss.2014.04.016, OpenAlex W2015941533.
  Query: https://api.openalex.org/works?filter=cites:W2015941533&per-page=100 (accessed
  2026-11-27), 27 works, titles only. Relevant titles:
  - Komorník, Komorníková, Kalická, "Dependence measures for perturbations of copulas", FSS
    2017, doi:10.1016/j.fss.2017.01.014. Not opened (not open access per OpenAlex; no abstract
    in OpenAlex).
  - "Families of Perturbation Copulas Generalizing the FGM Family and Their Relations to
    Dependence Measures", AGOP 2017, doi:10.1007/978-3-319-59306-7_6. Not opened. A search
    snippet says that it extends a class of perturbations of an arbitrary copula to
    parameters in [−1,0]. Under the literal sign of (2), this is the n = 2 case of Problem 4.1
    (see the remark in section 1). **This is a lead, not a verified finding.**
  - **J. Fernández-Sánchez, M. Úbeda-Flores, "Solution to two open problems on perturbations
    of the product copula"**, FSS, doi:10.1016/j.fss.2018.06.013 (OpenAlex year 2018; a search
    summary says 2019). Not opened: the Bohrium listing page was blocked by a bot check, and
    OpenAlex has no abstract. A search-engine summary of that listing (snippet only, not seen
    by the auditor) says the paper treats open questions on perturbations of the product
    copula and "also extend[s] the discussion to higher dimensions". OpenAlex does not list
    the 2015 open-problems paper among its references, and OpenAlex reference lists can be
    incomplete. **Highest-priority unchecked lead.**
  - X. Zhu, T. Wang, V. Pipitpojanakarn, "Constructions of Multivariate Copulas", in
    *Robustness in Econometrics*, Studies in Computational Intelligence 692 (2017),
    doi:10.1007/978-3-319-50742-2_15. Not opened. A search snippet says it studies
    perturbations C = C* + H of an n-copula C*, with conditions on H for groundedness, uniform
    margins and n-increasingness. Whether it treats H = −λ∏(x_i − C) is unknown.
  - "The impact on the properties of the EFGM copulas when extending this family" (FSS 2020,
    doi:10.1016/j.fss.2020.11.001); "Parameterized transformations and truncation: When is
    the result a copula?" (J. Comput. Appl. Math. 2023, doi:10.1016/j.cam.2023.115340); "A
    Procedure of Perturbation Leading to a New Class of Asymmetric Copulas" (Mathematics 2026,
    doi:10.3390/math14071093); "On comprehensive families of copulas involving the three basic
    copulas and transformations thereof" (Dependence Modeling 2024). **None of these was
    opened.**
  - The other titles are bivariate (by title), shock or maxmin models, or Markov-chain mixing.
- **Mesiar, Sheikhi, Komorníková, "Random noise and perturbation of copulas".** Kybernetika
  55(2) (2019) 422–434, doi:10.14736/kyb-2019-2-422. **Full text read** (pp. 422–423 and
  432–434) from https://www.kybernetika.cz/content/2019/2/422/paper.pdf, accessed 2026-11-27.
  - The paper studies the copula of (X + Z, Y) for noise Z, which is a different perturbation
    mechanism.
  - p. 423: "In this paper, we consider only binary copulas".
  - Concluding remarks, p. 433: "in the next study the general case of n–dimensional random
    vectors affected by noise should be considered."
  - Its 8 references include neither the 2015 open-problems paper nor MKK 2015. It is not
    relevant to Problem 4.1.
- **Saminger-Platz, Kolesárová, Šeliga, Mesiar, Klement, "New results on perturbation-based
  copulas".** Dependence Modeling 9 (2021) 347–373, doi:10.1515/demo-2021-0116.
  - **Full text not read**: degruyter.com redirected to degruyterbrill.com, which returned
    HTTP 405.
  - Abstract, through the OpenAlex summariser (accessed 2026-11-27): it opens with "A prominent
    example of a perturbation of the bivariate product copula" (EFGM), and covers
    perturbations of Π and of general copulas, perturbations of Π by two univariate
    functions, ordinal sums, flippings, survival copulas, the Markov product and dependence
    parameters. The abstract does not mention dimension n ≥ 3.
  - OpenAlex lists 103 references, and W2036212222 is not among them.
- **Longla, Djongreba Ndikwa, Muia Nthiani, Takam Soh, "Perturbations of copulas and mixing
  properties".** arXiv:2101.04573v2 (journal version doi:10.1007/s42952-021-00133-5). Pages 1–8
  read from https://arxiv.org/pdf/2101.04573, accessed 2026-11-27.
  - Bivariate only in the pages read.
  - p. 5 cites the special case H_θ = θ(x − C)(y − C), θ ∈ [0,1], of Mesiar et al. (2015).
  - p. 6 repeats that Mesiar et al. (2019) left the n-dimensional noise case for future
    research.
  - Nothing in the pages read concerns the n-ary perturbation (2).
- **Mesiar–Komorníková–Komorník (2015) itself** (reference [38] of the problem paper): **not
  opened** (paywalled; no author copy found within budget). Whether it contains remarks on
  n ≥ 3 is unknown.

## 4. Not accessed (to check next)

1. Fernández-Sánchez, Úbeda-Flores, FSS, doi:10.1016/j.fss.2018.06.013 (the "higher
   dimensions" snippet). ScienceDirect was not tried, and the Bohrium page was blocked.
2. Zhu, Wang, Pipitpojanakarn (2017), doi:10.1007/978-3-319-50742-2_15 (general n-dimensional
   perturbation framework).
3. Komorník, Komorníková, Kalická et al., AGOP 2017, doi:10.1007/978-3-319-59306-7_6
   (parameters in [−1,0], relevant to n = 2 under the literal sign).
4. Durante, Fernández-Sánchez, Trutschnig, Dependence Modeling 2 (2014) 1–8 (which open problem
   it solves).
5. Full texts of MKK 2015 (FSS 268); Komorník et al. FSS 2017; Saminger-Platz et al. 2021;
   the EFGM-extension paper (FSS 2020); and the J. Comput. Appl. Math. 2023 paper.
6. Not searched: Google Scholar, zbMATH Open, MathSciNet, MathOverflow and OEIS. Also not
   searched: literature on multivariate FGM or Ali–Mikhail–Haq families in its own right.
   Note that for C = Π and n ≥ 3, ∏(x_i − Π) = Π·∏_i(1 − ∏_{j≠i} x_j) is not of the standard
   n-dimensional FGM form.
7. Formalization (task item 5): **not checked in this audit**. The formal-conjectures
   repository and Mathlib were not searched. The dossier's statement that Mathlib has no
   copulas was not re-verified.

## 5. Web operations run (2026-11-27)

1. WebFetch, UTIA author copy PDF (read as page images, pp. 112–117).
2. WebFetch, OpenAlex `cites:W2036212222` (32 works).
3. WebFetch, Semantic Scholar citations of doi:10.1016/j.fss.2014.07.012 (30 works).
4. WebSearch, `"Solution to an open problem about a transformation on the space of copulas"`.
5. WebSearch (extended), `multivariate perturbation of copulas n-dimensional "C(x) - λ" product (x_i - C(x)) n-copula Mesiar open problem`.
6. WebFetch, arXiv 2101.04573 (pp. 1–8 read as page images).
7. WebSearch, `"New results on perturbation-based copulas" Saminger-Platz Kolesárová Šeliga Mesiar Klement`.
8. WebSearch, `perturbation of n-dimensional copulas "n-copula" perturbation product copula higher dimensions Komorník Komorníková Mesiar`.
9. WebFetch, degruyter.com demo-2021-0116 (redirect).
10. WebFetch, degruyterbrill.com demo-2021-0116 (HTTP 405).
11. WebSearch, `"Problem 4.1" Mesiar Stupňanová copula n-increasing perturbation answer`.
12. WebFetch, OpenAlex `works/doi:10.1515/demo-2021-0116` (abstract, references).
13. WebFetch, IDEAS page of Durante–Fernández-Sánchez–Trutschnig (2014).
14. WebFetch, Kybernetika 2019 PDF (pp. 422–423 and 432–434 read as page images).
15. WebFetch, OpenAlex search `"Perturbation of bivariate copulas"`.
16. WebSearch, `"perturbation" copulas "higher dimensions" OR "multivariate case" Mesiar Komorníková Kalická "n-dimensional" ... Fuzzy Sets and Systems`.
17. WebFetch, OpenAlex `cites:W2015941533` (27 works).
18. WebFetch, OpenAlex metadata for W2810661996, W2587646203 and W2583390502 (no abstracts available).
19. WebSearch, `Fernández-Sánchez Úbeda-Flores "Solution to two open problems on perturbations of the product copula" abstract`.
20. WebSearch, `Zhu Wang Pipitpojanakarn "Constructions of Multivariate Copulas" perturbation n-dimensional`.
21. WebFetch, Bohrium listing of doi:10.1016/j.fss.2018.06.013 (blocked by a bot check; no content).

## 6. Limits

- The citation indexes were screened by title, and by abstract only where the fetch summariser
  reported one. Citing works whose relevance shows only in the body text would be missed.
- The two indexes disagree (32 vs 30 works, with 3 works only in Semantic Scholar). Neither is
  complete.
- No work was found that restates Problem 4.1 as open.
- Snippets from the search tool are second-hand summaries. They are recorded as leads, never
  as findings.
