/-
RESEARCH — problem CJ-0001 (Collins–Shor peak conjecture), supporting lemma.

Source statement: "General form" of R1 in
`research/active/CJ-0001-collins-shor-peak/notes/lemmas.md`:

  Let `a_0, …, a_r` be positive and log-concave and let `1 ≤ j ≤ r`. Then every
  maximizing index of the sequence is `≥ j` if and only if `a_{j−1} < a_j`.

This is an elementary fact about finite log-concave sequences. It is a tool of
the investigation, not a claimed result, and it says nothing about distance
matrices of trees: that the coefficient sequence of CJ-0001 is positive and
log-concave is an external theorem that is not formalized here.

Encoding (see the clause-by-clause comparison in the registry entry and in the
session report):

* the sequence is `a : ℕ → ℝ`; only the values `a 0, …, a r` are constrained or
  mentioned, the values at indices `> r` are irrelevant;
* positivity: `∀ k ≤ r, 0 < a k`;
* log-concavity `a_k² ≥ a_{k−1} a_{k+1}` for `1 ≤ k ≤ r − 1` is written with the
  middle index shifted by one, `∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2`,
  which avoids subtraction in `ℕ`; `logConcave_shift_iff` proves that this is
  equivalent to the literal form;
* `1 ≤ j ≤ r` is the pair of hypotheses `1 ≤ j`, `j ≤ r`, and `a_{j−1}` is
  `a (j - 1)` with truncated subtraction in `ℕ`, which is the true predecessor
  because `1 ≤ j`;
* "`i` is a maximizing index" is `i ≤ r ∧ ∀ k ≤ r, a k ≤ a i`, written inline.
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace Conjectura.Research.CollinsShorPeak

/-- The shifted form of log-concavity used in this file is equivalent to the
literal form `a_k² ≥ a_{k−1} a_{k+1}` for `1 ≤ k ≤ r − 1` of the written
statement (`k ≤ r − 1` is written `k + 1 ≤ r`). -/
theorem logConcave_shift_iff (a : ℕ → ℝ) (r : ℕ) :
    (∀ k, 1 ≤ k → k + 1 ≤ r → a (k - 1) * a (k + 1) ≤ a k ^ 2) ↔
      (∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2) := by
  constructor
  · intro h k hk
    have h' := h (k + 1) (by omega) (by omega)
    rw [Nat.add_sub_cancel] at h'
    exact h'
  · intro h k h1 hk
    obtain ⟨m, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, by omega⟩
    have h' := h m (by omega)
    rw [Nat.add_sub_cancel]
    exact h'

