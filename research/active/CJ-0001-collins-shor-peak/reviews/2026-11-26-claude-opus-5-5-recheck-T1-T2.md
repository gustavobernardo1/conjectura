# Recheck of a revision — CJ-0001 — Theorems T1 (double stars) and T2 (caterpillars K(a,b,c))

**This is a recheck of one revision of two files, not a full review.** It asks
whether the changes made after the earlier reviews alter the mathematics, and
whether the earlier verdicts still apply to the revised texts. It does not
re-review the proofs from scratch.

- **Reviewer:** `claude-opus-5-5` (Claude Opus 5.5, Anthropic), acting as Adversarial Reviewer.
- **Date:** 2026-11-26.
- **Independence and its limits:** fresh subagent context, launched by the
  Research Director with the file paths, the two reviewed revisions and the
  questions to answer. I was not given the author's reasoning. I did not open
  `journal.md`, `STATE.md` or the earlier review `reviews/2026-11-26-claude-fable-5-2.md`.
  Limits:
  1. As instructed, I read the two earlier review reports, which contain the
     earlier reviewers' reasoning.
  2. Three tool outputs showed me the author's own description of the changes,
     although I did not seek it:
     - `git show --stat 1c38662` displayed the commit message, which says the
       notes were revised "without change to any statement, formula or step of
       a proof";
     - a repository-wide grep for `spine length` displayed single matching lines
       of `STATE.md` and `journal.md`, without my opening those files;
     - a grep of `research/discoveries.json` displayed its lines 426 and 473.

     I classified the hunks from the diffs alone and did not rely on any of
     these descriptions.
  3. My model identifier is the same as that of the earlier T2 reviewer
     (`claude-opus-5-5`). It differs from that of the author (`claude-fable-5-2`;
     commit `1c38662` is co-authored by "Claude Fable 5.2"). All are Anthropic
     Claude models, so this is not independence of vendor, and there is no human
     review.
  4. This session's scratch directory also holds the scripts of the earlier T2
     review (`rev_t2/`). I did not open them.
- **Revision rechecked:** `1c386621bbf5083e89259a9e6ff9cae341c3b4a7` (`HEAD` of
  branch `research`). `git status --short` was empty before and after the work,
  apart from this report, so the files are unmodified in the working tree.

  | File | SHA-256 (working tree = `git show HEAD:…`) | Git blob |
  | --- | --- | --- |
  | `research/active/CJ-0001-collins-shor-peak/notes/double-stars.md` | `c7b0db848586a293d8e26d18fc36e7a81c4a0dbac4eb1089e67f1c56900c951a` | `bee050f8cb1a77cf447b45d29a4387289bafa461` |
  | `research/active/CJ-0001-collins-shor-peak/notes/spine3.md` | `3584da55306486b2ee3478c23aa56849597ffdbfb68a5ec4c8c90b8adcccf1d5` | `254a0daf29d4262c111a82253ebb062440b1240a` |
  | `experiments/CJ-0001-collins-shor-peak/spine3.py` | `2ca1e1fe740fc1e29e1d7b3039ca3a2fcea1fecd03df9c80a38af5f52e873ecb` | `a1307d91c27a0f99a9ba67372931fb1901fbc636` |

- **Earlier texts (base of the diffs):**
  - `double-stars.md` at `5e5ef14ddf754d2b9e2b99c13e3285a2331c7900` has SHA-256
    `ed379f3a…5d11d`. This equals the hash recorded in the T1 review.
  - `spine3.md` at `74cb5bbba6b84b905cf09e3908292578cb891025` has SHA-256
    `5b626fb6…b4b5`. This equals the hash recorded in the T2 review.
  - `spine3.py` at `74cb5bb` has SHA-256 `0cd63aea…6be5`. This equals the hash
    recorded in the T2 review.
- **History of the files:**
  - `double-stars.md` was touched only by `241dc03` and `1c38662`;
    `git diff --stat 241dc03 5e5ef14` lists only `results/double-stars.json`.
  - `spine3.md` and `spine3.py` were touched only by `74cb5bb` and `1c38662`.
  - `lemmas.md` is unchanged between each reviewed revision and `HEAD`, and so
    is `double_stars.py`.
- **Diffs examined:**
  - `git diff 5e5ef14 HEAD -- …/double-stars.md`: 8 hunks;
  - `git diff 74cb5bb HEAD -- …/spine3.md`: 5 hunks;
  - `git diff 74cb5bb HEAD -- …/spine3.py`: 1 hunk.

  Each was read both as a line diff and as `--word-diff=plain`.
