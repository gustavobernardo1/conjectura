# Experiments for CJ-0001 (Collins–Shor conjecture)

Mathematical question: for a tree `T` of order `n`, where is the maximum of the
normalized coefficients `d_0, …, d_{n−2}` of its distance characteristic
polynomial? The conjecture says: between `⌊n/2⌋` and `⌈n − n/√5⌉`. Definitions,
findings and their evidence levels are in
[`research/active/CJ-0001-collins-shor-peak/STATE.md`](../../research/active/CJ-0001-collins-shor-peak/STATE.md).

All arithmetic is exact (integers and rationals). Decimal numbers in result
files are renderings of exact rationals. Nothing here uses floating point to
decide an inequality.

## Files

| File | Purpose |
| --- | --- |
| `distpoly.py` | Core: tree enumeration, distance matrix, exact coefficients `s_k = 2^k |δ_k|`, peak, conjectured interval. |
| `independent_check.py` | Independent method (Laplacian formula, pure-Python rationals); shares no code with `distpoly.py`. |
| `exhaustive.py` | Tests the conjecture on every tree of given orders. |
| `ratio_extremality.py` | Tests Hypotheses A(i) and A(ii): comparison of consecutive-coefficient ratios with the star and the path; exhaustive and sampled modes. |
| `near_star_families.py` | Double stars (orders 6–41) and balanced caterpillars up to order 10⁶ through a quotient-matrix formula. |
| `double_stars.py` | Closed forms for the coefficients of double stars and stars around the middle index (Theorem T1 of `notes/double-stars.md`): symbolic quotient determinant, all double stars with `a + b ≤ 200`, direct determinants up to `a + b ≤ 40`. |
| `spine3.py` | Closed forms around the middle index for the caterpillars `K(a,b,c)` with three spine vertices carrying `a, b, c ≥ 1` leaves (Theorem T2 of `notes/spine3.md`; `b = 0` is not covered): symbolic quotient determinant and symbolic reduction of the two differences, the sign conditions of the proof for `m ≤ 2000`, all `K(a,b,c)` with `a + b + c ≤ 300`, whole sequences up to `a + b + c ≤ 60`, direct determinants up to `a + b + c ≤ 20`. |
| `diameter4.py` | The caterpillars `K(a,0,c)` of diameter 4 with no leaf at the centre (Theorem T3 of `notes/diameter4-caterpillars.md`): the formula of `spine3.py` at `b = 0` against the direct determinant for `a + c ≤ 40`, the closed forms for `a + c ≤ 600`, the sign conditions for `m ≤ 2000`, and the path `P_5`. |
| `mixed_partials.py` | Exploration for Hypothesis V of `notes/vertex-principle.md`: for caterpillars with 2 to 8 spine vertices and orders up to 200, the closed form by interpolation, a certificate for the sign of the mixed second partials of `d_m − d_{m−1}`, and the values at the vertices of each slice. Evidence for a hypothesis, not a proof. |
| `mixed_partials_s3.py` | The same mixed partials for three spine vertices as polynomials in `m`, valid for every order: symbolic derivation, comparison with the forms stated in `notes/vertex-principle.md`, and the values at the vertices. Prints its findings; no result file. |
| `skeleton_structure.py` | Trees made of a skeleton with pendant leaves (`notes/skeleton-identity.md`): for every tree with 2 to 8 vertices as skeleton, the closed form against direct determinants, the expansion over subsets (Proposition S2), the top coefficient (S3), the order-independent Property Γ for every subset with at least two elements, and, in a range of orders, the certificate of `mixed_partials.py`. |
| `locality_check.py` | Session 6 (`notes/skeleton-locality.md`): the definition of `r_A` against Propositions S6 to S10 on the 47 trees with 2 to 8 vertices; shares no code with `skeleton_structure.py`. |
| `gamma_pieces.py` | Session 6 (`notes/gamma-reduction.md`): which pieces of the Laplacian form of `r_A` have non-negative half-gamma expansions, on the same trees. |
| `component_form.py` | Session 7 (`notes/gamma-components.md`): real negative roots of `r_A` (Sturm sequences), its leading coefficient, the component form, Lemma G entry by entry and the recurrences for `R(T, ν)` on weighted trees with at most 7 vertices and weights 0 to 2. Pure Python integers. |
| `slope_family.py` | Objective O7 (`STATE.md`, "Next step"): the polynomial `F(T, ν, u)`, statement (E″) with `ν = 0` included, the three leaf identities for `F`, and the slope statement (S), on every weighted tree with at most 6 vertices and weights 0 to 4. Pure Python integers. Details below. |
| `slope_family_extension.py` | For the failures of (S) and (E″) stored by `slope_family.py`: the tree with one more leaf (a failure of (E″) for a larger weight) and statement (E) on the corresponding trees. Imports `slope_family.py`. |
| `slope_family_verify.py` | Independent checker of the stored failures (hypotheses, then the violation): evaluation at integer points, Gauss–Jordan elimination over `Fraction`, interpolation. Shares no code with the two scripts above. |
| `upper_bound.py` | Session 13: exact checks around `tr(T) = trace (I+L)^{-1}` and an upper bound on the peak index: path minimality of `tr`, the path value, the peak bound `p < n - n/sqrt 5 + 3/5`, pendant-path merging, a path inequality, the merge identity. Imports `lower_bound.py`, `distpoly.py`, `tree_shift.py`. Details below. |
| `manuscript_check.py` | Session 14: independent exact check of the lower half as restated in `manuscripts/CJ-0001-collins-shor/main.tex` (rooted calculus with root weights, plant and merge rules, leaf recursion, distance formulas, the sum of squares, the cone memberships, star minimality), written from the manuscript's definitions and sharing no code with the other scripts. Details below. |
| `amw_reduction_check.py` | Session 15: exact checks behind revision 3 of the manuscript: the subdivision identity `avm(S(T)) = n − tr(I+L_T)^{−1}` and `m_k(S(T)) = [t^k] det(I + tL_T)` (Remark 9.6), the path as the unique maximizer of the average matching size, `avm(P_N) > aN + b` (the comparison with Theorem 4.4 of arXiv:1903.09825), the orders for which peak-maximality of the path is settled (Section 12, item 1), the tie at order 13. Details below. |
| `results/*.json` | Outputs of the runs below. |

Validation: `uv run pytest tests/test_cj0001_distpoly.py` (101 tests) and
`uv run pytest tests/test_cj0001_component_form.py` (11 tests, about 5 s:
`component_form.py` with small parameters, `slope_family.py` on small ranges
and on values computed by hand, the search code against the checker).

