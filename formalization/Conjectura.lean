/-
Root module of the Conjectura formal library.

Every module that is part of the verified library must be imported here; the
verification script audits exactly the declarations reachable from this file
whose module name starts with `Conjectura`.

* `Conjectura.Calibration.*` — known results, used only to exercise the
  verification pipeline. They are not research results of this project.
* `Conjectura.Research.*`    — formal statements and proofs attached to
  catalogue problems. A theorem here is what its own statement says; whether
  it matches a written statement is recorded in `registry.json`.
-/
import Conjectura.Calibration.SumOdd
import Conjectura.Calibration.OddPrime
import Conjectura.Research.CollinsShorPeak.LogConcavePeak
import Conjectura.Research.CollinsShorPeak.ExtremalReduction
import Conjectura.Research.CollinsShorPeak.VertexPrinciple
import Conjectura.Research.CollinsShorPeak.HalfGammaCone
import Conjectura.Research.CollinsShorPeak.WienerCone
import Conjectura.Research.CollinsShorPeak.LowerBoundCone
import Conjectura.Research.CollinsShorPeak.UpperBoundPeak
