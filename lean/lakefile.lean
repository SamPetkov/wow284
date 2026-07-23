import Lake

open Lake DSL

package Wow284 where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.31.0"

@[default_target]
lean_lib Wow284

/-- Opt-in build target for the induced-graph extension.  Keeping a separate
target prevents incomplete endpoint wrappers from enlarging the public
formal-verification claim while still making every staged module compile in
CI. -/
lean_lib Wow284Extension where
  roots := #[`Wow284Extended]
