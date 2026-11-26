/-
RESEARCH — problem CJ-0001 (Collins–Shor peak conjecture), supporting
definitions and lemmas.

Source: `research/active/CJ-0001-collins-shor-peak/notes/skeleton-locality.md`,
section "Lemma C (the cone of Property Γ)", and the head of
`notes/gamma-components.md` ("Two elementary facts about the cones").

  `C_d` is the set of non-negative combinations of the polynomials
  `x^e (1 + x)^i` with `e, i ≥ 0`, `e + i ≤ d` and `2e + i ≥ d`
  ("polynomials of weight at least `d`").

This module defines that cone over `Polynomial ℝ` and proves its elementary
closure properties. It says nothing about trees or distance matrices, and it
does not prove Property Γ for any polynomial of the investigation.

Encoding:

* coefficients are real: the cone lives in `Polynomial ℝ`;
* `HalfGammaCone d p` ("`p ∈ C_d`") is an inductive predicate: the smallest
  set of polynomials that contains `0` and the generators
  `X ^ e * (1 + X) ^ i` (`e + i ≤ d`, `d ≤ 2 * e + i`) and is closed under
  addition and under multiplication by `C a` with `0 ≤ a`. This is the set of
  finite non-negative combinations of the generators. That this predicate
  coincides with the set of explicit sums `∑ c(e, i) x^e (1 + x)^i`, `c ≥ 0`,
  is NOT proved in this module, and no non-membership example is proved;
* a non-negative scalar multiple is `Polynomial.C a * p`;
* a non-negative half-gamma expansion of degree `d` is
  `HasNonnegHalfGamma d p`: `p = ∑_{e = 0}^{d} c_e b_{d,e}` with all `c_e ≥ 0`,
  where `b_{d,e} = x^e (1 + x)^(d − 2e)` if `2e < d` and `b_{d,e} = x^e` if
  `d ≤ 2e` (`halfGammaBasis`). This is the expansion
  `Σ_{2e<d} ρ_e x^e (1+x)^{d−2e} + Σ_{d ≤ 2e ≤ 2d} σ_e x^e` of the notes with
  the two families of coefficients indexed by the single index `e ≤ d`; in
  `d - 2 * e` the subtraction is the true one because it is used only when
  `2 * e < d`.

`hasNonnegHalfGamma_of_halfGammaCone` is Lemma C: every element of `C_d` has a
non-negative half-gamma expansion of degree `d`. The uniqueness of the
expansion (invoked in the notes for the last sentence of Lemma C) is not
needed for that statement and is not formalized.
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace Conjectura.Research.CollinsShorPeak

open Polynomial

/-- `HalfGammaCone d p`: the real polynomial `p` is a non-negative combination
of the polynomials `X ^ e * (1 + X) ^ i` with `e + i ≤ d` and `d ≤ 2 * e + i`
(the cone `C_d` of the notes). -/
inductive HalfGammaCone (d : ℕ) : Polynomial ℝ → Prop
  | zero : HalfGammaCone d 0
  | gen (e i : ℕ) (h1 : e + i ≤ d) (h2 : d ≤ 2 * e + i) :
      HalfGammaCone d (X ^ e * (1 + X) ^ i)
  | add {p q : Polynomial ℝ} : HalfGammaCone d p → HalfGammaCone d q → HalfGammaCone d (p + q)
  | smul {p : Polynomial ℝ} (a : ℝ) (ha : 0 ≤ a) : HalfGammaCone d p → HalfGammaCone d (C a * p)

