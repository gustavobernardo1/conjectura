# CJ-0001 — the upper bound `⌈n − n/√5⌉` for every tree: distance spectrum, Darroch's rule, and the trace of `(I + L)^{−1}`

Status of this file: written by an AI agent (Claude, model `claude-opus-5-5`)
on 2026-11-27, session 13. Lemmas S40 to S46 and Theorems T9 and T10 have
written proofs below. **Nothing here is an established result**: a statement
of this file counts as reviewed only where a report under
[`../reviews/`](../reviews/) names this file and its revision. Nothing here
is a claim of novelty. Unlike the notes of sessions 9 to 12, the proof of
T9 (and of everything it uses, S40 to S46 and T10) uses none of the cone
machinery and none of the candidate results MD-0015 to MD-0021, only the
classical facts listed under "Tools"; Corollary 1 alone uses Theorem T6(c)
(MD-0019).

**Revision 1** (same session), after two independent AI reviews of revision
`53421a6` (`../reviews/2026-11-27-claude-opus-5-5-upper-bound.md`,
`../reviews/2026-11-27-claude-sonnet-5-5-upper-bound.md`; both "no gap found
within stated scope"). Changes, all of wording, notation or citation (no
statement and no step of a proof changed): the stored computation is cited
with the revision at which it is committed and run (both reviews, D1); the
closed form of `det(tI + L_{P_m})` is written out (Sonnet review, D3); the
case `n = 1` and `e^{iπm/n} ≠ 1` are stated in S46 (Sonnet, D6); the last
remark is reworded (both, D2/D4); the header names the proof of T9 (Sonnet,
D5); overloaded symbols renamed (Opus review, D3): the lengths of the
pendant paths in S45 and T10 are `j_1, j_2` (not `p, q`), the constant
`2 log φ` is `γ` (not `c`), a mode of `q` is `m_q`; a pointer to
[`path-peak.md`](path-peak.md) for the peak of the path.

What this file does. It proves the **upper half** of the Collins–Shor
conjecture (Conjecture 1.2 of arXiv:1507.02341):

> **Theorem T9.** For every tree `T` of order `n ≥ 3`, every maximizing index
> `p` of the normalized coefficients `d_0, …, d_{n−2}` satisfies
> `p < n − n/√5 + 3/5`; in particular `p ≤ ⌈n − n/√5⌉`.

The route is spectral and does not pass through the polynomial identities of
the earlier notes: (1) `ℓ_T = 4(α − x)q(x)` with `q` real-rooted (the
negative distance eigenvalues); (2) the peak of `d` is at most the mode of
`q` (Lemma S41); (3) the mode of `q` is within 1 of its mean (Darroch's
rule); (4) the mean of `q` is at most `n − tr(I + L)^{−1}` (interlacing,
Lemma S42); (5) the path minimizes `tr(I + L)^{−1}` among trees of order `n`
(Theorem T10); (6) `tr(I + L_{P_n})^{−1} > n/√5 + 2/5` (Lemma S46).

## Notation

`T` is a tree of order `n`, `D` its distance matrix, `L` its Laplacian,
`τ = (2 − deg v)_v`. `ℓ_T(x) = −2^{−(n−2)} det(2xI − D)`; its coefficient of
`x^k` is `d_k` for `0 ≤ k ≤ n − 2` ([`lemmas.md`](lemmas.md), from
Observation 3.1 of the source). `M = ⌈n − n/√5⌉`. For a graph `H`,
`G_H = (I + L_H)^{−1}` and `tr(H) = tr G_H`. `φ = (1 + √5)/2`.

A **rooted tree** `(X, v)` has `g_X = (G_X)_{vv}`, `k_X = (G_X²)_{vv}`,
`ε_X = 1/g_X − 1`, `κ_X = k_X/g_X²`, `t_X = tr G_X`.

## Tools (classical; cited, not reproved)

- **(GL)** Graham–Lovász: `D^{−1} = −L/2 + ττᵀ/(2(n−1))`; Graham–Pollak:
  `det D = (−1)^{n−1}(n−1)2^{n−2}` (both as used in L1 of `lemmas.md`).
- **(W)** Weyl interlacing for a rank-one positive semidefinite update: if
  `B = A + wwᵀ` with `A` symmetric, eigenvalues in decreasing order satisfy
  `λ_i(A) ≤ λ_i(B) ≤ λ_{i−1}(A)`.
