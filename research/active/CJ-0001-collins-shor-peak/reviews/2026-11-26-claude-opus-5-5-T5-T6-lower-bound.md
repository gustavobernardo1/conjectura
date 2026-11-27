# Independent review — CJ-0001 — Lemma S32, Propositions S33 to S36, Theorems T5 and T6 (`notes/lower-bound.md`), with Proposition S23(a)–(c)

- **Reviewer:** Claude, model identifier `claude-opus-5-5` (AI adversarial reviewer).
- **Date:** 2026-11-26.
- **Independence:** a fresh subagent context, started for this review only. It
  received the task brief (catalogue id, file paths, the headline claim, the
  list of dependencies, instructions) and nothing of the author's reasoning
  trail, journal or session notes. The author of the note is recorded in its
  header as `claude-fable-5-2`. The reviewer is a different model identifier,
  but of the same vendor and model family, so independence is limited to a
  separate context. No earlier review report was opened. Part of `STATE.md`
  (lines 1–120: statement, definitions, status table) was read, as the brief
  instructed; it was used only to locate the statement and the status of
  dependencies.
- **Revision reviewed:** Git commit `74d65b010289e236fc3387b37010290a2d266241`
  (`74d65b0`), branch `research`. Files, SHA-256 of their content at `74d65b0`
  (all checked with `git show 74d65b0:<path> | sha256sum`; they match the
  files read):
  - `research/active/CJ-0001-collins-shor-peak/notes/lower-bound.md`:
    `d149fd5b6d3ac510f07f4aacca7f419dfbdc9d4dfb5d4bdf38719ac2b07c614d` (the object under review)
  - `notes/leaf-telescoping.md`: `66c64a0f250f2dd0420cce99cdfff3d81de3d1fd8fe0f0446ebd96f8df88d06e` (S23(a)–(c) under review)
  - `notes/wiener-form.md`: `f8d0d773da704d1d09b89fbb0ba1914224eba699a6f11cd1a0c01309d5bc707c`
  - `notes/rooted-calculus.md`: `5080ea4888af2498dd8c2db4e8cfa79741cd3768b5752949b774ce830140bc92`
  - `notes/gamma-components.md`: `f2057b1fb60f65be9b073058999a076b5d2505f92e317e5049fdaa574a1d18ee`
  - `notes/lemmas.md`: `a225898814df1ae584d9c58cb2c983d89bcbbd83121458c8058e9bfc4ca03c6e`
  - `notes/gamma-reduction.md`: `49f33f738105a7733a04bb3115274c07d86f7716ea4e3c523a296e4422dff875`
  - `STATE.md`: `9539625cbb755d84c3a4839128bfac0d48d1420c20b0043d7fc743269f1f9310`
- **Material given to the reviewer:** the files above, and the primary source
  arXiv:1507.02341v3. The reviewer opened the source PDF and read pages 1–3.
  During the review, other files appeared in the working tree, uncommitted:
  an untracked `experiments/CJ-0001-collins-shor-peak/lower_bound.py`, an
  untracked `results/lower-bound.json`, an untracked
  `tests/test_cj0001_lower_bound.py`, and modified `STATE.md`, `README.md` and
  dossier. Another context was evidently working on them. They are **not**
  part of the reviewed revision, and the reviewer neither read nor ran them.

## Statement as read from the primary source

The reviewer wrote this section before reading the proof. It was then checked
against arXiv:1507.02341v3, pages 2–3, read by the reviewer.

- `T` is a tree on `n ≥ 3` vertices with distance matrix `D`. `δ_k(T)` is the
  coefficient of `x^k` in `det(D − xI)`. The normalized coefficients are
  `d_k(T) = 2^k |δ_k(T)| / 2^{n−2}` for `0 ≤ k ≤ n − 2`. Fact 1.1 of the source
  gives `(−1)^{n−1} δ_k > 0` for these `k`.
