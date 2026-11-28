# Independent review — CJ-0001 — direct proof of Collins's formula for the path

- **Reviewer:** claude-sonnet-5-5 (Sonnet 5.5)
- **Date:** 2026-11-27
- **Independence:** fresh subagent context. It was given the claim file, the
  manuscript statements, and the instruction not to read the journal, STATE.md or
  other notes. It did not see the author's reasoning trail. I re-derived the
  steps myself and ran my own code. The reviewer is a different model from the
  author (`claude-opus-5-5`), but both are Claude models.
- **Revision reviewed:** commit e15ae8f16b7d961f34a77e80bdef91debeede1cb (branch `research`).
  - `research/active/CJ-0001-collins-shor-peak/notes/path-formula.md`: SHA-256 06dbd51c87089c8a98815d2c4a77f550fceced95fc9272439c4f1b1800f53f1d (matches the hash given).
  - `manuscripts/CJ-0001-collins-shor/main.tex`: SHA-256 3477baa0902eb3446415167baf38e83e939fb68f002f55b1162ebee2337d917b.
  - `experiments/CJ-0001-collins-shor-peak/path_formula_check.py`: SHA-256 ee5f524e94c1a72a28dc8ff92949ba6120ef915bba421497ee23924b7654e512.
- **Material given to the reviewer:** the note, the manuscript (Lemma 2.1
  `lem:ident`, Lemma L1 `lem:L1`, `lem:path` read in the manuscript), and the check script.

## Statement as read from the primary source

For n ≥ 2 and 2 ≤ k ≤ n: d_{n−k}(P_n) = C(n+k−1, 2k−1)(k−1)n/k. Here
d_j = 2^{j−(n−2)}|δ_j| and δ_j = [x^j] det(D − xI), with D the distance matrix of
P_n. The quantifiers are over all n ≥ 2 and all k in [2, n], that is, over
j = n−k in [0, n−2]. This matches the range in Lemma 2.1.

Manuscript conventions, checked:
- ℓ_T = −2^{−(n−2)} det(2xI − D).
- Lemma 2.1: [x^j]ℓ_T = d_j for 0 ≤ j ≤ n−2, n ≥ 2. The proof in the manuscript
  gives [x^k]ℓ_T = (−1)^{n−1}2^{k−(n−2)}δ_k with sign (−1)^{n−1}δ_k > 0. This agrees
  with the definition of d_j by absolute value.
- Lemma L1: ℓ_T = (n−1)Φ_T − x τᵀ adj(M) τ with M = I + xL. The proof was checked
  (matrix determinant lemma, signs, scaling by det D). It also holds for n = 2 by
  the explicit computation in the manuscript.
