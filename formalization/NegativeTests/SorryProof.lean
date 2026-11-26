/- NEGATIVE TEST. Must be rejected: the proof is `sorry` (axiom `sorryAx`). -/
namespace NegativeTests

theorem sorry_claim : (2 : Nat) + 2 = 5 := by
  sorry

end NegativeTests
