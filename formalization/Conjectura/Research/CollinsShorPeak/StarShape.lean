/-
RESEARCH — problem CJ-0001 (Collins–Shor peak conjecture), supporting lemma.

Source statement: Lemma 7.5 ("the star", label `lem:starshape`) of
`manuscripts/CJ-0001-collins-shor/main.tex` at revision 87c3c8c, read as a
statement about binomial coefficients:

  Let `n ≥ 3`, `N = n − 2`, `m = ⌊n/2⌋` and, for every integer `k`,
  `c(k) = (n−1)·C(N,k) + 4(n−2)·C(N,k−1) − 4·C(N,k−2)`, with `C(N,j) = 0` for
  `j < 0` or `j > N`. Then
  (a) `c(k−1) < c(k)` for every `1 ≤ k ≤ m`, and
  (b) `c(k) < c(k−1)` for every `m+1 ≤ k ≤ n−2`.

In the manuscript `c(k) = [x^k] ℓ_{S_n}` (Corollary `cor:leaf`(d), as used in
the proof of Lemma `lem:starvalue`), and `[x^k] ℓ_T = d_k(T)` for
`0 ≤ k ≤ n − 2` (Lemma `lem:ident`); the lemma is stated there for the `d_k`
of the star. That connection is NOT formalized: nothing about trees, distance
matrices or the polynomial `ℓ_{S_n}` appears here. Only the binomial statement
is formalized. The conclusion "so `⌊n/2⌋` is the unique maximizing index of the
star" is not formalized either, and the closed form of Lemma `lem:starvalue`
for `k = m` is not used.

Encoding:

* `n : ℕ` with `3 ≤ n`; `N = n − 2` is the natural-number subtraction `n - 2`,
  which is the true difference because `3 ≤ n`;
* `starBinom N j` is `C(N,j)` for an integer `j`: `Nat.choose N j` for `j ≥ 0`
  (which is `0` for `j > N`), and `0` for `j < 0`
  (`starBinom_natCast`, `starBinom_of_neg`, `starBinom_of_lt`);
* `starCoeff n k` is `c(k)` for an integer `k`, computed in `ℤ`, with
  `(n : ℤ) - 1` and `(n : ℤ) - 2` (integer subtraction);
* `m = ⌊n/2⌋` is the natural-number division `n / 2`, cast to `ℤ`;
* `n − 2` in the range of (b) is the integer `(n : ℤ) - 2`.

Proof (not the manuscript's route through `F(j) = C(N,j) − C(N,j−1)` and ratio
bounds, but a cross-multiplied polynomial identity): for `k = j + 3` with
`j : ℕ`, the three relations `C(N,i+1)(i+1) = C(N,i)(N−i)` give
`(j+1)(j+2)(j+3)·(c(j+3) − c(j+2)) = C(N,j) · P(N,j)` for an explicit integer
polynomial `P` (`starCoeff_diff_identity`). Substituting `N = 2j + 4 + s`
(the range of (a)) turns `P` into a polynomial in `j, s` with positive
coefficients, and substituting `N = j + 3 + u`, `j = u + v` (the range of (b))
turns `−P` into one. The cases `k = 1` and `k = 2` of (a) are computed
directly.
-/
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace Conjectura.Research.CollinsShorPeak

/-- The binomial coefficient `C(N,j)` for an integer lower index `j`: zero for
`j < 0`, and `Nat.choose N j` (zero for `j > N`) otherwise. -/
def starBinom (N : ℕ) (j : ℤ) : ℤ :=
  if 0 ≤ j then ((N.choose j.toNat : ℕ) : ℤ) else 0

theorem starBinom_natCast (N j : ℕ) : starBinom N (j : ℤ) = (N.choose j : ℤ) := by
  simp [starBinom]

theorem starBinom_of_neg (N : ℕ) (j : ℤ) (hj : j < 0) : starBinom N j = 0 := by
  simp [starBinom, not_le.mpr hj]

theorem starBinom_of_lt (N : ℕ) (j : ℤ) (hj : (N : ℤ) < j) : starBinom N j = 0 := by
  obtain ⟨i, rfl⟩ : ∃ i : ℕ, j = (i : ℤ) := ⟨j.toNat, by omega⟩
  rw [starBinom_natCast, Nat.choose_eq_zero_of_lt (by omega)]
  simp

/-- `c(k) = (n−1)·C(n−2,k) + 4(n−2)·C(n−2,k−1) − 4·C(n−2,k−2)`, the coefficient
of Lemma 7.5 of the manuscript (in ℤ). -/
def starCoeff (n : ℕ) (k : ℤ) : ℤ :=
  ((n : ℤ) - 1) * starBinom (n - 2) k + 4 * ((n : ℤ) - 2) * starBinom (n - 2) (k - 1)
    - 4 * starBinom (n - 2) (k - 2)

