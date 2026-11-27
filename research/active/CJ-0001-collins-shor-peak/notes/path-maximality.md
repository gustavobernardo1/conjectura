# CJ-0001 — the generalized tree shift in the cone order, and path maximality

Status of this file: written by an AI agent (Claude, model `claude-opus-5-5`)
on 2026-11-26, session 12. **Draft**: session 12 was stopped (at the director's
request) before this note was reread, stored with its computation or
reviewed; see the journal entry of session 12. Lemma S37, Proposition S38, Lemma S39 and
Theorems T7 and T8 have written proofs below; the proof of Lemma S37 uses one
finite exact computation (stated, with its command). **Nothing here is an
established result**: a statement counts as reviewed only where a report under
[`../reviews/`](../reviews/) names this file and its revision. Nothing here is
a claim of novelty. Everything here rests on the candidate results of
[`lower-bound.md`](lower-bound.md) (MD-0019) and on Proposition S19 of
[`rooted-calculus.md`](rooted-calculus.md) (MD-0015).

What this file does. Theorem T6(b) of `lower-bound.md` puts the star at the
bottom of the cone order on the polynomials `ℓ_T` of the trees of order `n`.
This file puts the path at the top (Theorem T8), so that for every tree

`ℓ_{S_n} ≤ ℓ_T ≤ ℓ_{P_n}` in the order `f ≤ g ⇔ g − f ∈ C_{n−1}`,

and in particular `d_k(S_n) ≤ d_k(T) ≤ d_k(P_n)` for every `k`. The tool is
Csikvári's generalized tree shift (P. Csikvári, *On a poset of trees*,
Combinatorica 30 (2010); *On a poset of trees II*, J. Graph Theory 74 (2013);
the second was read in part by the literature audit of session 11, see the
dossier). The operation of Proposition S36 of `lower-bound.md` is its case of
a path of length one. Theorem T7 says that every shift lowers `ℓ` in the cone
order, with an explicit formula for the difference (Lemma S37).

## Notation

That of `lower-bound.md`: a rooted tree `(A, u)` has weight zero, order `a`,
state `(Ψ, H, G, Ω, E)` with `E = R − Ω + (1+2x)²Ψ − 2xG`; `Ĝ := G/x` (a
polynomial, S33(c)); the cones `K_d`, `C_d`, the properties (K2), (K4) and
Lemma K; `ℓ_T`, `d_k`, `λ_μ`. Plant and merge are the operations of
`rooted-calculus.md` (S19) with all weights zero; `•` is the single vertex.

For `j ≥ 0` let `a_j` be the determinant of the `j × j` tridiagonal matrix with
`1 + 2x` on the diagonal and `−x` next to it (`a_0 = 1`), so that
`a_j = (1+2x)a_{j−1} − x²a_{j−2}` and `Σ_j a_j t^j = 1/Q(t)`,
`Q(t) = 1 − (1+2x)t + x²t²`. For `k ≥ 1` put

`γ_k = Σ_{i=0}^{k−1} x^i a_{k−1−i}`,  `γ_0 = 0`,
`ρ_k = x Σ_{i=0}^{k−2} (i+1)(k−1−i) x^i a_{k−2−i}`.

**The generalized tree shift.** Let `(A, u)` and `(B, v)` be rooted trees and
`k ≥ 1`. `T_k(A, B)` is `A` and `B` joined by a path of length `k` from `u` to
`v` (its `k − 1` inner vertices are new and have degree 2). `T′_k(A, B)` is
`A` and `B` glued at `u = v`, with a new pendant path of length `k` attached at
the glued vertex. Both have order `n = a + b + k − 1`. Passing from `T_k` to
`T′_k` is Csikvári's generalized tree shift for the path from `u` to `v` (all
neighbours of `v` off the path are moved to `u`); for `k = 1` it is the
operation of S36. In the rooted calculus,

`T_k = merge(plant^k(A, u), (B, v))`,  `T′_k = merge(merge((A, u), (B, v)), plant^k(•))`,

because planting `k` times grows a path of length `k` from `u` whose far end
becomes the root, and merging identifies roots.

## Lemma S37 (the difference under a shift)

**Lemma S37.** For rooted trees `(A, u)`, `(B, v)` and every `k ≥ 1`,

