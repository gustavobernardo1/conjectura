/-
RESEARCH — problem CJ-0001 (Collins–Shor peak conjecture), supporting
definitions and lemmas.

Source: `research/active/CJ-0001-collins-shor-peak/notes/wiener-form.md`,
paragraph "The cones `K_d`" (with (K1), (K2)) and "Lemma A" in the section
"Theorem T4".

  `K_d` is the set of finite non-negative combinations of the polynomials
  `x^e (1 + x)^i` with `e, i ≥ 0` and `2e + i ≥ d`.

  Lemma A. Let `μ ≥ 1`, `g = x^e (1 + x)^i`, `λ_μ(f) = [x^μ] f − [x^{μ−1}] f`.
  (a) If `2e + i ≥ 2μ − 1`, then `λ_μ(g) ≥ 0`.
  (b) If `2e + i ≥ 2μ` and `W ≥ 3n`, then `λ_μ((W − n x) g) ≥ 0`.

This module defines the cone over `Polynomial ℝ`, proves (K1), (K2), the
binomial inequalities behind Lemma A, and Lemma A for every element of the
cone (by linearity). It says nothing about trees or distance matrices: neither
Proposition S25, nor S26, nor Theorem T4 of the note is formalized here.

Encoding:

* coefficients are real: the cone lives in `Polynomial ℝ`;
* `WienerCone d p` ("`p ∈ K_d`") is an inductive predicate, in the style of
  `HalfGammaCone`: the smallest set of polynomials that contains `0` and the
  generators `X ^ e * (1 + X) ^ i` (`d ≤ 2 * e + i`) and is closed under
  addition and under multiplication by `C a` with `0 ≤ a`. That this predicate
  coincides with the set of explicit finite sums is NOT proved here, and no
  non-membership example is proved;
* the index `d` is a natural number; the note allows an integer `d` (for
  `d ≤ 0` the condition `2e + i ≥ d` is void, as it is for `d = 0`);
* `W − n x` is `C W - C n * X`, with real `W`, `n`;
* in the binomial statements the convention "`C(i, k) = 0` for `k < 0`" of the
  note is written out: the term `C(i, a − 2)` is
  `if a = 1 then 0 else i.choose (a - 2)`. All other natural subtractions
  (`a - 1`, `a - 2` in the `else` branch, `μ - 1`) are true subtractions under
  the hypotheses in force;
* in Lemma A(b) the note takes `W, n` positive with `W ≥ 3n`; here the
  non-strict statements assume only `0 ≤ n` and `3 * n ≤ W` (weaker
  hypotheses), and the strict binomial statement assumes `0 < n`.

Strictness. The note states the strict inequality of Lemma A(b) for one
generator with `a = μ − e ≥ 1` (`wiener_choose_step_strict` is its binomial
form) and uses it in Theorem T4 for a combination in which some generator with
`e = 0` has a positive coefficient, which it derives from `Φ(0) = 1`. The cone
statement proved here (`WienerCone.coeff_sub_mul_pred_lt_coeff`) takes that
hypothesis in the form `0 < f.coeff 0`. The strict inequality for a single
generator with `e > 0`, `a ≥ 1` is covered only by the binomial form, not by a
cone-level statement.
-/
import Conjectura.Research.CollinsShorPeak.HalfGammaCone
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity

namespace Conjectura.Research.CollinsShorPeak

open Polynomial

/-! ### Binomial inequalities (Lemma A for one generator) -/

/-- **Lemma A(a), binomial form.** If `1 ≤ a` and `2a ≤ i + 1`, then
`C(i, a − 1) ≤ C(i, a)`. -/
theorem choose_pred_le_choose {i a : ℕ} (ha : 1 ≤ a) (h : 2 * a ≤ i + 1) :
    i.choose (a - 1) ≤ i.choose a := by
  obtain ⟨b, rfl⟩ : ∃ b, a = b + 1 := ⟨a - 1, by omega⟩
  rw [Nat.add_sub_cancel]
  have h2 := Nat.choose_succ_right_eq i b
  have hle : b + 1 ≤ i - b := by omega
  have h3 : i.choose b * (b + 1) ≤ i.choose b * (i - b) := Nat.mul_le_mul_left _ hle
  rw [← h2] at h3
  exact Nat.le_of_mul_le_mul_right h3 (Nat.succ_pos b)