/-- Agreement with the textbook definition on examples. For `n = 3`,
`(1+x)(2+4x−4x²) = 2 + 6x + 0x² − 4x³`; for `n = 4`,
`(1+x)²(3+8x−4x²) = 3 + 14x + 15x² + 0x³ − 4x⁴`; the coefficients vanish
outside `0 ≤ k ≤ n`. -/
theorem starCoeff_examples :
    (starCoeff 3 (-1) = 0 ∧ starCoeff 3 0 = 2 ∧ starCoeff 3 1 = 6 ∧ starCoeff 3 2 = 0 ∧
      starCoeff 3 3 = -4 ∧ starCoeff 3 4 = 0) ∧
    (starCoeff 4 0 = 3 ∧ starCoeff 4 1 = 14 ∧ starCoeff 4 2 = 15 ∧ starCoeff 4 3 = 0 ∧
      starCoeff 4 4 = -4 ∧ starCoeff 4 5 = 0) := by
  decide

/-- `C(N,j+1)(j+1) = C(N,j)(N−j)` in `ℤ`, for every `j` (both sides vanish for
`j > N`). -/
theorem choose_succ_mul_int (N j : ℕ) :
    ((N.choose (j + 1) : ℕ) : ℤ) * ((j : ℤ) + 1) = (N.choose j : ℤ) * ((N : ℤ) - j) := by
  rcases le_or_gt j N with hj | hj
  · have h := Nat.choose_succ_right_eq N j
    have h' : ((N.choose (j + 1) * (j + 1) : ℕ) : ℤ) = ((N.choose j * (N - j) : ℕ) : ℤ) := by
      rw [h]
    push_cast [Nat.cast_sub hj] at h'
    linear_combination h'
  · rw [Nat.choose_eq_zero_of_lt hj, Nat.choose_eq_zero_of_lt (by omega : N < j + 1)]
    simp

/-- The polynomial `P(N,j)` with
`(j+1)(j+2)(j+3)·(c(j+3) − c(j+2)) = C(N,j)·P(N,j)` for `n = N + 2`. -/
def starDiffPoly (N j : ℤ) : ℤ :=
  (((N + 1) * (N - j - 2) + (j + 3) * (3 * N - 1)) * (N - j - 1)
      - 4 * (j + 2) * (j + 3) * (N + 1)) * (N - j)
    + 4 * (j + 1) * (j + 2) * (j + 3)

theorem starCoeff_diff_identity (N j : ℕ) :
    ((j : ℤ) + 1) * ((j : ℤ) + 2) * ((j : ℤ) + 3) *
        (starCoeff (N + 2) ((j : ℤ) + 3) - starCoeff (N + 2) ((j : ℤ) + 2)) =
      (N.choose j : ℤ) * starDiffPoly N j := by
  have r1 := choose_succ_mul_int N j
  have r2 := choose_succ_mul_int N (j + 1)
  have r3 := choose_succ_mul_int N (j + 2)
  have e1 : (j : ℤ) + 3 = ((j + 3 : ℕ) : ℤ) := by push_cast; ring
  have e2 : (j : ℤ) + 3 - 1 = ((j + 2 : ℕ) : ℤ) := by push_cast; ring
  have e3 : (j : ℤ) + 3 - 2 = ((j + 1 : ℕ) : ℤ) := by push_cast; ring
  have e4 : (j : ℤ) + 2 = ((j + 2 : ℕ) : ℤ) := by push_cast; ring
  have e5 : (j : ℤ) + 2 - 1 = ((j + 1 : ℕ) : ℤ) := by push_cast; ring
  have e6 : (j : ℤ) + 2 - 2 = (j : ℤ) := by ring
  have hN : N + 2 - 2 = N := by omega
  simp only [starCoeff, hN, e2, e3, e5, e6]
  rw [e1, e4]
  simp only [starBinom_natCast]
  rw [show j + 1 + 1 = j + 2 from rfl] at r2
  rw [show j + 2 + 1 = j + 3 from rfl] at r3
  push_cast at r1 r2 r3 ⊢
  unfold starDiffPoly
  linear_combination
    ((j : ℤ) + 1) * ((j : ℤ) + 2) * ((N : ℤ) + 1) * r3
    + ((j : ℤ) + 1) * (((N : ℤ) + 1) * ((N : ℤ) - j - 2) + ((j : ℤ) + 3) * (3 * (N : ℤ) - 1)) * r2
    + ((((N : ℤ) + 1) * ((N : ℤ) - j - 2) + ((j : ℤ) + 3) * (3 * (N : ℤ) - 1)) *
        ((N : ℤ) - j - 1) - 4 * ((j : ℤ) + 2) * ((j : ℤ) + 3) * ((N : ℤ) + 1)) * r1