- Conjecture 1.2 (Collins–Shor), verbatim from the source: "The [normalized]
  coefficients of the distance characteristic polynomial for any tree T with
  n vertices are unimodal with peak between ⌊n/2⌋ and ⌈n − n/√5⌉."
- The lower half, in the project's strong reading of ties, says: for every tree
  of order `n ≥ 3`, every index at which `d_0, …, d_{n−2}` attains its maximum
  is `≥ m = ⌊n/2⌋`. The sequence is positive (Fact 1.1) and log-concave. The
  source announces log-concavity as Theorem 2.1. It also follows from Newton's
  inequalities, because `det(D − xI)` is real-rooted and its first `n − 1`
  coefficients have one sign. By the general form of R1, the lower half is
  therefore equivalent to `d_{m−1} < d_m`.
- The claim under review is T6(c): for every tree `T` of order `n ≥ 3`,
  `d_{m−1}(T) < d_m(T)`. It is stated for every tree, with no restriction of
  family, parity or size. It concerns exactly the lower half of Conjecture 1.2
  as defined above. The upper half is not claimed.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | T6(c) assumes only that `T` is a tree with `n ≥ 3`, as the conjecture does. T5 holds for rooted trees of every order `a ≥ 1` with weight zero. T6(a) holds for `n ≥ 1` and T6(b) for `n ≥ 2`. S36 needs a non-pendant edge, that is `a, b ≥ 2`. The formula also holds trivially for `a = 1`, where `T′ = T`. Every weight that the proofs feed into Lemma K is non-zero: `e_c`, `e_{a_{K′}}` and `e_c + e_{a_{K′}}`. Lemma S32 is stated for `ν ≥ 0` with the zero weight allowed. Its proof needs weights only in the blocks `M[Q]`, and those weights are always non-zero. No hidden hypothesis was found. |
