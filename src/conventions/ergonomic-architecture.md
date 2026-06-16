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

## How to use in artifacts

- In technical feature briefs, use this summary to translate architecture goals into explicit constraints and acceptance criteria.
- Cite only the constraints that are relevant to the requested change.
- Do not restate the whole architecture.
- If the source material names a more specific EA target, combine that target with the applicable rules from this summary.
