/-
CALIBRATION — a classical known result, not a research result of this project.
Purpose: exercise build, axiom audit, statement fingerprinting and kernel replay
on a statement without hypotheses.
-/
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.Ring

namespace Conjectura.Calibration

open Finset

/-- The sum of the first `n` odd natural numbers equals `n ^ 2`. -/
theorem sum_range_odd (n : ℕ) : ∑ i ∈ range n, (2 * i + 1) = n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, ih]
    ring

end Conjectura.Calibration
