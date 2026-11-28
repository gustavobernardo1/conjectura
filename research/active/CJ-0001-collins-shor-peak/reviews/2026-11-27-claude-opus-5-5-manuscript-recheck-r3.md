# Independent review — CJ-0001 — manuscript revision 3 (changes since revision 2)

- **Reviewer:** Claude, model `claude-opus-5-5` (Anthropic), adversarial reviewer role.
- **Date:** 2026-11-27 (about 21:21 to 21:40 local time, by `date`).
- **Independence:** fresh subagent context. It received the task statement,
  the commit identifiers and the file hash, not the author's reasoning. **The
  independence is limited.** The reviewer is the same model and vendor as the
  author of the manuscript text (`claude-opus-5-5`, see "Use of AI systems").
  Following the instructions, the reviewer did not read
  `reviews/2026-11-27-codex-gpt-astra-6-manuscript-r2.md` (the author's
  assessment), the session-15 journal entry, `STATE.md` or the notes. Section 1
  of the external report (Portuguese original), its sections 3–5, and the
  verdict lines of `2026-11-27-claude-sonnet-5-5-manuscript-recheck-r2.md` were
  read only after the reviewer's own checks were done. Excerpts of the dossier
  `research/candidates/CJ-0001-collins-shor-peak.md` (the Graham–Pollak and
  OpenAlex records) were read to check provenance statements.
- **Revision reviewed:** commit `f695cbd1c78ecb0b817ced0c5d94776d8e310fa6`
  (revision 3), compared with `87c3c8c` (revision 2).
  - `manuscripts/CJ-0001-collins-shor/main.tex`, SHA-256
    `3477baa0902eb3446415167baf38e83e939fb68f002f55b1162ebee2337d917b`. This
    hash is identical at `f695cbd` and in the working tree. It is also
    unchanged at `9f6c091`, a records-only commit that appeared during this
    review.
  - Revision 2 at `87c3c8c`, SHA-256
    `5dd8d2b397e78ddf7a41d13d3fe07f115e5405583ee379e2fc0bd184865b42a9`. It
    equals the hash in the external report and `versions/r2/main.tex` at
    `f695cbd`.
  - `experiments/CJ-0001-collins-shor-peak/amw_reduction_check.py`, SHA-256
    `3331e9d8e0a56d55815ab4950ccae9532179d3ba45da886522cac884a7428636` (as at
    `f695cbd`).
  - `results/exhaustive-03-20.json` `bfb41569…8da94` and
    `results/exhaustive-21-23.json` `b438cee7…62302` (unchanged since `f695cbd`).
- **Material given to the reviewer:** the task statement of the research
  director, the repository, and the primary sources (fetched by the reviewer):
  - arXiv:1507.02341v3, pp. 1–3;
  - arXiv:1903.09825v1, pp. 6–18;
  - the scan of Graham–Lovász (1978), p. 83.
- **Scope:** every hunk of `git diff 87c3c8c f695cbd -- manuscripts/CJ-0001-collins-shor/main.tex`
  (183 insertions, 64 deletions; only `f695cbd` touches `main.tex` between the
  two revisions), read together with the surrounding text it depends on:
  - Section 5 (definition of `R_w`);
  - Theorem 7.1 and Remark 7.8;
  - Lemmas 9.1–9.7 and Theorem 9.5;
  - Theorem 10.1;
  - Lemma 11.1 and Corollary 11.2;
  - Sections 12–16.

  Not in scope: anything in sections 2–11 that revision 3 did not change.

## Statement as read from the primary source

Aalipour et al., arXiv:1507.02341v3, p. 2. For a graph `G` of order `n` and
`0 ≤ k ≤ n−2`, the normalized coefficients are `d_k(G) = 2^k |δ_k(G)| / 2^{n−2}`,
where `δ_k(G)` is the coefficient of `x^k` in `det(D(G) − xI)`. The order is
assumed to be at least 3.

**Conjecture 1.2 (Collins–Shor), p. 3.** "The [normalized] coefficients of
the distance characteristic polynomial for any tree `T` with `n` vertices are
unimodal with peak between `⌊n/2⌋` and `⌈n − n/√5⌉`."

