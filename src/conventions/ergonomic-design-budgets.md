# Ergonomic design budgets

Apply these measurable limits together with the task-specific conventions selected by `./code-implementation.md`.

## Tests

- At least 90% of tests must have an average execution time under 50 ms on a modern high-end machine.
- Shared test infrastructure must start in under 10 seconds for the whole suite.

## Data

- Prefer no more than 10 fields per production data type.

## Subprograms

- Keep cognitive complexity at most 4 for subprograms that perform I/O or change observable state and at most 15 for I/O-free pure computations.

## Components

- Keep each component to at most 10 direct component dependencies.
