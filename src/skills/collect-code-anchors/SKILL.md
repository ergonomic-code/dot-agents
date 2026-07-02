---
name: collect-code-anchors
description: Collect concrete code anchors for target or related behavior. Use when you need an auxiliary list of verified endpoints, handlers, operations, models, repositories, queries, tables, migrations, config, i18n keys, or other code locations connected to a requested behavior.
---

# Collect Requirement Code Anchors

## Task-directory behavior

- default source artifact: `<task-dir>/010-task-brief.md`
- default output artifact: `<task-dir>/020-code-anchors.md`
- Use an explicit output path when provided.
- Otherwise, write the default output artifact to `<task-dir>/020-code-anchors.md` when a task directory resolves .
- Return the artifact inline only when no output path or task directory resolves.

## Scope

- Collect only anchors that help implement, review, or test the target behavior or tightly related existing behavior.
- Do not map every requirement phrase or domain term to code.
- Do not produce a two-column requirements-to-code table.
- Prefer production source code over tests, generated docs, or secondary descriptions.
- Do not design the implementation beyond identifying verified anchors.

## Workflow

1. Identify the target behavior from the prompt and, when useful, from the source artifact named in the prompt or from the default source artifact.
2. Resolve the output path from the prompt or from the default output artifact.
3. If the output artifact already exists, read it before editing.
4. Extract concrete code starting points from the prompt, such as source/test paths, endpoints, classes, methods, operations, DTOs, table names, config keys, i18n keys, logs, or exact code search strings.
5. Do not count task ids, issue ids, task directories, source artifacts, briefs, todo files, requirements text, or docs as code starting points.
6. If the prompt has no concrete code starting points, ask the user for one or more and stop.
7. Search from the provided starting points and read only code needed to verify anchors.
8. Collect the narrowest concrete anchors where target or related behavior is exposed, enforced, stored, configured, localized, or scheduled.
9. Preserve correct existing anchors and rewrite only stale, vague, conflicting, or missing parts.
10. Merge duplicates and drop anchors that add no new behavioral location.
11. If an output path is resolved, write or update the anchor-list artifact.

## Anchor Rules

- Prefer direct code evidence.
- Include short anchor chains only when one location is misleading without its caller, callee, query, model, or table.
- Mark each anchor as `target` or `related`.
- Say what behavior the anchor proves or connects to.
- Say so explicitly when an anchor is inferred from naming or structure.
- Do not invent anchors from name similarity alone.

## Output

- Write the artifact in the configured `artifact_language`.
- Use Markdown.
- When the artifact is in Russian and the source artifact path is safely renderable relative to the output artifact, use the heading `# Технические якоря к [<source-file-name>](./<source-file-name>)`.
- Otherwise use the heading `# Технические якоря к <source-file-name>`.
- Write or return only the artifact text.
- Render anchors as a compact bullet list grouped by subsystem, layer, or behavior when grouping helps scanning.
- Keep exact code identifiers in monospace.
- Prefer Markdown clickable relative links such as `[File.kt](../../path/to/File.kt):12` when the output file path is known.
- Keep commentary minimal and local to the anchor entry.

## Stop Conditions

- Stop and ask for concrete code starting points when the prompt has none.
- Stop and report a short issue list when a user-requested source artifact is missing.
- Stop and report a short issue list when the target behavior or related-behavior boundary is materially ambiguous.
- Stop and report attempted searches when the provided starting points do not resolve to verified anchors.

## Before Finishing

- Check that every kept anchor has code evidence or is explicitly marked as inferred.
- Check that every kept anchor has a location, behavior connection, and `target` or `related` status.
- Check that unresolved ambiguity is reported instead of guessed.
