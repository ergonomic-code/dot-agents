---
name: design-feature-test-cases
description: Design formal requirement cases for a new feature from a feature brief, current implementation summary, optional current relevant cases, and optional API IR. Use when you need to derive the target case set for the feature first, then decide which old cases stay unchanged, which must be removed, which must be updated, and which new cases must be added.
---

# Design Feature Test Cases

Read `../write-grekhin-test-case/SKILL.md`.
Read the format reference at `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.

## Inputs

Required:
- feature brief.

Recommended:
- current implementation summary;
- API IR or another explicit API change description.

Optional:
- current relevant test cases.
- optional source-location metadata for current relevant test cases.
  - include it only when you know the source commit, source file path, and source test method line.
- optional artifact output path.
  - use it when the artifact will be written to a concrete Markdown or AsciiDoc file.

If current test cases are absent, still design the target case set and return empty `removed`, `changed`, and `unchanged` sections.
If API IR is absent, derive the target set from the brief and implementation summary only.

## Core Rule

Design the target test case set for the new feature first.
Treat old cases only as reusable material and migration input, not as the source of truth.

## Workflow

1. Read the feature brief and extract the target behavior.
   - Prefer explicit acceptance scenarios, business rules, invariants, compatibility constraints, and error conditions.
   - Separate independent behavior properties into separate `Rule`s.
2. Read the implementation summary and API IR.
   - Use them to refine the contract, identify touched surfaces, and detect migration-sensitive behavior.
   - Prefer the feature brief and explicit API rules over narrative implementation details when they conflict.
3. Design the target case set from scratch.
   - Cover only behavior that is actually implied by the inputs.
   - Add positive, negative, boundary, fallback, and compatibility cases only when the inputs justify them.
   - Merge duplicates and keep one `Scenario` per materially distinct branch.
   - Prefer abstract contract wording over literal sample data unless exact values are behaviorally required.
4. Normalize current relevant cases if they exist.
   - If they are not already in artifact form, recover stable `Feature` / `Rule` / `Scenario` anchors without changing meaning.
   - If they are already in artifact form, treat their wording as canonical and keep it verbatim when reusing or citing them.
   - Use the recovered anchor as the source reference in `changed` cases.
5. Compare current cases against the target case set.
   - `unchanged`: one current case already matches one target case with no behavioral edits.
   - `changed`: one current case maps to one target case, but preconditions, action, or assertions must change.
   - `removed`: one current case no longer belongs to the target set.
   - preserve the old `Rule` when the obligation itself stays valid and only the scenario needs to change.
   - for `changed` cases, minimize the difference between the new `Rule` name and the source `Rule` name; rename it only when the old wording becomes incorrect.
6. Mark as `added` every target case that has no reusable current source case.
7. Render the four output lists.

## Classification Rules

- Put every current case into exactly one bucket: `removed`, `changed`, or `unchanged`.
- Put every target case into exactly one bucket: `added`, `changed`, or `unchanged`.
- Use `changed`, not `removed` + `added`, only when the old and new cases clearly test the same behavior lineage.
- Use `removed` when the old case targets behavior that is obsolete, contradicted, overspecified, or no longer worth keeping as a separate guarantee.
- Use `unchanged` only when the old case can be kept as-is.
- Do not keep a case in `unchanged` if its assertions, inputs, or expectation wording need behavioral edits.
- Do not invent new obligations from implementation hints alone unless the brief or API contract makes them test-worthy.

## Output

Return exactly four sections in this order:
- `Удаляемые тест-кейсы`
- `Изменяемые тест-кейсы`
- `Добавляемые тест-кейсы`
- `Актуальные тест-кейсы без изменений`

Write human-readable text in the configured artifact language.
Base the case bodies on `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Follow `../write-grekhin-test-case/SKILL.md` for wording and step structure.
Match the artifact container format requested by the user.
If the user did not request a container format, default to AsciiDoc.
- For Markdown files, use Markdown headings.
- For AsciiDoc files, use AsciiDoc headings.
- When explicit source-location metadata is available for a source-derived case and the artifact output path is explicit or can be inferred from the requested target file, add exactly one clickable link to the source test method line.
  - use visible text `<commit>:<file-name>:<line-num>`;
  - use target `<path-relative-to-target-artifact-file>`;
  - resolve that target relative to the directory of the target Markdown or AsciiDoc file, not relative to the repository root;
  - in Markdown, render `[<commit>:<file-name>:<line-num>](<path-relative-to-target-artifact-file>)`;
  - in AsciiDoc, render `link:<path-relative-to-target-artifact-file>[<commit>:<file-name>:<line-num>]`;
  - if either the source-location metadata or the artifact output path is missing, omit the source link instead of inventing it.
