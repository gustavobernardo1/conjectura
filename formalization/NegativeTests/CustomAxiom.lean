/- NEGATIVE TEST. Must be rejected: the theorem depends on a project-defined axiom. -/
namespace NegativeTests

axiom convenient : ∀ n : Nat, n < 10

theorem uses_custom_axiom : (100 : Nat) < 10 :=
  convenient 100

end NegativeTests
