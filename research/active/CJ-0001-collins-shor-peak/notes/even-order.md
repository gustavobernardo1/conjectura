# CJ-0001 — the even orders: a rooted form, the leaf polynomial, and the remainder `Ω_T`

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 10. Propositions S28, S29 and S30 have written proofs
below; **none has been reviewed** unless a report under
[`../reviews/`](../reviews/) names this file. Statement (SM⁺) is a
**conjecture** supported by exact finite computation only. Finding S31 is a
computation. Nothing here is a claim of novelty, and **the lower bound
`⌊n/2⌋` of the Collins–Shor conjecture for trees of even order is not proved
here**: it is reduced to an inequality for one polynomial, `Ω_T`.

Notation and tools: those of [`wiener-form.md`](wiener-form.md) (revision of
session 10): `M = I + xL`, `Φ = det M`, `ℓ_T`, L1, identity (1)
(`Lδ_c = τ − 2e_c`), the cones `K_d` with (K2), Lemma K with identity (K3),
Lemma S24, Lemma A, `λ_m(f) = [x^m]f − [x^{m−1}]f`. In addition, for a set
`S` of vertices of a tree `T`,

`Π_S := det M[V ∖ S]`  (`Π_∅ = Φ`, `Π_V = 1`),  `Ψ_c := Π_{{c}}`,

and for two vertices `u, v`, `Π_{uv} = Π_{path(u,v)}` as in Lemma S24. We write
`Π_{S}(T)` when the tree must be named. `Cat_k = C(2k, k)/(k+1)`.

**(P)** If `S ≠ ∅`, then `Π_S ∈ K_{n−|S|}`. Indeed `M[V ∖ S]` is block
diagonal over the components `K` of `T − S`, with blocks
`I + x(L_K + diag ν_K)`, `ν_K(w)` the number of neighbours of `w` in `S`
(the degree of `w` in `T` is its degree in `K` plus `ν_K(w)`); `T` is
connected and `S ≠ ∅`, so every component has a vertex adjacent to `S` and
`ν_K ≠ 0`; Lemma K gives `Φ(K, ν_K) ∈ K_{|K|}`, and (K2) the product.

L1 holds for every tree of order `n ≥ 1`: for `n ≥ 2` it is the statement of
[`lemmas.md`](lemmas.md) (the derivation there needs only that `D` is
invertible; for `n = 2` both sides are `1 − 4x²`), and for `n = 1`,
`ℓ_T = −2·det(2x) = −4x` and `(n−1)Φ − xτᵀadj(M)τ = −x·2·1·2 = −4x`.

## Proposition S28 (the rooted form)

**Proposition S28.** Let `T` be a tree of order `n ≥ 1`, `c` a vertex, and
`δ_v = dist(c, v)`. Then

`ℓ_T = Σ_{e ∈ E} Π_e + 4 Σ_{v ≠ c} δ_v x^{δ_v} Π_{cv} − 4x Ψ_c + Σ_{u<v, dist(u,v) ≥ 2} (δ_u − δ_v)² x^{dist(u,v)−1} Π_{uv}`.

*Proof.* As in Proposition S25, for real `x > 0` and `G = M^{−1}` (symmetric,
`G1 = 1`, `xLG = xGL = I − G`). By identity (1), `τ = Lδ + 2e_c`, so

`x τᵀGτ = x δᵀLGLδ + 4x e_cᵀGLδ + 4x G_{cc}`.

`x δᵀLGLδ = δᵀ(I − G)Lδ = δᵀLδ − (δᵀδ − δᵀGδ)/x`, and `δᵀLδ = n − 1` (each
edge contributes `1`). `4x e_cᵀGLδ = 4 e_cᵀ(I − G)δ = −4 Σ_v G_{cv} δ_v`
(`δ_c = 0`). By L1,

`ℓ_T/Φ = (n−1) − x τᵀGτ = (δᵀδ − δᵀGδ)/x + 4 Σ_v δ_v G_{cv} − 4x G_{cc}`.

`δᵀδ − δᵀGδ = Σ_{u<v} G_{uv}(δ_u − δ_v)²` (symmetry and unit row sums).
Multiply by `Φ` and use `ΦG_{uv} = x^{dist(u,v)} Π_{uv}` (Lemma S24):
`ℓ_T = Σ_{u<v} (δ_u − δ_v)² x^{dist(u,v)−1} Π_{uv} + 4 Σ_{v≠c} δ_v x^{δ_v} Π_{cv} − 4xΨ_c`.
For an edge `uv`, `(δ_u − δ_v)² = 1`. ∎

