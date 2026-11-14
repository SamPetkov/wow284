import Wow284
import Wow284.Induced40.Structural
import Wow284.Induced40.DiagonalizationData
import Wow284.Induced40.Gap
import Wow284.Induced40.SpectralEndpoint
import Wow284.Induced40.Counterexample
import Wow284.Induced38.FiniteCertificates
import Wow284.Induced38.LDLData
import Wow284.Induced38.Gap
import Wow284.Induced38.SpectralBridge
import Wow284.Induced38.Counterexample
import Wow284.DiameterThreeScalar
import Wow284.MooreSecondThreshold
import Wow284.PuncturedMooreThreshold
import Wow284.DiameterThreeMatrix
import Wow284.Induced40X.FiniteCertificates
import Wow284.Induced40X.Counterexample
import Wow284.Induced40Y.FiniteCertificates
import Wow284.Induced40Y.Counterexample
import Wow284.Induced40Z.FiniteCertificates
import Wow284.Induced40Z.Counterexample

/-!
Top-level imports for the WOW-284 extension package.

Files ending in `.lean.template` are deliberately excluded.  They record
remaining generic mechanisms; the explicit 40- and 38-vertex counterexample
certificates are imported above and are not dependent on those templates.

`Wow284.DiameterThreeMatrix` proves the graph-level diameter-three distance
identities (regular and irregular forms).  `Wow284.Induced40X`,
`Wow284.Induced40Y` and `Wow284.Induced40Z` are generated certificates
(`scripts/generate_lean40_hs_extra.py`) for three irregular order-40
counterexamples inside the Hoffman--Singleton graph; `Induced40X` is `X42`
minus the endpoints of an edge.
-/
