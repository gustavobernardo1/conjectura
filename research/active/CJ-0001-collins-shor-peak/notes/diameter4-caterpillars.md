# CJ-0001 — the caterpillars K(a,0,c): the peak is at ⌊n/2⌋

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 4. Review status and novelty are recorded in
`research/discoveries.json` (record MD-0008) and in `../STATE.md`, not here.
Nothing in this file is a claim of novelty.

This file continues [`spine3.md`](spine3.md) (Theorem T2) and uses its
notation and its Lemmas C1 and C2. `T` is a tree of order `n`, `D` its distance
matrix, `δ_k` the coefficient of `x^k` in `det(D − xI)`,
`d_k = 2^{k−(n−2)} |δ_k|` for `0 ≤ k ≤ n−2`, and
`ℓ_T(x) = −2^{−(n−2)} det(2xI − D)`, whose coefficient of `x^k` is `d_k` for
`0 ≤ k ≤ n−2` (Fact 1.1 and Observation 3.1 of arXiv:1507.02341). `C(N, i)` is
the binomial coefficient, equal to `0` when `i < 0` or `i > N`.

For integers `a, c ≥ 1`, `K(a,0,c)` is the tree with a path `v_1 v_2 v_3` in
which `v_1` carries `a` pendant leaves, `v_3` carries `c` pendant leaves and
`v_2` none. Its order is `n = a + c + 3 ≥ 5`, and `K(1,0,1)` is the path `P_5`.
Throughout `m = ⌊n/2⌋`, `u = a + c = n − 3` and `v = ac`.

## T3. Statement

**Theorem T3.** Let `a, c ≥ 1` be integers with `a + c ≥ 3`, `T = K(a,0,c)`,
`n = a + c + 3 ≥ 6` and `m = ⌊n/2⌋`. Then

1. `d_{m−1}(T) < d_m(T)`;
2. `d_{m+1}(T) < d_m(T)`.

Consequently `m = ⌊n/2⌋` is the only index at which `d_0(T), …, d_{n−2}(T)`
attains its maximum, and Conjecture 1.2 of arXiv:1507.02341 holds for `T`,
also in the reading in which every maximizing index must lie in the interval.

**Corollary (caterpillars of diameter 4), conditional on Theorem T2.** A
caterpillar of diameter 4 is a tree `K(a,b,c)` with `a, c ≥ 1` and `b ≥ 0`
(three spine vertices `v_1 v_2 v_3`; the two outer ones must carry a leaf for
the diameter to be 4). If T2 of `spine3.md` holds, then for every caterpillar
of diameter 4 the only maximizing index is `⌊n/2⌋`: T2 covers `b ≥ 1`, T3
covers `b = 0` with `a + c ≥ 3`, and the remaining tree is `P_5`, whose
normalized coefficients are `4, 30, 70, 50` (maximum at index `2 = ⌊5/2⌋`
only; direct computation, `diameter4.py`).

The proof of T3 uses: the argument of Lemma L3 of `lemmas.md` for a partition
into five classes (Step 1), with Fact 1.1 and Observation 3.1 of the source;
Lemmas C1 and C2 of `spine3.md` as identities between polynomials (Steps 1
and 2; both are computer-assisted, see `spine3.md`); and, in Step 4, Fact 1.1,
Theorem 2.1 of the source and the direction "if `a_{j−1} < a_j` then every
maximizing index is `≥ j`" of the general form of R1 in `lemmas.md`.

## Step 1. The formula of Lemma C1 at `b = 0`

**Lemma C1′.** Let `a, c ≥ 1` with `n = a + c + 3 ≥ 6`, and let
`g_0, …, g_6` be the polynomials of Lemma C1 of `spine3.md`. Then for
`0 ≤ k ≤ n − 2`

`d_k(K(a,0,c)) = Σ_{j=0}^{6} g_j(a, 0, c) C(n − 6, k − j)`.