**Remark.** This is the case `π = e_c` of a family: for a real vector `π` with
`1ᵀπ = 1` and `f = Dπ` one has `Lf = τ − 2π`, and the same computation gives
`ℓ_T = −2(πᵀDπ)Φ + (1/x) Σ_{u<v} (f_u − f_v)² adj_{uv} + 4 πᵀ adj f − 4x πᵀ adj π`.
The uniform `π` is the Wiener form (S25); `π = τ/2` gives `f` constant and
returns L1. Only the cases `π = e_c` (here) and `π = 1/n` (S25) are checked
by machine.

## Proposition S29 (the leaf polynomial)

For a tree `T` and a vertex `c`, let `T⁺` be `T` with a new pendant vertex `w`
attached at `c`, and define

`r_c(T) := ℓ_{T⁺} − (1+x) ℓ_T`,  `Ω_c(T) := r_c(T) − (1+4x) Ψ_c(T)`.

(By Proposition S23(b) of [`leaf-telescoping.md`](leaf-telescoping.md), which
is unreviewed, these are the `r_u` and `Ω_u` of that note; nothing below uses
that identification.)

**Proposition S29.** With `δ_v = dist(c, v)` in `T`,

`r_c(T) = (1+4x) Ψ_c + x Σ_{e ∈ E, c ∉ e} Π_{e ∪ c} + Σ_{a<b, dist(a,b) ≥ 2, c ∉ path(a,b)} (δ_a − δ_b)² x^{dist(a,b)} Π_{path(a,b) ∪ c} + Σ_{a: δ_a ≥ 2} (δ_a − 1)² x^{δ_a} Π_{path(a,c)}`.

In particular `Ω_c(T)` has non-negative coefficients.

*Proof.* Write `Π⁺` for the polynomials of `T⁺` and `M⁺ = I + xL_{T⁺}`. On
`V`, `M⁺` is `M + x e_c e_cᵀ`; the row of `w` has `1 + x` at `w` and `−x` at
`c`. For `S ⊆ V`:

- (i) if `c ∈ S`: `M⁺[V⁺ ∖ S]` is block diagonal with the block `(1+x)` of
  `w` and `M[V ∖ S]`, so `Π⁺_S = (1+x) Π_S`;
- (ii) if `c ∉ S`: expanding along the row of `w`, and using linearity in the
  row of `c`,
  `Π⁺_S = (1+x)(Π_S + xΠ_{S∪c}) − x²Π_{S∪c} = (1+x)Π_S + xΠ_{S∪c}`;
- (iii) `Π⁺_{S ∪ w} = Π_S` if `c ∈ S` (the vertex `w` is removed and `c` with
  it).

Apply Proposition S28 to `T⁺` with the root `c` (`δ_w = 1`, the other
distances unchanged). The pairs of `T⁺` are the pairs of `T` and the pairs
`{a, w}`, `a ∈ V`, with `dist(a, w) = δ_a + 1` and `path(a, w) = path(a, c) ∪ w`:

`ℓ_{T⁺} = Σ_{e∈E} Π⁺_e + Π⁺_{cw} + 4 Σ_{v∈V∖c} δ_v x^{δ_v} Π⁺_{cv} + 4x Π⁺_{cw} − 4x Π⁺_{{c}} + Σ_{u<v in V, dist ≥ 2} (δ_u − δ_v)² x^{dist−1} Π⁺_{uv} + Σ_{a ∈ V∖c} (δ_a − 1)² x^{δ_a} Π⁺_{path(a,c) ∪ w}`.

By (iii), `Π⁺_{cw} = Ψ_c` and `Π⁺_{path(a,c)∪w} = Π_{path(a,c)}`; by (i),
`Π⁺_{{c}} = (1+x)Ψ_c` and `Π⁺_{cv} = (1+x)Π_{cv}`; by (i) and (ii), for an
edge or a path `S` of `T`, `Π⁺_S = (1+x)Π_S + [c ∉ S]·xΠ_{S∪c}`. Subtracting
`(1+x)ℓ_T`, written by Proposition S28 with the same root, everything that
carries the factor `(1+x)` cancels except `−4x(1+x)Ψ_c` against itself, and
what remains is the formula (the terms with `δ_a = 1` in the last sum
vanish). ∎

