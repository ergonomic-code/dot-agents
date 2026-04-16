# Structure Chart v1 Rendering Rules

These rules define how to render a `structure-chart/v1` document to Mermaid.

## Core mapping

1. Render each module as a Mermaid node.
2. Render each lambda as a Mermaid node inside the `subgraph` of its owner module.
3. Prefix lambda display labels with `λ `.
4. If a module has children, render it as a Mermaid `subgraph`.
5. Put direct child modules and owned lambdas inside that `subgraph`.
6. Use `title` verbatim when present, including embedded `<br/>`.

## Edge policy

7. Render exactly one arrow per `calls[*]` record.
8. Do not create extra arrows for parameter passing or returned values.
9. Do not create nodes for `forEach`, `map`, or `filter`.
10. Do not render reverse arrows for `out` values unless there is a real reverse call edge in the source document.

## Edge label format

11. Build the label from up to four lines, in this exact order:
   - `if: ...`
   - `loop: ...`
   - `in: ...`
   - `out: ...`
12. Omit any line whose source field is absent or empty.
13. Separate rendered edge-label lines with an empty visual line.
14. Render `loop` as:
   - `loop: <collection>` when only `collection` is present
   - `loop: <collection>, <condition>` when both fields are present
15. Render `in` and `out` as comma-separated lists.
16. Render flow items as:
   - data item: the raw data name, e.g. `recipient`
   - module item: the referenced module id, e.g. `validate_recipient`
   - lambda item: the referenced lambda id, e.g. `build_payload`

## Visual conventions

18. Emit a Mermaid init block that slightly increases node and rank spacing.
19. Remove the background behind edge-label text.
20. Left-align rendered text in nodes and edge labels.
21. Use solid arrows (`-->`) for all call edges.
22. Distinguish lambdas visually with a Mermaid class or styling rule.
23. If a lambda has captures, optionally append `<br/>captures: ...` inside its node label.
24. If a lambda has params, optionally append `<br/>params: ...` inside its node label.
25. Keep node labels short. Prefer ids or titles, not long prose.

## Module ownership and nesting

26. Render a child module inside its parent module `subgraph` only when `parent` is present in the source document.
27. If nested subgraphs become unreadable, flatten only the visual layout; do not change edges or ownership semantics.
28. Never place a lambda outside the visual region of its owner module.
