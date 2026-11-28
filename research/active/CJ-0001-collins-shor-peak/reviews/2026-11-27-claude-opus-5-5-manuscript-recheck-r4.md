# Independent review — CJ-0001 — manuscript revision 4 (changes since revision 3, and Lemma 11.3)

- **Reviewer:** Claude, model `claude-opus-5-5` (Anthropic), adversarial reviewer role.
- **Date:** 2026-11-27, about 21:42 to 21:52 local time (by `date`).
- **Independence:** fresh subagent context. It received the director's task
  statement, the commit identifiers and the file hash, not the author's
  reasoning.

  **Limits on independence.**
  - The reviewer is the same model and vendor as the author of the
    manuscript text (`claude-opus-5-5`).
  - The reviewer is the same model as the reviewer of revision 3, whose
    report (the D1–D8 table) was part of the task.

  **Reading order.**
  - Not read: the session-15 journal entry, `STATE.md`, and
    `reviews/2026-11-27-codex-gpt-astra-6-manuscript-r2.*`.
  - Read only after the reviewer's own checks of Lemma 11.3 were complete
    (derivation, own code, project script): `notes/path-formula.md` and the
    checklist and verdict of `reviews/2026-11-27-claude-sonnet-5-5-path-formula.md`.
- **Revision reviewed:** commit `4b021468b854bd88f3a7a0e002f79fb617d3b909`
  (revision 4), compared with `f695cbd` (revision 3).

  Files reviewed, all with their SHA-256 at `4b02146`:

  | File | SHA-256 |
  | --- | --- |
  | `manuscripts/CJ-0001-collins-shor/main.tex` | `5e0957a406004a83628c91fe007dd3fb06829cf347baf260f857a1144d1bf4ab` |
  | `experiments/CJ-0001-collins-shor-peak/path_formula_check.py` | `ee5f524e94c1a72a28dc8ff92949ba6120ef915bba421497ee23924b7654e512` |
  | `experiments/CJ-0001-collins-shor-peak/results/path-formula-check.json` | `a74c3c1e29990e9d567c500b33f18cdc6490cd4ef02c34effde3487dfb16d826` |
  | `experiments/CJ-0001-collins-shor-peak/results/amw-reduction-check.json` | `17b4e8ef5f14957c522422be8464bc3dd6e7e337b05edb15708aa86530648567` |
  | `formalization/Conjectura/Research/CollinsShorPeak/StarShape.lean` | `7d8a9007e3178a33329de130849014d684cf91926a132fc9bbdc2f5b0ddb7aa0` |
  | `manuscripts/CJ-0001-collins-shor/versions/r3/main.tex` | `3477baa0…917b` |

  - The hash of `main.tex` is the same in the working tree.
  - It is also unchanged at `f37b2ad`, a records-only commit that appeared
    during this review.
  - The frozen copy `versions/r3/main.tex` is byte-identical to revision 3 at
    `f695cbd`, as the header claims.
- **Material given to the reviewer:**
  - the task statement;
  - the repository;
  - the revision-3 recheck `reviews/2026-11-27-claude-opus-5-5-manuscript-recheck-r3.md`,
    for the D1–D8 table.

  The primary statement (arXiv:1507.02341, Conjecture 1.2) was not refetched.
  Its reading below is the one recorded from page images in the revision-3
  recheck by the same reviewer model, and it agrees with the manuscript's
  verbatim quotation (line 144).
- **Scope:**
  - every hunk of `git diff f695cbd 4b02146 -- manuscripts/CJ-0001-collins-shor/main.tex`
    (125 insertions, 32 deletions), read in context;
  - Lemmas 2.1, 2.2, 4.1–4.3 and Section 11, as far as Lemma 11.3 uses them;
  - the cited result files, the script and the Lean file named in Section 14.

## Statement as read from the primary source

Aalipour et al., arXiv:1507.02341, p. 2. For a tree `T` of order `n`, let
`δ_k` be the coefficient of `x^k` in `det(D − xI)`. The normalized
coefficients are `d_k(T) = 2^k |δ_k| / 2^{n−2}` for `0 ≤ k ≤ n−2`.

**Conjecture 1.2 (Collins–Shor), p. 3.** The normalized coefficients of every
tree of order `n` are unimodal with peak between `⌊n/2⌋` and `⌈n − n/√5⌉`.