## Reproduction

Environment: Python 3.12.4, python-flint 0.9.0, networkx 3.7 (`uv.lock`).
Hardware used: Intel Core i7-7700 (4 cores, 8 threads), 16 GB RAM, Windows 10.
From the repository root:

```sh
uv run python experiments/CJ-0001-collins-shor-peak/exhaustive.py --min-order 3 --max-order 20 --workers 7 \
    --out experiments/CJ-0001-collins-shor-peak/results/exhaustive-03-20.json                # about 1.5 min
uv run python experiments/CJ-0001-collins-shor-peak/exhaustive.py --min-order 21 --max-order 23 --workers 7 \
    --out experiments/CJ-0001-collins-shor-peak/results/exhaustive-21-23.json                # about 34 min
uv run python experiments/CJ-0001-collins-shor-peak/ratio_extremality.py exhaustive --min-order 4 --max-order 17 \
    --out experiments/CJ-0001-collins-shor-peak/results/ratio-extremality-04-17.json
uv run python experiments/CJ-0001-collins-shor-peak/ratio_extremality.py exhaustive --min-order 18 --max-order 20 --workers 7 \
    --out experiments/CJ-0001-collins-shor-peak/results/ratio-extremality-18-20.json
uv run python experiments/CJ-0001-collins-shor-peak/ratio_extremality.py sampled --orders 24 30 40 60 90 --samples 400 \
    --seed 20261126 --out experiments/CJ-0001-collins-shor-peak/results/ratio-extremality-sampled.json
uv run python experiments/CJ-0001-collins-shor-peak/near_star_families.py \
    --out experiments/CJ-0001-collins-shor-peak/results/near-star-families.json
uv run python experiments/CJ-0001-collins-shor-peak/double_stars.py \
    --out experiments/CJ-0001-collins-shor-peak/results/double-stars.json                    # about 1 min
uv run python experiments/CJ-0001-collins-shor-peak/spine3.py     --out experiments/CJ-0001-collins-shor-peak/results/spine3.json                          # about 6 min
uv run python experiments/CJ-0001-collins-shor-peak/diameter4.py     --out experiments/CJ-0001-collins-shor-peak/results/diameter4.json                       # under 2 min
uv run python experiments/CJ-0001-collins-shor-peak/mixed_partials.py --max-spine 8 --max-order 200     --out experiments/CJ-0001-collins-shor-peak/results/mixed-partials.json                  # under 1 min
uv run python experiments/CJ-0001-collins-shor-peak/mixed_partials_s3.py                     # seconds
uv run python experiments/CJ-0001-collins-shor-peak/skeleton_structure.py --max-skeleton 8 --max-order 40     --out experiments/CJ-0001-collins-shor-peak/results/skeleton-structure.json              # about 1 min (about 3 min with --max-order 100)
uv run python experiments/CJ-0001-collins-shor-peak/locality_check.py --max-skeleton 8     --out experiments/CJ-0001-collins-shor-peak/results/locality-check.json                  # about 35 s
uv run python experiments/CJ-0001-collins-shor-peak/gamma_pieces.py --max-skeleton 8     --out experiments/CJ-0001-collins-shor-peak/results/gamma-pieces.json                    # about 12 s
uv run python experiments/CJ-0001-collins-shor-peak/component_form.py --max-skeleton 8 --max-component 7 --max-weight 2 --max-component3 6     --out experiments/CJ-0001-collins-shor-peak/results/component-form.json                  # about 3 min
uv run python experiments/CJ-0001-collins-shor-peak/slope_family.py --max-order 6 --max-weight 4     --out experiments/CJ-0001-collins-shor-peak/results/slope-family.json                    # about 5.5 min
uv run python experiments/CJ-0001-collins-shor-peak/slope_family_extension.py --max-n 200     --out experiments/CJ-0001-collins-shor-peak/results/slope-family-extension.json          # about 3 s
uv run python experiments/CJ-0001-collins-shor-peak/slope_family_verify.py     --out experiments/CJ-0001-collins-shor-peak/results/slope-family-verify.json             # under 1 s
```

The exhaustive runs are deterministic. The sampled run is deterministic given
the seed. Timing fields in the result files vary between runs.

## Provenance of the stored result files

Each result file has a `run` block with the command line, the Git revision, the
state of the working tree and the dependency versions. Two caveats:

- `results/exhaustive-21-23.json` was produced on 2026-11-26 before the first
  commit of the repository, by the version of `exhaustive.py` and `distpoly.py`
  committed at `e34acfc`, and has no `run` block. It has not been rerun since.
- The other five files were regenerated in one batch at revision `ed232ec`.
  The first of them records a clean tree; the later ones record
  `tree_clean: false` only because the earlier runs of the same batch had just
  rewritten result files. All numbers were identical to the first run.

## What the exhaustive search covers

For each order `n`, one tree per isomorphism class, generated by the
Wright–Richmond–Odlyzko–McKay successor functions of networkx 3.7 (private
functions `_next_tree` and `_next_rooted_tree`; the dependency is pinned). The
number of trees generated is compared with OEIS A000055 for every order, and for
orders up to 10 the trees are checked to be pairwise non-isomorphic with an
independent canonical form.

On every tree the run also checks Graham–Pollak (`d_0 = n − 1`) and unimodality;
a failure of either would indicate a computational error and is reported as a
guard failure. There were none.

| Orders | Trees | Violations | Result file |
| --- | ---: | ---: | --- |
| 3–20 | 1,346,022 | 0 | `results/exhaustive-03-20.json` |
| 21–23 | 22,596,335 | 0 | `results/exhaustive-21-23.json` |

"No violation" means: among all trees of these orders. It is not a proof of the
conjecture.

## The slope family (objective O7): `slope_family.py`

Question. With the notation of `notes/gamma-components.md` (weighted tree
`(T, ν)`, `M = I + x(L_T + diag ν)`, `Φ = det M`, `p_v = 1 + (2 − k_v − ν_v)x`,
`π_u = e_uᵀ adj(M) p`, cones `C_d`) and

`F(T, ν, u) = (1 + 5x + 3x²)Φ(T, ν) + (x + 4x²) adj(M(T, ν))_{uu} + 2x² π_u(T, ν)`:

1. (E″), with `ν = 0` included: is `F(T, ν, u) ∈ C_{j+2}`?
2. For a leaf `w ≠ u` with neighbour `v`, `n = ν_w`, `m = 1 + (1+n)x`,
   `θ = x(1 + nx)`: the identities
   `F(T, ν, u) = m F(T−w, ν, u) + θ F(T_c, ν + e_{v_c}, u) Π_{l≠c} Φ_l − 4n x⁴ adj(M(T−w, ν))_{uv}` (`v ≠ u`),
   `F(T, ν, u) = m F(T−w, ν, u) + [x + (5+n)x² + (3+5n)x³ − n x⁴] adj(M(T−w, ν))_{uu}` (`v = u`),
   `F(T, ν, u) − F(T, ν − e_w, u) = x [F(T−w, ν + e_v, u) − 2x³ adj(M(T−w, ν))_{uv}]` (`ν_w ≥ 1`).
3. (S): is `x [F(T, ν + e_v, u) − 2x³ adj(M(T, ν))_{uv}] ∈ C_{j+3}` for all
   vertices `u, v`?

Inputs: `--max-order J`, `--max-weight W`, `--time-limit` (seconds, default
600; the run stops there and records where), `--out`. Search space: one tree
per isomorphism class with `1 ≤ j ≤ J` vertices (`networkx.nonisomorphic_trees`;
the single vertex for `j = 1`), every weight in `{0..W}^j` on its labelled
vertices (zero included; weightings that differ by an automorphism are counted
separately), every vertex `u`, every leaf `w ≠ u`, every ordered pair `(u, v)`.
Algorithm: `det` and `adj` of `I + xL` by the Faddeev–LeVerrier recursion on
integer matrices (exact divisions asserted), polynomials as lists of Python
integers, the half-gamma expansion of `component_form.py`. No floating point.

Stored run (`J = 6`, `W = 4`; 14 trees, 104,530 weighted trees; 330 s):

| Check | Cases | Failures |
| --- | ---: | ---: |
| (E″), `ν = 0` | 65 | 0 |
| (E″), `ν ≠ 0` | 614,740 | 1 |
| leaf identity, `v ≠ u` | 1,403,375 | 0 |
| leaf identity, `v = u` | 359,675 | 0 |
| slope identity | 1,410,440 | 0 |
| (S) | 3,630,605 | 7,225 (31 with `j = 5`, 7,194 with `j = 6`; none with `j ≤ 4`, none with `ν = 0`) |
| bracket of (S) in `C_{j+2}` | 3,630,605 | 7,655 |

The three identities hold on the whole range. **(S) and (E″) are false as
stated.** Smallest failure of (S) found (least order, then least total
weight): the star with four leaves, centre of weight 0, leaves of weights
2, 3, 4, 4, `u = v` the centre:
`S = x + 28x² + 324x³ + 1994x⁴ + 6905x⁵ + 12765x⁶ + 9824x⁷ − 5x⁸`.
The failure of (E″): the star with five leaves, centre of weight 0, every leaf
of weight 4, `u` the centre: `F = (1 + 5x)⁴ (1 + 16x + 84x² + 164x³)` has
degree 7, and a polynomial `P ∈ C_8` has `[x⁸]P ≥ P(0)`. (This one is checked
by hand in the tests.) The bracket of (S) has constant term 1 and degree at
most `j + 2`, so for the same reason it is never in `C_{j+3}`; the result file
records that count (all cases).

`slope_family_extension.py` (`--max-n 200`): for each of the 5 stored failures
of (S), a new leaf of weight `n` attached at `v` gives a failure of (E″) on 6
vertices at `n = 14` (leaf weights 2, 4, 4, 4, 14) or `n = 59`; and statement
(E) of `notes/gamma-components.md` on the trees obtained by attaching one more
leaf at `u` **holds** for every `n = 1..200` (1,000 cases, 0 failures), as it
does for the stored failure of (E″). `slope_family_verify.py` confirms, by a
different method, the hypotheses and the violation for the 5 failures of (S)
and the 6 failures of (E″), and the 6 values of `E`.

These are finite exact checks. They establish the identities on the range
computed and nothing more; the failures are counterexamples to (S) and (E″)
as stated in `STATE.md` (statements of this investigation, not the published
conjecture), and they say nothing against (E), Γ_c or Conjecture Γ.

## The rooted state, and statement (Λ): `rooted_state.py`

Session 8, [`notes/rooted-calculus.md`](../../research/active/CJ-0001-collins-shor-peak/notes/rooted-calculus.md).
Exact Python integers; importable (the computation runs only under
`__main__`). For a weighted tree `(T, ν)` and a root `u` it computes, each
from its definition, `Ψ`, `H`, `G`, `Ω`, `R`, `F`, `Λ` and the polynomial of
statement (S), and checks:

- Part A: the identities of Propositions S19 and S20 (raising the root
  weight, a new root above, merging two rooted trees, the increment of `R` at
  a new leaf and at any vertex), and that `G` and `Ω` have non-negative
  coefficients;
- Part B: the cone memberships (E″), (S), (Λ), monotonicity of `R` in one
  weight, and Γ_c;
- Part C: the leading coefficient of `F` on stars (Proposition S21) and
  Part B on rooted stars with heavy leaves;
- Part D: Part B on random trees (fixed seed).

```sh
uv run python experiments/CJ-0001-collins-shor-peak/rooted_state.py --star-weight 5 --random-trials 600 --out experiments/CJ-0001-collins-shor-peak/results/rooted-state.json   # about 2.5 min
```

Stored run (`results/rooted-state.json`, revision and tree state in its
provenance block; 146 s):

| Range | Rooted trees | Identity failures | (E″) fails | (S) fails | (Λ) fails | monotonicity fails | Γ_c fails |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| all trees, `j ≤ 5`, weights 0 to 2, every root | 4,395 (and 10,404 merges, `j ≤ 3`) | 0 | 0 | 0 of 21,099 | 0 | 0 of 4,366 | 0 of 4,366 |
| stars, at most 6 leaves, leaf weights 0 to 5, centre 0, 1, 3 (2,769 stars) | 11,085 | 0 (leading coefficient) | 185 | 3,354 of 69,297 | 0 | 0 of 11,073 | 0 of 11,073 |
| 600 random trees, 2 to 9 vertices, weights up to 20, seed 20261126 | 3,269 | — | 37 | 411 of 21,109 | 0 | 0 of 3,213 | 0 of 3,213 |