/-- **Products.** `C_d · C_d' ⊆ C_{d + d'}`: the two index conditions are
additive. -/
theorem HalfGammaCone.mul {d d' : ℕ} {p q : Polynomial ℝ}
    (hp : HalfGammaCone d p) (hq : HalfGammaCone d' q) : HalfGammaCone (d + d') (p * q) := by
  induction hp with
  | zero =>
    rw [zero_mul]
    exact HalfGammaCone.zero
  | gen e i h1 h2 =>
    induction hq with
    | zero =>
      rw [mul_zero]
      exact HalfGammaCone.zero
    | gen e' i' h1' h2' =>
      have h : (X : Polynomial ℝ) ^ e * (1 + X) ^ i * (X ^ e' * (1 + X) ^ i') =
          X ^ (e + e') * (1 + X) ^ (i + i') := by
        rw [pow_add, pow_add]
        ring
      rw [h]
      exact HalfGammaCone.gen (e + e') (i + i') (by omega) (by omega)
    | add _ _ ih1 ih2 =>
      rw [mul_add]
      exact HalfGammaCone.add ih1 ih2
    | smul a ha _ ih =>
      rw [mul_left_comm]
      exact HalfGammaCone.smul a ha ih
  | add _ _ ih1 ih2 =>
    rw [add_mul]
    exact HalfGammaCone.add ih1 ih2
  | smul a ha _ ih =>
    rw [mul_assoc]
    exact HalfGammaCone.smul a ha ih

/-- `1 ∈ C_0`. -/
theorem HalfGammaCone.one_mem_zero : HalfGammaCone 0 (1 : Polynomial ℝ) := by
  have h := HalfGammaCone.gen (d := 0) 0 0 (by norm_num) (by norm_num)
  simpa using h

/-- `x ∈ C_1`. -/
theorem HalfGammaCone.X_mem_one : HalfGammaCone 1 (X : Polynomial ℝ) := by
  have h := HalfGammaCone.gen (d := 1) 1 0 (by norm_num) (by norm_num)
  simpa using h

/-- `x ∈ C_2`. -/
theorem HalfGammaCone.X_mem_two : HalfGammaCone 2 (X : Polynomial ℝ) := by
  have h := HalfGammaCone.gen (d := 2) 1 0 (by norm_num) (by norm_num)
  simpa using h

/-- `1 + x ∈ C_1`. -/
theorem HalfGammaCone.one_add_X_mem_one : HalfGammaCone 1 (1 + X : Polynomial ℝ) := by
  have h := HalfGammaCone.gen (d := 1) 0 1 (by norm_num) (by norm_num)
  simpa using h

/-- `x (1 + x) ∈ C_3`. -/
theorem HalfGammaCone.X_mul_one_add_X_mem_three :
    HalfGammaCone 3 (X * (1 + X) : Polynomial ℝ) := by
  have h := HalfGammaCone.gen (d := 3) 1 1 (by norm_num) (by norm_num)
  simpa using h

/-- `x · C_d ⊆ C_{d+1}`. -/
theorem HalfGammaCone.X_mul_mem_succ {d : ℕ} {p : Polynomial ℝ} (hp : HalfGammaCone d p) :
    HalfGammaCone (d + 1) (X * p) := by
  rw [mul_comm X p]
  exact hp.mul HalfGammaCone.X_mem_one

/-- `x · C_d ⊆ C_{d+2}`. -/
theorem HalfGammaCone.X_mul_mem_add_two {d : ℕ} {p : Polynomial ℝ} (hp : HalfGammaCone d p) :
    HalfGammaCone (d + 2) (X * p) := by
  rw [mul_comm X p]
  exact hp.mul HalfGammaCone.X_mem_two

/-- `(1 + x) · C_d ⊆ C_{d+1}`. -/
theorem HalfGammaCone.one_add_X_mul_mem_succ {d : ℕ} {p : Polynomial ℝ}
    (hp : HalfGammaCone d p) : HalfGammaCone (d + 1) ((1 + X) * p) := by
  rw [mul_comm (1 + X) p]
  exact hp.mul HalfGammaCone.one_add_X_mem_one

/-- `x (1 + x) · C_d ⊆ C_{d+3}`. -/
theorem HalfGammaCone.X_mul_one_add_X_mul_mem_add_three {d : ℕ} {p : Polynomial ℝ}
    (hp : HalfGammaCone d p) : HalfGammaCone (d + 3) (X * (1 + X) * p) := by
  rw [mul_comm (X * (1 + X)) p]
  exact hp.mul HalfGammaCone.X_mul_one_add_X_mem_three

/-- `1 + 4x ∈ C_1`: `1 + 4x = (1 + x) + 3x`. -/
theorem HalfGammaCone.one_add_four_X_mem_one :
    HalfGammaCone 1 (1 + 4 * X : Polynomial ℝ) := by
  have h : (1 + 4 * X : Polynomial ℝ) = (1 + X) + C 3 * X := by
    rw [show (C 3 : Polynomial ℝ) = 3 from map_ofNat C 3]
    ring
  rw [h]
  exact HalfGammaCone.add HalfGammaCone.one_add_X_mem_one
    (HalfGammaCone.smul 3 (by norm_num) HalfGammaCone.X_mem_one)

/-- `x (1 + 5x + 3x²) ∈ C_4`: `x (1 + 5x + 3x²) = x (1 + x)² + 3x² + 2x³`. -/
theorem HalfGammaCone.X_mul_cubic_mem_four :
    HalfGammaCone 4 (X * (1 + 5 * X + 3 * X ^ 2) : Polynomial ℝ) := by
  have h : (X * (1 + 5 * X + 3 * X ^ 2) : Polynomial ℝ) =
      X ^ 1 * (1 + X) ^ 2 + (C 3 * (X ^ 2 * (1 + X) ^ 0) + C 2 * (X ^ 3 * (1 + X) ^ 0)) := by
    rw [show (C 3 : Polynomial ℝ) = 3 from map_ofNat C 3,
      show (C 2 : Polynomial ℝ) = 2 from map_ofNat C 2]
    ring
  rw [h]
  exact HalfGammaCone.add (HalfGammaCone.gen 1 2 (by norm_num) (by norm_num))
    (HalfGammaCone.add
      (HalfGammaCone.smul 3 (by norm_num) (HalfGammaCone.gen 2 0 (by norm_num) (by norm_num)))
      (HalfGammaCone.smul 2 (by norm_num) (HalfGammaCone.gen 3 0 (by norm_num) (by norm_num))))

/-- The half-gamma basis of degree `d`, indexed by `e` (meaningful for
`e ≤ d`): `x^e (1 + x)^(d − 2e)` if `2e < d`, and `x^e` if `d ≤ 2e`. -/
noncomputable def halfGammaBasis (d e : ℕ) : Polynomial ℝ :=
  if 2 * e < d then X ^ e * (1 + X) ^ (d - 2 * e) else X ^ e

/-- `p` has a non-negative half-gamma expansion of degree `d`: it is a
combination of the basis elements `halfGammaBasis d e`, `e ≤ d`, with
non-negative real coefficients. -/
def HasNonnegHalfGamma (d : ℕ) (p : Polynomial ℝ) : Prop :=
  ∃ c : ℕ → ℝ, (∀ e, 0 ≤ c e) ∧ p = ∑ e ∈ Finset.range (d + 1), C (c e) * halfGammaBasis d e

theorem HasNonnegHalfGamma.zero (d : ℕ) : HasNonnegHalfGamma d 0 :=
  ⟨fun _ => 0, fun _ => le_rfl, by simp⟩

theorem HasNonnegHalfGamma.add {d : ℕ} {p q : Polynomial ℝ}
    (hp : HasNonnegHalfGamma d p) (hq : HasNonnegHalfGamma d q) :
    HasNonnegHalfGamma d (p + q) := by
  obtain ⟨c, hc, rfl⟩ := hp
  obtain ⟨c', hc', rfl⟩ := hq
  refine ⟨fun e => c e + c' e, fun e => add_nonneg (hc e) (hc' e), ?_⟩
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun e _ => ?_)
  simp only [C_add, add_mul]

