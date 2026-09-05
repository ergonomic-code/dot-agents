# Database context

Load only the entries matching the requested or planned database work:

- production schema migrations or persistence changes requiring them: `../conventions/db-schema-migrations.md`;
- database transaction boundaries or database-backed mutations: `../conventions/transaction-boundaries.md`;
- database-backed reads, ordering, filtering, pagination, limiting, deduplication, or existence checks: `../conventions/db-query-shaping.md`;
- query-mapped types, views, projections, row DTOs, or row mappers: `../conventions/db-read-model-boundaries.md`;
- database-backed mutations whose correctness depends on a current-state precondition: `../conventions/db-conditional-writes.md`;
- persistence-backed classes, constructors, factories, repository mappings, serializers, or adapters: `../conventions/persistence-models.md`.
