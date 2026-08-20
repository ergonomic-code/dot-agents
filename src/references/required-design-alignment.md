# Required design alignment

Use this reference when a selected test case may require production or test-side design changes before coding.
Apply `../conventions/process/tasks.md`, `../conventions/test-fixture-architecture.md`, `../conventions/test-doubles.md`, `../conventions/code-implementation.md`, and `../conventions/ergonomic-component-structure.md`.

## Evidence before design

For every public contract, production type or signature, test API, fixture, preset, or configuration surface that the case appears to need:

1. State the selected-case action, setup, or observation it must support.
2. Inspect existing surfaces and their usages that could already support it.
3. Reuse a sufficient existing surface.
4. Add or change a surface only when the inspected alternatives are insufficient without widening their responsibility or leaking an implementation detail.

For every added or changed surface, report the inspected alternatives and their precise insufficiency.
If no surface is missing, record the no-change result instead of inventing one.
Do not design a surface for a later case, a production-scale fixture, or easier test setup alone.

## Artifact update

Keep the solution brief at overall solution direction.
Put selected-case implementation details in the current target design artifact according to the ownership rules in `../conventions/process/tasks.md`.
When creating that artifact, write only design details introduced by the selected case.
Do not migrate existing task content, narrate the increment, or restate framework rules merely to demonstrate compliance.

## Output

Return one decision for every examined surface:

- `reuse` with the existing symbol or configuration;
- `add` or `change` with the evidence-backed gap and owning artifact;
- `no-change` when the case needs no surface in that category.
