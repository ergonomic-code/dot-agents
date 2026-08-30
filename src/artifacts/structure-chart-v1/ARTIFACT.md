# Structure Chart

Use `structure-chart/v1` to describe and agree on the high-level structure of a proposed solution.

## Content

Show only:
- major solution modules;
- module responsibilities in short labels;
- containment when it clarifies ownership;
- interactions material to the proposed solution;
- conditions or transferred information when they clarify an interaction.

Omit source references, internal representation, exhaustive call flows, and implementation detail that does not affect the high-level design.
Prefer the smallest diagram sufficient for agreement.

## Conventions

- Start with `flowchart LR`.
- Use stable descriptive `snake_case` identifiers.
- Declare modules before interactions.
- Keep related declarations adjacent and order them in the intended reading sequence.
- Use `subgraph` only for meaningful containment.
- Use `-->` for interactions.
- Put a short interaction label on an edge only when an unlabeled edge is ambiguous.
- Do not duplicate Mermaid content in metadata or another file.

See `references/example-structure-chart.mmd` for the expected shape.