| Quantifiers | "For every tree, every vertex" is used correctly. T6(b) needs only *some* construction leaf by leaf, and one exists for every tree. The star uses the construction from its centre. T5 quantifies over every rooted tree, and the induction uses (i)–(iii) for every rooted tree of smaller order. This matches what (i) and (ii) consume: `(A_i, c_i)` with `a_i ≤ a − 1`. |
| Mathematical definitions | `d_k`, `δ_k` and `ℓ_T = −2^{−(n−2)} det(2xI − D)` agree with the source. The coefficient of `x^k` in `ℓ_T` is `d_k` for `k ≤ n−2`, and the top coefficients are `0` and `−4`. This was re-derived by hand and checked by the reviewer's code on every tree of order 3 to 18. `M(T, ν)`, `p`, `N` and `R(T, ν)` agree with `gamma-components.md`. The rooted state `(Ψ, H, G, Ω, R)` and the operations raise, plant and merge agree with `rooted-calculus.md`. `K_d` follows `wiener-form.md` (it includes negative `d`, which the proofs use only on the zero polynomial) and `C_d` follows `gamma-reduction.md`. (K4) was re-proved: a non-negative combination with positive coefficients has degree equal to the largest degree of a generator in it, so every generator has `e + i ≤ d`. |
| Boundary cases | Each case was checked by hand, and by code where noted. `a = 1`: `Ψ = 1`, `H = G = Ω = 0`, `R = −(1+2x)²` (S19(a) with weight 0), `E = 0`, `R(A, e_u) = 0`. `a = 2` (an edge rooted at an end): `Ψ = 1+x`, `H = 1`, `G = 0`, `Ω = 0`, `E = 0`. S35 with `a_i = 1`: both sides equal `xR¹_l`. `q = 1` in S34(d) and T5: `E = E^_1`. A child subtree that is a single vertex: `E^ = 0`, `Ψ^ = 1+x`. Lemma S32 with `v = v′` (`d = 0`) and with `Q = ∅`. T6(a) with `n = 1`: the difference is `0`. T6(b) with `n = 2`: the difference is `0`. T6(c) with `n = 3, 4`: `m = 1, 2` and `1 ≤ m ≤ n−2`. The star value at `m = 2`: `d_2 − d_1 = 1`. S23(a) with `n = 1`: `ℓ = −4x`. The reviewer's code covered all trees of order 3 and 4, all rooted trees of order 1 and 2, and the star at every order up to 18 and at `n = 100`. |
| Lemma S32 | **Verified.** The reviewer re-read the proof of S24 (Schur complement on the path, tridiagonal `S`, the `(0, d)` cofactor equal to `x^d`). It uses only symmetry, positive definiteness for `x > 0`, the entries `−x` on tree edges and `0` elsewhere, and invertibility of `M[Q]`. All of these hold for `I + x(L + diag ν)` with `ν ≥ 0`. The block weights `ν|_{K′} + e_{a_{K′}}` are non-zero, so Lemma K applies, and (K2) gives `K_{j−d−1}`. The first equality was checked entry by entry, by cofactors, on all rooted trees of order ≤ 9 with `ν = 0` (S24). For `M¹` it was checked only through the identity S33(e). The weighted form for other weights was not checked entry by entry. |
| Proposition S33 | **Verified**, every part re-derived by hand. (a): `x^{δ−1}K_{a−δ−1} ⊆ K_{a+δ−3}`. (b): `M1 = 1` gives `Φ = Σ_v adj_{uv}`. (c): `Lδ = τ − 2e_u` (recomputed); `p = 1 + (M−I)δ + 2xe_u`; `π_u = Φ + 2xΨ − xΣδ_v a_v`; `G = xΣ(δ_v−1)a_v`. (d): S32 with `v = v′ = u`. (e): `p = M¹(1+δ) − δ`; `(1+δ)ᵀM¹(1+δ) = Σ(1+δ_v)² + xa`; `R(A,e_u) = Φ¹Σδ² − δᵀadj(M¹)δ`. Substituting the row sums `Σ_{v′}adj_{vv′} + x adj_{vu} = Φ¹` and symmetrizing gives the stated form. The `(v,u)` minors of `M¹` and `M` agree, and `x^d K_{a−d−1} ⊆ K_a` for `d ≥ 1`. On all 749 (tree, root) pairs of order 1 to 9, the identities (b), (c), (e) hold exactly with `adj(M¹)` taken from cofactors. Each of `Ψ, H, G/x, Q¹, a_v` lies in the stated `C` cone. |
| Proposition S34 | **Verified.** (a): S19(b) with `ν_u = 0`. (b): every term of the expansion was recomputed, and the coefficient of `H` is `3x² + 2x³`. (c): S19(d) with both root weights zero; the term `(1+2x)²Ψ_1Ψ_2` is split once into each bracket. (d): the induction on `q` was re-done, and the bookkeeping of `P_i`, `P_{il}` is correct. The reviewer's code checked, from the matrices: (a) and (b), including `Ψ^, H^, G^, Ω^`, on all 749 rooted pairs of order ≤ 9; and (c) on all 1,878 ordered pairs of rooted trees with total order ≤ 9, using the state of the merged tree computed directly. |
| Proposition S35 | **Verified.** `G^_i = x²J_i` with `J_i = Σδ_v a_v`, and `R¹_i = Q¹_i + x²W_i`. The bracket `H_1W_2 + H_2W_1 − 2J_1J_2 = Σ a_v a_{v′}(δ_v − δ_{v′})²` was re-derived. The cone degrees were recounted: `2+(a_1−1)+(a_2+1)`, `4+(a_1−2)+a_2` and `8+(a_1−2)+(a_2−2)`, all `≥ a_1+a_2+2`. The case `a_i = 1` was checked. The identity and the membership of the left side in `C_{a_1+a_2+2}` hold on all 1,878 ordered pairs with `a_1 + a_2 ≤ 9`; the hatted states were computed from the matrices of the planted trees. |
| Theorem T5 | **Verified.** The induction is on `a`. The base case `a = 1` is correct. For `a ≥ 2` it uses (i)–(iii) only for the subtrees `(A_i, c_i)`, with `a_i ≤ a−1`, so it is well-founded. S33, S34 and S35 are used unconditionally or with hypotheses supplied by (iii) on smaller trees. Levels recounted: (i) `(a_i+1) + Σ_{l≠i} a_l = a`; `E^_i ∈ K_{a_i+2}`, because each of `xE_i ∈ K_{a_i+3}`, `xΩ_i ∈ K_{a_i+2}`, `2x²(G_i/x) ∈ K_{a_i+3}`, `3x²H_i ∈ K_{a_i+2}` and `2x³H_i ∈ K_{a_i+4}` is in it; `E^_iP_i ∈ K_{a+1}` and `X_{il}P_{il} ∈ K_{a+1}`; (iii) `(1+x)Ω ∈ K_{a+1}` and `x(1+x)H ∈ K_{(a−2)+3}`. The degree bound `deg R(A,e_u) ≤ a+1` is correct, so (K4) gives `C_{a+1}`. The reviewer checked by code that `Ω ∈ C_a`, `E ∈ C_{a+1}` and `R(A, e_u) ∈ C_{a+1}` on all 749 rooted pairs of order ≤ 9. Every claimed membership has degree at most its level, so for these polynomials `K` membership and `C` membership coincide. The `C` test is the unique half-gamma expansion, which decides `C_d` membership. |
| Theorem T6 | **Verified.** (a): the claim `Φ(B,e_c) − (1+x)^j ∈ K_j` was re-proved through (K3) (here `ν′ = e_c ≠ 0`, so the use is inside the proven setting of Lemma K) and S32 with `d = 1`. The product expansion is correct. `(1+4x) = (1+x) + 3x` gives `K_n`, and `Ω ∈ K_n` is T5(i). (b): subtracting the two telescoped sums is correct; each term lies in `(1+x)^{n−1−k}K_k ⊆ K_{n−1}`; the top two coefficients agree; (K4) applies. (c): `K_{n−1} ⊆ K_{2m−1}`; Lemma A(a), re-proved by the reviewer, gives `λ_m ≥ 0` on generators; for `n ≥ 3`, `λ_m(ℓ) = d_m − d_{m−1}`; the star value is S23(d), whose arithmetic was recomputed for both parities (`(6m−7)(m+1) − 12(m−1) = (2m−1)(3m−5)` and `2(2m−1)(m+2) − 4(m−1) = 4m² + 2m`); R1 then applies. Remark 3 (the Catalan form) was checked by hand. |
| Proposition S36 | **Verified.** The whole computation was redone by hand: `Φ_T − (1+x)Φ_Z − xΨψ = x²Hh`, the expansion of `R_T − (1+x)R_Z`, the cancellations, `(1+x) + (1+4x) = 2 + 5x`, and the regrouping into `xHε + xhE`. The cone levels `K_{n−1}` and `K_n` were recounted. The formula was checked exactly against distance-matrix differences on all 1,227 ordered pairs with `a, b ≥ 2` and `a + b ≤ 9`, and on four explicit larger pairs of total order 14, 14, 15 and 16. A wrong coefficient (`2 + 4x`) fails, as a negative control. `ℓ_T − ℓ_{T′} ∈ C_{n−1}` holds for every tree of order 4 to 16 and every non-pendant edge: 220,181 (tree, edge) pairs, the same count as the note. It also holds on up to three sampled non-pendant edges of each large tree listed below. |
| Proposition S23(a)–(c) (`leaf-telescoping.md`, never reviewed before) | **Verified**, together with what it cites. (a): `M1 = 1`, `1ᵀτ = 2`, then L1; the case `n = 1` was checked by hand. (b): S15 for the leaf of weight 0 was **re-derived by the reviewer**, line by line from Lemma G2, including `Σ(N_i + j_i − 1) = N − ν_u + j − 2`. It holds also when `T` is a single vertex. The expansion `Φ_{T⁺} = (1+x)Φ_T + xΨ_u` was re-derived. (c): the telescoping was checked by induction. By code, independently of L1: (a) holds with `ℓ` taken from the characteristic polynomial of the distance matrix and `R(T,0)` from the Laplacian determinants, and (b) holds with both sides from the distance matrices, on all 749 rooted pairs of order 1 to 9. Also `ℓ_{T+leaf at u} − (1+x)ℓ_T − (1+4x)(1+x)^{n−1} ∈ C_n` (T6(a) read through S23(b)) holds for every vertex of every tree of order 3 to 14: 72,142 (tree, vertex) pairs. One citation defect is below (L1 used for `n = 2`). Lemma G2 itself was not re-derived; it was reviewed earlier at `b0a4dbe`. |
| Logical implications | T5(i) needs T5(iii) on smaller trees; T6(a) needs T5(i) and Lemma K; T6(b) needs T6(a) and S23(c),(d); T6(c) needs T6(b), Lemma A(a), S23(d) and R1, with positivity and log-concavity taken from Fact 1.1 and Theorem 2.1 of the source (the latter also follows from Newton's inequalities). Every arrow was checked. No implication uses an unproved statement of the open chain ((SM), (Γ_c¹), Γ_c, (E), (Λ)). T5 *proves* (Γ_c¹), and T6(b) *proves* (SM). The proofs use the cones `K_d`, Lemma K and (K4); they need neither Lemma F nor Lemma C. |
| Dependency assumptions | Re-derived by the reviewer in this review: Lemma K, Lemma S24 (the cofactor step), Lemma A(a), R1 (general form), S15, S23(a)–(d), and L1 at `n = 2`. Used with their earlier review status and checked here only through their consequences, by computation: S19(b),(c),(d) (reviewed at `59c47f7`), Lemma G2 (reviewed at `b0a4dbe`), and L1 for `n ≥ 3` (known: Graham–Lovász and Graham–Pollak, as quoted in `lemmas.md`). External: Fact 1.1 and Theorem 2.1 of arXiv:1507.02341. The reviewer read the definitions and Fact 1.1 on page 2 of the source, but not the proof of Theorem 2.1. |
| Counterexample attempts | None found. Reviewer's own code, exact integer arithmetic (python-flint `fmpz_mat.charpoly`, Bareiss determinants over `Z[x]`, an exact half-gamma decomposition); no project module was imported. **All trees of order 3 to 18** (205,002 trees): T6(c) (`d_{m−1} < d_m`, and the gap at least that of the star, with equality only for the star), T6(b) (`d_k(T) ≥ d_k(S_n)` for all `k`, and `ℓ_T − ℓ_{S_n} ∈ C_{n−1}`), and the sign convention: 0 failures. T6(a) through distance matrices for every vertex of every tree of order 3 to 14: 0 failures. S36 cone for orders 4 to 16: 0 failures. **Large and extreme trees**, all passing T6(b) (coefficients and cone), T6(c) (strict, and at least the star's gap) and the sampled S36 cone: paths `P_50, P_100, P_101, P_150, P_200`; the star `S_100`; brooms `(50,50), (10,90), (90,10), (3,97)` at `n = 100`; spiders with legs of length 2: `2^50` (`n = 101`) and `2^60` (`n = 121`); the same with one pendant at the centre: `2^49+1` (`n = 100`, the S31 family) and `2^60+1` (`n = 122`); spiders `3^33` (`n = 100`) and `3^33+1+1` (`n = 102`); double stars `S(49,49), S(1,97), S(30,69)`; caterpillars `cat(20,4)` and `comb(50)` (`n = 100`); the complete binary tree of depth 6 (`n = 127`); and 15 random Prüfer trees (`n = 100, 120, 150`, seed 20261126). The smallest ratio `d_m/d_{m−1}` was `1.0048` (spider `2^60+1`), printed in floating point for display only. |
| Formalization scope | No Lean formalization is claimed for this note. The reviewer did not run `scripts/verify_lean.py`. Lemma A(a), the cones and the general form of R1 are formalized according to `STATE.md`; that formalization is not relied on here, because each of them was re-proved by hand. |
| Novelty coverage | Not assessed. The note makes no novelty claim, and the brief excluded an originality assessment. The reviewer made no literature search. The only observation is that the source (arXiv:1507.02341v3, page 3) proves only a lower bound `n/(d+1)` (`d` the diameter) on the peak, so the lower bound `⌊n/2⌋` for all trees was not established in that source. Whether it has been resolved since is unknown to this review. |
| Unresolved gaps | None found within the scope below. |

