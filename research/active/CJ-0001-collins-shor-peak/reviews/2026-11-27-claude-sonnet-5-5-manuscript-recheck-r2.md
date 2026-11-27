# Independent recheck — CJ-0001 — manuscript revision 2 (changes of `87c3c8c` against `8df6bea`)

- **Reviewer:** Claude, model `claude-sonnet-5-5` (Anthropic), adversarial reviewer.
- **Date:** 2026-11-27.
- **Independence:** fresh subagent context. I received the task message only
  (primary source: Conjecture 1.2 of arXiv:1507.02341; the file; the two
  revisions; the instruction to read the two earlier reviews only after my own
  checks). I wrote the statement and the definitions down, reconstructed Lemma
  7.5 and its proof by hand, and wrote my own code (scratchpad `t.py`, `t2.py`,
  `t3.py`, `t4.py`) from the manuscript's formulas before I opened either
  earlier review. I did not open the author's scripts or the notes. Limit: same
  vendor as the author, and the same model identifier as one of the two
  earlier reviewers of `8df6bea` (and as the author of earlier reviews of
  parts); this is a fresh context, not a different model. I did not read the
  primary source PDF again; the statement is as given in the task and as
  recorded in the earlier reviews.
- **Revisions:** first version `8df6bea`; revision 2 `87c3c8c`
  (`87c3c8c36a4cc1acac50fb48102497ef73c56022`; `git status` clean at the start).
  File `manuscripts/CJ-0001-collins-shor/main.tex` at `87c3c8c`, SHA-256
  `5dd8d2b397e78ddf7a41d13d3fe07f115e5405583ee379e2fc0bd184865b42a9`
  (`sha256sum` of the working-tree file, which equals the committed file: the
  tree was clean). The review applies to this revision and only to the changes
  of revision 2 (`git diff 8df6bea 87c3c8c -- manuscripts/CJ-0001-collins-shor/main.tex`,
  all hunks read). The parts of the document that did not change are covered by
  the two earlier reviews of `8df6bea`, not by this one.

## Statement (written before reading the proofs)

Tree T of order n >= 3, d_k = 2^{k-(n-2)}|delta_k|, 0 <= k <= n-2. Claim: every
index p with d_p = max_k d_k satisfies floor(n/2) <= p <= ceil(n - n/sqrt5).
Revision 2 claims, in addition to what 8df6bea claimed, that (i) the star's
sequence is strictly increasing up to m = floor(n/2) and strictly decreasing
after it (Lemma 7.5, `lem:starshape`), (ii) Theorem 7.3(c) follows without
log-concavity (LC) and without Collins's Theorem 1, (iii) the Main Theorem is
assembled without them, (iv) the Merris chain in the remark of Section 8 is
corrected, plus wording and bookkeeping changes.

## Findings