/-- In the range of (a), `k = j + 3 ≤ ⌊n/2⌋`, i.e. `2j + 4 ≤ N`: `P(N,j) > 0`. -/
theorem starDiffPoly_pos (N j : ℕ) (h : 2 * j + 4 ≤ N) : 0 < starDiffPoly N j := by
  obtain ⟨s, rfl⟩ : ∃ s, N = 2 * j + 4 + s := ⟨N - (2 * j + 4), by omega⟩
  have e : starDiffPoly ((2 * j + 4 + s : ℕ) : ℤ) (j : ℤ) =
      10 * (j : ℤ) ^ 3 * s + 6 * (j : ℤ) ^ 3 + 17 * (j : ℤ) ^ 2 * (s : ℤ) ^ 2
        + 94 * (j : ℤ) ^ 2 * s + 41 * (j : ℤ) ^ 2 + 8 * (j : ℤ) * (s : ℤ) ^ 3
        + 99 * (j : ℤ) * (s : ℤ) ^ 2 + 284 * (j : ℤ) * s + 89 * (j : ℤ) + (s : ℤ) ^ 4
        + 23 * (s : ℤ) ^ 3 + 143 * (s : ℤ) ^ 2 + 277 * (s : ℤ) + 60 := by
    unfold starDiffPoly
    push_cast
    ring
  rw [e]
  positivity

/-- In the range of (b), `⌊n/2⌋ + 1 ≤ k = j + 3 ≤ n − 2`, i.e.
`j + 3 ≤ N ≤ 2j + 3`: `P(N,j) < 0`. -/
theorem starDiffPoly_neg (N j : ℕ) (h1 : j + 3 ≤ N) (h2 : N ≤ 2 * j + 3) :
    starDiffPoly N j < 0 := by
  obtain ⟨u, rfl⟩ : ∃ u, N = j + 3 + u := ⟨N - (j + 3), by omega⟩
  obtain ⟨v, rfl⟩ : ∃ v, j = u + v := ⟨j - u, by omega⟩
  have e : -starDiffPoly ((u + v + 3 + u : ℕ) : ℤ) ((u + v : ℕ) : ℤ) =
      10 * (u : ℤ) ^ 3 * v + 4 * (u : ℤ) ^ 3 + 13 * (u : ℤ) ^ 2 * (v : ℤ) ^ 2
        + 72 * (u : ℤ) ^ 2 * v + 36 * (u : ℤ) ^ 2 + 4 * (u : ℤ) * (v : ℤ) ^ 3
        + 57 * (u : ℤ) * (v : ℤ) ^ 2 + 182 * (u : ℤ) * v + 104 * (u : ℤ)
        + 8 * (v : ℤ) ^ 3 + 66 * (v : ℤ) ^ 2 + 160 * (v : ℤ) + 96 := by
    unfold starDiffPoly
    push_cast
    ring
  have : 0 < -starDiffPoly ((u + v + 3 + u : ℕ) : ℤ) ((u + v : ℕ) : ℤ) := by
    rw [e]
    positivity
  linarith

