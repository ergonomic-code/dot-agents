# DB schema migrations

## Scope

- Apply this convention when changing or adding production database schema migrations for tables that may already contain rows.

## Required columns

- When adding a required column to an existing table, add it nullable, backfill all existing rows from current persisted data or explicit domain meaning, then add the `NOT NULL` constraint.
- Do not use a database `DEFAULT` to populate historical rows unless the default is also the intended permanent insert behavior.
- If future inserts need a database-level default, add or keep the `DEFAULT` only when it is part of the storage contract.
- If a required value cannot be derived safely for old rows, stop and ask for the migration rule instead of guessing.
