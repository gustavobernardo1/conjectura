# CJ-0001 — double stars: the peak is at ⌊n/2⌋

Status of this file: written by an AI agent (Claude, model `claude-fable-5-2`)
on 2026-11-26, session 2. Review status and novelty are recorded in
`research/discoveries.json` (record MD-0006) and in `../STATE.md`, not here.
Nothing in this file is a claim of novelty.

Notation is that of [`lemmas.md`](lemmas.md). `T` is a tree of order `n ≥ 3`,
`D` its distance matrix, `δ_k` the coefficient of `x^k` in `det(D − xI)`,
`d_k = 2^{k−(n−2)} |δ_k|` for `0 ≤ k ≤ n−2`, and
`ℓ_T(x) = −2^{−(n−2)} det(2xI − D)`, whose coefficient of `x^k` is `d_k` for
`0 ≤ k ≤ n−2` (Observation 3.1 of arXiv:1507.02341). `C(N, i)` is the binomial
coefficient, equal to `0` when `i < 0` or `i > N`.

The double star `S(a,b)`, `a, b ≥ 1`, has two adjacent vertices (the centres)
carrying `a` and `b` pendant leaves; its order is `n = a + b + 2 ≥ 4`.
Throughout, `s = a + b = n − 2`, `t = ab ≥ 1`, `N = n − 4 = s − 2 ≥ 0` and
`m = ⌊n/2⌋`.

## T1. Statement

**Theorem T1.** Let `a, b ≥ 1`, `T = S(a,b)`, `n = a + b + 2`, `m = ⌊n/2⌋`. Then

1. `d_{m−1}(T) < d_m(T)`;
2. if `m + 1 ≤ n − 2`, then `d_{m+1}(T) < d_m(T)`.

Consequently `m = ⌊n/2⌋` is the only index at which `d_0(T), …, d_{n−2}(T)`
attains its maximum, and since `⌊n/2⌋ ≤ ⌈n − n/√5⌉` the Collins–Shor conjecture
(Conjecture 1.2 of arXiv:1507.02341, in the strong reading of ties) holds for
every double star.

The proof uses: Lemma L3 of `lemmas.md` with spine length 2; Theorem 2.1 of
arXiv:1507.02341 (the sequence `d_0, …, d_{n−2}` is positive and log-concave),
only in Step 4; and the general form of R1 in `lemmas.md`, only in Step 4.

## Step 1. The coefficients of a double star

**Lemma D1.** For `0 ≤ k ≤ n − 2`,

`d_k(S(a,b)) = Σ_{j=0}^{4} g_j C(N, k − j)`,

with

`g_0 = s + 1`, `g_1 = 2t + 6s + 2`, `g_2 = 5t + 9s − 3`, `g_3 = 4s − 8`, `g_4 = −4`.

*Proof.* `S(a,b)` is the caterpillar with spine length 2 and `c_1 = a`,
`c_2 = b`. Lemma L3 gives `ℓ_T(x) = −2^{−2} (x+1)^{n−4} det(2xI − Q)` with, in
the order (centre 1, centre 2, leaves of centre 1, leaves of centre 2),

```
      | 0   1   a        2b      |
Q  =  | 1   0   2a       b       |
      | 1   2   2(a−1)   3b      |
      | 2   1   3a       2(b−1)  |
```

Expanding the determinant,

`det(2xI − Q) = 16x⁴ − (16s − 32)x³ − (20t + 36s − 12)x² − (8t + 24s + 8)x − (4s + 4)`,

so `−det(2xI − Q)/4 = g_0 + g_1 x + g_2 x² + g_3 x³ + g_4 x⁴`, and the
coefficient of `x^k` in `(x+1)^N (g_0 + … + g_4 x⁴)` is `Σ_j g_j C(N, k−j)`. ∎

The determinant is affine in `a` (which occurs only in the third column) and
in `b` (only in the fourth), which is why it depends on `a, b` only through
`s`, `t` and is affine in `t`. The expansion was obtained symbolically
(`double_stars.py`, function `symbolic_4g`) and can be confirmed by hand by
evaluating both sides at `(a,b) ∈ {(0,0), (1,0), (0,1), (1,1)}`.

*Checks.* `d_0 = g_0 = n − 1` (Graham–Pollak).
`d_1 = g_0 N + g_1 = s² + 5s + 2t`, which equals `2n² − 6 − Σ deg(v)²` (L2).
The coefficient of `x^{n−1}` in `ℓ_T` is `g_3 + g_4 N = 0` and that of `x^n` is
`g_4 = −4`, as in Observation 3.1 of arXiv:1507.02341.

## Step 2. `d_{m−1} < d_m`

The identity `(k+1) C(N, k+1) = (N − k) C(N, k)` holds for every integer
`k ≥ 0` (both sides vanish when `k ≥ N`), and `C(N, k) = C(N, N − k)`.

### Even order, `n = 2m`, `m ≥ 2`

Here `N = 2m − 4` and `s = 2m − 2`. Put `c_i = C(N, m − 2 + i)` for every
integer `i`; then `c_{−i} = c_i`, `c_0 > 0`, and by the identity above