`ℓ_{T_k} − ℓ_{T′_k} = a_{k−1}(H_AE_B + E_AH_B) + 2xγ_k Ĝ_AĜ_B + 2x²γ_{k−1}(H_AĜ_B + Ĝ_AH_B) + x[2(1+x)γ_k + 3x a_{k−1} + ρ_k] H_AH_B`.

For `k = 1` this is Proposition S36 (`a_0 = 1`, `γ_1 = 1`, `γ_0 = ρ_1 = 0`).

*Proof.* By S34(b), plant is a linear map of the state, `s ↦ Ps`, with

```
Ψ' = (1+x)Ψ + xH,   H' = Ψ + xH,   G' = x²H + xG,
Ω' = E + (1+x)Ω + x(1+x)H,   E' = xE + xΩ + 2xG + x²(3+2x)H;
```

by S34(c), merge is a bilinear map `m(s, s′)` of the two states; and by S23(a)
and the definition of `E`, `xℓ = λ(s) := E + Ω + 2xG + x(1+4x)H − 4x²Ψ`
(`R = E + Ω − (1+2x)²Ψ + 2xG` and `Φ = Ψ + xH`). Hence

`Δ_k := x(ℓ_{T_k} − ℓ_{T′_k}) = λ(m(P^k s_A, s_B)) − λ(m(m(s_A, s_B), P^k e))`,

`e = (1, 0, 0, 0, 0)` the state of `•`. This also holds for `k = 0` with
`Δ_0 = 0`, since merging with `•` changes no state.

*Generating functions.* `Σ_{k≥0} P^k t^k = (I − tP)^{−1} = adj(I − tP)/det(I − tP)`
as formal power series in `t` with coefficients in `ℤ[x]`, and `λ`, `m` are
(bi)linear with coefficients independent of `t`, so
`F(t) := Σ_k Δ_k t^k = L(t)/det(I − tP)` with `L` a polynomial in `t` of degree
at most 4 (the entries of the adjugate of a `5 × 5` matrix linear in `t`). In
the order `(Ψ, H | G | Ω, E)` the matrix `P` is block lower triangular with
diagonal blocks `[[1+x, x], [1, x]]`, `(x)`, `[[1+x, 1], [x, x]]`, each
`2 × 2` block having trace `1 + 2x` and determinant `x²`; so
`det(I − tP) = (1 − xt)Q(t)²`.

Let `C(t) := Σ_{k≥1} c_k t^k`, `c_k` being `x` times the right side of the
lemma. With `Σ_{k≥1} a_{k−1}t^k = t/Q`, `Σ_{k≥1} γ_k t^k = t/((1 − xt)Q)`,
`Σ_{k≥1} γ_{k−1}t^k = t²/((1 − xt)Q)` and
`Σ_{k≥1} ρ_k t^k = x t²(Q − tQ′)/((1 − xt)²Q²)` (`Q′ = dQ/dt`; the convolution
of `(i+1)x^i` with `(j+1)a_j`), `C` is a sum of these four functions with
coefficients that do not depend on `t`. Put `D = (1 − xt)²Q²` (degree 6). Then
`N := D(F − C)` is a polynomial in `t`: `DF = (1 − xt)L` has degree at most 5,
and the four contributions to `DC` are `t(1 − xt)²Q`, `t(1 − xt)Q`,
`t²(1 − xt)Q` and `x t²(Q − tQ′)` times constants, of degree at most 5. So
`deg N ≤ 5`, and `N = 0` as soon as the coefficients of `t^0, …, t^5` in
`F − C` vanish, that is as soon as `Δ_k = c_k` for `0 ≤ k ≤ 5` (both sides are
`0` at `k = 0`). That finite identity — in the free variables `Ψ_A, …, E_B`,
which is more than needed — was checked by exact symbolic computation for
`k = 1, …, 12`; and `F = C` was also checked directly as an identity of
rational functions (command below). Dividing `Δ_k = c_k` by `x` gives the
lemma. ∎