- Quantifiers: every tree `T` of order `n ≥ 3`.
- How a tie is read is not fixed by the source. The manuscript proves the
  reading in which every maximizing index is bounded.

The manuscript defines `d_k = 2^{k−(n−2)}|δ_k|` (line 126), which is the same
quantity.

**Statement of Lemma 11.3 (written down before reading its proof).**

- For the path `P_n`, `n ≥ 2`, and `2 ≤ k ≤ n`:
  `d_{n−k}(P_n) = C(n+k−1, 2k−1)·(k−1)n/k`.
- The index `j = n − k` runs over exactly `0..n−2`, the full range of the
  `d_j`.
- For `n ≥ 3` this is item (C) of Section 2, which is Collins 1989,
  Theorem 3.
- The lemma also covers `n = 2`, where it says `d_0 = 1`. This is true:
  `det(D − xI) = x² − 1`.

## Findings

### Lemma 11.3, step by step (own derivation)

**Conventions.** They agree with Sections 2 and 4.

- Section 2 defines `M = I + xL`, `Φ_T = det M` and `τ_v = 2 − k_v`, and
  `ℓ_T = −2^{−(n−2)} det(2xI − D)`.
- Section 4 defines `M(K,ν) = I + x(L_K + diag ν)` with `ν ∈ Z_{≥0}^U`, so
  `ν = 0` is allowed and `M(K,0) = M`.
- The lemma's `Φ_n` is `Φ_{P_n}`. `A_n = det M[V∖{1}]` is new local notation.

**Step 1.** Reconstructed.

- For `n ≥ 3`, the ends of the path have degree 1 and inner vertices degree
  2, so `τ = e_1 + e_n`. For `n = 2` both vertices have degree 1, so again
  `τ = e_1 + e_n`.
- `M` is symmetric, so `τᵀ adj(M) τ = adj_11 + adj_nn + 2 adj_1n`.
- `adj_11 = det M[V∖{1}] = A_n`. The reversal `i ↦ n+1−i` is an automorphism
  of the path, so `adj_nn = A_n`.
- **The cofactor `adj_1n`.** Lemma 4.3 with `(K,ν) = (P_n, 0)`, `v = 1`,
  `v' = n`, `d = n−1`, `Q = ∅` gives `x^{n−1} det M[∅] = x^{n−1}`.
  - Lemma 4.3's first equality needs only `d ≥ 1`, `x > 0` and positive
    definiteness, all of which hold for `ν = 0`.
  - Its membership part calls Lemma 4.2 only on components with weight
    `ν|_{K'} + e_a ≠ 0`, and here there are none.
  - Direct check: the minor is triangular with `n−1` entries `−x`, so
    `(−1)^{1+n}(−x)^{n−1} = x^{n−1}`.
- Lemma 2.2 then gives `ℓ = (n−1)Φ_n − 2xA_n − 2x^n`.
- For `0 ≤ j ≤ n−2`, the `x^n` term does not contribute, and
  `[x^{−1}]A_n = 0`. Lemma 2.1 (valid for `n ≥ 2`) then gives
  `d_j = (n−1)[x^j]Φ_n − 2[x^{j−1}]A_n`. Correct.

**Step 2 (forest expansion).** Reconstructed.

- `L = BBᵀ` for any orientation, and `M[W] = I + xB_W B_Wᵀ`.
- Sylvester's identity gives `det(I_{|E|} + x B_Wᵀ B_W)`.
- The displayed double sum follows from one application of Cauchy–Binet to
  `[I_E | √x B_Wᵀ]` times its transpose. It also follows from the
  principal-minor expansion of `det(I + xG)` combined with Cauchy–Binet on
  each `G[S]`. The text names only "Cauchy–Binet"; either route is standard,
  so this is not a gap.
- **Block structure.** Every edge of `S` lies in one component of the
  spanning forest `(V,S)`, and a vertex row meets only the edges of its own
  component. So `B[R,S]` is block diagonal with blocks
  `(R∩C_i) × (S∩E(C_i))`, of size `|R∩C_i| × (|C_i|−1)`.
- **Singularity.** The row and column totals are equal. If any block is not
  square, some block has more rows than columns, its rows are dependent, and
  the matrix is singular. Correct.
