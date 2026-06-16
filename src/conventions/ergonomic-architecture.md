# Ergonomic Architecture summary

Use this file when a task explicitly depends on Ergonomic Architecture or on architecture-shaping constraints from an EA source.
Use it as a compact framework-owned summary for routing, brief writing, and architecture decisions.
Do not treat it as a replacement for narrower conventions such as `operations-design.md`.

## When to load

- Load this file when the request or referenced material mentions Ergonomic Architecture, `EA`, `EP`, aggregates, resources, operations, DOPs, target architecture, architecture refactoring, or acceptance by tech lead through code shape.
- Load this file when a technical feature brief, blueprint, or refactoring task must align with a named architecture source such as `ergo-arch.adoc`.

## Data structure projection

- Model the domain with entities, value objects, and aggregates.
- Entities and value objects should be effectively immutable.
- Prefer a small number of meaningful fields.
- Aggregates are the persistence unit and should be loaded and saved as a whole.
- References inside an aggregate may be direct.
- References between aggregates should go by identifier.
- Do not create cycles between aggregates.
- Do not model many-to-many links directly in the data model.
- Split oversized entities into separate aggregates or aspect entities when that improves boundaries without losing meaning.

## State structure projection

- Expose system behavior through explicit operations over explicit state elements.
- Keep aggregate and resource responsibilities bounded and readable.
- Separate independent responsibilities into distinct aggregates or resources instead of growing one universal holder.

## Behavior structure projection

- Decompose behavior into operations, DOPs, resources, and ports with explicit responsibilities.
- An operation should serve one use case and orchestrate a small multi-step workflow.
- Prefer explicit behavior layering: operations on top, optional domain operations below them, resources below operations, and optional infrastructure resources below resources.
- For each behavior layer except DOPs, forbid horizontal dependencies between peers on the same layer.
- Inject the resources an operation uses directly into that operation.
- Keep domain operations, when they exist, between orchestration-level operations and resources instead of mixing those responsibilities.
- Keep infrastructure concerns behind infrastructure resources instead of leaking them into domain-facing resources or operations.
- Do not hide core dependencies behind incidental facades when direct operation-to-resource wiring is the intended shape.
- Keep each subprogram on one abstraction level.

## Terminology

 Use these EA terms by default when the named source does not define another vocabulary.

### Data structure projection terminology

- `entities` — domain objects with identity.
- `value objects` — immutable domain objects without identity that are compared by value.
- `aggregates` — persistence and loading units of the domain model that are loaded and saved as a whole.
- `aspect entities` — technical or design-driven entity slices that reuse the identity of another entity instead of defining a new one.
- `anchor entities` — the ordinary entities whose identity is reused by aspect entities.

### State structure projection terminology

- `ports` — entry points that receive external signals and delegate to one operation or one resource method.
- `operations` — top-level scenario components that orchestrate one use case over resources.
- `domain operations` (`DOPs`) — reusable lower-level effect sequences that are shared by multiple operations.
- `resources` — stateful or externally connected runtime components that expose explicit effects over aggregates, integrations, or other state.
- `primitive resources` — resources that are internal implementation parts of a higher-level resource.
- `infrastructure resources` — project-owned infrastructure-facing resources reused as implementation parts of multiple domain-facing resources.

### Behavior structure projection terminology

- `input` — behavior code that loads data into program memory.
- `transformation` — behavior code that transforms data or makes decisions without performing I/O.
- `output` — behavior code that modifies external state.
- `orchestration` — behavior code that routes data through input, transformation, and output steps.

## How to use in artifacts

- In technical feature briefs, use this summary to translate architecture goals into explicit constraints and acceptance criteria.
- Cite only the constraints that are relevant to the requested change.
- Do not restate the whole architecture.
- If the source material names a more specific EA target, combine that target with the applicable rules from this summary.
- Preserve component vocabulary from the named EA source and this summary instead of introducing adjacent local synonyms or alternative taxonomy.