- Quantifiers: every tree `T` of order `n` (with `n ≥ 3`).
- How a tie between maximal coefficients is read is not specified.

The manuscript's Conjecture 1 quotes this statement verbatim. Its Main Theorem
proves the strong reading, in which every maximizing index is bounded. The
claim reviewed here concerns the revision-3 changes only, and is about this
statement.

The same page quotes Graham–Lovász: "… unimodal with the maximum value
occurring for `k = ⌊n/2⌋`." The original scan of Graham–Lovász (1978), p. 83,
reads: "It appears that in fact for each tree T, the quantities
(−1)^{n−1}δ_k(T)/2^{n−k−2} are *unimodal* with the maximum value occurring for
k = [n/2]. We see no way to prove this, however."

## Findings

### The six findings of the external review of revision 2

| # | Finding of the external review (section 1) | Corrected? | Is the correction correct? |
| --- | --- | --- | --- |
| 1 | Remark 9.6: wrong multiplicity of the eigenvalue 0 in the spectrum of `S(T)` | Yes | Yes (details under (a) below) |
| 2 | Section 12, item 1: overclaim that a sharper mode–mean inequality is needed | Yes | Mostly. The overclaim is gone, and the characterization of the settled orders, the `n = 9` example and the count 806 are correct. One new imprecision: **D1** below |
| 3 | `φ` not defined | Yes | Yes. `φ = (1+√5)/2` is defined in the introduction (line 207, first use) and in the Conventions (line 230). No use precedes line 207 |
| 4 | Abstract: Graham–Lovász peak at `n/2` | Yes | Yes. The abstract has `⌊n/2⌋`. The introduction quotes p. 83 verbatim as "with the maximum value occurring for `k=[n/2]`", checked against the scan, and correctly glosses `[n/2]` as the integer part |
| 5 | Relation of Theorem 9.5 to AMW should be stated precisely | Yes | Yes. Remark 9.6 now contains a complete reduction, checked step by step below. Section 15 calls Theorem 9.5 "a rediscovery" "as a statement" and keeps "our proof … is independent" |
| 6 | `R(K,ν)` undefined (Section 12, item 3) | Yes | Yes (details under (d) below) |

#### (a) Remark 9.6: derivation of Theorem 9.5 from AMW

I re-derived every step.

**Spectrum of the subdivision.**
- `A_{S(T)} = [[0, B], [Bᵀ, 0]]`, where `B` is the `n × (n−1)` unsigned
  incidence matrix.
- `BBᵀ = diag(k_v) + A_T = ΣLΣ`, where `Σ` is the ±1 diagonal matrix of the
  bipartition. This holds because `ΣA_TΣ = −A_T` for a bipartite graph.
- `rank B = rank BBᵀ = rank L_T = n − 1`, because a tree is connected.
- The nonzero eigenvalues of the block matrix are `±` the nonzero singular
  values of `B`, which are `√μ_j` for the `n − 1` positive Laplacian
  eigenvalues.
- The nullity is `(2n−1) − 2(n−1) = 1`, so there is **exactly one zero
  eigenvalue**. This is correct.

**Matching polynomial of a forest.**
- In `det(yI − A)`, a permutation with a cycle of length at least 3 would need
  a cycle in the graph, so only fixed points and transpositions along edges
  survive.
- Each transposition contributes `sgn = −1` and `(−1)(−1) = 1`. This gives
  `Σ_k (−1)^k m_k y^{N−2k}`. Correct.

**Generating function.**
- `y∏(y² − μ_j) = Σ(−1)^k e_k(μ) y^{2n−1−2k}`, so `m_k(S(T)) = e_k(μ)`.
- Therefore `Σ m_k t^k = ∏(1 + μ_j t)`. Correct.

**Logarithmic derivative.**
- At `t = 1` it gives `avm(S(T)) = Σ μ_j/(1+μ_j)`.
- Since `tr(I+L)^{-1} = 1 + Σ 1/(1+μ_j)`, this equals `n − tr(I+L_T)^{-1}`.
  Correct.
