# CJ-0001 — Conjecture Γ: the chain of sufficient conditions (status as of session 10)

Moved verbatim from `STATE.md` in session 10 (2026-11-26) to keep that file compact; nothing was changed.
It continues the list under "Conjecture Γ — open (MD-0010)" of [`../STATE.md`](../STATE.md). Notation:
[`gamma-components.md`](gamma-components.md), [`rooted-calculus.md`](rooted-calculus.md),
[`skeleton-identity.md`](skeleton-identity.md).

- **Chain of sufficient conditions** (each arrow a proved implication; only
  S11 is an equivalence):
  `Γ ⇐ Γ⁺ ⇐ Γ⁺ for A independent (S11) ⇐ Γ_c (S14) ⇐ (E) (S18) ⇐ (Λ) (S22)`.
  - **Γ_c**: `R(T, ν) ∈ C_{j+1}` for every weighted tree, `ν ≠ 0`. Exact for
    all 29,336 weighted trees with `j ≤ 7`, weights 0 to 2; for 11,073 rooted
    stars with heavy leaves and 3,213 rooted random trees (session 8).
  - **(E)**: for every tree all of whose leaves have weight `≥ 1` there is a
    leaf `w` with `E = R(T, ν⁰ + e_w) − R(T, ν⁰) ∈ C_{j+1}`. No failure known
    (17,856 cases of session 7; every counterexample to (E″) and (S)).
  - **(Λ)** (session 8, replaces (E″)): `Λ(T, ν, u) = x[(1−x)Φ + 2xΨ + R(T, ν+e_u) − 2xG] ∈ C_{j+2}`
    for every rooted weighted tree, zero weight included; equivalently
    `E − (1+2x)²Φ(T′, ν+e_u) ∈ C_{j′+2}` at a new leaf. **Open**; no failure
    in 4,395 + 11,085 + 3,269 rooted trees (`results/rooted-state.json`), nor
    in two scratch runs (29,295 rooted stars with up to 7 leaves and weights
    up to 8; 8,198 rooted random trees; not stored).
    The reviewer's own search (stars with equal leaf weights up to about
    30, at most 6 leaves; 2,462 rooted cases) found none either. Brooms,
    spiders, double stars and paths with heavy weights are **untested**
    beyond the random sample.
  - **(E″), (S)**: false (S21). The family indexed by multisets of vertices
    that session 7 proposed is abandoned.
- **What the application needs is weaker (Γ_w)**: S4 uses `r_A` only through
  `([x^c] − [x^{c−1}])(1+x)^L r_A ≥ 0`, `L ≥ d − 1`, `c = ⌈(L+d)/2⌉`. That
  cone is strictly larger than `C_d` (`1 + x + x²`), but it is not known to
  be closed under products, which every proof so far uses.
- Not covered by Γ: trees with fewer leaves than non-leaf vertices; the trees
  "skeleton plus one star" themselves (positive in all computed cases); the
  upper half.

## Text moved from `STATE.md` in session 11 (verbatim except for the targets of relative links)

The section "Conjectures and hypotheses" of `STATE.md`, as it read at the end of session 10:

**Conjecture Γ — open (MD-0010).** For every tree `S` on `s ≥ 2` vertices and
every `A ⊆ V(S)` with `|A| ≥ 2`, the polynomial
`r_A(x) = −2^{2−s} x det(2x I_Ā − P − 1_A1ᵀ − 11_Aᵀ − (|A|/2x)J)` is a
non-negative combination of `x^e (1+x)^{d−2e}` (`2e < d`) and `x^e`
(`d ≤ 2e ≤ 2d`), `d = s − |A| + 1`. Statement and consequences:
[`notes/skeleton-identity.md`](skeleton-identity.md).

- True for `A = V` (S3), for every `A` whose complement is independent (S10)
  or has at most two vertices (S8, S9), and for every subset of the 47 trees
  with 2 to 8 vertices (exact).
- Every `r_A` has only real negative roots (S13); this does not give the
  expansion.
- It does not depend on the order `n` nor on the leaf numbers. If true for
  `S`: Hypothesis V for `S` and every order (S4), and by L4 the lower half of
  Collins–Shor for the trees `S(c)`, `n ≥ 2s`, is reduced to the trees
  "skeleton plus one star".
- **Chain of sufficient conditions** `Γ ⇐ Γ⁺ ⇐ Γ⁺ for A independent (S11) ⇐ Γ_c (S14) ⇐ (E) (S18) ⇐ (Λ) (S22)`,
  with the exact ranges tested for Γ_c, (E), (Λ), the weaker statement (Γ_w)
  that S4 actually needs, and what Γ does not cover:
  [`notes/gamma-chain.md`](gamma-chain.md). (E″), (S): false (S21).

**Hypothesis V — open in general (MD-0009).** The mixed second partials of
`D_n` are non-negative for caterpillars with any number `s` of spine vertices.
A consequence of Γ for path skeletons: computer-assisted for `s ≤ 8` and
every order. The analogue for `d_m − d_{m+1}` is false from `s = 4`.

The part of the dependency map of `STATE.md` on the route of sessions 4 to 8, as it read at the end of session 10:

```
  --- the route of sessions 4 to 8 (leafy trees only; superseded for the lower half by the two lines above) ---
  trees S(c) with at least as many leaves as non-leaf vertices (n ≥ 2s):
    ⇐ S1 (closed form)                               [proved, AI-reviewed]
    ⇐ L4 (vertex principle)                          [proved, AI-reviewed; Lean: see Status]
    ⇐ S4 [AI-reviewed] + Property Γ for the skeleton S [conjecture in general (MD-0010)]
        (S4 needs only Γ_w, strictly weaker than Γ)   [observation, session 8]
        Γ for A with V∖A independent or |V∖A| ≤ 2     [proved for every tree, AI-reviewed (MD-0011)]
        Γ ⇐ Γ⁺ ⇐ Γ⁺ for A independent                 [S11 (MD-0012)]
        Γ⁺ ⇐ Γ_c (one weighted tree)                  [S14 (MD-0014)]
        Γ_c ⇐ (E): raising a leaf weight 0 → 1         [S18 (MD-0014); (E) OPEN]
        (E) ⇐ (Λ)                                      [S22 (MD-0015); (Λ) OPEN, exact on the ranges above]
        (E) ⇐ (E″) ⇐ (S)                               [(E″), (S) FALSE: S21 (MD-0015)]
    ⇐ d_{m−1} < d_m for "skeleton plus one star"     [OPEN in general; s ≤ 3 paths done (T1 to T3)]
  trees with fewer leaves than non-leaf vertices     [OPEN; no approach]
  special cases with complete candidate proofs, both halves, peak exactly m:
    diameter 3: T1;  caterpillars of diameter 4: T2, T3, P_5;  stars: Collins 1989 (not read)
```
