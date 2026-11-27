/-
RESEARCH — problem CJ-0001 (Collins–Shor peak conjecture), supporting lemma.

Source statement: Lemma S41 of
`research/active/CJ-0001-collins-shor-peak/notes/upper-bound.md`, read as a
statement about finite real sequences:

  Let `n ≥ 3` and `0 ≤ k ≤ n − 3`. If `q_{k+1} < q_k`, then `d_{j+1} < d_j`
  for every `k ≤ j ≤ n − 3`; hence every maximizing index of
  `d_0, …, d_{n−2}` is `≤ k`.

Only the sequence lemma is formalized. The facts that the proof of S41 takes
from elsewhere are hypotheses here: positivity of `q_0, …, q_{n−1}`, the
strict decrease of the ratios `q_{j+1}/q_j` (which the note derives from
Newton's inequalities), `α > 0`, and `q_{n−1}/q_{n−2} = 1/α` (which the note
derives from `α = Σ β_i`). Nothing about trees, distance matrices, Lemma S40,
Darroch's rule or the trace of `(I + L)^{−1}` is formalized.

Encoding:

* `N = n − 1` (so `n ≥ 3` is `2 ≤ N`), and the sequence is `q : ℕ → ℝ`; only
  `q 0, …, q N` are constrained, values at indices `> N` are irrelevant;
* positivity: `∀ j ≤ N, 0 < q j`;
* strictly decreasing ratios `q_{j+1}/q_j` (`0 ≤ j ≤ N − 1`) is written without
  division and without subtraction in `ℕ` as
  `∀ j, j + 2 ≤ N → q j * q (j + 2) < q (j + 1) ^ 2`;
  `ratio_strictAnti_iff` proves that, under positivity, this is equivalent to
  `q (j + 2) / q (j + 1) < q (j + 1) / q j` for `j + 2 ≤ N`;
* `t_{n−2} = q_{n−1}/q_{n−2} = 1/α` with `α > 0` is written
  `q (N - 1) = α * q N` (truncated subtraction is the true predecessor
  because `2 ≤ N`);
* `d_k = α q_k − q_{k−1}` with `q_{−1} = 0` is `upperD α q k`; the note's
  `d_k` is `4 * upperD α q k` (the positive factor 4 changes no inequality
  between the `d_j`); `upperD_zero` and `upperD_of_pos` give the two cases;
* `0 ≤ k ≤ n − 3` is `k + 2 ≤ N`; `k ≤ j ≤ n − 3` is `k ≤ j`, `j + 2 ≤ N`;
* "`p` is a maximizing index of `d_0, …, d_{n−2}`" is
  `p + 1 ≤ N ∧ ∀ j, j + 1 ≤ N → upperD α q j ≤ upperD α q p`.
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace Conjectura.Research.CollinsShorPeak

/-- `upperD α q k = α q_k − q_{k−1}`, with `q_{−1} = 0`: a quarter of the
coefficient `d_k` of Lemma S40 in `notes/upper-bound.md`. -/
def upperD (α : ℝ) (q : ℕ → ℝ) : ℕ → ℝ
  | 0 => α * q 0
  | k + 1 => α * q (k + 1) - q k

theorem upperD_zero (α : ℝ) (q : ℕ → ℝ) : upperD α q 0 = α * q 0 := rfl

theorem upperD_of_pos (α : ℝ) (q : ℕ → ℝ) (k : ℕ) (hk : 1 ≤ k) :
    upperD α q k = α * q k - q (k - 1) := by
  obtain ⟨m, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, by omega⟩
  rfl

/-- Agreement with the textbook definition on an example: for `α = 2` and
`q = (3, 2, 1, …)`, `d_0 = 6`, `d_1 = 1`, `d_2 = 0`. -/
theorem upperD_example :
    let q : ℕ → ℝ := fun j => if j = 0 then 3 else if j = 1 then 2 else 1
    upperD 2 q 0 = 6 ∧ upperD 2 q 1 = 1 ∧ upperD 2 q 2 = 0 := by
  simp only [upperD]
  norm_num

/-- Under positivity, the product form of the ratio hypothesis is equivalent
to strict decrease of the ratios `q_{j+1}/q_j` for `0 ≤ j ≤ N − 1`. -/
theorem ratio_strictAnti_iff (q : ℕ → ℝ) (N : ℕ) (hpos : ∀ j ≤ N, 0 < q j) :
    (∀ j, j + 2 ≤ N → q j * q (j + 2) < q (j + 1) ^ 2) ↔
      (∀ j, j + 2 ≤ N → q (j + 2) / q (j + 1) < q (j + 1) / q j) := by
  constructor
  · intro h j hj
    have h0 := hpos j (by omega)
    have h1 := hpos (j + 1) (by omega)
    rw [div_lt_div_iff₀ h1 h0]
    have := h j hj
    nlinarith
  · intro h j hj
    have h0 := hpos j (by omega)
    have h1 := hpos (j + 1) (by omega)
    have := h j hj
    rw [div_lt_div_iff₀ h1 h0] at this
    nlinarith