- Comparison with AMW Lemma 5.1, which holds for all graphs:
  `avm(G) = ½ Σ λ²/(λ²+1)` over the zeros of the matching polynomial. For
  `S(T)` this gives the same value. "The case of a forest" is an acceptable
  description.

**AMW statements, checked against the arXiv v1 PDF.**
- **Theorem 4.4 (p. 8):** "For every tree T of order n that is not a path,
  avm(T) ≤ an + b, where b = (7√5 − 17)/10 … Consequently, the path maximizes
  …". There is no restriction on `n`: the proof starts "For n ≤ 3, there is
  nothing to prove".
- **Constants:** `a = (5−√5)/10` (p. 8) and `b` match the manuscript.
- **Lemma 4.2, eq. (8):** matches the manuscript's formula verbatim. AMW
  takes it from their reference [1].
- **The 35 computer-checked cases:** introduced on p. 13 (case `k = 3`, i.e. a
  vertex of degree 3). On p. 15 AMW write that they "can all be checked easily
  with a computer". The citation pp. 13–15 is correct.
- **The strict form** `avm(P_n) > an + b ≥ avm(T)` is stated at the end of the
  proof on p. 16. This is correct.
- **Observation 1 (not a defect).** AMW p. 14 also relies on "an exhaustive
  case check" for branches of order at most 4. The manuscript's word
  "includes" is accurate but does not list all unpublished checks.
- **Observation 2.** AMW's bound is attained with equality by a non-path tree,
  the spider `S(K_{1,3})` of order 7 (AMW p. 15, and my exact computation:
  `avm − (7a+b) = 0`). The uniqueness of the maximizer therefore rests
  entirely on the strict inequality for the path. The manuscript argues it
  correctly.

**Strictness from eq. (8).**
- `(1−√5)/10 − b = (9−4√5)/5`, checked exactly in Q(√5).
  `(9−4√5)/5 > 0.011` is equivalent to `80 < 8.945² = 80.013`. True.
- For odd `N ≥ 5`, the absolute value of the last term at `N = 5` is
  `6/(√5(φ^{12}−1)) = (27−12√5)/20`, computed exactly. `< 0.0084` is
  equivalent to `26.832² = 719.956 < 720`. True, with a narrow margin.
- The sign of the last term by parity is correct: for even `N` the denominator
  `√5(−φ^{2N+2} − 1)` is negative, so the term is positive.
- **Unstated step.** That the absolute value decreases over odd `N` is not
  stated. It is immediate: consecutive odd `N` change the numerator by a
  factor at most 4/3 and the denominator by about `φ⁴ ≈ 6.85`. I do not count
  this as a gap.
- Conclusion: `avm(P_N) > aN + b` for `N ≥ 4`. Correct. It fails at `N = 1`
  and `N = 3`, where the path is the only tree.

**Quantifiers.**
- "Unique maximizer for every `N`" is correct: trivially for `N ≤ 3`, and by
  Theorem 4.4 together with the strict bound for `N ≥ 4`.
- `S(P_n) = P_{2n−1}`.
- `S(T)` keeps the degree of every original vertex, so it is a path only if
  `T` is.
- A tree `T ≇ P_n` needs `n ≥ 4`, so `N ≥ 7`.

**Conclusion.** The reduction is complete and correct, conditional on AMW
Theorem 4.4. That proof relies on computer and case checks that AMW do not
publish, and the manuscript says so in part.

#### (b) Section 12, item 1

- **Characterization.**
  - `p(P_n) = K := ⌈ξ − 2/5⌉` implies that every tree peaks no later than
    `P_n` (by Theorem 10.1).
  - `K = ⌊ξ⌋` exactly when `frac ξ < 2/5`. In that case `θ > 3/5` and
    Corollary 11.2(a) gives `p(P_n) = ⌊ξ⌋ = K`.
  - `p(P_n) = ⌈ξ⌉` forces `frac ξ > 4/5`, so `K = ⌈ξ⌉`.
  - Therefore `p(P_n) < K` if and only if `p(P_n) = ⌊ξ⌋` and `frac ξ > 2/5`.
  - All correct.
