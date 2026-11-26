/-
NEGATIVE TEST. A "theorem" `bogus : False` is added to the environment with
kernel type checking disabled; its proof term `True.intro` does not have type
`False`. The declaration depends on no axioms, so the axiom audit alone would
accept it. It must be rejected by the kernel replay (`leanchecker`) and by the
source scan (`debug.skipKernelTC`).
-/
import Lean

open Lean Elab Command

set_option debug.skipKernelTC true in
run_cmd liftCoreM do
  addDecl <| .thmDecl {
    name := `NegativeTests.bogus
    levelParams := []
    type := mkConst ``False
    value := mkConst ``True.intro }
