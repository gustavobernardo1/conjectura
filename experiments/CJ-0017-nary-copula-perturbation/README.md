# CJ-0017 — the perturbation C − ∏(x_i − C) of the product copula

Exact computations for `research/active/CJ-0017-nary-copula-perturbation/notes/product-copula.md`.
All arithmetic is exact (`fractions.Fraction`) unless stated. Python ≥ 3.12,
standard library; `density_bounds_z3.py` needs `z3-solver` (5.4.1.0).

| Script | What it does | Expected output | Time |
| --- | --- | --- | --- |
| `box_search.py` | volumes of all grid cells of C_1 = Π − ∏(x_i − Π), n = 2 (den 40), 3 (den 20), 4 (den 10); prints the most negative cell | n = 2 all positive (min 79/2560000); n = 3 min −13069643/512000000000 on [11/20,3/5]×[19/20,1]²; n = 4 min −52892698073/400000000000000 | ~6 s |
| `nice_box.py` | all boxes with endpoints in (1/d)Z, d = 2..10, n = 3; first d with a negative box | d = 2, 3, 4 none; d = 5: three, most negative −23/1953125 on [3/5,4/5]×[4/5,1]² | ~1 min |
| `independent_check.py` | independent: monomial expansion of C_1 (n = 3), boundary conditions on a grid, volume of [3/5,4/5]×[4/5,1]² as the integral of the mixed partial | `CHECK PASSED ... -23/5^9 < 0` | <1 s |
| `edge_density.py` | exact polynomial t ↦ d_n(t,1,…,1), n = 2..8, and its minimum over t ∈ (1/1000)Z | e.g. n = 4: 8 − 84t + 216t² − 148t³, min −8 at t = 1; n = 5 min at t = 159/200 | ~1 min |
| `density_bounds_z3.py` | z3 nonlinear real arithmetic on the bounds of d_3 | min queries `unknown` (120 s timeout each); `d3 > 3` sat at (0, 7/8, 7/8) | ~4 min |

Commands: `uv run python <script>` from this directory (`independent_check.py`
and `edge_density.py` were run with `-I`). Run on 2026-11-27/28.