- **Example `n = 9`.** `ξ = 4.97508…`, `K = 5`, `⌊η⌋ = 4`,
  `h_9(4) = 320 + 32 − 16 − 2 − 324 = 10`. By Lemma 11.1, `p(P_9) = 5`. Correct.
- **Count.** Independent recount (see Reproduction): 806 orders in
  `[3, 2000]` with `p(P_n) < K`, the smallest being 3, 5, 7, 8, 10. The split
  is 799 / 393 / 806. This agrees with the manuscript.
- **Orders up to 23.** In both stored exhaustive files, `max_peak` equals
  `path_peak` for every order 3–23. `max_peak` is the largest *last*
  maximizing index over all trees (`exhaustive.py`, lines 50 and 60–61).
  The claim "for `n ≤ 23` it holds by the exhaustive computation" is
  therefore supported. Orders 21–23 come from a single implementation, which
  Section 13 discloses.
- **Defect.** See **D1**.

#### (c) Lemma 9.3, end of proof

- `tanh(3 log φ) = (φ⁶−1)/(φ⁶+1) = (8φ+4)/(8φ+6)`, using `φ⁶ = 8φ+5`. This
  equals `2/√5`, because `√5(8+4√5) = 2(10+4√5)`.
- `tanh(log φ) = (φ−φ⁻¹)/(φ+φ⁻¹) = 1/√5`, so `log φ = artanh(1/√5) > 1/√5`.
- Since `z tanh z` is increasing, `z tanh z > (3/√5)(2/√5) = 6/5 > 1` for
  `z ≥ 3 log φ`.
- The reduction of `ψ'' > 0` to `z tanh z > 1` was also re-derived:
  `ψ'' = γσ(1−σ)[γx(1−2σ) − 2]` with `1 − 2σ = tanh(γx/2)`.
- Everything is exact and correct.

#### (d) `R(K, ν)` (Section 12, item 3)

- Setting `ν = w e_u` gives `|ν| = w`, `j = a`, `M(K, w e_u) = M_w` and
  `p^ν = 1 + xτ − w x e_u = p^{(w)}`. So `R(K, w e_u) = R_w(K, u)` exactly
  (Section 5, line 479).
- `τ_v = 2 − k_v` is fixed by the explicit gloss `p^ν_v = 1 + (2 − k_v − ν_v)x`.
- The case `ν = e_u` is `R_1 ∈ K_{a+1}` (Theorem 7.1(iii)), and lies in
  `C_{a+1}` by Remark 7.8 (degree at most `a+1`). Correct.
- Sanity check with `j = 1`, `w = 2`: `R = 1 + 6x + 4x² = (1+x)² + 4x + 3x²`,
  which is in `C_2`.

#### (e) `φ` and Graham–Lovász

See rows 3 and 4 of the table above. The bibliographic entry
`GL78`, Adv. Math. 29 (1978) 60–88, is consistent with p. 83 being page 24 of
the scan.

### Checklist

