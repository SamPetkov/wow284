import Lake

open Lake DSL

package Wow284 where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.31.0"

@[default_target]
lean_lib Wow284

/-- Opt-in build target for the committed induced-graph extension. -/
lean_lib Wow284Extension where
  roots := #[`Wow284Extended]

/-- Deterministically generated order-39 and order-42 counterexample
certificates. The root and its imported modules are created before this target
is built in CI. -/
lean_lib Wow284Generated3942 where
  roots := #[`Wow284Generated3942]
