# The perturbation C − ∏(x_i − C) of the product copula in dimension n ≥ 3

*Note written 2026-11-27 by `claude-opus-5-5`. Candidate, not reviewed.
Revision 1.*

## 1. The question and its reading

Mesiar, Stupňanová, *Open problems from the 12th International Conference on
Fuzzy Set Theory and Its Applications*, Fuzzy Sets Syst. 261 (2015) 112–123,
Problem 4.1 (Mesiar), p. 114 (author copy
<http://library.utia.cas.cz/separaty/2019/E/mesiar-0506948.pdf>, read by the
project's scout and auditor as page images; wording quoted in
`research/candidates/CJ-0017-nary-copula-perturbation.md`): for an n-ary
copula C (Definition 4.1 there, n ≥ 2),

    C_1(x_1, …, x_n) = C(x) − ∏_{i=1}^n (x_i − C(x)).

"Is the function C_1 n-increasing, i.e., is it an n-copula? If in general not,
characterize all n-copulas C such that C_1 is an n-copula, too." The problem
is introduced as extending the bivariate construction C + λ(x − C)(y − C),
λ ∈ [0,1], to higher dimensions; the source notes that if C_1 is an
n-copula then so is C − λ∏(x_i − C) for λ ∈ [0,1].

**Reading.** (i) Read literally (any n ≥ 2), the first question has the
trivial answer *no* at n = 2: for W(x,y) = max(0, x + y − 1), C_1(x,y) = −xy < 0
when x + y < 1 (observation of the literature auditor,
`research/candidates/CJ-0017-nary-copula-perturbation-audit.md`). (ii) For the
product copula Π, C_1 is a 2-copula for n = 2 (C_1 = xy(1 − (1−x)(1−y)), the
Farlie–Gumbel–Morgenstern copula with parameter −1). This note shows that
the extension fails for Π in every dimension n ≥ 3 that was examined, and in
all even dimensions, and determines the exact parameter range for Π in
dimension 3. These are contributions to the characterisation part only; they
do not settle it.

## 2. Results

Let P(x) = ∏ x_i and C_1^{(n)} = P − ∏_i (x_i − P) on [0,1]^n. C_1^{(n)} is a
polynomial satisfying the boundary conditions of an n-copula (if some
x_j = 0 then P = 0 and the factor x_j − P = 0; if x_j = 1 for all j ≠ i then
P = x_i and the factor x_i − P = 0). Hence C_1^{(n)} is an n-copula iff it is
n-increasing iff its density d_n = ∂ⁿC_1^{(n)}/∂x_1⋯∂x_n is ≥ 0 on [0,1]^n
(for a polynomial, the volume of a box is the integral of d_n over it; if
d_n(p) < 0 at some p, a small box around p, taken inside [0,1]^n, has
negative volume).

**Proposition 1 (n = 3, an explicit box).** For B = [3/5, 4/5] × [4/5, 1] × [4/5, 1],
V_{C_1^{(3)}}(B) = −23/5⁹ < 0. Hence C_1^{(3)} is not a 3-copula.

**Proposition 2 (corner density; all even n ≥ 4).** For every n ≥ 2,
d_n(1, …, 1) = 1 − (−1)ⁿ · D_n, where D_n is the number of derangements of
n elements. Hence for every even n ≥ 4 (D_n ≥ 9 > 1), d_n(1,…,1) < 0 and
C_1^{(n)} is not an n-copula.

**Proposition 3 (n = 5, 7).** d_5(159/200, 1, 1, 1, 1) < 0 and
d_7(177/200, 1, …, 1) < 0 (exact rational evaluation). Hence C_1^{(n)} is not
an n-copula for n = 5, 7.

**Proposition 4 (n = 3, exact parameter range).** For real λ, let
D_λ = Π − λ∏_{i=1}^3 (x_i − Π) on [0,1]³. Then D_λ is a 3-copula if and only if
−1/3 ≤ λ ≤ 15/19. (The density of D_λ is 1 − λ(1 − d_3); the extrema of d_3
on [0,1]³ are min d_3 = −4/15, attained at the points with two coordinates 1
and the third 8/15, and max d_3 = 4, attained at the points with one
coordinate 0 and the other two 1.)