*Computation.* `experiments/CJ-0001-collins-shor-peak/tree_shift_symbolic.py`
(the scratch script of session 12, saved as it ran; sympy 1.14.0, exact
rational arithmetic; command `uv run --with sympy==1.14.0 python
experiments/CJ-0001-collins-shor-peak/tree_shift_symbolic.py`) checks
`F = C` as an identity of rational functions, and the series of `1/Q` and
of the generating function of `ρ_k` against their definitions up to `t^8`.
The check `Δ_k = c_k` for `k = 1, …, 12` is the scratch computation of
session 11 (its code is in the journal entry of session 11). **Owed:** a
stored experiment with a test and a README entry that also checks the
factorization of `det(I − tP)` and the lemma on actual trees, with `ℓ`
taken from the distance matrix.

## Proposition S38 (each term is in the cone)

**Proposition S38.** If `a, b ≥ 2` and `k ≥ 1`, each of the four terms on the
right of Lemma S37 is in `K_{n−1}`, `n = a + b + k − 1`.

*Proof.* `a_j = Φ(P_j, e_1 + e_j)`: in `I + x(L_{P_j} + diag(e_1 + e_j))` every
diagonal entry is `1 + 2x` (inner vertices have degree 2, the two ends degree
1 and weight 1; for `j = 1` the single vertex has weight 2) and the entries
next to the diagonal are `−x`. The weight is not zero, so `a_j ∈ K_j` by
Lemma K (`a_0 = 1 ∈ K_0`). By (K2), `x^i a_{k−1−i} ∈ K_{k−1+i} ⊆ K_{k−1}`, so
`γ_k ∈ K_{k−1}` for `k ≥ 1` and `γ_{k−1} ∈ K_{k−2}` for `k ≥ 2` (`γ_0 = 0`);
and `x·x^{i+1}a_{k−2−i} ∈ K_{k+2+i} ⊆ K_{k+2}`, so `xρ_k ∈ K_{k+2}`.

By S33 and Theorem T5 of `lower-bound.md`: `H_A ∈ K_{a−2}`, `Ĝ_A ∈ K_{a−1}`,
`E_A ∈ K_{a+1}`, and the same for `B`. With (K2), and `n − 1 = a + b + k − 2`:

- `a_{k−1}H_AE_B ∈ K_{(k−1)+(a−2)+(b+1)} = K_{n−1}`, and the same for `E_AH_B`;
- `2xγ_kĜ_AĜ_B ∈ K_{2+(k−1)+(a−1)+(b−1)} = K_n`;
- `2x²γ_{k−1}H_AĜ_B ∈ K_{4+(k−2)+(a−2)+(b−1)} = K_{n}` (zero if `k = 1`);
- `x·2(1+x)γ_kH_AH_B ∈ K_{2+1+(k−1)+(a−2)+(b−2)} = K_{n−1}`;
  `x·3x a_{k−1}H_AH_B ∈ K_{4+(k−1)+(a−2)+(b−2)} = K_{n}`;
  `xρ_kH_AH_B ∈ K_{(k+2)+(a−2)+(b−2)} = K_{n−1}`;

and `K_n ⊆ K_{n−1}`. ∎

## Theorem T7 (a shift lowers `ℓ` in the cone order)

**Theorem T7.** Let `(A, u)`, `(B, v)` be rooted trees with `a, b ≥ 2` and
`k ≥ 1`, and `n = a + b + k − 1`. Then `ℓ_{T_k} − ℓ_{T′_k} ∈ C_{n−1}`. In
particular `d_j(T_k) ≥ d_j(T′_k)` for `0 ≤ j ≤ n − 2`, and
`d_μ(T_k) − d_{μ−1}(T_k) ≥ d_μ(T′_k) − d_{μ−1}(T′_k)` for `1 ≤ μ ≤ ⌊n/2⌋`.

*Proof.* By Lemma S37 and Proposition S38 the difference is in `K_{n−1}`. The
coefficients of `x^n` and `x^{n−1}` in `ℓ` are `−4` and `0` for every tree of
order `n`, so the difference has degree at most `n − 2` and is in `C_{n−1}` by
(K4). Elements of `K_{n−1}` have non-negative coefficients; and for
`μ ≤ ⌊n/2⌋`, `K_{n−1} ⊆ K_{2μ−1}`, where `λ_μ ≥ 0` (Lemma A(a)); `μ ≤ n − 2`
when `n ≥ 3`, so `λ_μ` reads `d_μ − d_{μ−1}`. ∎

(If `a = 1` or `b = 1` the shift does not change the tree, and the right side
of Lemma S37 is `0`: `H = G = E = 0` for the single vertex.)

