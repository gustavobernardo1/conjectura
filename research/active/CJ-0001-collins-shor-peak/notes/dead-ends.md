# CJ-0001 — failed approaches, refuted hypotheses and closed routes (detail)

This file keeps, verbatim, text that was in `STATE.md` until session 8
(2026-11-26), when that file was compacted. Negative results are preserved
here; `STATE.md` has a short summary of each and links to this file.
Nothing here is an established result of the project.

## Hypothesis A(i) (refuted in session 2)

**Hypothesis A(i) — refuted.** *Statement:* `ρ_k(T) ≥ ρ_k(S_n)` for every tree
`T` of order `n` and every `0 ≤ k ≤ ⌊n/2⌋ − 1`. *Motivation:* it holds for all
522,956 trees of order 4 to 19, and at `k = ⌊n/2⌋ − 1` it would have given the
lower half of the conjecture from Collins's theorem on stars.
*Refutation:* at order 20 it fails for exactly 10 trees, all at the last index
`k = 9` and all close to the star: the nine double stars `S(a, 18−a)`,
`1 ≤ a ≤ 9`, and the spider with two legs of length 2 and fifteen of length 1.
Explicit counterexample: the double star `S(9,9)`,

`q(S(9,9)) = 10255/10791 ≈ 0.950329 > q(S_20) = 94/99 ≈ 0.949495`,

confirmed by two implementations that share no code
(`test_refutation_of_star_minimality_at_order_20_by_both_methods`). Double stars were
compared with the star for every order from 6 to 41: some double star has a
larger `q` than the star at every even order from 20 to 40 and at every odd
order from 29 to 41, and at no other order in that range. All these values of
`q` stay below 1, so the Collins–Shor conjecture itself is not affected.

*What this teaches:* at those orders the star is not the extremal tree for the
lower bound, so a proof of the lower bound cannot go through comparison with
the star at the critical index. Do not retry star-comparison at `k = ⌊n/2⌋ − 1`.
Whether star-minimality holds for `k ≤ ⌊n/2⌋ − 2` at larger orders is untested.

*How it was found:* the pattern was perfect on every tree up to order 17; the
falsification test on sampled trees of order 24 and above broke it within
minutes.

## Session 7 — three dead ends for Γ

**Session 7 — three dead ends for Γ.** (1) *Roots.* `r_A` is real-rooted
(S13), but real negative roots do not imply membership in `C_d`
(`1 + 5x/2 + x²/2`); pairing roots `μ_i μ_{d+1−i} ≥ 1` cannot work for long
paths (the smallest eigenvalue of `L_B` tends to 0; not computed). (2)
*Darroch's theorem on the mode* applied to `(1+x)^K r_A`: the index needed by
S4 is the upper central one, where a symmetric polynomial has equality, so a
bound on the mean decides nothing (for `A = V` the mean is below the index and
the inequality still holds); real roots with mean equal to half the degree are
not enough (`(1+0.6x)²(1+3x)(1+x)²`, hand computation). (3) *Termwise
absorption in S17.* The part `E* = 2x²π′ + (3x+2x²)Φ′ + 3x²Ψ` of `E` is not in
the cone by itself (star with three leaves of weights 2, 2, 3 and centre of
weight 0: leading coefficient `−6`); a proof of (E) must use
`xR(T′, ν+e_u)` or `(1+x)Φ(T, ν⁰)`.

## The route through (E″) and (S): objective O7 as left by session 7 (closed in session 8)

Session 8 showed that (E″) and (S) below are **false** (Proposition S21 of
[`rooted-calculus.md`](rooted-calculus.md); `slope_family.py`,
`slope_family_verify.py`). The identities for `F` quoted below are correct
(`results/slope-family.json`: 0 failures in 1,403,375, 359,675 and 1,410,440
cases); what fails is the cone membership of `F` and of its slope for heavier
weights than session 7 had tried. The text is kept as it was written.

**Objective O7.** Prove statement (E) of `notes/gamma-components.md` through
the stronger statement **(E″)**, which involves no `R`. Since
`E = x R(T′, ν + e_u) + [(1+x)Φ(T, ν⁰) + E*]` and `Φ(T, ν⁰) = (1+x)Φ′ + xΨ`,
(E) follows (under the induction hypothesis of S18) from

> (E″) for every tree `T′` on `j′ ≥ 1` vertices, every vertex `u` and every
> integer weight `ν ≥ 0`, `ν ≠ 0`:
> `F(T′, ν, u) := (1 + 5x + 3x²)Φ′ + (x + 4x²)Ψ + 2x²π′ ∈ C_{j′+2}`,

`Φ′ = Φ(T′, ν)`, `Ψ = adj(M(T′, ν))_{uu}`, `π′ = e_uᵀ adj(M(T′, ν)) p`.
(E″) is an observation of session 7: exact for the 17,856 rooted cases with
`j′ ≤ 5`, weights 0 to 2 (`component_form.py`, field
`part3_E_minus_xR_not_in_cone`), and in a trial with weights up to 4 and
`j′ ≤ 4` (31,460 cases, not stored). It is not in the note and not reviewed.

What session 7 found about (E″), **on paper and in a scratch computation
only** (all weighted rooted trees with at most 5 vertices, weights 0 to 2,
every root and every leaf `w ≠ u`: 10,089 cases, 0 failures; script not
stored, nothing written up or reviewed). For a leaf `w ≠ u` of `T` with
neighbour `v` and weight `n`, `m = 1 + (1+n)x`, `θ = x(1+nx)`, by Lemma G2:

- `v ≠ u`: `F(T, ν, u) = m F(T − w, ν, u) + θ F(T_c, ν + e_{v_c}, u) Π_{l≠c} Φ_l − 4n x⁴ adj(M(T − w, ν))_{uv}`
  (`T_c` the component of `T − w − v` containing `u`);
- `v = u`: `F(T, ν, u) = m F(T − w, ν, u) + [x + (5+n)x² + (3+5n)x³ − n x⁴] Ψ_u(T − w)`;
- `F` is affine in `n`, with slope
  `x [F(T − w, ν + e_v, u) − 2x³ adj(M(T − w, ν))_{uv}]`;
- `F(T, ν, u) ∈ C_{j+2}` held in every case, **also for `ν = 0`**, and so did
  the slope.

So for `n = 0` every term is in the cone under the induction hypothesis
(`x(1 + 5x + 3x²) ∈ C_4`), and **(E″) — hence (E), Γ_c, Γ⁺ and Conjecture Γ —
would follow from the slope statement**

> (S) for every tree `T` on `j ≥ 1` vertices, all vertices `u, v` and every
> integer weight `ν ≥ 0`:
> `x [F(T, ν + e_v, u) − 2x³ adj(M(T, ν))_{uv}] ∈ C_{j+3}`,

with (E″) stated for all `ν ≥ 0`, zero included. `adj(M)_{uv}` is
`x^{dist(u,v)}` times the product of the polynomials `Φ` of the components
off the path from `u` to `v`. First step of the next session: put these
identities and (S) into `component_form.py` (weights up to 4, `j ≤ 6`), then
attack (S) by the same leaf removal. The expression in (S) is again affine in
the weight of a leaf `w ≠ u`; its slope subtracts two adjugate entries, so
the induction needs a family indexed by a multiset of vertices `v`, and
leaves that belong to the multiset have weight at least 1 — that is where the
session stopped.

Cheap exact computations that remain: Γ_c for `j = 8`; (E) and (E″) with
weights up to 6; the trees "skeleton plus one star" as polynomials in `m`.
