# Full Mode

Use this mode for executable or near-executable checks, reverse-engineered checks, and code generation input.

Output `SUT`, `Check`, optional `Variant`, `Given`, `When`, `Then`, and `And`.
An optional source reference line may appear immediately under `Check` or after its `Variant` per `references/source-reference.md`.

Put only outcome-relevant preconditions in `Given`.
Describe setup with concrete domain objects, states, and literals only when they materially affect the check.
Put the action under test in `When`.
Prefer one action in `When`.
Add a second action only for explicit read-after-write or another essential composite flow.
In read-after-write command checks with a public observation operation, put the command in `When` and the observation operation in `And`.
If command-returned data must be checked before observation, use `When`, `Then`, `And`, `Then`: command, command result, observation operation, observed state.
Otherwise keep both actions before `Then`.
In other composite flows, put the first action in `When` and each later action in following `And`.
Put only observable results, side effects, rejections, ordering guarantees, and cardinality guarantees in `Then` and `And` lines that continue `Then`.
Do not pair a positive result with the mirrored absence of an alternative result unless that absence is a distinct contract obligation.
Use `And` only to continue the previous step type, except the read-after-write observation `And` after a command-result `Then`.
