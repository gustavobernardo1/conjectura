# CJ-0001 — the leaf recursion of the distance polynomial, and star minimality in the cone order

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 9. Proposition S23 and Proposition S27 have written
proofs below; **none has been reviewed** unless a report under
[`../reviews/`](../reviews/) names this file. Statement (SM) is a
**conjecture** of this session, supported by exact finite computation only.
Nothing here is a claim of novelty.

Notation: that of [`gamma-components.md`](gamma-components.md) and
[`rooted-calculus.md`](rooted-calculus.md) (`Φ(T, ν)`, `R(T, ν)`, the rooted
state `Ψ`, `Ω`, the cones `C_d`), and of [`wiener-form.md`](wiener-form.md)
(`ℓ_T`, the cones `K_d`, `λ_μ`). `S_n` is the star of order `n`. For a tree
`T` and a vertex `u`, `T_1, …, T_q` are the components of `T − u`, `u_i` the
neighbour of `u` in `T_i`, and

`r_u(T) := (1 + 4x) Ψ_u + Ω_u`,  `Ψ_u = Π_i Φ(T_i, e_{u_i})`,  `Ω_u = Σ_i R(T_i, e_{u_i}) Π_{l≠i} Φ(T_l, e_{u_l})`

(`Ψ_u = 1`, `Ω_u = 0` for the tree with one vertex). For `|T| ≥ 2` this is the
polynomial `r_A` of the earlier notes for `A = {u}` (Proposition S14 with
`e_A = 0`).

## Proposition S23 (leaf recursion and telescoping)

**Proposition S23.** (a) For every tree `T` of order `n ≥ 1`,
`R(T, 0) = x ℓ_T − (1 + 4x) Φ_T`.

(b) If `T⁺` is obtained from `T` by attaching a new pendant vertex at `u`,
then `ℓ_{T⁺} = (1 + x) ℓ_T + r_u(T)`.

(c) If `T_1 ⊂ T_2 ⊂ … ⊂ T_n = T` are subtrees with `|T_k| = k` and `T_{k+1}`
is `T_k` with a pendant vertex attached at `u_k`, then

`ℓ_T = −4x(1+x)^{n−1} + Σ_{k=1}^{n−1} (1+x)^{n−1−k} r_{u_k}(T_k)`.

(d) `ℓ_{S_n} = (1+x)^{n−2} [(n−1) + 4(n−2)x − 4x²]` for `n ≥ 2`, and for
`n ≥ 3`, `m = ⌊n/2⌋`: `d_{m−1}(S_n) < d_m(S_n)`.

*Proof.* (a) With `ν = 0`: `M = I + xL`, `p = 1 + xτ`, `M1 = 1`, so
`adj(M)1 = Φ1` and, as `1ᵀτ = 2`,
`pᵀadj(M)p = nΦ + 4xΦ + x² τᵀadj(M)τ`. Then
`R(T, 0) = (n−1)(1+x)Φ − pᵀadj(M)p = x[(n−1)Φ − x τᵀadj(M)τ] − (1+4x)Φ`, and
the bracket is `ℓ_T` by L1 (for `n = 1`: `ℓ = −4x = −2^{1} det(2x)`, and
`R = −(1+2x)²`).

(b) Proposition S15 for the leaf `w` of `T⁺` (weight `0`, `T′ = T`, `ν = 0`):
`R(T⁺, 0) = (1+x)R(T, 0) + xΩ_u`. By the expansion in the proof of Lemma F,
`Φ_{T⁺} = (1+x)Φ_T + xΨ_u` (as in Proposition S26). By (a) for `T⁺` and `T`:

`x ℓ_{T⁺} = (1+x)[xℓ_T − (1+4x)Φ_T] + xΩ_u + (1+4x)[(1+x)Φ_T + xΨ_u] = x[(1+x)ℓ_T + (1+4x)Ψ_u + Ω_u]`.

(c) Apply (b) `n − 1` times, starting from `ℓ_{T_1} = −4x`.

(d) For the star built from its centre, every `T_k − u_k` consists of `k − 1`
single vertices of weight `1`, for which `Φ = 1 + x` and `R = 0`; so
`r_{u_k}(T_k) = (1+4x)(1+x)^{k−1}` and (c) gives
`ℓ_{S_n} = (n−1)(1+4x)(1+x)^{n−2} − 4x(1+x)^{n−1}`. Put `N = n − 2`,
`m = ⌊n/2⌋`; then
`d_m − d_{m−1} = (n−1)[C(N,m) − C(N,m−1)] + 4(n−2)[C(N,m−1) − C(N,m−2)] − 4[C(N,m−2) − C(N,m−3)]`.
*`n = 2m ≥ 4`*: with `b = C(2m−2, m−2) = C(2m−2, m)`, `C(2m−2, m−1) = b·m/(m−1)`,
`C(2m−2, m−3) = b(m−2)/(m+1)`:
`d_m − d_{m−1} = b[(3n−7)/(m−1) − 12/(m+1)]`, and
`(6m−7)(m+1) − 12(m−1) = (2m−1)(3m−5) > 0`; for `m = 2`, `b = 1 > 0`.
*`n = 2m+1 ≥ 5`*: `C(2m−1, m) = C(2m−1, m−1)`, and with `b = C(2m−1, m−2)`,
`C(2m−1, m−1) = b(m+1)/(m−1)`, `C(2m−1, m−3) = b(m−2)/(m+2)`:
`d_m − d_{m−1} = 4b[2(2m−1)/(m−1) − 4/(m+2)] > 0`. *`n = 3`*: `ℓ = (1+x)(2+4x−4x²)`,
`d_0 = 2 < d_1 = 6`. ∎

