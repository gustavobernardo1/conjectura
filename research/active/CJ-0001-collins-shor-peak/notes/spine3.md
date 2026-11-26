# CJ-0001 — caterpillars with spine length 3: the peak is at ⌊n/2⌋

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 3. Review status and novelty are recorded in
`research/discoveries.json` (record MD-0007) and in `../STATE.md`, not here.
Nothing in this file is a claim of novelty.

Notation is that of [`lemmas.md`](lemmas.md) and
[`double-stars.md`](double-stars.md). `T` is a tree of order `n`, `D` its
distance matrix, `δ_k` the coefficient of `x^k` in `det(D − xI)`,
`d_k = 2^{k−(n−2)} |δ_k|` for `0 ≤ k ≤ n−2`, and
`ℓ_T(x) = −2^{−(n−2)} det(2xI − D)`, whose coefficient of `x^k` is `d_k` for
`0 ≤ k ≤ n−2` (Fact 1.1 and Observation 3.1 of arXiv:1507.02341). `C(N, i)` is
the binomial coefficient, equal to `0` when `i < 0` or `i > N`.

For integers `a, b, c ≥ 1`, `K(a,b,c)` is the caterpillar whose spine is a path
`v_1 v_2 v_3` and in which `v_1, v_2, v_3` carry `a, b, c` pendant leaves. Its
order is `n = a + b + c + 3 ≥ 6`. Throughout,

`m = ⌊n/2⌋ ≥ 3`, `N = n − 6 ≥ 0`, `u = a + c`, `v = ac`.

`K(a,b,c)` and `K(c,b,a)` are isomorphic. These trees are exactly the
caterpillars of diameter 4 whose central vertex carries at least one leaf.

## T2. Statement

**Theorem T2.** Let `a, b, c ≥ 1` be integers, `T = K(a,b,c)`,
`n = a + b + c + 3` and `m = ⌊n/2⌋`. Then

1. `d_{m−1}(T) < d_m(T)`;
2. `d_{m+1}(T) < d_m(T)`.

(The index `m + 1` is at most `n − 2` because `n ≥ 6`.) Consequently
`m = ⌊n/2⌋` is the only index at which `d_0(T), …, d_{n−2}(T)` attains its
maximum, and since `⌊n/2⌋ ≤ ⌈n − n/√5⌉` the Collins–Shor conjecture
(Conjecture 1.2 of arXiv:1507.02341) holds for `T`, also in the reading in
which every maximizing index must lie in the interval.

The proof uses: Lemma L3 of `lemmas.md` with spine length 3 (which rests on
Fact 1.1 and Observation 3.1 of the source for the passage from the
characteristic polynomial to the `d_k`); Theorem 2.1 of arXiv:1507.02341 (the
sequence `d_0, …, d_{n−2}` is log-concave) and Fact 1.1 of the same paper
(`(−1)^{n−1} δ_k > 0`, so the `d_k` are positive), both only in Step 4; and the general form of R1 in `lemmas.md`, only in
Step 4.

Two steps are **computer-assisted**: the expansion of a `6 × 6` determinant
with polynomial entries (Lemma C1) and the simplification of four polynomial
expressions (Lemma C2). Both are identities between polynomials with integer
coefficients; they are computed in exact arithmetic by
`experiments/CJ-0001-collins-shor-peak/spine3.py` (functions `symbolic_g` and
`symbolic_differences`), and everything needed to recompute them
independently is stated below. Steps 3 and 4 are by hand.

## Step 1. The coefficients

**Lemma C1.** For `0 ≤ k ≤ n − 2`,

`d_k(K(a,b,c)) = Σ_{j=0}^{6} g_j C(N, k − j)`,

with

- `g_0 = a + b + c + 2`,
- `g_1 = 2(ab + ac + bc) + 10a + 8b + 10c + 12`,
- `g_2 = 3abc + 9ab + 14ac + 9bc + 31a + 22b + 31c + 24`,
- `g_3 = 6abc + 12ab + 24ac + 12bc + 40a + 28b + 40c + 16`,
- `g_4 = 5ab + 12ac + 5bc + 22a + 17b + 22c − 6`,
- `g_5 = 4(a + b + c) − 12`,
- `g_6 = −4`.

