# Database conditional writes

## Scope

- Apply this convention when the correctness of a database-backed mutation depends on evaluating a precondition against current database state.
- Treat insert-if-absent, first-writer-wins, deduplication, compare-and-set, and conditional update or delete as conditional writes.

## Rules

- By default, enforce the condition and mutation atomically in the database with constraints, conditional write primitives, or both.
- Do not enforce correctness with an application-level read, check, and write sequence because concurrent operations may change the state between calls.
- A preceding read may provide inputs, but it must not be the sole enforcement of the write precondition.
- When one atomic statement cannot express the transition, use a transaction with locking or isolation that preserves the invariant and state why it is necessary.
