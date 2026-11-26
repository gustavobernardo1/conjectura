/-
NEGATIVE TEST. Must be rejected: the module declares an `unsafe` definition and
disables kernel type checking for a declaration.
-/
namespace NegativeTests

unsafe def unchecked : Nat := 0

set_option debug.skipKernelTC true in
theorem skips_kernel : (1 : Nat) = 1 := rfl

end NegativeTests
