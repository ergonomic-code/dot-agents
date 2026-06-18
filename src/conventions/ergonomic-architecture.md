# Ergonomic Architecture summary

Use this file when a task explicitly depends on Ergonomic Architecture or on architecture-shaping constraints from an EA source.
Use it as a compact framework-owned summary for routing, brief writing, and architecture decisions.
Do not treat it as a replacement for projection-specific conventions or narrower conventions such as `operations-design.md`.

## When to load

- Load this file when the request or referenced material mentions Ergonomic Architecture, `EA`, `EP`, aggregates, resources, operations, DOPs, target architecture, architecture refactoring, or acceptance by tech lead through code shape.
- Load this file when a technical feature brief, blueprint, or refactoring task must align with a named architecture source such as `ergo-arch.adoc`.
- Also load `./ergonomic-data-structure.md` when the task concerns domain data shape, entities, value objects, aggregates, references, or persistence boundaries.
- Also load `./ergonomic-component-structure.md` when the task concerns ports, operations, DOPs, resources, component dependencies, or effect graph shape.
- Also load `./ergonomic-behavior-structure.md` when the task concerns input, transformation, output, orchestration, method structure, or behavior decomposition.

## How to use in artifacts

- In technical feature briefs, use this summary to translate architecture goals into explicit constraints and acceptance criteria.
- Cite only the constraints that are relevant to the requested change.
- Do not restate the whole architecture.
- If the source material names a more specific EA target, combine that target with the applicable rules from this summary.
- Preserve EA vocabulary from the named EA source and the projection-specific conventions instead of introducing adjacent local synonyms or alternative taxonomy.