| Item | Finding |
| --- | --- |
| Hypotheses | None of the Main Theorem's hypotheses is changed by revision 3. The hypotheses of Remark 9.6 (tree of order `n ≥ 2`; AMW Theorem 4.4 for all orders) are stated and used correctly. |
| Quantifiers | "Unique maximizer for every `N`" (Remark 9.6) is correct (see (a)). In item 1 the quantifier over orders (`p(P_n) = K` implies the claim for every tree of order `n`) is correct. The extent of "remains open" is misstated (D1). |
| Mathematical definitions | `φ` is defined. `R(K,ν)` is defined and agrees with `R_w` (see (d)). `avm` and `m_k` are defined. The local symbols `a`, `b`, `N` of Remark 9.6 reuse letters with other meanings elsewhere (`a = 1/g_X` in Lemma 9.4, `b = 2s+1` in Lemma 9.3). This is cosmetic. |
| Boundary cases | **Remark 9.6:** for `n = 2, 3` the claim is trivial; `N = 1, 3` fail the strict bound but have one tree; `N = 4` is even and positive; `N = 5` is the binding odd case (margin about 0.0028); `N = 2` is positive. **Item 1:** `n = 3` (one tree) is listed among the "open" orders, which is wrong as stated (D1). **Lemma 9.3:** the estimate is needed exactly at `z = 3 log φ` and is exact there. |
| Lemma 9.3 (end of proof, changed) | Correct, exact (see (c)). |
| Remark 9.6 (rewritten) | Correct. Every step was reconstructed (see (a)). The only unstated step is the monotonicity over odd `N`, which is trivial. |
| Section 12, item 1 (rewritten) | Characterization, example and count are correct. Wording defect D1. |
| Section 12, item 3 (rewritten) | Correct (see (d)). |
| Section 13 (tie; revision-3 item) | The tie (order 13, indices 6 and 7, value 189972) was reproduced by my own exact characteristic polynomial (Faddeev–LeVerrier over Q) of that tree. The stored exhaustive data show `trees_with_tied_maximum = 1` at order 13 and 0 at every other order 3–23. The external report (section 3) does record finding `d_6 = d_7 = 189972`, and says it did not check uniqueness. The manuscript attributes uniqueness to the separate recomputation, which is correct. The script's claims were reproduced (see Reproduction). Provenance defects D2 and D3. |
| Logical implications | Remark 9.6 shows: avm reduction + AMW 4.4 + strict path bound ⇒ Theorem 9.5, including the equality case. Item 1 shows: Theorem 10.1 + Lemma 11.1 + Corollary 11.2(a),(c) ⇒ the settled set. Both checked. |
| Changes touching the Main Theorem | Only the end of the proof of Lemma 9.3, which the Main Theorem uses via Lemma 9.4 → Theorem 9.5 → Theorem 10.1. Its new justification is correct and exact, so the chain is intact. The definition of `φ` matches every earlier implicit use. The (GP) and (D) items changed only provenance text. All other changes are in remarks, discussion, status or literature. The sentence "No step used by the Main Theorem changed" (Section 16) is therefore literally inaccurate (D5), though harmless. |
| Cross-references | Compiled with `pdflatex` three times (MiKTeX, output in a scratch directory). There were no undefined or multiply defined references. Label numbers: `lem:S44` = 9.3, `thm:T10` = 9.5, `rem:AMW` = 9.6, `lem:S46` = 9.7, `lem:S47` = 11.1, `cor:pathceil` = 11.2, `thm:T5` = 7.1, `rem:Ccone` = 7.8, `sec:rooted` = 5, `sec:minors` = 4, `sec:open` = 12, `sec:comp` = 13, `sec:status` = 16. Every new `\ref` points to the intended statement. "Lemmas 9.1–9.4 may be skipped" is correct: they are referenced only in Lemma 9.4, Theorem 9.5 and Section 13. |
| Dependency assumptions | Remark 9.6 depends on AMW Theorem 4.4, whose proof contains unpublished computer and case checks (pp. 13–15). This is disclosed in part. Lemma 4.2 eq. (8) is quoted from AMW's ref. [1]. I verified it independently and exactly. The Main Theorem does not depend on Remark 9.6. |
| Counterexample attempts | **Remark 9.6:** searched for a non-path tree with `avm ≥ avm(P_N)` over all trees of orders 2–13 with my own matching recursion. None found. The equality `avm(S(K_{1,3})) = 7a+b` shows the AMW bound is tight, but below `avm(P_7)`. **Spectrum claim:** rank of `A_{S(T)}` is `N − 1` for all 94 trees of orders 2–9 (no counterexample to "exactly one zero"). **Item 1:** for `n ≤ 60`, `p(P_n)` from the distance matrix agrees with Lemma 11.1, so no counterexample to the classification arises. |
| Formalization scope | Revision 3 changes no formal claim. Observation outside the diff: Section 14 does not mention the Lean formalization of the binomial statement of Lemma 7.5 (`StarShape.lean`, session 14, before revision 3). This understates rather than overstates. |
| Novelty coverage | **New Section 15 counts:** OpenAlex was queried by the reviewer today. `filter=cites:W2923064778` gives `meta.count` 14 (titles consistent with the matching and domination literature). `filter=cites:W2116451290\|W4243586797,publication_year:>2022` gives `meta.count` 63. Both counts are confirmed. The arXiv:2411.11488 abstract is consistent with "a rooted-spanning-forest formula … coefficients of the distance polynomial"; Theorem C numbering was not checked. The Chebotarev 2008 entry was not checked. **Own search:** one web search ("Collins Shor conjecture peak distance characteristic polynomial tree n − n/√5 proof"). Results: arXiv:1507.02341, 2104.14516, 2103.00647, 2206.07561, 2407.03309, 2207.03343. None resolves the conjecture; 2207.03343 is covered in the project dossier. No prior resolution was found within this single query. That is not evidence of novelty. "Theorem 9.5 is a rediscovery" is now stated plainly. No overstatement found in Section 15. |
| Unresolved gaps | None in the mathematics of the changes. Defects D1–D8 below are wording, status or provenance defects, not proof gaps. |

