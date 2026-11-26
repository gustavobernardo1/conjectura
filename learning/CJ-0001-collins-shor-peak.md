# Learning guide — CJ-0001, the Collins–Shor conjecture

*Educational material for the project director. Everything stated here as a
theorem is a known result attributed to its source; nothing in this guide is a
research result of the project. The project's own findings are in
[`research/active/CJ-0001-collins-shor-peak/STATE.md`](../research/active/CJ-0001-collins-shor-peak/STATE.md).*

## 1. Prerequisites

- Linear algebra: determinant, characteristic polynomial, eigenvalues of a real
  symmetric matrix, trace, rank-one updates.
- Graph theory: trees, paths, stars, degree, distance, diameter, the Laplacian
  matrix.
- Sequences: unimodal and log-concave sequences.
- Python at the level of reading `experiments/CJ-0001-collins-shor-peak/distpoly.py`.

## 2. Definitions, with the smallest example

For a connected graph `G` on vertices `v_1, …, v_n`, the **distance matrix**
`D(G)` has `(i, j)` entry equal to the length of a shortest path from `v_i` to
`v_j`. For the path on three vertices:

```
D(P_3) = [0 1 2]
         [1 0 1]
         [2 1 0]
```

Write `δ_k` for the coefficient of `x^k` in `det(D − xI)`. For `P_3`,
`det(D − xI) = −x³ + 6x + 4`, so `δ_0 = 4`, `δ_1 = 6`.

The **normalized coefficients** of a tree `T` of order `n` are
`d_k(T) = 2^{k−(n−2)} |δ_k(T)|` for `0 ≤ k ≤ n−2`. For `P_3`: `d_0 = 2`,
`d_1 = 6`.

A sequence `a_0, …, a_r` is **unimodal** if it rises and then falls, and
**log-concave** if `a_j² ≥ a_{j−1} a_{j+1}` for all interior `j`. The **peak** is
an index where the maximum is attained.

**The conjecture (Collins–Shor).** For every tree on `n` vertices, the peak of
`d_0, …, d_{n−2}` lies between `⌊n/2⌋` and `⌈n − n/√5⌉`.
For `P_3` the peak is at `k = 1 = ⌊3/2⌋`.

## 3. Fundamental theorems

1. **Graham–Pollak (1971).** For every tree on `n` vertices,
   `det D = (−1)^{n−1} (n−1) 2^{n−2}`. The determinant does not depend on the
   shape of the tree. Consequence: `d_0(T) = n − 1`.
2. **Graham–Lovász (1978).** For a tree, `D^{-1} = −L/2 + ττᵀ / (2(n−1))`, where
   `L` is the Laplacian and `τ_i = 2 − deg(v_i)`. They also showed that the
   normalized coefficients count certain subforests of the tree, and asked
   whether they are unimodal with peak at `⌊n/2⌋`.
3. **Collins (1989).** The peak is at `⌊n/2⌋` for stars but at about
   `(1 − 1/√5) n ≈ 0.553 n` for paths — so the peak claim of Graham and Lovász
   is false. The corrected conjecture is attributed by Collins to Peter Shor.
4. **Aalipour, Abiad, Berikkyzy, Hogben, Kenter, Lin, Tait (2018).** The
   sequence is log-concave, hence unimodal, for every tree. The peak is at most
   `⌈2n/3⌉`, and at least `⌊(n−2)/(1+d)⌋` for a tree of diameter `d`.
5. **Newton's inequalities.** If a polynomial with real coefficients has only
   real roots, its coefficient sequence satisfies a strong form of
   log-concavity. This is the engine behind item 4: `D` is real symmetric, so
   `det(xI − D)` is real-rooted.
6. **A positive log-concave sequence is unimodal.** Short exercise below.

## 4. Why the problem is difficult

Unimodality needs only that the roots are real. The *location* of the peak
depends on the fine shape of the tree: it is decided by whether
`d_k / d_{k−1}` is above or below 1 at one specific index, and these ratios are
close to 1 near the peak. The known bounds (`2n/3` above, a diameter-dependent
bound below) come from the first two and the last two coefficients only, which
see little of the tree. The project's computations show how thin the margin is:
for some near-star trees of even order the critical ratio differs from 1 by
about `1.3 × 10⁻⁶` at order `10⁵` (see `STATE.md`).

