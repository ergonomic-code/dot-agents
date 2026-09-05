# Ergonomic behavior structure projection

## Terminology

- `input` — behavior code that loads data into program memory.
- `transformation` — behavior code that transforms data or makes decisions without performing I/O.
- `output` — behavior code that modifies external state.
- `orchestration` — behavior code that routes data through input, transformation, and output steps.

## Rules

- Decompose behavior into operations, DOPs, resources, and ports with explicit responsibilities.
- Keep each subprogram on one abstraction level.