- In AsciiDoc, render each scenario as its own `[source,gherkin]` + `....` block.
- Do not merge several scenarios into one gherkin block even if they share `Feature` or `Rule`; repeat shared `Feature` and `Rule` headers as needed.

For `removed` cases:
- keep `Feature`, `Rule`, and `Scenario`;
- omit `Given` / `When` / `Then`;
- this is the only intentional `short`-mode output in this skill;
- add one short line `Причина удаления: ...`.
- if a source link is available, place it immediately after the removal reason.

For `changed` cases:
- if the output is Markdown, render each case as text with:
  - old case reference;
  - `Причина изменения: ...`;
  - `Изменения:` followed by a flat list of concrete deltas;
  - then the updated full case in artifact form.
- if the output is AsciiDoc, render them as a two-column `|===` table with header cells `| Было | Стало`;
  - use `a|` for both content cells because they contain blocks and lists;
  - the left content cell is `a|`, then one `[source,gherkin]` + `....` block with only the old case body, then the source link if available;
  - the right content cell is `a|`, then one `[source,gherkin]` + `....` block with only the updated full case body, then `Причина изменения: ...`, then `Изменения:` with a flat list;
  - do not repeat the old case reference in the `Стало` column;
  - do not place the source link in the `Стало` column.
- if the output is Markdown and a source link is available, place it after the updated case body and after the reason/change notes.
- do not prepend `Комментарий к коду:` unless the user explicitly asked for that wording.
- keep the old case reference verbatim.
- keep the updated `Rule` name as close as possible to the source `Rule` name when the behavior lineage is preserved.

For `added` cases:
- render the full new case in artifact form;
- do not attach an old source reference.

For `unchanged` cases:
- render the source case verbatim in artifact form;
- do not add extra comment lines after the case body.
- if a source link is available, place it immediately after the case block.

When current cases are absent, keep the first, second, and fourth sections explicit and say that there are no source cases for those buckets.

## Before Finishing

Check all of these:
- the target case set was designed before comparing old cases;
- the target case set covers the feature brief, explicit API changes, and material compatibility/fallback behavior from the inputs;
- no current case appears in more than one of `removed`, `changed`, `unchanged`;
- no target case appears in more than one of `added`, `changed`, `unchanged`;
- every `changed` case has a reason and a concrete delta list;
- when a changed case keeps the same behavioral obligation, the old `Rule` is preserved;
- every reused source case reference is copied verbatim;
- every `unchanged` case body is copied verbatim from the source;
- every `changed` case keeps the `Rule` name as close as possible to the source unless the old wording is no longer correct;
- every `removed` case has a removal reason and no `Given` / `When` / `Then`;
- every `unchanged` case is truly reusable without behavioral edits;
- in AsciiDoc, every scenario is rendered in its own `[source,gherkin]` + `....` block and no block contains several scenarios;
- every removed case is in `short` mode and every added, changed, or unchanged case is in `full` mode;
- when output is AsciiDoc, every `changed` case is rendered in the `|===` table shape with `a|` content cells, the `Было` cell contains the source link when available, and the `Стало` cell does not repeat the old case reference or contain the source link;
- when explicit source-location metadata is available and the artifact output path is explicit or inferable, every `removed`, `changed`, or `unchanged` case has exactly one clickable link to the source test method line with visible text `<commit>:<file-name>:<line-num>` and target `<path-relative-to-target-artifact-file>`, resolved relative to the target Markdown or AsciiDoc file directory;
- when either prerequisite for a source link is missing, no source link is invented;
- no `unchanged` case adds any trailing keep-as-is note after the case body;
- every new or updated case is written as the most abstract correct behavior case and avoids unnecessary concrete values;
- the output contains only the four requested sections.