- **Primary source:** arXiv:1507.02341v3 (Aalipour, Abiad, Berikkyzy, Hogben,
  Kenter, Lin, Tait, *Proof of a conjecture of Graham and Lovász concerning
  unimodality of coefficients of the distance characteristic polynomial of a
  tree*, revised 20 April 2017). I fetched the PDF from `https://arxiv.org/pdf/1507.02341v3`;
  its SHA-256 is `2f87e6dbc7bec8b191733459875c097868a90a32fa855756c58853b6b4575b40`.
  I read pages 1–6 and 10–11 before judging the revised attributions.

## What the source says, as read for this recheck

- **p. 2, notation:** `δ_k(G)` is the coefficient of `x^k` in `det(D(G) − xI)`.
  For `0 ≤ k ≤ n−2`, `d_k(G) = (1/2^{n−2}) 2^k |δ_k(G)|`. Order `n ≥ 3`.
- **p. 2, unimodality:** "unimodal if there is a `k` such that `a_{i−1} ≤ a_i` for
  `i ≤ k` and `a_i ≥ a_{i+1}` for `i ≥ k`". The word "peak" is used without a
  definition and nothing is said about ties.
- **Fact 1.1** ([8] = Graham–Lovász 1978, Eq. (44)): for a tree `T` on `n`
  vertices, `(−1)^{n−1} δ_k(T) > 0` for `0 ≤ k ≤ n−2`. Hence
  `d_k(T) = (−1)^{n−1}δ_k(T)/2^{n−k−2}` "by Fact 1.1".
- **p. 3, Collins and Conjecture 1.2:** Collins [4] (DAM 25, 1989) showed that
  for stars and paths the sequence is unimodal, with the peak "at `⌊n/2⌋` for
  stars". The paper says "[4, Theorem 1] establishes `⌊n/2⌋` as the peak
  location for a star". Nothing is said about ties or about uniqueness of the
  maximizing index.

  Conjecture 1.2 reads: the normalized coefficients of every tree with `n`
  vertices "are unimodal with peak between `⌊n/2⌋` and `⌈n − n/√5⌉`".
- **Theorem 2.1:**
  - (i) the coefficient sequence of `p_D` is log-concave;
  - (ii) `|δ_0|, …, |δ_{n−2}|` is log-concave and unimodal;
  - (iii) `d_0, …, d_{n−2}` is log-concave and unimodal.

  Positivity is not part of the statement. In the proof it comes from Fact 1.1.
- **Observation 3.1:** `ℓ_T(x) = −(1/2^{n−2}) det(2xI − D(T))` is real-rooted.
  Its coefficients are `−4` for `x^n`, `0` for `x^{n−1}`, and `d_k(T) > 0` for
  `x^k` when `0 ≤ k ≤ n−2`.

## Question 1 — the hunks, classified

Classes:
- **(i)** presentation only;
- **(ii)** a change to what the proof cites or to how a step is justified;
- **(iii)** a change to the mathematics.

### `double-stars.md` (T1), `git diff 5e5ef14 HEAD`

| Hunk | Lines at `HEAD` | Change (quoted or summarized) | Class |
| --- | --- | --- | --- |
| H1 `@@ -3,7 +3,8 @@` | 6–7 | Adds "The file was revised after its review; what changed is listed under *Revision history* at the end." | (i) |
| H2 `@@ -17,6 +18,13 @@` | 21–26 | New paragraph: in `lemmas.md` "`s` is the number of spine vertices of a caterpillar (here 2) and `c_1, …, c_s` are the numbers of leaves; in this file `s` is always `a + b` … from Step 2 on `c_i` denotes a binomial coefficient. The only place where `c_1, c_2` are numbers of leaves is the first sentence of the proof of Lemma D1". | (i) |
| H3 `@@ -26,12 +34,16 @@`, first part | 35–39 | Consequence sentence. Old: "(Conjecture 1.2 of arXiv:1507.02341, in the strong reading of ties) holds for every double star". New: "holds for every double star, also in the strong reading of ties, in which every maximizing index must lie in the interval (the source does not say how a tie is to be read)". The numbered parts 1 and 2 of T1 are context lines and are unchanged. | (i): the content is the same, and a term is defined |
| H3, second part | 41–46 | Dependency list. Old: L3; "Theorem 2.1 … (the sequence … is positive and log-concave), only in Step 4"; R1, "only in Step 4". New: "in Step 1, Lemma L3 … together with Fact 1.1 and Observation 3.1 … for the passage from the characteristic polynomial to the `d_k`; in Step 4, Fact 1.1 again (`(−1)^{n−1} δ_k > 0`, so the `d_k` are positive), Theorem 2.1 … (… log-concave), and the general form of R1". Citations are added and positivity is re-attributed; nothing is removed. | **(ii)** |
| H4 `@@ -62,8 +74,11 @@` | 76–81 | Sentence after the ∎ of D1. It adds "and it is symmetric under `a ↔ b` (exchanging the two centres is an automorphism of the family); a polynomial that is affine in each of `a, b` and symmetric is of the form `α + β(a + b) + γab`", and replaces "it" by "the determinant". The proof of D1, the matrix `Q`, the quartic and the `g_j` are unchanged. | (i): an aside outside the proof, as the T1 review called it |
| H5 `@@ -168,8 +183,9 @@` | 186–188 | Step 4. Old: "positive and log-concave (Theorem 2.1 of arXiv:1507.02341)". New: "positive (Fact 1.1 of arXiv:1507.02341) and log-concave (Theorem 2.1 of the same paper)". The logic of the step is unchanged. | **(ii)** |
| H6 `@@ -197,13 +213,16 @@` | 216–225 | Remarks. "Trees of diameter at most 3" is rewritten (see F-T1-3). In "What T1 does not say", "tends to `0` … (it is of order `1/n`), so T1 is an exact statement, not a consequence of a crude bound" becomes "In the exact values computed, the relative margin … decreases roughly like `1/n`; this is an observation, not proved here." | (i): the remarks are not part of the proof |
| H7 `@@ -212,11 +231,13 @@` | 234–240 | Checks. "agreement … with" becomes "proportionality … to", plus "(which shares Lemma L3 with the closed form and is not independent evidence for Lemma D1)" and "(the comparison is made on `|δ_k|`, so it does not test the sign asserted by Fact 1.1)". | (i) |
| H8 `@@ -224,3 +245,22 @@` | 249–266 | New *Revision history* section. | (i) |