Open for this note: odd n ≥ 9; whether D_λ is an n-copula for some λ > 0
when n ≥ 4; the characterisation of all C for which C_1 is an n-copula
(C = M is one: C_1 = M, since the factor of a minimal coordinate vanishes).

## 3. Proofs

**Proposition 1.** C_1^{(3)} = xyz[1 − (1−yz)(1−xz)(1−xy)] has 7 monomials;
the volume is the alternating sum over the 8 vertices of B, equivalently the
integral of d_3 over B. Both were computed exactly and give −23/1953125
(`experiments/CJ-0017-nary-copula-perturbation/box_search.py`,
`nice_box.py`, and the independent `independent_check.py`, which expands the
polynomial, differentiates and integrates monomials; no code shared).

**Proposition 2.** d_n = ∂_1⋯∂_n P − ∂_1⋯∂_n ∏_i f_i with f_i = x_i − P, and
∂_1⋯∂_n P = 1. By the Leibniz rule, ∂_1⋯∂_n ∏_i f_i is the sum, over all
maps assigning each derivative ∂_j to one factor, of the products of the
correspondingly differentiated factors. At x = (1,…,1) every f_i vanishes
(1 − 1 = 0), so a term survives only if every factor receives at least one
derivative; with n derivatives and n factors each receives exactly one, and
the surviving terms are indexed by permutations σ (∂_{σ(i)} applied to f_i):
the value is Σ_σ ∏_i ∂_{σ(i)} f_i(1,…,1). Now ∂_j f_i = δ_{ij} − ∏_{k≠j} x_k,
which is δ_{ij} − 1 at (1,…,1). So the value is the permanent of I − J
(J the all-ones matrix): a permutation with a fixed point contributes 0, and a
derangement contributes (−1)ⁿ. Hence ∂_1⋯∂_n ∏ f_i (1,…,1) = (−1)ⁿ D_n and
d_n(1,…,1) = 1 − (−1)ⁿ D_n. For even n ≥ 4, D_n ≥ D_4 = 9. (Exact check: the
edge polynomials printed by `edge_density.py` give d_n(1,…,1) = 0, 3, −8, 45,
−264, 1855, −14832 for n = 2, …, 8, equal to 1 − (−1)ⁿ D_n with
D_n = 1, 2, 9, 44, 265, 1854, 14833.)

**Proposition 3.** `edge_density.py` computes the exact polynomial
t ↦ d_n(t, 1, …, 1) from the monomial expansion and evaluates it at the
stated rationals: d_5(159/200, 1,1,1,1) = −4880548111/320000000 and
d_7(177/200, 1,…,1) = −41596459182289961/64000000000000.

**Proposition 4.** Write p = xy, s = x + y. Then
d_3 = 4(xy + yz + zx) − 12xyz(x + y + z) + 27x²y²z², and as a polynomial in z,

    d_3 = 4p + 4s(1 − 3p) z + p(27p − 12) z².          (Q)

On [0,1]² one has 2√p ≤ s ≤ 1 + p (AM–GM and (1−x)(1−y) ≥ 0).

*The face z = 1.* d_3(x,y,1) = 27p² − 8p + 4s(1 − 3p). As a polynomial in y
for fixed x it is a(x) y² + b(x) y + 4x with a = x(27x − 12),
b = 4 − 8x − 12x². If x ≤ 4/9 (a ≤ 0) its minimum over y ∈ [0,1] is at y = 0
(value 4x ≥ 0) or y = 1 (value 15x² − 16x + 4, whose minimum on [0,1] is
−4/15 at x = 8/15). If x > 4/9 the minimum is at y = 0 or y = 1, or at the
critical point y* = 2(3x − 1)(x + 1)/(x(27x − 12)) when y* ≤ 1, i.e. when
21x² − 16x + 2 ≥ 0, i.e. x ≥ x₀ = (8 + √22)/21 ≈ 0.6043; the critical value
is G(x) = 4x − 4(3x − 1)²(x + 1)²/(x(27x − 12)). For x ∈ [x₀, 1],
G(x) + 4/15 = (4/15)·(1 − x)(135x³ − 90x² + 33x − 15)/(x(27x − 12)) ≥ 0, because
135x³ − 90x² + 33x − 15 is increasing (its derivative 405x² − 180x + 33 has
negative discriminant) and positive at x = 3/5 (value 39/25) and x₀ > 3/5.
So min over the face z = 1 is −4/15, attained only at (8/15, 1, 1) — and, by
symmetry, the faces x = 1 and y = 1 behave the same.

