---
name: finding-touched-tables
description: Find database tables and views touched by code referenced from an existing `structure-chart/v1` diagram. Use when the input is a ready structure chart and you need the list of tables that are read or written along the charted execution path, including reads performed through SQL views and, when recoverable, the base tables behind those views.
---

# Finding Touched Tables

Input is an existing `structure-chart/v1` YAML.
Use `../../artifacts/structure-chart-v1` only as the format reference.
Do not rebuild the chart unless the user explicitly asks for it.

## Workflow

1. Read the chart and collect all code anchors from `modules[*].code`, `lambdas[*].code`, and the allowed edges from `calls[*]`.
2. Inspect only the code needed to resolve persistence access reachable along those charted calls.
3. Track concrete reads and writes.
4. Return a deduplicated list of touched database objects with evidence.

## What Counts As A Touched Object

Treat these as evidence of table or view access:
- hardcoded SQL;
- jOOQ tables, views, DSL queries, and generated records;
- repository or DAO methods whose target table or view is explicit in code;
- ORM entity mappings when they clearly resolve to a concrete table or view;
- database views referenced by queries, repositories, or mappings.

Do not report guessed tables from naming alone.
If the code suggests persistence access but the concrete object cannot be resolved, report the uncertainty explicitly instead of inventing a table name.

## Read And Write Rules

Mark an object as `read` when the code performs `select`, `exists`, `count`, joins, subqueries, or other lookup-style access.
Mark an object as `write` when the code performs `insert`, `update`, `delete`, `merge`, upsert-like operations, or other state-changing access.
If one path both reads and writes the same object, report both modes.

## Views

If the code reads from a view, include the view itself in the output.
If the underlying base tables are recoverable from repository code, SQL text, jOOQ metadata, or a database view definition available in the repository, include those base tables too.
Mark such tables as `read via view <view-name>`.
If the view is known but its base tables are not recoverable from available evidence, keep the view and say that the expansion is unresolved.

## Scope Rules

Stay inside the execution path represented by the diagram.
Follow only the nodes and `calls[*]` present in the chart.
Use non-chart code only to resolve the concrete persistence object behind a charted node or charted call.
Exclude tests, fixtures, and dead code unless the user explicitly asks for them.
Read migrations only when they are the only available evidence for the definition of a referenced view.
Prefer direct evidence over framework conventions.

## Output

Return concise Markdown.
Group by object and list:
- object name;
- kind: `table` or `view` when known;
- access: `read`, `write`, or both;
- evidence: repository-relative path and line;
- note when the object is reached through a view or when part of the chain is inferred.

When nothing concrete is found, say so and list the unresolved persistence touch points you checked.
