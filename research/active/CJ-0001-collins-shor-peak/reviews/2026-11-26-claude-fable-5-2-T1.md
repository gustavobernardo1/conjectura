# Independent review — CJ-0001 — Theorem T1 and Lemma D1 (double stars: the peak is at ⌊n/2⌋)

- **Reviewer:** AI model, exact identifier as reported by the environment:
  `claude-fable-5-2` (it matches the file name). Role: adversarial reviewer.
- **Date:** 2026-11-26.
- **Independence:** fresh context. The reviewer received the location of the
  claim and the primary source, not the author's reasoning trail. Not read:
  `STATE.md`, `journal.md`, `research/discoveries.json`, and the earlier review
  file `reviews/2026-11-26-claude-fable-5-2.md` (only the one-sentence mention of
  it in the header of `lemmas.md` was seen). **Limitation:** the note says it
  was written by `claude-fable-5-2`; the reviewer is the same model. Independence
  is of context only, not of model. This is an AI review, not a human review.
- **Revision reviewed:** Git commit `5e5ef14ddf754d2b9e2b99c13e3285a2331c7900`,
  branch `research`, working tree clean before and after the review (apart from
  this report).

  | File | SHA-256 | Git blob |
  | --- | --- | --- |
  | `research/active/CJ-0001-collins-shor-peak/notes/double-stars.md` | `ed379f3ace093b873d530a554b8ec62ce8f6301bb014962da3ea5cbfc515d11d` | `d8fafb4c9d493f78b6e5d0aac7b955c94b128d8d` |
  | `research/active/CJ-0001-collins-shor-peak/notes/lemmas.md` (notation paragraph, R1 general form, L3) | `a225898814df1ae584d9c58cb2c983d89bcbbd83121458c8058e9bfc4ca03c6e` | `62dc09c52c5342841db6daf14142bb327f548029` |
  | `experiments/CJ-0001-collins-shor-peak/double_stars.py` | `e706ef04e9c5a0a832b1852cd79f0dd9c45f1e5c6960eb5b64dfb6e3234f1f06` | `297439b2040cd931a1e45d6c6a90ed0a9837fa6c` |
  | `experiments/CJ-0001-collins-shor-peak/results/double-stars.json` | `9a88033e356cef9121eeac6e8001e9e169b48d4e4014b612cd36c636c080bfa9` | `5ef140f20e90e0a6108ec6be2a7ea4f84e3d5fb9` |
  | `tests/test_cj0001_distpoly.py` (`test_double_star_closed_forms_and_peak`) | `6c770862aa35f1a4bb192696ceb7533552b46dba3a36209fd2d7faeca71457a3` | `572ceeb72bb970b9fead2ef07d910cb6d8e2cb75` |

  Helper modules imported by the check, of which only the functions named below
  were read (not audited as a whole): `near_star_families.py`
  (`bfd8b203…c3d7`, blob `1c05dee0…`), `distpoly.py` (`43a481a0…13d0`, blob
  `4bfc6949…`), `independent_check.py` (`9e69a180…1a51`, blob `dc796345…`).
- **Material given to the reviewer:** the paths above; the reference
  arXiv:1507.02341. The reviewer downloaded the TeX source of version 3
  (`https://arxiv.org/e-print/1507.02341v3`, SHA-256 of the archive
  `bd9e2115f6790a0fa8e2970f737d226167601d08bb3b204b77005ebd9a80e587`) and read
  Sections 1 to 3 before opening the proof.

## Statement as read from the primary source

Written from the TeX source of arXiv:1507.02341v3 before reading the claim.

- **Objects.** `G` simple, finite, undirected, connected; `D(G)` its distance
  matrix. `δ_k(G)` is the coefficient of `x^k` in `det(D(G) − xI)`. Standing
  assumption of the paper: order `n ≥ 3`. For `0 ≤ k ≤ n−2`,
  `d_k(G) = 2^k |δ_k(G)| / 2^{n−2}` (normalized coefficients).