- **Unimodularity.** Each square block is the incidence matrix of a tree with
  one row `o` removed.
  - A tree with at least 2 vertices has at least 2 leaves, so there is a leaf
    other than `o`.
  - The row of that leaf has a single `±1`.
  - Expanding along that row leaves the incidence matrix of the tree minus
    the leaf, still without row `o`.
  - Induction ends at a single vertex: a 0×0 block with determinant 1.
  - The determinant is therefore `±1`. Correct.
- Isolated vertices give 0×0 blocks, and `R` must omit them.
- **Counting.**
  - `W = V` gives `Π|C_i|`.
  - `W = V∖{u}` forces `u` to be the omitted vertex of its own component,
    which gives `Π_{u∉C_i}|C_i|`.
  - `S = ∅` gives the constant term 1.
  - Correct.

**Step 3.** Reconstructed.

- Edge sets of `P_n` with `r` components correspond bijectively to the
  compositions of `n` into `r` parts (cut `r−1` of the `n−1` edges), with
  `|S| = n − r`.
- `[x^{n−r}]Φ_n = Σ Πc_i = [z^{n−r}](1−z)^{−2r} = C(n+r−1, 2r−1)`.
- Vertex 1 lies in the first part, so
  `[x^{n−r}]A_n = [z^n] z^r(1−z)^{−(2r−1)} = C(n+r−2, 2r−2)`.
- The `r = 1` term is `C(n−1, 0) = 1`. This is the leading coefficient of
  the `(n−1)×(n−1)` determinant `A_n`, as it must be.
- For `r > n` both binomials vanish by the convention `C(i,k) = 0` unless
  `0 ≤ k ≤ i`.

**Step 4.** Reconstructed.

- `r = k` gives `C(n+k−1, 2k−1)`.
- `r = k+1` gives `C(n+k−1, 2k) = C(n+k−1, 2k−1)(n−k)/(2k)`. For `k = n`:
  `C(2n−1, 2n) = 0 = [x^{−1}]A_n`.
- Then `(n−1) − (n−k)/k = n(k−1)/k`.
- Boundary cases:
  - `k = n`: `d_0 = n−1`, which agrees with Graham–Pollak.
  - `k = 2`: `d_{n−2} = C(n+1, 3)·n/2`.
  - `n = 2`: `d_0 = 1`.

**Circularity.** There is none.

- Lemma 11.3 uses Lemma 2.1 (the sign fact of GL78/AAB), Lemma 2.2 ((GL),
  (GP)), Lemma 4.3 (Lemmas 4.1 and 4.2 and the cones) and Cauchy–Binet.
- None of these uses Section 11 or (C).
- Lemma 11.1 cites (C) for `n ≥ 3`. Lemma 11.3 proves it for `n ≥ 2`. The
  forward reference is harmless.

**Transcription.** Compared after the reviewer's own checks: the
manuscript's proof matches `notes/path-formula.md` step by step.

- The notes argue singularity from a block with fewer rows than columns; the
  manuscript argues from a block with more rows than columns. Both are valid.
- The notes' review (`claude-sonnet-5-5`, commit `e15ae8f`) gives
  `no gap found within stated scope`, as Section 16 states.

### The eight defects of the revision-3 recheck