- **(N)** Newton's inequalities: a polynomial `Σ_{k=0}^{N} q_k x^k` with only
  real roots and positive coefficients has
  `q_k² ≥ q_{k−1}q_{k+1}(1 + 1/k)(1 + 1/(N − k)) > q_{k−1}q_{k+1}`, `1 ≤ k ≤ N−1`.
- **(D)** Darroch's rule (J. N. Darroch, Ann. Math. Statist. 35 (1964)
  1317–1321, Theorem 4; as stated by J. Pitman, J. Combin. Theory Ser. A 77
  (1997) 279–303, p. 284): if a polynomial with non-negative coefficients
  has only real zeros, every index `m` at which its coefficient is maximal
  satisfies `|m − μ| < 1`, `μ = P′(1)/P(1)`.
- **(M)** `(I + L)` is a non-singular M-matrix; for a connected graph its
  inverse is entrywise positive; `(I + L)1 = 1`, so every row of `G` sums
  to 1.
- The Laplacian eigenvalues of `P_n` are `2 − 2cos(jπ/n)`, `0 ≤ j ≤ n − 1`.

## Lemma S40 (spectral form of `ℓ_T`)

**Lemma S40.** Let `T` be a tree of order `n ≥ 2`. The matrix `D/2` has one
positive eigenvalue `α` and `n − 1` negative eigenvalues `−β_1, …, −β_{n−1}`,
and `α = Σ β_i`. With `q(x) = Π_{i=1}^{n−1}(x + β_i) = Σ_{k=0}^{n−1} q_k x^k`,

`ℓ_T(x) = 4(α − x) q(x)`,  so  `d_k = 4(α q_k − q_{k−1})` for `0 ≤ k ≤ n−2` (`q_{−1} = 0`).

*Proof.* By (GL), `2D^{−1} = −L + wwᵀ`, `w = τ/√(n−1)`. The eigenvalues of
`−L` are `0 ≥ −μ_(1) ≥ … ≥ −μ_(n−1)`, `0 < μ_(1) ≤ … ≤ μ_(n−1)` the non-zero
Laplacian eigenvalues (a tree is connected). By (W), the eigenvalues
`ν_1 ≥ … ≥ ν_n` of `2D^{−1}` satisfy `ν_i ≤ λ_{i−1}(−L) ≤ 0` for `i ≥ 2`, and
none is zero, so `ν_2, …, ν_n < 0`; the product `Π ν_i` has the sign of
`det D`, that is `(−1)^{n−1}`, so `ν_1 > 0`. The eigenvalues of `D/2` are
`1/ν_i`. `tr D = 0` gives `α = Σ β_i`. Finally
`det(2xI − D) = 2^n Π(x − θ_i)` over the eigenvalues `θ_i` of `D/2`, so
`ℓ_T = −4(x − α)q(x)`. ∎

## Lemma S41 (the peak of `d` lies at or before the mode of `q`)

**Lemma S41.** Let `n ≥ 3` and `0 ≤ k ≤ n − 3`. If `q_{k+1} < q_k`, then
`d_{j+1} < d_j` for every `k ≤ j ≤ n − 3`; hence every maximizing index of
`d_0, …, d_{n−2}` is `≤ k`.

*Proof.* `q` has positive coefficients and real roots, so by (N) the ratios
`t_j = q_{j+1}/q_j` (`0 ≤ j ≤ n − 2`) are strictly decreasing, and
`t_{n−2} = q_{n−1}/q_{n−2} = 1/e_1(β) = 1/α`. Hence `α t_j > 1` for
`j ≤ n − 3`. Fix `j` with `k ≤ j ≤ n − 3`; then `t_j ≤ t_k < 1`. Now
`d_{j+1} − d_j = 4[α(q_{j+1} − q_j) − (q_j − q_{j−1})]`.
If `j = 0`: this is `4[α(q_1 − q_0) − q_0] < 0`.
If `j ≥ 1` and `q_j ≥ q_{j−1}`: the first term is negative, the second
non-positive.
If `j ≥ 1` and `q_j < q_{j−1}`: then `t_j < t_{j−1} < 1` and
`d_{j+1} − d_j = 4q_{j−1}[(1 − t_{j−1}) − α t_{j−1}(1 − t_j)]`; since
`α t_{j−1} > 1` and `1 − t_j > 1 − t_{j−1} > 0`, the bracket is negative.
So `d` is strictly decreasing from index `k` to `n − 2`. ∎