*Proof.* Partition the vertices of `T = K(a,0,c)` into the five classes
`{v_1}`, `{v_2}`, `{v_3}`, `L_1` (the leaves at `v_1`) and `L_3` (the leaves at
`v_3`). The sum of the distances from a vertex to the vertices of a class
depends only on the class of the vertex, so the partition is equitable for
`D`; let `Q′` be its `5 × 5` quotient matrix. As in the proof of Lemma L3,
vectors constant on classes form a `D`-invariant subspace on which `D` acts as
`Q′`, and its orthogonal complement is spanned by vectors supported on one of
`L_1`, `L_3` with entries summing to zero, on which `D` acts as multiplication
by `−2` (two leaves of the same class are at distance 2 and have equal
distances to every other vertex). The complement has dimension
`(a − 1) + (c − 1) = n − 5`. Hence `det(xI − D) = (x + 2)^{n−5} det(xI − Q′)`
and

`ℓ_T(x) = −2^{−(n−2)} (2x + 2)^{n−5} det(2xI − Q′) = −2^{−3} (x + 1)^{n−5} det(2xI − Q′)`.

Now let `Q` be the `6 × 6` matrix of Lemma C1 of `spine3.md`, with its entries
regarded as polynomials in `a, b, c`. The variable `b` occurs only in its
fifth column, whose entries are `2b, b, 2b, 3b, 2(b−1), 3b`. At `b = 0` this
column is `(0, 0, 0, 0, −2, 0)ᵀ`, so the fifth column of `2xI − Q` is
`(0, 0, 0, 0, 2x + 2, 0)ᵀ`, and expanding along it,

`det(2xI − Q)|_{b=0} = (2x + 2) det(2xI − Q″)`,

where `Q″` is `Q` with its fifth row and fifth column deleted. The entries of
`Q″` are the distance sums between the classes `{v_1}, {v_2}, {v_3}, L_1, L_3`
given by the rules of Lemma L3 (which do not involve the leaves at `v_2`), so
`Q″ = Q′`. Lemma C1 of `spine3.md` is the identity
`−det(2xI − Q)/16 = Σ_j g_j(a,b,c) x^j` between polynomials in `a, b, c, x`;
at `b = 0` it gives `−(2x + 2) det(2xI − Q′)/16 = Σ_j g_j(a,0,c) x^j`.
Therefore, since `n − 6 ≥ 0`,

`ℓ_T(x) = (x + 1)^{n−6} · [−(2x + 2) det(2xI − Q′)/16] = (x + 1)^{n−6} Σ_j g_j(a,0,c) x^j`,

and the coefficient of `x^k` is `Σ_j g_j(a,0,c) C(n − 6, k − j)`. ∎

The restriction `n ≥ 6` is needed: for `P_5` the exponent `n − 6` is negative.

*Check.* For all 399 trees `K(a,0,c)` with `3 ≤ a + c ≤ 40`, and three larger
ones, the whole sequence given by Lemma C1′ equals the one computed from the
`n × n` distance matrix (`diameter4.py`).

## Step 2. The two differences

Lemma C2 of `spine3.md` consists of four identities between polynomials in
`m, a, c`, obtained from the formula `d_k = Σ_j g_j(a,b,c) C(n − 6, k − j)` by
substituting `b = n − 3 − a − c` and using the recurrences of the binomial
coefficients, which hold for every `m ≥ 3`. By Lemma C1′ the same formula holds
for `K(a,0,c)`, where `b = 0`, that is `a + c = n − 3`. Hence, with
`u = n − 3` (`u = 2m − 3` for even order, `u = 2m − 2` for odd order) and
`v = ac`, the four identities EL, EU, OL, OU of Lemma C2 hold for `K(a,0,c)`.
At this value of `u`:

| Case | `K* = K(m, n−3)` | `H* = (n − 4) K* + R(m, n−3)` |
| --- | --- | --- |
| EL | `20m(m+1)(2m−5)` | `2(2m−5)(50m³ − 111m² + 49m − 30)` |
| EU | `8(m+1)(2m−5)(4m−3)` | `10(2m−5)(22m³ − 39m² − 7m + 18)` |
| OL | `4(m+1)(m+2)(23m−36)` | `4(2m−3)(65m³ + 53m² − 80m − 92)` |
| OU | `12(m+1)(m+2)(m−2)` | `12(2m−3)(m+2)(5m² + 3m − 6)` |

