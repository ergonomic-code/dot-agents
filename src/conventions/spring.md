# Spring

## Scope

- Apply this convention in Spring projects.

## Defaults

- Unless project context overrides, use `org.springframework.jdbc.core.simple.JdbcClient` for new or changed Spring JDBC SQL access.
- Do not migrate existing working data access solely to satisfy the `JdbcClient` default.
- For Spring JDBC row mapping, use `jdbcAggregateTemplate.getRowMapper(Target::class.java)` before `DataClassRowMapper`, and use manual `RowMapper` only when neither fits.
- Use constructor injection for Spring-managed dependencies; use field injection only when constructor injection is unavailable or incompatible with framework or test lifecycle.
- Do not introduce managed beans if the component does not need other managed beans as dependencies.
  Use plain Kotlin singleton objects in this case.

## Triggers

- If the task adds or changes Spring HTTP JSON API error handling or error body contracts, load `../conventions/spring-http-json-api.md` and follow it.
- If the request changes externally visible HTTP endpoint behavior and the planned write set still includes a Spring MVC handler target (`*Controller.kt`, `@RestController` / `@Controller`, mapping handler methods, or a related `@ExceptionHandler`), load `.agents/SPRING-MVC-HANDLER-EDIT.md` and follow it.
