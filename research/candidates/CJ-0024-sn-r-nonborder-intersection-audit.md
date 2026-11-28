# CJ-0024 / CJ-0023: literature audit

*Literature audit, 2026-11-27, by the literature-auditor subagent (model claude-opus-5-5). Budget: about 30 web operations and about 20 minutes. About 29 web operations were used. All URLs below were accessed on 2026-11-27. This file supplements `CJ-0024-sn-r-nonborder-intersection.md` and also covers Problem 4.5(ii) (CJ-0023). It does not edit either dossier.*

## 0. Summary of verdicts (read the coverage statement in section 6 first)

No prior resolution was found within this coverage.

| Problem | Verdict |
| --- | --- |
| Problem 4.2(i) of the 2013 chapter (= Problem 4.8.1 of the 2008 monograph, in the chapter's wording) | **No answer found within this coverage.** It was last restated as open in Baczyński and Jayaram (2013 chapter, Section 4). Earlier restatements: the 2010 QL paper, p. 180 ("as yet, it is only known that I_WB ∈ I_{S,N} ∩ I_T"), and the 2008 survey, Problem 7.1(iv). |
| Problem 4.2(ii) | No answer found within this coverage (it depends on 4.2(i)). |
| Problem 4.5(ii) of the 2013 chapter (QL ∩ R from non-left-continuous T) | **No answer found within this coverage.** It was last restated as open in the 2013 chapter, Section 4 ("originally appeared as open in [2] and still remain so"). Earlier: the 2010 QL paper, p. 184 ("A complete characterization of the above intersection is as yet unknown"). |
| The family T_c / I_c (1 < c < 2) | Not found, as an explicit family, in any source opened. The general construction it belongs to does appear in the literature: a t-subnorm M with the drastic boundary, and the residual formula. See section 3.3. |

Caveats: the source most likely to contain a post-2013 update was **not read**. That source is the 2015 handbook chapter "Fuzzy Implications: Past, Present, and Future" (doi:10.1007/978-3-662-43505-2_12). The full text of the 2024 position paper by Massanet, Fernández-Peralta, Baczyński and Jayaram was also not read. See section 5.

## 1. Exact statements (primary and pre-primary sources)

### 1.1 The 2013 chapter (primary source)

M. Baczyński, B. Jayaram, "Fuzzy Implications: Some Recently Solved Problems", in *Advances in Fuzzy Implication Functions*, STUDFUZZ 300, Springer 2013, pp. 177-204, doi:10.1007/978-3-642-35677-3_8. I read it from the local text extraction of the author PDF (`.../scratchpad/dl_bj2013/chapter.txt`, made from https://people.iith.ac.in/jbala/publications/book_chapters/mb_bj_adv_fi.pdf).

- Section 3.1.3 (p. 193), quoting the monograph: "Problem 4.8.1 in [2]: Is there a fuzzy implication I, other than the Weber implication I_WB, which is both an (S,N)-implication and an R-implication which is obtained from a non-left continuous t-norm and cannot be obtained as the residual of any other left-continuous t-norm, i.e., is the following equality true I_{S,N} ∩ (I_T \ I_{T?}) = {I_WB}?" The decoration on the second I_T is lost in the text extraction, so I write it as I_{T?}. See the remark below.
- Same page: "Note that for an I_T to be an (S,N)-implication, it needs to satisfy (EP) and hence the above question roughly translates into finding t-norms T such that I_T satisfies (EP)." and "From the results above, it is clear that when T is a border-continuous t-norm, then the above intersection is empty, i.e., I_{S,N} ∩ (I_T \ I_{T?}) = ∅."
- Section 4 (p. 202): "Problem 4.1. Give a necessary condition on a non-border continuous t-norm T for the corresponding I_T to satisfy (EP). It should be mentioned that some related work on the above problem has appeared in [20]. Once again, as stated before, the above problem is also related to the following question regarding the intersection of (S,N)- and R-implications which still remains open: Problem 4.2. (i) Is there a fuzzy implication I, other than the Weber implication I_WB, which is both an (S,N)-implication and an R-implication which is obtained from a non-border continuous t-norm and cannot be obtained as the residual of any other left-continuous t-norm? (ii) If the answer to the above question is in the affirmative, characterize the above non-empty intersection."
- Same page: "The following problems originally appeared as open in [2] and still remain so: ... Problem 4.5. (i) Characterize the non-empty intersection I_{S,N} ∩ I_QL. (ii) Is the Weber implication I_WB the only QL-implication that is also an R-implication obtained from a non-left continuous t-norm? If not, give other examples from the above intersection and hence, characterize the non-empty intersection I_QL ∩ I_T."
- p. 189, on the drastic product T_D: "The R-implication generated from T_D is given by I_TD(x,y) = 1, if x < 1; y, if x = 1." This is the Weber implication (see also Table 8 of the 2010 QL paper: T_D ↦ I_WB).
- p. 189: "Recently, JAYARAM ET AL. [21] have partially solved the above problem [necessary condition for (EP)] for border-continuous t-norms. A complete characterization is not yet available."
- References: [20] = Jayaram, Baczyński, Mesiar, "R-implications and the Exchange Principle: A Complete Characterization", EUSFLAT 2011. [21] = the same authors, "... the case of border continuous t-norms", FSS (listed as "submitted").

**Remarks on the statement.**
1. *"non-left continuous" (monograph wording) versus "non-border continuous" (Problem 4.2).* The chapter itself says the intersection is empty for border-continuous T. Every border-continuous T then contributes nothing outside the left-continuous residuals, so within the chapter the two wordings ask for the same set. A border-continuous T may still have I_T ∈ I_{S,N} if I_T is also the residual of a left-continuous t-norm. This reading of the chapter's own claim is mine; the chapter does not spell it out.
2. *The decoration on I_{T?}.* In the 2010 QL paper, 𝕀_{T*} is "the family of all R-implications obtained from left-continuous t-norms having strong induced negations", and 𝕀_{T_LC} is "the family of all R-implications obtained from left-continuous t-norms". The 2008 survey (Section 6.4) and the 2010 QL paper (p. 180) state that 𝕀_{S,N} ∩ 𝕀_{T_LC} = 𝕀_{T*}. Hence 𝕀_{S,N} ∩ (𝕀_T \ 𝕀_{T_LC}) = 𝕀_{S,N} ∩ (𝕀_T \ 𝕀_{T*}), so both readings of the decoration define the same set. (This is a one-line set computation from the quoted equality.)
3. The 2008 monograph (STUDFUZZ 231) itself was **not** opened. Its Problem 4.8.1 is known here only through the chapter's quotation.

### 1.2 Earlier statements of the same questions

**(a) Baczyński and Jayaram, "(S,N)- and R-implications: a state-of-the-art survey", FSS 159 (2008) 1836-1859.** DOI verified as 10.1016/j.fss.2007.11.015 (OpenAlex W2096071080; https://api.openalex.org/works?search=... returned this DOI with volume 159, pages 1836-1859). Author PDF read (pages 1854-1859): https://people.iith.ac.in/jbala/publications/fss/sn_r_imp_survey.pdf.
- p. 1856: "Firstly, note that since I_TD is both an (S,N)- and R-implications, we have I_TD ∈ 𝕀_{S,N} ∩ 𝕀_T ≠ ∅, i.e., the intersection of (S,N)- and R-implications is non-empty."
- Section 6.4 (p. 1857): "𝕀_S ∩ 𝕀_TLC = 𝕀_{S,N} ∩ 𝕀_TLC = 𝕀_{N_T(T),N_T} = 𝕀_T*".
- Remark 6.4 (p. 1857): "(i) The left-continuity of T is very important in the above theorems. For example, consider any t-conorm S whose natural negation N_S ≠ N_D2. But, I_{S,N_D2} = I_TD which is also an R-implication obtained from the non-left-continuous t-norm T_D. ... (ii) ... consider the t-norm T_nM* from Example 5.6 (iv). Now, N_{T_nM*} = N_C and I_{T_nM*} = I_FD, which is an (S,N)-implication." The Fodor implication I_FD is also the residual of the left-continuous nilpotent minimum (2013 chapter, p. 189), so it lies outside the set asked about in Problem 4.2.
- pp. 1858-1859: "Also, characterization of R-implications generated from non-left-continuous t-norms is still unknown. All this discussion leaves us with the following open problems. Problem 7.1. Characterize the following: (i) (S,N)-implications generated from non-continuous negations; (ii) R-implications generated from non-left-continuous t-norms; (iii) continuous R-implications generated from non-left-continuous t-norms; (iv) the non-empty intersection 𝕀_{S,N} ∩ 𝕀_T."
- Fig. 3 (p. 1858) shows "?" regions in 𝕀_T ∩ 𝕀_{S,N} outside 𝕀_TLC.

**(b) Baczyński and Jayaram, "QL-implications: some properties and intersections", FSS 161 (2010) 158-188.** DOI 10.1016/j.fss.2008.09.021 (OpenAlex W2150824422). Author PDF: https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf. Read: pp. 158-159 and 179-185.
- p. 180: "Note that, as yet, it is only known that I_WB ∈ 𝕀_{S,N} ∩ 𝕀_T. A complete characterization of the intersection of these classes is still an open problem."
- Theorem 6.1 (p. 180): "The QL-implication I_{T,S,N}, where S is a positive t-conorm, is an (S,N)-implication. In fact, I_{T,S,N} = I_WB."
- Remark 6.3(iv) (p. 181): "I_WB is an (S,N)-implication obtained from any t-conorm S and N = N_D2, i.e., I_WB = I_{S,N_D2}".
- Section 7 (p. 183): "Firstly, if S is a positive t-conorm or if N = N_D2, then the QL-implication I_{T,S,N} is the R-implication I_WB obtained from the non-left-continuous t-norm T_D. Hence 𝕀_QL ∩ 𝕀_T ≠ ∅."
- p. 184: "A complete characterization of the above intersection is as yet unknown. However, as we show below, the exact intersection of the family of QL-implications 𝕀_QL with the family of R-implications obtained from left-continuous t-norms 𝕀_TLC can be precisely determined." Theorem 7.2 then gives 𝕀_QL ∩ 𝕀_TLC = 𝕀_TLC ∩ 𝕀_{S,N} = 𝕀_QL ∩ 𝕀_TLC ∩ 𝕀_{S,N} = 𝕀_{S*,N*_S} = 𝕀_T*.
- Example 7.3 (p. 185): I_TB (the residual of a border-continuous, non-left-continuous t-norm) is not a QL-implication, by Proposition 4.23 of the paper (Proposition 4.23 itself was not read). Summary list: "I_WB ∈ 𝕀_QL \ 𝕀_TLC", "I_TB ∈ 𝕀_T \ 𝕀_QL". Fig. 3 has a "?" region.
- Proof of Proposition 7.1(i) (p. 184) uses Propositions 4.23 and 3.6: the natural negation of a QL-implication that is an R-implication I_T* with T* left-continuous "is either strong or discontinuous but strictly decreasing". That proof is for left-continuous T* only.

**(c) Jayaram, Baczyński, Mesiar, "R-implications and the Exchange Principle: A Complete Characterization", EUSFLAT-LFA 2011, pp. 223-229,** doi:10.2991/eusflat.2011.63. Read in full (7 pages) from https://www.atlantis-press.com/article/2248.pdf, reached from the DOI through three atlantis-press redirects.
- Abstract: "The work presents a complete characterization of the class of t-norms whose residuals satisfy (EP)."
- Definition 1.3: a t-norm is "border-continuous, if it is continuous on the boundary of the unit square [0,1]^2, i.e., on the set [0,1]^2 \ ]0,1[^2."
- Section 4 "Non border-continuous t-norms" (p. 227): "Let M be a t-subnorm and T_M the t-norm obtained from M as follows (see [5, Corollary 1.8]): T_M(x,y) = M(x,y) if (x,y) ∈ [0,1[^2, min(x,y) otherwise. (5) Then, as it can be verified, the corresponding residual is related as follows: I_{T_M}(x,y) = I_M(x,y) if x ≠ 1, y if x = 1. (6)" Here [5] is Klement, Mesiar and Pap, *Triangular Norms* (2000).
- Definition 4.1 defines the "border-continuous projection" M_T(x,y) = T(x,y) on [0,1[^2 and T(x^-,y^-) otherwise. Theorem 4.5 reads: "For a t-norm T the following statements are equivalent: (i) I_T satisfies (EP). (ii) M_T satisfies (CLCC-A)-property (i.e., M*_T is associative) and I_{M_T} = I_{M*_T}." Examples 4.4 and 4.6 give a non-border-continuous t-norm T_Z (from [5, Example 3.19]) whose residual satisfies (EP).
- **No mention** of (S,N)-implications, QL-implications or the Weber implication in the paper (all 7 pages read).
- **Observation, not a finding:** this paper states a characterization of (EP) for *all* t-norms. Yet the 2013 chapter lists the non-border-continuous case as open (Problem 4.1) and calls [20] only "related work". The 2013 journal version (item (d)) states results only for border-continuous and ordinal-sum t-norms. No erratum or explanation was found. The project should not rely on Theorem 4.5 of the EUSFLAT paper without checking its proof independently.

**(d) Jayaram, Baczyński, Mesiar, "R-implications and the exchange principle: The case of border continuous t-norms", FSS 224 (2013) 93-105,** doi:10.1016/j.fss.2012.12.005. Author copy: https://people.iith.ac.in/jbala/publications/fss/bj_mb_rm_fss_rimp_ep.pdf. Read: p. 93 (abstract, introduction start) and pp. 103-105 (end of the proofs, concluding remarks, references); pp. 94-102 were not read.
- Abstract: "We present a complete characterization of two classes of t-norms whose residuals satisfy (EP), viz., t-norms that are border-continuous and those that have an ordinal sum representation. Based on the obtained results we characterize t-norms, whose residuals satisfy both the exchange principle and the ordering property."
- Corollary 4.6 (ordinal sums): "I_T satisfies (EP)" iff "For every k ∈ K, I_{T_k} satisfies (EP) and either T_k is border-continuous or β_k = 1." No mention of (S,N)- or QL-implications in the pages read.

## 2. Equivalent and related formulations

- Problem 4.2(i) ⇔ "is I_{S,N} ∩ (I_T \ I_{T_LC}) = {I_WB}?" (monograph 4.8.1, as quoted). By Remark 2 in section 1.1 this is the same as I_{S,N} ∩ (I_T \ I_{T*}).
- The chapter (p. 193) reduces the question to "finding t-norms T such that I_T satisfies (EP)", because (EP) is necessary for (S,N)-implications. This links Problem 4.2 to Problem 4.1 (EP for non-border-continuous T), to 2008 survey Problem 7.1(ii) and (iv), and to Problem 4.3 of the chapter (characterising (S,N)-implications from non-continuous negations).
- Problem 4.3 (= 2008 survey Problem 7.1(i)) is addressed by Fernández-Peralta, Massanet, Mesiarová-Zemánková, Mir, "A general framework for the characterization of (S,N)-implications with a non-continuous negation based on completions of t-conorms", FSS (Semantic Scholar year 2021; DBLP key journals/fss/Fernandez-Peralta22; doi:10.1016/j.fss.2021.06.009). Only the abstract was seen, through the Semantic Scholar API, as summarised by the fetch tool. By that summary, it gives a general characterization in which "the existence of a completion of a binary function" is the key property, plus axiomatic characterizations when N has one discontinuity point. The abstract does not mention R-implications. The full text was not read, so whether it discusses the intersection with R-implications is unknown. This paper is the natural tool for checking whether a given I_T is an (S,N)-implication with a non-continuous N.
- For the QL question: by the 2010 QL paper, any QL-implication with a positive S, or with N = N_D2, *is* I_WB. A second example therefore needs a non-positive S and N ≠ N_D2.

## 3. Partial results found

1. 𝕀_{S,N} ∩ 𝕀_TLC = 𝕀_T* (2008 survey, Section 6.4).
2. 𝕀_QL ∩ 𝕀_TLC = 𝕀_{S,N} ∩ 𝕀_TLC = 𝕀_T* (2010 QL paper, Theorem 7.2).
3. I_WB = I_TD ∈ 𝕀_{S,N} ∩ 𝕀_QL ∩ 𝕀_T, and I_WB ∉ 𝕀_TLC (2008 survey, p. 1856; 2010 QL paper, pp. 180, 183, 185).
4. For border-continuous T: I_T satisfies (EP) iff T has the (CLCC-A) property and I_T = I_{T*}, where T* is the conditionally left-continuous completion (FSS 2013; chapter Theorem 3.12). Consequently 𝕀_{S,N} ∩ (𝕀_T \ 𝕀_{T*}) receives nothing from border-continuous T (chapter, p. 193).
5. Ordinal sums: (EP) characterised (FSS 2013, Corollary 4.6).
6. Non-border-continuous T: a claimed characterization (EUSFLAT 2011, Theorem 4.5). It was not carried into the journal version as far as the pages read show, and the 2013 chapter treats this case as open (Problem 4.1).
7. Continuity: the only continuous (S,N)-implication that is also an R-implication from any t-norm is Łukasiewicz up to isomorphism. This is **from a search-engine summary of** Baczyński and Jayaram, Nonlinear Analysis (2009), https://people.iith.ac.in/jbala/publications/na/na7854.pdf, which was **not opened**. If correct, a new element of the intersection cannot be continuous.

### 3.3 The family T_c / I_c

- The candidate T_c(x,y) = max(0, x+y-c) on [0,1[^2, min(x,y) otherwise, has the form (5) of the EUSFLAT 2011 paper, T_M, with M(x,y) = max(0, x+y-c). The residual formula (6) of that paper, I_{T_M}(x,y) = I_M(x,y) for x ≠ 1 and y for x = 1, is the general formula from which I_c is obtained. *This identification is the auditor's; no source names this M or this family.* Whether M is a t-subnorm was not checked here, as instructed.
- None of the sources opened gives T_c, I_c, the negation N_c(x) = min(1, c-x) (x < 1), N_c(1) = 0, or the representation I_c = S_L(N_c(x), y) as an (S,N)-implication. Nor does any opened source give any element of 𝕀_{S,N} ∩ (𝕀_T \ 𝕀_TLC) other than I_WB, or any QL-implication that is the residual of a non-left-continuous t-norm other than I_WB.
- Not checked: Klement, Mesiar and Pap, *Triangular Norms* (2000), Corollary 1.8, Example 3.19 and Proposition 3.66 (cited in EUSFLAT 2011 for the T_M construction and examples). That book may contain T_c as an example t-norm. Even so, it would not by itself address the (S,N)-representation.

## 4. Citation trails (title screening only)

- **2013 chapter** (doi:10.1007/978-3-642-35677-3_8). Semantic Scholar API (https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-642-35677-3_8/citations?fields=title,year,abstract,externalIds&limit=100) returned 1 citing work: the 2015 handbook chapter. The earlier scout recorded four citing works via OpenAlex (not re-fetched).
- **2008 survey** (OpenAlex W2096071080). https://api.openalex.org/works?filter=cites:W2096071080&per-page=200&select=id,doi,title,publication_year returned meta.count 169; all 169 titles were listed and screened (the work record shows cited_by_count 177).
- **2010 QL paper** (W2150824422). https://api.openalex.org/works?filter=cites:W2150824422&per-page=200&select=doi,title,publication_year returned meta.count 79; all titles screened.
- **2015 handbook chapter** (W2221355491; doi:10.1007/978-3-662-43505-2_12). https://api.openalex.org/works?filter=cites:W2221355491&per-page=200&select=doi,title,publication_year returned meta.count 105; all titles screened.
- **Screening result:** no title in the three lists refers to an intersection of R-implications from non-left-continuous or non-border-continuous t-norms with (S,N)- or QL-implications, to the Weber implication, or to a t-norm of the T_c type. **Abstracts were not screened** (the queries returned titles only), so a paper whose title does not show the topic could have been missed.
- Titles flagged as possibly relevant but **not opened**:
  - "The law x ≤ I(y; x) and the three main classes of fuzzy implications" (FUZZ-IEEE 2012, doi:10.1109/fuzz-ieee.2012.6251333)
  - "On the continuity of residuals of triangular norms" (2009, doi:10.1016/j.na.2009.07.041)
  - "Continuous R-implications" (2009)
  - "Formulas for generators of R-implications" (FSS 2018, doi:10.1016/j.fss.2018.09.011)
  - "Residual operations of monotone binary operations over complete lattices" (IJAR 2019, doi:10.1016/j.ijar.2019.04.005)
  - "A structural characterization of R-implications satisfying the special property" (FSS 2026, doi:10.1016/j.fss.2026.110074)
  - "Characterizations of fuzzy implications by the laws of contraposition" (FSS 2025, doi:10.1016/j.fss.2025.109285)
  - "Representations of the fuzzy implications satisfying the law of left or right contraposition" (FSS 2025, doi:10.1016/j.fss.2025.109580; authors Dai, Dan, Pan, Wang per Semantic Scholar; the abstract is null in Semantic Scholar)
  - "On a Class QL-Implications" (2011, doi:10.1007/978-3-642-25002-6_18)
  - "An Overview of Fuzzy Implication and Its Generalizations" (Mathematics 2026, doi:10.3390/math14020330)
  - "On the non-uniqueness of representation of (U, N)-implications" (FSS 2025, doi:10.1016/j.fss.2025.109680)
- "Further results on fuzzy negations and implications induced by fuzzy conjunctions and disjunctions" (arXiv:2601.21156, Zhang and Wang, 2026; cites the 2008 survey). The abstract was read (https://arxiv.org/abs/2601.21156). It concerns (D,N)-implications and does not mention R-, (S,N)- or QL-implications or the Weber implication.
- "On valuable and troubling practices in the research on classes of fuzzy implication functions" (Massanet, Fernández-Peralta, Baczyński, Jayaram, FSS 476 (2024) 108786, doi:10.1016/j.fss.2023.108786). The abstract was read on the repository record https://repisalud.isciii.es/entities/publication/21bd14a7-b4c7-4316-81db-9b629448bb48/full, which lists the item as "open access" under CC BY-NC 4.0 but has no file attached. The abstract mentions "the problems that remain unsolved" in general terms. The full text was not obtained.
- Fernández-Peralta, "A Comprehensive Survey of Fuzzy Implication Functions", arXiv:2503.05702v1 (submitted 6 Feb 2025). Read through https://arxiv.org/html/2503.05702 in two chunks (characters 0-100000 and 100000 to the end), with keyword extraction by the fetch tool. It lists I_WB in Table 2 (Section 3.1). Its Table 1 says of (EP): "In [24] the authors characterize the residuals that satisfy (EP)". No passage on the intersection of R-implications with (S,N)- or QL-implications for non-left-continuous t-norms was reported. Section 4 lists "intersections" only as general future work ("like the main properties studied for each family, their characterizations, and intersections"). The extraction was automated; a manual full read was not done.

## 5. Sources not accessed

- Baczyński and Jayaram, *Fuzzy Implications*, STUDFUZZ 231 (2008), the monograph: not accessed. Problem 4.8.1 and the original wording of 4.5(ii) are known only through the 2013 chapter.
- Baczyński, Jayaram, Massanet and Torrens, "Fuzzy Implications: Past, Present, and Future", Springer Handbook of Computational Intelligence (2015), pp. 183-202, doi:10.1007/978-3-662-43505-2_12: **not accessed** (paywalled; no author copy found; the IITH publications repository host publications.iith.ac.in failed DNS resolution). This is the most likely post-2013 source for a restatement or an update.
- The full text of the 2024 position paper (doi:10.1016/j.fss.2023.108786): not obtained.
- The full text of Fernández-Peralta et al. on (S,N)-implications with non-continuous negations (doi:10.1016/j.fss.2021.06.009): only the abstract was seen. The volume and pages "FSS 441 (2022) 1-32" were not verified.
- FSS 2025 papers 109580 and 109285: not opened (no abstract available for 109580 in Semantic Scholar).
- Nonlinear Analysis 2009 (na7854.pdf): not opened; its result is known here only from a search summary.
- Klement, Mesiar and Pap, *Triangular Norms* (2000): not accessed.
- The 2013 FSS paper, pp. 94-102: not read.
- 2010 QL paper, Sections 3-4 (including Proposition 4.23, Example 4.14) and pp. 186-188: not read.
- zbMATH, MathSciNet and Google Scholar "cited by": not searched. MathOverflow, erdosproblems.com and OEIS: not searched (judged not relevant to this topic). Formalization: Mathlib, formal-conjectures and other libraries were **not checked** in this audit.

## 6. Coverage statement and limits

Queries and URLs, all accessed 2026-11-27:
1. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-642-35677-3_8/citations?fields=title,year,abstract,externalIds&limit=100
2. https://api.openalex.org/works?search=%22(S,N)-%20and%20R-implications%22%20state-of-the-art%20survey&per-page=5 (verified the 2008 survey's DOI)
3. https://api.openalex.org/works?filter=cites:W2096071080&per-page=200&select=id,doi,title,publication_year
4. https://api.openalex.org/works/https://doi.org/10.1016/j.fss.2008.09.021?select=id,doi,title,publication_year,cited_by_count
5. https://api.openalex.org/works/https://doi.org/10.1007/978-3-662-43505-2_12?select=id,doi,title,publication_year,cited_by_count
6. https://api.openalex.org/works?filter=cites:W2150824422&per-page=200&select=doi,title,publication_year
7. https://api.openalex.org/works?filter=cites:W2221355491&per-page=200&select=doi,title,publication_year
8. https://doi.org/10.2991/eusflat.2011.63, then the atlantis-press redirects, then https://www.atlantis-press.com/article/2248.pdf (read in full)
9. https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf (pp. 158-159, 179-185 read)
10. https://people.iith.ac.in/jbala/publications.html (no relevant entries listed)
11. Web search: `"Weber implication" "(S,N)-implication" R-implication non-left-continuous t-norm intersection`
12. Web search: `"Fuzzy implications: past, present, and future" Baczyński Jayaram Massanet Torrens open problems pdf`
13. https://people.iith.ac.in/jbala/publications/fss/sn_r_imp_survey.pdf (pp. 1854-1859 read)
14. https://publications.iith.ac.in/publication/fuzzy-implications-past-present-and-future-1 (DNS failure)
15. https://arxiv.org/pdf/2503.05702 (binary, not parsed); https://arxiv.org/html/2503.05702 (two chunks)
16. Web search: `"non-border-continuous" OR "non border-continuous" t-norm residual "exchange principle" (S,N)-implication`
17. https://people.iith.ac.in/jbala/publications/fss/bj_mb_rm_fss_rimp_ep.pdf (pp. 93, 103-105 read)
18. Semantic Scholar paper records: DOI:10.1016/j.fss.2025.109580, DOI:10.1016/j.fss.2021.06.009, DOI:10.1016/j.fss.2023.108786
19. Web search: `"On valuable and troubling practices in the research on classes of fuzzy implication functions" pdf intersections open problems`
20. Web search: `R-implication "(S,N)-implication" t-norm "non-left-continuous" intersection Weber "other than" example residual t-subnorm Łukasiewicz boundary`
21. https://repisalud.isciii.es/entities/publication/21bd14a7-b4c7-4316-81db-9b629448bb48/full
22. https://arxiv.org/abs/2601.21156

## 7. Addendum (coordinator request): Problems 9.3 and 9.4(iii) of the 2010 QL paper

*Added 2026-11-27, after the main audit, when only about one web operation of the budget remained. The coverage is therefore thin and is stated exactly below.*

### 7.1 Exact statements

Source: Baczyński and Jayaram, FSS 161 (2010) 158-188, Section 9 "Concluding remarks", pp. 187-188. I read them from the local text extraction `C:\Users\bezze\AppData\Local\Temp\claude\150e3719c412ed18\c06221b9-25bc-46ba-a9aa-ef998ec1e85e\scratchpad\dl_bj2010\ql.txt`, lines 1740-1790. That file was made from the author PDF; in this audit I read pp. 179-185 of the PDF as images, not p. 187.

- Context, verbatim: "Although Theorem 6.2 gives an equivalence condition for a QL-implication I_{T,S,N}, with a continuous negation N, to satisfy (EP), it is obvious that its utility is quite limited. Nevertheless, all the examples, so far, seem to point that a QL-implication that satisfies (EP) also turns out to be an (S,N)-implication. The answers to the following posers will be of immense help in resolving the exact intersection between families of (S,N)- and QL-implications."
- "Problem 9.3. (i) Is Theorem 6.2 true even when N is not continuous, i.e., is any QL-implication I_{T,S,N} that satisfies (EP) also an (S,N)-implication? (ii) If not, give a counter-example and hence obtain an alternate necessary and sufficient condition for a QL-implication I_{T,S,N} to satisfy (EP)."
- Context, verbatim: "However, it is not yet clear if there is a QL-implication which can be represented as an R-implication of some non-left-continuous t-norm, but which is not an (S,N)-implication. Note that Theorem 7.2 assumes the left-continuity of the t-norm T* (see Fig. 3)."
- "Problem 9.4. (i) Characterize the non-empty intersection I_{S,N} ∩ I_QL. (ii) Is the Weber implication I_WB the only QL-implication that is also an R-implication obtained from a non-left continuous t-norm? If not, give other examples from the above intersection and hence, characterize the non-empty intersection I_QL ∩ I_T. (iii) Prove or disprove by giving an example: (I_QL ∩ I_T) \ I_{S,N} = ∅. (iv) Is the intersection I_{F,∞} ∩ I_QL non-empty? If yes, then characterize the intersection I_{F,∞} ∩ I_QL." (Here I_{F,∞} is the family of f-generated implications with f(0) < ∞, as the paper defines it just before; the symbols are partly lost in the extraction.)
- Theorem 6.2 of the same paper (p. 180, read as an image): "For a QL-implication I_{T,S,N}, with a continuous negation N, the following statements are equivalent: (i) I_{T,S,N} satisfies (EP). (ii) I_{T,S,N} is an (S,N)-implication generated from N."

### 7.2 Relation to the 2013 chapter

- 2010 Problem 9.4(i) and (ii) reappear verbatim as Problem 4.5(i) and (ii) of the 2013 chapter, under the heading "The following problems originally appeared as open in [2] and still remain so". 2010 Problem 9.1 ("Characterize triples (T, S, N) such that I_{T,S,N} satisfies (I1)") reappears as chapter Problem 4.4.
- 2010 Problem 9.4(iv) is reported **solved** in the chapter, as "Solved Problem 7 ([2, Problem 4.8.3])". The chapter writes: "(i) Is the intersection I_{F,∞} ∩ I_QL non-empty? (ii) If yes, then characterize the intersection". The solution is attributed to [36] = Massanet and Torrens, "Intersection of Yager's implications with QL and D-implications", IJAR 53 (2012) 467-479, Theorem 13 (chapter Theorem 3.30). I read this in the local chapter text, lines 1213-1233. The IJAR paper itself was not opened.
- 2010 Problems **9.2, 9.3 and 9.4(iii) appear nowhere in the 2013 chapter**, either as solved or as open. I searched the local chapter text for "9.3", "9.4", "QL-impl" and "Solved Problem". The only QL material is Definition 3.29, Solved Problem 7 and Problem 4.5. The chapter's lists are drawn mainly from the monograph [2] (and [29], [28]), not from the 2010 paper. So the omission does **not** show that 9.3 or 9.4(iii) were solved: the chapter gives no reason for leaving them out, and they may simply never have been in the monograph's list. Whether the monograph contains them was not checked, since the monograph was not accessed.

### 7.3 Search for answers (2010 onward)

- One web search, accessed 2026-11-27: `QL-implication "exchange principle" non-continuous negation "(S,N)-implication" counterexample Baczyński Jayaram problem open`. Results: DBLP and researchr records; the arXiv survey 2503.05702; the 2008 survey; Mas, Monserrat and Torrens, Kybernetika 42 (2006) 351-366, https://www.kybernetika.cz/content/2006/3/351/paper.pdf (not opened; it predates the 2010 problems); arXiv:1612.04979; and two others. The search summary did not identify any source that answers Problem 9.3 or 9.4(iii). The search tool's own summary said so; I did not verify this by reading the sources.
- The OpenAlex title screen of the 79 works citing the 2010 QL paper (section 4, query 6) contains "Intersection of Yager's implications with QL and D-implications" (Massanet and Torrens, IJAR 2011/2012, doi:10.1016/j.ijar.2011.11.001; this addresses 9.4(iv)) and "On a Class QL-Implications" (2011, doi:10.1007/978-3-642-25002-6_18; authors not recorded here). Neither was opened. "The law of importation versus the exchange principle on fuzzy implications" (Massanet and Torrens, FSS 2011, doi:10.1016/j.fss.2010.12.012) cites the 2008 survey; it was not opened, and its title concerns (LI) versus (EP), not QL-implications specifically.
- No title in the screened lists refers to (EP) for QL-implications with non-continuous negations, or to QL-implications that are R-implications but not (S,N)-implications.
- Not done for this addendum: opening any of the papers above; checking works by Shi, Van Gasse, Ruan and Kerre (e.g. their QL-implication papers) beyond what appears in the OpenAlex title lists; a citation trail of Massanet and Torrens (2012); zbMATH, MathSciNet and Google Scholar.

### 7.4 Verdicts (addendum)

| Problem (2010 QL paper) | Verdict |
| --- | --- |
| 9.3(i)-(ii): does every QL-implication satisfying (EP) belong to I_{S,N} when N is not continuous? | **No answer found within this coverage** (one web search; title screening of the citing works only). The 2013 chapter neither restates it as open nor reports it solved. Status after 2010 is unknown. |
| 9.4(iii): (I_QL ∩ I_T) \ I_{S,N} = ∅? | **No answer found within this coverage.** Same remark: it is absent from the 2013 chapter, and the absence is not evidence either way. The 2010 paper's text ("it is not yet clear if there is a QL-implication which can be represented as an R-implication of some non-left-continuous t-norm, but which is not an (S,N)-implication") is the latest open-status statement found. |
| 9.4(iv) (for context) | Answered: Massanet and Torrens, IJAR 53 (2012) 467-479, Theorem 13, as reported by the 2013 chapter (Solved Problem 7). The IJAR paper itself was not opened. |

Limits: about 30 web operations in total (29 before the addendum, 1 for it); citing-work lists screened by title only; Google Scholar, zbMATH and MathSciNet not used; the 2015 handbook chapter, the 2008 monograph and the 2024 position paper (full text) not read; Chinese-language and conference literature reached only through OpenAlex titles. The search terms were in English only. **An unsuccessful search does not establish that the problems are open or that the T_c family is new.** It establishes only that none of the sources listed above, read to the extent stated, answers them.
