/-
Axiom and declaration audit, instantiated by `scripts/verify_lean.py`.

`__MODULE__` is replaced by the root module to audit and `__PREFIX__` by the
module-name prefix that identifies project-owned declarations. The file is
elaborated with `lake env lean`; it prints one JSON array describing every
declaration whose defining module starts with the prefix:

  name, module, kind, unsafe, partial, axioms (transitive), statement, type_hash

The decision about what is acceptable is taken in Python, so that the policy
lives in one place (`docs/verification-policy.md`, `scripts/verify_lean.py`).
-/
import __MODULE__
import Lean

open Lean Elab Command Meta

namespace ConjecturaAudit

def kindOf : ConstantInfo → String
  | .axiomInfo _ => "axiom"
  | .defnInfo _ => "def"
  | .thmInfo _ => "theorem"
  | .opaqueInfo _ => "opaque"
  | .quotInfo _ => "quot"
  | .inductInfo _ => "inductive"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"

end ConjecturaAudit

run_cmd do
  let env ← getEnv
  let pfx : Name := `__PREFIX__
  let owned : Array (Name × ConstantInfo × Name) :=
    env.constants.fold (init := #[]) fun acc name ci =>
      match env.getModuleIdxFor? name with
      | some idx =>
        let modName := env.header.moduleNames[idx.toNat]!
        if pfx.isPrefixOf modName then acc.push (name, ci, modName) else acc
      | none => acc
  let mut rows : Array Json := #[]
  for (name, ci, modName) in owned do
    let axioms ← collectAxioms name
    let statement ←
      match ci with
      | .thmInfo _ => liftTermElabM do pure (← ppExpr ci.type).pretty
      | _ => pure ""
    rows := rows.push <| Json.mkObj [
      ("name", toJson (toString name)),
      ("module", toJson (toString modName)),
      ("kind", toJson (ConjecturaAudit.kindOf ci)),
      ("unsafe", toJson ci.isUnsafe),
      ("partial", toJson ci.isPartial),
      ("axioms", toJson (axioms.map toString)),
      ("statement", toJson statement),
      ("type_hash", toJson (toString ci.type.hash))]
  IO.println "CONJECTURA_AUDIT_BEGIN"
  IO.println (Json.arr rows).compress
  IO.println "CONJECTURA_AUDIT_END"