The field `named_examples` holds the counterexamples quoted in the note (the
star with five leaves of weight 4 for (E″); four leaves of weight 4 for (S)).
These are finite exact checks: the identities are proved in the note and
confirmed here on the range computed; for (Λ), monotonicity and Γ_c the
absence of failures is evidence on that range, not a proof. Regression test:
`tests/test_cj0001_rooted_state.py`.

## The Wiener form and the leaf recursion (session 9): `wiener_form.py`, `leaf_telescoping.py`

Notes: `research/active/CJ-0001-collins-shor-peak/notes/wiener-form.md`
(Lemma S24, Propositions S25 and S26, Theorem T4) and
`notes/leaf-telescoping.md` (Propositions S23 and S27, statement (SM)). Both
scripts use exact integers, import `distpoly.py` and `rooted_state.py`, and
read the revision and the state of the tree before the computation starts.

`wiener_form.py`, for every tree of order 2 to `--max-order`: the identity
`n^2 l_T = 4(W - nx) Phi + sum_{u<v} (t_u - t_v)^2 x^(d-1) Pi_uv` with `l_T`
from the characteristic polynomial of the distance matrix (W1); the adjugate
of `I + xL` entry by entry against the product over the components off the
path (W2); the cone memberships (W3); the sign of every pair term (W4) and of
the main term (W5) in the proof of Theorem T4; the inequality
`d_{mu-1} < d_mu`, `mu = floor((n-1)/2)` (W6); the decomposition (W7);
`W >= (n-1)^2` (W8). Then W6 alone up to `--peak-order`.

`leaf_telescoping.py`, part A (every tree of order 1 to `--max-rooted`, every
vertex): the Laplacian formula against the distance matrix, `R(T, 0)`, the
leaf recursion, the telescoped formula, `r_u in C_n`, its lower bound,
`R(T, e_u) in C_{n+1}` and `Phi(T, e_u) - (1+x)^n in C_n`. Part B (every tree
of order 3 to `--max-order`, from the distance matrix only): the closed form
of the star, `l_T - l_star in C_{n-1}` (statement (SM)),
`l_T + 4x(1+x)^(n-1) in C_{n-1}`, and the smallest gap.

```sh
cd experiments/CJ-0001-collins-shor-peak
uv run python wiener_form.py --max-order 12 --peak-order 19 --out results/wiener-form.json          # about 2 min
uv run python leaf_telescoping.py --max-rooted 11 --max-order 20 --out results/leaf-telescoping.json   # about 6 min
```

Stored runs (clean tree at start): `results/wiener-form.json` at `f414cd8`
(987 trees and 56,764 pairs for W1 to W8; 499,372 trees of order 13 to 19 for
W6; 0 failures), `results/leaf-telescoping.json` at `6c23eea` (4,394 rooted
trees in part A; 1,346,023 trees of order 3 to 20 in part B; 0 failures).
Regression test: `tests/test_cj0001_wiener_form.py`. These are finite checks;
Theorem T4 rests on its written proof, and (SM) is a conjecture.

## The even orders (session 10): `even_order.py`

Note: `research/active/CJ-0001-collins-shor-peak/notes/even-order.md`
(Propositions S28 to S30, statement (SM⁺), Finding S31). Exact integers;
`ℓ_T` from the characteristic polynomial of the distance matrix
(python-flint); determinants `det (I + xL)[V ∖ S]` by python-flint and, for
part C2, also by a recursion over the forest in pure Python integers.

- Part A, every tree of order 2 to `--max-a` and every root: the rooted form
  (S28) and the explicit leaf polynomial (S29).
- Part B, every tree of order 3 to `--max-b`: `Ω_T` has non-negative
  coefficients (S30(b)); `Ω_T ∈ C_{n−1}` (statement (SM⁺), a conjecture);
  `Θ_T − (n−1)(1+x)^{n−2} ∈ C_{n−2}`.
- Part C, inequality (3) of `wiener-form.md`: C1, the sign of its right side
  for every tree of even order 6 to `--max-c`; C2, the same for the spiders
  with `(n−2)/2` legs of length 2 and one pendant vertex, even `n` in
  `--family lo hi`, by the two implementations, together with the sign of
  `d_m − d_{m−1}` from the distance matrix.

```sh
uv run python even_order.py --max-a 9 --max-b 15 --max-c 14 --family 80 110 --out results/even-order.json   # about 2 min
```

Regression test: `tests/test_cj0001_even_order.py`. Finite checks: S28 to
S30 rest on their written proofs, (SM⁺) is a conjecture, and S31 (the right
side of inequality (3) is negative from `n = 100` in that family) is a
computation on the stated range.

## The lower bound `⌊n/2⌋` (session 11): `lower_bound.py`

Note: `research/active/CJ-0001-collins-shor-peak/notes/lower-bound.md`
(Propositions S33 to S36, Theorems T5 and T6). Question: do the identities
and the cone memberships stated there hold on small trees? Exact integers;
imports `distpoly.py` (enumeration of trees, `d_k` from the characteristic
polynomial of the distance matrix, python-flint) and `rooted_state.py` (the
state `(Ψ, H, G, Ω, R)` of a rooted tree, each entry from its definition;
`det` and `adj` of `I + xL` by the Faddeev–LeVerrier recursion). No floating
point.

Inputs: `--max-rooted`, `--max-merge`, `--max-pairs`, `--max-contract`,
`--time-limit` (seconds, default 300; tested before each order of each part,
the run stops there, records where and exits with status 2), `--out`. Exit
status 1 if any check fails. Every failing check stores its first instance in
the result file.

- Part A, every rooted tree of order 1 to `--max-rooted`, one per isomorphism
  class of rooted trees (the trees of `distpoly.layouts`, every vertex as
  root, duplicates removed by the canonical code of the rooted tree; the
  count per order is compared with OEIS A000081): S33(b), (c), (e) with
  `a_v = x^{δ_v−1} Π_{uv}` computed from the minor `Π_{uv}` of its definition
  (and `x a_v = adj(M)_{uv}`, Lemma S24); S34(a); S34(b) and the other plant
  rules against the state of the planted tree computed from its definition;
  the memberships `Ψ ∈ C_{a−1}`, `H ∈ C_{a−2}`, `G/x ∈ C_{a−1}`, `Ω ∈ C_a`,
  `E ∈ C_{a+1}`, `R(A, e_u) ∈ C_{a+1}`, `Q¹ ∈ C_a`, `a_v ∈ C_{a−2}`,
  `a_v ∈ C_{a+δ_v−3}` and `r_u − (1+4x)(1+x)^{a−1} ∈ C_a` (Theorem T6(a)).