*The interior in z.* For fixed (x,y), (Q) is a quadratic in z. If
p ≤ 4/9 its leading coefficient is ≤ 0 and the minimum over z ∈ [0,1] is at
z = 0 (value 4p ≥ 0) or z = 1 (the face). If p > 4/9 the minimum is at an
endpoint or at z* = 2s(3p − 1)/(p(27p − 12)) when z* ≤ 1, with value
F = 4p − 4s²(3p − 1)²/(p(27p − 12)), a decreasing function of s. The condition
z* ≤ 1 is s ≤ σ(p) := p(27p − 12)/(2(3p − 1)). Let s̃ = min(1 + p, σ(p)) ≥ s.
If s̃ = σ(p), then F ≥ F|_{s=σ(p)}, which is the value of (Q) at z = 1 with
s = σ(p); since 2√p ≤ s ≤ σ(p) ≤ 1 + p, the pair (σ(p), p) is realised by
some (x', y') ∈ [0,1]², so this value is d_3(x', y', 1) ≥ −4/15. If
s̃ = 1 + p (which happens iff 21p² − 16p + 2 ≥ 0 with p > 4/9, i.e.
p ≥ x₀), then F ≥ G(p) ≥ −4/15 by the computation above (G is the same
function). Hence d_3 ≥ −4/15 on [0,1]³, with equality at (8/15,1,1) and its
permutations.

*The maximum.* At z = 0, d_3 = 4p ≤ 4. At z = 1: if p ≤ 1/3, then
4s(1 − 3p) ≤ 4(1 + p)(1 − 3p) and d_3 ≤ 15p² − 16p + 4 ≤ 4 (p ≤ 16/15); if
p > 1/3, then 4s(1 − 3p) ≤ 8√p(1 − 3p) and, with q = √p ∈ ]0,1],
4 − d_3 ≥ 4 − 8q + 8q² + 24q³ − 27q⁴ ≥ 4 − 8q + 8q² − 3q³ ≥ 4 − 8q + 5q² > 0
(27q⁴ ≤ 27q³, q³ ≤ q², negative discriminant). In the interior: if
p ≥ 4/9 (Q) is convex in z and its maximum is at an endpoint; if p < 4/9 the
maximum is at an endpoint or at z* = 2s(1 − 3p)/(p(12 − 27p)) ∈ [0,1], which
requires p ≤ 1/3, with value 4p + 2s(1 − 3p) z* ≤ 4p + 2s(1 − 3p) ≤
4p + p(12 − 27p) = 16p − 27p² ≤ 64/27 < 4 (using z* ≤ 1 ⟺
2s(1 − 3p) ≤ p(12 − 27p)). So max d_3 = 4, attained at (0,1,1) and
permutations.

*Conclusion.* D_λ satisfies the boundary conditions for every λ (the
product term vanishes there), and its density is 1 − λ(1 − d_3). For λ ≥ 0
this is ≥ 0 on the cube iff λ(1 − min d_3) ≤ 1 iff λ ≤ 15/19; for λ < 0 iff
|λ|(max d_3 − 1) ≤ 1 iff λ ≥ −1/3. A polynomial with non-negative density
and the boundary conditions is a 3-copula (its box volumes are integrals of
the density); a negative density value gives a box of negative volume. ∎

## 4. Novelty and caveats

- Literature audit: `research/candidates/CJ-0017-nary-copula-perturbation-audit.md`
  (no answer found within its coverage). **Not read:** J. Fernández-Sánchez,
  M. Úbeda-Flores, *Solution to two open problems on perturbations of the
  product copula*, Fuzzy Sets Syst. 354 (2019) 116–122,
  doi:10.1016/j.fss.2018.06.013 (closed access; a search snippet says it
  extends the discussion to higher dimensions; its OpenAlex reference list
  does not include the 2015 problem paper). That paper may contain some or
  all of Propositions 1–4. Until it is read, novelty is `unknown`.
- Proposition 4's proof is a case analysis written here for the first time;
  it has not been checked by anyone else. A z3 attempt to decide min d_3 ≥
  −4/15 exactly timed out (120 s per query); the exploratory floating-point
  grid agrees with the extrema.
