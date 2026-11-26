/- NEGATIVE TEST. Must be rejected: the statement is false and the file does not compile. -/
namespace NegativeTests

theorem wrong_claim : (2 : Nat) + 2 = 5 := by
  decide

end NegativeTests
