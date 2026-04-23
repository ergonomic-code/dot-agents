---
name: map-requirements-to-code
description: Map a feature brief or another requirements artifact to the concrete code anchors that already implement it or must change for it. Use when you need a `020-technical-mapping.adoc` artifact with a required two-column table that links domain terms and observable behavior to endpoints, handlers, operations, models, repositories, queries, tables, migrations, config, i18n keys, or future change points in code.
---

# Map Requirements To Code

Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Read `framework_checkout_root/src/conventions/feature-stage-skill.md`.

## Feature-stage bindings

- stage code: `020`
- default feature-dir output path: `<feature-dir>/020-technical-mapping.adoc`
- default source artifact: `<feature-dir>/010-feature-brief.md`
- progress.md checklist item: `Маппинг требований на прод-код`

## Scope

- Map only behavior and terms that matter for implementing, reviewing, or testing the requested change.
- Cover both domain terms and observable behavior statements.
- Prefer the smallest set of mappings that makes the brief traceable into code.
- Prefer production source code over tests, generated docs, or secondary descriptions.
- Do not rewrite the brief.
- Do not design the implementation beyond identifying the nearest concrete change points.

## Workflow

1. If the output artifact already exists, read it before editing.
2. Prefer the main source artifact from the user request.
3. Otherwise use the default source artifact when it resolves.
4. Read the source requirements artifact and extract candidate phrases.
5. Keep only materially distinct terms, actions, inputs, outputs, ordering rules, fallbacks, invariants, storage concepts, and user-visible variants.
6. For each candidate, find the narrowest concrete code anchor or anchor chain that explains it.
7. Read only the code needed to resolve that mapping.
8. Preserve correct existing mappings and rewrite only stale, vague, conflicting, or missing parts.
9. Merge duplicates and drop mappings that add no new traceability.
10. If an output path is resolved, write or update the mapping artifact.

## Mapping Rules

- Map user actions to concrete entry points such as HTTP endpoints, handlers, jobs, commands, or public operations.
- Map request-visible values to concrete params, DTO fields, enum values, or value objects.
- Map domain entities and result items to concrete models, views, records, or table-backed rows.
- Map filtering, ordering, fallback, and side-effect rules to the layer that actually enforces them.
- When one behavior spans several layers, include the shortest useful chain such as `Controller -> Op -> Repo`.
- When the behavior is not implemented yet, map it to the nearest verified future change point and say that the behavior is not in code yet.
- When storage meaning matters, include the concrete repository, query, table, view, migration, or schema anchor.
- When labels or localization matter, include the concrete i18n key and message files if they are part of the behavior.
- Prefer direct evidence.
- If part of the mapping is inferred from naming or structure, say so explicitly.
- Do not invent anchors from name similarity alone.

## Output

- Write the artifact in the configured `artifact_language`.
- Use AsciiDoc.
- Add the document attribute line `:max-width: 95%` before the document title.
- When the artifact is in Russian and the source artifact path is safely renderable relative to the output artifact, use the heading `= Технический маппинг к link:./<source-file-name>[<source-file-name>]`.
- Otherwise use the heading `= Технический маппинг к <source-file-name>`.
- If an output path is resolved, write only the artifact text to that file.
- Otherwise return only the artifact text.
- Always render mappings as a two-column `|===` table.
- Use the header row `| Формулировка в брифе | Техническое соответствие`.
- Render each mapping as one table row.
- Use `a|` cells when a side needs more than one line.
- Keep exact code identifiers in monospace.
- Prefer AsciiDoc clickable relative links such as `link:../../path/to/File.kt[File.kt]` when the output file path is known.
- Mention “точка будущего изменения” when the current code does not implement the requirement yet.
- Keep commentary minimal and local to the mapping entry.

## Stop Conditions

- Stop and report a short issue list when the main source artifact is missing.
- Stop and report a short issue list when the main entry point or anchor set is materially ambiguous.
- Stop and report a short issue list when the requirements conflict and the requested target behavior cannot be mapped coherently.

## Before Finishing

- Check that every kept mapping is backed by code evidence or is explicitly marked as a future change point.
- Check that the output covers the main brief terms and observable behaviors without repeating synonyms.
- Check that each mapping points to the narrowest useful code anchor.
- Check that unresolved ambiguity is reported instead of guessed.