*Proof.* Lemma L3 with `s = 3` and `(c_1, c_2, c_3) = (a, b, c)` gives
`ℓ_T(x) = −2^{−4} (x+1)^{n−6} det(2xI − Q)` with, in the order
(`v_1, v_2, v_3`, leaves of `v_1`, leaves of `v_2`, leaves of `v_3`),

```
      | 0   1   2   a        2b       3c      |
      | 1   0   1   2a       b        2c      |
Q  =  | 2   1   0   3a       2b       c       |
      | 1   2   3   2(a−1)   3b       4c      |
      | 2   1   2   3a       2(b−1)   3c      |
      | 3   2   1   4a       3b       2(c−1)  |
```

Expanding the determinant (computer-assisted) gives
`−det(2xI − Q)/16 = g_0 + g_1 x + … + g_6 x⁶`, and the coefficient of `x^k` in
`(x+1)^N (g_0 + … + g_6 x⁶)` is `Σ_j g_j C(N, k−j)`. ∎

*Checks.* `d_0 = g_0 = n − 1` (Graham–Pollak). The coefficient of `x^{n−1}` in
`ℓ_T` is `g_5 + g_6 N = 4(n−6) − 4(n−6) = 0` and that of `x^n` is `g_6 = −4`,
as in Observation 3.1 of the source. Each `g_j` is affine in each of `a, b, c`
(`a` occurs only in the fourth column of `Q`, `b` only in the fifth, `c` only
in the sixth) and symmetric under `a ↔ c`.

## Step 2. The two differences as polynomials

The identity `(k+1) C(N, k+1) = (N − k) C(N, k)` holds for every integer
`k ≥ 0`, and `C(N, k) = C(N, N − k)` for every integer `k`.

**Even order, `n = 2m`.** Here `N = 2m − 6` and `a + b + c = 2m − 3`. Put
`c_i = C(N, m − 3 + i)` for every integer `i`. Then `c_{−i} = c_i`, `c_0 > 0`,
and

`(m−2) c_1 = (m−3) c_0`, `(m−1) c_2 = (m−4) c_1`, `m c_3 = (m−5) c_2`, `(m+1) c_4 = (m−6) c_3`,

so that, with `σ_E = (m−2)(m−1)m(m+1) > 0`, each `σ_E c_i / c_0` (`|i| ≤ 4`) is
a polynomial in `m`:

`σ_E c_i / c_0 = Π_{0 ≤ t < |i|} (m − 3 − t) · Π_{|i| ≤ t ≤ 3} (m − 2 + t)`.

By Lemma C1, `d_m = Σ_j g_j c_{3−j}`, `d_{m−1} = Σ_j g_j c_{2−j}` and
`d_{m+1} = Σ_j g_j c_{4−j}`.

**Odd order, `n = 2m + 1`.** Here `N = 2m − 5` and `a + b + c = 2m − 2`. Put
`e_i = C(N, m − 2 + i)` for every integer `i`. Then `e_{−1−i} = e_i`,
`e_0 > 0`, and

`(m−1) e_1 = (m−3) e_0`, `m e_2 = (m−4) e_1`, `(m+1) e_3 = (m−5) e_2`, `(m+2) e_4 = (m−6) e_3`,

so that, with `σ_O = (m−1)m(m+1)(m+2) > 0`, for `0 ≤ i ≤ 4`

`σ_O e_i / e_0 = Π_{0 ≤ t < i} (m − 3 − t) · Π_{i ≤ t ≤ 3} (m − 1 + t)`.

By Lemma C1, `d_m = Σ_j g_j e_{2−j}`, `d_{m−1} = Σ_j g_j e_{1−j}` and
`d_{m+1} = Σ_j g_j e_{3−j}`; the indices that occur lie between `−5` and `3`,
and `e_{−1} = e_0`, `e_{−2} = e_1`, `e_{−3} = e_2`, `e_{−4} = e_3`,
`e_{−5} = e_4`.