| ID | Corrected? | Assessment |
| --- | --- | --- |
| D1 | In substance, yes | Recount below. The numbers 806, 11, 795 and 25 are all right, but the list of the eleven orders is wrong as written (**N1**). |
| D2 | Yes | `results/amw-reduction-check.json` is in the tree at `4b02146`. Its run block records `git_revision f695cbd…`, `tree_clean: true`, as the new sentence says. |
| D3 | Yes | The sentence on the 60-digit floating-point comparison was deleted. No remaining claim without a command was found (`grep digit`: no match). |
| D4 | Yes | The notice box now refers to Section 16. Section 16 states the recheck of revision 3, with its model, scope, verdict and number of defects, all of which agree with the recheck report. It also states that the transcription of Lemma 11.3 and the other changes of revision 4 are not rechecked. That is accurate at `4b02146`: no review of revision 4 existed before this one. |
| D5 | Yes | Section 16 now states that the end of the proof of Lemma 9.3 ("Lemma S44") is a step used by the Main Theorem through Theorem 9.5, and that it was made exact. "No other step … changed" is accurate. The revision-4 claim "No step used by the proof of the Main Theorem changed" was checked hunk by hunk. It is accurate: the changes are in the notice box, (C), remarks, the new Lemma 11.3, and Sections 12–16. |
| D6 | Partly | Section 16 now maps the six findings correctly: 1 and 5 merged, then 3, 4, 2 and 6, plus the suggestion on Lemma 9.3. The header comment's revision-3 entry (lines 13–20) is unchanged and still lists "all six" with the Lemma S44 suggestion among them (**N2**; not typeset). |
| D7 | Yes | The new notice box has no contradiction: "its parts and its first versions by models of the author's vendor, revision 2 as a whole also by a model of another vendor". |
| D8 | Yes | "(checked by the reviewer of revision 3)" is accurate: the revision-3 recheck checked it algebraically. The identity is also sound: `S(P_n) = P_{2n−1}` and Remark 9.6 give `tr(I+L_{P_n})^{−1} = n − avm(P_{2n−1})`. I verified this exactly for `n = 1..15` (own code). |

### Checklist

| Item | Finding |
| --- | --- |
| Hypotheses | Lemma 11.3: `n ≥ 2` and `2 ≤ k ≤ n` are exactly what Lemmas 2.1 and 2.2 need, and they give the full index range `0..n−2`. No hidden hypothesis. The cited Lemma 4.3 allows `ν = 0`. |
| Quantifiers | Correct. "For every `n ≥ 2` and every `k` in `[2,n]`" is proved for all cases, with no case split needed except `k = n` (handled). |
| Mathematical definitions | `M`, `Φ`, `τ` and `ℓ` agree with Section 2, and `M(K,0)` with Section 4. New local symbols reuse letters: `E` (edge set) versus the matrix unit `E_uu` of the Conventions; `A_n` versus `A = −M` in the proof of Lemma 2.2; `R`, `S`, `W`. All are cosmetic (**N7**). |
| Boundary cases | All correct (Step 4 above): `n = 2` (`τ = e_1 + e_2`, `adj_12 = x`, `d_0 = 1`); `k = n` (`[x^{−1}]A_n = 0 = C(2n−1, 2n)`, `d_0 = n−1`); `k = 2`; `S = ∅`; isolated vertices; `r = 1` and `r > n`. |
| Lemma 11.3, Step 1 | Correct, reconstructed. |
| Lemma 11.3, Step 2 | Correct, reconstructed. The principal-minor or Cauchy–Binet step is compressed but standard. |
| Lemma 11.3, Step 3 | Correct, reconstructed. |
| Lemma 11.3, Step 4 | Correct, reconstructed. |
| Section 12, item 1 (D1) | Count correct. Listing of the eleven orders wrong (N1). |
| Section 13 (revision 3 and revision 4 items) | Files exist at `4b02146`, and the run blocks match the text: amw at `f695cbd` (clean); path formula at `e15ae8f` (clean, `--max-n 60`, 59 cases, 0 failures). The script is unchanged between `e15ae8f` and `4b02146`. The distance-matrix claim for `n = 2` is not what the script does (N3). |
| Section 14 | The StarShape description is accurate in substance. `StarShape.lean` proves (a) `c(k−1) < c(k)` for `1 ≤ k ≤ ⌊n/2⌋` and (b) `c(k) < c(k−1)` for `⌊n/2⌋+1 ≤ k ≤ n−2`, for `c` as written, with no link to `d_k(S_n)`. Two imprecisions (N5): the range `k ≤ n−2` is missing, and the list of formalized statements omits two modules. Both understate rather than overstate. |
| Section 15 | "whether this proof is in the literature was not searched" is honest. The forest expansion itself is classical and is not attributed (N6). |
| Section 16, notice box, Limitations | Accurate about what is and is not reviewed (D4, D7). One wording point in the notice box (N8). |
| Logical implications | Steps 1–4 imply Lemma 11.3. Lemma 11.3 implies (C) for `n ≥ 3`, which implies Lemma 11.1 and Corollary 11.2. The claim "Section 11 no longer needs (C) as a citation" holds. Section 11 still depends on (GL), (GP) and the GL78 sign fact through Lemmas 2.1 and 2.2, which the Main Theorem cites anyway. |
| Dependency assumptions | Lemma 11.3 depends on: (GL), cited, read in a scan with two signs fixed; (GP), cited; the GL78 sign fact via AAB Fact 1.1; Lemma 4.3. The summaries "from Lemmas L1 and path" in Section 11 and Section 16 omit Lemma 2.1 (N7; the proof itself cites it). |
| Counterexample attempts | None found. Lemma 11.3 was tested against the distance matrix for `n = 2..22`. Step 2 was tested on 300 random trees with random `W` (not only `V∖{u}`), using the general count for a component `C`: `|C|` if `C ⊆ W`, 1 if `|C∖W| = 1`, 0 otherwise. The unimodularity claim was tested on 500 random oriented trees. All without failure. |
| Formalization scope | Revision 4 changes no Lean file: `formalization/` is unchanged between `8cbc015` (receipt `20261127T213151Z-8cbc0151bc-passed.json`) and `4b02146`. `verify_lean.py` was **not** rerun in this review. No Lean claim concerns Lemma 11.3. |
| Novelty coverage | One web search (standard mode) for a resolution of the Collins–Shor peak conjecture (query: Collins–Shor, distance characteristic polynomial, tree, peak, `⌊n/2⌋`, `n − n/√5`, proof). It returned arXiv:1507.02341 (v1–v3), 2103.00647, 2207.03343, 2104.14516, an NSYSU copy of the EJLA version and a CORE PDF. None proves the peak-location statement. No search was made for prior proofs of Collins's formula by forest expansion. Nothing here supports a novelty claim. |
| Unresolved gaps | None in the mathematics of the changes. N1–N8 are defects of wording, provenance, attribution and typesetting. |