### Defects found

| ID | Location | Defect | Severity |
| --- | --- | --- | --- |
| D1 | Section 12, item 1 (lines 1652–1656) | "It remains open for the `n` with `p(P_n) < ⌈ξ−2/5⌉` … 806 of the `n` with `3 ≤ n ≤ 2000` (exact count), the smallest being 3, 5, 7, 8, 10; for `n ≤ 23` it holds by the exhaustive computation." The set counted is the set of orders *not settled by Theorem 10.1*, not the set of open orders. The orders cited as the smallest open ones are all settled: `n = 3` trivially (one tree), and all `n ≤ 23` by the stored exhaustive computation. Eleven of the 806 are at most 23 (3, 5, 7, 8, 10, 12, 14, 16, 19, 21, 23). Within `[3, 2000]` the question is actually open for **795** orders, the smallest being **25**. The count 806 is correct for what it counts; the sentence mislabels it, in the item whose purpose in revision 3 was to state "exactly which orders remain open". | Minor (statement imprecision in a discussion item not used by the Main Theorem) |
| D2 | Section 13, item "Revision 3" | It cites "result `results/amw-reduction-check.json`", which is **absent from revision `f695cbd`**. An untracked file with that name, recording `git_revision f695cbd` and `tree_clean true`, appeared in the working tree at 21:22:22, after the commit (21:21:10). It was committed later in `9f6c091`, where `main.tex` is unchanged. At the reviewed revision the reference does not resolve. Resolved at `9f6c091` (0 failures, 806). | Minor (provenance) |
| D3 | Section 13, item "Revision 3", last sentence | "eq. (8) of [AMW] was compared with the exact value of `avm(P_N)` for `N ≤ 80` in 60-digit floating point (exploratory; agreement to 50 digits)". No script or command in the repository performs this comparison. I searched every `*.py` for `avm`, `1903.09825`, `mpmath`, and Decimal precision settings: `amw_reduction_check.py` has no such part, and the only 60-digit code is unrelated. As recorded, the check is not reproducible. This review's exact check (eq. (8) holds identically in Q(√5) for `N = 1…120`) supersedes it, but the manuscript's sentence still has no recorded command. | Minor (provenance) |
| D4 | Notice box (lines 101–105) and Section 16 (lines 1884–1885) | The box says revision 3 "has been rechecked only as stated in Section 16". Section 16 says only "The recheck of revision 3 is recorded in the project's journal, not here." At `f695cbd` no review of revision 3 exists in `reviews/`, and this review began after the commit. The document asserts a completed recheck that no review record at that revision supports. Its reader is also referred to a journal that is not part of the document. Not checked: whether the journal at `f695cbd` records anything, because I was instructed not to read it. | Minor (status overstatement or circular reference) |
| D5 | Section 16, line 1883 | "No step used by the Main Theorem changed." The end of the proof of Lemma 9.3 was rewritten, and the Main Theorem uses it (Lemma 9.3 → 9.4 → Theorem 9.5 → Theorem 10.1). The new argument is correct, so nothing breaks, but the sentence is inaccurate as worded. Something like "no step changed in substance; the justification of the last estimate of Lemma 9.3 was made exact" would be accurate. | Minor (wording) |
| D6 | Section 16, lines 1877–1883, and the header comment (lines 13–20) | "corrects all six:" is followed by a list that merges findings 1 and 5 of the external report into one item and adds the Lemma 9.3 estimate. That estimate was a suggestion in section 2 of the report, not one of its six classified findings. All six findings are addressed, but the list does not map onto them. | Cosmetic (bookkeeping) |
| D7 | Notice box, lines 97–99 | "Its parts were reviewed only by AI reviewers … (models of the same vendor)" now sits next to the new sentence saying revision 2 was reviewed by a model of another vendor. It is readable as a contradiction, unless "parts" is understood as the component reviews listed in Section 16. | Cosmetic |
| D8 | Remark after Lemma 9.7 (lines 1448–1451; unchanged in revision 3) | "(not checked by a reviewer)" is now stale. With the identity of Remark 9.6, Lemma 9.7 follows from eq. (8) for `P_{2n−1}`. I checked this algebraically: `n − avm(P_{2n−1}) = n/√5 + 2/5 + 2n/(√5(φ^{4n}−1))`, which equals the formula of Lemma 9.7. | Cosmetic (outside the diff) |

