# Independent review — CJ-0001 — `notes/upper-bound.md` (Theorem T9, the upper half; Lemmas S40 to S46, Theorem T10)

- **Reviewer:** Claude, model `claude-opus-5-5`, run as the `adversarial-reviewer` subagent.
- **Date:** 2026-11-27
- **Independence:** fresh subagent context. The reviewer received the task
  description (catalogue id, primary source, path and revision of the claim,
  instruction to attack it) and nothing of the author's reasoning trail,
  journal or conclusion. The reviewer read `STATE.md` only for the exact
  statement and the definitions, and `notes/lemmas.md` only for `ℓ_T`. The
  model is the same model family as the author of the note (`claude-opus-5-5`),
  so independence is limited to context, not to model. The reviewer wrote its
  own check scripts (outside the repository, in the session scratchpad) and
  did not run or read the author's experiment (`upper_bound.py`, which is not
  in the revision under review anyway; see finding D1).
- **Revision reviewed:** commit `53421a6f519c49a042f9e70836c4089dd0a1e2f8`
  (`53421a6`), read with `git show 53421a6:<path>`.
  - `research/active/CJ-0001-collins-shor-peak/notes/upper-bound.md`: git blob
    `f3e7f4210efd7e5fe147d5001b6775f5effb6e14`, SHA-256
    `5643424ee9465e16a59c13ec2038baa5c7ff01c7b742d2fac40fae2810deb13a`.
  - `research/active/CJ-0001-collins-shor-peak/notes/lemmas.md` (definition of
    `ℓ_T`, `d_k` only): git blob `62dc09c52c5342841db6daf14142bb327f548029`,
    SHA-256 `a225898814df1ae584d9c58cb2c983d89bcbbd83121458c8058e9bfc4ca03c6e`.
  - `research/active/CJ-0001-collins-shor-peak/STATE.md` (statement and
    definitions only): SHA-256
    `08ff743afc071624674de817909f6eb9ac4f8a39afed06a5aa3690341d83eccc`.
- **Material given to the reviewer:** the task message naming the primary
  source (Conjecture 1.2 of arXiv:1507.02341, statement as recorded in
  `STATE.md`), the claim file and revision, and the template.

## Statement as read from the primary source

Written before reading the claim, from `STATE.md` ("Exact statement",
"Definitions and conventions"), which quotes Conjecture 1.2 of
arXiv:1507.02341 verbatim:

> The [normalized] coefficients of the distance characteristic polynomial for
> any tree `T` with `n` vertices are unimodal with peak between `⌊n/2⌋` and
> `⌈n − n/√5⌉`.

- **Objects.** `T` a tree of order `n ≥ 3`; `D` its distance matrix; `δ_k`
  the coefficient of `x^k` in `det(D − xI)`; `d_k = 2^{k−(n−2)}|δ_k|`,
  `0 ≤ k ≤ n − 2` (positive).
- **Quantifiers.** For every `n ≥ 3` and every tree `T` of order `n`.
- **Conclusion (upper half, the part claimed here).** Every index `p` with
  `d_p = max_k d_k` satisfies `p ≤ M := ⌈n − n/√5⌉` (the project's strong
  reading of ties: every maximizing index). Unimodality is Theorem 2.1 of the
  source and is not part of this claim. By R1 this is equivalent to
  `M ≥ n − 2` or `d_{M+1} < d_M`.

The claim (Theorem T9) is: for every tree of order `n ≥ 3`, every maximizing
index `p` satisfies `p < n − n/√5 + 3/5`, hence `p ≤ ⌈n − n/√5 − 2/5⌉ ≤ M`.
This is the upper half of the published statement with the same hypotheses,
the same quantifiers and the strong tie reading, and a conclusion at least as
strong. It is about the right statement.

## Reconstruction of the argument

The reviewer re-derived every step independently before checking it
numerically. Summary of the chain, with the reviewer's verdict on each link:

1. (S40) From Graham–Lovász `2D^{−1} = −L + ττᵀ/(n−1)` and Weyl interlacing
   for a rank-one PSD update, `2D^{−1}` has exactly one positive eigenvalue
   (sign of `det D` from Graham–Pollak) and `n − 1` negative ones; hence
   `det(xI − D/2) = (x − α)q(x)`, `q = Π(x + β_i)`, `β_i > 0`, `α = Σβ_i`
   (`tr D = 0`), and `ℓ_T = 4(α − x)q`. Reproduced, including the constant
   `−2^{−(n−2)}·2^n = −4`. As a by-product, S40 itself shows the coefficients
   of `ℓ_T` of degree `≤ n−2` are positive, so the identification with `d_k`
   does not depend on a separate sign convention.
2. (S41) Newton gives `t_j = q_{j+1}/q_j` strictly decreasing,
   `t_{n−2} = 1/α`, so `αt_j > 1` for `j ≤ n − 3`; the three cases of the
   sign of `d_{j+1} − d_j` are correct (the factorisation
   `4q_{j−1}[(1 − t_{j−1}) − αt_{j−1}(1 − t_j)]` re-derived).
3. (S42) `μ_q = Σ 1/(1 + β_i) = Σ |ν_i|/(1 + |ν_i|)` and the lower Weyl
   bound `ν_i ≥ λ_i(−L) = −μ_(i−1)`; monotonicity of `y/(1+y)`; the identity
   `Σ μ_j/(1+μ_j) = n − tr(I+L)^{−1}`. Reproduced.
4. (S43) Schur complement plus Sherman–Morrison for gluing at a vertex;
   `s = ε_Y`; the two diagonal blocks of `G_T` share only `(v,v)`. Reproduced.
5. (S43′) Positivity and row sums of `G`; the maximum-principle argument for
   `2G_{w*v} ≤ G_vv`. Reproduced; the bound `κ ≤ (1+a)/2` is attained (for
   example `X = P_2`), which does not matter since S45 needs only `≤`.
6. (S44) `e_j = cosh((2j+1)u)/cosh u`, `det(tI + L_{P_m}) = 2 sinh u
   sinh(2mu)/cosh u`, formula (1), its log-derivative, the values at
   `u = log φ` (`sinh u = 1/2`, `cosh u = √5/2`, `sinh 2u = √5/2`), formula
   (2), the reduction of (iii) to `ψ(x) = x/(φ^{2x}+1)`, the telescoping, the
   identity `ψ(1) − 2ψ(3) + ψ(5) = 0` (via `φ^x + φ^{−x} = √5F_x` for odd `x`
   and `φ⁴ − 3φ² + 1 = 0`), and the convexity criterion `z tanh z > 1`; at
   `x = 3`, `tanh(3 log φ) = 2/√5 = 0.894427…` and `3 log φ = 1.44364…`, so the
   stated numerical bounds (`> 0.894`, `> 1.443`, product `> 1.29`) are true,
   though the first is tight to three decimals.
7. (S45) The algebra `a(a+E)(a+E′)[Θ(E′,c′) − Θ(E,c)] = a𝒩` re-derived term by
   term; the lower bound `𝒩 ≥ (a−1)(E−E′)(c − 1/2) > 0` uses exactly S43′
   (`a > 1`, `κ ≤ (1+a)/2`), S44(i) (`E > E′`), S44(iii) (`c′ ≥ c`) and
   S44(ii) (`c > 3/5 > 1/2`). The hypotheses `p, q ≥ 1` give
   `1 ≤ p ≤ N − 1` and `N ≥ 2`, as S44 requires; `|X| ≥ 2` gives `a > 1`.
8. (T10) Induction on the number of leaves; the choice of `v` (degree `≥ 3`,
   farthest from a leaf root `ρ`) makes every branch at `v` away from `ρ` a
   pendant path attached by an end; `X` contains `v` and `ρ ≠ v`, so
   `|X| ≥ 2`; the leaf count drops by exactly one and the order is unchanged.
   Reproduced.
9. (S46) `r = φ^{−2}` satisfies `r² − 3r + 1 = 0`, the Poisson-kernel
   expansion, `r/(1 − r²) = 1/√5`, and the three cases of
   `Σ_j cos(mjπ/n)`. Reproduced.