(Substitution of `u` in the polynomials `K`, `R` of Lemma C2; verified
symbolically by `diameter4.py`, function `symbolic_check`. For instance, in
case EL, `6m² + 25m − 91 − 3(m−1)(2m−3) = 40m − 100`.)

## Step 3. Positivity

Here `n ≥ 6`, so `m ≥ 3`, and `a, c ≥ 1` gives `v = ac ≥ a + c − 1 = u − 1 = n − 4`.

**(i) `K* > 0`.** For `m ≥ 3` every factor in the second column of the table is
positive (`2m − 5 ≥ 1`, `4m − 3 > 0`, `23m − 36 > 0`, `m − 2 ≥ 1`).

**(ii)** By (i) and `v ≥ n − 4`: `vK* + R ≥ (n − 4)K* + R = H*`.

**(iii) `H* > 0` for `m ≥ 3`.** `2m − 5`, `2m − 3` and `m + 2` are positive, and

- `50m³ − 111m² + 49m − 30 = m²(50m − 111) + 49m − 30 ≥ 39m² + 49m − 30 > 0`;
- `22m³ − 39m² − 7m + 18 = m²(22m − 39) − 7m + 18 ≥ 27m² − 7m + 18 > 0`;
- `65m³ + 53m² − 80m − 92 = m(65m² − 80) + (53m² − 92) > 0`;
- `5m² + 3m − 6 > 0`.

Since the scale factors `σ_E`, `σ_O` and the binomials `c_0`, `e_0` of Lemma C2
are positive, `d_m − d_{m−1} > 0` and `d_m − d_{m+1} > 0` in both parities.
(The index `m + 1` is at most `n − 2` because `n ≥ 6`.) ∎ (parts 1 and 2)

## Step 4. The peak

As in Step 4 of `spine3.md`: the sequence is positive (Fact 1.1) and
log-concave (Theorem 2.1); by the general form of R1 applied to the sequence
and to its reversal, parts 1 and 2 give that `m` is the only maximizing index;
and `⌊n/2⌋ ≤ ⌈n − n/√5⌉`. ∎

## Remarks

**Dependence on T2.** T3 itself does not use Theorem T2, only Lemmas C1 and C2
of `spine3.md`. The corollary uses T2.

**Relation to the range of `u` in T2.** In T2 (`b ≥ 1`) the largest value of
`u` is `n − 4`; here `u = n − 3`. The polynomial `H(m, u) = (u−1)K + R` of T2
is therefore evaluated one step beyond the range treated there.

## Checks

`experiments/CJ-0001-collins-shor-peak/diameter4.py` (exact arithmetic), result
file `results/diameter4.json`:

- `K*` and `H*` agree symbolically with `K(m, n−3)` and `(n−4)K + R` computed
  from the polynomials of Lemma C2 as stated in `spine3.py`;
- `K* > 0` and `H* > 0` for `3 ≤ m ≤ 2000` (a finite check of Step 3);
- for all 399 trees with `3 ≤ a + c ≤ 40` and three larger ones: equality of the
  whole sequence of Lemma C1′ with the direct `n × n` determinant. This is the
  check that tests Lemma C1′ against the tree;
- for every `K(a,0,c)` with `a + c ≤ 600`: the identities of Lemma C2 at
  `b = 0` between integers and `d_{m−1} < d_m > d_{m+1}`, and for `a + c ≤ 100`
  the whole sequence (positive, `m` the only maximizing index). In these two
  items the `d_k` are taken from the formula of Lemma C1′;
- `P_5`: normalized coefficients `4, 30, 70, 50` from the direct determinant.

Tests: `test_diameter4_caterpillars_without_central_leaf` in
`tests/test_cj0001_distpoly.py`.

A finite check is not a proof. The proof is Steps 1 to 4; it relies on the
computer-assisted identities of Lemmas C1 and C2 of `spine3.md`.
