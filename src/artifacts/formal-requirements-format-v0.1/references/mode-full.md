# Full Mode

Use this mode for executable or near-executable cases, reverse-engineered cases, and code generation input.

Output `Feature`, `Rule`, `Scenario`, `Given`, `When`, `Then`, and `And`.
An optional source reference line may appear immediately under `Scenario` per `references/source-reference.md`.

Put only outcome-relevant preconditions in `Given`.
Describe setup with concrete domain objects, states, and literals only when they materially affect the branch.
Put the action under test in `When`.
Prefer one action in `When`.
Add a second action only for explicit read-after-write or another essential composite flow.
In a composite flow, put the first action in `When` and each later action in following `And`.
Put only observable results, side effects, rejections, ordering guarantees, and cardinality guarantees in `Then` and following `And`.
Use `And` only to continue the previous step type.