## Proposition S30 (the remainder `Ω_T` and the even orders)

Let `T` be a tree of order `n ≥ 1` and
`Θ_T := (Φ_T − (1+x)^{n−1})/x` (a polynomial: `Φ_T(0) = 1`),

`Ω_T := ℓ_T + 4x(1+x)^{n−1} − (1+4x) Θ_T`,  so that  `ℓ_T = (1+4x)Θ_T − 4x(1+x)^{n−1} + Ω_T`.

Call an edge `e` of a tree **deep** with respect to a vertex `c` if both its
ends are at distance at least `2` from `c`.

**Proposition S30.** Let `T_1 ⊂ T_2 ⊂ … ⊂ T_n = T` be subtrees with
`|T_k| = k`, `T_{k+1}` being `T_k` with a pendant vertex attached at `u_k`.

(a) `Θ_T = Σ_{k=1}^{n−1} (1+x)^{n−1−k} Ψ_{u_k}(T_k)` and
`Ω_T = Σ_{k=1}^{n−1} (1+x)^{n−1−k} Ω_{u_k}(T_k)`. The right sides do not
depend on the construction chosen.

(b) `Ω_T` has non-negative coefficients, and

`Ω_T − x Σ_{k=1}^{n−1} (1+x)^{n−1−k} Σ_{e deep in T_k w.r.t. u_k} Π_{e ∪ u_k}(T_k) ∈ K_{n−1}`,

the subtracted sum being in `K_{n−2}`. In particular `Ω_T ∈ K_{n−2}`, and
`Ω_T ∈ K_{n−1}` if `T` has a construction without deep edges.

(c) `Θ_T − (n−1)(1+x)^{n−2} ∈ K_{n−2}` (for `n ≥ 2`).

(d) If `n = 2m ≥ 4` is even, then

`d_m(T) − d_{m−1}(T) ≥ (n−1)(3m−5)/(m+1) · Cat_{m−1} + λ_m(Ω_T)`,

with equality for the star, for which `Ω_T = 0`. Consequently, **for a tree
of even order `n = 2m ≥ 4`, `λ_m(Ω_T) > −(n−1)(3m−5)/(m+1)·Cat_{m−1}` implies
`d_{m−1} < d_m`** (the lower bound `⌊n/2⌋` of the conjecture for `T`, by R1);
it is enough that `λ_m(Ω_T) ≥ 0`, and by (b) only the deep-edge terms can
make `λ_m(Ω_T)` negative.

*Proof.* (a) By the definition of `r`, `ℓ_{T_{k+1}} = (1+x)ℓ_{T_k} + r_{u_k}(T_k)`,
and `ℓ_{T_1} = −4x`; so
`ℓ_T = −4x(1+x)^{n−1} + Σ_k (1+x)^{n−1−k} r_{u_k}(T_k)`. By the proof of
Proposition S26, `Φ_{T_{k+1}} = (1+x)Φ_{T_k} + xΨ_{u_k}(T_k)`, and `Φ_{T_1} = 1`;
so `Φ_T = (1+x)^{n−1} + x Σ_k (1+x)^{n−1−k} Ψ_{u_k}(T_k)`, which is the formula
for `Θ_T`. Substituting `r = (1+4x)Ψ + Ω` gives
`ℓ_T = −4x(1+x)^{n−1} + (1+4x)Θ_T + Σ_k (1+x)^{n−1−k} Ω_{u_k}(T_k)`, and the
last sum is `Ω_T` by the definition of `Ω_T`. `Θ_T` and `Ω_T` are defined
without reference to the construction.