### Defects found

| ID | Location | Defect | Severity |
| --- | --- | --- | --- |
| N1 | Section 12, item 1, line 1724 | "Eleven of them, `3,5,7,\dots,23`". The ellipsis reads as the odd integers 3 to 23. There are also exactly eleven of those, and they include 9, which the same item shows is reached by Theorem 10.1 (`p(P_9) = 5 = ⌈ξ−2/5⌉`). They also include 11, 13, 15 and 17, and omit 8, 10, 12, 14 and 16. The eleven orders not reached by the argument are 3, 5, 7, 8, 10, 12, 14, 16, 19, 21, 23 (own recount). This was the item that the D1 correction was meant to make exact. | Minor (statement imprecision in a discussion item not used by the Main Theorem) |
| N2 | Header comment, lines 13–20 (revision-3 entry) | Residue of D6. It still says "all six:" and lists the Lemma S44 decimal estimate among them, merging findings 1 and 5. Section 16 was corrected; the comment was not. | Cosmetic (not typeset) |
| N3 | Section 2 item (C) (line 307), remark after Lemma 11.3 (lines 1703–1705), Section 13 item "Revision 4" (lines 1814–1819) | These say that Lemma 11.3 or (C) was checked against the distance matrix for `2 ≤ n ≤ 60`. `path_formula_check.py` compares with the normalized `|δ_j|` of `det(D − xI)` only under `if n >= 3:`. At `n = 2` it checks only `ℓ` (computed from `det(2xI − D)`) against the identity of Step 1, plus the coefficients of `Φ_2` and `A_2`. The statement at `n = 2` is true (own check, via `|δ_0|`), but the stored run does not do what the text says at `n = 2`. | Cosmetic (provenance) |
| N4 | Lemma 11.3, Step 3 display (source line 1691; PDF p. 27) | Overfull `\hbox` by 121 pt. The second equation runs into the right margin. | Cosmetic (typesetting) |
| N5 | Section 14, lines 1825–1834 | (i) "rise strictly up to `⌊n/2⌋` and fall strictly after it" omits the range `k ≤ n−2`. The Lean theorem has this range (as does Lemma 7.5), and beyond it the statement is false: `c(n) = −4 < 0 = c(n+1)`. (ii) The sentence lists what is formalized in `formalization/…/CollinsShorPeak/` and omits `VertexPrinciple.lean` and `ExtremalReduction.lean` (discrete core of the "vertex principle" L4 and one exchange step), which are in that directory. Both points understate or are imprecise; neither overstates. | Cosmetic |
| N6 | Remark after Lemma 11.3 (lines 1700–1701); Section 15, last bullet; Appendix A | (i) Step 2 is called "the matrix-forest expansion" but no source is cited for it, although `[CS06]` (Chebotarev–Shamis, *Matrix-forest theorems*) is already in the bibliography. Section 15 does not list the expansion among the known results reproved. (ii) Appendix A has no row for Lemma 11.3 (`notes/path-formula.md`; review `2026-11-27-claude-sonnet-5-5-path-formula.md`). | Cosmetic (attribution and provenance) |
| N7 | Lemma 11.3 and its introduction; Section 16 | The dependency summaries ("from Lemmas 2.2 and 4.3 and the Cauchy–Binet formula"; "from Lemmas L1 and path") omit Lemma 2.1, which the proof uses. Local notation reuses `E`, `A`, `R`, `S`, `W`, which have other meanings elsewhere in the text. | Cosmetic |
| N8 | Notice box, lines 107–109 | "None of these reviews found a gap". This matches the verdicts (`no gap found within stated scope`). But Section 16 records that the reviews of the first version found "two errors in remarks or proofs not used by the Main Theorem", and that the external review of revision 2 found an error in a remark. Something like "none found a gap in the proof of the Main Theorem; the errors and defects they reported were corrected" would not invite the reading "no error found". | Cosmetic (status wording) |