## Lemma S39 (every tree but the path is the result of a shift)

**Lemma S39.** Let `T′` be a tree of order `n` that is not a path. Then there
are rooted trees `(A, u)`, `(B, v)` with `a, b ≥ 2` and `k ≥ 1` such that
`T′ ≅ T′_k(A, B)`, and `T_k(A, B)` has exactly one leaf fewer than `T′`.

*Proof.* Take a leaf `w` of `T′` and walk from `w` along vertices of degree 2
until the first vertex `z` of degree at least 3; it exists, since otherwise
the walk would exhaust a tree all of whose vertices have degree at most 2,
that is a path. The walk is a pendant path of length `k ≥ 1` from `z` to `w`.
`z` has at least two neighbours off this path; split them into two non-empty
sets `N_1`, `N_2`, let `A` be `z` together with the components of `T′ − z`
that contain a vertex of `N_1`, rooted at `u = z`, and `B` the same for `N_2`,
rooted at `v = z`. Then `a, b ≥ 2` and `T′ = T′_k(A, B)`.

In `T′` the leaves are `w`, the leaves of `A` other than `z`, and the leaves
of `B` other than `z` (`z` has degree at least 3). In `T_k(A, B)` the ends of
the path have degree `deg_A(u) + 1 ≥ 2` and `deg_B(v) + 1 ≥ 2`, its inner
vertices degree 2, and every other vertex keeps its degree; so the leaves are
those of `A` other than `u` and those of `B` other than `v`. ∎

## Theorem T8 (path maximality)

**Theorem T8.** For every tree `T` of order `n ≥ 2`: `ℓ_{P_n} − ℓ_T ∈ C_{n−1}`.
Together with Theorem T6(b) of `lower-bound.md`,

`ℓ_T − ℓ_{S_n} ∈ C_{n−1}` and `ℓ_{P_n} − ℓ_T ∈ C_{n−1}`.

In particular, for `0 ≤ k ≤ n − 2`, `d_k(S_n) ≤ d_k(T) ≤ d_k(P_n)`; and for
`n ≥ 3` and `1 ≤ μ ≤ ⌊n/2⌋`,
`d_μ(S_n) − d_{μ−1}(S_n) ≤ d_μ(T) − d_{μ−1}(T) ≤ d_μ(P_n) − d_{μ−1}(P_n)`.

*Proof.* Induction on the number of leaves of `T`. A tree with two leaves is
the path. If `T` has more, Lemma S39 gives `T ≅ T′_k(A, B)` with
`T_0 := T_k(A, B)` of order `n` with one leaf fewer, and Theorem T7 gives
`ℓ_{T_0} − ℓ_T ∈ C_{n−1}`; by induction `ℓ_{P_n} − ℓ_{T_0} ∈ C_{n−1}`, and
`C_{n−1}` is closed under addition. The inequalities follow as in Theorem T7.
(`n = 2`: the only tree is the path.) ∎

**Remarks.** 1. The equality cases are not determined here. Exact
computation (below) found no tree other than `P_n` with `ℓ_T = ℓ_{P_n}` for
`n ≤ 17`.

2. The interval `[ℓ_{S_n}, ℓ_{P_n}]` of the cone order does not locate the
peak: the cone controls `λ_μ` only for `μ ≤ n/2` (Lemma A), while the upper
half of the conjecture concerns `μ = M + 1 > n/2`. Along a shift the ratio
`d_{j+1}/d_j` is not monotone for `j ≥ ⌊n/2⌋` (session 11, scratch), but in
every case computed the largest maximizing index did not increase
(observation (PM) of `STATE.md`; not proved).

3. For the Laplacian and the adjacency (matching) polynomials the analogous
extremality of the star and the path, and the monotonicity along the shift,
are theorems of Zhou–Gutman, Mohar and Csikvári (dossier, audit of session
11). No version for the distance characteristic polynomial was found in that
audit's coverage; originality is not established.

## Exact checks

Not yet stored (see the Computation paragraph of Lemma S37). The scratch
runs of session 11 found: Theorem T7's conclusion on every tree of order 5 to 13 and every shift
(no failure), and Theorem T8's on the 81,134 trees of order 4 to 17. These are
finite checks; the proofs above do not depend on them, except for the finite
identity in the proof of Lemma S37.