### Defects (not gaps)

1. **Missing artifact at the reviewed revision.** The section "Exact checks"
   says the stored version is `experiments/CJ-0001-collins-shor-peak/lower_bound.py`
   and refers to "its entry in the experiments README". At `74d65b0` neither
   exists: `git show 74d65b0:experiments/CJ-0001-collins-shor-peak/lower_bound.py`
   fails, and the README has no such entry. The counts are therefore not
   reproducible from the repository at this revision. (During the review, HEAD moved to `4ad6c92` and then to `f2a46c8`. The
   commit message of `f2a46c8` says it adds `lower_bound.py`, its test and
   the README entry. `git diff 74d65b0 f2a46c8` shows no change in `notes/`.
   The reviewer did not examine those commits, so this defect may be
   resolved there; this report does not cover that.) The reviewer independently reproduced
   two of the counts: 486 rooted trees of order 1 to 9, and 220,181
   (tree, non-pendant edge) pairs of order 4 to 16. The proofs do not depend on
   these checks.
2. **Citation range of L1.** S23(a) in `leaf-telescoping.md` applies L1 for
   every `n ≥ 2`. `lemmas.md` states L1 under the notation "a tree of order
   `n ≥ 3`". L1 does hold for `n = 2`: the reviewer checked by hand that both
   sides equal `1 − 4x²`, and that Graham–Pollak and the inverse formula hold
   at `n = 2`. The reviewer's code also confirms S23(a) at `n = 2` from the
   distance matrix. The defect is the citation, not the mathematics.
