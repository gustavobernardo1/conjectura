# CJ-0001 — lemmas and their proofs

Status of everything in this file: written by an AI agent (Claude, model
`claude-fable-5-2`) on 2026-11-26; **not independently reviewed**; novelty
**unknown** (these are elementary consequences of classical results and are
very likely known, at least implicitly). They are tools for the investigation,
not claimed results.

Notation. `T` is a tree of order `n ≥ 3`, `D` its distance matrix, `L` its
Laplacian, `τ = (2 − deg(v))_v`, `δ_k` the coefficient of `x^k` in
`det(D − xI)`, and `d_k = 2^{k−(n−2)} |δ_k|` for `0 ≤ k ≤ n−2`. By Fact 1.1 of
arXiv:1507.02341 (Graham–Lovász), `(−1)^{n−1} δ_k > 0` for `0 ≤ k ≤ n−2`, so
`d_k = 2^{k−(n−2)} (−1)^{n−1} δ_k > 0`. Put
`ℓ_T(x) = −2^{−(n−2)} det(2xI − D)`; then the coefficient of `x^k` in `ℓ_T` is
`d_k` for `0 ≤ k ≤ n−2` (Observation 3.1 of arXiv:1507.02341).

## R1. The conjecture as two inequalities

**Statement.** Let `m = ⌊n/2⌋` and `M = ⌈n − n/√5⌉`. Then

- every maximizing index of `d_0, …, d_{n−2}` is `≥ m` if and only if `d_{m−1} < d_m`;
- every maximizing index is `≤ M` if and only if `M ≥ n−2` or `d_{M+1} < d_M`.

**Proof.** The sequence is positive and log-concave (Theorem 2.1 of
arXiv:1507.02341). For a positive log-concave sequence the ratios
`d_{k+1}/d_k` are non-increasing in `k`. If `d_{m−1} < d_m`, the ratios are
`> 1` at every index `≤ m−1`, so the sequence is strictly increasing up to `m`
and no index below `m` is maximizing. If `d_{m−1} ≥ d_m`, the ratios are `≤ 1`
at every index `≥ m−1`, so the sequence is non-increasing from `m−1` on and its
maximum is attained at some index `≤ m−1`. The second claim is the first one
applied to the reversed sequence, which is also positive and log-concave. ∎

Note `m − 1 ≥ 0` and `m ≤ n − 2` for `n ≥ 3`, so the first inequality always
makes sense.

## L1. A Laplacian formula for the normalized coefficients

**Statement.** `ℓ_T(x) = (n−1) det(I + xL) − x · τᵀ adj(I + xL) τ`.

**Proof.** Two classical facts are used: `det D = (−1)^{n−1}(n−1)2^{n−2}`
(Graham–Pollak) and `D^{-1} = −L/2 + ττᵀ/(2(n−1))` (Graham–Lovász). Then

`det(2xI − D) = det(D) · det(2xD^{-1} − I) = det(D) · det(−(I + xL) + (x/(n−1)) ττᵀ)`.

By the matrix determinant lemma `det(A + uvᵀ) = det A + vᵀ adj(A) u`, applied
to `A = −(I + xL)` (so `det A = (−1)^n det(I + xL)` and
`adj A = (−1)^{n−1} adj(I + xL)`):

`det(−(I + xL) + (x/(n−1)) ττᵀ) = (−1)^n [det(I + xL) − (x/(n−1)) τᵀ adj(I + xL) τ]`.

Multiplying by `det D` and by `−2^{−(n−2)}` gives the statement. ∎

*Caveat on sources.* The inverse formula is quoted from memory of Graham and
Lovász (1978), which was not accessed in this session. As a safeguard, L1 was
checked exactly against the direct computation of `det(D − xI)` on every tree
of order 3 to 9 and on the two order-20 trees of the refutation below
(`tests/test_cj0001_distpoly.py`).

