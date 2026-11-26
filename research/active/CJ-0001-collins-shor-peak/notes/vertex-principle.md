# CJ-0001 — a vertex principle for caterpillars (exploration)

Status of this file: an **exploration note**, written by an AI agent (Claude,
model `claude-fable-5-2`) on 2026-11-26, session 4. It contains one short
lemma with a proof (L4), one lemma with a proof sketch (L3′), one hypothesis
supported only by exact finite computation (V), and what would follow from it.
Nothing here has been reviewed, and nothing is a claim of novelty. The
hypothesis is registered as MD-0009 with the status it has: a conjecture.

Question of the session: do the polynomial identities and positivity arguments
found for spines of two and three vertices (T1, T2, T3) point to a mechanism
that does not depend on the spine length?

## Setting

A caterpillar with `s ≥ 2` spine vertices has a path `v_1 … v_s` and `c_i`
pendant leaves at `v_i`, with `c_1, c_s ≥ 1` and `c_i ≥ 0` for `1 < i < s`.
Its order is `n = s + Σ c_i` and its diameter is `s + 1`. Write
`c = (c_1, …, c_s)` and `m = ⌊n/2⌋`.

Let `Q(c)` be the `2s × 2s` matrix of Lemma L3 (`lemmas.md`), its entries read
as polynomials in `c`, and define `g_0(c), …, g_{2s}(c)` by

`−det(2xI − Q(c)) / 4^{s−1} = Σ_{j=0}^{2s} g_j(c) x^j`.

Each `c_i` occurs only in column `s + i` of `Q`, so every `g_j` is of degree at
most 1 in each `c_i` (*multi-affine*).

**Lemma L3′ (empty classes; proof sketch).** If `n ≥ 2s`, then for
`0 ≤ k ≤ n − 2`

`d_k = Σ_{j=0}^{2s} g_j(c) C(n − 2s, k − j)`,

also when some of the inner `c_i` are `0`.

*Sketch.* For `c_i ≥ 1` throughout this is Lemma L3. If `c_i = 0`, column
`s + i` of `2xI − Q` is `2x + 2` on the diagonal and `0` elsewhere, so the
determinant is `(2x + 2)` times the determinant for the partition without the
empty class; each empty class thus contributes a factor `x + 1` and one fewer
eigenvalue `−2`, which cancel in `ℓ_T(x) = (x+1)^{n−2s} Σ_j g_j x^j` as long as
the exponent `n − 2s` is non-negative. For `s = 3` and one empty class this is
written out as Lemma C1′ of `diameter4-caterpillars.md`. For general `s` it has
not been written out. *Check:* the formula equals the direct `n × n`
determinant on every caterpillar with `2 ≤ s ≤ 8` spine vertices and small
leaf numbers, zeros included (`mixed_partials.py`; the ranges are in the
result file).

## The difference as a multi-affine function

Fix `s` and an order `n ≥ 2s`. Put

`D_n(c) = Σ_j g_j(c) [C(n − 2s, m − j) − C(n − 2s, m − 1 − j)]`.

Here `n` (hence `m` and the binomials) is a parameter and `c` ranges over
`ℝ^s`: `D_n` is a multi-affine polynomial in `c`. On the *slice*
`Σ c_i = n − s` it equals `d_m − d_{m−1}` of the caterpillar `c` (Lemma L3′).
The lower half of the Collins–Shor conjecture for the caterpillar `c` is
`D_n(c) > 0` (R1).

## Lemma L4 (vertex principle)

**Lemma L4.** Let `f : ℝ^s → ℝ` be a polynomial of degree at most 1 in each
variable, let `λ ∈ ℤ^s` and let `S > Σ λ_i` be an integer. Suppose that for all
`i ≠ k` the mixed partial derivative `∂²f/∂x_i∂x_k` is non-negative at every
real point `x` with `x ≥ λ` coordinatewise. Then for every integer point `c`
with `c ≥ λ` and `Σ c_i = S`,

`f(c) ≥ min_{1 ≤ p ≤ s} f(λ + (S − Σ λ_i) e_p)`.

*Proof.* By induction on the number `r(c)` of indices with `c_i > λ_i`. Since
`Σ c_i = S > Σ λ_i`, `r(c) ≥ 1`, and if `r(c) = 1` then `c = λ + (S − Σλ_i) e_p`
for some `p`. Let `r(c) ≥ 2` and choose `i ≠ k` with `c_i > λ_i`, `c_k > λ_k`.
For real `t` put `φ(t) = f(c + t(e_i − e_k))`. Because `f` is of degree at most
1 in `x_i` and in `x_k`,

