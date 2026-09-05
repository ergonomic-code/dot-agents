# Semantic value types

## Rules

- Prefer types that make the value meaning, unit, range, and nullability obvious.
- Use domain value types, standard semantic types such as `Instant`, `LocalDate`, `UUID`, or enums, or existing project types when they fit.
- Keep transport and storage primitives at the boundary that requires them.
- Convert primitive wire values in controllers or boundary adapters before passing them to operations.
- Convert semantic values to storage primitives in repositories, SQL binders, row mappers, or persistence adapters when storage requires primitives.
- Avoid integer timestamps in application code.
- If an integer timestamp remains in a public or storage contract, make its unit explicit in the name or documentation.
