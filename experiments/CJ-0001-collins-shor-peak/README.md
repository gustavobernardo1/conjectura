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