(b) By Proposition S29, for a tree `B` of order `k` and a vertex `c`,
`Ω_c(B)` is the sum of: `xΠ_{e∪c}` over the edges `e ∌ c`; the pair terms
`(δ_a − δ_b)² x^d Π_{path(a,b)∪c}`, `d = dist(a,b) ≥ 2`; and
`(δ_a − 1)² x^{δ_a} Π_{path(a,c)}`, `δ_a ≥ 2`. All have non-negative
coefficients (each `Π_S` is a product of polynomials in cones `K_j`, by (P)).
By (P) and (K2): `xΠ_{e∪c} ∈ K_{2 + k − 3} = K_{k−1}`; a pair term is in
`K_{2d + k − (d+2)} = K_{k+d−2} ⊆ K_k`; a term of the last sum is in
`K_{2δ_a + k − (δ_a+1)} = K_{k+δ_a−1} ⊆ K_{k+1}`. An edge `e = ab ∌ c` that is
not deep has an end `a` adjacent to `c` and its other end `b` at distance `2`
with `path(b, c) = e ∪ c`; the term `a := b` of the last sum is `x²Π_{e∪c}`,
and `xΠ_{e∪c} + x²Π_{e∪c} = x(1+x)Π_{e∪c} ∈ K_{3 + k − 3} = K_k`; distinct such
edges use distinct terms of the last sum, and the terms left over are in
`K_k`. Hence `Ω_c(B) − x Σ_{e deep} Π_{e∪c} ∈ K_k` and the subtracted sum is in
`K_{k−1}`. Multiply by `(1+x)^{n−1−k}` and sum over `k` ((a) and (K2)).

(c) First, for a tree `K` on `j ≥ 1` vertices and a vertex `a`:
`Φ(K, e_a) − (1+x)^j ∈ K_j`. Induction on `j`; for `j = 1` it is `0`. For
`j ≥ 2` take a leaf `w ≠ a`, with neighbour `u`; identity (K3) with `ν = e_a`,
`ν_w = 0` reads `Φ(K, e_a) = (1+x)Φ(K − w, e_a) + xΨ` with `xΨ ∈ K_j` (as in
the proof of Lemma K), so
`Φ(K, e_a) − (1+x)^j = (1+x)[Φ(K − w, e_a) − (1+x)^{j−1}] + xΨ ∈ K_j`.
Next, `Ψ_c(B) = Π_i Φ(K_i, e_{a_i})` over the components of `B − c`; writing
each factor as `(1+x)^{j_i} + B_i` with `B_i ∈ K_{j_i}` and expanding,
`Ψ_c(B) − (1+x)^{k−1} ∈ K_{k−1}` (`k = |B|`). By (a),
`Θ_T − (n−1)(1+x)^{n−2} = Σ_k (1+x)^{n−1−k} [Ψ_{u_k}(T_k) − (1+x)^{k−1}] ∈ K_{n−2}`.

(d) `m ≤ n − 2`, so `d_m − d_{m−1} = λ_m(ℓ_T) = λ_m((1+4x)Θ_T) − 4λ_m(x(1+x)^{n−1}) + λ_m(Ω_T)`.

For `g ∈ K_{2m−2}`: `(1+4x)g = (1+x)g + 3xg` with `(1+x)g ∈ K_{2m−1}` and
`xg ∈ K_{2m} ⊆ K_{2m−1}`, so `λ_m((1+4x)g) ≥ 0` by Lemma A(a). By (c),
`λ_m((1+4x)Θ_T) ≥ (n−1) λ_m((1+4x)(1+x)^{2m−2})`, and, as
`C(2m−2, m) = C(2m−2, m−2)`,
`λ_m((1+4x)(1+x)^{2m−2}) = 3[C(2m−2, m−1) − C(2m−2, m−2)] = 3 Cat_{m−1}`.

`λ_m(x(1+x)^{2m−1}) = C(2m−1, m−1) − C(2m−1, m−2) = C(2m−1, m−1)·2/(m+1)`,
and `C(2m−1, m−1) = (2m−1) Cat_{m−1}`; so
`4λ_m(x(1+x)^{n−1}) = 8(n−1) Cat_{m−1}/(m+1)`.

Together: `d_m − d_{m−1} ≥ (n−1)[3 − 8/(m+1)] Cat_{m−1} + λ_m(Ω_T)`, and
`3 − 8/(m+1) = (3m−5)/(m+1) > 0` for `m ≥ 2`. For the star built from its
centre every `T_k` is a star with centre `u_k`, so by Proposition S29
`Ω_{u_k}(T_k) = 0` (no edge avoids the centre and no vertex is at distance
`2`), `Ψ_{u_k}(T_k) = (1+x)^{k−1}`, and every inequality above is an
equality. ∎

**Remarks.** (1) Stars and double stars have constructions without deep
edges (centre or central edge first, then the leaves), so for them
`Ω_T ∈ K_{n−1}` and (d) gives `d_{m−1} < d_m` for even order; for double stars
this is contained in the candidate Theorem T1, proved differently. A tree of
diameter at least `4` has no such construction: when the second branch of
length `2` at a common vertex is completed, the edge at the end of the first
one is deep. (2) By (a) and Proposition S23(a) of `leaf-telescoping.md`
(unreviewed), `xΩ_T = R(T, 0) + (1+2x)²(1+x)^{n−1}`.

