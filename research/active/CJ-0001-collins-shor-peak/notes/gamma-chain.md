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