## Reproduction

All commands were run on the working tree, whose `main.tex` and
`amw_reduction_check.py` are byte-identical to `f695cbd`.

1. **Project script.**
   `uv run python experiments/CJ-0001-collins-shor-peak/amw_reduction_check.py`
   (no `--out`, so nothing was written) ran in 15.1 s with
   `failures_total: 0`:
   - A: 94 trees of orders 2–9, 0 failures.
   - B: 32,507 trees of orders 2–16, 0 failures. Both counts agree with
     A000055.
   - C: 197 values of `N` (4–200), 0 failures.
   - D: 799 / 393 / **806**; first open orders 3, 5, 7, 8, 10, 12, 14, 16,
     19, 21; first ceiling cases 9, 18, 27, …
   - E: 1,301 trees of order 13, one tie, indices [6, 7], value 189972.

   `uv run pytest -q tests/test_cj0001_amw_reduction.py`: 4 passed.

   I read the script. Part C's identity
   `10(avm − aN − b) = (10avm − 5N + 17) + √5(N−7)` is correct, `sign_q5` is
   correct, and the formula for `⌈ξ−2/5⌉` (`n − ⌊η + 2/5⌋`, tested via
   `(5j−2)² ≤ 5n²`) is correct.

2. **Independent code, subdivision and AMW.** The script
   `indep_amw.py` (scratch directory, not stored in the repository) does not
   import the project's modules.
   - Matchings by edge deletion–contraction.
   - `det(λI − L_T)` by exact Faddeev–LeVerrier over Q, so that
     `[t^k] det(I + tL) = (−1)^k c_k`.
   - `tr(I+L)^{-1} = −p'(−1)/p(−1)`.
   - Rank of `A_{S(T)}` by exact Gaussian elimination.

   Results:
   - Subdivision identity and avm identity: 94 trees of orders 2–9, 0
     failures.
   - Rank `N − 1` (exactly one zero eigenvalue): 0 failures.
   - Path as unique avm maximizer: 2,287 trees of orders 2–13, 0 failures.
   - AMW eq. (8): exact equality in Q(√5) for `N = 1…120`, 0 mismatches.
   - `avm(P_N) > aN + b`: true for every `N` in 4–400. The signs for
     `N = 1…6` are `−, +, −, +, +, +`.
   - Constants exact:
     - `(1−√5)/10 − b = (9−4√5)/5`;
     - `6/(√5(φ^{12}−1)) = 27/20 − (3/5)√5`;
     - both decimal bounds checked by integer squaring.
   - `avm(S(K_{1,3})) = 7a + b` exactly.