*Checks.* The coefficient of `x^n` is `−τᵀ adj(L) τ = −(Σ τ_v)² = −4`, since
`adj(L) = J` for a tree and `Σ τ_v = 2n − 2(n−1) = 2`. This agrees with
Observation 3.1 of arXiv:1507.02341. The constant term is `n − 1`, in agreement
with Graham–Pollak.

## L2. The coefficient d_1 and its extremal trees

**Statement.** `d_1(T) = 2n² − 6 − Σ_v deg(v)²`. Consequently, for every tree
`T` of order `n`,

`(n+3)(n−2) = d_1(S_n) ≤ d_1(T) ≤ d_1(P_n) = 2n(n−2)`,

with equality on the left only for the star and on the right only for the path.
Since `d_0(T) = n − 1` for every tree, the same inequalities hold for the ratio
`ρ_0 = d_1/d_0`.

**Proof.** In L1 the coefficient of `x` is `(n−1) tr(L) − τᵀ τ`, because
`det(I + xL) = 1 + x tr(L) + …` and `adj(I + xL) = I + …`. Here
`tr(L) = Σ deg(v) = 2(n−1)` and
`τᵀτ = Σ (2 − deg v)² = 4n − 8(n−1) + Σ deg(v)²`. Hence
`d_1 = 2(n−1)² − 4n + 8(n−1) − Σ deg² = 2n² − 6 − Σ deg(v)²`.

For the extremes write `e_v = deg(v) − 1 ≥ 0`; then `Σ e_v = n − 2` and
`Σ deg(v)² = Σ e_v² + 2 Σ e_v + n = Σ e_v² + 3n − 4`. For non-negative integers,
`Σ e_v ≤ Σ e_v² ≤ (Σ e_v)²`; the left equality holds iff every `e_v ∈ {0,1}`,
i.e. the maximum degree is at most 2, i.e. `T` is a path; the right equality
holds iff a single `e_v` is non-zero, i.e. `T` is a star. So
`4n − 6 ≤ Σ deg² ≤ n² − n`, and the claim follows. ∎

*Check.* Exact agreement on every tree of order 3 to 11
(`test_d1_formula_first_zagreb_index`). *Relation to the literature.* Theorem
3.3 of arXiv:1507.02341 bounds the peak through the number of paths of length 2,
which is `Σ_v C(deg v, 2)`; L2 is the same information in another form.

## L3. Caterpillars through a quotient matrix

**Statement.** Let `T` be a caterpillar whose spine `v_1, …, v_s` is a path and
whose spine vertex `v_i` carries `c_i ≥ 1` pendant leaves (`n = s + Σ c_i`). Let
`Q` be the `2s × 2s` matrix with blocks, for `1 ≤ i, j ≤ s`,

- spine–spine: `|i − j|`;
- spine–leaf class: `(|i − j| + 1) c_j`;
- leaf class–spine: `|i − j| + 1`;
- leaf class–leaf class: `(|i − j| + 2) c_j` if `i ≠ j`, and `2(c_i − 1)` if `i = j`.

Then `det(xI − D) = (x + 2)^{n−2s} det(xI − Q)`, hence
`ℓ_T(x) = −2^{−(2s−2)} (x + 1)^{n−2s} det(2xI − Q)` and each `d_k` is a
combination of at most `2s + 1` binomial coefficients `C(n − 2s, k − j)`.

**Proof.** The partition of the vertices into the `s` singletons `{v_i}` and the
`s` leaf classes is equitable for `D`: the sum of the distances from a vertex to
the vertices of a class depends only on the class of the vertex, and these sums
are the entries of `Q`. Vectors constant on classes form a `D`-invariant
subspace on which `D` acts as `Q`. Its orthogonal complement is spanned by
vectors supported on one leaf class with entries summing to zero; two leaves of
the same class are at distance 2 and have equal distances to every other
vertex, so `D` acts on such a vector as `2(J − I)`, i.e. as multiplication by
`−2`. The complement has dimension `Σ (c_i − 1) = n − 2s`. ∎

*Check.* Exact agreement with the direct `n × n` computation on six caterpillars
(`near_star_families.py`, validation step).