- Lemma `lem:path`: adj(M)_{vv'} = x^d det M[Q]. The lemma is stated for weighted
  trees, and the unweighted case is ν = 0. For the end vertices of P_n, d = n−1 and
  Q = ∅, so det M[∅] = 1 and adj(M)_{1n} = x^{n−1}. The proof is stated for x > 0;
  both sides are polynomials in x, so the identity holds identically. The
  d = 0 case gives adj_{vv} = det M[V∖{v}].

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | The note uses only Lemma 2.1, L1, `lem:path` and Cauchy–Binet. Hypotheses n ≥ 2 and 2 ≤ k ≤ n are used exactly where needed. No defect. |
| Quantifiers | The range k in [2, n] is j in [0, n−2], the range of Lemma 2.1. The x^n term of ℓ (from 2x^n) is irrelevant for j ≤ n−2, as the note says. No defect. |
| Mathematical definitions | The sign and scaling conventions of the note agree with the manuscript (ℓ_T, M = I + xL, τ_v = 2 − deg v). No defect. |
| Boundary cases | k = n (j = 0): [x^{−1}]A_n = 0 and C(2n−1, 2n) = 0, consistent; formula gives C(2n−1, 2n−1)(n−1)n/n = n−1 = d_0. For n = 2, d_0 = 1 and ℓ = 1 − 4x², which matches. k = 2: r = 3 is used for A_n, which needs n ≥ 3 for a nonzero value, and C(n+1, 4) = 0 for n = 2 (and n = 3: C(4,4) = 1 is correct). The r = 1 term of A_n: the only composition is (n), the product c_2…c_r is empty = 1, and C(n−1, 0) = 1 (matches generating function z/(1−z)·(…)^0). No off-by-one found in the index of A_n. |
| Step 1 (τ, symmetry, cofactor) | τ_v = 2 − deg v is 1 at the two leaves and 0 elsewhere (n ≥ 3); for n = 2 both vertices have degree 1, so τ = e_1 + e_2 = e_1 + e_n. Hence τᵀ adj τ = adj_11 + adj_nn + 2 adj_1n = 2A_n + 2x^{n−1}, and x·(that) = 2xA_n + 2x^n. The symmetry adj_11 = adj_nn holds because the reversal permutation fixes M; adj_11 = det M[V∖{1}] = A_n. I reproduced this. d_j = (n−1)[x^j]Φ − 2[x^{j−1}]A (the 2x^n term is outside j ≤ n−2). No defect. |
| Step 2 (Cauchy–Binet forest expansion) | Reproduced. M[W] = I + x B_W B_Wᵀ holds for any orientation of B (L = BBᵀ). det(I_W + xXY) = det(I_{n−1} + x B_Wᵀ B_W) is Sylvester's identity. Cauchy–Binet applied to the principal minors of G = B_Wᵀ B_W gives Σ_S x^{|S|} det(B_W[·,S]ᵀ B_W[·,S]) = Σ_S x^{|S|} Σ_{R⊆W,|R|=|S|} det(B[R,S])². The case S = ∅ gives 1 (R = ∅). For the block-diagonal argument: edges of S lie inside components of the forest (V, S), so B[R,S] is block diagonal after ordering. The row total equals the column total, so if some block has fewer rows than columns, another has more rows than columns, and singularity follows from linearly dependent columns in the first block. Hence nonsingular ⇒ all blocks square. Each block is the incidence matrix of a tree with one row deleted, det ±1 (totally unimodular, and deleting a row of a tree incidence matrix leaves a nonsingular matrix: root it at the deleted vertex and order the columns by the leaf-to-root order, giving a triangular matrix with ±1). Isolated vertices: a 0×0 block, R must omit that vertex (one choice, |C| = 1), contributes factor 1. All consistent. For W = V∖{u}, the component containing u must omit u (1 choice), the others |C_i| choices each. Result Φ = Σ x^{|S|} Π|C_i| and det M[V∖{u}] = Σ x^{|S|} Π_{u∉C_i}|C_i| is correct. Check on P_2: Φ = 1 + 2x, M[V∖{1}] = 1 + x. Both match. No defect. |
| Step 3 (compositions, generating functions) | Spanning forests of P_n with r components correspond to compositions of n into r parts (choice of r−1 cut edges), |S| = n−r. Σ_{c≥1} c z^c = z/(1−z)², so [z^n](z/(1−z)²)^r = [z^{n−r}](1−z)^{−2r} = C(n−r+2r−1, 2r−1) = C(n+r−1, 2r−1). For A_n: u = 1 lies in c_1 (the first component), so the product is c_2…c_r and the generating function is z/(1−z)·(z/(1−z)²)^{r−1} = z^r/(1−z)^{2r−1}, so [z^n] = [z^{n−r}](1−z)^{−(2r−1)} = C(n−r+2r−2, 2r−2) = C(n+r−2, 2r−2). Both reproduced. No defect. |
| Step 4 (algebra) | j = n−k gives r = k for Φ (C(n+k−1, 2k−1)) and r = k+1 for [x^{n−k−1}]A_n = C(n+k−1, 2k). Ratio: C(n+k−1, 2k)/C(n+k−1, 2k−1) = (n+k−1−(2k−1))/(2k) = (n−k)/(2k). Then d_{n−k} = C·[(n−1) − 2(n−k)/(2k)] = C·[(n−1) − (n−k)/k] = C·(nk − k − n + k)/k = C·n(k−1)/k. Reproduced. |
| Logical implications | Step 1 reduces ℓ to Φ and A_n coefficients; Step 2 gives them as forest sums; Step 3 evaluates for P_n; Step 4 combines. All implications reproduced, and every case n ≥ 2, 2 ≤ k ≤ n is covered. |
| Dependency assumptions | Depends on manuscript Lemma 2.1 (from [AAB, GL78]), L1 (from (GL) inverse and (GP) determinant, both cited, not proved here), and `lem:path` for the cofactor x^{n−1} (this is the one place where the path cofactor is used; it is also elementary for a path: the cofactor of a tridiagonal matrix with off-diagonal −x is x^{n−1}, which I checked numerically). The note does not claim to be independent of (GL)/(GP), and the manuscript marks these as classical results used without proof. Collins's formula itself is not used in the proof (no circularity: Lemma `lem:path` and L1 do not use Section 11). |
| Counterexample attempts | The formula was checked exactly for all n = 2…15 (see Reproduction). No counterexample. |
| Formalization scope | Not applicable; no Lean claim is made. |
| Novelty coverage | Not assessed by this review. The note itself states novelty of the proof was not searched. Not searched here either. The formula is the published Theorem 3 of Collins (1989); the review concerns only the correctness of this independent derivation. |
| Unresolved gaps | None of mathematical substance. Cosmetic items below. |

Cosmetic observations (not gaps):
1. Step 4 of the note says "(Step 3, r = k+1; for k = n both sides are 0)". This is correct but the reader must note that r = n+1 gives an empty set of compositions.
2. `path_formula_check.py` skips the direct distance-matrix comparison for n = 2 (`if n >= 3`). I checked n = 2 by hand: d_0 = 1 = formula, ℓ = 1 − 4x².
3. The proof of Step 2 asserts "each block is the incidence matrix of a tree with one row removed, whose determinant is ±1" without proof. This is a standard fact (I reproduced it via a leaf-peeling argument). It is acceptable at this level, since the note says it cites nothing beyond Cauchy–Binet. The fact could be stated as a one-line lemma.
4. The note says "Lemma 4.3" for the path cofactor formula; the label in the manuscript is `lem:path` (section number not verified; the lemma exists and has the stated content).

## Reproduction

- `uv run python experiments/CJ-0001-collins-shor-peak/path_formula_check.py`
  (about 12 s; it uses python-flint). Output: `"failures": 0`,
  `"composition_sums": {"cases": 144, "failures": 0}`. I read the script: it
  computes Φ, A_n, ℓ by exact interpolation of determinants, compares the
  coefficient formulas of Step 3 (including r = 1 for A_n), the identity ℓ = (n−1)Φ − 2xA − 2x^n,
  and the distance-matrix coefficients via `fmpz_mat.charpoly` (normalisation 2^j/2^{n−2}, absolute value)
  for n ≥ 3, and brute-forces the composition sums for n ≤ 12. No logical defect found in the script.
  Note: the identity in the script includes the term rhs[n] −= 2, matching the 2x^n term. The
  script's "ell" is the true ℓ from the determinant of 2xI − D, not derived from the formula, so the check is not circular.
- My own independent code (exact `Fraction` arithmetic, Gaussian elimination and Vandermonde interpolation, no
  project code, no sympy): for n = 2…15, (a) d_{n−k} = 2^{j−(n−2)}|[x^j]det(D − xI)| equals C(n+k−1, 2k−1)(k−1)n/k for every 2 ≤ k ≤ n;
  (b) [x^{n−r}]det(I + xL) = C(n+r−1, 2r−1) and [x^{n−r}]det((I + xL)[V∖{1}]) = C(n+r−2, 2r−2) for all 1 ≤ r ≤ n.
  Result: 0 failures. (My attempt with sympy failed only because sympy is not installed; I did not use it.)
- Hand derivation of the algebra of Steps 1–4, as in the Findings.
- I did not re-run `scripts/verify_lean.py` (no Lean content). I did not run the full test suite.

## Verdict

`no gap found within stated scope`

Scope: this verdict covers the correctness of the written derivation of
formula (C) in `path-formula.md` at commit e15ae8f (hash above), given the
manuscript's Lemma 2.1, Lemma L1 and `lem:path` (including their classical
inputs (GL), (GP), [AAB], [GL78], which this review did not re-prove, but whose
combined consequences used here were checked exactly for n ≤ 15). It does not
cover novelty (not searched), the manuscript elsewhere, any Lean statement, or
anything other than this revision. Finite checks (n ≤ 15 mine, n ≤ 40 the
project's script) support but are not part of the proof; the proof rests on the
Steps re-derived above.