- **Fact 1.1** (quoted there from Graham–Lovász 1978, Eq. (44), without proof):
  for a tree `T` on `n` vertices, `(−1)^{n−1} δ_k(T) > 0` for `0 ≤ k ≤ n−2`.
- **Unimodal** (paper's definition): there is `k` with `a_{i−1} ≤ a_i` for
  `i ≤ k` and `a_i ≥ a_{i+1}` for `i ≥ k`. The paper does not define "peak" when
  the maximum is attained more than once.
- **Conjecture 1.2 (Collins–Shor).** For any tree `T` with `n` vertices, the
  normalized coefficients are unimodal with peak between `⌊n/2⌋` and
  `⌈n − n/√5⌉`. Quantifier: every tree, every `n` (with `n ≥ 3` by the standing
  assumption). The floor and ceiling are the paper's reading of Collins's
  Conjecture 9, which is stated without them.
- **Theorem 2.1(iii).** For a tree `T` of order `n`, `d_0(T), …, d_{n−2}(T)` is
  log-concave and unimodal. (Positivity is Fact 1.1, used in the proof; it is
  not part of the statement of Theorem 2.1.)
- **Observation 3.1.** `ℓ_T(x) = −2^{−(n−2)} det(2xI − D(T))` is real-rooted with
  coefficients `−4` for `x^n`, `0` for `x^{n−1}`, and `d_k(T) > 0` for `x^k`,
  `0 ≤ k ≤ n−2`.
- **About stars.** The paper reports that Collins [C89, Theorem 1] establishes
  `⌊n/2⌋` as the peak location for a star. It says nothing about uniqueness of
  the maximizing index.

The claim under review (T1) is about exactly these `d_k`, for the trees
`S(a,b)`, `a, b ≥ 1`, `n = a + b + 2 ≥ 4`. The definitions in the notation
paragraphs of `double-stars.md` and `lemmas.md` coincide with the source's.
T1 is a statement about a sub-family, not about the conjecture; it is presented
as such.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | `a, b ≥ 1` (so `n ≥ 4`, `m = ⌊n/2⌋ ≥ 2`, `N = n − 4 ≥ 0`, `t = ab ≥ 1`). L3 requires every `c_i ≥ 1`; here `c_1 = a`, `c_2 = b`, satisfied. R1 (general form) requires a positive log-concave sequence and `1 ≤ j ≤ r`; in Step 4, `r = n − 2`, `j = m` with `2 ≤ m ≤ n − 2`, and `j = n − 2 − m` with `1 ≤ j ≤ n − 2` when `m ≤ n − 3`. All satisfied. No vacuous hypothesis found. |
| Quantifiers | T1 is for all `a, b ≥ 1`. Part 2 is correctly conditioned on `m + 1 ≤ n − 2`, which fails exactly for `n = 4` (`S(1,1) = P_4`). The two parity cases `n = 2m` (`m ≥ 2`) and `n = 2m + 1` (`m ≥ 2`) cover every `n ≥ 4`. For part 2 the even case is `m ≥ 3` (index exists iff `m + 1 ≤ 2m − 2`) and the odd case `m ≥ 2` (iff `m + 1 ≤ 2m − 1`); together they cover every `n ≥ 5`. Nothing is left out. |
| Mathematical definitions | `δ_k`, `d_k`, `ℓ_T` agree with the source. I re-derived that the coefficient of `x^k` in `ℓ_T` is `(−1)^{n−1} 2^{k−(n−2)} δ_k`, which equals `d_k` **by Fact 1.1**. "Strong reading of ties" (T1, consequence) is not defined in the two notes reviewed; since T1 proves a unique maximizing index, the consequence holds under any reading. Notation collisions inside the claim: `c_1, c_2` denote `a, b` in the proof of D1 and central binomials in Step 2; `s` is the spine length in L3 and `a + b` in `double-stars.md`. Cosmetic, but in a proof document. |
| Boundary cases | `n = 4`, `S(1,1) = P_4`: by hand `det(D − xI) = x⁴ − 20x² − 32x − 12`, `d = (3, 16, 20)`; D1 gives `(g_0, g_1, g_2) = (3, 16, 20)` with `N = 0`; `m = 2 = n − 2`, part 2 void, Step 2 gives `6(d_2 − d_1) = 24`. `n = 5`, `S(1,2)`: `d = (4, 28, 58, 38)`. `n = 6`: `S(1,3)`: `(5, 42, 117, 136, 60)`; `S(2,2)`: `(5, 44, 126, 148, 65)`. `n = 7`: `S(1,4)`: `(6, 58, 200, 324, 258, 86)`; `S(2,3)`: `(6, 62, 222, 366, 292, 96)`. All from the definition (my computation), all equal to D1, unique maximum at `⌊n/2⌋`. Zero binomials: for `m = 2` (even) `c_1 = c_2 = c_3 = 0`, for `m = 3` (even) `c_2 = c_3 = 0`; for `m = 2` (odd) `e_1 = e_2 = e_3 = 0`, `m = 3` (odd) `e_2 = e_3 = 0`. The recurrences `(m−1)c_1 = (m−2)c_0`, `m c_2 = (m−3)c_1`, `(m+1)c_3 = (m−4)c_2` (and the odd analogues) remain true there because the identity `(k+1)C(N,k+1) = (N−k)C(N,k)` holds for all `k ≥ 0` with the zero convention, and the factor `(m−2)(m−3)` vanishes exactly where a negative value could have appeared. No division by zero: denominators are `m−1 ≥ 1`, `m`, `m+1`, `m+2`. `a = 1` with `b` large and `a = b`: covered by the general argument; additionally computed (below). |
| Lemma: L3 (spine length 2), as used | Reconstructed. The partition {centre 1}, {centre 2}, leaves of 1, leaves of 2 is equitable for `D`; `D·1_{C_j} = Σ_i Q_{ij} 1_{C_i}`, so `Q` is the matrix of `D` on the class-constant subspace. `D` is symmetric, so the orthogonal complement (vectors vanishing on the centres with zero sum on each leaf class) is invariant, and `D` acts on it as `−2` (same-class leaves are at distance 2 and equidistant from every other vertex). Dimension `(a−1)+(b−1) = n−4`. Hence `det(xI − D) = (x+2)^{n−4} det(xI − Q)` and `ℓ_T(x) = −2^{−2}(x+1)^{n−4} det(2xI − Q)`; I re-derived the power of 2. The `4×4` matrix `Q` printed in the note is exactly what the block rules of L3 give (rebuilt from the rules in my script and compared entry by entry), and equals the class sums of the true distance matrix on 129 double stars. **No gap found.** |
| Lemma: D1 | Expansion of `det(2xI − Q)` redone with my own multivariate integer-polynomial code (Leibniz sum over 24 permutations): it equals `16x⁴ − (16s−32)x³ − (20t+36s−12)x² − (8t+24s+8)x − (4s+4)` identically in `a, b, x`. So `−det/4 = g_0 + … + g_4x⁴` with the stated `g_j`, and the coefficient extraction `Σ_j g_j C(N, k−j)` is correct, including `N = 0`. Hand checks: `x³` coefficient `−8·tr Q = −(16s−32)`; `d_1 = g_0N + g_1 = s²+5s+2t`, which I matched both to L2 and to the source's formula `2n(n−1) − 2N_{P_3} − 4`; `g_3 + g_4N = 0`; `g_4 = −4`. Confirmed against the definition on 129 double stars (Faddeev–LeVerrier) and on 5 more by a second method (Bareiss at `n+1` points). **No gap found.** D1 depends on Fact 1.1 (through Observation 3.1) to identify the coefficients of `ℓ_T` with `d_k`; see "Dependency assumptions". The sentence "which is why it depends on `a, b` only through `s`, `t`" is incomplete as an explanation: multi-affinity gives `α + βa + γb + δab`; `β = γ` needs the symmetry `a ↔ b` as well. This is an aside, not a proof step. |
| Lemma: T1 part 1, even `n = 2m` | Reconstructed line by line: index map `C(N, m−j) = c_{2−j}`, `C(N, m−1−j) = c_{1−j}`; symmetry `c_{−i} = c_i` (valid for out-of-range indices too); regrouping to `(g_2−g_1)(c_0−c_1) + (g_3−g_0)(c_1−c_2) + g_4(c_2−c_3)`; `g_2−g_1 = 3t+6m−11`, `g_3−g_0 = 6m−15`; the three differences `c_0/(m−1)`, `3(m−2)c_0/((m−1)m)`, `5(m−2)(m−3)c_0/((m−1)m(m+1))`. Polynomial arithmetic redone by hand and symbolically: bracket `= 3tm(m+1) + 24m³ − 88m² + 98m − 30 = 3tm(m+1) + 2(2m−1)(2m−3)(3m−5)`. Positive for `m ≥ 2`, `t ≥ 1`, `c_0 = C(2m−4, m−2) > 0`. **No gap found.** |
| Lemma: T1 part 1, odd `n = 2m+1` | Reconstructed: `C(N, m−j) = e_{1−j}`, `C(N, m−1−j) = e_{−j}`; symmetry `e_{−1−i} = e_i`; the `g_1` term cancels; `(g_2−g_0)(e_0−e_1) + g_3(e_1−e_2) + g_4(e_2−e_3)` with `g_2−g_0 = 5t+16m−12`, `g_3 = 8m−12`; differences `2e_0/m`, `4(m−2)e_0/(m(m+1))`, `6(m−2)(m−3)e_0/(m(m+1)(m+2))`. Bracket redone by hand and symbolically: `10t(m+1)(m+2) + 16m(2m−1)(2m+1)` (the `m²` and constant terms cancel exactly). Positive; `e_0 = C(2m−3, m−1) > 0` for `m ≥ 2`. **No gap found.** |
| Lemma: T1 part 2, even | Reconstructed: `d_{m+1} − d_m = −g_0(c_2−c_3) − (g_1+4)(c_1−c_2) − (g_2−g_3)(c_0−c_1)`; `g_2−g_3 = 5t+5s+5 > 0`, `g_0 > 0`, `g_1 + 4 > 0`; `c_2−c_3 ≥ 0`, `c_1−c_2 ≥ 0`, `c_0−c_1 = c_0/(m−1) > 0`. Strictly negative. Every sign claim checked. **No gap found.** |
| Lemma: T1 part 2, odd | Reconstructed: `d_{m+1} − d_m = −(g_0+4)(e_1−e_2) − (g_1−g_3)(e_0−e_1)`; `g_1−g_3 = 2t+2s+10 > 0`; `e_1−e_2 ≥ 0`, `e_0−e_1 = 2e_0/m > 0`. Strictly negative. **No gap found.** |
| Lemma: R1, general form | Proof reconstructed in both directions (only "if `a_{j−1} < a_j` then every maximizing index is `≥ j`" is used by T1). For a positive log-concave sequence the ratios `a_{k+1}/a_k` are non-increasing; the rest follows. **No gap found.** This also covers the restated general form that `lemmas.md` says had not been re-reviewed (the two specialised bullets of R1 about `M` are outside this review). |
| Logical implications | Step 4: part 1 + R1 ⇒ every maximizing index `≥ m`; if `n = 4` then `m = n−2` is the last index; otherwise part 2 + R1 on the reversed sequence (`a_{j−1} = d_{m+1}`, `a_j = d_m`, `j = n−2−m`) ⇒ every maximizing index `≤ m`. Index bookkeeping verified. `⌊n/2⌋ ≤ n/2 < n − n/√5 ≤ ⌈n − n/√5⌉` is correct. With unimodality from Theorem 2.1 of the source, the consequence "Conjecture 1.2 holds for every double star" follows. **No gap found.** |
| Dependency assumptions | (1) **Fact 1.1 of the source** (Graham–Lovász 1978, Eq. (44)), needed for D1 (identification of the coefficients of `ℓ_T` with `d_k = 2^{k−(n−2)}|δ_k|`) and for positivity in Step 4. It is cited in the notation paragraph, **but the list "The proof uses: …" in T1 omits it** (and omits Observation 3.1), and Step 4 attributes positivity to Theorem 2.1, whose statement gives only log-concavity and unimodality. The source quotes Fact 1.1 without proof; neither I nor (per `lemmas.md`) the project has read Graham–Lovász 1978. My direct computation confirms the sign on the 129 + stars instances computed, which is finite evidence only. (2) **Theorem 2.1(iii) of the source**: I read its proof in the TeX source; it follows from real-rootedness of the characteristic polynomial of a symmetric matrix, Newton's inequalities (Lemma 1.4 there, cited to the literature), and Fact 1.1. I did not check the cited references for Lemma 1.4. (3) L3 with spine length 2: re-proved above. (4) No dependence on L1 or L2 except in the "Checks" paragraph of D1. |
| Counterexample attempts | (a) From the definition, exact: all `1 ≤ a ≤ b`, `a + b ≤ 22` (121 trees), four with `a > b`, and `S(1,40)`, `S(20,21)`, `S(2,37)`, `S(22,22)`: no violation of D1, of either inequality, of uniqueness of the peak, of log-concavity or of Fact 1.1. (b) Through D1 (valid only because D1 was verified symbolically): whole sequence for all `a ≤ b`, `a + b ≤ 260` (16,900 trees); the three middle coefficients for `260 < a + b ≤ 1500` (545,600 trees). No violation. (c) Degenerate `b = 0`: D1 then reproduces the star of order `a + 2` for `4 ≤ n ≤ 400` (consistent with the remark, outside the hypotheses of T1). No counterexample found. This is finite evidence and adds nothing to the proof beyond its range. |
| Formalization scope | No Lean statement is associated with this claim in the files reviewed. Lean was not run, as instructed. Formal status: not assessed. |
| Novelty coverage | **Not assessed.** I performed no literature search for a prior proof of the double-star case. Novelty remains unknown as far as this review is concerned. The note itself claims none. |
| Remarks: stars | The formula `ℓ(x) = (x+1)^{n−2}((n−1) + 4(n−2)x − 4x²)` re-derived (L3 with spine length 1, `Q = [[0, n−1], [1, 2(n−2)]]`, symbolic). The two closed forms for `d_m − d_{m−1}` hold exactly for `3 ≤ n ≤ 400` (my computation; formula vs definition for `n ≤ 30`) — the note states them without derivation, as a consistency check. The identity `C(2m−2,m−1)(m−1) = 2(2m−3)C(2m−4,m−2)` is correct, and the `t = 0` specialisation of the even formula does give the star formula (the odd one does too). The note proves nothing about `d_{m+1} < d_m` for stars and says the star result is Collins's, known to the project only through arXiv:1507.02341. That attribution matches what the source says. Correctly labelled as not a result. |
| Remarks: diameter at most 3 | The classification (order `≥ 3`: diameter 2 ⇒ star; diameter 3 ⇒ double star with `a, b ≥ 1`) is correct. **The corollary is not proved inside the project**: its star half rests entirely on Collins (1989, Theorem 1), a paper the note says has not been read, as reported second-hand by the source. The remark says "With Collins's theorem for stars", so the dependence is disclosed, but the sentence itself does not repeat that the theorem is unread. Further, the source's report gives "the peak is at `⌊n/2⌋`" for stars with no statement on uniqueness, so for stars the "strong reading of ties" used in T1 is **not** supported by what the project has; the remark does not claim it, and must not be read as claiming it. |
| Remarks: "What T1 does not say" | The statement that the relative margin `1 − d_{m−1}/d_m` is "of order `1/n`" is **asserted without proof**. My exploratory values of `n(1 − d_{m−1}/d_m)` (exact rationals, displayed as floats) lie between about 0.86 and 1.11 for `n` up to 5002, which is consistent with it and proves nothing. The remark is not used anywhere. |
| "Checks" section vs what was run | The counts are right (10,000 unordered pairs with `a + b ≤ 200`; 400 with `a + b ≤ 40`; 404 direct comparisons; 200 stars, 40 direct). Two wording points: (i) "agreement of the whole sequence with the numeric quotient-matrix computation" is, in the code, **proportionality** (`numeric[k]·d[0] == numeric[0]·d[k]`), and that computation builds `Q` by the same rule as L3, so it is not independent evidence for L3 or D1; the independent evidence is the direct `n×n` determinant. (ii) `matches_direct` compares with `2^k|δ_k|`, so the repository check does not test the sign in Fact 1.1 (mine does). The note ends with "A finite check is not a proof. The proof is Steps 1 to 4", and no finite computation is presented as a proof. `results/double-stars.json` records revision `241dc03`, not `5e5ef14`; `git diff --stat 241dc03 5e5ef14` shows the JSON file as the only difference, so the code and notes that produced it are those reviewed. |
| Unresolved gaps | None in the mathematics of D1 or of T1 parts 1 and 2 or Step 4. Open points, none of which invalidates T1: (1) the dependency list of T1 omits Fact 1.1 / Observation 3.1; (2) the diameter-≤-3 remark is conditional on an unread theorem and does not extend the "strong reading" to stars; (3) the "order `1/n`" remark is unproved; (4) notation collisions (`c_i`, `s`); (5) the "which is why" explanation needs the `a ↔ b` symmetry; (6) "agreement" with the numeric quotient computation means proportionality; (7) "strong reading of ties" is not defined in the reviewed notes. |

## Reproduction

All commands run on 2026-11-26 at revision `5e5ef14ddf754d2b9e2b99c13e3285a2331c7900`,
clean tree, Windows 10, with `PYTHONIOENCODING=utf-8`.

Repository commands:

- `uv run pytest tests/test_cj0001_distpoly.py -q` → `96 passed in 3.82s`
  (this includes `test_double_star_closed_forms_and_peak`).
- `uv run python experiments/CJ-0001-collins-shor-peak/double_stars.py --max-sum 60`
  → "symbolic quotient determinant agrees with the stated polynomials g_0..g_4";
  "double stars: 900 trees, closed forms and inequalities hold; 404 compared
  with the direct determinant"; "stars: 60 trees, closed forms and inequalities
  hold; 40 compared with the direct determinant". No `--out` was given; the
  result file was not rewritten.
- **Not rerun:** the default run with `--max-sum 200` that produced
  `results/double-stars.json` (10,000 trees). Its figures were compared with
  the code by counting, not by re-execution.
- `git diff --stat 241dc03 5e5ef14` → only `results/double-stars.json`.

Independent calculation (script kept outside the repository, in the session
scratch directory, file `review_t1.py`, SHA-256
`a62dd317327a48ed73c9e4d0859850b29be84ae342dc811bcf9124a6c3544600`; Python
3.12.4 started with `-I`; it imports only `fractions`, `itertools`, `math`,
`sys`, `time`; nothing from the repository, no `flint`). The script is not
preserved in the repository; its design is:

- **A.** A home-made multivariate integer polynomial type; `Q` built from the
  block rules of L3 and compared with the matrix in the note; `det(2xI − Q)` by
  the Leibniz formula; equality with the stated quartic and with `−4(g_0 + … + g_4x⁴)`.
  Same for the `2×2` star quotient. Passed.
- **B.** The two polynomial identities of Step 2 in `(m, t)` and the five
  differences of the `g_j`, symbolically. Passed.
- **C.** From the definition: adjacency list of `S(a,b)`, distances by BFS,
  `det(xI − D)` by Faddeev–LeVerrier in exact integers (with a Cayley–Hamilton
  self-check), `δ_k = (−1)^n ·` coefficient, sign test of Fact 1.1,
  `d_k = 2^k|δ_k|/2^{n−2}` as `Fraction`. For 129 double stars (all
  `a ≤ b`, `a + b ≤ 22`; `(5,1), (7,2), (9,3), (12,1)`; `(1,40), (20,21), (2,37), (22,22)`):
  equitable partition with the stated `Q`; `d` integral and equal to D1 for
  every `k`; log-concave; `d_{m−1} < d_m`; `d_{m+1} < d_m` when the index
  exists; unique maximizer `m`; `m ≤ n − isqrt(⌊n²/5⌋) = ⌈n − n/√5⌉`; both
  closed forms of Step 2. Passed (5.1 s).
- **D.** Second method: fraction-free Bareiss determinant of `2xI − D` at
  `x = 0, …, n`, compared with `−2^{n−2}(x+1)^{n−4}G(x)`; two polynomials of
  degree `n` agreeing at `n+1` points are equal. `S(1,1), S(1,2), S(3,3), S(1,30), S(17,30)`. Passed.
- **E.** Through D1: all of part C's checks on the whole sequence for all
  `a ≤ b`, `a + b ≤ 260` (16,900 trees), together with coefficient `0` at
  `x^{n−1}` and `−4` at `x^n`; the two inequalities for
  `260 < a + b ≤ 1500` (545,600 trees). Passed. Margin table (floats, display
  only, exploratory).
- **F.** Stars: formula vs definition for `3 ≤ n ≤ 30`; closed forms and unique
  maximizer `⌊n/2⌋` for `3 ≤ n ≤ 400`; D1 at `b = 0` vs the star formula for
  `4 ≤ n ≤ 400`. Passed.

Total run time 68 s. Hand calculations in addition: `P_4` characteristic
polynomial; both bracket expansions of Step 2; all regroupings of Steps 2 and
3; the `x³` coefficient of the quartic; `d_1` against L2 and against the
source's `P_3`-count formula.

## Verdict

`no gap found within stated scope`

Per item:

| Item | Verdict |
| --- | --- |
| Lemma D1 | no gap found (conditional on Fact 1.1 of the source, as is the definition-level identification of `ℓ_T`'s coefficients with `d_k`) |
| T1 part 1, even order | no gap found |
| T1 part 1, odd order | no gap found |
| T1 part 2, even order | no gap found |
| T1 part 2, odd order | no gap found |
| Step 4 (unique peak, interval, R1 general form) | no gap found; dependency list incomplete (Fact 1.1 / Observation 3.1 not listed; positivity attributed to Theorem 2.1) |
| Remarks | no mathematical error found; **not results**: the diameter-≤-3 corollary rests on Collins's Theorem 1, unread and second-hand, and does not carry the "strong reading of ties" for stars; the "order `1/n`" statement is unproved |

**Scope.** The verdict covers: the statement of T1 and D1 against the
definitions of arXiv:1507.02341v3; the proof in Steps 1 to 4 of
`double-stars.md`; L3 for spine length 2 (and 1, for the star remark); the
general form of R1; the consistency of the documented computation with what the
note says about it. It is conditional on two results taken from the source and
not re-proved by this review from first principles: Fact 1.1 (Graham–Lovász
sign pattern, quoted by the source) and Theorem 2.1(iii) (whose short proof in
the source I read, down to its cited Lemma 1.4).

**Not covered.** Novelty (no search was made; unknown). Any Lean
formalization (none examined; Lean not run). Collins (1989) and Graham–Lovász
(1978), which were not read. `STATE.md`, `journal.md`,
`research/discoveries.json` (record MD-0006) and the catalogue entry, so
whether the status recorded there matches this claim was not checked. L1, L2,
the two specialised bullets of R1, and the rest of `lemmas.md`. The helper
modules `distpoly.py`, `near_star_families.py`, `independent_check.py` beyond
the functions named. The default 10,000-tree run was not re-executed. Trees of
diameter 4 or more: T1 says nothing about them and neither does this review.

This is an AI review by the same model that wrote the claim, in a fresh
context. It is not human peer review. It applies only to revision
`5e5ef14ddf754d2b9e2b99c13e3285a2331c7900`; any material change to the
statement or the proof invalidates it until rechecked.
