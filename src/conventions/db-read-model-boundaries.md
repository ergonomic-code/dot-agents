# DB read-model boundaries

## Scope

- Apply this convention when a task changes a database-backed read, a repository/query return type, a `rowMapperClass`, or a class mapped directly from SQL/JDBC/SDJ results.

## Rules

- Keep query-mapped read models, views, projections, and row DTOs as plain carriers of selected fields and query-derived values.
- In Spring JDBC code, follow `spring.md` row-mapper priority before adding or keeping a dedicated row mapper.
- Do not add interface inheritance, wrappers, or marker supertypes to a DB-mapped class just to reuse helper behavior from another layer or model family.
- Before making a DB-mapped class implement or extend an existing type family, inspect project conversion and mapping registrations for that family, including `@ReadingConverter`, `GenericConverter`, `JdbcCustomConversions`, `CustomConversions`, and similar hooks.
- If the candidate supertype or wrapper participates in persistence conversion or mapping semantics, do not use it on the DB-mapped class unless that behavior is explicitly required by the query contract.
- Prefer derived properties, top-level or extension helpers, explicit SQL aliases, and dedicated row mappers over inheriting persistence semantics indirectly.
- Keep query-side type shaping explicit in SQL, projection definitions, or row mappers instead of relying on broad global converters through incidental interface implementation.