No hunk changes:
- the statement of T1 (parts 1 and 2), a hypothesis or a quantifier;
- the definitions of `δ_k`, `d_k`, `ℓ_T`, `S(a,b)`, `s`, `t`, `N`, `m`, `c_i`, `e_i`;
- the matrix `Q`, the quartic, the `g_j`, or any formula of Steps 2 and 3.

The word diff confirms that no character of those lines changed. **No hunk is
class (iii).**

### `spine3.md` (T2), `git diff 74cb5bb HEAD`

| Hunk | Lines at `HEAD` | Change | Class |
| --- | --- | --- | --- |
| H1 `@@ -1,9 +1,10 @@` | 1, 6–7 | Title: "caterpillars with spine length 3" becomes "the caterpillars K(a,b,c) with a, b, c ≥ 1". Adds the same header sentence as T1-H1. | (i) |
| H2 `@@ -21,6 +22,10 @@` | 25–28 | New: "In `lemmas.md` and in the file names of the project this family is said to have "spine length 3": the spine has three vertices (and two edges). The condition `a, b, c ≥ 1` is part of every statement below; the caterpillars with three spine vertices and `b = 0` are not treated in this file." | (i), but contains a false statement (F-T2-1) |
| H3 `@@ -36,12 +41,13 @@` | 44–50 | Dependency list. Old: "Lemma L3 … with spine length 3 (which rests on Fact 1.1 and Observation 3.1 of the source …); Theorem 2.1 … and Fact 1.1 …, both only in Step 4; and the general form of R1 …, only in Step 4". New: "in Step 1, Lemma L3 … with three spine vertices, together with Fact 1.1 and Observation 3.1 …; in Step 4, Fact 1.1 again …, Theorem 2.1 …, and the general form of R1 …, of which only the direction "if `a_{j−1} < a_j` then every maximizing index is `≥ j`" is used." The set of cited results is unchanged. Fact 1.1 is now placed in Step 1 as well as Step 4, and the use of R1 is narrowed to one direction. | **(ii)** |
| H4 `@@ -174,7 +180,7 @@` | 183 | Step 3(i): "at the largest `u`, and in fact at a larger value:" becomes "at the largest `u`:". The four bullet inequalities that follow are unchanged. | **(ii)**: the wording of a step's justification |
| H5 `@@ -270,15 +276,37 @@` | 279–290, 297–312 | Checks: adds "Here and in the next item the `d_k` are taken from the formula of Lemma C1, not computed from the tree: these two items test Lemma C2 and Step 3 given Lemma C1, and say nothing about Lemma C1 itself". Adds "(621 trees)" and "This is the only item, with the test below, that tests Lemma C1 against the tree." New *Revision history* section. | (i), but contains two inaccurate statements (F-T2-2, F-T2-3) |

The following are not touched by any hunk:
- the statement of T2 and its hypotheses `a, b, c ≥ 1`;
- `m`, `N`, `u`, `v`;
- the matrix `Q`, the `g_j`, the recurrences, the binomial-ratio products;
- `K`, `R`, the `H` table;
- every inequality of Step 3 and the text of Step 4.

**No hunk is class (iii).**