3. **Independent code, open-order count.** The script `indep_open.py`
   (scratch directory, about 3 minutes) does not use `h_n`. It computes
   `p(P_n)` as the argmax of Collins's closed form (C) over exact rationals,
   and checks it for `n ≤ 60` against the argmax of the normalized
   coefficients of the distance matrix of `P_n` (python-flint exact
   characteristic polynomial; 0 mismatches). `⌈ξ − 2/5⌉`, `⌊ξ⌋` and
   `frac ξ` versus `2/5` are computed by exact integer inequalities and
   cross-checked with 80-digit Decimal.

   Results:
   - Counts 799 / 393 / **806**.
   - First open orders 3, 5, 7, 8, 10, 12, 14, 16, 19, 21, 23, 25.
   - Open orders `≤ 23`: 3, 5, 7, 8, 10, 12, 14, 16, 19, 21, 23 (eleven
     orders), hence D1.
   - `n = 9`: `K = 5`, `h_9(4) = 10`, `p = 5`.

4. **Order-13 tie.** My own exact characteristic polynomial (Faddeev–LeVerrier
   over Q) of the distance matrix of the tree with edges
   `{01, 02, 06, 17, 1·11, 23, 34, 35, 78, 7·10, 89, 11·12}` gives maximizing
   indices [6, 7] and value 189972.

5. **Exhaustive data.** In `exhaustive-03-20.json` and `exhaustive-21-23.json`:
   - `max_peak == path_peak` for each order 3–23;
   - tree counts are the A000055 values;
   - `trees_with_tied_maximum` is 1 at order 13 and 0 elsewhere;
   - the total is 23,942,357.

6. **Typesetting.** `pdflatex` was run three times with output in the scratch
   directory. Exit code 0, no undefined references; label numbers as listed
   above.

7. **Sources consulted.**
   - arXiv:1507.02341v3, pp. 1–3 (page images).
   - arXiv:1903.09825v1, pp. 6–18 (page images): Lemma 4.2 and eq. (8),
     Theorem 4.4, the proof pp. 9–16 including the 35 cases (pp. 13–15) and
     the strict form (p. 16), Section 5 and Lemma 5.1 (p. 17).
   - Graham–Lovász (1978), scan p. 83.
   - OpenAlex API, two queries.
   - arXiv:2411.11488, abstract page.
   - One web search.

   Not checked: the Graham–Pollak scan (the dossier records the reading); the
   journal version of AMW; Chebotarev (2008); Theorem C of arXiv:2411.11488.

## Verdict

**`no gap found within stated scope`**

**Scope.** Every hunk of the revision-3 changes to
`manuscripts/CJ-0001-collins-shor/main.tex` (`87c3c8c` → `f695cbd`, file
SHA-256 `3477baa0…917b`), read in context, together with the computations of
Section 13 that revision 3 added.

**Main conclusions.**
- All six findings of the external review of revision 2 are corrected.
- The corrections that carry mathematics are correct: Remark 9.6, Section 12
  items 1 and 3, the exact estimate in Lemma 9.3, and the AMW-based strictness
  argument. Every step was reconstructed by the reviewer.
- The only change that touches the chain of the Main Theorem (the end of the
  proof of Lemma 9.3) is correct.
- Defects D1–D8 are wording, status and provenance defects:
  - D1–D5 are minor;
  - D6–D8 are cosmetic;
  - none is a gap in a proof.

**What this verdict does not cover.**
- Sections 2–11, except where revision 3 changed them or a changed passage
  depends on them.
- The correctness of AMW's proof of Theorem 4.4, including its unpublished
  computer and case checks.
- The novelty of any result.
- Lean sources.
- Records outside `main.tex` (STATE.md, journal, registry), which were not
  read.

**Independence.** Independence is limited: the reviewer is the same model as
the author of the text. This is an AI review, not peer review. It applies only
to revision `f695cbd`, whose `main.tex` is unchanged at `9f6c091`.
