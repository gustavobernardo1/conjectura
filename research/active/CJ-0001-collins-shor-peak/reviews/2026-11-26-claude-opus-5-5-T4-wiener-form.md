# Independent review — CJ-0001 — Lemma S24, Propositions S25, S26, Lemma A, Theorem T4 and its corollary (the Wiener form; peak at least floor((n-1)/2))

- **Reviewer:** `claude-opus-5-5` (Anthropic), acting as adversarial reviewer.
- **Date:** 2026-11-26 (21:51 to about 22:00 UTC; hard budget 14 minutes).
- **Independence:** fresh subagent context. I received the primary statement,
  the path and hash of the claimed proof, and the statement to be registered;
  I did not receive the author's reasoning trail or conclusions. The author's
  model is `claude-fable-5-2`; the reviewer is a different model of the same
  provider (same family of training, so independence is limited to a separate
  context and a different model, not a different provider). All computations
  below use my own script, written in this session; it shares no code with
  `experiments/CJ-0001-collins-shor-peak/*.py` (it uses the libraries
  `networkx` and `python-flint`, which the experiments may also use).
- **Revision reviewed:** commit `b5d9294df21b5ff0af2230ce5403a372483f5060`
  (branch `research`).
  - `research/active/CJ-0001-collins-shor-peak/notes/wiener-form.md`
    sha256 `6fc6fbe330c3e3e0f520a1e0243eea6503bf15abd70080d43d96a4d510789dbb`
    (working copy unmodified relative to the commit).
  - `research/active/CJ-0001-collins-shor-peak/notes/leaf-telescoping.md`
    sha256 `66c64a0f250f2dd0420cce99cdfff3d81de3d1fd8fe0f0446ebd96f8df88d06e`
    (partially reviewed, see below).
  - Dependencies read (statements only, not re-reviewed): `notes/lemmas.md`
    (notation, R1, L1, L2), `notes/gamma-reduction.md` (cones `C_d`, Lemma F
    statement), `notes/skeleton-locality.md` (Lemma C statement).
  - At review time the working tree had uncommitted changes by another
    context to `STATE.md`, `notes/obligations.md`, `research/discoveries.json`
    and an untracked `tests/test_cj0001_wiener_form.py`; none was read or
    reviewed.
- **Material given to the reviewer:** Conjecture 1.2 of arXiv:1507.02341 as
  quoted in the task (normalized coefficients `d_k = 2^{k-(n-2)} |delta_k|`,
  `delta_k` the coefficient of `x^k` in `det(D - xI)`, `0 <= k <= n-2`;
  unimodality and log-concavity are Theorem 2.1 there); the note; the statement
  to be registered (quoted in the findings).

## Statement as read from the primary source

Conjecture 1.2 (Aalipour et al.): for every tree `T` on `n` vertices, the
sequence `d_0, ..., d_{n-2}` is unimodal with peak between `floor(n/2)` and
`ceil(n - n/sqrt 5)`. Hypotheses: `T` a tree, `n` its order (implicitly
`n >= 3` so that the sequence has at least two terms). Quantifier: for all
trees of all orders. Definitions: `D` the distance matrix, `delta_k`,
`d_k` as above. "Peak" with ties: the strong reading (every maximizing index
lies in the interval) is the one the note uses; with R1 and positivity plus
log-concavity it is equivalent, for the lower bound, to
`d_{floor(n/2)-1} < d_{floor(n/2)}`.

Statement to be registered (compared word by word with the note):
(i) for `n >= 2`,
`n^2 l_T(x) = 4 (W - n x) Phi(x) + sum_{u<v} (t_u - t_v)^2 x^{dist(u,v)-1} Pi_uv(x)`,
with `l_T = -2^{-(n-2)} det(2xI - D)`, `Phi = det(I + xL)`,
`Pi_uv = det((I + xL)[Q,Q])`, `Q` the vertices off the `u`-`v` path;
(ii) for `n >= 3`, `mu = floor((n-1)/2)`: `d_{mu-1} < d_mu`, hence every
maximizing index is `>= floor((n-1)/2)`, and for odd `n` it is `>= floor(n/2)`.