3. **Remark 1 after S36 asserts without proof** that `Hε` and `hE` are
   divisible by `x²`. That requires `E ≡ 0 (mod x²)`, which the note does not
   argue. It is true: `R(A, e_u)(0) = 0` and `Ω(0) = 0` follow from S33(e),
   then `E(0) = 0` follows from S34(a), and S34(b),(d) and S35 give the factor
   `x²` by induction. The reviewer also checked the coefficient
   `[x]form = 2k_A(u)k_B(v)` on all 1,227 pairs. The remark is correct but
   unproved in the note.
4. **Notation clashes**, wording only:
   - `E = E(A, u)` of S34 is not the polynomial `E` of Corollary S17 and
     S20(b) in `rooted-calculus.md` (the increment
     `R(T^, ν+e_r) − R(T^, ν)`), although the notes share notation.
   - `ρ` denotes `R` of `(B, v)` in S36, but also `ρ_k = d_{k+1}/d_k` in
     `STATE.md` and the half-gamma coefficients.
   - `a` denotes `|A|`, the polynomials `a_v`, and the vertices `a_{K′}`.
   - `M` denotes the matrix here and the upper bound `⌈n − n/√5⌉` in
     `STATE.md`.
   - `Q` denotes a vertex set and `Q¹` a polynomial.
   - "S19(a) with `n = 0`" uses `n` for a weight in a note where `n` is the
     order.