The proof does not use the log-concavity of `d` (Theorem 2.1 of the source).

## Lemma S42 (the mean of `q` and the Laplacian spectrum)

**Lemma S42.** `μ_q := q′(1)/q(1) = Σ_i 1/(1 + β_i) ≤ Σ_j μ_(j)/(1 + μ_(j)) = n − tr(T)`.

*Proof.* With the notation of the proof of S40, `1/(1 + β_i) = |ν_{i+1}|/(1 + |ν_{i+1}|)`
after relabelling, since `β = −1/ν`. By (W), `ν_i ≥ λ_i(−L) = −μ_(i−1)`
for `i ≥ 2`, so `|ν_i| ≤ μ_(i−1)`, and `y ↦ y/(1+y)` is increasing. Finally
`tr(I + L)^{−1} = 1 + Σ_j 1/(1 + μ_(j))`, so `Σ_j μ_(j)/(1 + μ_(j)) = n − tr(T)`. ∎

The interlacing `0 > −2/μ_(n−1) ≥ ∂_2 ≥ −2/μ_(n−2) ≥ … ≥ ∂_n ≥ −2/μ_(1)`
between the distance eigenvalues `∂_i = 2θ_i` and the Laplacian ones is
R. Merris, J. Graph Theory 14 (1990) 365–369, eq. (2) (read by the literature
audit of session 13); the proof above is the same argument through (GL).

## Lemma S43 (gluing two rooted trees)

**Lemma S43.** Let `(X, v)`, `(Y, v)` be rooted trees and `T` the tree
obtained by identifying their roots. Then `1/g_T = 1/g_X + 1/g_Y − 1` (so
`ε_T = ε_X + ε_Y`) and

`t_T = t_X + t_Y − g_T[1 + ε_Y κ_X g_X + ε_X κ_Y g_Y]`.

*Proof.* Order the vertices `X` (containing `v`), then `Y ∖ v`. With
`C = (I + L_Y)[Y∖v]` and `b` the indicator of the neighbours of `v` in `Y`,
`I + L_T = [[I + L_X + deg_Y(v)E_vv, −b̃], [−b̃ᵀ, C]]` (`b̃` is `b` placed in
row `v`). By the Schur complement, the `X`-block of `G_T` is
`(I + L_X + s E_vv)^{−1}` with `s = deg_Y(v) − bᵀC^{−1}b`. In `Y` alone the
same elimination gives `1/g_Y = 1 + deg_Y(v) − bᵀC^{−1}b`, so `s = ε_Y`.
Sherman–Morrison: `(I + L_X + sE_vv)^{−1} = G_X − s G_Xe_ve_vᵀG_X/(1 + s g_X)`;
its `(v, v)` entry is `g_X/(1 + s g_X)` and its trace is `t_X − s k_X/(1 + s g_X)`.
Hence `g_T = g_X/(1 + ε_Y g_X)`, that is `1/g_T = 1/g_X + ε_Y`, which is the
first claim. Symmetrically the `Y`-block of `G_T` has trace
`t_Y − ε_X k_Y/(1 + ε_X g_Y)`. The two blocks share only `v`, so
`t_T = t_X − ε_Y k_X/(1 + ε_Y g_X) + t_Y − ε_X k_Y/(1 + ε_X g_Y) − g_T`.
Finally `ε_Y k_X/(1 + ε_Y g_X) = ε_Y κ_X g_X · g_X/(1 + ε_Y g_X) = g_T ε_Y κ_X g_X`,
and symmetrically. ∎

**Lemma S43′ (bounds at a root).** For a rooted tree `(X, v)` with
`|X| ≥ 2`: `0 < g_X < 1`, so `a := 1/g_X = 1 + ε_X > 1`, and
`1 ≤ κ_X ≤ 1 + ε_X/2 = (1 + a)/2`.

