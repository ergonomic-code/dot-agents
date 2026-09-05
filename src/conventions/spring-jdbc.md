---
keywords:
  - spring
  - jdbc
---

# Spring JDBC

- Unless project context overrides, use `org.springframework.jdbc.core.simple.JdbcClient` for new or changed Spring JDBC SQL access.
- Do not migrate existing working data access solely to satisfy the `JdbcClient` default.
- For Spring JDBC row mapping, use `jdbcAggregateTemplate.getRowMapper(Target::class.java)` before `DataClassRowMapper`, and use manual `RowMapper` only when neither fits.