`(m−1) c_1 = (m−2) c_0`, `m c_2 = (m−3) c_1`, `(m+1) c_3 = (m−4) c_2`.

Hence

- `c_0 − c_1 = c_0/(m−1)`,
- `c_1 − c_2 = 3c_1/m = 3(m−2) c_0 / ((m−1)m)`,
- `c_2 − c_3 = 5c_2/(m+1) = 5(m−2)(m−3) c_0 / ((m−1)m(m+1))`.

By Lemma D1, `C(N, m − j) = c_{2−j}` and `C(N, m − 1 − j) = c_{1−j}`, so

`d_m − d_{m−1} = Σ_j g_j (c_{2−j} − c_{1−j})`
`= g_0(c_2 − c_1) + g_1(c_1 − c_0) + g_2(c_0 − c_1) + g_3(c_1 − c_2) + g_4(c_2 − c_3)`
`= (g_2 − g_1)(c_0 − c_1) + (g_3 − g_0)(c_1 − c_2) + g_4 (c_2 − c_3)`,

where the symmetry `c_{−1} = c_1`, `c_{−2} = c_2`, `c_{−3} = c_3` was used.
With `g_2 − g_1 = 3t + 3s − 5 = 3t + 6m − 11`, `g_3 − g_0 = 3s − 9 = 6m − 15`
and `g_4 = −4`:

`(m−1) m (m+1) (d_m − d_{m−1}) = c_0 [ (3t + 6m − 11) m(m+1) + 3(6m − 15)(m−2)(m+1) − 20(m−2)(m−3) ]`
`= c_0 [ 3t m(m+1) + 24m³ − 88m² + 98m − 30 ]`
`= c_0 [ 3t m(m+1) + 2(2m−1)(2m−3)(3m−5) ]`.

For `m ≥ 2` each of `2m−1`, `2m−3`, `3m−5` is positive, `t > 0` and `c_0 > 0`.
Therefore `d_m − d_{m−1} > 0`.

### Odd order, `n = 2m + 1`, `m ≥ 2`

Here `N = 2m − 3` and `s = 2m − 1`. Put `e_i = C(N, m − 1 + i)` for every
integer `i`; then `e_{−1−i} = e_i` (in particular `e_{−1} = e_0`), `e_0 > 0`, and

`m e_1 = (m−2) e_0`, `(m+1) e_2 = (m−3) e_1`, `(m+2) e_3 = (m−4) e_2`.

Hence

- `e_0 − e_1 = 2e_0/m`,
- `e_1 − e_2 = 4e_1/(m+1) = 4(m−2) e_0 / (m(m+1))`,
- `e_2 − e_3 = 6e_2/(m+2) = 6(m−2)(m−3) e_0 / (m(m+1)(m+2))`.

By Lemma D1, `C(N, m − j) = e_{1−j}` and `C(N, m − 1 − j) = e_{−j}`, so

`d_m − d_{m−1} = Σ_j g_j (e_{1−j} − e_{−j})`
`= g_0(e_1 − e_0) + g_1(e_0 − e_{−1}) + g_2(e_{−1} − e_{−2}) + g_3(e_{−2} − e_{−3}) + g_4(e_{−3} − e_{−4})`
`= g_0(e_1 − e_0) + 0 + g_2(e_0 − e_1) + g_3(e_1 − e_2) + g_4(e_2 − e_3)`
`= (g_2 − g_0)(e_0 − e_1) + g_3 (e_1 − e_2) + g_4 (e_2 − e_3)`.

With `g_2 − g_0 = 5t + 8s − 4 = 5t + 16m − 12`, `g_3 = 4s − 8 = 8m − 12` and
`g_4 = −4`:

`m (m+1) (m+2) (d_m − d_{m−1}) = e_0 [ 2(5t + 16m − 12)(m+1)(m+2) + 4(8m − 12)(m−2)(m+2) − 24(m−2)(m−3) ]`
`= e_0 [ 10t (m+1)(m+2) + 16m(2m−1)(2m+1) ]`,

which is positive. Therefore `d_m − d_{m−1} > 0`. ∎ (part 1)

Every double star has `n ≥ 4`, so `m ≥ 2` in both cases and nothing is left out.

## Step 3. `d_{m+1} < d_m`

No computation is needed here beyond signs. Note `g_0 > 0`, `g_1 > 0`,
`g_2 − g_3 = 5t + 5s + 5 > 0`, `g_1 − g_3 = 2t + 2s + 10 > 0` and `g_4 = −4`.

### Even order, `n = 2m`, `m ≥ 3`

(The index `m + 1` exists exactly when `m + 1 ≤ 2m − 2`, that is `m ≥ 3`.) With
the `c_i` of Step 2, `C(N, m + 1 − j) = c_{3−j}` and `C(N, m − j) = c_{2−j}`, so

