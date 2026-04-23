---
name: map-requirements-to-code
description: Map a feature brief or another requirements artifact to the concrete code anchors that already implement it or must change for it. Use when you need a `020-technical-mapping.adoc` artifact with a required two-column table that links domain terms and observable behavior to endpoints, handlers, operations, models, repositories, queries, tables, migrations, config, i18n keys, or future change points in code.
---

# Map Requirements To Code

Read `framework_checkout_root/src/conventions/feature-workdir.md`.

## Resolve Paths

- If the user gave an explicit output path, use it.
- Otherwise resolve the active feature directory via `feature-workdir.md`.
- If the user gave a requirements file path inside a feature directory, use that feature directory.
- If no target feature directory is resolved and no explicit output path is given, stop and ask for the feature directory or output path.
- Prefer the main source artifact from the user request.
- Otherwise prefer `<feature-dir>/010-feature-brief.md`.
- Default output path to `<feature-dir>/020-technical-mapping.adoc`.

## Scope

- Map only behavior and terms that matter for implementing, reviewing, or testing the requested change.
- Cover both domain terms and observable behavior statements.
- Prefer the smallest set of mappings that makes the brief traceable into code.
- Prefer source code over generated docs or secondary descriptions.
- Do not rewrite the brief.
- Do not design the implementation beyond identifying the nearest concrete change points.

## Workflow

1. If the output artifact already exists, read it before editing.
2. Read the source requirements artifact and extract candidate phrases.
3. Keep only materially distinct terms, actions, inputs, outputs, ordering rules, fallbacks, invariants, storage concepts, and user-visible variants.
4. For each candidate, find the narrowest concrete code anchor or anchor chain that explains it.
5. Read only the code needed to resolve that mapping.
6. Preserve correct existing mappings and rewrite only stale, vague, conflicting, or missing parts.
7. Merge duplicates and drop mappings that add no new traceability.
8. Write or update the mapping artifact.
9. If the active feature directory is resolved and `<feature-dir>/progress.md` exists, change `- [ ] Привязка требований к коду и анализ текущего кода` to `- [x] Привязка требований к коду и анализ текущего кода` when that checklist item is present.

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
- Use the heading `= Технический маппинг к link:./<source-file-name>[<source-file-name>]` when the artifact is in Russian.
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
- Check that `progress.md` is updated only after the mapping artifact was successfully written.
