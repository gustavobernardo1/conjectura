# Independent review — CJ-0001 — MD-0016: the Wiener form and Theorem T4 (complete proof audit)

- **Reviewer:** `claude-opus-5-5` (Claude Opus 5.5), acting as adversarial reviewer.
- **Date:** 2026-11-26 (wall clock 22:51–23:05 UTC, budget 14 minutes).
- **Independence:** fresh subagent context. I did not read `journal.md`,
  `STATE.md`, any earlier review under `reviews/`, or the project script
  `experiments/CJ-0001-collins-shor-peak/wiener_form.py`. The author model is
  `claude-fable-5-2`; I am a different model of the same vendor. My own code was
  written in a scratch directory outside the repository. Limitation: the task
  message from the Research Director named the claims to check and listed the
  dependencies the revision says it uses; no reasoning or conclusion was given.
- **Revision reviewed:** commit `a3e5179595c41b38cbca5234a92685a0cc15c1fb`
  (branch `research`, confirmed with `git log -1`; the two files below are
  unmodified in the working tree, whose only changes are in `formalization/`).
  - [`../notes/wiener-form.md`](../notes/wiener-form.md), SHA-256
    `f8d0d773da704d1d09b89fbb0ba1914224eba699a6f11cd1a0c01309d5bc707c` (recomputed, matches).
  - [`../notes/lemmas.md`](../notes/lemmas.md), SHA-256
    `a225898814df1ae584d9c58cb2c983d89bcbbd83121458c8058e9bfc4ca03c6e` (recomputed, matches).
- **Material given to the reviewer:** the two notes above, the record MD-0016 in
  `research/discoveries.json`, the reference to arXiv:1507.02341.

## Statement as read from the primary source

Read from the arXiv PDF of 1507.02341v3 (pages 1–3; fetched 2026-11-26). For a
graph `G` of order `n`, `δ_k(G)` is the coefficient of `x^k` in
`det(D(G) − xI)`; for `0 ≤ k ≤ n−2`, `d_k(G) = 2^k |δ_k(G)| / 2^{n−2}` (the
normalized coefficients). Fact 1.1 (Graham–Lovász, eq. (44)): for a tree on `n`
vertices, `(−1)^{n−1} δ_k(T) > 0` for `0 ≤ k ≤ n−2`. Conjecture 1.2
(Collins–Shor): the normalized coefficients of any tree `T` with `n` vertices
are unimodal with peak between `⌊n/2⌋` and `⌈n − n/√5⌉`. Page 3 states that
Theorem 2.1 shows `d_0(T), …, d_{n−2}(T)` log-concave and unimodal; I read this
sentence, **not the statement of Theorem 2.1 itself**, and I did **not** read
Observation 3.1 (I re-derived the identification it is cited for; see below).
The source assumes order at least three throughout.