*Proof.* By (M), row `v` of `G_X` is positive and sums to 1, so
`ε_X = Σ_{w≠v} G_vw/G_vv > 0` and `κ_X − 1 = Σ_{w≠v}(G_vw/G_vv)²`. It is
enough to show `G_wv ≤ G_vv/2` for `w ≠ v`. Let `w*` maximize `G_wv` over
`w ≠ v` and let `d = deg w*`. Row `w*` of `(I + L)G = I` in column `v` reads
`(1 + d)G_{w*v} = Σ_{x∼w*} G_xv`. If `v` is not a neighbour of `w*`, the
right side is `≤ d G_{w*v}`, so `G_{w*v} ≤ 0`, contradicting (M). So `v ∼ w*`
and `(1 + d)G_{w*v} ≤ G_vv + (d − 1)G_{w*v}`, that is `2G_{w*v} ≤ G_vv`. ∎

## Lemma S44 (the path, seen from one vertex)

For `N ≥ 2` let `P = P_{N+1}` with vertices `0, …, N`, and for a vertex `r`
put `G = G_P`, `E_r = 1/G_rr − 1` and `c_r = (G²)_{rr}/G_rr`.

**Lemma S44.** For `1 ≤ r ≤ N − 1`: (i) `E_r > E_0`; (ii) `c_r > 3/5`;
(iii) `c_0 ≥ c_r`, with equality only for `N = 2`, `r = 1`.

*Proof.* Work with `G(t) = (tI + L_P)^{−1}`, `t > 0`, and write
`t = 4 sinh²u`, `u > 0`; `t = 1` is `u = log φ`. Let `e_j(t)` be the
determinant of the `j × j` tridiagonal matrix with diagonal
`(t + 1, t + 2, …, t + 2)` and `−1` next to the diagonal (`e_0 = 1`): it is
the minor of `tI + L_P` on a segment of `j` vertices containing an end of
`P` and not `r`. Since `t + 2 = 2cosh 2u`, `e_1 = t + 1 = cosh 3u/cosh u` and
`e_j = (t + 2)e_{j−1} − e_{j−2}`, we get `e_j = cosh((2j+1)u)/cosh u`.
Expanding at an end (`m ≥ 2`), `det(tI + L_{P_m}) = (t + 1)e_{m−1} − e_{m−2}`;
with `t + 1 = 2cosh 2u − 1` and `2cosh 2u·cosh((2m−1)u) = cosh((2m+1)u) + cosh((2m−3)u)`
this is `[cosh((2m+1)u) − cosh((2m−1)u)]/cosh u = 2 sinh u sinh(2mu)/cosh u`;
for `m = 1` the right side is `4 sinh²u = t`, as it should be.
Removing `r` splits `P` into segments of `r` and `s = N − r` vertices, so with
`a = 2r + 1`, `b = 2s + 1`, `a + b = 2N + 2`:

`G_rr(t) = e_r e_s / det(tI + L_P) = cosh(au) cosh(bu) / (2 sinh u cosh u sinh((a+b)u))`.  (1)

(i) By (1), `G_rr/G_00 = cosh(au)cosh(bu)/(cosh(u)cosh((a+b−1)u))`
`= [cosh((a+b)u) + cosh((a−b)u)]/[cosh((a+b)u) + cosh((a+b−2)u)] < 1`, because
`|a − b| < a + b − 2` when `a, b ≥ 3`. So `G_rr < G_00`.

(ii) `d/dt G(t) = −G(t)²`, so `c_r = −(d/dt) log G_rr(t)` at `t = 1`. From (1),
`(d/du) log G_rr = a tanh(au) + b tanh(bu) − tanh u − coth u − (a+b)coth((a+b)u)`,
and `dt/du = 4 sinh 2u`. At `u = log φ`: `sinh 2u = (φ² − φ^{−2})/2 = √5/2`,
`tanh u = 1/√5`, `coth u = √5`. Hence

`c_r = [6/√5 + (a+b)coth((a+b)u) − a tanh(au) − b tanh(bu)] / (2√5)`,  (2)

valid for every `0 ≤ r ≤ N` (for `r = 0`, `a = 1`, `b = 2N + 1`). Since
`coth > 1 > tanh` on `(0, ∞)`, the bracket exceeds `6/√5`, so `c_r > 3/5`.

(iii) By (2) (the `coth` terms are the same for `r` and for `0`) and
`tanh z = 1 − 2/(e^{2z} + 1)` (the linear parts cancel because
`a + b = 1 + (2N + 1)`):

`c_0 − c_r = [ψ(1) + ψ(2N+1) − ψ(a) − ψ(b)] / √5`,  `ψ(x) = x/(φ^{2x} + 1)`.

