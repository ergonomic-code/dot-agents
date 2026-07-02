# DB schema migrations

## Scope

- Apply this convention when changing or adding production database schema migrations for tables that may already contain rows.

## Migration file choice

- Before adding a new migration, inspect the latest adjacent migrations for the same schema object or active task.
- If an existing migration belongs to the current unfinished task and is not yet part of any deployed or externally applied schema history, amend that migration instead of adding a later migration.
- If deployment or external application status is unclear, ask before creating or amending the migration.

## Required columns

- When adding a required column to an existing table, add it nullable, backfill all existing rows from current persisted data or explicit domain meaning, then add the `NOT NULL` constraint.
- Do not use a database `DEFAULT` to populate historical rows unless the default is also the intended permanent insert behavior.
- If future inserts need a database-level default, add or keep the `DEFAULT` only when it is part of the storage contract.
- After adding a production migration, target the migrated schema in production persistence code; add runtime old-schema branches only for explicit mixed-version rollout compatibility.
- If a required value cannot be derived safely for old rows, stop and ask for the migration rule instead of guessing.