/-- The algebraic identity behind Lemma A(b): with `c1 = C(i, a − 1)`,
`c0 = C(i, a − 2)`, `c2 = C(i, a)`, `A = a`, `B = i − a + 2`, `s = i − 2a + 1`. -/
theorem wiener_real_identity {c0 c1 c2 A B s W n : ℝ} (hB : B = A + s + 1)
    (h1 : c1 * (A - 1) = c0 * B) (h2 : c2 * A = c1 * (B - 1)) :
    (W * (c2 - c1) - n * (c1 - c0)) * (A * B) =
      c1 * ((W - 3 * n) * (B * s) + n * (2 * A * (s - 1) + 3 * s ^ 2 + 3 * s)) := by
  subst hB
  linear_combination (W * (A + s + 1)) * h2 - (n * A) * h1

/-- Real form of Lemma A(b), non-strict. -/
theorem wiener_real_step {c0 c1 c2 A B s W n : ℝ} (hc1 : 0 ≤ c1) (hA : 1 ≤ A) (hs : 1 ≤ s)
    (hB : B = A + s + 1) (h1 : c1 * (A - 1) = c0 * B) (h2 : c2 * A = c1 * (B - 1))
    (hn : 0 ≤ n) (hW : 3 * n ≤ W) : n * (c1 - c0) ≤ W * (c2 - c1) := by
  have hid := wiener_real_identity (W := W) (n := n) hB h1 h2
  have hBpos : 0 < B := by rw [hB]; linarith
  have hAB : 0 < A * B := mul_pos (by linarith) hBpos
  have hq : 0 ≤ 2 * A * (s - 1) + 3 * s ^ 2 + 3 * s := by
    have hAs := mul_nonneg (by linarith : (0 : ℝ) ≤ A) (by linarith : (0 : ℝ) ≤ s - 1)
    nlinarith [hAs, sq_nonneg s, hs]
  have hW3 : 0 ≤ W - 3 * n := by linarith
  have hBs : 0 ≤ B * s := mul_nonneg hBpos.le (by linarith)
  have hr : 0 ≤ c1 * ((W - 3 * n) * (B * s) + n * (2 * A * (s - 1) + 3 * s ^ 2 + 3 * s)) :=
    mul_nonneg hc1 (add_nonneg (mul_nonneg hW3 hBs) (mul_nonneg hn hq))
  rw [← hid] at hr
  have h0 : 0 ≤ W * (c2 - c1) - n * (c1 - c0) := by
    by_contra hneg
    have hlt := mul_neg_of_neg_of_pos (not_le.mp hneg) hAB
    linarith
  linarith

/-- Real form of Lemma A(b), strict. -/
theorem wiener_real_step_strict {c0 c1 c2 A B s W n : ℝ} (hc1 : 0 < c1) (hA : 1 ≤ A)
    (hs : 1 ≤ s) (hB : B = A + s + 1) (h1 : c1 * (A - 1) = c0 * B)
    (h2 : c2 * A = c1 * (B - 1)) (hn : 0 < n) (hW : 3 * n ≤ W) :
    n * (c1 - c0) < W * (c2 - c1) := by
  have hid := wiener_real_identity (W := W) (n := n) hB h1 h2
  have hBpos : 0 < B := by rw [hB]; linarith
  have hAB : 0 < A * B := mul_pos (by linarith) hBpos
  have hq : 0 < 2 * A * (s - 1) + 3 * s ^ 2 + 3 * s := by
    have hAs := mul_nonneg (by linarith : (0 : ℝ) ≤ A) (by linarith : (0 : ℝ) ≤ s - 1)
    nlinarith [hAs, sq_nonneg s, hs]
  have hW3 : 0 ≤ W - 3 * n := by linarith
  have hBs : 0 ≤ B * s := mul_nonneg hBpos.le (by linarith)
  have hr : 0 < c1 * ((W - 3 * n) * (B * s) + n * (2 * A * (s - 1) + 3 * s ^ 2 + 3 * s)) :=
    mul_pos hc1 (add_pos_of_nonneg_of_pos (mul_nonneg hW3 hBs) (mul_pos hn hq))
  rw [← hid] at hr
  have h0 : 0 < W * (c2 - c1) - n * (c1 - c0) := by
    by_contra hneg
    have hle := mul_nonneg (neg_nonneg.mpr (not_lt.mp hneg)) hAB.le
    linarith
  linarith