This is a statement weaker than the conjectured lower bound for even `n` (by
one) and equal to it for odd `n`; it does not touch the upper bound.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | (i) needs only `T` a tree, `n >= 2`; the proof uses nothing more (positive definiteness of `M = I + xL` for real `x > 0`, which holds because `L` is positive semidefinite). For `n = 2` I checked by hand: `l_T = 1 - 4x^2`, `Phi = 1 + 2x`, `W = 1`, `t_u = t_v`, and `4(1 - 2x)(1 + 2x) = 4 l_T`. (ii) needs `n >= 3` so that `mu >= 1` and `mu <= n-2`; both hold (`n = 3`: `mu = 1 = n-2`). Lemma A(b) needs `W >= 3n`; T4 supplies it for `n >= 5` from `W >= (n-1)^2` and `(n-1)^2 - 3n = n^2 - 5n + 1 >= 1` at `n = 5`; orders 3 and 4 (where `W = 4`; `W = 9, 10` fail `W >= 3n`) are handled separately by L2. |
| Quantifiers | (i) is a polynomial identity for every tree of order `n >= 2`; the proof proves it for every real `x > 0` and concludes by polynomiality, which is valid (both sides are polynomials). (ii) is for every tree of order `n >= 3`. No hidden restriction found. |
| Mathematical definitions | `l_T`, `Phi`, `Pi_uv`, `t`, `W` as in the registered statement; `Pi_uv` uses the Laplacian of `T` (not of `T - P`), which is what Lemma S24 needs (the extra `+1` on the diagonal at `a_K`). The identification "the coefficient of `x^k` in `l_T` is `d_k` for `0 <= k <= n-2`" (note, lines 25-27) depends on the sign fact `(-1)^{n-1} delta_k > 0` (Fact 1.1 of arXiv:1507.02341, Graham-Lovasz) and on Observation 3.1 there; the note asserts it without citation, the citation is in `lemmas.md` lines 14-18. Wording defect, not a mathematical gap; my computation confirms the sign and the identification on the whole tested range. The note's description of `C_d` (half-gamma form, attributed to skeleton-locality.md) differs in form from the definition in gamma-reduction.md (generators with `e + i <= d`, `2e + i >= d`) used in the statement of Lemma F; the two sets coincide by Lemma C (each half-gamma generator satisfies the generator conditions, and Lemma C gives the converse), and both lie in `K_d`, so (K1) holds either way. |
| Boundary cases | `d = 0` in S24 (principal minor; the note says so); `Q` empty (`Pi = 1`, `det M[Q] = 1`, the Schur complement is `M[P]` itself, cofactor argument unchanged); `d = 1` in T4 (generator exponent `e + d - 1 = e >= 0`); `d = n-1` (path endpoints, `Q` empty, `Pi = 1 in K_0`); `mu = 1` (`n = 3, 4`, treated by L2; I recomputed `P_3`: `det(D - yI) = -y^3 + 6y + 4`, `d_0 = 2`, `d_1 = 6`); Lemma A with `a <= 0` (both parts), `a = 1` (`C(i, -1) = 0` agrees with the formula `C(i, a-1)(a-1)/(i-a+2)`), divisions by `a` and `i - a + 2` occur only when `a >= 1` and `i >= 2a`, so both divisors are positive; S26 with `n = 1` and `n = 2` (`Psi = 1`); stars and paths (stars give the smallest margins in my runs). No failing boundary case found. |
| Lemma S24 | Reconstructed. Each component `K` of `T - V(P)` meets `P` in exactly one edge; `M[Q]` is block diagonal with blocks `I + x(L_K + diag e_{a_K})`. The correction term `M[P,Q] M[Q]^{-1} M[Q,P]` has entry `(p_i,p_j)` equal to `x^2 sum_K [a_K ~ p_i][a_K ~ p_j] (M[K]^{-1})_{a_K a_K}`, zero for `i != j`. So `S` is tridiagonal with `-x` off the diagonal. The cofactor for `(S^{-1})_{0d}` is `(-1)^{0+d}` times the minor with row `d`, column `0` deleted; that minor (rows `0..d-1`, columns `1..d`) has entries `S_{r,c}` with `c in {r-1, r, r+1}`, i.e. on and below its diagonal, its diagonal entries being `S_{r,r+1} = -x`; so it is lower triangular with determinant `(-x)^d` and the cofactor is `x^d`. Sign checked. With `det M = det M[Q] det S` this gives `adj(M)_{uv} = x^d det M[Q]`. Cone claim: Lemma F applies to each `K` (`|K| >= 1`, integer weight `e_{a_K}`, not zero); the product rule is stated in gamma-reduction.md ("The cones `C_d`"), not in Lemma C as the note says (citation nit); `sum |K| = n - d - 1`. Independently checked: `det(M) (M^{-1})_{uv} = x^d det M[Q]` at `x = 2, 3, 7` for every ordered pair of every tree of order 2 to 10 (50,262 entries), no failure. No gap. |
| Proposition S25 | Reconstructed every line: `(L delta_c)_v = 2 - k_v` for `v != c`, `= -k_c` at `c`, so `L delta_c = tau - 2 e_c` and `L t = n tau - 2 1`; `delta_c^T L delta_c = n - 1 = delta_c^T tau`, so `t^T tau = n(n-1)`; `t^T L t = n^2(n-1) - 4W`; with `G = M^{-1}`, `G1 = 1`, `xLG = xGL = I - G`, `n^2 x tau^T G tau = t^T L t - (t^T t - t^T G t)/x + 4nx` (the cross term `1^T G L t = 1^T L t = 0`, `1^T G 1 = n`); L1 gives `n^2 l_T / Phi = 4W - 4nx + (t^T t - t^T G t)/x`; symmetry and unit row sums give `t^T t - t^T G t = sum_{u<v} G_uv (t_u - t_v)^2`; S24 converts `Phi G_uv`. The registered statement (i) is exactly S25. Remarks (2) and (3) re-derived (star: `n^2 l = (1+x)^{n-2}[(n-1)n^2 + 4n^2(n-2)x - 4n^2 x^2]`). Independently checked exactly (l_T from the characteristic polynomial of `D`, not from L1; `Pi_uv` from its definition as a determinant) on all 5,450 trees of orders 2 to 14 and on paths, stars, double stars, brooms, caterpillars and a spider of every order 11 to 40 (identity checked at every order in that range). No failure. No gap. |
| Proposition S26 | Reconstructed: cofactor expansion along the leaf row gives `Phi_T = (1+x) det M[V\w] - x^2 Psi`; `M[V\w] = (I + xL_{T'}) + x e_u e_u^T` because `u` loses one degree; linearity in row `u` gives `det M[V\w] = Phi_{T'} + x Psi` with `Psi = det M[V\{w,u}]`, which equals `Pi_uu` of `T'` (degrees of vertices other than `u, w` agree in `T` and `T'`); hence `Phi_T = (1+x)Phi_{T'} + x Psi`; `Psi in K_{n-2}` by S24 for `T'` with `d = 0` (`n' - 1 = n - 2`); (K2) closes the induction. `Phi_T(0) = det I = 1`. No gap. (Cone membership was not tested by machine: it is an LP and I had no time; the proof is complete as written.) |
| Lemma A | Reconstructed both parts, including the binomial conventions. (a): `a <= 0` gives `C(i,a) - C(i,a-1) = C(i,a) >= 0`; `a >= 1` gives `i >= 2a - 1 >= a` and `lambda = C(i,a-1)(i-2a+1)/a >= 0`. (b): for `a >= 1`, `i >= 2a`, `s = i - 2a + 1 >= 1`, `C(i,a) - C(i,a-1) = C(i,a-1) s/a`, `C(i,a-1) - C(i,a-2) = C(i,a-1)(s+2)/(a+s+1)`; with `W >= 3n`, `3s(a+s+1) - a(s+2) = 2a(s-1) + 3s^2 + 3s > 0`. Grid test (exact integers): `mu <= 12`, `e, i <= 30`, `n <= 24`, `W = 3n`: 10,882 cases of (a), none negative; no case of (b) negative or (for `a >= 1`) zero. Sharpness: taking `s = 1` (`i = 2a`) the sign of `lambda` in (b) is that of `W(a+2) - 3na`, so for every `W < 3n` there is a counterexample with `a > 2W/(3n - W)`; the hypothesis is therefore sharp in the limit `a -> infinity`, but the grid with `W = 3n - 1/100, 3n - 1/10, 3n - 1` (n = 10) found none because it does not reach such `a` (consistent with the threshold). Irrelevant for T4, where `W >= (n-1)^2`. No gap. |
| Theorem T4 | Reconstructed. `lambda_mu(l_T) = d_mu - d_{mu-1}` since `mu - 1, mu <= n - 2`. Orders 3, 4 by L2 (`d_1 = 6 > 2`; `d_1 >= 32 - 6 - 12 = 14 > 3`). For `n >= 5`: pair terms: generators `x^{e+d-1}(1+x)^i` with `2(e+d-1) + i >= n + d - 3 >= n - 2 >= 2mu - 1`, so Lemma A(a); main term: `Phi in K_{n-1} subset K_{2mu}` (`2mu <= n-1`), Lemma A(b) per generator; strictness: generators with `e >= 1` vanish at `0` and those with `e = 0` take the value `1`, so `Phi(0) = 1` forces a positive coefficient on some `e = 0` generator, for which `a = mu >= 1`. Linearity of `lambda_mu` over the non-negative combination is correct. Then R1 (general form, `j = mu`, `1 <= mu <= n-2 = r`), using positivity and log-concavity (Theorem 2.1 of the source). Statement (ii) is exactly what the proof proves. Independently: `d_{mu-1} < d_mu`, positivity, log-concavity and "every maximizer `>= mu`" checked exactly on all trees of orders 3 to 14 and on the special families to order 40; smallest margins `d_mu - d_{mu-1}`: 4, 11, 20, 54, 84, 231, 336, 942, 1320, 3762, 5148, 14872 for `n = 3..14`. No gap. |
| Corollary (odd order) | `floor((n-1)/2) = floor(n/2)` for odd `n`; follows from T4. Correct. |
| Honesty about even order | Explicit and correct: lines 13-17 and the section "What is not proved" state that for even `n = 2m` the theorem gives only `d_{m-2} < d_{m-1}` and that the conjectured `d_{m-1} < d_m` is not proved; the registered statement (ii) claims nothing more. The supporting claims in that section are correct: for `d >= 2` the pair terms lie in `K_{n+d-3} subset K_{n-1} = K_{2m-1}`; `lambda_m((1+x)^{2m-2}) = C(2m-2,m) - C(2m-2,m-1) < 0`; for the star only edges have `t_u != t_v`. (In my runs, every tree of even order up to 14 also satisfies the conjectured bound; this is finite evidence consistent with the conjecture, not part of the claim.) |
| Logical implications | S24 -> S25 (via `Phi G_uv = adj_uv`); S24 (`d = 0`) -> S26; S24, S25, S26, Lemma A -> T4 inequality; T4 + R1 + Theorem 2.1 -> maximizer statement; -> corollary. Each implication checked; the cases `n = 3, 4` versus `n >= 5` cover all `n >= 3`. |
| Dependency assumptions | L1 (Graham-Lovasz inverse formula, quoted from memory in lemmas.md, and Graham-Pollak) — not re-proved by me, but my exact check of (i) uses `det(D - yI)` directly and S25 is derived from L1, so L1 is confirmed on my range; L2 (formula from the source); R1 (formalized, general form read and correct); Fact 1.1 and Theorem 2.1 of arXiv:1507.02341 (external, not re-checked; numerically consistent on my range); Lemma F (AI-reviewed earlier; used with an admissible weight); cone product rule (gamma-reduction.md). Only membership in `K_d` is needed for T4, and `K_d` closure properties (K1), (K2) are immediate from the definition, so T4 does not depend on Lemma C beyond the equality of the two descriptions of `C_d` noted above. |
| Counterexample attempts | None found. See Reproduction. |
| Formalization scope | None of these statements is formalized; nothing to check. R1 is formalized (not re-run here; `scripts/verify_lean.py` was not run in this review). |
| Novelty coverage | Not asked to search the literature and did not search. Novelty not assessed. |
| leaf-telescoping.md (partial coverage) | **Covered:** S23(d) — the star formula agrees with my independent derivation from S25 Remark (3) and with my distance-polynomial computations on stars to order 40; the closed forms for `d_m - d_{m-1}` (even `n`, `m >= 3`; odd `n`, `m >= 2`) and positivity were checked exactly for `n = 3..200`, and the factorization `(6m-7)(m+1) - 12(m-1) = (2m-1)(3m-5)` was verified by hand. S27(a) — conditional on (SM), correct: `C_{n-1} subset K_{n-1} subset K_{2m-1}`, Lemma A(a) with `mu = m`, `m <= n - 2`, then R1. S27(b) — reconstructed by hand (leaf `w != c` exists for `j >= 2`; linearity in row `u` gives `Phi(B,e_c) = (1+x)Phi(B-w,e_c) + x Psi`, each component of `B - w - u` has non-zero integer weight; `xC_{j-2} subset C_j`, `(1+x)C_{j-1} subset C_j`), no gap. S27(c) — the algebra (subset expansion of the product, `1 + 4x in C_1`, the telescoped difference) is correct given (Γ_c¹), Lemma F and S23(c). **Not covered:** S23(a), (b), (c) — they use `R(T, nu)`, `Psi_u`, `Omega_u`, Propositions S14 and S15 from `gamma-components.md` and `rooted-calculus.md`, which I did not read; I could not assess them and S27(c) inherits that. |
| Unresolved gaps | None in wiener-form.md. Wording defects only: (1) lines 25-27 assert that the coefficients of `l_T` are `d_0..d_{n-2}` without citing Fact 1.1 / Observation 3.1 (the citation is in lemmas.md); (2) S24 attributes the cone product rule to Lemma C, whereas it is stated in gamma-reduction.md; (3) the description of `C_d` in "Notation" is the half-gamma form while Lemma F's statement uses the generator form of gamma-reduction.md; equal by Lemma C, but the note should say so. |

