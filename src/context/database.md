# Database context

Load only the entries matching the requested or planned database work:

- production schema migrations or persistence changes requiring them: `../conventions/database/db-schema-migrations.md`;
- database transaction boundaries or database-backed mutations: `../conventions/database/transaction-boundaries.md`;
- database-backed reads, ordering, filtering, pagination, limiting, deduplication, or existence checks: `../conventions/database/db-query-shaping.md`;
- query-mapped types, views, projections, row DTOs, or row mappers: `../conventions/database/db-read-model-boundaries.md`;
- database-backed mutations whose correctness depends on a current-state precondition: `../conventions/database/db-conditional-writes.md`.

Before finalizing applicable database changes, apply `../conventions/database/checklist.md`.
