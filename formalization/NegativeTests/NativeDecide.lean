/-
NEGATIVE TEST. Must be rejected: `native_decide` trusts the compiler and adds
the axiom `Lean.ofReduceBool`. The statement is true; the mechanism is untrusted.
-/
namespace NegativeTests

theorem by_native_decide : (2 : Nat) ^ 10 = 1024 := by
  native_decide

end NegativeTests