Put `f_k = ψ(2k + 1)` and `δ_k = f_k − f_{k+1}`. Then
`f_0 + f_N − f_r − f_s = Σ_{i=0}^{r−1} (δ_i − δ_{s+i})`. It suffices that
`δ` is non-increasing with `δ_0 = δ_1` and `δ_k > δ_{k+1}` for `k ≥ 1`:
then each term is `≥ 0` (`s + i > i`), and all vanish only if `r = 1` and
`s = 1`.
- `δ_0 = δ_1`: for odd `x`, `φ^{2x} + 1 = φ^x(φ^x + φ^{−x}) = √5 F_x φ^x`, so
  `ψ(1) − 2ψ(3) + ψ(5) = (φ^{−1} − 3φ^{−3} + φ^{−5})/√5 = φ^{−5}(φ⁴ − 3φ² + 1)/√5 = 0`,
  since `φ⁴ = 3φ + 2` and `3φ² = 3φ + 3`.
- `δ_k > δ_{k+1}` for `k ≥ 1`: this is strict convexity of `ψ` on `[3, ∞)`.
  With `γ = 2 log φ`, `σ = 1/(e^{γx} + 1)`, one has
  `ψ″(x) = γσ(1 − σ)[γx tanh(γx/2) − 2]`, positive iff `z tanh z > 1` for
  `z = x log φ`. `z tanh z` is increasing on `(0, ∞)`; at `x = 3`,
  `tanh(3 log φ) = (φ⁶ − 1)/(φ⁶ + 1) = (8φ + 4)/(8φ + 6) > 0.894` and
  `3 log φ > 1.443`, so `z tanh z > 1.29`. ∎

## Lemma S45 (merging two pendant paths lowers the trace)

**Lemma S45.** Let `(X, v)` be a rooted tree with `|X| ≥ 2` and `j_1, j_2 ≥ 1`.
Let `T(j_1, j_2)` be `X` with two pendant paths of `j_1` and `j_2` new
vertices attached at `v`, and `T(j_1+j_2, 0)` be `X` with one pendant path of
`j_1 + j_2` new vertices attached at `v`. Then `tr T(j_1, j_2) > tr T(j_1+j_2, 0)`.

*Proof.* Let `N = j_1 + j_2` and `P = P_{N+1}` as in S44. `T(j_1, j_2)` is `X`
glued at `v` to `(P, j_1)`, and `T(N, 0)` is `X` glued at `v` to `(P, 0)`. In
Lemma S43 with `Y = (P, r)`: `ε_Y = E_r`, `κ_Y g_Y = k_Y/g_Y = c_r`, and
`t_Y = tr P` does not depend on `r`. With `a = 1/g_X` and `κ = κ_X`,
S43 gives `tr T(N,0) = t_X + tr P − Θ(E_0, c_0)` and
`tr T(j_1,j_2) = t_X + tr P − Θ(E_{j_1}, c_{j_1})`, where

`Θ(E, c) = [1 + Eκ/a + (a − 1)c]/(a + E)`

(`g_T = 1/(a + E)`, `ε_X = a − 1`). Write `E = E_{j_1}`, `c = c_{j_1}`,
`E′ = E_0`, `c′ = c_0` (`1 ≤ j_1 ≤ N − 1`). Then
`tr T(j_1,j_2) − tr T(N,0) = Θ(E′, c′) − Θ(E, c)` and

`a(a + E)(a + E′)[Θ(E′, c′) − Θ(E, c)] = a·𝒩`,
`𝒩 = (E − E′)(1 − κ) + (a − 1)[(a + E)c′ − (a + E′)c]`.

(Multiply `Θ(E′,c′)` by `a(a+E′)` to get `a[1 + (a−1)c′] + κE′`, and
similarly; the `κ` terms give `κa(E′ − E)`.) By S44(i) `E > E′`, and by
S43′ `1 − κ ≥ −(a − 1)/2`, so
`𝒩 ≥ (a − 1)[(a + E)c′ − (a + E′)c − (E − E′)/2]`. By S44(iii) `c′ ≥ c`, so
`(a + E)c′ ≥ (a + E)c` and
`𝒩 ≥ (a − 1)(E − E′)(c − 1/2)`, which is positive by S43′ (`a > 1`),
S44(i) and S44(ii). ∎