**Lemma C2.** Substituting `b = n − 3 − a − c` in the `g_j`, the four
differences are, with `u = a + c` and `v = ac`:

| Case | Identity |
| --- | --- |
| EL | `σ_E (d_m − d_{m−1}) = c_0 (v K_EL + R_EL)` |
| EU | `σ_E (d_m − d_{m+1}) = c_0 (v K_EU + R_EU)` |
| OL | `σ_O (d_m − d_{m−1}) = e_0 (v K_OL + R_OL)` |
| OU | `σ_O (d_m − d_{m+1}) = e_0 (v K_OU + R_OU)` |

where `c_0 = C(2m−6, m−3)`, `e_0 = C(2m−5, m−2)` and

- `K_EL = m(m+1) [6m² + 25m − 91 − 3(m−1)u]`,
  `R_EL = 24m⁴u + 96m⁴ − 12m³u² − 60m³u − 592m³ + 18m²u² − 24m²u + 1272m² + 30mu² + 60mu − 1100m + 300`;
- `K_EU = (m+1) [30m³ − 47m² − 109m + 120 − 3m(5m−11)u]`,
  `R_EU = 88m⁴u + 224m⁴ − 44m³u² − 316m³u − 976m³ + 114m²u² + 152m²u + 1144m² + 38mu² + 316mu − 236m − 120u² − 240u − 60`;
- `K_OL = 4(m+1)(m+2) [6m² + 17m − 36 − 3mu]`,
  `R_OL = 80m⁴u + 256m⁴ − 40m³u² + 80m³u − 384m³ − 60m²u² − 260m²u − 64m² + 100mu² − 140mu + 96m + 120u² + 120u`;
- `K_OU = 6(m+1)(m+2) [2m² − 4 − mu]`,
  `R_OU = 32m⁴u + 64m⁴ − 16m³u² + 32m³u + 128m³ − 24m²u² − 104m²u − 208m² + 40mu² − 56mu − 320m + 48u² + 48u + 192`.

Moreover, for `H = (u − 1) K + R` in each case, `H` is a polynomial of degree
at most 2 in `u` whose coefficient of `u²` and whose values at the two ends of
the range of `u` are:

| Case | coefficient of `u²` in `H` | `H` at `u = 2` | largest `u` | `H` at the largest `u` |
| --- | --- | --- | --- | --- |
| EL | `−3m(m+1)(5m−11)` | `15(m−1)(2m−5)(5m²−7m+4)` | `2m−4` | `5(2m−5)(23m³−52m²+9m−12)` |
| EU | `−(m+1)(59m²−191m+120)` | `(2m−5)(215m³−378m²−53m+180)` | `2m−4` | `(2m−5)(279m³−554m²−149m+324)` |
| OL | `−4(m+1)(m+2)(13m−15)` | `4(110m⁴−67m³−197m²−32m+108)` | `2m−3` | `8(78m⁴−58m³−243m²+67m+234)` |
| OU | `−2(m+1)(m+2)(11m−12)` | `4(m+2)(35m³−32m²−73m+54)` | `2m−3` | `4(m+2)(41m³−53m²−70m+84)` |

*Proof.* Insert the polynomials `σ c_i/c_0` (or `σ e_i/e_0`) and the `g_j` in
the sums of Step 2, substitute `b`, and collect. The `g_j` are symmetric in
`a, c` and of degree at most 1 in each, and `b` is replaced by an expression
that is symmetric in `a, c` and of degree 1. Each monomial of a `g_j` is one
of `abc, ab, bc, ac, a, b, c, 1`, so after the substitution each difference is
a combination, with coefficients in `ℤ[m]`, of `a²c + ac² = uv`,
`a² + c² = u² − 2v`, `ac = v`, `a + c = u` and `1`: a polynomial in `m, u, v`
of degree at most 1 in `v`. The
expansion and the stated values of `H` are polynomial identities, verified
symbolically (computer-assisted, `symbolic_differences`). ∎