- Part B, every pair of these rooted trees of orders `a_1 ≤ a_2` with
  `a_1 + a_2 − 1 ≤ --max-merge` (every ordered pair when `a_1 = a_2`): the
  merge rules for `Ψ, H, G, Ω` and S34(c) against the state of the merged
  tree; the identity of S35, its left side taken from the states of the two
  planted trees, and that left side in `C_{a_1+a_2+2}`.
- Part C, every pair of orders `a ≤ b` with `a + b ≤ --max-pairs`: the trees
  `T` and `T′` of Proposition S36 are built, `ℓ` is taken from the distance
  matrix (and compared with `(R(T, 0) + (1+4x)Φ_T)/x`, S23(a)), and
  `ℓ_T − ℓ_{T′}` is compared with the formula of S36 and tested for
  membership in `C_{n−1}`. The pairs with `a = 1` (a pendant edge, `T = T′`,
  both sides zero) are outside the hypothesis of S36 and are counted apart.
- Part D, every tree of order 4 to `--max-contract` and every non-pendant
  edge, from the distance matrix only: `ℓ_T − ℓ_{T′} ∈ C_{n−1}`,
  `λ_m(ℓ_T − ℓ_{T′}) ≥ 0` for `m = ⌊n/2⌋`, and the coefficient of `x`
  (Remark 1 of S36).
- Part E, Theorem T6(b), (c) directly, every tree of order 2 to
  `--max-contract`, from the distance matrix only: the closed form
  `ℓ_{S_n} = (1+x)^{n−2}[(n−1) + 4(n−2)x − 4x²]` against the distance matrix
  of the star; `ℓ_T − ℓ_{S_n} ∈ C_{n−1}`; for `n ≥ 3`,
  `d_m(T) − d_{m−1}(T) ≥ d_m(S_n) − d_{m−1}(S_n) > 0` and every maximizing
  index at least `m = ⌊n/2⌋`; the value of the star for even `n` (Remark 3).

The note states its memberships in the cones `K_d`. The script tests
membership in `C_d` at the same index, which is equivalent for a polynomial
of degree at most `d` ((K1) and (K4) of the note) and is counted as a failure
if the degree is larger. Membership in `K_d` is not tested as such.

```sh
uv run python experiments/CJ-0001-collins-shor-peak/lower_bound.py --max-rooted 9 --max-merge 9 --max-pairs 10 --max-contract 16 \
    --out experiments/CJ-0001-collins-shor-peak/results/lower-bound.json                      # about 1 min
```

Stored run (`results/lower-bound.json`; 53.8 s; budget fixed beforehand: 5
minutes; completed):

| Part | Range | Objects | Checks | Failures |
| --- | --- | ---: | ---: | ---: |
| A | rooted trees of order 1 to 9 | 486 rooted trees (3,534 pairs `(u, v)`) | 20,331 | 0 |
| B | merged order at most 9 | 1,064 pairs | 4,256 | 0 |
| C | `a + b ≤ 10` | 1,064 pairs (486 with `a = 1`) | 5,320 | 0 |
| D | trees of order 4 to 16 | 32,505 trees, 220,181 pairs (tree, non-pendant edge) | 880,724 | 0 |
| E | trees of order 2 to 16 | 32,507 trees | 130,062 | 0 |

Provenance (corrected in session 13): the stored result is the run at
revision `b1359cc` on a clean tree (`tree_clean: true`; 53.8 s), committed at
`6e6432c`. An earlier run at `74d65b0` on a dirty tree (61 s; the script and
its test not yet committed, and a file of another session modified), which
this paragraph used to describe, was overwritten. The `sources` block of the
result file holds the SHA-256 of `lower_bound.py`, `distpoly.py` and
`rooted_state.py`.

Differences from the scratch computations of session 11 that the note
quotes: part B includes the pairs with `a_1 = 1`, `a_2 = 9`, which the
scratch loop left out (1,064 pairs instead of 778; the 778 are the pairs with
both orders at most 8); the left side of S35 comes from the planted trees
themselves instead of the plant rules; `a_v` comes from the minor instead of
the adjugate; `ℓ` in part C comes from the distance matrix instead of
S23(a); rooted trees are identified by a canonical code instead of by their
state (the same 486 classes); the checks of Lemma S24, S19(c), (d), S33(a) at
the index `a + δ_v − 3`, T6(a), Remarks 1 and 3, and part E are additions.
S34(d) (merge of several trees) is not tested directly.

Regression test: `tests/test_cj0001_lower_bound.py` (10 tests, about 2 s:
values by hand, the five parts on small orders, three negative controls in
which a wrong formula is reported as a failure, and the stored result).
These are finite checks on the stated ranges. They do not prove S33 to S36,
T5 or T6, which rest on the written proofs of the note (unreviewed at the
time of the run), and they say nothing about trees outside the ranges.

## The generalized tree shift and path maximality (session 12): `tree_shift.py`

Question. Finite exact checks of the statements of
`research/active/CJ-0001-collins-shor-peak/notes/path-maximality.md` (draft, not
reviewed): Lemma S37 (difference under a shift), Proposition S38, Theorems T7 and
T8, Lemma S39; and a falsification attempt on statement (PM), which is an
**open** conjecture, not a statement with a proof in the note: along every
generalized tree shift `T -> T'`, `pmax(T') <= pmax(T)` and `pmin(T') <= pmin(T)`
(`pmax`, `pmin`: largest and smallest index maximizing `d_0, ..., d_{n-2}`).
Arithmetic: Python integers and `python-flint` (as `lower_bound.py`), `Fraction`
for margins; no floating point supports a claim (decimals of margins are labelled
exploratory). Membership in `K_d` at any degree is decided from the unique
coordinates in the basis `x^e (1+x)^(d-2e)` (`2e < d`), `x^e` (`2e >= d`).

Command of the stored run (from the repository root; part A needs sympy, which is
not a project dependency, hence `--with`; without sympy part A is skipped and
recorded as skipped):

    uv run --with sympy==1.14.0 python experiments/CJ-0001-collins-shor-peak/tree_shift.py \
        --out experiments/CJ-0001-collins-shor-peak/results/tree-shift.json