theorem HasNonnegHalfGamma.smul {d : ℕ} {p : Polynomial ℝ} (a : ℝ) (ha : 0 ≤ a)
    (hp : HasNonnegHalfGamma d p) : HasNonnegHalfGamma d (C a * p) := by
  obtain ⟨c, hc, rfl⟩ := hp
  refine ⟨fun e => a * c e, fun e => mul_nonneg ha (hc e), ?_⟩
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun e _ => ?_)
  simp only [C_mul, mul_assoc]

theorem HasNonnegHalfGamma.basis (d e : ℕ) (he : e ≤ d) :
    HasNonnegHalfGamma d (halfGammaBasis d e) := by
  have hnn : ∀ e' : ℕ, (0 : ℝ) ≤ if e' = e then 1 else 0 := by
    intro e'
    split_ifs <;> norm_num
  refine ⟨fun e' => if e' = e then 1 else 0, hnn, ?_⟩
  rw [Finset.sum_eq_single e]
  · simp
  · intro b _ hb
    simp [hb]
  · intro h
    exact absurd (Finset.mem_range.mpr (by omega)) h

/-- The generators of `C_d` have a non-negative half-gamma expansion of degree
`d` (first sentence of Lemma C; induction on the exponent of `1 + x`). -/
theorem HasNonnegHalfGamma.gen (d : ℕ) : ∀ (i e : ℕ), e + i ≤ d → d ≤ 2 * e + i →
    HasNonnegHalfGamma d (X ^ e * (1 + X) ^ i) := by
  intro i
  induction i with
  | zero =>
    intro e h1 h2
    have hb : halfGammaBasis d e = X ^ e := by
      have hn : ¬ 2 * e < d := by omega
      simp [halfGammaBasis, hn]
    have h := HasNonnegHalfGamma.basis d e (by omega)
    rw [hb] at h
    rw [pow_zero, mul_one]
    exact h
  | succ i ih =>
    intro e h1 h2
    by_cases heq : 2 * e + (i + 1) = d
    · have hb : halfGammaBasis d e = X ^ e * (1 + X) ^ (i + 1) := by
        have hd : d - 2 * e = i + 1 := by omega
        have hlt : 2 * e < d := by omega
        simp [halfGammaBasis, hlt, hd]
      rw [← hb]
      exact HasNonnegHalfGamma.basis d e (by omega)
    · have hsplit : (X : Polynomial ℝ) ^ e * (1 + X) ^ (i + 1) =
          X ^ e * (1 + X) ^ i + X ^ (e + 1) * (1 + X) ^ i := by
        rw [pow_succ, pow_succ]
        ring
      rw [hsplit]
      exact HasNonnegHalfGamma.add (ih e (by omega) (by omega)) (ih (e + 1) (by omega) (by omega))

/-- **Lemma C.** Every element of the cone `C_d` has a non-negative half-gamma
expansion of degree `d`. -/
theorem hasNonnegHalfGamma_of_halfGammaCone {d : ℕ} {p : Polynomial ℝ}
    (hp : HalfGammaCone d p) : HasNonnegHalfGamma d p := by
  induction hp with
  | zero => exact HasNonnegHalfGamma.zero d
  | gen e i h1 h2 => exact HasNonnegHalfGamma.gen d i e h1 h2
  | add _ _ ih1 ih2 => exact ih1.add ih2
  | smul a ha _ ih => exact ih.smul a ha

end Conjectura.Research.CollinsShorPeak