## Reproduction

Script (mine, not committed):
`C:\Users\bezze\AppData\Local\Temp\claude\150e3719c412ed18\74a5f48a-5de6-4d5c-a1ad-3a8d3a49d2ac\scratchpad\rev_t4.py`
(sha256 `6a52b4839740bd458680593439c4c21b384e1711575340b91f58b42922ed8ba0`).
Trees from `networkx.nonisomorphic_trees`; `det(yI - D)` and `det(yI - L[Q])`
by `flint.fmpz_mat.charpoly` (exact integers); `det(I + xA)` obtained from the
characteristic polynomial of `A` by `[x^j] = (-1)^j c_{m-j}`; `l_T` and `d_k`
as exact rationals. Run from `d:\conjectura` at revision `b5d9294`:

- `uv run python rev_t4.py lemmaA` — Lemma A(a): 10,882 cases, 0 violations;
  (b) at `W = 3n`: 0 violations; `W = 3n - eps` (n = 10, a <= 12): none
  (expected; see the sharpness analysis).
- `uv run python rev_t4.py all 14` — for every tree of order 2 to 14
  (1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159 trees): coefficient
  identification and sign `(-1)^{n-1} delta_k > 0`, identity (i) exactly,
  `d_{mu-1} < d_mu`, log-concavity, all maximizers `>= mu`: all pass.