### `spine3.py`, `git diff 74cb5bb HEAD`

There is one hunk, `@@ -1,4 +1,4 @@`, which changes the first line of the
module docstring:
- old: "Caterpillars with spine length 3: closed forms around the middle index.";
- new: "The caterpillars K(a,b,c) with a, b, c >= 1: closed forms around the middle index.".

Nothing else changed. One qualification: the docstring is not inert. Line 248,
`argparse.ArgumentParser(description=__doc__.splitlines()[0])`, uses this line
at run time, so the `--help` text changes (I ran `spine3.py --help` and the new
description is printed). No computation, assertion or output field is
affected.

The `"experiment"` string at line 257 and docstring line 5 still say "spine
length 3". `results/spine3.json`, which records `git_revision` `74cb5bb`, was
therefore produced by code that is computationally identical to `HEAD`.

## Question 2 — are the new sentences true?

### T1

| New assertion | Check | Result |
| --- | --- | --- |
| In `lemmas.md`, `s` is the number of spine vertices and `c_1, …, c_s` the numbers of leaves | `lemmas.md` lines 111–112: "spine `v_1, …, v_s` … carries `c_i ≥ 1` pendant leaves" | True |
| In `double-stars.md`, `s` is always `a + b`; from Step 2 on `c_i` is a binomial; the only place where `c_1, c_2` are leaf numbers is the first sentence of the proof of D1 | Grep of the file. `s`: lines 18, 80, 97, 127, always `a+b`. Leaf numbers at line 58 only, apart from the new paragraph itself. Binomials at lines 97–169. | True |
| The source does not say how a tie is to be read | Source p. 2 (definition of unimodal) and p. 3 | True |
| Fact 1.1 and Observation 3.1 are used for the passage to the `d_k` (Step 1) | Source p. 2 and p. 5. Observation 3.1 states that the coefficient of `x^k` in `ℓ_T` is `d_k > 0`, and the paper derives the sign from Fact 1.1. | True |
| Step 4: positivity from Fact 1.1, log-concavity from Theorem 2.1 | Fact 1.1 gives `δ_k ≠ 0`, hence `d_k = 2^{k−(n−2)}|δ_k| > 0`. Theorem 2.1(iii) gives log-concavity, not positivity. | True. The new attribution is the correct one; the old one was the defect the T1 review reported. |
| The determinant is affine in `a` and in `b` and symmetric under `a ↔ b`; an affine, symmetric polynomial is `α + β(a+b) + γab` | Own exact multivariate computation, built from the L3 block rules (script A below): `det(2xI − Q)` has degree ≤ 1 in `a` and in `b`, is invariant under `a ↔ b`, and equals the stated quartic. In addition, `Q(b,a) = P Q(a,b) Pᵀ` with `P` the permutation (centre 1 ↔ centre 2, leaf class 1 ↔ leaf class 2). The algebraic claim holds: `α + βa + β'b + γab` symmetric forces `β = β'`. | True. The phrase "automorphism of the family" is loose (F-T1-2). |
| "T1 covers the trees of diameter 3" | Diameter-3 trees are exactly the `S(a,b)` with `a, b ≥ 1` (as in the T1 review) | True |
| The project relies on Collins's theorem as reported; the report does not say how ties are treated; "the formulas above prove only `d_{m−1} < d_m` for stars, that is, the lower bound" | Source p. 3. I re-derived the even star formula by hand: `m(m+1)(d_m − d_{m−1}) = C(2m−2,m−1)(6m² − 13m + 5) = C(2m−2,m−1)(2m−1)(3m−5)`. The note gives no formula for `d_{m+1} − d_m` of a star. | True. The conclusion does not say which reading of ties (F-T1-3). |
| "In the exact values computed, the relative margin … decreases roughly like `1/n`; this is an observation" | The note names no computation. In the repository I found exact values only in `results/near-star-families.json` (`double_star_vs_star`, the closest-to-violation double star per order 6–41) and in `results/double-stars.json` (one global minimum). Own exact computation (script B, all `1 ≤ a ≤ b`): see the table in *Reproduction*. | Consistent with the data, but unsourced and silent on the parity dependence (F-T1-1) |
| Checks: "proportionality" to the quotient-matrix computation, which "shares Lemma L3" | `double_stars.py:175–176`: `numeric[k]*d[0] == numeric[0]*d[k]`. `near_star_families.py:53–82` builds `Q` from the same block rules and uses an exact `fmpz_mat.charpoly`. | True. "numeric" is a pre-existing misnomer: the computation is exact. |
| Checks: the direct comparison is on `|δ_k|` and does not test the sign | `distpoly.py:78–82` returns `abs(charpoly[k]) << k`; `double_stars.py:140–142` compares with `d << (n−2)` | True |

