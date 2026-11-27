# Independent review — CJ-0001 — manuscript "On the peak of the coefficients of the distance characteristic polynomial of a tree: a candidate proof of the Collins–Shor conjecture" (both halves)

- **Reviewer:** Claude, model `claude-opus-5-5` (Anthropic), acting as adversarial reviewer.
- **Date:** 2026-11-27 (wall clock 17:33 to about 18:00).
- **Independence:** fresh subagent context. I received only the task message:
  the primary source (arXiv:1507.02341, Conjecture 1.2), the manuscript path
  and revision, and the instructions. I did not read anything under
  `research/active/CJ-0001-collins-shor-peak/notes/`, `STATE.md`, the journal,
  or any earlier review before finishing my own assessment of every proof.
  Afterwards I tried to list the earlier reviews for comparison; the
  environment's permission classifier refused that command, so **no comparison
  with earlier reviews was made**. The one project file I read besides the
  manuscript was a grep over `experiments/` for a tree count (defect 4).
  Limitation: I am the same vendor's model as the author of much of the text
  (the manuscript names `claude-opus-5-5` as the author of this text). That is a
  fresh context, not a different model.
- **Revision reviewed:** Git commit `8df6beac16b54e218d66ec3470a3f49a91546b17`
  (`8df6bea`). File `manuscripts/CJ-0001-collins-shor/main.tex` (1855 lines).
  - Git blob id at 8df6bea: `50136b053757650dcd5c8ee3f26b1b6089b69fb3`.
  - SHA-256 of the blob as stored in Git (LF endings, `git show 8df6bea:…`):
    `8feaaa4b7dc9cd2fe5131e67df3098c56c0138f2bec8513de40820da3aa1a5f0`.
  - SHA-256 of the working-tree file as read (92,100 bytes, 579 CR bytes):
    `0bf1928f33c215e046d49fd3e0a4b0db0cff80b3f8dd7d6819580da327e711c8`.
  - `git diff 8df6bea -- manuscripts/CJ-0001-collins-shor/main.tex` is empty.
    During the review HEAD moved to `2047ebb` (two commits by another session,
    neither touching the manuscript; checked with `git diff --stat 8df6bea HEAD`).