Defaults (chosen after timing, fixed before the stored run): `--k-max 6 --n-b 11
--n-c 15 --n-d 17 --n-e 15 --e-orders 20,30,45,60,80,100,120,150 --e-sample 200
--e-sample-big 50 --e-big-from 60 --e-random-trees 200 --e-random-shifts 20
--e-random-orders 30,100 --n-f 2000 --seed 20261127 --time-limit 570`. Budget: 10
minutes of wall-clock for the stored run; it took 298.9 s and completed every part.
Versions: python 3.12.4, python-flint 0.9.0, networkx 3.7, sympy 1.14.0 (part A).

| Part | Search space (exact) | Size | Cases | Failures |
| --- | --- | --- | --- | --- |
| A (sympy) | `det(I - tJ) = (1 - xt)Q(t)^2`; `Delta_k = c_k`, `k = 1..12`, free state variables | 1 + 12 | 13 | 0 |
| B | pairs of rooted trees (one per class), `a, b >= 2`, `a <= b` (both orders for `a = b`), `k = 1..6`, `n = a+b+k-1 <= 11` | 2,371 pairs | 26,089 | 0 |
| C | every tree of order 5..15 and every generalized shift (unordered end pair `x < y`) | 13,183 trees, 127,192 shifts | 381,576 | 0 |
| D | every tree of order 4..17 (`T8`); Lemma S39 recipe on every non-path tree of order <= 15, two splits of the neighbours | 81,134 trees | 296,094 | 0 |
| E(i) | every tree of order 5..15, every shift | 13,183 trees, 127,192 shifts | 254,384 | 0 |
| E(ii) | double stars, brooms, spiders, caterpillars (about 28 trees per order) at orders 20, 30, 45, 60, 80, 100, 120, 150; every shift if at most 200 (n <= 60: 200, above: 50 sampled with the seed) | 223 trees, 10,812 shifts tested | 21,624 | 0 |
| E(iii) | 200 random Pruefer trees of order 30..100, 20 random shifts each | 4,000 shifts | 8,000 | 0 |
| F | the path, `n = 3..2000` from Collins's closed form, against the distance matrix for `n <= 60` | 1,998 | 4,054 | 0 |

What is checked. B: for actual graphs `T_k`, `T'_k` (built from the edge lists,
`l` from the distance matrix, states of `(A,u)`, `(B,v)` from their definitions,
`E = R - Omega + (1+2x)^2 Psi - 2xG`) the identity of Lemma S37 with
`a_j` (also checked against the tridiagonal determinant at integer points),
`gamma_k`, `rho_k`; each of the four terms in the cone `K` at the index of
Proposition S38 (`K_{n-1}`, `K_n`, `K_n`, `K_{n-1}`, and the three pieces of the
last term), and the difference in `C_{n-1}`. C: `l_T - l_T'` in `C_{n-1}` (also in
`K_{n-1}` and coefficientwise `>= 0`). D: `l_{P_n} - l_T` in `C_{n-1}`; equality
`l_T = l_{P_n}` only for the path (14 trees in total, one per order 4..17, the
paths); the reversed difference is not in the cone for the 81,120 other trees; for
every non-path tree of order <= 15 the preimage `T_k(A,B)` built by the recipe of
the proof is a tree with exactly one leaf fewer, its shift along the path from `z`
to `w` is isomorphic (networkx `is_isomorphic`) to the original, and `a, b >= 2`.
E: the statement (PM) as above; a violation would be re-verified by an independent
method (Faddeev-LeVerrier on a breadth-first distance matrix, which shares no
code with the flint charpoly; it is tested, not triggered) and stop the run.
F: from `d_{n-k}(P_n) = C(n+k-1, 2k-1)(k-1)n/k` (`2 <= k <= n`).

Result. No failure in any part; no violation of (PM) among the trees and shifts
listed in the table (finite evidence about an open statement, nothing more).
Closest margin, exact (`margin1`: `(max_{j<=p} d_j(T') - max_{j>p} d_j(T')) /
max d(T')` with `p = pmax(T)`, positive exactly when `pmax(T') <= p`; `margin2`:
the same at `p = pmin(T)`, non-negative exactly when `pmin(T') <= p`): E(i)
`607/110068` (0.0055, order 15, `k = 1`); E(ii) about 0.00140 (order 120, a
caterpillar with one vertex of degree 20, `k = 1`; exact fraction in the result
file); E(iii) about 0.00234 (order 80, `k = 1`). `margin1 = margin2` in all three
because `pmax = pmin` at the minimizers. The margins are thin but positive, and
shrink with the order in these families. F: for every `n = 3..2000` the peak of
`d_k(P_n)` is unique (`pmax = pmin`) and equals either `M = n - isqrt(n^2 // 5)`
(that is `ceil(n - n/sqrt 5)`) in 393 cases, or `M - 1` (`floor`) in 1,605 cases;
no `n` is neither, so `pmax(P_n) <= M` and `pmin(P_n) >= M - 1`. For `n <= 60` the
peak is `M` exactly for `n` in {9, 18, 27, 36, 45, 47, 54, 56} (the full lists for
the floor case are in the result file, truncated beyond 400 entries).
Agreement with the note: the note's scratch counts (T8 on the 81,134 trees of
order 4..17; no tree other than the path with `l_T = l_{P_n}` for `n <= 17`) are
reproduced; T7 is now checked through order 15 instead of 13.

Provenance: revision `8b03309` with `tree_clean: false` (the script, its test and
the result file were not yet committed; no other file was modified). The
`sources` block holds the SHA-256 of `tree_shift.py`, `lower_bound.py`,
`distpoly.py`, `rooted_state.py`; the last three were identical to their blobs at
that revision, `tree_shift.py` is not in the revision.

Regression test: `tests/test_cj0001_tree_shift.py` (about 2 s: membership in `K_d`
by hand, shifts by hand, the independent method against flint, the sequences of
S37 by hand, the lemma on small orders, a negative control with a wrong
coefficient in the `G-hat G-hat` term, a reversed difference and a reversed shift
reported as failures, the path, part A when sympy is importable, and the stored
result). These are finite checks. They do not prove S37, S38, T7, T8, S39 (those
rest on the written proofs of the note, unreviewed) and say nothing about trees
outside the ranges; part E is evidence about an open statement, and the E(ii),
E(iii) samples are not exhaustive.

## The trace of `(I+L)^{-1}` and the peak bound (session 13): `upper_bound.py`