5. **Status sentence in the list of results used.** The bullet on S23 says
   "(a) to (c) not reviewed". This is accurate at `74d65b0`, but after this
   review it will be out of date. It should be updated only together with the
   registry, and not taken as a statement about this report.

## Reproduction

Scripts written by the reviewer in the session scratch directory, outside the
repository (not durable). They use exact integers only and do not import any
project module:

- `rev_common.py` (`7302209b2260bbd0630ecf3b09f9c66e8afb38d583a5679c814d4dee2178f2ac`): BFS distance matrix, `fmpz_mat.charpoly`, `2^{n−2}ℓ_T = −det(2xI − D)`, `s_k = 2^k|δ_k|` computed from the definition, and the exact half-gamma test for `C_d`. Negative controls: `(1+x)³ ∉ C_4`, `1 + x + x² ∉ C_2`, `2 + 5x + x² ∉ C_2`, and `λ_5((1+x)^8) = −14`.
- `partA.py` (`a88534ed9fb0fc93b580ce90a3fe808eec34866231b1082089dd3226234f3dd2`). Command: `uv run python partA.py 18 14 16` from the repository root. Result: for every order 3 to 18, `c_fail = cstar_fail = b_coef_fail = b_cone_fail = sign_fail = 0` and `eq_star = 1`. Tree counts: 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741, 19320, 48629, 123867. T6(a): 72,142 (tree, vertex) checks, 0 failures. S36 cone: 220,181 checks, 0 failures. Run time 164 s.
- `partB.py` (`4d882b11b7297572571cad4aec0491c4c34809d4731e3dc70eca8df816bdc31c`). Command: `uv run python partB.py 9 9`. Result: 749 rooted pairs, 1,878 pairs, 1,227 S36 pairs, 0 failures. It covers S23(a), S23(b), S24 by cofactors, S33(b),(c),(e), S34(a),(b),(c), S35 (identity and cone), S36 (formula and Remark 1), and the cones of `Ω, E, R(A,e_u), Ψ, H, G/x, Q¹, a_v`.
- `partC.py` (`f69ac3cbdac6b925bd573957d8444095f1bb04b6aaf6d96375a973b00bded64a`). Command: `uv run python partC.py`. Result: the large and extreme trees listed above all pass ("bad: []"), and the S36 formula matches on the four explicit pairs. Negative control: the coefficient `2 + 4x` in place of `2 + 5x` fails.