/-- One step downwards: an increase at `k + 1` forces an increase at `k`. -/
theorem lt_succ_of_succ_lt (a : ℕ → ℝ) (r : ℕ)
    (hpos : ∀ k ≤ r, 0 < a k)
    (hlc : ∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2)
    (k : ℕ) (hk : k + 2 ≤ r) (h : a (k + 1) < a (k + 2)) : a k < a (k + 1) := by
  have h1 := hpos (k + 1) (by omega)
  have h2 := hpos (k + 2) hk
  have h3 := hlc k hk
  by_contra hcon
  have hcon' : a (k + 1) ≤ a k := not_lt.mp hcon
  nlinarith [mul_le_mul_of_nonneg_right hcon' h2.le, mul_lt_mul_of_pos_left h h1]

/-- If the sequence increases strictly from `m` to `m + 1`, it increases
strictly at every earlier step. -/
theorem lt_succ_of_le (a : ℕ → ℝ) (r : ℕ)
    (hpos : ∀ k ≤ r, 0 < a k)
    (hlc : ∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2)
    (m : ℕ) (hm : m + 1 ≤ r) (h : a m < a (m + 1)) :
    ∀ k ≤ m, a k < a (k + 1) := by
  have key : ∀ d k, k + d = m → a k < a (k + 1) := by
    intro d
    induction d with
    | zero =>
      intro k hk
      have hkm : k = m := by omega
      rw [hkm]
      exact h
    | succ d ih =>
      intro k hk
      exact lt_succ_of_succ_lt a r hpos hlc k (by omega) (ih (k + 1) (by omega))
  intro k hk
  exact key (m - k) k (by omega)

/-- **Direction used by the investigation.** For a positive log-concave
sequence `a 0, …, a r` and `1 ≤ j ≤ r`, if `a (j - 1) < a j` then
`a i < a j` for every `i < j`. -/
theorem lt_of_pred_lt (a : ℕ → ℝ) (r j : ℕ)
    (hpos : ∀ k ≤ r, 0 < a k)
    (hlc : ∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2)
    (hj1 : 1 ≤ j) (hjr : j ≤ r) (h : a (j - 1) < a j) :
    ∀ i < j, a i < a j := by
  obtain ⟨m, rfl⟩ : ∃ m, j = m + 1 := ⟨j - 1, by omega⟩
  rw [Nat.add_sub_cancel] at h
  have inc := lt_succ_of_le a r hpos hlc m hjr h
  intro i hi
  have key : ∀ d, i + d ≤ m → a i < a (i + d + 1) := by
    intro d
    induction d with
    | zero =>
      intro hd
      exact inc i (by omega)
    | succ d ih =>
      intro hd
      exact lt_trans (ih (by omega)) (inc (i + (d + 1)) hd)
  have hkey := key (m - i) (by omega)
  have e : i + (m - i) + 1 = m + 1 := by omega
  rw [e] at hkey
  exact hkey

/-- **Direction used by the investigation, in the wording of the written
statement.** For a positive log-concave sequence `a 0, …, a r` and
`1 ≤ j ≤ r`, if `a (j - 1) < a j` then every maximizing index is `≥ j`. -/
theorem maxIndex_ge_of_pred_lt (a : ℕ → ℝ) (r j : ℕ)
    (hpos : ∀ k ≤ r, 0 < a k)
    (hlc : ∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2)
    (hj1 : 1 ≤ j) (hjr : j ≤ r) (h : a (j - 1) < a j) :
    ∀ i ≤ r, (∀ k ≤ r, a k ≤ a i) → j ≤ i := by
  intro i _ hmax
  by_contra hcon
  have hij : i < j := not_le.mp hcon
  exact absurd (lt_of_pred_lt a r j hpos hlc hj1 hjr h i hij) (not_lt.mpr (hmax j hjr))

/-- A finite sequence `a 0, …, a r` of reals has a maximizing index. -/
theorem exists_maxIndex (a : ℕ → ℝ) (r : ℕ) : ∃ i ≤ r, ∀ k ≤ r, a k ≤ a i := by
  induction r with
  | zero =>
    refine ⟨0, le_rfl, fun k hk => ?_⟩
    have hk0 : k = 0 := by omega
    rw [hk0]
  | succ r ih =>
    obtain ⟨i, hi, hmax⟩ := ih
    by_cases hc : a i ≤ a (r + 1)
    · refine ⟨r + 1, le_rfl, fun k hk => ?_⟩
      by_cases hk' : k ≤ r
      · exact le_trans (hmax k hk') hc
      · have hkr : k = r + 1 := by omega
        rw [hkr]
    · refine ⟨i, by omega, fun k hk => ?_⟩
      by_cases hk' : k ≤ r
      · exact hmax k hk'
      · have hkr : k = r + 1 := by omega
        rw [hkr]
        exact (not_le.mp hc).le

/-- If the sequence does not increase from `m` to `m + 1`, it is non-increasing
from `m` on. -/
theorem le_of_succ_le (a : ℕ → ℝ) (r : ℕ)
    (hpos : ∀ k ≤ r, 0 < a k)
    (hlc : ∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2)
    (m : ℕ) (h : a (m + 1) ≤ a m) :
    ∀ i, m ≤ i → i ≤ r → a i ≤ a m := by
  have dec : ∀ d, m + d + 1 ≤ r → a (m + d + 1) ≤ a (m + d) := by
    intro d
    induction d with
    | zero =>
      intro _
      exact h
    | succ d ih =>
      intro hd
      have hprev : a (m + d + 1) ≤ a (m + d) := ih (by omega)
      by_contra hcon
      have hlt : a (m + d + 1) < a (m + d + 2) := not_le.mp hcon
      exact absurd (lt_succ_of_succ_lt a r hpos hlc (m + d) (by omega) hlt) (not_lt.mpr hprev)
  have key : ∀ d, m + d ≤ r → a (m + d) ≤ a m := by
    intro d
    induction d with
    | zero =>
      intro _
      exact le_rfl
    | succ d ih =>
      intro hd
      exact le_trans (dec d hd) (ih (by omega))
  intro i hmi hir
  have hkey := key (i - m) (by omega)
  have e : m + (i - m) = i := by omega
  rw [e] at hkey
  exact hkey

/-- **General form of R1.** For a positive log-concave sequence `a 0, …, a r`
and `1 ≤ j ≤ r`: every maximizing index is `≥ j` if and only if
`a (j - 1) < a j`. -/
theorem maxIndex_ge_iff_pred_lt (a : ℕ → ℝ) (r j : ℕ)
    (hpos : ∀ k ≤ r, 0 < a k)
    (hlc : ∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2)
    (hj1 : 1 ≤ j) (hjr : j ≤ r) :
    (∀ i ≤ r, (∀ k ≤ r, a k ≤ a i) → j ≤ i) ↔ a (j - 1) < a j := by
  constructor
  · intro hall
    by_contra hcon
    have hle : a j ≤ a (j - 1) := not_lt.mp hcon
    obtain ⟨m, rfl⟩ : ∃ m, j = m + 1 := ⟨j - 1, by omega⟩
    rw [Nat.add_sub_cancel] at hle
    have dec := le_of_succ_le a r hpos hlc m hle
    obtain ⟨i, hi, hmax⟩ := exists_maxIndex a r
    have hji : m + 1 ≤ i := hall i hi hmax
    have hm : ∀ k ≤ r, a k ≤ a m := fun k hk => le_trans (hmax k hk) (dec i (by omega) hi)
    have hbad : m + 1 ≤ m := hall m (by omega) hm
    omega
  · exact maxIndex_ge_of_pred_lt a r j hpos hlc hj1 hjr

/-- Non-vacuity witness: the hypotheses of `lt_of_pred_lt`,
`maxIndex_ge_of_pred_lt` and `maxIndex_ge_iff_pred_lt` (including the strict
inequality `a (j - 1) < a j`) hold for the sequence `1, 2, 3, 4`, with `r = 3`
and `j = 2`. The log-concavity hypothesis is exercised at `k = 0` and `k = 1`. -/
theorem hypotheses_nonvacuous :
    ∃ (a : ℕ → ℝ) (r j : ℕ), (∀ k ≤ r, 0 < a k) ∧
      (∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2) ∧
      1 ≤ j ∧ j ≤ r ∧ a (j - 1) < a j := by
  refine ⟨fun k => (k : ℝ) + 1, 3, 2, ?_, ?_, by norm_num, by norm_num, by norm_num⟩
  · intro k _
    have hk0 : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
    show (0 : ℝ) < (k : ℝ) + 1
    linarith
  · intro k hk
    have hk01 : k = 0 ∨ k = 1 := by omega
    rcases hk01 with rfl | rfl <;> norm_num

/-- The hypotheses of `maxIndex_ge_iff_pred_lt` do not decide the equivalence:
they also hold for the constant sequence `1, 1, 1` with `r = 2`, `j = 1`, where
`a (j - 1) < a j` fails. -/
theorem hypotheses_nonvacuous_not_lt :
    ∃ (a : ℕ → ℝ) (r j : ℕ), (∀ k ≤ r, 0 < a k) ∧
      (∀ k, k + 2 ≤ r → a k * a (k + 2) ≤ a (k + 1) ^ 2) ∧
      1 ≤ j ∧ j ≤ r ∧ ¬ a (j - 1) < a j :=
  ⟨fun _ => 1, 2, 1, fun _ _ => one_pos, fun _ _ => by norm_num, le_rfl, by norm_num,
    by norm_num⟩

end Conjectura.Research.CollinsShorPeak