## Statement (SM⁺)

> **(SM⁺)** For every tree `T` of order `n ≥ 3`: `Ω_T ∈ C_{n−1}`.

(`Ω_T` has degree at most `n − 2`.) Exact for every tree of order 3 to the
bound in the result file (equality `Ω_T = 0` only for the star). Relations,
with the conjectures of `leaf-telescoping.md`:

`(Γ_c¹) ⇒ (SM⁺) ⇒ (SM)`,  and  `(SM⁺) ⇒ λ_m(Ω_T) ≥ 0 ⇒ d_{m−1} < d_m` for even `n = 2m ≥ 4` (S30(d)).

(Γ_c¹) puts each `Ω_{u_k}(T_k)` in `C_k` (proof of S27(c)), hence `Ω_T` in
`C_{n−1}` by S30(a). For (SM): by S30 and S23(d),
`ℓ_T − ℓ_{S_n} = (1+4x)[Θ_T − (n−1)(1+x)^{n−2}] + Ω_T`, and the bracket is in
`C_{n−2}` by S27(b) (the cone `C` version of S30(c)), with
`(1+4x)C_{n−2} ⊆ C_{n−1}`. These two implications rest on S23 and S27 of
`leaf-telescoping.md`, which are unreviewed; S30(d) does not.

(SM⁺) is not registered as a conjecture of its own: it is recorded as a
strengthening of (SM) (MD-0017), in the way (Γ_c¹) is.

## Finding S31 (inequality (3) of `wiener-form.md` is not enough)

Inequality (3) of `wiener-form.md` bounds `n²(d_m − d_{m−1})` from below, for
even `n = 2m`, by `λ_m(4(W − nx)Φ + Σ_{e ∈ E} (n − 2n_e)² Π_e)`, discarding
the pairs at distance at least `2`. Session 9 found this lower bound positive
for every tree of even order up to 14 and proposed to prove it positive in
general.

**It is not positive in general.** For the spider with `(n−2)/2` legs of
length `2` and one pendant vertex at the centre, the bound is positive for
the even orders up to `98` and **negative from `n = 100`** on the range
computed (two implementations: characteristic polynomials by python-flint,
and a recursion over the forest in pure Python integers; they agree at every
order; the range is in the result file). On the same trees `d_{m−1} < d_m`
holds (computed from the distance matrix): the conjecture is not affected,
only this route to it. A proof for even order through the Wiener form must
use the pairs at distance at least `3` (the pairs at distance `2` contribute
`(t_u − t_v)² xΠ_{uv}` with `xΠ_{uv} ∈ K_{n−1}`, on whose extreme generators
`λ_m` vanishes).

## What is not proved

The lower bound for even order. By S30 it is equivalent to nothing simpler
than itself, but it would follow from `λ_m(Ω_T) ≥ 0`, where `Ω_T` is an
explicit polynomial with non-negative coefficients, and the only terms of it
on which `λ_m` can be negative are the deep-edge terms
`x(1+x)^{n−1−k} Π_{e∪u_k}(T_k)`. No bound for these terms is proved here. The
level count that settles the odd orders does not settle them: the terms of
`Ω_T` that could compensate, at level `n` or higher, are the pair terms with
`dist ≥ 3` and the terms `x^{δ_a}Π_{path(a,c)}` with `δ_a ≥ 3`, and a term by
term comparison with one deep edge fails when the vertices near the edge
have large degree (hand estimate of session 10, not written out).

## Verification by computation

`experiments/CJ-0001-collins-shor-peak/even_order.py` (exact integers),
result file `results/even-order.json`. Part A: Propositions S28 and S29 for
every tree and every root up to the order in the file, with `ℓ_T` and
`ℓ_{T⁺}` taken from the characteristic polynomials of the distance matrices.
Part B: `Ω_T` has non-negative coefficients (S30(b)), (SM⁺), and S30(c) in
the cone `C_{n−2}`, for every tree up to the order in the file. Part C: the
sign of the right side of inequality (3) for every tree of even order up to
the bound in the file, and for the spiders of Finding S31. These checks
support the identities on the range computed; S28 to S30 rest on the written
proofs, S31 on the computation.