Claim checked (MD-0016 as registered): (i) for every tree of order `n ≥ 2`,
`n² ℓ_T = 4(W − nx)Φ + Σ_{u<v} (t_u − t_v)² x^{dist(u,v)−1} Π_{uv}`; (ii) for
`n ≥ 3` and `μ = ⌊(n−1)/2⌋`, `d_{μ−1} < d_μ`, so every maximizing index is at
least `⌊(n−1)/2⌋`, hence at least `⌊n/2⌋` for odd `n`. This is a statement
about the source's `d_k`, and for odd `n` it is the lower half of Conjecture 1.2
with ties read strictly. It is weaker than the conjecture's lower bound for even
`n`, and the note says so.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | Trees, `n ≥ 2` for (i), `n ≥ 3` for (ii). The definition of `d_k` in MD-0016 matches the source exactly (checked on page 2 of the PDF). No hidden hypothesis found. |
| Quantifiers | "For every tree", "every maximizing index": these match. The tie convention is strict: every maximizing index, not just some, is `≥ μ`, as R1 gives. |
| Mathematical definitions | `ℓ_T = −2^{−(n−2)} det(2xI − D)`. Re-derived: `[x^k] ℓ_T = 2^{k−(n−2)} (−1)^{n−1} δ_k`, because `det(yI − D) = (−1)^n det(D − yI)`; with Fact 1.1 this is `d_k`. The coefficient of `x^{n−1}` is 0 (zero trace) and the coefficient of `x^n` is −4. `K_d`, `Φ(K, ν)`, `Π_{uv}` and `λ_μ` are defined unambiguously. |
| Boundary cases | `n = 2`: (i) holds (`ℓ = 1 − 4x²`, `W = 1`, `t_u = t_v`); checked by hand and by computer. But see defect D3. `n = 3, 4`: L2 gives `d_1 = 6 > 2`, and `d_1 ≥ 14 > 3` from `Σ k² ≤ 12`; checked. `n = 5, 6`: `W ≥ (n−1)² ≥ 3n` needs the edge formula for `W`, because `C(n,2) < 3n` there (D2). `n = 5`: `16 ≥ 15`. Path, `Q = ∅` for the end vertices: S24 gives `adj_{uv} = x^{n−1}`, with `S = M`. Checked by hand and in all path cases computed. Lemma K: `j = 1` and `j = 2` (`Ψ = 1`) checked. Lemma A: `a ≤ 0` and `a = 1` (`C(i, −1) = 0`) checked. |
| Lemma K | **Re-proved.** Choice of leaf: a tree with `j ≥ 2` has two leaves, and if `ν` restricted to `U∖w₁` is zero then `ν` restricted to `U∖w₂` is not. Row expansion at a leaf: `det N = N_ww det N[U∖w] − N_wu N_uw Ψ`. `N[U∖w] = I + x(L_{K−w} + diag ν′) + x e_u e_uᵀ`, and linearity in row `u` gives `A + xΨ`. The minor of the `u`-row term is `Ψ`, because the degrees of vertices other than `u, w` are unchanged. (K3) by expansion: `(1+x+ν_w x)(A+xΨ) − x²Ψ`. Blocks of `N[U∖{w,u}]`: each component of `K − w − u` holds exactly one neighbour `a′` of `u`, whose `K`-degree is its `K′`-degree plus 1. The induction hypothesis is applied only to non-zero weights (`ν′`, `ν|K′ + e_{a′}`, `ν′ + e_u`). The induction is strong induction (blocks of order `≤ j − 2`); the text says "Induction on `j`" (D5, wording). |
| (K1), (K2) | Re-proved from the generators: `2e+i` is additive under products, rises by 1 under `(1+x)·` and by 2 under `x·`, and `K_{d+1} ⊆ K_d` is immediate. (K1) holds for both descriptions of `C_d`. |
| Lemma S24 | **Re-proved** for real `x > 0`, then extended as a polynomial identity. Each component of `T − V(P)` has exactly one edge to `P`, so `M[Q]` is block diagonal. The `(p_i, p_j)` entry of `M[P,Q] M[Q]^{−1} M[Q,P]` is `x² Σ_K [a_K∼p_i][a_K∼p_j] (M[K]^{−1})_{a_K a_K}`, which is diagonal. `S` is tridiagonal with off-diagonal `−x`. Cofactor `C_{d0}(S)`: the submatrix (rows `0..d−1`, columns `1..d`) is lower triangular with diagonal `S_{r,r+1} = −x`, so `C_{d0} = (−1)^d(−x)^d = x^d`. Then `adj_{uv} = det M · x^d / det S = x^d det M[Q]`. `d = 0` and `Q = ∅` checked. Cone part: membership in `K_{n−d−1}` follows from Lemma K and (K2). The `C_{n−d−1}` part of the statement rests on Lemma F and the product rule for `C_d` from another note, which the note discloses (D4); T4 does not use it. |
| Proposition S25 | **Re-proved line by line.** `(Lδ_c)_v = k_v r − (r−1) − (k_v−1)(r+1) = 2 − k_v` for `v ≠ c`, and `−k_c` at `c`, so `Lδ_c = τ − 2e_c` and `Lt = nτ − 2·1`. `δ_cᵀLδ_c = n−1`, since every edge changes the distance by exactly 1. So `δ_cᵀτ = n − 1`, `tᵀτ = n(n−1)` and `tᵀLt = n²(n−1) − 4W`. `n² xτᵀGτ = x tᵀLGLt + 4x·1ᵀGLt + 4x·1ᵀG1`, where `1ᵀGLt = 0`, `1ᵀG1 = n` and `x tᵀLGLt = tᵀLt − (tᵀt − tᵀGt)/x`. With L1 this gives `n²ℓ/Φ = 4W − 4nx + (tᵀt − tᵀGt)/x`, and the row sums give `tᵀt − tᵀGt = Σ_{u<v} G_{uv}(t_u−t_v)²`. Then `Φ G_{uv} = adj_{uv}` and S24. Every sign agrees. Remarks (2) and (3) re-derived (`n = 3`: `ℓ = 2 + 6x − 4x³`). |
| Proposition S26 | **Re-proved:** `Φ_T = (1+x)Φ_{T′} + xΨ` is (K3) with `ν = 0`, and the row expansion is valid for any `ν ≥ 0`. `Ψ = det M[V∖{w,u}]` equals `Π_{uu}` of `T′`, because degrees off `{u, w}` are unchanged, so `Ψ ∈ K_{n−2}` by S24 (`d = 0`). `n = 1, 2` checked. The proof cites "the expansion in the proof of Lemma F" (D1). |
| Lemma A | **Re-proved.** `[x^μ]g = C(i,a)`, `[x^{μ−1}]g = C(i,a−1)`, `[x^{μ−1}](xg) = C(i,a−2)`. (a): for `a ≤ 0`, `λ = C(i,a) ≥ 0`; for `a ≥ 1`, `λ = C(i,a−1)(i−2a+1)/a ≥ 0`. (b): `s = i−2a+1 ≥ 1` and `i−a+2 = a+s+1`; `C(i,a−2) = C(i,a−1)(a−1)/(i−a+2)` holds also for `a = 1`. The numerator satisfies `Ws(a+s+1) − na(s+2) ≥ n[2a(s−1) + 3s(s+1)] > 0`. |
| Theorem T4 | **Re-proved.** `1 ≤ μ ≤ n−2` for `n ≥ 3`. Orders 3 and 4 via L2. For `n ≥ 5`: `W ≥ (n−1)² ≥ 3n`. Pair terms: `x^{d−1}Π_{uv}` is a combination of `x^{e+d−1}(1+x)^i` with `2(e+d−1)+i ≥ n+d−3 ≥ n−2 ≥ 2μ−1`, and Lemma A(a) applies. Main term: `Φ ∈ K_{n−1} ⊆ K_{2μ}` and Lemma A(b) applies. `Φ(0) = 1` forces some generator with `e = 0` and a positive coefficient in any representation, and `a = μ ≥ 1` makes it strict. R1 (general form, `r = n−2`, `j = μ`) gives the consequence. |
| Corollary (odd order) | For `n = 2m+1`, `⌊(n−1)/2⌋ = m = ⌊n/2⌋`. Correct. |
| Even order / "What is not proved" | Honest: the note states that for even `n` only `m − 1` is obtained and that the conjectured `⌊n/2⌋` is not proved. Inequality (3) is not part of MD-0016. I checked its pair-term argument for `d ≥ 2` and that `λ_m((1+x)^{2m−2}) < 0`, which holds. |
| Logical implications | Every implication S24 → S25, (K2)+Lemma K → S24 cone → T4 pair terms, S26 → T4 main term, Lemma A → both, T4 → R1 → consequence was checked. Cases covered: `n = 3, 4` separately and `n ≥ 5` uniformly. No uncovered case. |
| Dependency assumptions | The claim was "self-contained except (i)–(iii)". Places that use something outside the note and outside (i)–(iii): **D1** S26 cites "the expansion in the proof of Lemma F", and the list "Used from earlier notes" still lists Lemma F with that expansion. The expansion is a one-line row expansion, reproduced in Lemma K's proof, so this is a citation defect, not a gap. **D2** T4 uses `W = Σ_e n_e(n − n_e)` (Wiener's edge formula), which the note does not prove and which is not in (i)–(iii). It is classical: each pair is counted once for each edge of its path. It is needed for `n = 5, 6`. Unlisted, not a gap. **D3** S25, and so MD-0016 (i), is claimed for `n ≥ 2`, but L1 in `lemmas.md` is stated under "Notation" for `n ≥ 3`. The proof of L1 works verbatim at `n = 2`: I checked both classical formulas for `n = 2`, and `n = 2` was verified exactly. This is a scope-citation defect. **D4** The `C_{n−d−1}` clause of S24 depends on Lemma F and the product rule for `C_d`, as disclosed. Standard linear algebra is also used: Schur complements, the matrix determinant lemma, the cofactor formula for the inverse, block determinants, and the fact that a tree has two leaves. |
| L1 (lemmas.md) | **Re-proved** from Graham–Pollak and Graham–Lovász. The steps are `det(2xI − D) = det D · det(2xD^{−1} − I)`, `2xD^{−1} − I = −(I+xL) + (x/(n−1))ττᵀ`, the matrix determinant lemma, and `adj(−B) = (−1)^{n−1}adj B`. The signs give exactly `ℓ = (n−1)Φ − xτᵀadjτ`. I also **re-proved Graham–Lovász's inverse** from S25's identity (1): `LD = τ1ᵀ − 2I` and `Dτ = (n−1)1` give `D(−L/2 + ττᵀ/(2(n−1))) = I`. **Graham–Pollak's determinant was not re-proved**, only checked numerically: the exact identity L1 at integer points, and Fact 1.1's sign on all trees up to order 16. |
| L2 (lemmas.md) | **Re-proved:** `[x]` of L1 is `(n−1)·2(n−1) − τᵀτ`, with `τᵀτ = 4n − 8(n−1) + Σk²`. `d_0 = n−1`. |
| R1 (lemmas.md) | **Re-proved** for the general form, only the "if" direction needed. Ratios are non-increasing, `a_{j−1} < a_j` makes every earlier ratio `> 1`, and so no index `< j` is maximizing. It relies on Theorem 2.1 of the source for log-concavity and on Fact 1.1 for positivity. |
| Counterexample attempts | None found. See Reproduction: S25, S24, L1, L2, Fact 1.1, and the cone memberships of `Φ` and `Π_{uv}` on all trees of orders 2–11 and on families up to order 11. T4 on all trees of orders 3–16 and on families up to order 40. (K3) and Lemma K on 285 random weighted trees. Lemma A on a grid. |
| Formalization scope | Not assessed. The revision makes no Lean claim for MD-0016 (formal status `not-started`). There is an untracked Lean file in the working tree, outside the revision, which I did not read. `scripts/verify_lean.py` was not run. |
| Novelty coverage | Not assessed by me: **no literature search was run** in this review. The section "Prior literature" claims no novelty ("This is not a claim of novelty") and attributes the first equality of S24 and identity (1) to prior sources. I did not check those attributions. |
| Unresolved gaps | None in the mathematics. Wording and citation defects D1–D5 (D5: "Induction on `j`" is strong induction). Two source items were not read: Theorem 2.1 itself (only its description on page 3) and Observation 3.1. |