/-- Lemma 7.5(a) of the manuscript: for `n ≥ 3` and every integer `k` with
`1 ≤ k ≤ ⌊n/2⌋`, `c(k−1) < c(k)`. -/
theorem starCoeff_lt_of_le_half (n : ℕ) (hn : 3 ≤ n) (k : ℤ) (hk1 : 1 ≤ k)
    (hkm : k ≤ ((n / 2 : ℕ) : ℤ)) : starCoeff n (k - 1) < starCoeff n k := by
  obtain ⟨N, rfl⟩ : ∃ N, n = N + 2 := ⟨n - 2, by omega⟩
  obtain ⟨k', rfl⟩ : ∃ k' : ℕ, k = (k' : ℤ) := ⟨k.toNat, by omega⟩
  have hN : N + 2 - 2 = N := by omega
  rcases (by omega : k' = 1 ∨ k' = 2 ∨ 3 ≤ k') with h | h | h
  · subst h
    have hN1 : 1 ≤ N := by omega
    have hc1 : N.choose 1 = N := Nat.choose_one_right N
    simp only [starCoeff, hN]
    norm_num [starBinom, hc1]
    nlinarith
  · subst h
    have hN2 : 2 ≤ N := by omega
    have r := choose_succ_mul_int N 1
    have hc1 : N.choose 1 = N := Nat.choose_one_right N
    rw [hc1] at r
    simp only [starCoeff, hN]
    norm_num [starBinom, hc1]
    obtain ⟨t, rfl⟩ : ∃ t, N = t + 2 := ⟨N - 2, by omega⟩
    push_cast at r ⊢
    nlinarith [sq_nonneg (t : ℤ), mul_nonneg (sq_nonneg (t : ℤ)) (Nat.cast_nonneg (α := ℤ) t)]
  · obtain ⟨j, rfl⟩ : ∃ j, k' = j + 3 := ⟨k' - 3, by omega⟩
    have hjN : 2 * j + 4 ≤ N := by omega
    have hid := starCoeff_diff_identity N j
    have hP := starDiffPoly_pos N j hjN
    have hC : 0 < (N.choose j : ℤ) := by exact_mod_cast Nat.choose_pos (by omega)
    have hprod : 0 < ((j : ℤ) + 1) * ((j : ℤ) + 2) * ((j : ℤ) + 3) := by positivity
    have ea : ((j + 3 : ℕ) : ℤ) - 1 = (j : ℤ) + 2 := by push_cast; ring
    have eb : ((j + 3 : ℕ) : ℤ) = (j : ℤ) + 3 := by push_cast; ring
    rw [ea, eb]
    have hpos : 0 < ((j : ℤ) + 1) * ((j : ℤ) + 2) * ((j : ℤ) + 3) *
        (starCoeff (N + 2) ((j : ℤ) + 3) - starCoeff (N + 2) ((j : ℤ) + 2)) := by
      rw [hid]
      exact mul_pos hC hP
    have := pos_of_mul_pos_right hpos hprod.le
    linarith

/-- Lemma 7.5(b) of the manuscript: for `n ≥ 3` and every integer `k` with
`⌊n/2⌋ + 1 ≤ k ≤ n − 2`, `c(k) < c(k−1)`. -/
theorem starCoeff_lt_of_half_lt (n : ℕ) (hn : 3 ≤ n) (k : ℤ)
    (hkm : ((n / 2 : ℕ) : ℤ) + 1 ≤ k) (hkn : k ≤ (n : ℤ) - 2) :
    starCoeff n k < starCoeff n (k - 1) := by
  obtain ⟨N, rfl⟩ : ∃ N, n = N + 2 := ⟨n - 2, by omega⟩
  obtain ⟨j, rfl⟩ : ∃ j : ℕ, k = (j : ℤ) + 3 := ⟨(k - 3).toNat, by omega⟩
  have h1 : j + 3 ≤ N := by omega
  have h2 : N ≤ 2 * j + 3 := by omega
  have hid := starCoeff_diff_identity N j
  have hP := starDiffPoly_neg N j h1 h2
  have hC : 0 < (N.choose j : ℤ) := by exact_mod_cast Nat.choose_pos (by omega)
  have hprod : 0 < ((j : ℤ) + 1) * ((j : ℤ) + 2) * ((j : ℤ) + 3) := by positivity
  have ea : (j : ℤ) + 3 - 1 = (j : ℤ) + 2 := by ring
  rw [ea]
  have hneg : ((j : ℤ) + 1) * ((j : ℤ) + 2) * ((j : ℤ) + 3) *
      (starCoeff (N + 2) ((j : ℤ) + 3) - starCoeff (N + 2) ((j : ℤ) + 2)) < 0 := by
    rw [hid]
    exact mul_neg_of_pos_of_neg hC hP
  have : starCoeff (N + 2) ((j : ℤ) + 3) - starCoeff (N + 2) ((j : ℤ) + 2) < 0 := by
    by_contra hc
    replace hc := not_lt.mp hc
    have := mul_nonneg hprod.le hc
    linarith
  linarith

/-- Non-vacuity of the hypotheses of `starCoeff_lt_of_le_half` (`n = 3`,
`k = 1`) and of `starCoeff_lt_of_half_lt` (`n = 5`, `k = 3`). -/
theorem starShape_hypotheses_nonvacuous :
    (∃ (n : ℕ) (k : ℤ), 3 ≤ n ∧ 1 ≤ k ∧ k ≤ ((n / 2 : ℕ) : ℤ)) ∧
    (∃ (n : ℕ) (k : ℤ), 3 ≤ n ∧ ((n / 2 : ℕ) : ℤ) + 1 ≤ k ∧ k ≤ (n : ℤ) - 2) :=
  ⟨⟨3, 1, by norm_num, by norm_num, by norm_num⟩,
    ⟨5, 3, by norm_num, by norm_num, by norm_num⟩⟩

end Conjectura.Research.CollinsShorPeak