### T2

| New assertion | Check | Result |
| --- | --- | --- |
| "In `lemmas.md` … this family is said to have "spine length 3"" | `lemmas.md` contains neither "spine length" nor "length 3". Its only occurrence of "length" is "paths of length 2" (line 105), and L3 is written with "spine `v_1, …, v_s`". The phrase "spine length 3" occurs in: the old title, `spine3.py` lines 5 and 257, `results/spine3.json` line 2, and the old README row. The file names contain `spine3`. | **False as to `lemmas.md`** (F-T2-1) |
| "the spine has three vertices (and two edges)" | Definition of `K(a,b,c)` | True |
| "The condition `a, b, c ≥ 1` is part of every statement below; … `b = 0` … not treated" | T2, C1 and C2 are about `K(a,b,c)`, which is defined only for `a, b, c ≥ 1`. The Scope remark excludes `b = 0`. | True |
| Fact 1.1 and Observation 3.1 enter in Step 1; Fact 1.1 (positivity) and Theorem 2.1 (log-concavity) in Step 4 | As for T1 | True |
| Only the direction "if `a_{j−1} < a_j` then every maximizing index is `≥ j`" of R1 is used | Step 4 applies R1 with `j = m` to `d` and with `j = n−2−m ≥ 1` to the reversed sequence, each time from a strict inequality. Both are uses of that direction. `lemmas.md` lines 27–36 state and prove it for positive log-concave sequences with `1 ≤ j ≤ r`. | True |
| Step 3(i): the bounds are at the largest `u` (the phrase "in fact at a larger value" is removed) | Script C: `3(m−1)(2m−4) = 6m²−18m+12`, `3m(5m−11)(2m−4) = 30m³−126m²+132m`, `3m(2m−3) = 6m²−9m`, `m(2m−3) = 2m²−3m`, and the four bracket values `43m−103`, `79m²−241m+120`, `26m−36`, `3m−4` are exact equalities at `u_max`. These are polynomial identities of degree ≤ 3 in `m`, checked at 37 values of `m`. | True. The removed phrase was false, as D5 said. |
| "Here and in the next item the `d_k` are taken from the formula of Lemma C1, not computed from the tree" | `spine3.py` lines 282 and 289 call `coefficients(a, b, c, …)`, which implements the C1 formula | True |
| "these two items test Lemma C2 and Step 3 given Lemma C1, and say nothing about Lemma C1 itself" | The second item includes `spine3.py:293–294`, proportionality to `near_star_families.caterpillar_coefficients([a, b, c], …)`. For each tree, that function forms the 6 × 6 quotient matrix from the L3 rules, takes its exact characteristic polynomial (`fmpz_mat.charpoly`) and multiplies by the binomials. That is a per-tree test of the expansion step of C1 (the stated `g_j`), conditional on L3. Also, the second item checks no identity of Lemma C2. | **Inaccurate** (F-T2-3) |
| "six larger caterpillars (621 trees)" | `spine3.py:296–302, 311`: 615 trees with `a ≤ c`, `a+b+c ≤ 20` (own count, script D), plus the list `larger` of six. One of them, `(1, 1, 1)`, has `a+b+c = 3` and is already in the range. So there are 621 comparisons of 620 distinct trees, and only five of the six are "larger". | **"621 trees" is wrong by one; "six larger" (pre-existing wording) is wrong** (F-T2-2) |
| "This is the only item, with the test below, that tests Lemma C1 against the tree." | `matches_direct` builds the distance matrix from the parent array (`distpoly.py:65–82`) and does not use L3. `test_spine3_closed_forms_and_peak` compares orders 6–17 with the direct determinant and five trees with the Laplacian method. The other items use the formula or the rule-built `Q`. | True ("against the tree") |

## Question 3 — were the earlier defects addressed, and was anything removed that a reviewer relied on?

### T1: the list in the T1 review, "Unresolved gaps" items 1–7 and the two wording points of its "Checks" row

| Earlier point | Addressed? |
| --- | --- |
| (1) The dependency list omits Fact 1.1 and Observation 3.1; Step 4 attributes positivity to Theorem 2.1 | Yes (H3, H5) |
| (2) The diameter-≤-3 remark rests on an unread theorem and does not carry the strong reading to stars | Yes (H6). The concluding sentence does not name the reading (F-T1-3). |
| (3) "order `1/n`" is unproved | Yes (H6). It is now labelled an observation, with an unsourced basis (F-T1-1). |
| (4) Notation collisions `c_i`, `s` | Yes (H2) |
| (5) "which is why" needs the `a ↔ b` symmetry | Yes (H4) |
| (6) "agreement" means proportionality, and the comparison does not test the sign | Yes (H7) |
| (7) "strong reading of ties" is undefined | Yes (H3) |

