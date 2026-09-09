# Structure Chart

Use `structure-chart/v1` to represent the static referential structure of a modular program in the notation of Structured Design.
A structure chart shows system pieces, references between them, and optional interface or procedural annotations.
It does not directly model control flow, data flow, or execution time.
The caller selects the represented root, modules, and decomposition depth from the request and applicable context.

## Elements

### System pieces

- A `module` represents a named method or another program unit whose implementation is or will be lexically contiguous and referenceable as one piece.
- A `predefined module` is a pre-existing or externally supplied module.

### Connections

- A `call` points from a module containing a normal subordinating reference to the referenced module.
- An `asynchronous call` activates the referenced module asynchronously or in parallel.

### Annotations

- A `data couple` identifies data passed to or returned from a referenced module.
- A `control couple` identifies a flag or other information whose purpose is to affect the recipient's control.
- An `iteration` marks references used from within a loop.
- A `decision` marks alternative or conditional references.
- A `lexical inclusion` states that one module is defined wholly inside another.
- A `comment` adds explanatory information without introducing another system piece.

## Mermaid Rendering

- Start with `flowchart TD` so subordinating connections normally place superordinate modules above their subordinates.
- Use stable descriptive `snake_case` identifiers and declare every node before its connections.
- Render a module as `module_id["Module name"]`.
- Render a predefined module as `module_id[["Module name"]]`.
- Render a call as `caller --> callee`.
- Render an asynchronous call as `caller -. "async" .-> target`.
- Add couples and procedural annotations to the applicable connection label as semicolon-separated `<kind>: <value>` clauses.
- Interpret `to` and `from` in annotation kinds relative to the referenced target module.
- Use annotation kinds `data-to`, `data-from`, `control-to`, `control-from`, `repeat`, `when`, and `once`.
- Render lexical inclusion as `owner -.->|"lexically-contains"| nested`.
- Render a comment as `comment_id["Note: <text>"]:::comment` with `module_id -.- comment_id`, and add `classDef comment fill:none,stroke-dasharray:3 3` once.
- Keep a connection unlabeled when no connection kind, couple, or procedural annotation is represented.
- Put parameter-table references in a connection label as `parameters: P<n>` and place the referenced table outside the Mermaid block.
- Use connectors only to split an otherwise unreadable chart, and render each end as `connector_id(("connector: <name>"))` with the same displayed name.

See `references/example-structure-chart.mmd` for the expected Mermaid shape.