`φ(t) = f(c) + t (∂f/∂x_i − ∂f/∂x_k)(c) − t² (∂²f/∂x_i∂x_k)(c)`,

and `∂²f/∂x_i∂x_k` does not depend on `x_i, x_k`. Its value at `c` is
non-negative, so `φ` is concave. On the interval
`−(c_i − λ_i) ≤ t ≤ c_k − λ_k` a concave function is at least the smaller of
its values at the two ends. Both ends are integer points `c′ ≥ λ` with the same
coordinate sum `S`: at `t = −(c_i − λ_i)` the `i`-th coordinate equals `λ_i`,
at `t = c_k − λ_k` the `k`-th equals `λ_k`, and no other coordinate changes
except the other one of the pair. So `r(c′) = r(c) − 1` in both cases, and
`f(c) ≥ min(f(c′), f(c″)) ≥ min_p f(λ + (S − Σλ_i) e_p)` by induction. ∎

## Hypothesis V

**Hypothesis V(s).** For every order `n ≥ 2s` and all `1 ≤ i < k ≤ s`,

`∂²D_n/∂c_i∂c_k ≥ 0` at every real `c` with `c_1, c_s ≥ 1` and `c_j ≥ 0` for `1 < j < s`.

**Evidence** (exact computation, `mixed_partials.py`, result file
`results/mixed-partials.json`; the ranges of `s` and `n` are those of the
file). For each `s`, `n` and pair `i < k` the mixed partial was written as a
polynomial in `y = c − λ`, `λ = (1, 0, …, 0, 1)`, in the remaining `s − 2`
variables, and every coefficient was found to be non-negative. This is a
*certificate*: it implies non-negativity for all `y ≥ 0`. The same holds with
`λ = (1, …, 1)`. No failure was found in the range computed. A finite range of
orders proves nothing about all `n`.

**Known cases.** `V(2)` holds for every `n ≥ 4`: in Lemma D1 of
`double-stars.md` the product `ab` occurs only in `g_1` and `g_2`, and Step 2
there shows that its coefficient in `d_m − d_{m−1}` is `3c_0/(m−1)` for even
order and `10e_0/m` for odd order, both positive (candidate proof T1).

**`V(3)` for every order (computer-assisted, not reviewed).** Write the leaf
numbers as `(a, b, c)` and let `σ_E, c_0, σ_O, e_0` be the positive quantities
of Lemma C2 of `spine3.md`. For every `n ≥ 6`, as polynomials in `m, a, b, c`:

| | even order, times `σ_E/c_0` | odd order, times `σ_O/e_0` |
| --- | --- | --- |
| `∂²D_n/∂a∂c` | `20m(m+1)(2m−5) + 3m(m−1)(m+1)·b` | `4(m+1)(m+2)(23m−36) + 12m(m+1)(m+2)·b` |
| `∂²D_n/∂a∂b` | `3m(m+1)(5m−11) + 3m(m−1)(m+1)·(c−1)` | `4(m+1)(m+2)(13m−15) + 12m(m+1)(m+2)·(c−1)` |
| `∂²D_n/∂b∂c` | `3m(m+1)(5m−11) + 3m(m−1)(m+1)·(a−1)` | `4(m+1)(m+2)(13m−15) + 12m(m+1)(m+2)·(a−1)` |

All six are positive for `m ≥ 3`, `a, c ≥ 1`, `b ≥ 0`. The identities were
obtained symbolically from the `g_j` of Lemma C1 of `spine3.md` and the
binomial recurrences, and are checked by `mixed_partials_s3.py`; they have not
been derived by hand. The values of `D_n` at the vertices of the slice are, up
to the same factors, the polynomial `H*` of `diameter4-caterpillars.md` at
`(n−4, 0, 1)` and `(1, 0, n−4)`, and `H(m, 2)` of `spine3.md` at `(1, n−5, 1)`;
all are positive for `m ≥ 3`. With Lemma L4 this is a second derivation of
part 1 of T2 and of T3 (the lower inequality for every `K(a,b,c)` with
`a, c ≥ 1`, `b ≥ 0`, `n ≥ 6`), in which the reduction in the variables
`u = a + c`, `v = ac` used there is replaced by the vertex principle. It is
recorded here as a consistency check of the method; T2 and T3 remain the
statements that were written out and reviewed.