Question. Finite exact checks of the ingredients of an upper bound on the peak
index of `d_0, ..., d_{n-2}` through `tr(T) := trace (I+L)^{-1}` (`L` the
Laplacian), computed exactly as `-p'(-1)/p(-1)`, `p(y) = det(yI - L)`. The
checks concern statements to be used in a proof; none of them is a proof.
Arithmetic: Python integers, `Fraction`, `python-flint`. Two items are not exact
and are labelled so in the code and in the result file: part B2 (50 significant
digits with `decimal`: `high-precision numeric`) and part F (`EXPLORATORY`,
floating point). Decimal renderings of exact margins are labelled
`decimal_exploratory`.

Command of the stored run (from the repository root):

    uv run python experiments/CJ-0001-collins-shor-peak/upper_bound.py \
        --out experiments/CJ-0001-collins-shor-peak/results/upper-bound.json

No seeds (everything is exhaustive or a closed form). Defaults: `--v-max 9 --n-a 20
--n-c 18 --n-path 2000 --n-b1 200 --n-b2 60 --x-max 8 --pq-max 8 --n-e 60 --n-f 14
--m-size 6 --time-limit 780`. Budget fixed before the run: 15 minutes of
wall-clock in total; the stored run took 298.7 s and completed every part (a first run on a dirty tree took 293.2 s, same results; it was overwritten). Versions:
python 3.12.4, python-flint 0.9.0, networkx 3.7. `numpy` is not installed, hence
part F takes the eigenvalues from the flint complex roots of the characteristic
polynomial of `D` (midpoints of the enclosures, converted to floats).

| Part | Statement checked | Search space (exact) | Cases | Failures |
| --- | --- | --- | --- | --- |
| V | `tr` by three methods (charpoly of `L`; flint exact inverse; `Fraction` Gauss-Jordan sharing no code with flint) agree; by-hand values `tr(P_1)=1`, `tr(P_2)=4/3`, `tr(P_3)=7/4`, `tr(K_{1,3})=11/5`; a continuant formula for `tr(P_n)` equals the charpoly value | every tree of order 1..9 (95 trees), the path `P_n`, `n = 1..40` | 139 | 0 |
| A | `tr(T) >= tr(P_n)`, equality only for the path | every tree of order 2..20 (1,346,023 trees) | 2,692,065 | 0 |
| B1 | `tr(P_n) - 2/5 > n/sqrt 5` (squares compared in Q, both sides positive) | `n = 1..200` | 400 | 0 |
| B2 | `tr(P_n) = n/sqrt5 + 2/5 + (2n/sqrt5) r^{2n}/(1 - r^{2n})`, `r = phi^{-2}`, to 50 significant digits (high-precision numeric, working precision 90 digits) | `n = 1..60` | 60 | 0 |
| C (path) | every maximizing index `p` satisfies `5 n^2 < (5(n-p)+3)^2` (exactly `p < n - n/sqrt5 + 3/5`); the coefficients come from Collins's closed form `d_{n-k}(P_n) = C(n+k-1, 2k-1)(k-1)n/k`, equal to the distance-matrix value for `n <= 30` | `P_n`, `n = 3..2000` | 2,026 | 0 |
| C (trees) | the same condition for every maximizing index of every tree | every tree of order 3..18 (205,002 trees) | 205,003 | 0 |
| D | `tr(T(p,q)) > tr(T(p+q,0))` | rooted trees `(X,v)` with `2 <= |X| <= 8` (199 classes), pairs `1 <= q <= p`, `p+q <= 8` (16 pairs) | 3,184 | 0 |
| E | `c(0) >= c(r)`, equality only at `N = 2, r = 1` | `P_{N+1}`, `N = 2..60`, `1 <= r <= N-1` (1,770 pairs) | 1,771 | 0 |
| M | `g_T = 1/(1+eps_A+eps_B)` and `tr(T) = tr(A) + tr(B) - g_T - g_T(eps_B kappa_A g_A + eps_A kappa_B g_B)`, with `g`, `k` the root entries of `(I+L)^{-1}`, `(I+L)^{-2}`, `eps = 1/g - 1`, `kappa = k/g^2` | all ordered pairs of rooted trees, `1 <= |A|,|B| <= 6` (37 classes, 1,369 pairs), glued at the roots | 2,738 | 0 |
| F (exploratory) | `sum 1/(1+beta_i) <= n - tr(T)` (tolerance `1e-9`), `beta_i = -theta_i` for the `n-1` negative eigenvalues of `D/2` (one positive, `n-1` negative checked); `n - tr(T) <= n - tr(P_n)` exactly | every tree of order 3..14 (5,445 trees) | 16,335 | 0 |

Result. No failure in any part, among the trees and parameter ranges of the
table.

- (A) The minimum of `tr(T) - tr(P_n)` over the non-paths is positive in every
  order 4..20 and increases with `n`: exactly `1/105` at order 4 (the star
  `K_{1,3}`: `11/5` against `46/21`), `5/286` at order 5, `1/51` at order 6, and
  then approaches about `0.0201626` (exploratory decimals; order 12:
  `0.02016260`, order 20: `0.02016261`). The exact fractions and the minimizing
  trees are in the result file. In this range the minimum does not tend to zero.
- (B1) The smallest margin of squares is at `n = 200` (exact rational in the
  result file). (B2) The largest relative difference is `8.3e-90`, far below the
  required `1e-50`.
- (C, path) For `n = 3..2000` the peak is unique (no tied peak) and equals
  `ceil(n - n/sqrt5) = n - isqrt(n^2 // 5)` in 393 cases and `floor` in 1,605
  cases, never anything else (the same counts as `tree_shift.py`, part F). In the
  393 `ceil` cases the minimum of the fractional part of `n - n/sqrt5` is
  `0.80128` (at `n = 1436`; `decimal`, 60 digits, high-precision numeric), above
  `2/5`, as the strict inequality requires there. The smallest exact slack
  `(5(n-p)+3)^2 - 5n^2` over the path and all trees of order 3..18 is the integer
  89 (order 4, `p = 2`).
- (C, trees) The largest peak index over all trees of order `n` is
  `1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10` for `n = 3..18`, each below
  `n - n/sqrt5 + 3/5` (2.26, 2.81, ..., 10.55).
- (D) The smallest margin is `1/105` (`X` an edge, `p = q = 1`: the star against
  `P_4`).
- (E) The only equality is `N = 2, r = 1` (`c(0) = c(1) = 3/4`); the smallest
  strict gap is `1/26` at `N = 3, r = 1`.
- (F) The smallest gap over the 5,445 trees is about 0.0179 (order 3); no
  violation. Exploratory.