## Reproduction

Scripts, written by me and not in the repository:
`C:\Users\bezze\AppData\Local\Temp\claude\150e3719c412ed18\c083ebfc-0d09-45cf-8637-b832544d491c\scratchpad\audit.py`
and `audit2.py` in the same directory. They use python-flint 0.9.0 and
networkx 3.7. All arithmetic is exact: integer determinants at integer points
(`fmpz_mat`), exact Lagrange interpolation over `Fraction`, and the charpoly of
`D` from `fmpz_mat.charpoly()`. `ℓ_T` was taken from the charpoly of `D`, not
from L1. Polynomials are recovered by interpolation at `deg+2` integer points.
Cone membership was tested only by **sufficient certificate**: for a polynomial
of degree `≤ d`, the unique expansion in the triangular basis
`x^e(1+x)^{d−2e}` (`2e < d`), `x^e` (`d ≤ 2e ≤ 2d`) has non-negative
coefficients. Each such generator satisfies `2e+i ≥ d`. No LP test was used,
and none was needed, since every certificate passed. `Φ(K,ν)` has degree
exactly `j`, `Φ_T` has degree `n−1` and `Π_{uv}` has degree `n−d−1`.

- `uv run python audit.py 9`, all trees of orders 2–9 (192 trees). Checks per
  tree: the Fact 1.1 sign and `[x^k]ℓ = d_k`; `[x^{n−1}]ℓ = 0` and
  `[x^n]ℓ = −4`; L1 at `n+3` integer points; L2; `Φ ∈ K_{n−1}`; for every pair,
  `Π_{uv} ∈ K_{n−d−1}` and S24 (cofactor of `M` against `x^d Π_{uv}`) at every
  needed integer point; S25 coefficientwise; T4; for `n ≥ 5`, `W ≥ 3n`,
  `λ_μ((W−nx)Φ) > 0` and every pair term `≥ 0`. Pairs (S24 / Π-cone checks):
  2703 cumulative. Same run: (K3) and Lemma K on 285 random weighted trees of
  orders 1–9 (weights in `{0,1,2,3}`, non-zero), (K3) at every admissible leaf
  and `x = 0..3`. Lemma A on the grid `μ ≤ 13`, `e, i < 30`, `n ≤ 7`,
  `W ∈ {3n, 3n+1, 10n}`: 237471 checks, including strictness for `a ≥ 1`. All
  passed.