## Step 3. Positivity

The range of `u = a + c`. Since `a, c ≥ 1` and `b ≥ 1`: `2 ≤ u ≤ n − 4`, that
is `2 ≤ u ≤ 2m − 4` for even order and `2 ≤ u ≤ 2m − 3` for odd order. Since
`(a − 1)(c − 1) ≥ 0`: `v ≥ u − 1`. Recall `m ≥ 3`.

**(i) `K > 0` in each case.** `K` decreases in `u`, so it suffices to bound it
at the largest `u`, and in fact at a larger value:

- EL: for `u ≤ 2m − 4`, `3(m−1)u ≤ 6m² − 18m + 12`, so the bracket is at least
  `43m − 103 > 0`.
- EU: `5m − 11 > 0`; for `u ≤ 2m − 4`, `3m(5m−11)u ≤ 30m³ − 126m² + 132m`, so
  the bracket is at least `79m² − 241m + 120 = m(79m − 241) + 120`, which is
  `108` at `m = 3` and positive for `m ≥ 4`.
- OL: for `u ≤ 2m − 3`, `3mu ≤ 6m² − 9m`, so the bracket is at least
  `26m − 36 > 0`.
- OU: for `u ≤ 2m − 3`, `mu ≤ 2m² − 3m`, so the bracket is at least
  `3m − 4 > 0`.

**(ii) Reduction to `v = u − 1`.** By (i) and `v ≥ u − 1`,
`vK + R ≥ (u − 1)K + R = H(m, u)`.

**(iii) `H` is concave in `u`.** Its coefficient of `u²` is negative in each
case: `5m − 11 > 0`, `13m − 15 > 0` and `11m − 12 > 0` for `m ≥ 3`, and
`59m² − 191m + 120 = m(59m − 191) + 120` equals `78` at `m = 3` and is positive
for `m ≥ 4`. A concave function on an interval is at least the smaller of its
values at the two ends, so for `2 ≤ u ≤ u_max`

`H(m, u) ≥ min( H(m, 2), H(m, u_max) )`.

**(iv) `H > 0` at both ends, for `m ≥ 3`.** Each factor is positive:

- `m − 1 > 0`, `2m − 5 > 0`, `m + 2 > 0`; `5m² − 7m + 4 > 0` (negative
  discriminant).
- `23m³ − 52m² + 9m − 12 = m²(23m − 52) + 9m − 12 ≥ 17m² + 9m − 12 > 0`.
- `215m³ − 378m² − 53m + 180 = m²(215m − 378) − 53m + 180 ≥ 267m² − 53m + 180 > 0`.
- `279m³ − 554m² − 149m + 324 = m²(279m − 554) − 149m + 324 ≥ 283m² − 149m + 324 > 0`.
- `110m⁴ − 67m³ − 197m² − 32m + 108`: `m³(110m − 67) ≥ 263m³`,
  `263m³ − 197m² = m²(263m − 197) ≥ 592m²`, and `592m² − 32m + 108 > 0`.
- `78m⁴ − 58m³ − 243m² + 67m + 234`: `m³(78m − 58) ≥ 176m³`,
  `176m³ − 243m² = m²(176m − 243) ≥ 285m² > 0`, and `67m + 234 > 0`.
- `35m³ − 32m² − 73m + 54 = m²(35m − 32) − 73m + 54 ≥ 73m² − 73m + 54 > 0`.
- `41m³ − 53m² − 70m + 84 = m²(41m − 53) − 70m + 84 ≥ 70m² − 70m + 84 > 0`.

(Each bound uses `m ≥ 3` in the linear factor: `23·3 − 52 = 17`,
`215·3 − 378 = 267`, `279·3 − 554 = 283`, `110·3 − 67 = 263`,
`263·3 − 197 = 592`, `78·3 − 58 = 176`, `176·3 − 243 = 285`,
`35·3 − 32 = 73`, `41·3 − 53 = 70`.)