**The top coefficient, uniformly in `s` (observation).** For every
`2 ≤ s ≤ 8` the product `c_1 c_2 ⋯ c_s` occurs in exactly two of the `g_j`:
in `g_{s−1}` with coefficient `s` and in `g_s` with coefficient `s + 3`
(exact, from the interpolated polynomials of `mixed_partials.py`; for `s = 2`
and `s = 3` this can be read off Lemma D1 and Lemma C1). If that holds for a
given `s`, the coefficient of `c_1 ⋯ c_s` in `D_n` — the mixed partial of
order `s` — follows by a two-line computation with `k = m − s`:

- even order (`n − 2s = 2k`): `s·[C(2k, k+1) − C(2k, k)] + (s+3)·[C(2k, k) − C(2k, k−1)] = 3·C(2k, k)/(k+1)`,
  three times a Catalan number, whatever `s` is;
- odd order (`n − 2s = 2k + 1`): the first bracket vanishes and the coefficient
  is `(s+3)·[C(2k+1, k) − C(2k+1, k−1)] = (2s + 6)·C(2k+1, k+1)/(k+2)`.

Both are positive. The values `3c_0/(m−1)` and `10e_0/m` of T1 and the
coefficients of `b`, `c − 1`, `a − 1` in the table above are the cases
`s = 2` and `s = 3`. This is the first statement of the investigation that has
the same form for every spine length. It concerns only the highest mixed
partial; the mixed partials of order 2 in Hypothesis V involve all the lower
coefficients, for which no uniform description is known. Why the two
coefficients are `s` and `s + 3` has not been examined.

## What would follow

**Proposition (conditional on V(s) and on L3′).** Assume `V(s)`. Then for every
caterpillar `c` with `s` spine vertices and order `n ≥ 2s`,

`d_m − d_{m−1} ≥ min_{1 ≤ p ≤ s} D_n(λ + (n − s − 2) e_p)`, `λ = (1, 0, …, 0, 1)`.

*Proof.* Lemma L4 with `f = D_n`, `λ` as stated and `S = n − s` (if
`n − s = 2` the caterpillar is `λ` itself). ∎

The point `λ + (n − s − 2) e_p` is the tree obtained from the path `P_{s+2}` by
attaching `n − s − 2` pendant leaves to its `(p+1)`-th vertex. So, under
`V(s)`, the lower half of the conjecture for all caterpillars of diameter
`s + 1` with at least `s` leaves reduces to `⌈s/2⌉` one-parameter families
(by the symmetry `p ↔ s + 1 − p`), each of which is, for fixed `s`, a question
about one polynomial in `m` per parity. In the range computed the minimum is
attained at the middle position `p = ⌈s/2⌉`, and all vertex values are
positive.

**What this does not give.** (1) `V(s)` is not proved for any `s ≥ 4`; for
`s = 3` it is a computer-assisted identity that no one has reviewed. The
vertex families are not proved positive for any `s ≥ 4`. (2) Nothing here is
uniform in `s`: for each `s` there is a finite list of polynomials in `m`, but
their number and degree grow with `s`. (3) Caterpillars with fewer leaves than
spine vertices (`n < 2s`) are outside the binomial formula. (4) Trees that are
not caterpillars are not touched. (5) The upper inequality `d_{m+1} < d_m`
does not behave this way: the same certificate fails for the upper difference
from `s = 4` on, and for `s = 6` some vertex trees have `d_{m+1} ≥ d_m` — as
expected, since for long spines the peak moves above `⌊n/2⌋`, towards that of
the path.

## Why this is the natural generalization of T1 to T3

In T1 the difference is affine in `ab` with a positive coefficient: that is
`V(2)`, and the minimizing tree has `a = 1`. In T2 and T3 the difference is
`vK + R` with `K > 0` (`v = ac`), the minimum is on the boundary `v = u − 1`,
and concavity in `u` moves it to an endpoint: these are the two moves of
Lemma L4, made by hand in particular coordinates. The principle isolates what
was used: multi-affinity (from the quotient determinant) and the sign of the
mixed partials.

## Next

1. Have the `s = 3` case above reviewed, or derive its six polynomials by
   hand.
2. `s = 4`: write the six mixed partials and the two vertex families as
   polynomials in `m`; this would give the lower half for all caterpillars of
   diameter 5 with at least four leaves.
3. Look for a reason for `V(s)` that does not go through explicit polynomials —
   for instance an interpretation of `∂²D_n/∂c_i∂c_k` through the Laplacian
   formula L1, in which adding leaves at `v_i` and `v_k` has a combinatorial
   meaning.
4. Formalize Lemma L4 in Lean: it is elementary, independent of the tree, and
   every later use of the principle rests on it.
