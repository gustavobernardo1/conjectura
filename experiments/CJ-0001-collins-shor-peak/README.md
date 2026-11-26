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
| `results/*.json` | Outputs of the runs below. |

Validation: `uv run pytest tests/test_cj0001_distpoly.py` (101 tests).

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
