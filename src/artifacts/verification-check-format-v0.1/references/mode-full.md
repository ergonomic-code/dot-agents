# Full Mode

Use this mode for executable or near-executable checks, reverse-engineered checks, and code generation input.

Output `Feature`, `Rule`, `Example`, `Given`, `When`, `Then`, and `And`.
Each `Rule` has at least one `Example`.
Use `Example` with no name when no materially distinct input or context class name is needed.
If a `Rule` has an unnamed `Example`, that unnamed example must be the only `Example` under that `Rule`.
An optional source reference line may appear immediately under the matching `Example` per `references/source-reference.md`.

Put only outcome-relevant preconditions in `Given`.
Describe setup with concrete domain objects, states, and literals only when they materially affect the example.
Put the action under test in `When`.
Prefer one action in `When`.
Add a second action only for explicit read-after-write or another essential composite flow.
In read-after-write command checks with a public observation operation, put the command in `When` and the observation operation in `And`.
If command-returned data must be checked before observation, use `When`, `Then`, `And`, `Then`: command, command result, observation operation, observed state.
If several observation endpoint calls are required, put each observation action in its own following `And`, with its result in the next `Then`.
Otherwise keep both actions before `Then`.
In other composite flows, put the first action in `When` and each later action in following `And`.
Put only observable results, side effects, rejections, ordering guarantees, and cardinality guarantees in `Then` and `And` lines that continue `Then`.
Do not pair a positive result with the mirrored absence of an alternative result unless that absence is a distinct contract obligation.
Use `And` only to continue the previous step type, except the read-after-write observation `And` after a command-result `Then`.