## Theorem T10 (the path minimizes `tr(I + L)^{−1}`)

**Theorem T10.** For every tree `T` of order `n ≥ 1`,
`tr(I + L_T)^{−1} ≥ tr(I + L_{P_n})^{−1}`, with equality only for `T ≅ P_n`.
Equivalently, `Σ_j μ_j/(1 + μ_j)` over the Laplacian eigenvalues is
maximized, among trees of order `n`, exactly by the path.

*Proof.* By induction on the number of leaves. A tree with at most two
leaves is a path. Otherwise root `T` at a leaf `ρ` and let `v` be a vertex of
degree `≥ 3` at maximum distance from `ρ`. Every branch at `v` not
containing `ρ` has no vertex of degree `≥ 3`, so it is a path attached to `v`
by an end; there are `deg v − 1 ≥ 2` of them. Take two, with `j_1` and `j_2`
vertices, and let `X` be `T` without them (`v ∈ X`, `ρ ∈ X`, `|X| ≥ 2`). By
S45, `T′ = T(j_1+j_2, 0)` has `tr T′ < tr T`, and `T′` has one leaf fewer (the
two ends are replaced by one, and `v` keeps degree `≥ 2`). ∎

*Second route (literature audit of session 13; not reviewed).* For a forest
the matching polynomial is the characteristic polynomial; the subdivision
`S(T)` has adjacency eigenvalues `±√μ_j` and zeros; Lemma 5.1 of
E. O. D. Andriantiana, V. Razanajatovo Misanantenaina, S. Wagner, *The
average size of matchings in graphs*, Graphs Combin. 36 (2020) 539–560
(arXiv:1903.09825), gives `avm(S(T)) = Σ_j μ_j/(1 + μ_j)`, and their
Theorem 4.4 says the path maximizes `avm` among trees of a given order. Since
`S(P_n) = P_{2n−1}`, T10 follows. This derivation is the auditor's; its two
classical steps were not checked against a source in the session. If it is
correct, T10 is a **known consequence** of a published theorem, and the
proof above is an independent, self-contained one.

## Lemma S46 (the value for the path)

**Lemma S46.** For `n ≥ 1`, with `r = φ^{−2}`,

`tr(I + L_{P_n})^{−1} = n/√5 + 2/5 + (2n/√5) r^{2n}/(1 − r^{2n}) > n/√5 + 2/5`.

*Proof.* The eigenvalues of `I + L_{P_n}` are `3 − 2cos θ_j`, `θ_j = jπ/n`,
`0 ≤ j ≤ n − 1`. Since `r² − 3r + 1 = 0`,
`1/(3 − 2cos θ) = r/(1 − 2r cos θ + r²) = (1/√5)(1 + 2Σ_{m≥1} r^m cos mθ)`
(Poisson kernel; `r/(1 − r²) = 1/(φ² − φ^{−2}) = 1/√5`), absolutely
convergent. Now `Σ_{j=0}^{n−1} cos(mθ_j)` is `n` if `2n | m`, `0` if `m` is
even and `2n ∤ m`, and `Re[(1 − e^{iπm})/(1 − e^{iπm/n})] = Re[2/(1 − e^{iπm/n})] = 1`
if `m` is odd (then `m/n` is not an even integer, so `e^{iπm/n} ≠ 1`, and
`Re[1/(1 − e^{iψ})] = 1/2` for `e^{iψ} ≠ 1`); this covers `n = 1` (one
eigenvalue, `1`). Summing,
`tr = (1/√5)[n + 2Σ_{m odd} r^m + 2nΣ_{l≥1} r^{2nl}]` and `2r/(1 − r²) = 2/√5`. ∎

The same value follows from Lemma 4.2 of Andriantiana–Misanantenaina–Wagner
(eq. (8), with `2n − 1` vertices), as the literature audit noted.

## Theorem T9 (the upper half) — proof

Let `n ≥ 3`, `x = n − n/√5` (irrational, since `√5` is) and
`K = ⌈x − 2/5⌉`; note `K ≤ ⌈x⌉ = M`. By S42, T10 and S46,

`μ_q ≤ n − tr(T) ≤ n − tr(P_n) < x − 2/5`.

By (D), applied to `q` (positive coefficients, real zeros), every
maximizing index `m_q` of `q_0, …, q_{n−1}` satisfies
`m_q < μ_q + 1 < (x − 2/5) + 1`; as `m_q` is an integer and `x − 2/5` is not,
`m_q ≤ K`.