/-- The two ratio identities between consecutive binomial coefficients used in
Lemma A(b), over `ℝ`, with `C(i, a − 2)` read as `0` when `a = 1`. -/
theorem wiener_choose_data {i a : ℕ} (ha : 1 ≤ a) (hi : 2 * a ≤ i) :
    (i.choose (a - 1) : ℝ) * ((a : ℝ) - 1) =
        (if a = 1 then 0 else (i.choose (a - 2) : ℝ)) * ((i : ℝ) - a + 2) ∧
      (i.choose a : ℝ) * (a : ℝ) = (i.choose (a - 1) : ℝ) * ((i : ℝ) - a + 2 - 1) := by
  obtain ⟨b, rfl⟩ : ∃ b, a = b + 1 := ⟨a - 1, by omega⟩
  have hbi : b ≤ i := by omega
  have h2 : (i.choose (b + 1) : ℝ) * ((b : ℝ) + 1) = (i.choose b : ℝ) * ((i : ℝ) - b) := by
    have h := congrArg (Nat.cast : ℕ → ℝ) (Nat.choose_succ_right_eq i b)
    push_cast [Nat.cast_sub hbi] at h
    exact h
  refine ⟨?_, ?_⟩
  · rcases b with _ | b'
    · simp
    · have hbi' : b' ≤ i := by omega
      have h1 : (i.choose (b' + 1) : ℝ) * ((b' : ℝ) + 1) =
          (i.choose b' : ℝ) * ((i : ℝ) - b') := by
        have h := congrArg (Nat.cast : ℕ → ℝ) (Nat.choose_succ_right_eq i b')
        push_cast [Nat.cast_sub hbi'] at h
        exact h
      have hne : ¬ (b' + 1 + 1 = 1) := by omega
      have e1 : b' + 1 + 1 - 1 = b' + 1 := by omega
      have e2 : b' + 1 + 1 - 2 = b' := by omega
      rw [ite_eq_right hne, e1, e2]
      push_cast
      linear_combination h1
  · rw [Nat.add_sub_cancel]
    push_cast
    linear_combination h2

/-- **Lemma A(b), binomial form.** For `1 ≤ a`, `2a ≤ i` and reals `0 ≤ n`,
`3n ≤ W`:
`n (C(i, a − 1) − C(i, a − 2)) ≤ W (C(i, a) − C(i, a − 1))`,
where `C(i, a − 2)` is `0` for `a = 1`. -/
theorem wiener_choose_step {i a : ℕ} (ha : 1 ≤ a) (hi : 2 * a ≤ i) {W n : ℝ}
    (hn : 0 ≤ n) (hW : 3 * n ≤ W) :
    n * ((i.choose (a - 1) : ℝ) - (if a = 1 then 0 else (i.choose (a - 2) : ℝ))) ≤
      W * ((i.choose a : ℝ) - (i.choose (a - 1) : ℝ)) := by
  obtain ⟨h1, h2⟩ := wiener_choose_data ha hi
  have hiR : (2 : ℝ) * a ≤ i := by exact_mod_cast hi
  have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
  exact wiener_real_step (A := (a : ℝ)) (B := (i : ℝ) - a + 2) (s := (i : ℝ) - 2 * a + 1)
    (Nat.cast_nonneg _) haR (by linarith) (by ring) h1 h2 hn hW

/-- **Lemma A(b), binomial form, strict.** For `1 ≤ a`, `2a ≤ i` and reals
`0 < n`, `3n ≤ W` the inequality of `wiener_choose_step` is strict. -/
theorem wiener_choose_step_strict {i a : ℕ} (ha : 1 ≤ a) (hi : 2 * a ≤ i) {W n : ℝ}
    (hn : 0 < n) (hW : 3 * n ≤ W) :
    n * ((i.choose (a - 1) : ℝ) - (if a = 1 then 0 else (i.choose (a - 2) : ℝ))) <
      W * ((i.choose a : ℝ) - (i.choose (a - 1) : ℝ)) := by
  obtain ⟨h1, h2⟩ := wiener_choose_data ha hi
  have hiR : (2 : ℝ) * a ≤ i := by exact_mod_cast hi
  have haR : (1 : ℝ) ≤ a := by exact_mod_cast ha
  have hle : a - 1 ≤ i := by omega
  have hpos : (0 : ℝ) < (i.choose (a - 1) : ℝ) := by exact_mod_cast Nat.choose_pos hle
  exact wiener_real_step_strict (A := (a : ℝ)) (B := (i : ℝ) - a + 2)
    (s := (i : ℝ) - 2 * a + 1) hpos haR (by linarith) (by ring) h1 h2 hn hW

/-- Lemma A(b), binomial form, for `a = b + 2 ≥ 2` (no convention needed):
`n (C(i, b + 1) − C(i, b)) ≤ W (C(i, b + 2) − C(i, b + 1))` when
`2 (b + 2) ≤ i`. -/
theorem wiener_choose_step_add_two {i b : ℕ} (hi : 2 * (b + 2) ≤ i) {W n : ℝ}
    (hn : 0 ≤ n) (hW : 3 * n ≤ W) :
    n * ((i.choose (b + 1) : ℝ) - (i.choose b : ℝ)) ≤
      W * ((i.choose (b + 2) : ℝ) - (i.choose (b + 1) : ℝ)) := by
  have ha : 1 ≤ b + 2 := by omega
  have h := wiener_choose_step ha hi hn hW
  have hne : ¬ (b + 2 = 1) := by omega
  have e1 : b + 2 - 1 = b + 1 := by omega
  have e2 : b + 2 - 2 = b := by omega
  rw [ite_eq_right hne, e1, e2] at h
  exact h

/-- Lemma A(b), binomial form, for `a = 1`: `n C(i, 0) ≤ W (C(i, 1) − C(i, 0))`
when `2 ≤ i` (the term `C(i, −1)` is `0`). -/
theorem wiener_choose_step_one {i : ℕ} (hi : 2 ≤ i) {W n : ℝ}
    (hn : 0 ≤ n) (hW : 3 * n ≤ W) :
    n * (i.choose 0 : ℝ) ≤ W * ((i.choose 1 : ℝ) - (i.choose 0 : ℝ)) := by
  have hi' : 2 * 1 ≤ i := by omega
  have h := wiener_choose_step (a := 1) le_rfl hi' hn hW
  have e1 : (1 : ℕ) - 1 = 0 := rfl
  rw [ite_eq_left rfl, e1, sub_zero] at h
  exact h

/-! ### The cone `K_d` -/

/-- `WienerCone d p`: the real polynomial `p` is a non-negative combination of
the polynomials `X ^ e * (1 + X) ^ i` with `d ≤ 2 * e + i` (the cone `K_d` of
the notes). -/
inductive WienerCone (d : ℕ) : Polynomial ℝ → Prop
  | zero : WienerCone d 0
  | gen (e i : ℕ) (h : d ≤ 2 * e + i) : WienerCone d (X ^ e * (1 + X) ^ i)
  | add {p q : Polynomial ℝ} : WienerCone d p → WienerCone d q → WienerCone d (p + q)
  | smul {p : Polynomial ℝ} (a : ℝ) (ha : 0 ≤ a) : WienerCone d p → WienerCone d (C a * p)

/-- **(K2), monotonicity.** `K_d ⊆ K_d'` for `d' ≤ d`. -/
theorem WienerCone.mono {d d' : ℕ} (h : d' ≤ d) {p : Polynomial ℝ} (hp : WienerCone d p) :
    WienerCone d' p := by
  induction hp with
  | zero => exact WienerCone.zero
  | gen e i h1 => exact WienerCone.gen e i (by omega)
  | add _ _ ih1 ih2 => exact WienerCone.add ih1 ih2
  | smul a ha _ ih => exact WienerCone.smul a ha ih

/-- **(K2).** `K_{d+1} ⊆ K_d`. -/
theorem WienerCone.of_succ {d : ℕ} {p : Polynomial ℝ} (hp : WienerCone (d + 1) p) :
    WienerCone d p :=
  hp.mono (Nat.le_succ d)

/-- **(K2), products.** `K_d · K_d' ⊆ K_{d + d'}`. -/
theorem WienerCone.mul {d d' : ℕ} {p q : Polynomial ℝ}
    (hp : WienerCone d p) (hq : WienerCone d' q) : WienerCone (d + d') (p * q) := by
  induction hp with
  | zero =>
    rw [zero_mul]
    exact WienerCone.zero
  | gen e i h1 =>
    induction hq with
    | zero =>
      rw [mul_zero]
      exact WienerCone.zero
    | gen e' i' h1' =>
      have h : (X : Polynomial ℝ) ^ e * (1 + X) ^ i * (X ^ e' * (1 + X) ^ i') =
          X ^ (e + e') * (1 + X) ^ (i + i') := by
        rw [pow_add, pow_add]
        ring
      rw [h]
      exact WienerCone.gen (e + e') (i + i') (by omega)
    | add _ _ ih1 ih2 =>
      rw [mul_add]
      exact WienerCone.add ih1 ih2
    | smul a ha _ ih =>
      rw [mul_left_comm]
      exact WienerCone.smul a ha ih
  | add _ _ ih1 ih2 =>
    rw [add_mul]
    exact WienerCone.add ih1 ih2
  | smul a ha _ ih =>
    rw [mul_assoc]
    exact WienerCone.smul a ha ih

/-- `1 ∈ K_0`. -/
theorem WienerCone.one_mem_zero : WienerCone 0 (1 : Polynomial ℝ) := by
  have h := WienerCone.gen (d := 0) 0 0 (by norm_num)
  simpa using h

/-- `1 + x ∈ K_1`. -/
theorem WienerCone.one_add_X_mem_one : WienerCone 1 (1 + X : Polynomial ℝ) := by
  have h := WienerCone.gen (d := 1) 0 1 (by norm_num)
  simpa using h

/-- `x ∈ K_2`. -/
theorem WienerCone.X_mem_two : WienerCone 2 (X : Polynomial ℝ) := by
  have h := WienerCone.gen (d := 2) 1 0 (by norm_num)
  simpa using h

/-- **(K2).** `(1 + x) · K_d ⊆ K_{d+1}`. -/
theorem WienerCone.one_add_X_mul_mem_succ {d : ℕ} {p : Polynomial ℝ}
    (hp : WienerCone d p) : WienerCone (d + 1) ((1 + X) * p) := by
  rw [mul_comm (1 + X) p]
  exact hp.mul WienerCone.one_add_X_mem_one

/-- **(K2).** `x · K_d ⊆ K_{d+2}`. -/
theorem WienerCone.X_mul_mem_add_two {d : ℕ} {p : Polynomial ℝ} (hp : WienerCone d p) :
    WienerCone (d + 2) (X * p) := by
  rw [mul_comm X p]
  exact hp.mul WienerCone.X_mem_two

/-- **(K1).** `C_d ⊆ K_d`. -/
theorem WienerCone.of_halfGammaCone {d : ℕ} {p : Polynomial ℝ} (hp : HalfGammaCone d p) :
    WienerCone d p := by
  induction hp with
  | zero => exact WienerCone.zero
  | gen e i _ h2 => exact WienerCone.gen e i h2
  | add _ _ ih1 ih2 => exact WienerCone.add ih1 ih2
  | smul a ha _ ih => exact WienerCone.smul a ha ih

/-! ### Lemma A on the cone -/

/-- Coefficients of a generator: `[x^k] x^e (1 + x)^i = C(i, k − e)` for
`e ≤ k`, and `0` otherwise. -/
theorem coeff_X_pow_mul_one_add_X_pow (e i k : ℕ) :
    ((X : Polynomial ℝ) ^ e * (1 + X) ^ i).coeff k =
      if e ≤ k then (i.choose (k - e) : ℝ) else 0 := by
  rw [coeff_X_pow_mul', coeff_one_add_X_pow]

/-- **Lemma A(a) on the cone**, index `μ = m + 1`: for `f ∈ K_{2m+1}`,
`[x^m] f ≤ [x^{m+1}] f`. -/
theorem WienerCone.coeff_le_coeff_succ {m : ℕ} {f : Polynomial ℝ}
    (hf : WienerCone (2 * m + 1) f) : f.coeff m ≤ f.coeff (m + 1) := by
  induction hf with
  | zero => simp
  | gen e i h =>
    rw [coeff_X_pow_mul_one_add_X_pow, coeff_X_pow_mul_one_add_X_pow]
    by_cases h1 : e ≤ m
    · have h1' : e ≤ m + 1 := by omega
      have ha : 1 ≤ m + 1 - e := by omega
      have hi : 2 * (m + 1 - e) ≤ i + 1 := by omega
      have hc := choose_pred_le_choose ha hi
      have e1 : m + 1 - e - 1 = m - e := by omega
      rw [e1] at hc
      rw [ite_eq_left h1, ite_eq_left h1']
      exact_mod_cast hc
    · rw [ite_eq_right h1]
      split_ifs
      · exact Nat.cast_nonneg _
      · exact le_rfl
  | add _ _ ih1 ih2 =>
    rw [coeff_add, coeff_add]
    linarith
  | smul a ha _ ih =>
    rw [coeff_C_mul, coeff_C_mul]
    exact mul_le_mul_of_nonneg_left ih ha

/-- **Lemma A(a) on the cone.** For `μ ≥ 1` and `f ∈ K_{2μ−1}`:
`[x^{μ−1}] f ≤ [x^μ] f`. -/
theorem WienerCone.coeff_pred_le_coeff {μ : ℕ} (hμ : 1 ≤ μ) {f : Polynomial ℝ}
    (hf : WienerCone (2 * μ - 1) f) : f.coeff (μ - 1) ≤ f.coeff μ := by
  obtain ⟨m, rfl⟩ : ∃ m, μ = m + 1 := ⟨μ - 1, by omega⟩
  have e1 : 2 * (m + 1) - 1 = 2 * m + 1 := by omega
  rw [e1] at hf
  rw [Nat.add_sub_cancel]
  exact hf.coeff_le_coeff_succ

/-- **Lemma A(b) on the cone**, index `μ = m + 1`: for `f ∈ K_{2(m+1)}` and
reals `0 ≤ n`, `3n ≤ W`: `[x^m] (W − n x) f ≤ [x^{m+1}] (W − n x) f`. -/
theorem WienerCone.coeff_sub_mul_le_coeff_succ {m : ℕ} {f : Polynomial ℝ}
    (hf : WienerCone (2 * (m + 1)) f) {W n : ℝ} (hn : 0 ≤ n) (hW : 3 * n ≤ W) :
    ((C W - C n * X) * f).coeff m ≤ ((C W - C n * X) * f).coeff (m + 1) := by
  induction hf with
  | zero => simp
  | gen e i h =>
    have hcoef : ∀ k : ℕ, ((C W - C n * X) * (X ^ e * (1 + X) ^ i)).coeff k =
        W * (if e ≤ k then (i.choose (k - e) : ℝ) else 0) -
          n * (if e + 1 ≤ k then (i.choose (k - (e + 1)) : ℝ) else 0) := by
      intro k
      have hsplit : (C W - C n * X) * (X ^ e * (1 + X) ^ i) =
          C W * (X ^ e * (1 + X) ^ i) - C n * (X ^ (e + 1) * (1 + X) ^ i) := by
        rw [pow_succ]
        ring
      rw [hsplit, coeff_sub, coeff_C_mul, coeff_C_mul, coeff_X_pow_mul_one_add_X_pow,
        coeff_X_pow_mul_one_add_X_pow]
    rw [hcoef, hcoef]
    by_cases h1 : e ≤ m
    · -- `a = m + 1 - e ≥ 1`
      have ha : 1 ≤ m + 1 - e := by omega
      have hi : 2 * (m + 1 - e) ≤ i := by omega
      have hstep := wiener_choose_step ha hi hn hW
      have h1' : e ≤ m + 1 := by omega
      have h1'' : e + 1 ≤ m + 1 := by omega
      have x1 : m - e = m + 1 - e - 1 := by omega
      have x2 : m + 1 - (e + 1) = m + 1 - e - 1 := by omega
      have x3 : (if e + 1 ≤ m then (i.choose (m - (e + 1)) : ℝ) else 0) =
          (if m + 1 - e = 1 then 0 else (i.choose (m + 1 - e - 2) : ℝ)) := by
        by_cases h2 : e + 1 ≤ m
        · have hne : ¬ (m + 1 - e = 1) := by omega
          have x4 : m - (e + 1) = m + 1 - e - 2 := by omega
          rw [ite_eq_left h2, ite_eq_right hne, x4]
        · have heq : m + 1 - e = 1 := by omega
          rw [ite_eq_right h2, ite_eq_left heq]
      rw [ite_eq_left h1, ite_eq_left h1', ite_eq_left h1'', x3, x1, x2]
      linarith
    · have h2 : ¬ (e + 1 ≤ m) := by omega
      have h3 : ¬ (e + 1 ≤ m + 1) := by omega
      rw [ite_eq_right h1, ite_eq_right h2, ite_eq_right h3]
      have hW0 : 0 ≤ W := by linarith
      split_ifs
      · have hc : (0 : ℝ) ≤ (i.choose (m + 1 - e) : ℝ) := Nat.cast_nonneg _
        have := mul_nonneg hW0 hc
        linarith
      · linarith
  | add _ _ ih1 ih2 =>
    rw [mul_add, coeff_add, coeff_add]
    linarith
  | smul a ha _ ih =>
    rw [mul_left_comm, coeff_C_mul, coeff_C_mul]
    exact mul_le_mul_of_nonneg_left ih ha

/-- **Lemma A(b) on the cone.** For `μ ≥ 1`, `f ∈ K_{2μ}` and reals `0 ≤ n`,
`3n ≤ W`: `[x^{μ−1}] (W − n x) f ≤ [x^μ] (W − n x) f`. -/
theorem WienerCone.coeff_sub_mul_pred_le_coeff {μ : ℕ} (hμ : 1 ≤ μ) {f : Polynomial ℝ}
    (hf : WienerCone (2 * μ) f) {W n : ℝ} (hn : 0 ≤ n) (hW : 3 * n ≤ W) :
    ((C W - C n * X) * f).coeff (μ - 1) ≤ ((C W - C n * X) * f).coeff μ := by
  obtain ⟨m, rfl⟩ : ∃ m, μ = m + 1 := ⟨μ - 1, by omega⟩
  rw [Nat.add_sub_cancel]
  exact hf.coeff_sub_mul_le_coeff_succ hn hW

/-- **Lemma A(b) on the cone, strict**, index `μ = m + 1`: for `f ∈ K_{2(m+1)}`
with `0 < [x^0] f` and reals `0 < n`, `3n ≤ W`:
`[x^m] (W − n x) f < [x^{m+1}] (W − n x) f`. (A positive constant term forces
a generator with `e = 0` and positive coefficient.) -/
theorem WienerCone.coeff_sub_mul_lt_coeff_succ {m : ℕ} {f : Polynomial ℝ}
    (hf : WienerCone (2 * (m + 1)) f) {W n : ℝ} (hn : 0 < n) (hW : 3 * n ≤ W) :
    0 < f.coeff 0 →
      ((C W - C n * X) * f).coeff m < ((C W - C n * X) * f).coeff (m + 1) := by
  induction hf with
  | zero =>
    intro h0
    simp at h0
  | gen e i h =>
    intro h0
    have he : e = 0 := by
      by_contra he
      have hne : ¬ (e ≤ 0) := by omega
      rw [coeff_X_pow_mul_one_add_X_pow, ite_eq_right hne] at h0
      exact lt_irrefl _ h0
    have hcoef : ∀ k : ℕ, ((C W - C n * X) * (X ^ e * (1 + X) ^ i)).coeff k =
        W * (if e ≤ k then (i.choose (k - e) : ℝ) else 0) -
          n * (if e + 1 ≤ k then (i.choose (k - (e + 1)) : ℝ) else 0) := by
      intro k
      have hsplit : (C W - C n * X) * (X ^ e * (1 + X) ^ i) =
          C W * (X ^ e * (1 + X) ^ i) - C n * (X ^ (e + 1) * (1 + X) ^ i) := by
        rw [pow_succ]
        ring
      rw [hsplit, coeff_sub, coeff_C_mul, coeff_C_mul, coeff_X_pow_mul_one_add_X_pow,
        coeff_X_pow_mul_one_add_X_pow]
    rw [hcoef, hcoef]
    have h1 : e ≤ m := by omega
    have ha : 1 ≤ m + 1 - e := by omega
    have hi : 2 * (m + 1 - e) ≤ i := by omega
    have hstep := wiener_choose_step_strict ha hi hn hW
    have h1' : e ≤ m + 1 := by omega
    have h1'' : e + 1 ≤ m + 1 := by omega
    have x1 : m - e = m + 1 - e - 1 := by omega
    have x2 : m + 1 - (e + 1) = m + 1 - e - 1 := by omega
    have x3 : (if e + 1 ≤ m then (i.choose (m - (e + 1)) : ℝ) else 0) =
        (if m + 1 - e = 1 then 0 else (i.choose (m + 1 - e - 2) : ℝ)) := by
      by_cases h2 : e + 1 ≤ m
      · have hne : ¬ (m + 1 - e = 1) := by omega
        have x4 : m - (e + 1) = m + 1 - e - 2 := by omega
        rw [ite_eq_left h2, ite_eq_right hne, x4]
      · have heq : m + 1 - e = 1 := by omega
        rw [ite_eq_right h2, ite_eq_left heq]
    rw [ite_eq_left h1, ite_eq_left h1', ite_eq_left h1'', x3, x1, x2]
    linarith
  | @add p q hp hq ih1 ih2 =>
    intro h0
    rw [coeff_add] at h0
    have lp := hp.coeff_sub_mul_le_coeff_succ hn.le hW
    have lq := hq.coeff_sub_mul_le_coeff_succ hn.le hW
    rw [mul_add, coeff_add, coeff_add]
    by_cases hp0 : 0 < p.coeff 0
    · have sp := ih1 hp0
      linarith
    · have hq0 : 0 < q.coeff 0 := by linarith [not_lt.mp hp0]
      have sq := ih2 hq0
      linarith
  | @smul p a ha hp ih =>
    intro h0
    rw [coeff_C_mul] at h0
    have ha' : 0 < a := by
      rcases ha.lt_or_eq with h | h
      · exact h
      · rw [← h, zero_mul] at h0
        exact absurd h0 (lt_irrefl _)
    have hp0 : 0 < p.coeff 0 := by
      by_contra hc
      have hle := mul_nonneg ha (neg_nonneg.mpr (not_lt.mp hc))
      linarith
    rw [mul_left_comm, coeff_C_mul, coeff_C_mul]
    exact mul_lt_mul_of_pos_left (ih hp0) ha'

/-- **Lemma A(b) on the cone, strict.** For `μ ≥ 1`, `f ∈ K_{2μ}` with
`0 < [x^0] f` and reals `0 < n`, `3n ≤ W`:
`[x^{μ−1}] (W − n x) f < [x^μ] (W − n x) f`. -/
theorem WienerCone.coeff_sub_mul_pred_lt_coeff {μ : ℕ} (hμ : 1 ≤ μ) {f : Polynomial ℝ}
    (hf : WienerCone (2 * μ) f) {W n : ℝ} (hn : 0 < n) (hW : 3 * n ≤ W)
    (h0 : 0 < f.coeff 0) :
    ((C W - C n * X) * f).coeff (μ - 1) < ((C W - C n * X) * f).coeff μ := by
  obtain ⟨m, rfl⟩ : ∃ m, μ = m + 1 := ⟨μ - 1, by omega⟩
  rw [Nat.add_sub_cancel]
  exact hf.coeff_sub_mul_lt_coeff_succ hn hW h0

/-! ### Non-vacuity -/

/-- `(1 + x)^i ∈ K_i`. -/
theorem WienerCone.one_add_X_pow_mem (i : ℕ) :
    WienerCone i ((1 + X : Polynomial ℝ) ^ i) := by
  have h := WienerCone.gen (d := i) 0 i (by omega)
  simpa using h

/-- The hypotheses of the cone statements of Lemma A are satisfiable for every
`μ`: `(1 + x)^{2μ} ∈ K_{2μ}` has constant term `1 > 0` (and `K_{2μ} ⊆ K_{2μ−1}`),
with for instance `W = 3`, `n = 1`. -/
theorem WienerCone.lemmaA_hypotheses_witness (μ : ℕ) :
    WienerCone (2 * μ) ((1 + X : Polynomial ℝ) ^ (2 * μ)) ∧
      WienerCone (2 * μ - 1) ((1 + X : Polynomial ℝ) ^ (2 * μ)) ∧
      0 < ((1 + X : Polynomial ℝ) ^ (2 * μ)).coeff 0 ∧ (0 : ℝ) < 1 ∧ (3 : ℝ) * 1 ≤ 3 := by
  refine ⟨WienerCone.one_add_X_pow_mem _,
    (WienerCone.one_add_X_pow_mem _).mono (Nat.sub_le _ _), ?_, one_pos, by norm_num⟩
  rw [coeff_one_add_X_pow]
  simp

end Conjectura.Research.CollinsShorPeak
