/-
NEGATIVE TEST. The theorem is kernel-valid and axiom-free, but its hypothesis is
unsatisfiable, so it proves nothing. The registry check must reject it when it
is registered without a non-vacuity witness.
-/
namespace NegativeTests

theorem vacuous_claim (n : Nat) (h : n < 0) : n = 37 :=
  absurd h (Nat.not_lt_zero n)

end NegativeTests