Nothing the T1 reviewer relied on was removed or weakened. The proof text that
the review reconstructed (D1, Steps 2–4) is unchanged except for the corrected
citation in Step 4. The review itself had already identified that citation:
"Fact 1.1 … needed … for positivity in Step 4". The deleted clause "so T1 is
an exact statement, not a consequence of a crude bound" was not used by the
review.

### T2: defects D3–D7 of the T2 review

| Defect | Addressed? |
| --- | --- |
| D3: which checks take the `d_k` from C1 | Yes, but the new text overstates it in the other direction: it says the second item says "nothing about Lemma C1" (F-T2-3). It also introduces a miscount (F-T2-2). |
| D4: the title is broader than the theorem; "length 3" | Yes (H1, H2). The explanatory sentence wrongly attributes the phrase "spine length 3" to `lemmas.md` (F-T2-1). |
| D5: "in fact at a larger value" | Yes (H4). The change is correct. |
| D6: the inconsistent sentence placing Fact 1.1 "only in Step 4" | Yes (H3) |
| D7: dependency on R1's general form, recorded as not re-reviewed | **Partly.** The revision narrows the use to one direction. Neither note records the review status of R1's general form, and `lemmas.md` (unchanged) still says at lines 6–7 that R1 "was restated afterwards … and has not been re-reviewed". On record, the T1 review of `5e5ef14` says it covered "the restated general form", and the T2 review checked the direction used. The status line of `lemmas.md` is therefore out of date, but that is outside the two files rechecked here (F-T2-5). |

Nothing the T2 reviewer relied on was removed or weakened. The text the T2
review verified is unchanged: the statement, C1, C2, the `H` table, the
inequalities of Step 3 (verified at `u_max`), Step 4 and the Scope remark.

## Question 4 — do the "Revision history" sections describe the diffs?

**T1** (lines 249–266). Items (a)–(g) each correspond to a real hunk, and each
description is accurate. "No statement, formula or step of the proof was
changed" is accurate in the sense established above: the only change inside a
proof step is the citation in Step 4, which item (a) records. It omits two
things:
- the deletion of the clause "so T1 is an exact statement, not a consequence of
  a crude bound" (item (c) names only the "tends to 0" and "order `1/n`"
  assertions);
- the header sentence, which is trivial.

The first entry ("`241dc03` … unchanged at `5e5ef14`") is correct
(`git log --follow`).

**T2** (lines 297–312). The listed changes are accurate:
- the title (D4);
- the dependency list (D6, D7);
- the Step 3(i) phrase (D5);
- the checks description (D3).