10. (T9) `μ_q ≤ n − tr(T) ≤ n − tr(P_n) < x − 2/5`; Darroch gives every mode
    of `q` `< μ_q + 1 < x + 3/5`, so `≤ K = ⌈x − 2/5⌉` (this holds whether or
    not `x − 2/5` is an integer); if `K ≤ n − 3`, then `q_{K+1} < q_K` (the
    argument that otherwise some mode is `≥ K + 1` is correct, including a
    tie `q_K = q_{K+1}`), and S41 with `k = K` (`0 ≤ K ≤ n − 3`; `K ≥ 2` for
    `n ≥ 3`) gives every maximizing index of `d` `≤ K`; if `K ≥ n − 2` the
    conclusion is trivial. `K ≤ ⌈x⌉ = M`. Reproduced.

No step could not be reproduced.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | T9 assumes only that `T` is a tree of order `n ≥ 3`, exactly the hypothesis of Conjecture 1.2. Lemma hypotheses are met where used: S40 needs `n ≥ 2` and connectivity (tree); S41 needs `0 ≤ k ≤ n − 3` (T9 uses it only in the branch `K ≤ n − 3`, with `K ≥ 2`); S43′ needs `|X| ≥ 2` (ensured in T10 because the leaf root `ρ` differs from `v`); S44 needs `N ≥ 2`, `1 ≤ r ≤ N − 1` (ensured by `p, q ≥ 1`); S45 needs `|X| ≥ 2`, `p, q ≥ 1`. The reviewer checked that S45 is false-as-strict without `|X| ≥ 2` (for `|X| = 1` both trees are paths and the traces are equal), so that hypothesis is necessary and is correctly stated and supplied. |
| Quantifiers | "For every tree of order `n ≥ 3`, every maximizing index" — matches the published statement under the strong tie reading. T10 is "for every tree of order `n ≥ 1`"; S46 "for `n ≥ 1`". No quantifier is weakened. Ties in `d` and ties in `q` are both handled (T9's proof covers `q_K = q_{K+1}` explicitly; S41 gives strict decrease of `d` after `K`, so every maximizing index of `d` is `≤ K`). |
| Mathematical definitions | `ℓ_T = −2^{−(n−2)}det(2xI − D)` and its coefficients `d_k`, `0 ≤ k ≤ n − 2`, agree with `lemmas.md` and with `STATE.md`'s `d_k = 2^{k−(n−2)}|δ_k|`; the reviewer confirmed this exactly for every tree of order 3 to 17 (positivity, `ℓ_{n−1} = 0`, `ℓ_n = −4`). `M = ⌈n − n/√5⌉` as in the source. `G_H`, `g_X`, `k_X`, `ε_X`, `κ_X`, `t_X`, `E_r`, `c_r` are defined before use and consistently. Notational overloads (not errors): `tr(H)` denotes `tr G_H`; the letter `q` is both the polynomial and a pendant-path length in S45/T10; `c` is both `c_r` and `2 log φ` in S44; `m` is a mode of `q` in T9 while `STATE.md` uses `m = ⌊n/2⌋`. See D3. |
| Boundary cases | `n = 3, 4`: `K ≥ n − 2`, trivial branch, consistent with exact data. `K` vs `n − 3`: both branches exercised in the reviewer's runs. S44 `r = 0` / `r = N`: formula (2) valid (`a = 1`); S44 is only claimed for `1 ≤ r ≤ N − 1`, and only that range is used. S44(iii) equality `N = 2, r = 1`: confirmed exactly to be the only equality case for `N ≤ 60`; it does not hurt S45 because S45 uses only `c′ ≥ c`. S43′ upper bound is attained (`κ = (1+a)/2`, e.g. `X = P_2`); S45 uses it as `≤`, so this is fine. `c_r → 3/5` as `r, s → ∞` (S44(ii) is asymptotically tight) but S45 needs only `c > 1/2`. S43 with `|Y| = 1` (`ε_Y = 0`) is consistent. S46 at `n = 1` gives 1 exactly. |
| Lemma S40 | Correct. Weyl (W) is stated correctly for decreasing order. Exactly verified by the reviewer: Graham–Lovász `D^{−1}` formula for every tree of order 3 to 17; the inertia `(1, n−1)` of `D` and `α = Σβ_i` (rigorous balls, 300 bits); `d_k = 4(αq_k − q_{k−1})`. |
| Lemma S41 | Correct. The proof uses strict Newton inequalities, valid since `q` has `n − 1` negative real roots and positive coefficients. Conclusion (peak of `d` ≤ largest mode of `q`) checked on every tree of order 3 to 17. |
| Lemma S42 | Correct. Checked (rigorous balls vs exact rational traces) on every tree of order 3 to 17. Citation of Merris (J. Graph Theory 14 (1990) 365–369) checked by the reviewer against the paper's first two pages: its theorem is that the eigenvalues of `−2K^{−1}` interlace those of `D`, `K = 2I + A(T*)`, whose eigenvalues are the non-zero Laplacian eigenvalues; consistent with the note's description. Equation number "(2)" not checked. |
| Lemma S43 | Correct. Exact rational check of `1/g_T = 1/g_X + 1/g_Y − 1` and of the trace formula on 400 random pairs of rooted trees (orders 1 to 8 each). |
| Lemma S43′ | Correct. Exact check on all 4,393 rooted trees of order 2 to 11 (`0 < g < 1`, `1 ≤ κ ≤ (1+a)/2`, `2G_wv ≤ G_vv` for all `w ≠ v`); the maximum of `(κ−1)/((a−1)/2)` is exactly 1. |
| Lemma S44 | Correct. (i), (ii), (iii) checked in exact rational arithmetic for `2 ≤ N ≤ 60`, all `1 ≤ r ≤ N − 1`; equality in (iii) only at `(N, r) = (2, 1)`. The analytic proof was re-derived in full (see reconstruction, item 6). |
| Lemma S45 | Correct. Exact check on all rooted trees `(X, v)` of order 2 to 8 with `1 ≤ p ≤ q ≤ 6` (6,825 cases): strict inequality in every case. |
| Theorem T10 | Correct (proof by S45 and leaf induction). Exact check: for every `n ≤ 17` the path is the unique minimizer of `tr(I + L)^{−1}` among all trees of order `n`. The "second route" via Andriantiana–Misanantenaina–Wagner is labelled unreviewed by the author; the reviewer did not check it (only the arXiv abstract of arXiv:1903.09825 was read, which does not name the extremal tree). It bears on novelty, not correctness. |
| Lemma S46 | Correct. Closed form agrees with the exact rational trace of `(I + L_{P_n})^{−1}` to `10^{−300}` for `n = 1..59, 100, 150, 200`. |
| Theorem T9 | Correct; see reconstruction item 10. Checked on every tree of order 3 to 17 and on 198 further trees of order 20 to 70 (random trees and brooms), and on paths of order 3 to 160 (exact `d`): every maximizing index is `≤ K ≤ M`. For paths, the peak equals `M` exactly for `n ∈ {9, 18, 27, 36, 45, 47, …, 159}` and in each such case `frac(n − n/√5) ≥ 0.81 > 2/5`, consistent with Corollary 2. |
| Corollaries | (1) correctly states its dependence on the candidate T6(c) (MD-0019) and that neither half is established. (2) is a correct consequence of T9; its parenthetical "checked in the stored experiment, part C" refers to material absent from the revision (D1). (3) follows from S41, (D) and S42 as stated (the reviewer re-derived it: if the largest mode `k*` of `q` is `≤ n − 3`, S41 applies with `k = k*`; otherwise `p ≤ n − 2 ≤ k*`). |
| Logical implications | Every implication in the chain S40 → S41; S40 → S42; S43, S43′, S44 → S45 → T10; S42 + T10 + S46 + (D) + S41 → T9 was checked; no missing case. The case split in T9 (`K ≥ n − 2` / `K ≤ n − 3`) is exhaustive. T9 does not use log-concavity or unimodality of `d` (Theorem 2.1 of the source), nor any candidate result of the project, as the note says. |
| Dependency assumptions | Classical results used: Graham–Lovász `D^{−1}` (verified exactly by the reviewer on all trees `n ≤ 17`, not against the 1978 paper); Graham–Pollak `det D` (implied by the reviewer's exact charpolys, not checked against the paper); Weyl interlacing for rank-one updates and Newton's inequalities (standard; statements as written are correct); Darroch's rule — checked by the reviewer against Pitman, J. Combin. Theory Ser. A 77 (1997), p. 284 (Berkeley technical report 453 version, journal pagination): "Darroch showed that such a mode `m` differs from the mean `μ` by less than 1", with the precise form of Darroch's Theorem 4 as eq. (13), whose two-mode case also satisfies `|m − μ| < 1` for both modes; so "every maximizing index" is justified. Darroch's original paper was not read by the reviewer. (M): standard. Laplacian spectrum of `P_n`: standard, and confirmed indirectly by the S46 exact check. |
| Counterexample attempts | (a) Exhaustive exact/rigorous check of every intermediate inequality and of T9 on all non-isomorphic trees of order 3 to 17 (result in "Reproduction"). (b) Paths to order 160 (the extremal family). (c) Random trees and brooms of order 20 to 70. (d) S45 at the excluded boundary `|X| = 1` (equality, as expected). (e) Tightness probes: S43′ bound attained, S44(ii) bound approached asymptotically, S44(iii) equality case. No counterexample to any lemma or to T9 was found. |
| Formalization scope | Nothing of this note is formalized in Lean; no Lean statement to compare. Not assessed. |
| Novelty coverage | The reviewer ran 5 web searches (general web search tool; one in "extended" mode) and fetched arXiv:2407.03309 (abstract), arXiv:2601.02547 (abstract; unrelated: matroids, ultrametric trees), arXiv:1903.09825 (abstract), Pitman 1997 (pp. 282–286) and Merris 1990 (pp. 365–366). No source proving the peak location of the distance coefficients of trees (the Collins–Shor interval) was found; arXiv:2407.03309 locates the peak for the Min-4PC matrix, a different matrix. Not searched: MathSciNet, zbMATH, Google Scholar forward citations of arXiv:1507.02341 / ELA 2018, MathOverflow. This coverage establishes nothing about originality. T10 may be a known consequence of Andriantiana–Misanantenaina–Wagner (the note says so); the reviewer could not confirm or refute this from the abstract. |
| Unresolved gaps | No mathematical gap found. Defects that do not affect the proof are listed below (D1 to D4). |

### Defects (none is a gap in the proof of T9)

- **D1 (provenance; must be fixed before promotion).** The section "Exact
  checks" and Corollary 2 cite a "stored experiment"
  `experiments/CJ-0001-collins-shor-peak/upper_bound.py` with result
  `results/upper-bound.json`, "see the README of that directory". At revision
  `53421a6` neither file exists in the tree (`git ls-tree` lists neither; in
  the working copy both are untracked), and the README at `53421a6` does not
  mention them. Statements of this note that rest on that experiment
  (Corollary 2's "checked in the stored experiment, part C", and the claim that
  a stored check exists) are unsupported at the reviewed revision. The
  reviewer's own computations independently confirm the mathematical content
  they would have supported.
- **D2 (wording).** Remarks, third bullet: "Only `tr(I + L_T)^{−1} ≥ n/√5` is
  needed in T9 (with the `2/5` absorbing the step from `μ_q` to the mode)".
  The first half is correct (with `tr ≥ n/√5`, `μ_q ≤ x`, every mode of `q`
  is `< x + 1`, hence `≤ ⌈x⌉ = M`), but the parenthetical is misleading: the
  `2/5` is not needed for `M`; it is what yields the sharper `K`.
- **D3 (notation).** Overloaded symbols (`q` polynomial vs. path length in
  S45/T10; `c` for `c_r` and `2 log φ` in S44; `m` a mode of `q` in T9 vs.
  `m = ⌊n/2⌋` in `STATE.md`; `tr(H)` for `tr G_H`). No step is affected.
- **D4 (citations not checked at source).** Darroch (1964) was checked only
  through Pitman's restatement; Graham–Lovász and Graham–Pollak were checked
  only numerically; the "second route" for T10 is unchecked (as the note
  itself says). Merris eq. "(2)" was not located (the theorem itself was).

## Reproduction

All scripts are the reviewer's own (python-flint 0.9.0 for exact `fmpz`/`fmpq`
matrices and rigorous `arb` balls; networkx 3.7 for tree enumeration), run with
`uv run python <script>` from `d:\conjectura` on 2026-11-27 (Windows 10). They
live in the session scratchpad, not in the repository, and import no project
code.

1. `rev_check.py 17` — for every non-isomorphic tree of order 3 to 17
   (81,135 trees: 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1,301, 3,159, 7,741, 19,320, 48,629 for n = 3..17; run 15:59 to 16:07, exit code 0): exact characteristic polynomial of `D`; `d_k > 0`,
   `ℓ_{n−1} = 0`, `ℓ_n = −4`; exact Graham–Lovász identity; roots of
   `det(xI − D/2)` as rigorous balls (300 bits): one positive, `n − 1`
   negative, `α = Σβ` to `10^{−60}`; `d_k = 4(αq_k − q_{k−1})`; strict Newton
   for `q`; `μ_q ≤ n − tr(I + L)^{−1}` (exact rational trace); every mode of
   `q` within 1 of `μ_q`; max peak of `d` ≤ max mode of `q`;
   `tr(T) ≥ tr(P_n)` with equality only for the path; max peak of `d`
   `≤ K ≤ M`; S46 for the path. Result: all assertions passed; per order, the
   unique trace minimizer is the path. The bound `K` of T9 is attained (some
   maximizing index equals `K`) by 2, 6, 2, 41, 523, 4,851 and 38,683 trees at
   n = 4, 6, 9, 11, 13, 15, 17 and by none at the other orders, so the sharpened
   bound is not slack at small orders; no tree exceeds it.
2. `rev_lemmas.py` — S43 exact on 400 random rooted pairs; S43′ exact on all
   4,393 rooted trees of order 2 to 11; S44 (i)–(iii) exact for `N = 2..60`
   (equality in (iii) only at `(2, 1)`); S45 exact on 6,825 cases (`|X| = 2..8`,
   `1 ≤ p ≤ q ≤ 6`), plus the boundary `|X| = 1` (equality). All passed.
3. `rev_large.py` — paths of order 3 to 160 (exact `d` from the integer
   characteristic polynomial): peak `≤ K ≤ M`; peak `= M` at 27 orders, all
   with fractional part of `n − n/√5` at least 0.8124. Full chain of item 1 on
   198 random trees and brooms of order 20 to 70. All passed.
4. `rev_s46.py` — S46 closed form vs. exact trace, `n = 1..59, 100, 150, 200`,
   2000-bit balls, agreement to `10^{−300}`. Passed.

The author's experiment `upper_bound.py` was not run (it is not part of the
revision under review; D1).

## Verdict

**`no gap found within stated scope`**

Scope: the mathematical content of
`research/active/CJ-0001-collins-shor-peak/notes/upper-bound.md` at commit
`53421a6` (blob `f3e7f421…`): Lemmas S40, S41, S42, S43, S43′, S44, S45, S46,
Theorem T10 (first proof) and Theorem T9, and Corollaries 2 and 3 as
consequences of T9. Every step was reconstructed independently and every
lemma was tested in exact or rigorous arithmetic; T9 itself was tested on all
trees of order at most 17 and on paths up to order 160. Classical tools were
taken as stated, with Darroch's rule checked against Pitman's restatement only.

Not covered: Corollary 1 (depends on T6(c), reviewed elsewhere or not at all);
the "second route" to T10; the author's experiment (absent from the revision,
D1); originality (searches listed above establish nothing); Lean (none
exists). The reviewer is the same model as the author, so independence is of
context only. This is one AI review, not human peer review, and it applies
only to the revision named above; defect D1 should be repaired before the
note is cited as having a stored computation.