| Item | Finding |
| --- | --- |
| Lemma 7.5 (star), hypotheses and set-up | Hand reconstruction, every step. Notation: N = n-2, F(j) = C(N,j) - C(N,j-1). (1) F(N+1-j) = C(N,N+1-j) - C(N,N-j) = C(N,j-1) - C(N,j) = -F(j): correct. (2) F(j) = C(N,j)(N-2j+1)/(N-j+1): correct; positive exactly for j < (N+1)/2, i.e. 0 <= j <= N/2: correct. (3) The ratio formula (eq:Fratio), F(j)/F(j+1) = (j+1)(N-2j+1)/((N-j+1)(N-2j-1)), needs N-2j-1 > 0, i.e. j < (N-1)/2: re-derived from C(N,j)/C(N,j+1) = (j+1)/(N-j): correct. (4) lambda_k(l_{S_n}) = (n-1)F(k) + 4(n-2)F(k-1) - 4F(k-2) for 1 <= k <= n-2: follows from Cor. 5.3(d) ([x^k] l = (n-1)C(N,k) + 4(n-2)C(N,k-1) - 4C(N,k-2)) by taking differences; and [x^k]l = d_k for k <= n-2 (Lemma 2.1). I checked it against the star's actual distance matrix (exact, determinant by Fractions) for 3 <= n <= 12: the formula equals d_k - d_{k-1} for all k, and the unique maximizing index is floor(n/2). |
| Lemma 7.5(a) (increase up to m) | k = m: Lemma 7.4 (starvalue; unchanged, reviewed earlier, and re-checked by my data: lambda_m > 0 for 3 <= n <= 1200). 1 <= k <= m-1: 2k <= 2m-2 <= N, so F(k), F(k-1) > 0: correct. k = 1: lambda_1 = (n-1)F(1) + 4(n-2)F(0) > 0, F(-1) = 0, F(0) = 1: correct. k >= 2, j = k-2: 2j = 2k-4 < N and 2j+1 = 2k-3 < N, so the ratio formula applies; N-2j-1 = N-2k+3 >= 3. Then F(k-2)/F(k-1) = [(j+1)/(N-j+1)] * [1 + 2/(N-2j-1)], with (j+1)/(N-j+1) < 1 (as 2j < N) and 1 + 2/(N-2j-1) <= 5/3, so the ratio is < 5/3: correct (the text writes 1 + 2/3 and bounds the first factor by 1). n >= 2m >= 2k+2 >= 6: correct. 4F(k-2) < (20/3)F(k-1) < 4(n-2)F(k-1) because n-2 >= 4 > 5/3: correct. Hence lambda_k > (n-1)F(k) > 0: correct. Edge: for n = 3, m = 1, there is no k in 1..m-1 (vacuous, k = m is Lemma 7.4); n = 4: m = 2, k = 1 only. Both handled. |
| Lemma 7.5(b) (decrease after m) | m+1 <= k <= N (vacuous for n <= 4, where N = m). m = floor(N/2)+1, so k >= floor(N/2)+2 > (N+1)/2, hence F(k) < 0 (by antisymmetry F(k) = -F(N+1-k), 1 <= N+1-k <= N/2): correct. k-1 >= m >= (N+1)/2, hence F(k-1) <= 0 (zero only for N odd, k-1 = (N+1)/2: the text says <= 0): correct. Case F(k-2) >= 0: lambda_k <= (n-1)F(k) < 0: correct (both other terms are <= 0). Case F(k-2) < 0: this forces k-2 > (N+1)/2 (k-2 >= m-1 >= 0, and F >= 0 on [0,(N+1)/2]): correct. Then j = N+2-k satisfies j <= N (so F's symmetric partner indices are in range), j >= 2 (k <= N), and j < (N-3)/2 < (N-1)/2: the text's stated j < (N-1)/2 is true (weaker than what holds). -F(k-1) = F(N+2-k) = F(j) > 0 and -F(k-2) = F(N+3-k) = F(j+1) > 0 (j+1 <= N/2): correct. F(j+1)/F(j) = (N-j+1)(N-2j-1)/((j+1)(N-2j+1)) < (N-j+1)/(j+1) <= (N-1)/3 (decreasing in j, j >= 2) < N: correct. So -4F(k-2) < 4(n-2)(-F(k-1)), and lambda_k < (n-1)F(k) < 0: correct. Conclusion: d_k - d_{k-1} < 0 for m+1 <= k <= n-2, so d_m > d_{m+1} > ... > d_{n-2}; with (a), floor(n/2) is the unique maximizing index of the star: correct. |
| Lemma 7.5, numerical test (my own code) | `t4.py`: exact integers, for every 3 <= n <= 1200 and every 1 <= k <= n-2: lambda_k > 0 for k <= m and lambda_k < 0 for k > m. 0 failures. `t.py`: every intermediate inequality of the proof (antisymmetry; F >= 0 / F < 0 ranges; the ratio formula against the definition; ratio < 5/3; 4F(k-2) < (20/3)F(k-1) < 4(n-2)F(k-1); in (b): k > (N+1)/2, k-1 >= m >= (N+1)/2, F(k-1) <= 0, and in the sub-case F(k-2) < 0 the facts j >= 2, 2j < N-1, -F(k-1) = F(j) > 0, -F(k-2) = F(j+1) > 0, F(j+1)/F(j) < (N-j+1)/(j+1) <= (N-1)/3 < n-2) was asserted with `Fraction` arithmetic for 3 <= n < 200: 0 failures. Star cross-check against distance matrices: n = 3..12 (see above). Boundary cases n = 3, 4, 5, 6, both parities, k = 1, k = m-1, k = m+1, k = n-2 are all inside these ranges. No counterexample. |
| Theorem 7.3(c), new proof | For 1 <= mu <= m: 2mu-1 <= 2m-1 <= n-1, so K_{n-1} is contained in K_{2mu-1} (K2), and lambda_mu(l_T - l_{S_n}) >= 0 by (b) and Lemma 3.2 (A). Lemma 3.2 re-read: for f = x^e(1+x)^i with 2e+i >= 2mu-1, a = mu - e: a <= 0 gives C(i,a) >= 0; a >= 1 gives i >= 2a-1 >= a and lambda = C(i,a-1)(i-2a+1)/a >= 0: correct. mu <= m <= n-2 for n >= 3 (n = 3: m = 1 = n-2), so Lemma 2.1 gives lambda_mu(l_T) = d_mu(T) - d_{mu-1}(T) and the same for the star: correct. Then d_mu(T) - d_{mu-1}(T) >= star's > 0 by Lemma 7.5(a) (mu = m also Lemma 7.4). Hence d_0(T) < ... < d_m(T), and no index p < m is a maximizing index (d_p < d_{p+1}): correct. The strengthened statement of the theorem ("more generally ... for 1 <= mu <= m", "Hence d_0 < ... < d_m") matches the proof. No circularity: Lemma 7.5 is placed after Theorem 7.3 but uses only Lemma 7.4, Cor. 5.3(d) and Lemma 2.1; none of them uses Theorem 7.3. |
| Main Theorem and its proof | Lower bound: Theorem 7.3(c). Upper bound: Theorem 10.1 (unchanged; I re-read its proof: it uses Lemmas 8.1, 8.2, 8.3, Theorem 9.5, Lemma 9.7 and Darroch's rule on q, and no use of (LC) or of the sequence d being unimodal: the "q_{K+1} < q_K" step uses the ratios of q, and Lemma 8.2 gives the conclusion for d). Attainment, new: star's unique maximizing index is floor(n/2) (Lemma 7.5): correct. Path: by Cor. 11.2, for infinitely many n the unique maximizing index of P_n is ceil(xi), xi = n - n/sqrt5, and for those n the fractional part of xi exceeds 4/5 (Cor. 11.2(c): p = ceil(xi) implies theta < 1/5, fractional part of xi = 1 - theta > 4/5). Then xi - 2/5 has the same integer part as xi (fractional part f - 2/5 > 2/5 > 0), so ceil(xi - 2/5) = ceil(xi): both forms of the upper bound are attained: correct. The statement of the Main Theorem adds the n >= 3 domain remark (n = 2: the sequence is (d_0), floor(2/2) = 1 > 0): correct and consistent with the source's convention. The sentence "The proof of the two bounds does not use that theorem [(LC), AAB Thm 2.1]" is true: I checked every use of the words log-concave, unimodal, (LC), R1 in the file (grep); remaining occurrences are in the abstract, the introduction (history, and the remark that (LC) supplies "unimodal"), the list (LC) in Section 2.2 marked "Not used in the proofs below", Remark 7.6 (`rem:noLC`), the formalization paragraph (the Lean lemma is described as no longer used), Section 15's list "Known results used or reproved here" (see Nit 1) and the status paragraph. |
| Merris chain (remark in Section 8) | New chain: 0 > -2/mu_(n-1) >= d_2 >= -2/mu_(n-2) >= d_3 >= ... >= -2/mu_(1) >= d_n, with 0 < mu_(1) <= ... <= mu_(n-1) the non-zero Laplacian eigenvalues (the document's own convention, Section 8) and d_1 >= ... >= d_n the distance eigenvalues (written with a partial sign as in the text). Re-derived: D^{-1} = -L/2 + tau tau^T/(2(n-1)) (GL) is a rank-one PSD update of A = -L/2, whose eigenvalues are 0 and -mu_(j)/2; by (W), b_i in [a_i, a_{i-1}]; D^{-1} has eigenvalues 1/d_1 > 0 > 1/d_n >= ... >= 1/d_2, so b_2 = 1/d_n, ..., b_n = 1/d_2. Then 1/d_2 in [-mu_(n-1)/2, -mu_(n-2)/2] gives -2/mu_(n-2) <= d_2 <= -2/mu_(n-1)... (inverting negative numbers reverses the order), and in general d_{i+1} lies between -2/mu_(n-i) and -2/mu_(n-i-1) consistent with the chain; the last link comes from b_2 = 1/d_n >= a_2 giving d_n <= -2/mu_(1). The chain written in revision 2 is the correct one; the first version had the last link reversed. Independent numerical check (floating, exploratory; numpy, `t2.py`): 80 random trees of orders 4, 6, 9, 12, all links hold within 1e-9. The text keeps the caveat that the equation number in Merris was not confirmed; unchanged. |
| Cross-references and compilation | `pdflatex` (MiKTeX), two passes, in a temporary copy of the file outside the repository (scratchpad `tex/`): exit code 0 both times, 32 pages, `main.log` has 0 occurrences of "undefined" and no LaTeX warnings. `lem:R1` is no longer referenced anywhere (grep). `rem:noLC`, `rem:star-peak`, `lem:starvalue`, `lem:starshape` are all referenced or defined and resolve. No other statement depends on Lemma R1 or on (LC) (see the Main Theorem row). The Lean lemma that formalizes R1 remains in the library (unused); the document says so in Section 14. |
| Other changed passages | (a) Abstract and introduction: Graham-Lovasz "conjectured unimodal with peak at n/2" attributed to [Col89, p. 29]: not checked by me against the source (the earlier reviewers did not either); and "Collins showed that the peak of the path is near n - n/sqrt5" is a restatement of what the document had. (b) Kronecker symbol xi renamed zeta: harmless (the name xi is used for n - n/sqrt5 elsewhere); the change removes a clash. (c) Section 12, item 2, star comparison: I recomputed the double star S(9,9) (order 20, two adjacent centres with 9 leaves each) exactly from its distance matrix: d_10/d_9 = 10791/10255, the star S_20 has ratio 99/94, and 10791/10255 < 99/94 (exact). So "false at order 20" holds, with the direction now stated. The claim "holds for all trees of order 4 to 19" I did NOT check (only that order 20 fails for this tree; no exhaustive run). (d) Section 13: the tree count 1,346,022 for orders 3 to 20 matches `experiments/CJ-0001-collins-shor-peak/results/exhaustive-03-20.json` (`total_trees`: 1346022) and the loop `for n in range(3, max_order + 1)` in `leaf_telescoping.py`; the remark that the notes' 1,346,023 is the count for orders 2 to 20 is consistent with `upper-bound.json` (1346023). I did not re-run `leaf_telescoping.py`. (e) Section 15: five citing papers listed by arXiv number; I did not re-check that list. (f) Section 16: statuses and provenance updated to say what was and was not reviewed; they say plainly that revision 2 is unreviewed, which is correct at the time of writing. (g) "Lemma 7.5 was checked exactly for 3 <= n < 800" (Section 16): my independent range is 3 <= n <= 1200, consistent. |

## Nits (not gaps)

1. Section 15, "Known results used or reproved here", still lists (LC) among
   the facts used ("Lemma 2.1, (GL), (GP), (LC)"). After revision 2 no proof
   uses (LC); the list is stale. The same list says the peak of the star is
   from [Col89, Theorem 1]; revision 2 proves it (Lemma 7.5), so the line is
   an attribution, not a dependency. Harmless.
2. The Lean lemma on log-concave sequences remains in the formalization
   directory and is described as no longer used. I did not run
   `scripts/verify_lean.py` (it writes a receipt; I may write only this
   report); no claim in the document relies on it.
3. In Lemma 7.5(b) the text says "j < (N-1)/2 (since F(k-2) < 0 forces
   k-2 > (N+1)/2)". True (indeed j < (N-3)/2), only less sharp than what
   the argument gives; the inequality the proof needs is j < (N-1)/2 for the
   ratio formula, and it holds.
4. Collins's formula (C) for the path is still a citation, and the "upper bound
   attained for infinitely many n" rests on it (Main Theorem now says so
   explicitly). Unchanged since 8df6bea and already stated as such.

## Defects of the two earlier reviews of `8df6bea`: corrected by revision 2?

Read only after my own checks.

Opus review (`2026-11-27-claude-opus-5-5-manuscript.md`):

| # | Defect | Corrected in `87c3c8c`? |
| --- | --- | --- |
| 1 | Merris chain wrong at its last link | Yes. Corrected to "... >= -2/mu_(1) >= d_n" with a note; I re-derived the chain and checked it numerically (exploratory). |
| 2 | R1 "only if" proof has a false sentence | Yes, by removal: Lemma R1 is deleted, nothing in the document refers to it (grep). Lean lemma left in place, noted as unused. |
| 3 | Domain n >= 3 not stated; false at n = 2 | Yes. The introduction says the convention n >= 3 is that of [AAB] and why (n = 2: floor(n/2) = 1 > 0). |
| 4 | 1,346,023 vs 1,346,022 trees | Yes. The text now says 1,346,022 for orders 3 to 20 and explains 1,346,023 (orders 2 to 20); consistent with the stored result file. |
| 5 | Graham-Lovasz "asked where the sequence peaks" understates | Yes (conjectured peak at n/2, citing [Col89, p. 29]; the page citation I could not check). |
| 6 | Attainment by the star rests on a citation | Yes. Lemma 7.5 proves it for all n >= 3 (my hand check and exact computation to n = 1200). |
| 7 | Citations not checked against sources (Col89 Conjecture 9, GL78 p. 66, Col89 p. 31, Pit97, Dar64) | No, and not claimed: these remain unchecked in the sources; unchanged. |

Sonnet review (`2026-11-27-claude-sonnet-5-5-manuscript.md`):

| # | Defect | Corrected in `87c3c8c`? |
| --- | --- | --- |
| 1 | R1 proof sentence false | Yes (removal), as Opus 2. |
| 2 | Tree count 1,346,023 | Yes, as Opus 4. |
| 3 | Attainment clauses rest on citations (star: Collins Thm 1 plus finite check; path: (C)) | Star: yes (Lemma 7.5, all n). Path: not changed in substance; the Main Theorem now says that the path attainment uses Collins's formula (C), which is still a cited, unproved formula (checked against the distance matrix by the project for 3 <= n <= 30). The tool-based conclusion "upper bound attained for infinitely many n" is therefore as strong as (C); this is disclosed. |
| 4 | Classical sources unread (Darroch, Collins, GL, GP); quotation of Col89 Conj. 9 not verified | No, and not claimed; still disclosed in the document. |
| 5 | Main Theorem: attained bound is ceil(xi), the displayed upper bound is ceil(xi - 2/5) | Yes. The proof of the Main Theorem now shows that for the relevant n the fractional part of xi exceeds 4/5, hence the two ceilings coincide. I re-derived it. |
| 6 | Section 12 item 2: direction of the star comparison unstated | Yes. Direction stated; S(9,9) numbers recomputed exactly (10791/10255 < 99/94). The "order 4 to 19" claim is unchecked by me. |
| 7 | Literature: arXiv:2206.07561, 2407.03309 not listed | Yes, both are now named in the coverage paragraph (with 2104.14516, 2103.00647, 1812.05734), with the statement that none resolves the conjecture. I did not re-check the other three. |
| 8 | Status section on earlier reviews | Yes. Section 16 now describes the two earlier reviews as of the first version only and says revision 2 is unreviewed; this recheck is itself the first review of the changes. |

## Does revision 2 introduce a gap?

No gap found. Lemma 7.5, the new proof of Theorem 7.3(c) and the new proof of
the Main Theorem are correct as written; every step was reproduced by hand and
every inequality used was tested exactly. The document still compiles with all
cross-references resolved. The bounds no longer depend on (LC), on Collins's
Theorem 1, or on Lemma R1.

## Reproduction

Scripts are in the session scratchpad (not committed); run with Python 3 (and
`uv run --with numpy` for the two floating-point checks).

- `t4.py`: exact integers; lambda_k(l_{S_n}) = (n-1)F(k) + 4(n-2)F(k-1) - 4F(k-2)
  with F(j) = C(N,j) - C(N,j-1), N = n-2; for every 3 <= n <= 1200 and
  1 <= k <= n-2: lambda_k > 0 iff k <= floor(n/2). Result: `bad 0`.
- `t.py`: the same for 3 <= n < 200, plus `Fraction` assertions of every
  intermediate inequality of the proof of Lemma 7.5 (listed in the table).
  Result: 0 failures, no assertion error.
- `t2.py`: exact (Fraction determinants; polynomial recovered by
  interpolation at n+1 points) d_k of the star from the distance matrix for
  3 <= n <= 12: d_k - d_{k-1} equals the binomial formula for every k and the
  unique maximum is at floor(n/2). Then 80 random trees (orders 4, 6, 9, 12),
  float eigenvalues: Merris chain of revision 2 holds (exploratory).
- `t3.py`: double star S(9,9) from the distance matrix, exact: d_9 = 10665200,
  d_10 = 11222640, d_10/d_9 = 10791/10255 < 99/94 = ratio of S_20.
- `pdflatex` on a copy of the file in the scratchpad, twice: 32 pages, 0
  undefined references, no warnings.
- `git diff 8df6bea 87c3c8c -- manuscripts/CJ-0001-collins-shor/main.tex` read in
  full; `sha256sum` of the file: value above.
- Not run: `scripts/verify_lean.py`, `uv run pytest`,
  `experiments/.../manuscript_check.py` (the stored run of the author is for
  `8df6bea`), `leaf_telescoping.py`, the exhaustive tree runs.

## Novelty and literature coverage

Not part of this recheck (revision 2 changes no claim of novelty). I did not
search. Novelty stays unknown beyond the document's own coverage statement.

## Verdict

**`no gap found within stated scope`**

Scope: the changes of revision 2 (`87c3c8c`, file SHA-256 above) against
`8df6bea`: Lemma 7.5 (`lem:starshape`), the new proof of Theorem 7.3(c), the new
assembly and attainment statements of the Main Theorem, the corrected Merris
remark, the removal of Lemma R1 and of the dependence on (LC) and Collins's
Theorem 1, the corrected bookkeeping and wording listed above, and
cross-reference consistency. Not covered: the unchanged parts (covered only by
the two reviews of `8df6bea`, which I did not repeat), the correctness of the
cited classical results at their sources (including (C) for the path), the
claim "holds for all trees of order 4 to 19" in Section 12 (unchecked), the
page citation [Col89, p. 29], novelty, and the Lean development. This is an AI
review by a model of the same vendor as the author, not a peer review and not a
human review.