**Remark.** (b) expresses the one-element polynomials through distance
polynomials: `r_u(T) = ℓ_{T⁺} − (1+x)ℓ_T`. It is the case `c = e_u` of the
expansion of Proposition S2, which was stated there only for `n ≥ 2s`. In
contrast with S1, S2 and L4, the telescoping (c) applies to **every** tree,
and uses one-element sets only.

## Statement (SM) and Proposition S27

> **(SM)** For every tree `T` of order `n ≥ 3`: `ℓ_T − ℓ_{S_n} ∈ C_{n−1}`.

(`ℓ_T − ℓ_{S_n}` has degree at most `n − 2`: the coefficients of `x^n` and
`x^{n−1}` cancel.)

> **(Γ_c¹)** For every tree `B` on `j ≥ 1` vertices and every vertex `c`:
> `R(B, e_c) ∈ C_{j+1}`.

(Γ_c¹) is the case of Γ_c in which the weight is one unit at one vertex; it
has no parameter besides the rooted tree.

**Proposition S27.** (a) If (SM) holds for `T`, then
`d_m(T) − d_{m−1}(T) ≥ d_m(S_n) − d_{m−1}(S_n) > 0`, `m = ⌊n/2⌋`. So (SM)
implies the lower bound `⌊n/2⌋` of the Collins–Shor conjecture for every
tree, of even and of odd order.

(b) For every rooted tree `(B, c)` on `j` vertices,
`Φ(B, e_c) − (1+x)^j ∈ C_j`.

(c) (Γ_c¹) implies `r_u(T) − (1+4x)(1+x)^{n−1} ∈ C_n` for every tree `T` of
order `n` and every vertex `u`, and this implies (SM).

*Proof.* (a) `2m − 1 ≤ n − 1`, so `C_{n−1} ⊆ K_{n−1} ⊆ K_{2m−1}` and `λ_m ≥ 0`
on it (Lemma A(a) of `wiener-form.md`); `m ≤ n − 2`, so `λ_m` reads
`d_m − d_{m−1}` on `ℓ_T` and on `ℓ_{S_n}`; the star is S23(d); then R1.

(b) Induction on `j`; for `j = 1`, `Φ = 1 + x`. For `j ≥ 2` take a leaf
`w ≠ c` with neighbour `u`. By the expansion in the proof of Lemma F,
`Φ(B, e_c) = (1+x)Φ(B − w, e_c) + xΨ`, where `Ψ` is a product of polynomials
`Φ(K, ν_K)` with `ν_K ≠ 0` over the components of `B − w − u`, with
`j − 2` vertices in all; `Ψ ∈ C_{j−2}` by Lemma F, and `xΨ ∈ C_j`. So
`Φ(B, e_c) − (1+x)^j = (1+x)[Φ(B − w, e_c) − (1+x)^{j−1}] + xΨ ∈ C_j`.

(c) By (b) and the product rule, `Ψ_u − (1+x)^{n−1} ∈ C_{n−1}` (expand
`Π_i (a_i + b_i) − Π_i a_i` with `a_i = (1+x)^{j_i}`, `b_i ∈ C_{j_i}`), so
`(1+4x)[Ψ_u − (1+x)^{n−1}] ∈ C_n`; and under (Γ_c¹) and Lemma F each term of
`Ω_u` is in `C_{j_i+1} · C_{n−1−j_i} = C_n`. For (SM), subtract from S23(c)
the same formula for the star (S23(d)):
`ℓ_T − ℓ_{S_n} = Σ_k (1+x)^{n−1−k} [r_{u_k}(T_k) − (1+4x)(1+x)^{k−1}]`, and
`(1+x)^{n−1−k} C_k ⊆ C_{n−1}`. ∎

**Evidence for (SM)** (exact; `leaf_telescoping.py`,
`results/leaf-telescoping.json`, run on a clean tree at `6c23eea`): (SM)
holds for every tree of order 3 to 20 (1,346,023 trees; equality only for the
star). For every tree of order 1 to 11 and every vertex (4,394 rooted
trees): S23(a), (b), (c), (Γ_c¹), S27(b) and the inequality of S27(c) — no
failure. This is finite evidence, not a proof.

**Relation to the rest.** (Γ_c¹) is a special case of Γ_c, hence of (Λ)
(`rooted-calculus.md`). So the chain is now

```
lower bound floor(n/2), every tree  ⇐ (SM)  ⇐ (Γ_c¹)  ⇐ Γ_c  ⇐ (E)  ⇐ (Λ)        [(SM), (Γ_c¹), Γ_c, (E), (Λ) OPEN]
lower bound floor(n/2), odd order                                               [Theorem T4, wiener-form.md]
```

and the route through Hypothesis V, Lemma L4 and the trees "skeleton plus
one star" is no longer needed for the lower bound. The natural recursion for
`R(B, e_c)` (removing a leaf of `B` that is not adjacent to `c`) leaves the
family of unit weights — it produces a component of weight 2 — which is why
(Γ_c¹) is not proved here. A formula that may help (hand computation of this
session, **not checked by machine and not reviewed**): with `δ` the vector of
distances from `c` in `B` and `M¹ = I + x(L_B + e_c e_cᵀ)`,
`R(B, e_c) = Σ_{u<v} (δ_u − δ_v)² adj(M¹)_{uv} + x Σ_v δ_v² adj(M¹)_{vc}`,
a sum with non-negative coefficients.