## Reproduction

All runs were on the working tree. `main.tex` and `path_formula_check.py`
there are byte-identical to `4b02146`.

1. **Independent exact code for Lemma 11.3.** Script `indep_collins.py` in
   the reviewer's scratch directory. It is not stored in the repository and
   imports nothing from the project.
   - Method: Bareiss determinants over `Fraction`, evaluation at integer
     points and Lagrange interpolation.
   - Run as `uv run --no-project python -I indep_collins.py 15`
     (10.5 s, 0 failures) and with argument `22` (115 s, 0 failures).
   - For every `2 ≤ n ≤ 22` it checks:
     - the Step 3 coefficients of `Φ_n` and `A_n` for `1 ≤ r ≤ n+1`;
     - the Step 1 identity, coefficient by coefficient up to `x^n`;
     - `adj(M)_{1n} = x^{n−1}` by the signed cofactor;
     - `adj_nn = A_n`;
     - Lemma 11.3 against `d_j = 2^{j−(n−2)}|δ_j|` from `det(D − xI)` of the
       BFS distance matrix, for every `k` in `[2,n]`, **including `n = 2`**;
     - `[x^j]ℓ = d_j` (Lemma 2.1).
   - Step 2 for a general `W`: 300 random trees of order 1–8 with random
     `W ⊆ V`, 0 failures.
   - Incidence matrix of a tree with one row removed has `|det| = 1`: 500
     random oriented trees of order 1–9, 0 failures.
2. **Project script.**
   `uv run python experiments/CJ-0001-collins-shor-peak/path_formula_check.py`
   (default `--max-n 40`, no `--out`, nothing written), 7.9 s:
   - `cases 39, failures 0`;
   - `composition_sums: cases 144, failures 0`.

   I read the script. It checks (a)–(e) as its docstring says, with one
   exception: (d), the comparison with `|δ_j|`, runs only for `n ≥ 3` (N3).
   The (b) test also asserts `len(A) == n` (degree `n−1`).

   The stored result `results/path-formula-check.json` records:
   - command `--max-n 60 --out …`, revision `e15ae8f`, `tree_clean: true`;
   - 59 cases, 0 failures; 144 composition cases, 0 failures.

   The script is unchanged between `e15ae8f` and `4b02146`.
   `uv run pytest -q tests/test_cj0001_path_formula.py`: 3 passed.
3. **D1 recount.** Script `d1count.py` (scratch directory), integer
   arithmetic.
   - `p(P_n) = n − k_0(n)` by Lemma 11.1, cross-checked for `n ≤ 60` against
     the argmax of the closed form.
   - `⌈ξ − 2/5⌉ = n − max{j : (5j−2)² < 5n²}`.
   - Results, over `3 ≤ n ≤ 2000`:
     - **806** orders with `p(P_n) < ⌈ξ−2/5⌉`;
     - **11** of them are ≤ 23: `3, 5, 7, 8, 10, 12, 14, 16, 19, 21, 23`;
     - **795** are above 23, the smallest **25** (then 28, 30, 32, 34);
     - `n = 9` is not among them (`p(P_9) = 5 = K`).
   - The odd numbers 3 to 23 are also eleven in number, hence N1.
   - In `results/exhaustive-03-20.json` and `exhaustive-21-23.json`,
     `max_peak == path_peak` for every order 3–23. So the eleven orders ≤ 23
     are settled by that computation, as stated.