Range actually run. The request was orders 2..17 for (A) and 3..16 for (C); the
first complete run with those ranges took 32 s, far below the budget, so the
ranges were extended to 2..20 and 3..18 before the stored run (the first run was
overwritten; same code, same results on the overlap). The numbers of trees per
order equal OEIS A000055 (`distpoly.layouts`, validated in
`tests/test_cj0001_distpoly.py`).

Provenance: the stored result is the run at `917d657` in a temporary clean
worktree of the repository (`tree_clean: true`, empty `dirty_files`; the main
working tree then held another agent's uncommitted Lean files), committed in
`2037b18`. The SHA-256 of `upper_bound.py` and of the modules it imports is in
the `sources` block. (An earlier run at `53421a6` on a dirty tree, with the
same code and results, was overwritten.)

Regression test: `tests/test_cj0001_upper_bound.py` (about 1 s: the trace by hand
and by three methods, small orders of A and C with the star-path difference
`1/105` by hand, the peak condition by hand and at the boundary `p = n - 1`, the
path peaks and closed form, B1, B2 with a negative control showing that a wrong
constant is detected, D on small ranges with `T(1,1) = K_{1,3}` against `P_4` by
hand, E with `P_3` by hand, M with a negative control in which the sign of the
correction term is flipped, F on small orders, and the stored result). These are
finite checks. They do not prove path minimality of `tr`, the peak bound for all
trees, or the merge identity; part F is exploratory.

## The manuscript check (session 14): `manuscript_check.py`

Question. Do the identities and cone memberships of Sections 4 to 7 of
`manuscripts/CJ-0001-collins-shor/main.tex` hold, as written there, on small
trees? The script was written from the manuscript's definitions only (root
weight `w` at the root, `R_w`, `π_w`, the branch polynomials `Ψ`, `Ω`, and
`H`, `G`, `E`); it imports nothing from the other scripts. Arithmetic: exact
(`fractions.Fraction`); every matrix polynomial is computed by evaluation at
integer points and Lagrange interpolation; `K_d` membership by the
coordinates in the basis `{x^e(1+x)^(d-2e): 2e < d} ∪ {x^e: 2e ≥ d}`.

Checks, per rooted tree of order `≤ --max-rooted` (one per isomorphism class
of rooted trees): Lemma 5.1 for `w = 0, 1, 2`; `Ψ` as the product over the
branches; Proposition 5.2(b) and (c) (raise, plant, including `Φ̂_0`);
Proposition 6.2(a), (b); Corollary 5.3(a), (b); Proposition 6.1(b), (c), (e)
(both forms of `R_1`); the memberships of Proposition 6.1, Corollary 4.4 and
Theorem 7.1. Per pair of rooted trees whose merge has order `≤ --max-merge`:
Proposition 5.2(d), Proposition 6.2(c), Proposition 6.3 (identity and
membership). Per tree of order 2 to `--max-order-sm`: Theorem 7.3(b) and (c).
(Numbers as in the manuscript compiled in session 14.)

Command of the stored run (from the repository root):

    uv run python experiments/CJ-0001-collins-shor-peak/manuscript_check.py \
        --max-rooted 8 --max-order-sm 12 --max-merge 8 \
        --out experiments/CJ-0001-collins-shor-peak/results/manuscript-check.json

No seeds (exhaustive). Budget fixed before the run: 10 minutes of wall-clock.
A scratch run with the same parameters before the script was stored took
220.8 s: 11,379 checks, 0 failures. The stored result
`results/manuscript-check.json` is the run made in a clean temporary Git
worktree at `8df6bea` (its `run` block records that revision and
`tree_clean: true`; the `--out` path in the recorded command is the
worktree's, the file was then copied here): 11,379 checks, 0 failures,
258.5 s. A second run in the main tree, started at `8df6bea` and finished
after the commit `44ca448` (which did not change the script), gave the same
counts and was discarded. Regression test:
`tests/test_cj0001_manuscript_check.py`.

## The AMW reduction and the open orders (session 15): `amw_reduction_check.py`

Exact checks for revision 3 of `manuscripts/CJ-0001-collins-shor/main.tex`
(integers, `fractions.Fraction`, and sign tests in `Q(√5)`; part E uses
python-flint for exact characteristic polynomials):

| Part | What | Range | Result of the stored run |
| --- | --- | --- | --- |
| A | matching numbers of the subdivision `S(T)` equal the coefficients of `det(I + tL_T)`; `avm(S(T)) = n − tr(I+L_T)^{−1}` | every tree of order 2..9 (94) | 0 failures |
| B | the path is the unique maximizer of `avm` | every tree of order 2..16 (32,507) | 0 failures |
| C | `avm(P_N) > aN + b`, `a = (5−√5)/10`, `b = (7√5−17)/10` | `4 ≤ N ≤ 200` | 0 failures |
| D | orders `n` with `p(P_n) = ⌈ξ − 2/5⌉` (so `p(T) ≤ p(P_n)` for every tree by Theorem 10.1), from the criterion of Lemma 11.1 | `3 ≤ n ≤ 2000` | 799 with fractional part of `ξ` below `2/5`, 393 more with `p(P_n) = ⌈ξ⌉`, 806 open (first 3, 5, 7, 8, 10) |
| E | ties among the maximal coefficients | every tree of order 13 (1,301) | one tie, indices 6 and 7, value 189972 |

Command of the stored run (from the repository root):

    uv run python experiments/CJ-0001-collins-shor-peak/amw_reduction_check.py \
        --out experiments/CJ-0001-collins-shor-peak/results/amw-reduction-check.json

Defaults: `--max-identity 9 --max-avm 16 --max-path 200 --max-open 2000`. No
seeds. Budget fixed before the run: 5 minutes. The stored result was made in a
clean temporary Git worktree at `f695cbd` (`tree_clean: true`), 19.7 s, 0
failures. Regression test: `tests/test_cj0001_amw_reduction.py`. Exploratory
only, not stored: eq. (8) of arXiv:1903.09825 agrees with the exact `avm(P_N)`
for `N ≤ 80` to 50 digits (60-digit floating point).

## Limits

- Orders 21–23 were computed by one implementation (with the guards above). The
  independent method was compared on every tree only up to order 9, and on
  selected trees of order 20.
- The sampled run is evidence only about the 10,000 trees it drew.
- `near_star_families.py` examines balanced caterpillars with spine length at
  most 80 (at most 16 for the table by spine length); other shapes are not
  covered.
- Order 24 (39,299,897 trees) would take roughly an hour on this hardware and
  was not run.