**Conclusion.** In each of the four cases `vK + R ≥ H(m,u) > 0`. Since `σ_E`,
`σ_O`, `c_0`, `e_0` are positive, Lemma C2 gives `d_m − d_{m−1} > 0` and
`d_m − d_{m+1} > 0` for both parities. ∎ (parts 1 and 2)

When `m = 3` and `n = 6` the range of `u` is the single point `u = 2`
(`a = b = c = 1`); the two endpoint formulas of case EL then agree
(`840 = 840`), as they must.

## Step 4. The peak

The sequence `d_0, …, d_{n−2}` is positive (Fact 1.1 of the source) and
log-concave (Theorem 2.1 of the source). By the general form
of R1 with `j = m`, part 1 says that every maximizing index is `≥ m`. Apply
the general form of R1 to the reversed sequence `a_i = d_{n−2−i}` with
`j = n − 2 − m ≥ 1`: since `a_{j−1} = d_{m+1} < d_m = a_j`, every maximizing
index `i` of `a` is `≥ j`, that is, every maximizing index of `d` is `≤ m`. So
`m` is the only maximizing index. Finally `1/√5 < 1/2` gives
`⌊n/2⌋ ≤ n/2 < n − n/√5 ≤ ⌈n − n/√5⌉`. ∎

## Remarks

**Scope.** T2 covers the caterpillars of diameter 4 whose central vertex has a
pendant leaf. It does not cover `b = 0` (Lemma L3 is stated for `c_i ≥ 1`), nor
the trees of diameter 4 that are not caterpillars. The path `P_5` is the case
`a = c = 1`, `b = 0`.

**Structure, compared with T1.** For double stars the difference
`d_m − d_{m−1}` is affine in `t = ab` with positive coefficients and the
proof ends there. Here the differences are again affine in the product of the
two outer leaf numbers, `v = ac`, with a positive coefficient, but the
remainder depends on `u = a + c`; the proof uses the reduction to the boundary
`v = u − 1` (one of the outer spine vertices has a single leaf) and concavity
in `u`. The upper inequality is proved by the same reduction as the lower
one; a proof by signs alone, as in Step 3 of T1, was not attempted.

**Where the margin is smallest.** By (ii) and (iii), for fixed `n` the minimum
of `vK + R` over the family is attained at `a = 1` or `c = 1` with `u = 2` or
`u = u_max`, that is at `K(1, n−5, 1)` or at `K(1, 1, n−5)`. This is a
statement about the polynomial `vK + R`, hence about `d_m − d_{m−1}` and
`d_m − d_{m+1}`; the relative margin `1 − d_{m−1}/d_m` is a different quantity
and was not analysed.

## Checks

`experiments/CJ-0001-collins-shor-peak/spine3.py` (exact arithmetic), result
file `results/spine3.json`:

- the `g_j` agree with the symbolic expansion of the `6 × 6` determinant;
- the four polynomials `vK + R`, derived symbolically from the `g_j` and the
  recurrences of Step 2, agree with Lemma C2, including the coefficient of
  `u²` in `H` and both endpoint values;
- the sign conditions of Step 3 for `3 ≤ m ≤ 2000` (a finite check of what
  Step 3 proves for all `m ≥ 3`);
- for every `K(a,b,c)` with `a + b + c ≤ 300`: the four identities of Lemma C2
  between integers, and `d_{m−1} < d_m > d_{m+1}`;
- for `a + b + c ≤ 60`: positivity of the whole sequence, `m` as the only
  maximizing index, and proportionality of the whole sequence to the numeric
  quotient-matrix computation of `near_star_families.py` (this shares Lemma L3
  with the closed form and is not independent evidence for it);
- for `a + b + c ≤ 20` and six larger caterpillars: equality of the whole
  sequence with the direct `n × n` determinant, which does not use Lemma L3.

Tests: `test_spine3_closed_forms_and_peak` in `tests/test_cj0001_distpoly.py`.

A finite check is not a proof. The proof is Steps 1 to 4, of which Lemma C1
and Lemma C2 are computer-assisted polynomial identities.
