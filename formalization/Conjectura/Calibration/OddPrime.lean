/-
CALIBRATION — a classical known result, not a research result of this project.
Purpose: exercise the non-vacuity requirement. The theorem has hypotheses, so
the registry must name a witness showing that the hypotheses are satisfiable.
-/
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime

namespace Conjectura.Calibration

/-- Every prime greater than `2` is odd. -/
theorem odd_of_prime_of_two_lt (p : ℕ) (hp : p.Prime) (h : 2 < p) : Odd p :=
  hp.odd_of_ne_two (Nat.ne_of_gt h)

/-- Non-vacuity witness for `odd_of_prime_of_two_lt`: its hypotheses hold for `p = 3`. -/
theorem odd_of_prime_of_two_lt_nonvacuous : ∃ p : ℕ, p.Prime ∧ 2 < p :=
  ⟨3, by norm_num, by norm_num⟩

end Conjectura.Calibration