- `uv run python rev_t4.py special 11 40 24` and `special 25 40 40` — paths,
  stars, all double stars, brooms, four caterpillars, a spider with legs of
  length 2, orders 11 to 40 (19 to 64 trees per order): identity (i) and
  inequality (ii) pass at every order.
- Inline script: S24 adjugate entries at `x = 2, 3, 7`, all trees of order 2
  to 10, 50,262 entries, all equal.
- Inline script: S23(d) closed forms and star inequality, `n = 3..200`, pass.

These checks are finite evidence on the stated ranges only.

## Verdict

`no gap found within stated scope`

Scope: Lemma S24, Proposition S25, Proposition S26, Lemma A, Theorem T4 and
its odd-order corollary in `notes/wiener-form.md` at revision `b5d9294`, and
the registered statement (i)-(ii) as quoted above, which matches what the note
proves. The verdict assumes the cited external facts (Graham-Pollak, the
Graham-Lovasz inverse used in L1, Fact 1.1, Observation 3.1 and Theorem 2.1 of
arXiv:1507.02341) and the earlier reviewed Lemma F and Lemma C, which I did not
re-prove. In `notes/leaf-telescoping.md` only S23(d), S27(a) and S27(b), and the
algebra of S27(c), were assessed (no gap); S23(a)-(c) were not assessed. The
theorem does not prove the conjectured lower bound for even `n` and does not
address the upper bound; the note says so. No literature search was made. This
review applies only to the revision named above; it is an AI review of limited
independence (different model, same provider), not human peer review.
