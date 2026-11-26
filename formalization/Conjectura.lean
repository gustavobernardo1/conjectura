/-
Root module of the Conjectura formal library.

Every module that is part of the verified library must be imported here; the
verification script audits exactly the declarations reachable from this file
whose module name starts with `Conjectura`.

* `Conjectura.Calibration.*` — known results, used only to exercise the
  verification pipeline. They are not research results of this project.
* `Conjectura.Research.*`    — (none yet) formal statements and proofs attached
  to catalogue problems.
-/
import Conjectura.Calibration.SumOdd
import Conjectura.Calibration.OddPrime