If `K ≥ n − 2`, every maximizing index `p` of `d_0, …, d_{n−2}` satisfies
`p ≤ n − 2 ≤ K`. Otherwise `K ≤ n − 3`, and `q_{K+1} < q_K`: if not, the
ratios `t_j = q_{j+1}/q_j` being strictly decreasing (proof of S41),
`t_j > t_K ≥ 1` for `j < K`, so `q_0 < q_1 < … < q_K ≤ q_{K+1}` and some
maximizing index of `q` would be `≥ K + 1`. Lemma S41 with `k = K` then
gives `p ≤ K`. In both cases `p ≤ K ≤ M` and `p < x + 3/5`. ∎

**Corollaries.**
1. With Theorem T6(c) of [`lower-bound.md`](lower-bound.md) (a candidate
   proof of the lower half, MD-0019), **the Collins–Shor conjecture holds for
   every tree**: every maximizing index lies in `[⌊n/2⌋, ⌈n − n/√5⌉]`. Both
   halves are candidate proofs; neither is established.
2. The bound of T9 is a little sharper than the conjecture: `p ≤ K =
   ⌈n − n/√5 − 2/5⌉`, which is `⌊n − n/√5⌋` when the fractional part of
   `n − n/√5` is below `2/5`. It is consistent with the path: its peak can be
   `⌈n − n/√5⌉` only when that fractional part exceeds `2/5` (checked in the
   stored experiment, part C; in fact only when it exceeds `4/5`, Corollary
   S48 of [`path-peak.md`](path-peak.md), which also locates the peak of the
   path exactly).
3. For an individual tree, `p_max(T) < 1 + Σ_j μ_j/(1 + μ_j) = n + 1 − tr(I + L_T)^{−1}`.

## Remarks

- Where the earlier attempts failed. The cone order of sessions 9 to 12
  controls `λ_μ` only for `μ ≤ n/2` (`path-maximality.md`), and ratio
  dominance fails at the peak (MD-0021). Here the location of the peak is
  read off the *mean* of a real-rooted polynomial, which is additive over the
  spectrum, so extremality of a spectral sum (T10) is enough. Darroch's
  rule was set aside in session 7 for a different polynomial (`r_A`, at the
  lower central index); for `q` and the upper index it decides.
- The statement (PX-peak) of MD-0021 (the path has the largest peak) is not
  proved here; T9 does not need it.
- For the bound `p ≤ ⌈n − n/√5⌉` of the conjecture, `tr(I + L_T)^{−1} > n/√5`
  is enough (it gives `m_q < x + 1`, hence `m_q ≤ ⌈x⌉`, and then S41). The
  extra `2/5` of S46 is used only for the sharper `K = ⌈x − 2/5⌉`. T10 is
  stronger than either.

## Exact checks

Stored experiment `experiments/CJ-0001-collins-shor-peak/upper_bound.py`,
committed at `3b95386` with its test `tests/test_cj0001_upper_bound.py` and a
README entry; its result `results/upper-bound.json` records the command, the
revision and a clean tree in its provenance block (run at `917d657` on a clean
checkout, 299 s, 0 failures in every part). It checks exactly: T10 on
all trees of order 2 to 20; S46 (the inequality exactly for `n ≤ 200`, the
closed form to 50 digits for `n ≤ 60`); the bound `p < n − n/√5 + 3/5` of T9
on all trees of order 3 to 18 and on the path for `n ≤ 2000`; S45 on all
rooted trees with `2 ≤ |X| ≤ 8` and `j_1 + j_2 ≤ 8`; S44(iii) for `N ≤ 60`;
the trace formula of S43 on all pairs of rooted trees of order `≤ 6`; and, in
floating point (exploratory), S42 on all trees of order 3 to 14. The two
reviewers of `53421a6` made their own independent checks (their reports). Exploratory floating-point checks made
while the argument was found (scratch, not stored): on all trees of order
4 to 16, the peak of `d` never exceeds the mode of `q`, `μ_q ≤ n − tr(T)`,
and `tr(T) ≥ tr(P_n)`; Lemma S45 on all rooted trees of order 2 to 11 with
`j_1, j_2 ≤ 8`; formula (1) and (2) against matrix inverses for `N = 3, 6, 9`.