/-- Step (A) of the proof of S41: `α t_j > 1`, that is `α q_{j+1} > q_j`, for
`j ≤ N − 2`. -/
theorem upper_alpha_ratio_gt (q : ℕ → ℝ) (N : ℕ) (α : ℝ) (hN : 2 ≤ N)
    (hpos : ∀ j ≤ N, 0 < q j)
    (hrat : ∀ j, j + 2 ≤ N → q j * q (j + 2) < q (j + 1) ^ 2)
    (hα : 0 < α) (hlast : q (N - 1) = α * q N) :
    ∀ j, j + 2 ≤ N → q j < α * q (j + 1) := by
  have key : ∀ g j, j + 2 + g = N → q j < α * q (j + 1) := by
    intro g
    induction g with
    | zero =>
      intro j hj
      have e : N - 1 = j + 1 := by omega
      rw [e] at hlast
      have hr := hrat j (by omega)
      have hN' : q N = q (j + 2) := by rw [← hj]
      rw [hN'] at hlast
      have h2 := hpos (j + 2) (by omega)
      -- q j * q (j+2) < q (j+1)^2 = α q (j+2) q (j+1)
      have : q j * q (j + 2) < (α * q (j + 1)) * q (j + 2) := by
        rw [hlast] at hr ⊢
        nlinarith
      exact lt_of_mul_lt_mul_right this h2.le
    | succ g ih =>
      intro j hj
      have ih' := ih (j + 1) (by omega)
      have hr := hrat j (by omega)
      have h0 := hpos j (by omega)
      have h1 := hpos (j + 1) (by omega)
      have h2 := hpos (j + 2) (by omega)
      have hA : α * (q j * q (j + 2)) < α * q (j + 1) ^ 2 := mul_lt_mul_of_pos_left hr hα
      have hB : q (j + 1) * q j < α * q (j + 2) * q j := mul_lt_mul_of_pos_right ih' h0
      have : q j * q (j + 1) < (α * q (j + 1)) * q (j + 1) := by nlinarith
      exact lt_of_mul_lt_mul_right this h1.le
  intro j hj
  exact key (N - (j + 2)) j (by omega)

/-- Step (B) of the proof of S41: once `q_{k+1} < q_k`, the sequence `q` is
strictly decreasing from `k` to `N`. -/
theorem upper_q_succ_lt (q : ℕ → ℝ) (N : ℕ)
    (hpos : ∀ j ≤ N, 0 < q j)
    (hrat : ∀ j, j + 2 ≤ N → q j * q (j + 2) < q (j + 1) ^ 2)
    (k : ℕ) (hk : q (k + 1) < q k) :
    ∀ j, k ≤ j → j + 1 ≤ N → q (j + 1) < q j := by
  have key : ∀ g, k + g + 1 ≤ N → q (k + g + 1) < q (k + g) := by
    intro g
    induction g with
    | zero => intro _; simpa using hk
    | succ g ih =>
      intro hg
      have ih' := ih (by omega)
      have hr := hrat (k + g) (by omega)
      have h0 := hpos (k + g) (by omega)
      have h1 := hpos (k + g + 1) (by omega)
      have e1 : k + (g + 1) = k + g + 1 := by omega
      rw [e1]
      show q (k + g + 2) < q (k + g + 1)
      have : q (k + g) * q (k + g + 2) < q (k + g) * q (k + g + 1) := by nlinarith
      exact lt_of_mul_lt_mul_left this h0.le
  intro j hkj hj
  have e : k + (j - k) = j := by omega
  have := key (j - k) (by omega)
  rw [e] at this
  exact this

/-- **Lemma S41 (sequence form), first part.** Let `N ≥ 2`, `q_0, …, q_N > 0`
with strictly decreasing ratios `q_{j+1}/q_j`, `α > 0` with
`q_{N−1} = α q_N`, and `d_k = α q_k − q_{k−1}` (`q_{−1} = 0`). If
`k ≤ N − 2` and `q_{k+1} < q_k`, then `d_{j+1} < d_j` for every
`k ≤ j ≤ N − 2`. The hypothesis `k ≤ N − 2` (`_hkN`) is kept to match the
source statement; the proof does not use it. -/
theorem upperD_succ_lt (q : ℕ → ℝ) (N : ℕ) (α : ℝ) (hN : 2 ≤ N)
    (hpos : ∀ j ≤ N, 0 < q j)
    (hrat : ∀ j, j + 2 ≤ N → q j * q (j + 2) < q (j + 1) ^ 2)
    (hα : 0 < α) (hlast : q (N - 1) = α * q N)
    (k : ℕ) (_hkN : k + 2 ≤ N) (hk : q (k + 1) < q k) :
    ∀ j, k ≤ j → j + 2 ≤ N → upperD α q (j + 1) < upperD α q j := by
  intro j hkj hj
  have hdec := upper_q_succ_lt q N hpos hrat k hk
  cases j with
  | zero =>
    have h10 := hdec 0 hkj (by omega)
    have h0 := hpos 0 (by omega)
    simp only [upperD]
    nlinarith
  | succ i =>
    -- a = q i, b = q (i+1), c = q (i+2)
    have hcb := hdec (i + 1) hkj (by omega)
    have h0 := hpos i (by omega)
    have h1 := hpos (i + 1) (by omega)
    have hr := hrat i (by omega)
    have hA := upper_alpha_ratio_gt q N α hN hpos hrat hα hlast i (by omega)
    simp only [upperD]
    rcases le_or_gt (q i) (q (i + 1)) with hab | hab
    · nlinarith
    · -- a (b − c) > b (a − b), from b² > a c
      have h3 : q (i + 1) * (q i - q (i + 1)) < q i * (q (i + 1) - q (i + 2)) := by
        nlinarith
      have h4 : α * (q (i + 1) * (q i - q (i + 1))) <
          α * (q i * (q (i + 1) - q (i + 2))) := mul_lt_mul_of_pos_left h3 hα
      have h5 : q i * (q i - q (i + 1)) < α * q (i + 1) * (q i - q (i + 1)) :=
        mul_lt_mul_of_pos_right hA (by linarith)
      have h6 : q i * (q i - q (i + 1)) < q i * (α * (q (i + 1) - q (i + 2))) := by
        nlinarith
      have h7 : q i - q (i + 1) < α * (q (i + 1) - q (i + 2)) :=
        lt_of_mul_lt_mul_left h6 h0.le
      linarith

/-- **Lemma S41 (sequence form), consequence.** Under the hypotheses of
`upperD_succ_lt`, every maximizing index `p ≤ N − 1` of `d_0, …, d_{N−1}`
satisfies `p ≤ k`. -/
theorem upperD_maxIndex_le (q : ℕ → ℝ) (N : ℕ) (α : ℝ) (hN : 2 ≤ N)
    (hpos : ∀ j ≤ N, 0 < q j)
    (hrat : ∀ j, j + 2 ≤ N → q j * q (j + 2) < q (j + 1) ^ 2)
    (hα : 0 < α) (hlast : q (N - 1) = α * q N)
    (k : ℕ) (hkN : k + 2 ≤ N) (hk : q (k + 1) < q k) :
    ∀ p, p + 1 ≤ N → (∀ j, j + 1 ≤ N → upperD α q j ≤ upperD α q p) → p ≤ k := by
  intro p hp hmax
  by_contra hcon
  obtain ⟨m, rfl⟩ : ∃ m, p = m + 1 := ⟨p - 1, by omega⟩
  have hlt := upperD_succ_lt q N α hN hpos hrat hα hlast k hkN hk m (by omega) (by omega)
  have hle := hmax m (by omega)
  linarith

/-- Non-vacuity witness: all hypotheses of `upperD_succ_lt` and
`upperD_maxIndex_le` hold for `N = 2`, `q = (3, 2, 1)`, `α = 2`, `k = 0`
(`2² > 3·1`, `q_1 = 2 q_2`, `q_1 < q_0`). -/
theorem upperD_hypotheses_nonvacuous :
    ∃ (q : ℕ → ℝ) (N : ℕ) (α : ℝ) (k : ℕ), 2 ≤ N ∧ (∀ j ≤ N, 0 < q j) ∧
      (∀ j, j + 2 ≤ N → q j * q (j + 2) < q (j + 1) ^ 2) ∧
      0 < α ∧ q (N - 1) = α * q N ∧ k + 2 ≤ N ∧ q (k + 1) < q k := by
  refine ⟨fun j => if j = 0 then 3 else if j = 1 then 2 else 1, 2, 2, 0,
    le_rfl, ?_, ?_, by norm_num, by norm_num, le_rfl, by norm_num⟩
  · intro j hj
    have : j = 0 ∨ j = 1 ∨ j = 2 := by omega
    rcases this with rfl | rfl | rfl <;> norm_num
  · intro j hj
    have : j = 0 := by omega
    subst this
    norm_num

end Conjectura.Research.CollinsShorPeak
