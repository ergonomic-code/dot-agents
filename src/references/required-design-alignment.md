# Required design alignment

Use this reference when a selected test case may require production or test-side interfaces, boundary data, or configuration before coding.
Apply `../conventions/process/tasks.md`, `../conventions/test-fixture-architecture.md`, `../conventions/test-doubles.md`, `../conventions/code-implementation.md`, and `../conventions/ergonomic-component-structure.md`.

## Evidence before design

Treat an interface as an externally callable source-level contract, not as a requirement to introduce a language-level interface type.
Treat a provisional `Feature` without a SUT reference as proof that the selected case requires its new SUT interface to be designed.
Design only the selected case's required:

- SUT interface;
- test-helper interfaces, including TestApi;
- data types passed through those interfaces;
- configuration contract, including required keys, value types, requiredness or defaults, constraints, and case-required values.

For every such interface or configuration contract:

1. State the selected-case action, setup, or observation it must support.
2. Inspect existing surfaces and their usages that could already support it.
3. Reuse a sufficient existing surface.
4. Add or change a surface only when the inspected alternatives are insufficient without widening their responsibility or leaking an implementation detail.

For every added or changed surface, report the inspected alternatives and their precise insufficiency.
If no surface is missing, record the no-change result instead of inventing one.
Specify exact callable signatures and the shapes of data crossing their boundaries.
Resolve technical and architecture choices from the selected behavior, task artifacts, project conventions, existing surfaces, and their usages.
Do not ask the user to supply a symbol, method, path, signature, or other technical reference merely because it was not decided before case design.
When several viable technical designs remain, select the best-supported one and report the material alternatives and tradeoffs for review.
Stop only when the exact interface depends on unresolved observable product behavior, conflicts with approved artifacts, or cannot be selected without widening the approved scope.
Do not design a surface for a later case or easier test setup alone.
Do not design internal decomposition, collaborators, persistence queries, algorithms, infrastructure, or wiring beyond what is necessary to define the required interfaces.
Use component and call-structure diagrams only when they are necessary to express those interfaces.

## Artifact update

Keep the solution brief at overall solution direction.
When the selected case has a provisional `Feature`, append the exact evidence-backed SUT reference after designing its interface.
Do not change the human-readable verified object, behavior, or scope while materializing the reference.
Update the current implementation-design artifact according to the ownership and optional section order in `../conventions/process/tasks.md`.
Place each required design change under its owning implementation level and omit empty sections.
Treat the selected case as scope evidence only; do not name or narrate the case or increment in the artifact.
Do not migrate existing task content or restate framework rules merely to demonstrate compliance.

## Output

Return one decision for every examined interface or configuration contract:

- `reuse` with the exact existing symbol or configuration;
- `add` or `change` with the exact contract, evidence-backed gap, and owning artifact section;
- `no-change` when the case needs no surface in that category.

Do not return `required-design-aligned` while the selected case still has a provisional `Feature`.