`d_{m+1} − d_m = g_0(c_3 − c_2) + g_1(c_2 − c_1) + g_2(c_1 − c_0) + g_3(c_0 − c_{−1}) + g_4(c_{−1} − c_{−2})`
`= −g_0 (c_2 − c_3) − (g_1 + 4)(c_1 − c_2) − (g_2 − g_3)(c_0 − c_1)`.

By the formulas of Step 2, `c_2 − c_3 ≥ 0`, `c_1 − c_2 ≥ 0` and
`c_0 − c_1 = c_0/(m−1) > 0`. All three terms are non-positive and the last is
negative. Therefore `d_{m+1} − d_m < 0`.

### Odd order, `n = 2m + 1`, `m ≥ 2`

(The index `m + 1` exists exactly when `m + 1 ≤ 2m − 1`, that is `m ≥ 2`.) With
the `e_i` of Step 2, `C(N, m + 1 − j) = e_{2−j}` and `C(N, m − j) = e_{1−j}`, so

`d_{m+1} − d_m = g_0(e_2 − e_1) + g_1(e_1 − e_0) + g_2(e_0 − e_{−1}) + g_3(e_{−1} − e_{−2}) + g_4(e_{−2} − e_{−3})`
`= g_0(e_2 − e_1) + g_1(e_1 − e_0) + 0 + g_3(e_0 − e_1) + g_4(e_1 − e_2)`
`= −(g_0 + 4)(e_1 − e_2) − (g_1 − g_3)(e_0 − e_1)`.

Here `e_1 − e_2 ≥ 0` and `e_0 − e_1 = 2e_0/m > 0`. Therefore
`d_{m+1} − d_m < 0`. ∎ (part 2)

## Step 4. The peak

The sequence `d_0, …, d_{n−2}` is positive and log-concave (Theorem 2.1 of
arXiv:1507.02341). By the general form of R1 with `j = m`, part 1 says that
every maximizing index is `≥ m`. If `m = n − 2` (this happens only for
`n = 4`) there is no larger index. Otherwise apply the general form of R1 to
the reversed sequence `a_i = d_{n−2−i}` with `j = n − 2 − m ≥ 1`: since
`a_{j−1} = d_{m+1} < d_m = a_j`, every maximizing index `i` of `a` is `≥ j`,
that is, every maximizing index of `d` is `≤ m`. So `m` is the only maximizing
index.

Finally `1/√5 < 1/2` gives `n − n/√5 > n/2 ≥ ⌊n/2⌋`, so
`⌊n/2⌋ ≤ ⌈n − n/√5⌉` and the maximizing index lies in the conjectured
interval. ∎

## Remarks

**Stars (known).** The same method with spine length 1 gives, for the star
`S_n`, `ℓ(x) = (x+1)^{n−2} ((n−1) + 4(n−2)x − 4x²)`, hence
`d_k = (n−1) C(n−2, k) + 4(n−2) C(n−2, k−1) − 4 C(n−2, k−2)`, and

- `n = 2m`: `m (m+1) (d_m − d_{m−1}) = C(2m−2, m−1) (2m−1)(3m−5)`,
- `n = 2m+1`: `(m+1)(m+2) (d_m − d_{m−1}) = C(2m−1, m) · 8m(2m+1)`,

both positive for `n ≥ 3`. That the peak of a star is `⌊n/2⌋` is a theorem of
Collins (1989, Theorem 1, as reported in arXiv:1507.02341; the paper has not
been read by the project). It is recorded here as a consistency check, not as
a result: putting `t = 0` in the even formula of Step 2 gives exactly the star
formula, because `C(2m−2, m−1) (m−1) = 2(2m−3) C(2m−4, m−2)`.

**Trees of diameter at most 3.** A tree of order `n ≥ 3` has diameter 2 (a
star) or, if its diameter is 3, is a double star. With Collins's theorem for
stars, T1 gives the Collins–Shor conjecture for all trees of diameter at most 3.

**What T1 does not say.** Nothing about trees of diameter 4 or more. The
relative margin `1 − d_{m−1}/d_m` of a double star tends to `0` as `n → ∞`
(it is of order `1/n`), so T1 is an exact statement, not a consequence of a
crude bound.

## Checks

`experiments/CJ-0001-collins-shor-peak/double_stars.py` (exact arithmetic):

- the polynomials `g_0, …, g_4` agree with the symbolic expansion of the
  `4 × 4` determinant;
- for all 10,000 double stars with `a + b ≤ 200`: the two closed forms of
  Step 2, both inequalities, uniqueness of the peak, and agreement of the whole
  sequence `d_0, …, d_{n−2}` with the numeric quotient-matrix computation of
  `near_star_families.py`;
- for all 400 double stars with `a + b ≤ 40` and four larger ones: agreement of
  the whole sequence with the direct `n × n` determinant;
- the star formulas for orders 3 to 202 (direct determinant up to order 42).

Result file: `results/double-stars.json`. Tests:
`test_double_star_closed_forms_and_peak` in `tests/test_cj0001_distpoly.py`,
which also compares with the independent Laplacian method.

A finite check is not a proof. The proof is Steps 1 to 4.