## 5. How the concepts connect to the investigation

| Concept | Where it is used |
| --- | --- |
| Characteristic polynomial, exact integer arithmetic | `distpoly.py` computes every `d_k` exactly. |
| Graham–Pollak | Guard on every tree in the exhaustive search: `d_0 = n − 1`. |
| Graham–Lovász inverse formula and the matrix determinant lemma | `independent_check.py` recomputes the `d_k` from the Laplacian, sharing no code with the main computation. |
| Unimodality (item 4) | Turns "the peak is at least `m`" into the single inequality `d_{m−1} < d_m`. |
| Equitable partitions and quotient matrices | `near_star_families.py` handles caterpillars with a million vertices through a `2s × 2s` matrix. |
| First Zagreb index `Σ deg(v)²` | Gives `d_1` in closed form, the first case of the ratio comparison with the star and the path. |

## 6. Reading

1. Aalipour et al., *Proof of a conjecture of Graham and Lovász concerning
   unimodality of coefficients of the distance characteristic polynomial of a
   tree*, arXiv:1507.02341 — Sections 1 and 2 first (ten pages), then Section 3.
2. Graham and Lovász, *Distance matrix polynomials of trees*, Adv. Math. 29
   (1978) 60–88 — the inverse formula and the subforest interpretation.
3. Collins, *On a conjecture of Graham and Lovász about distance matrices*,
   Discrete Appl. Math. 25 (1989) 27–35 — stars and paths. (Not yet read by the
   project; listed as an obligation in `STATE.md`.)
4. Brändén, *Unimodality, log-concavity, real-rootedness and beyond* (survey in
   the Handbook of Enumerative Combinatorics, 2015) — Section on real-rooted
   polynomials and Newton's inequalities.
5. For equitable partitions: any text on algebraic graph theory, chapter on
   quotient matrices (for example Godsil and Royle, *Algebraic Graph Theory*).

## 7. Exercises

Answers can be checked with the code in `experiments/CJ-0001-collins-shor-peak/`.

1. Compute `D`, `det(D − xI)` and `d_0, d_1, d_2` by hand for the star and the
   path on four vertices. Check with `distpoly.scaled_coefficients` (which
   returns `2^{n−2} d_k`).
2. Verify Graham–Pollak by hand for both trees on four vertices.
3. Prove that a positive log-concave sequence is unimodal.
4. Using unimodality, prove: every maximizing index of `d_0, …, d_{n−2}` is at
   least `m` if and only if `d_{m−1} < d_m`.
5. For a tree, use `D^{-1} = −L/2 + ττᵀ/(2(n−1))` and `det D` to show
   `ℓ_T(x) := −2^{−(n−2)} det(2xI − D) = (n−1) det(I + xL) − x τᵀ adj(I + xL) τ`.
   (The matrix determinant lemma is `det(A + uvᵀ) = det A + vᵀ adj(A) u`.)
6. From exercise 5, read off the coefficient of `x`:
   `d_1(T) = 2n² − 6 − Σ_v deg(v)²`. Deduce that among trees of order `n` the
   star minimizes `d_1` and the path maximizes it.
7. Show that the distance matrix of the star `S_n` has eigenvalue `−2` with
   multiplicity `n − 2`, and find the quadratic satisfied by the other two
   eigenvalues. (Use the partition {centre}, {leaves}.)
8. Run the exhaustive search for orders 3 to 12 and explain every column of the
   output.

## 8. What worked and what did not (so far)

- *Worked:* exact enumeration reproduces the published verification (orders up
  to 20) and extends it; an independent formula confirms the computation.
- *Worked:* comparing each tree with the path. In all exact tests the path has
  the largest ratio `d_{k+1}/d_k` at every index up to its own peak, which would
  explain the upper bound.
- *Did not work:* the mirror-image idea for the lower bound — that the star has
  the smallest ratio at every index up to its peak. It holds for all trees of
  order at most 19 and fails at order 20: from there on, the balanced double star
  is closer to violating the lower bound than the star is. The lesson is the
  standard one: a pattern verified on all small cases is still only a
  hypothesis, and the falsification test on larger structured examples is what
  exposed it.