- `uv run python audit2.py full 10 11`: all 341 trees of orders 10–11, all the
  checks above, 17695 pairs. All passed.
- `uv run python audit2.py all 10 16`: T4, Fact 1.1's sign and log-concavity
  from the distance charpoly on all trees of orders 10–16 (106, 235, 551,
  1301, 3159, 7741, 19320 trees). All passed.
- `uv run python audit2.py fam 3 40 11`: paths, stars, all double stars, all
  brooms, spiders with equal legs, and one caterpillar per order, orders 3–40.
  1365 T4 checks, of which 118 at orders `≤ 11` also had the full check above.
  All passed. A first run with full checks up to order 16 was killed by its
  60-second timeout before printing and is not counted.

Total computation time is about 3 minutes.

## Verdict

**`no gap found within stated scope`**

Scope: the proofs in `wiener-form.md` of Lemma K, (K1)–(K2), Lemma S24 (except
its `C_{n−d−1}` clause, which rests on Lemma F of another note and is not used
by T4), Proposition S25, Proposition S26, Lemma A, Theorem T4 and the odd-order
corollary; and L1, L2 and R1 (general form) of `lemmas.md`, at revision
`a3e5179`. I reconstructed every step listed in the Findings. I found no
mathematical gap. The claim "self-contained except (i)–(iii)" holds in
substance, with these defects of presentation:

- D1: S26 still cites Lemma F, and the list "Used from earlier notes" still
  lists it.
- D2: the Wiener edge formula is an unlisted classical dependency.
- D3: S25 is claimed for `n = 2`, but L1 is stated for `n ≥ 3`.
- D4: the `C_{n−d−1}` clause of S24 depends on Lemma F (disclosed).
- D5: the induction in Lemma K is strong induction.

None of these invalidates T4.

Not covered: Graham–Pollak's determinant formula (cited, checked only
numerically); the statements of Theorem 2.1 and Observation 3.1 of the source
as printed (not read); any literature or novelty assessment; any Lean
formalization. Computer checks cover the ranges stated above and nothing more.
This review applies only to revision `a3e5179` and the two file hashes above.
