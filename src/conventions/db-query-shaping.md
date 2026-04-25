# Database query shaping

## Scope

- Apply this convention when a read path is backed by a database query or repository call.
- Apply it especially when behavior mentions sorting, filtering, pagination, result limiting, deduplication, or existence checks.
- Pair this convention with `db-read-model-boundaries.md` when the task introduces or changes query-mapped return types, projections, views, or row-mapper targets.

## Rules

- Keep query-expressible result shaping in the query layer.
- Prefer `WHERE`, `ORDER BY`, `LIMIT`, `OFFSET`, aggregates, `DISTINCT`, and existence checks in SQL, query DSL, or repository methods over materializing rows and reshaping them in application code.
- Do not fetch a broader row set only to sort, filter, page, or trim it in application code unless the rule is not practical to express in the query layer.
- Application-layer reshaping is acceptable only for post-query composition, such as adding synthetic items, merging non-database data, or applying rules that cannot reasonably live in the query layer.
- When post-query composition is needed, keep the database part already filtered, ordered, and bounded as far as the database can express it.