4. **D8 identity.** Script `d8.py` (scratch directory):
   `tr(I+L_{P_n})^{−1}` by exact Gauss–Jordan elimination equals
   `n − avm(P_{2n−1})` (matching polynomial of the path by recursion) for
   `n = 1..15`.
5. **Typesetting.** The file `main.tex` at `4b02146` was compiled with
   `pdflatex` three times (MiKTeX) in a scratch directory.
   - Exit code 0.
   - No undefined or multiply defined references; no LaTeX warnings.
   - Ten overfull boxes; the only one in revision-4 text is at line 1691
     (N4).
   - Label numbers: `lem:ident` 2.1, `lem:L1` 2.2, `lem:path` 4.3,
     `lem:starshape` 7.5, `rem:AMW` 9.6, `lem:S46` 9.7, `sec:path` 11,
     `lem:S47` 11.1, `lem:collins` 11.3, `sec:open` 12, `sec:comp` 13,
     `sec:formal` 14, `sec:literature` 15, `sec:status` 16.
   - Every new `\ref` points to the intended object. The PDF page with
     Lemma 11.3 (p. 27) was inspected visually.
6. **Lean.** `StarShape.lean` at `4b02146` was read in full (statement,
   encoding, theorems `starCoeff_lt_of_le_half`, `starCoeff_lt_of_half_lt`).
   The directory listing was checked.
   - `formalization/` has no diff between `8cbc015` (last passing receipt)
     and `4b02146`.
   - `scripts/verify_lean.py` was **not run** in this review.
7. **Not checked.**
   - Collins 1989 and his thesis: the description "Collins's proof goes
     through the counting of his thesis" was not verified.
   - The journal version of AAB.
   - Literature on the Laplacian coefficients of paths, or on forest-expansion
     proofs of (C).

## Verdict

**`no gap found within stated scope`**

**Scope.** This verdict covers:

- every hunk of the revision-4 changes to
  `manuscripts/CJ-0001-collins-shor/main.tex`
  (`f695cbd` → `4b02146`, SHA-256 `5e0957a4…bf4ab`), read in context;
- the complete proof of Lemma 11.3 (Collins's formula), every step of which
  was reconstructed by the reviewer and checked by independent exact code for
  `2 ≤ n ≤ 22`;
- the corrections of D1–D8;
- the result files and the Lean file that the changed text cites.

**Main conclusions.**

- Lemma 11.3 is correct and complete.
- It does not depend circularly on Section 11.
- (C) is therefore proved within the manuscript for all `n ≥ 2`, modulo the
  classical results the manuscript already cites ((GL), (GP), the GL78 sign
  fact).
- D2, D3, D4, D5, D7 and D8 are corrected.
- D1 is corrected in its numbers (806 / 11 / 795 / 25, reproduced), but the
  list of the eleven orders is wrong as written (N1, minor).
- D6 is corrected in Section 16 but not in the header comment (N2,
  cosmetic).
- N3–N8 are cosmetic defects of provenance, typesetting, formalization
  description, attribution and wording.
- None of N1–N8 is a gap in a proof, and none touches the Main Theorem.

**What this verdict does not cover.**

- Sections 2–11 beyond what Lemma 11.3 uses or what revision 4 changed.
- The correctness of the cited classical results:
  - (GL), (GP) and the GL78 sign fact, on which Lemmas 2.1, 2.2 and hence
    Lemma 11.3 depend;
  - AMW Theorem 4.4.
- Novelty of anything, including the forest-expansion proof of (C).
- Rerunning `verify_lean.py`.
- Records outside `main.tex` (STATE.md, journal, registry).

**Independence.** Limited: the reviewer is the same model as the author of
the text and as the reviewer of revision 3. This is an AI review, not peer
review. It applies only to revision `4b02146`.