Environment: python-flint 0.9.0, networkx 3.7 (used only for
`nonisomorphic_trees`), run through `uv run` in the repository environment on
Windows. This is finite evidence; the verdict rests on the reconstruction of
the written proofs.

## Verdict

`no gap found within stated scope`

Scope: revision `74d65b0`, the file `notes/lower-bound.md` (SHA-256 above), in
full. This covers Lemma S32, Propositions S33 to S36, Theorems T5 and T6, and
their remarks. It also covers Proposition S23(a)–(c) of
`notes/leaf-telescoping.md` at the same revision, and S23(d) as used. Every
step of these proofs was reconstructed by the reviewer. Within this scope the
claim T6(c) holds: for every tree of order `n ≥ 3`, `d_{m−1} < d_m` with
`m = ⌊n/2⌋`, so every maximizing index is `≥ ⌊n/2⌋`. This is the lower half
of Conjecture 1.2 of arXiv:1507.02341 in the strong reading of ties.

The verdict rests on the following, which this review did not re-derive:

- S19(b),(c),(d) and Lemma G2, as reviewed earlier. Only their consequences
  used here were checked, by exact computation, up to order 9.
- L1 for `n ≥ 3`, a classical formula.
- Fact 1.1 and Theorem 2.1 of the source.

The review does not cover:

- the upper half of the conjecture;
- Proposition S30 and statement (SM⁺), which Remark 2 of T6 mentions;
- any Lean statement;
- novelty;
- the uncommitted files that appeared in the working tree during the review.

This is an AI review by one fresh context of the same model family as the
author. It is not a human review. It applies only to the revision named above.