- **Material given to the reviewer:** the task message only. I read the
  primary source myself (arXiv:1507.02341v3, fetched and converted with
  `pdftotext`; floors and ceilings were lost in conversion, so for those
  symbols I relied on the task statement and on the source's surrounding prose).

## Statement as read from the primary source

Written before I read the proofs.

- *Objects.* A tree T of order n with distance matrix D(T). δ_k(T) is the
  coefficient of x^k in det(D − xI). Fact 1.1 of the source:
  (−1)^{n−1} δ_k > 0 for 0 ≤ k ≤ n−2. Normalized coefficients
  d_k = 2^{k−(n−2)} |δ_k| = (−1)^{n−1} δ_k / 2^{n−k−2}, for 0 ≤ k ≤ n−2.
- *Standing convention of the source.* "Throughout this discussion, the order
  of a graph is assumed to be at least three (any sequence a_0 is trivially
  unimodal and the peak location is 0)."
- *Conjecture 1.2 (Collins–Shor).* For every tree T with n vertices, the
  normalized coefficients are unimodal, with peak between ⌊n/2⌋ and
  ⌈n − n/√5⌉. Unimodality is Theorem 2.1 of the source, with log-concavity.
- *Quantifiers.* For all n ≥ 3 (by the convention) and all trees T of order n.
- *Reading of ties (as instructed).* Strong reading: **every** index p with
  d_p = max_k d_k satisfies ⌊n/2⌋ ≤ p ≤ ⌈n − n/√5⌉.
- *Degenerate case.* For n = 2 the sequence is (d_0) = (1). The peak is 0,
  and ⌊2/2⌋ = 1 > 0, so the literal statement is false at n = 2. The source's
  n ≥ 3 convention is what excludes this case.
- *Source's own status.* Section 3 says the peak location "remains open" and
  that Sage confirmed the conjecture for all trees of order at most 20. The
  source proves peak ≤ ⌈2n/3⌉ (Theorem 3.3) and peak ≥ ⌊(n−2)/(d+1)⌋
  (Theorem 3.6).

The manuscript's Main Theorem is about this statement with n ≥ 3, in the
strong reading of ties. It is in fact stronger on the upper side: every
maximizer satisfies p ≤ ⌈n − n/√5 − 2/5⌉, equivalently p < n − n/√5 + 3/5. The
restriction n ≥ 3 is the source's convention, but the manuscript does not say
so (defect 3).

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | Every result states its order hypothesis (n ≥ 1, ≥ 2 or ≥ 3). I checked each one against the lemmas it calls: Lemma S41 needs n ≥ 3 and k ≤ n−3; Theorem 6.6(c) needs 1 ≤ m ≤ n−2, which holds for n ≥ 3; Lemma 7.3 (S43p) needs \|X\| ≥ 2, which Lemma S45 and Theorem T10 supply. The cited classical results are used within their hypotheses. (W) is used for a rank-one PSD update. (N) and (D) are applied to q, which has positive coefficients and only negative real zeros. (M) is applied to connected graphs. (LC) is applied to trees of order ≥ 3. |
| Quantifiers | Main Theorem: for all n ≥ 3, all trees T of order n, every maximizing index p. This matches the strong reading. The lower half proves strict increase up to m = ⌊n/2⌋ (Lemma R1 "if" direction with (LC)). The upper half proves strict decrease from K on (Lemma S41). So no maximizer lies outside [m, K], and ties are covered on both sides. |
| Mathematical definitions | d_k, ℓ_T = −2^{−(n−2)} det(2xI − D) and Lemma 2.1 match the source (Observation 3.1, Fact 1.1). Cones K_d and properties (K1), (K2): checked by hand. Rooted-tree state (Ψ, H, G, Ω, R_0), root weights, E, a_v, J, W, Q^1: all well defined. H is a polynomial because Φ_0 and Ψ have constant term 1. Division by Ψ is division by a nonzero polynomial. |
| Boundary cases | a = 1: Ψ = 1, Ω = H = G = E = R_1 = 0, R_0 = −(1+2x)^2. Checked by hand and in my code. n = 1: ℓ = −4x, and Corollary 4.4(a) holds. n = 2: Lemma L1 checked directly; Theorem 6.6(b) is trivial since T = S_2. n = 3: Lemma 6.7 value is 4; the upper bound is trivial (K = 2 ≥ n−2 = 1). n = 3, 4, 5: path cases of Lemma S47, all six values of h_n recomputed. q = 1 in Proposition 5.4(d): trivial, and it is the case a = 2 of Theorem T5. Empty sums: \|A_i\| = 1 makes H_i, G_i and the double sum in S35 vanish, and K_{−1} = K_0. d ≤ 0 cones: K_d = K_0, used for H ∈ K_{a−2} at a = 1, 2. Lemma A: a ≤ 0 and a ≥ 1 both checked. Lemma S44: r = 0 is allowed in (eq:Grr) and (eq:cr); the equality case N = 2, r = 1 is correct. |
| Lemma 2.3 (R1) | "If" direction (the only one used): correct. **"Only if" proof contains a false sentence** ("j−1 is a maximizing index"); see defect 2. The conclusion of that direction is still true. |
| Lemma 2.4 (L1) | Reconstructed: the matrix determinant lemma with A = −M, the signs (−1)^n and (−1)^{n−1}, and (GP). Checked indirectly by my exact check of Corollary 4.4(a), which computes ℓ_T from D (all trees of order ≤ 7, 3 rational points). |
| Lemma 3.2 (A) | Reconstructed. Correct. |
| Lemma 4.1 (blocks) | Correct: a component of T − V(P) joined to P by two edges would close a cycle. |
| Lemma 4.2 (K) | Expansion (eq:K3) re-derived: the affine-in-(u,u)-entry step and the cancellation of x^2·det N[U∖{w,u}]. Membership induction checked. A leaf w with ν' ≠ 0 always exists for j ≥ 2. The components of K − {w,u} get unit extra weight. Correct. |
| Lemma 4.3 (path cofactor) | Checked: the Schur complement on V(P) is tridiagonal, because each component of K[Q] touches P at exactly one vertex through exactly one edge. The cofactor of S at (d,0) is the determinant of a lower-triangular matrix, (−x)^d, and the sign (−1)^d gives x^d. Membership via Lemma K with weights ν\|_{K'} + e_a ≠ 0 holds even when ν = 0. Correct. |
| Corollary 4.4 (phi1) | Correct (a leaf w ≠ c exists, ν_w = 0, and the minor lies in K_{b−2}). |
| Lemma 5.1 (star identity) | Reconstructed: Schur complement at u, q_i = p^{(1)} of the branch, Σa_i = a−1. Checked exactly for w = 0, 1, 2 on all rooted trees of order ≤ 7. Correct. |
| Proposition 5.2 (rules a–d) | (b): re-derived the coefficient (1+2x)^2. (c): re-derived Φ̂_0, Ĝ = x(xH+G), and row r of adj(M̂_0); the R̂_0 algebra was checked by exact computation rather than by hand. (d): re-derived the expansion and −2G_1G_2 + c^2Ψ_1Ψ_2. All checked exactly (see Reproduction). Correct. |
| Corollary 5.3 (leaf recursion) | (a), (b), (c), (d) re-derived. (b) uses that R_0 does not depend on the root, which holds. Checked exactly. Correct. |
| Proposition 6.1 (S33) | (a) to (e) re-derived, including Lδ = τ − 2e_u, p^{(1)} = M^1(1+δ) − δ, (1+δ)^T L(1+δ) = a−1, the symmetrization producing Q^1, and adj(M^1)_{vu} = x^{δ_v}Π_{uv}. Memberships follow from (K2) arithmetic, which I checked. Identities (b), (c), (e) checked exactly. Correct. |
| Proposition 6.2 (S34) | (a) to (d) re-derived by hand. (b): the coefficient of H is 3x^2 + 2x^3. Checked exactly. Correct. |
| Proposition 6.3 (S35) | Re-derived: Ĝ_i = x^2J_i and the sum-of-squares bracket. Membership degrees: a_1+a_2+2, a_1+a_2+2 and a_1+a_2+4. Identity checked exactly on all pairs of rooted trees of order ≤ 4. Correct. |
| Theorem 6.4 (T5) | Induction structure checked: (iii) follows from (i) and (ii) at the same order; (ii) uses (iii) for branches only. All cone levels recomputed: Ê_i ∈ K_{a_i+2}, P̂_i ∈ K_{a−1−a_i}, X̂_il P̂_il ∈ K_{a+1}. Correct. |
| Theorem 6.6 (lower bound) | (a): expanding the product Π((1+x)^{t_i} + b_i) is correct. (b): the telescoping difference is correct. The difference has degree ≤ n−2 because the x^n and x^{n−1} coefficients agree. (c): K_{n−1} ⊆ K_{2m−1} and 1 ≤ m ≤ n−2 are correct. Correct. |
| Lemma 6.7 (star value) | Formulas re-derived for even n. All three closed forms checked exactly against the binomial expression for 3 ≤ n ≤ 59, and against the distance matrix for n ≤ 13. Correct. |
| Remarks 6.8–6.10 | 6.8: attainment by the star rests on a citation; the argument is not reproduced (defect 6). I verified it in two lines (see defect 6) and exactly for n ≤ 59. 6.10 (cone C_d): correct, since a positive combination cannot cancel leading terms. |
| Lemma 7.1 (S40) | Correct: Weyl gives ν_2, …, ν_n ≤ 0, nonzero by (GP); the sign of the product gives ν_1 > 0; tr D = 0 gives α = Σβ_i. |
| Lemma 7.2 (S41) | All three cases reconstructed (j = 0; q_j ≥ q_{j−1}; q_j < q_{j−1}). αϱ_{j−1} > 1 needs j−1 ≤ n−3, which holds. Correct. |
| Lemma 7.3 (S42) | Correct: the Weyl lower bound gives \|ν_i\| ≤ μ_(i−1), and y/(1+y) is increasing. |
| Remark after S42 (Merris) | **The displayed interlacing chain is wrong at its end**; see defect 1. It is not used in any proof. |
| Lemma 8.1 (S43, gluing) | Re-derived: Schur complement, s = ε_Y, Sherman–Morrison, the trace of two blocks sharing v, and the conversion to g_T form. The degenerate cases Y = {v} and X = {v} were checked. Correct. |
| Lemma 8.2 (S43p) | Correct: the maximum-principle argument for G_{w*v} ≤ G_{vv}/2. |
| Lemma 8.3 (S44) | Re-derived e_j = cosh((2j+1)u)/cosh u, the path determinant, (eq:Grr), (i), (eq:cr) (constants 6/√5 and 2√5), the ψ-reduction of (iii), δ_0 = δ_1 (φ^4 − 3φ^2 + 1 = 0), the convexity criterion z·tanh z > 1, and tanh(3 log φ) = 2/√5. Correct. |
| Lemma 8.4 (S45) | Re-derived the identity for a(a+E)(a+E')[Θ(E',c') − Θ(E,c)] and the lower bound (a−1)(E−E')(c−1/2) > 0. Correct. |
| Theorem 8.5 (T10) | Induction on the number of leaves is correct: v is a vertex of degree ≥ 3 farthest from a leaf root; at least two of its branches are pendant paths; T' has one leaf fewer. Checked exactly on all trees of order 2 to 10 (strict, except for the path). |
| Lemma 8.7 (S46) | Poisson-kernel computation re-derived, including the three cases of Σ_j cos(mθ_j) and n = 1. The formula agrees with exact traces for n = 2 to 10 (exploratory float comparison, error < 1e−12). Correct. |
| Theorem 9.1 (upper half) | Correct: μ_q < ξ − 2/5, then Darroch, then m_q ≤ ⌈ξ − 2/5⌉ (since ξ − 2/5 is irrational), then q_{K+1} < q_K (which uses "every maximizer ≤ K"), then Lemma S41. The strong form of Darroch's rule (every mode is ⌊μ⌋ or ⌈μ⌉, and unique if μ is an integer) is consistent with the secondary account in arXiv:2408.06477, §5.1. Darroch's paper and Pitman's p. 284 were **not** read by me. |
| Corollary 9.2, remark | (a), (b) and the remark that Tr(T) > n/√5 suffices: correct. |
| Lemma 10.1 (S47) | Ratio formula re-derived; h_n ≡ −2 (mod k) excludes integer zeros; k_0 ≤ n−1; the location argument for n ≥ 6 (η > 1+√2) and the direct cases n = 3, 4, 5. Criterion checked exactly against the peak computed from (C) for 3 ≤ n ≤ 399. Correct, given (C). |
| Corollary 10.2 (pathceil) | Re-derived h_n(⌊η⌋)/⌊η⌋ = 2η(1−5θ) + 5θ^2 − 2θ − 4 − 2/k, and (a), (b), (c). Kronecker gives infinitely many n. Correct, given (C). |
| Logical implications | Main Theorem = Theorem 6.6(c) + Theorem 9.1. Both are proved for all n ≥ 3 in the strong reading. Attainment = Remark 6.8 (cited) + Corollary 10.2 (proved from cited (C)). No circularity: the lower half uses (LC) only at the last step, and the upper half does not use (LC). |
| Dependency assumptions | Cited without proof: (GL), (GP), (LC), (W), (N), (D), (M), (PS), (C), (Kr), and Col89 Theorem 1 (only for attainment). I did not read GL78, GP71, Col89, Dar64 or Pit97. I checked (GL)+(GP) indirectly (Lemma L1 by exact computation, order ≤ 7) and (C) exactly for 3 ≤ n ≤ 15. (LC) is in the source as Theorem 2.1. |
| Counterexample attempts | (1) Exhaustive exact peak computation over all trees of order 2 to 13: see Reproduction. (2) Coefficientwise star minimality and λ_μ(T) ≥ λ_μ(S_n) for 1 ≤ μ ≤ ⌊n/2⌋: all trees of order 3 to 11, no failure. (3) Lemma R1: counterexample to one sentence of its proof (defect 2). (4) Merris remark: counterexample to the displayed chain (defect 1). (5) Double star S(9,9): confirmed the claim of Section 11 item 2 that the ratio comparison with the star fails at k = 9 (exact: 1.05227 < 1.05319). No counterexample to any result used in the proofs. |
| Formalization scope | Section 13 claims only auxiliary formalization and says plainly that nothing about trees, determinants, Darroch's rule or traces is formalized. I did **not** run `scripts/verify_lean.py`: it writes a receipt, and I am permitted to write only this report. The formal status (partial, auxiliary only) is described accurately. |
| Novelty coverage | The manuscript claims no originality, and its "not found within coverage" statements are hedged. The exception is defect 5 (the GL attribution). My own search was 2 web searches and 1 abstract (arXiv:2206.07561, about block graphs; it does not address Collins–Shor for trees). I found no prior proof of either half. That is a very small coverage and establishes nothing. I did not search MathSciNet, zbMATH, Google Scholar, or the papers citing AAB. "Theorem T10 very probably known" via AMW is an appropriately cautious, unreviewed claim; I did not check AMW. |
| Unresolved gaps | None in the proofs within the stated scope, given the cited classical results. See the defect list for errors and wording. |

## Reproduction

All code is mine, written in this context from the manuscript's definitions,
in exact rational arithmetic (`fractions.Fraction`) unless labelled
exploratory. The scripts are in the session scratchpad
(`dk.py`, `ids.py`, `chk2.py`, `ds.py`, `merris.py`). They are not committed.
I ran them with `uv run python …` from `d:\conjectura` at revision 8df6bea
(working tree clean apart from an untracked review file of another session).

1. `dk.py N`: computes the characteristic polynomial of D exactly
   (Faddeev–LeVerrier over Q), d_k = (−1)^{n−1}δ_k/2^{n−k−2}, all maximizers,
   and the interval [⌊n/2⌋, ⌈n − n/√5⌉]. ⌈·⌉ is computed exactly by an
   integer comparison 5(n−m)^2 ≤ n^2. Result for orders 2 to 8 (run 1):
   orders 3 to 8 have 0 violations and 0 ties. Order 2 violates, as expected
   (peak 0 < 1). The run for orders 2 to 13 is reported below.
2. `ids.py`: at x ∈ {3/7, 5/2, 1/11}, for all rooted trees of order ≤ 7 (every
   root of every tree), checks exactly:
   - Lemma 5.1 (w = 0, 1, 2);
   - Proposition 5.2(b), (c);
   - Proposition 5.4(a), (b);
   - Proposition 6.1(b), (c), (e);
   - Corollary 5.3(a), (b), with ℓ_T taken from the distance matrix.

   For all pairs of rooted trees of order ≤ 4 it checks Proposition 5.2(d),
   Proposition 5.4(c) and Proposition 6.3. Result: **12,636 checks, 0 failures.**
   (Identities only. Cone memberships were checked by hand, not by LP; scipy is
   not available in the environment.)
3. `chk2.py`: exact checks.
   - (i) d_k(T) ≥ d_k(S_n) for all k, and λ_μ(T) ≥ λ_μ(S_n) for
     1 ≤ μ ≤ ⌊n/2⌋, on all trees of order 3 to 11: 0 failures.
   - (ii) Lemma 6.7 closed forms for 3 ≤ n ≤ 59, the star coefficients against
     the distance matrix for n ≤ 13, and the star's unique peak at ⌊n/2⌋ for
     n ≤ 59: 0 failures.
   - (iii) (C) against the distance matrix for 3 ≤ n ≤ 15: 0 failures.
   - (iv) Lemma 10.1 criterion and the bound p < ξ + 3/5 for P_n,
     3 ≤ n ≤ 399, via (C): 0 failures.
   - (v) Theorem T10 strictly on all trees of order 2 to 10 (exact traces), and
     Lemma 8.7 against a float evaluation of the closed form (exploratory):
     0 failures.
4. `ds.py`: S(9,9) against S_20 at k = 9. The claim of Section 11 item 2 is
   confirmed.
5. `merris.py` (exploratory: float bisection on exact characteristic
   polynomials): the smallest distance eigenvalue against −2/μ_(1). Strict
   inequality ∂_n < −2/μ_(1) occurs already at n = 5, for the spider with
   degree sequence (1,1,1,2,3): ∂_5 ≈ −3.86269, −2/μ_(1) ≈ −3.85501. The same
   holds for its analogues at n = 6, 7, 8.
6. Tree counts (OEIS A000055 values): orders 3..23 total 23,942,357, which
   matches Section 12 item 1. Orders 3..20 total **1,346,022**, which differs
   from Section 12 item 2 (defect 4). A grep in `experiments/` shows
   `results/exhaustive-03-20.json` with `"total_trees": 1346022`. It also
   shows the README's own label "every tree of order 2..20 (1,346,023 trees)"
   for `upper_bound.py`.

7. `dk.py 13` (run 2; exact; all non-isomorphic trees of order 2 to 13,
   2,287 trees): every maximizer lies in [⌊n/2⌋, ⌈n − n/√5⌉] for every order
   3 to 13 (0 violations). Order 2 violates, as stated above. Every d_k is an
   integer. Exactly one tree has a tie, at order 13, which agrees with
   Section 12 item 1 of the manuscript. Over all trees of each order the peak
   lies in {⌊n/2⌋, ⌊n/2⌋+1}. Runs to order 14 exceeded my time limit and were
   killed without output; they are not claimed.

## Verdict

**`no gap found within stated scope`**

Scope:
- The mathematical proofs of the Main Theorem: Theorem 6.6 (lower half),
  Theorem 9.1 (upper half), and their supporting lemmas in Sections 2 to 10.
- Ties are read in the strong sense, for trees of order n ≥ 3.
- The cited classical results (GL), (GP), (LC), (W), (N), (D), (M), (PS), (C),
  (Kr) and Col89 Theorem 1 are taken as correctly stated. I did not read GL78,
  GP71, Col89, Dar64 or Pit97.
- I reconstructed every step of every proof by hand. The R̂_0 algebra of
  Proposition 5.2(c) and some identities were also, or only, confirmed by
  exact computation at rational points.

Not covered:
- The correctness of the cited sources and quotations, in particular the
  verbatim quotation of Col89 Conjecture 9.
- Novelty, beyond a three-query search.
- The Lean development (not re-run).
- The computational claims of Section 12, except where re-done above.
- Comparison with earlier reviews (refused by the environment).

This review applies only to `manuscripts/CJ-0001-collins-shor/main.tex` at
`8df6bea` (blob `50136b05…`). It is an AI review by a model of the same vendor
as the author, not a human or peer review.

### Defects

1. **error** (Remark after Lemma 7.3, lines 1057–1066). The displayed Merris
   chain
   "0 > −2/μ_(n−1) ≥ ∂_2 ≥ −2/μ_(n−2) ≥ … ≥ ∂_n ≥ −2/μ_(1)" is false at its
   last link.
   - The manuscript's own proof of Lemma 7.1 gives ν_2 ∈ [−μ_(1), 0), hence
     ∂_n = 2/ν_2 ≤ −2/μ_(1). The chain should end "… ≥ ∂_{n−1} ≥ −2/μ_(1) ≥ ∂_n".
   - Counterexample (exploratory float, margin about 8·10^{−3}): the spider on
     5 vertices with degrees (1,1,1,2,3) has ∂_5 ≈ −3.8627 < −2/μ_(1) ≈ −3.8550.
   - The remark is not used in any proof. It attributes a misstated inequality
     to Merris.
2. **error** (proof of Lemma 2.3, "only if" direction, lines 286–288). The
   sentence "the sequence is non-increasing from j−1 on and j−1 is a maximizing
   index" is false.
   - The positive log-concave sequence (1, 2, 1, 1/2) with j = 3 has
     a_2 ≥ a_3, but its only maximizing index is 1.
   - The conclusion of that direction (some maximizing index is < j) is still
     true, since the maximum over indices ≥ j−1 is a_{j−1}.
   - Only the "if" direction is used, in Theorem 6.6(c). The lemma is listed as
     formalized "in its general form" (Section 13); I did not check the Lean
     statement.
3. **wording** (statement domain; lines 116–128 and 140).
   - Conjecture 1.2 is quoted as being about "any tree T with n vertices". The
     text then says "Together with [AAB, Theorem 2.1] this is
     Conjecture 1.2", while the Main Theorem assumes n ≥ 3.
   - The restriction is the source's standing convention ("the order of a
     graph is assumed to be at least three"). The manuscript does not say so,
     and does not note that at n = 2 the floor reading is false (peak 0 < 1).
   - AGENTS.md §1.3 requires the domain to be spelled out.
4. **wording / bookkeeping** (Section 12 item 2, line 1596). "1,346,023 trees
   of order 3 to 20" is inconsistent.
   - The number of trees of orders 3 to 20 is 1,346,022 (A000055, and the
     project's own `exhaustive-03-20.json`). 1,346,023 is the count for
     orders 2 to 20.
   - Either the range or the count is wrong. I did not check which by running
     `leaf_telescoping.py`.
5. **wording / citation** (abstract line 52; Introduction lines 104–105). "Graham
   and Lovász asked where this sequence peaks" understates the source.
   - GL78, as quoted in AAB, wrote that the sequence appears to be unimodal
     with maximum at k = ⌊n/2⌋. That is a conjectured location, which Collins
     disproved.
   - The manuscript should say they conjectured the peak at ⌊n/2⌋.
6. **wording** (Main Theorem lines 136–137; Remark 6.8). The attainment of the
   lower bound by the star "for every n ≥ 3" is asserted in the Main Theorem.
   The document does not prove it: it cites Col89 Theorem 1 and says the
   computation is "not reproduced here".
   - The missing step is two lines. Write λ_{m+1}(ℓ_{S_n}) as
     (n−1)[C(N,m+1) − C(N,m)] + 4(n−2)[C(N,m) − C(N,m−1)] − 4[C(N,m−1) − C(N,m−2)],
     with N = n−2 and m = ⌊n/2⌋.
   - Each bracket has a fixed sign by the symmetry of C(N,·) about N/2. This
     gives λ_{m+1} < 0 for n ≥ 4; n = 3 is trivial.
   - I verified this exactly for n ≤ 59. As written, a claim of the Main
     Theorem rests on a citation and a finite check instead of the text.
7. **citation (not a defect found; coverage note)**. I did not check against
   their sources:
   - the verbatim quotation of Col89 Conjecture 9;
   - the location "[GL78, Lemma 1, p. 66]";
   - "[Col89, Theorem 3 and its proof, p. 31]";
   - "[Pit97, p. 284, eq. (13)]";
   - "[Dar64, Theorem 4]".

   The strong form of Darroch's rule used is consistent with the secondary
   account in arXiv:2408.06477, §5.1.

None of defects 1 to 6 affects the validity of the proofs of Theorem 6.6 or
Theorem 9.1.

## Sources consulted

- arXiv:1507.02341v3, https://arxiv.org/abs/1507.02341 (primary source, read in full via pdftotext).
- arXiv:2408.06477, https://arxiv.org/html/2408.06477v1 (statement of Darroch's rule, §5.1; secondary).
- arXiv:2206.07561, https://arxiv.org/abs/2206.07561 (abstract only; block graphs).
- Web searches (2): "Darroch's rule mode mean … Pitman 1997"; "Collins Shor conjecture peak distance characteristic polynomial tree proof n − n/sqrt5".