The claim "No statement, formula or step of the proof was changed" is accurate.
Three changes are not mentioned:
- the second added sentence of H2 ("The condition `a, b, c ≥ 1` is part of
  every statement below; … `b = 0` … not treated");
- the count "(621 trees)";
- the header sentence.

The added sentence "This is the only item … against the tree" falls under the
D3 description. Calling D7 addressed overstates it slightly (see Question 3).
The first entry ("`74cb5bb` … first version") is correct.

## Findings

Numbered for reference. None is a mathematical gap in T1 or T2.

- **F-T2-1 (new false statement).** `spine3.md` lines 25–26 say that `lemmas.md`
  calls this family "spine length 3". It does not: `lemmas.md` never uses the
  phrase "spine length". The underlying clarification, that the project counts
  spine vertices, is correct.
- **F-T2-2 (new wrong count).** `spine3.md` line 287 says "six larger
  caterpillars (621 trees)". The code makes 621 comparisons on 620 distinct
  trees, because `(1, 1, 1)` is both in the `a+b+c ≤ 20` range and in the
  `larger` list. Only five of the six are larger. The phrase "six larger"
  predates the revision and was not flagged by the T2 review. The number 621
  is new. `results/spine3.json` reports 621 under
  `compared_with_direct_determinant`, which counts comparisons.
- **F-T2-3 (new inaccurate description).** `spine3.md` lines 279–282 say that
  the `a+b+c ≤ 300` item and the `a+b+c ≤ 60` item "test Lemma C2 and Step 3
  given Lemma C1, and say nothing about Lemma C1 itself". This is wrong in two
  ways:
  - the `≤ 60` item includes the proportionality check against the exact
    characteristic polynomial of the rule-built quotient matrix, which tests
    the computer-assisted expansion step of C1 tree by tree (conditional on L3,
    not against the tree);
  - that item does not test C2 at all.

  The error understates the evidence; it does not overstate it.
- **F-T2-4 (incomplete history).** See Question 4.
- **F-T2-5 (D7 partly addressed; record inconsistency outside the two files).**
  See Question 3.
- **F-T2-6 (`spine3.py`).** Only docstring line 1 changed. That line feeds the
  `argparse` description, so `--help` output changed; nothing computational
  changed. Docstring line 5 and the `"experiment"` string at line 257 still say
  "spine length 3".
- **F-T1-1 (unsourced observation).** `double-stars.md` lines 224–225, "In the
  exact values computed, the relative margin … decreases roughly like `1/n`",
  names no computation. My exact computation is consistent with it, but the
  constant depends on parity:
  - `n(1 − d_{m−1}/d_m)` lies in about [0.84, 1.11] for even `n`;
  - it lies in about [2.68, 3.11] for odd `n`.

  The sentence also leaves open which double star of order `n` is meant.
- **F-T1-2 (loose wording).** Line 78: "exchanging the two centres is an
  automorphism of the family". The exchange is an isomorphism `S(a,b) ≅ S(b,a)`,
  and an automorphism of a single tree only when `a = b`. The conclusion
  (`det(2xI − Q)` is symmetric in `a, b`) is true. I verified it directly as
  `Q(b,a) = P Q(a,b) Pᵀ` and on the expanded polynomial.
- **F-T1-3 (unnamed reading).** Lines 220–221 say "the conjecture for all trees
  of diameter at most 3" holds on the strength of T1 and Collins's theorem,
  without saying which reading of ties. For stars, only the weak reading
  follows from what the project has. The clause just before it ("that report
  does not say how ties are treated") implies this but does not state it.
- **F-T1-4 (incomplete history).** See Question 4.
- **Pre-existing, outside the diff, not counted against the revision.** Line
  215 is an unchanged context line: "A tree of order `n ≥ 3` has diameter 2 (a
  star) or, if its diameter is 3, is a double star". Read literally, it omits
  "of diameter at most 3", which the heading supplies.

## Question 5 — does each earlier verdict still apply?

**T1: `earlier review still applies to the revised text`.**

- There is no class (iii) hunk.
- The class (ii) changes are H3 (second part, the dependency list) and H5
  (Step 4 positivity). They change only which published results are cited,
  and where. They add Fact 1.1 and Observation 3.1 and move positivity from
  Theorem 2.1 to Fact 1.1.
- These citations are exactly the dependencies the T1 review had already
  established and conditioned its verdict on ("conditional on two results taken
  from the source … Fact 1.1 … and Theorem 2.1(iii)", and the dependency row).
- What needed re-review was whether the new citations match the source and
  support the step. I checked this against arXiv:1507.02341v3, pages 2, 4 and 5.
  They do.
- The class (i) hunks touch no proof step. F-T1-1 to F-T1-4 concern remarks,
  the checks description and the history. They are not covered by the earlier
  review, because they did not exist when it was written, and they do not bear
  on T1.

**T2: `earlier review still applies to the revised text`.**

- There is no class (iii) hunk.
- The class (ii) changes are H3 (the dependency list) and H4 (Step 3(i)
  wording).
  - H3 cites the same set of results as before. It places Fact 1.1 and
    Observation 3.1 in Step 1, which matches the T2 review's D6, and it
    restricts R1 to the direction that the T2 review checked ("Only the 'if'
    direction is used … It is correct").
  - H4 removes a false phrase. The inequalities of Step 3(i) are unchanged and
    were verified by the T2 review as exact equalities at `u_max`. I verified
    them again (script C).
- What needed re-review was the R1 direction statement against Step 4, and the
  location of the bounds in Step 3(i). Both are confirmed.
- F-T2-1, F-T2-2 and F-T2-3 are new errors in descriptive text: the
  family-name paragraph and the Checks section. They lie outside the proof and
  outside the earlier verdict's scope. They should be corrected, but they do
  not affect T2.

**On the author's assertion that the revision "changes presentation only".**
It is not refuted as far as the mathematics goes:
- no statement, hypothesis, quantifier, definition used in a proof, or formula
  changed, and no step changed its logical content;
- strictly, two hunks per file are class (ii): they change citations or the
  wording of a justification, not presentation alone.

What is refuted is narrower. The revised presentation is not free of error:
three new sentences of `spine3.md` are false or inaccurate (F-T2-1, F-T2-2,
F-T2-3).

## Reproduction

All on 2026-11-26, at `1c386621bbf5083e89259a9e6ff9cae341c3b4a7`, clean tree,
Windows 10, Python 3.12.4.

Repository commands:
- `git rev-parse HEAD` gave `1c386621…a7`. `git status --short` gave empty
  output before and after.
- `git diff 5e5ef14 HEAD -- …/double-stars.md`,
  `git diff 74cb5bb HEAD -- …/spine3.md …/spine3.py`, and both with
  `--word-diff=plain`.
- `git log --oneline --follow` on each file;
  `git diff --stat 241dc03 5e5ef14` (only `results/double-stars.json`);
  `git diff --stat` of `lemmas.md`, `experiments/` and `tests/` between each
  reviewed revision and `HEAD`.
- `sha256sum` on the working-tree files and on `git show <rev>:<path>`;
  `git hash-object`.
- `uv run pytest tests/test_cj0001_distpoly.py -k "spine3 or double_star" -q`
  gave `2 passed, 95 deselected in 2.55s`. `uv` printed a warning that an
  unrelated `VIRTUAL_ENV` was ignored.
- `uv run python experiments/CJ-0001-collins-shor-peak/spine3.py --help`
  prints the new docstring line as the description.
- **Not rerun:** the full `spine3.py` and `double_stars.py` runs that produced
  the result files. Lean was not run: no Lean statement concerns T1 or T2, and
  formalization is outside this recheck.

Independent calculation:
- The script is
  `C:\Users\bezze\AppData\Local\Temp\claude\150e3719c412ed18\7b0a0d46-923f-4f04-ae71-5a9e832991c4\scratchpad\recheck\recheck.py`
  (SHA-256 `754892c38717deb6bfed6b136c00b5431afcfc3a917dccea64e8ec082dd78fec`),
  driven by `fastb.py` in the same directory.
- It ran under `python -I`, imports only `fractions`, `itertools` and `math`,
  and imports nothing from the repository. It lives outside the repository and
  is not preserved.
- A first, slower driver (the script's own `__main__`) was started in the
  background with a 600 s timeout. The timeout stopped it (exit code 124)
  before it printed anything, so no result from it is used.

What the script does and found:
- **A.** Builds `Q` for `S(a,b)` from the L3 block rules as exact polynomials in
  `(a, b, x)` and expands `det(2xI − Q)` by the Leibniz formula. The result is
  affine in `a`, affine in `b` and symmetric, and it equals the stated quartic.
  `Q(b,a) = P Q(a,b) Pᵀ` holds. All checks True.
- **B.** Computes `d_k` from the definition (BFS distance matrix and exact
  Faddeev–LeVerrier characteristic polynomial, with the sign of Fact 1.1
  asserted). These equal D1 for `1 ≤ a ≤ 6`, `a ≤ b ≤ 8`. Then
  `n(1 − d_{m−1}/d_m)` was computed exactly over all `1 ≤ a ≤ b`, using D1,
  which the T1 review verified. Values below are rounded floats, for display
  only:

  | `n` | min | at | max | at |
  | --- | --- | --- | --- | --- |
  | 6 | 0.838 | (1,3) | 0.892 | (2,2) |
  | 7 | 2.679 | (1,4) | 2.754 | (2,3) |
  | 14 | 0.964 | (1,11) | 0.996 | (6,6) |
  | 15 | 2.853 | (1,12) | 2.936 | (6,7) |
  | 100 | 0.909 | (49,49) | 1.088 | (1,97) |
  | 101 | 2.910 | (49,50) | 3.064 | (1,98) |
  | 2000 | 0.860 | (999,999) | 1.110 | (1,1997) |
  | 2001 | 2.861 | (999,1000) | 3.109 | (1,1998) |

  The other orders computed (8–13, 40, 41, 400, 401) lie within these ranges
  for their parity.
- **C.** The Step 3(i) bounds of T2 at `u = u_max` are exact equalities. True.
- **D.** The count of trees in `spine3.py`'s direct comparison: 615 with
  `a+b+c ≤ 20`, plus 6 listed, of which 5 have `a+b+c > 20`. So 621 comparisons
  and 620 distinct trees.

## Verdict

- **`double-stars.md` (T1):** `earlier review still applies to the revised text`.
- **`spine3.md` (T2):** `earlier review still applies to the revised text`.

**Scope.** This recheck covers:
- the diffs `5e5ef14..1c38662` of `double-stars.md` and `74cb5bb..1c38662` of
  `spine3.md` and `spine3.py`;
- the truth of every added or reworded sentence in them;
- whether the citations to Fact 1.1, Observation 3.1 and Theorem 2.1 of
  arXiv:1507.02341v3 agree with the source;
- whether the earlier verdicts carry over.

**Not covered.** This recheck does not cover:
- a fresh review of the proofs;
- novelty, which was not assessed;
- formalization;
- `lemmas.md` beyond the lines cited;
- `STATE.md`, `journal.md` and `research/discoveries.json`, and so whether the
  registry entries for MD-0006 and MD-0007 match these texts;
- the other files changed by `1c38662`;
- re-execution of the full documented computations.

This is an AI recheck, not human review. It applies only to revision
`1c386621bbf5083e89259a9e6ff9cae341c3b4a7`.
