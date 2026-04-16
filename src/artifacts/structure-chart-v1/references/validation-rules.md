# Structure Chart v1 Validation Rules

These rules are imperative semantic validations that go beyond JSON Schema.

## Identifier and reference integrity

1. Treat `modules[*].id` and `lambdas[*].id` as a single global namespace.
2. Reject the document if any identifier is duplicated across modules and lambdas.
3. Reject the document if `modules[*].parent` does not reference an existing module.
4. Reject the document if `lambdas[*].owner` does not reference an existing module.
5. Reject the document if `calls[*].from` or `calls[*].to` does not reference an existing module or lambda.
6. Reject the document if any `in` or `out` item references a non-existent module or lambda.

## Hierarchy integrity

7. Build the module tree from `modules[*].parent`.
8. Use `modules[*].parent` only when the child function is syntactically nested inside the parent function in source code.
9. Do not use `parent` for methods that merely call each other, share a class, or live in the same file.
10. Reject the document if a lambda is referenced as a `parent` of a module.

## Source reference integrity

11. Prefer `code.path` and `code.line` on every module and lambda.
12. Use repository-relative paths in `code.path`.
13. Use 1-based source lines in `code.line`.

## Edge normalization

14. Treat each `calls[*]` record as the single merged edge for one ordered pair `(from, to)`.
15. Reject the document if more than one call record has the same `(from, to)` pair.
16. Do not represent `forEach`, `map`, or `filter` as modules, lambdas, or intermediary call targets.
17. Model those constructs as ordinary call edges with `loop.collection` and optional `loop.condition`.

## Edge semantics

18. Allow `if` only on a call edge, never as a standalone node.
19. Allow `loop` only on a call edge, never as a standalone node.
20. Treat `in` as the set of values supplied to the target during the call represented by that edge.
21. Treat `out` as the set of values produced by the target during that same call.
22. If a module or lambda is passed as a parameter, represent it in `in`, not as a separate node or helper edge.
23. If a module or lambda is returned as a result, represent it in `out`, not as a reverse edge.
24. If a passed or returned callable is later invoked, model that invocation as a normal call edge to the callable itself.

## Recommended quality checks

25. Warn if a module has neither incoming nor outgoing edges and is not a root module.
26. Warn if a lambda has no incoming call edges.
27. Warn if a call edge has no `in`, no `out`, no `if`, and no `loop`; this is legal but often underspecified.
28. Warn if a flow item name is repeated verbatim within the same `in` or `out` list.
29. Warn if a call edge points from a child module to its ancestor and the intent is not documented in `notes`.
30. Warn if a module or lambda has no `code.path` or `code.line`.

## Rendering-oriented checks

31. Preserve declaration order for `modules`, `lambdas`, and `calls` when deterministic rendering matters.
32. Prefer stable identifiers and stable list ordering to keep diffs small.
33. Prefer concise `if` and `loop.condition` expressions; they should be labels, not full executable code.
34. Prefer module `title` values copied verbatim from code names.
35. For methods and extension functions, prefer `title` in the form `<ClassName>.<br/>methodName`.
