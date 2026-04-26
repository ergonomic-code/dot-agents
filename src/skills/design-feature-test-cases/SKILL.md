---
name: design-feature-test-cases
description: Design feature test-case refresh artifacts from a feature brief, implementation/API context, and optional current cases. Prefer added cases for new obligations; update old cases only when forced.
---

# Design Feature Test Cases

Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Read `framework_checkout_root/src/conventions/feature-stage-skill.md`.
Read `../write-grekhin-test-case/SKILL.md`.
Read the format reference at `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`.

## Feature-stage bindings

- stage code: `040`
- default feature-dir output path: `<feature-dir>/040-test-cases-refresh.adoc`
- progress.md checklist item: `Обновление тест-кейсов`

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
- optional explicit artifact output path.
  - use it when the artifact will be written to a concrete Markdown or AsciiDoc file.

If current test cases are absent, still design the target case set and keep `removed`, `changed`, and `unchanged` sections explicit and empty.
If API IR is absent, derive the target set from the brief and implementation summary only.

## Core Rule

Design the target test case set first; treat old cases only as reusable material and migration input, not as the source of truth.
Prefer `added` for new obligations; keep old cases unchanged unless they contradict new rules, would stop compiling, would fail under new conditions, or are baseline save/return cases for model field-set changes.

## Workflow

1. If the output artifact already exists, read it before editing.
2. Read the feature brief and extract the target behavior.
   - Prefer explicit acceptance scenarios, business rules, invariants, compatibility constraints, and error conditions.
   - Separate independent behavior properties into separate `Rule`s.
3. Read the implementation summary and API IR.
   - Use them to refine the contract, identify touched surfaces, and detect migration-sensitive behavior.
   - Prefer the feature brief and explicit API rules over narrative implementation details when they conflict.
4. Design the target case set from scratch.
   - Cover only behavior that is actually implied by the inputs.
   - Add positive, negative, boundary, fallback, and compatibility cases only when the inputs justify them.
   - Merge duplicates and keep one `Scenario` per materially distinct branch.
   - Prefer abstract contract wording over literal sample data unless exact values are behaviorally required.
5. Normalize current relevant cases if they exist.
   - If they are not already in artifact form, recover stable `Feature` / `Rule` / `Scenario` anchors without changing meaning.
   - If they are already in artifact form, treat their wording as canonical and keep it verbatim when reusing or citing them.
   - Treat any optional scenario source reference as metadata, not as part of the canonical case wording.
   - Use the recovered anchor as the source reference in `changed` cases.
6. Compare current cases against the target case set with preservation bias.
   - `unchanged`: the current case stays valid as-is.
   - `changed`: the current case must change by the Core Rule.
   - `removed`: the current case no longer belongs to the target set.
   - for `changed`, preserve the old `Rule` unless the old wording becomes incorrect.
7. Mark as `added` every target case that is not `changed` or `unchanged`.
8. Render the four output lists.
9. If an output path is resolved, write the result to that Markdown or AsciiDoc file.

## Classification Rules

- Put every current case into exactly one bucket: `removed`, `changed`, or `unchanged`.
- Put every target case into exactly one bucket: `added`, `changed`, or `unchanged`.
- Prefer `added` for every new obligation.
- Use `changed` only when the old case itself must change by the Core Rule.
- A related old case plus a new behavior branch is `unchanged` + `added`, not `changed`.
- Use `removed` when the old case targets behavior that is obsolete, contradicted, overspecified, or no longer worth keeping as a separate guarantee.
- Use `unchanged` only when the old case can be kept as-is, with no assertion, input, or expectation edits.
- Do not invent new obligations from implementation hints alone unless the brief or API contract makes them test-worthy.

## Output

The artifact content must contain exactly four sections in this order:
- `Удаляемые тест-кейсы`
- `Изменяемые тест-кейсы`
- `Добавляемые тест-кейсы`
- `Актуальные тест-кейсы без изменений`

Write human-readable text in the configured artifact language.
Base the case bodies on `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Follow `../write-grekhin-test-case/SKILL.md` for wording and step structure.
Match the artifact container format requested by the user.
If the user did not request a container format, infer it from the explicit output path extension when present.
Otherwise default to AsciiDoc.
- For Markdown files, use Markdown headings.
- For AsciiDoc files, use AsciiDoc headings.
- If an output path is resolved, write only the artifact text to that file.
- Otherwise return only the artifact text.
- When source-location metadata is available for a source-derived case, render exactly one source reference using `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`.
- In Markdown or AsciiDoc, use the human clickable form when the artifact output path is explicit or can be inferred.
- In the human form, keep visible text `<commit>:<file-name>:<line-num>` and keep the target equal to the relative source file path resolved from the target artifact file directory.
- When the artifact output path is missing or a safe clickable link cannot be rendered, use the machine form instead of dropping the source reference.
- In AsciiDoc, render each scenario as its own `[source,gherkin]` + `....` block.
- Do not merge several scenarios into one gherkin block even if they share `Feature` or `Rule`; repeat shared `Feature` and `Rule` headers as needed.

For `removed` cases:
- keep `Feature`, `Rule`, and `Scenario`;
- omit `Given` / `When` / `Then`;
- this is the only intentional `short`-mode output in this skill;
- add one short line `Причина удаления: ...`.
- if a source reference is available, place it immediately after the removal reason.

For `changed` cases:
- if the output is Markdown, render each case as text with:
  - old case reference;
  - `Причина изменения: ...`;
  - `Изменения:` followed by a flat list of concrete deltas;
  - then the updated full case in artifact form.
- if the output is AsciiDoc, render them as a two-column `|===` table with header cells `| Было | Стало`;
  - use `a|` for both content cells because they contain blocks and lists;
  - the left content cell is `a|`, then one `[source,gherkin]` + `....` block with only the old case body, then the source reference if available;
  - the right content cell is `a|`, then one `[source,gherkin]` + `....` block with only the updated full case body, then `Причина изменения: ...`, then `Изменения:` with a flat list;
  - do not repeat the old case reference in the `Стало` column;
  - do not place the source reference in the `Стало` column.
- if the output is Markdown and a source reference is available, place it after the updated case body and after the reason/change notes.
- do not prepend `Комментарий к коду:` unless the user explicitly asked for that wording.
- keep the old case reference verbatim.
- keep the updated `Rule` name as close as possible to the source `Rule` name when the behavior lineage is preserved.

For `added` cases:
- render the full new case in artifact form;
- do not attach an old source reference.

For `unchanged` cases:
- render the source case verbatim in artifact form;
- do not add extra comment lines after the case body.
- if a source reference is available, place it immediately after the case block.

When current cases are absent, keep the first, second, and fourth sections explicit and say that there are no source cases for those buckets.

## Before Finishing

Check all of these:
- the target case set was designed before comparing old cases;
- the target case set covers the feature brief, explicit API changes, and material compatibility/fallback behavior from the inputs;
- no current or target case appears in more than one bucket;
- every `changed` case has a reason and a concrete delta list;
- no current case is `changed` only because it is related to a new obligation, except baseline save/return cases for model field-set changes;
- when a changed case keeps the same behavioral obligation, the old `Rule` is preserved;
- every reused source case `Feature` / `Rule` / `Scenario` anchor is copied verbatim;
- every `unchanged` case body is copied verbatim from the source;
- every `changed` case keeps the `Rule` name as close as possible to the source unless the old wording is no longer correct;
- every `removed` case has a removal reason and no `Given` / `When` / `Then`;
- every `unchanged` case is truly reusable without behavioral edits;
- in AsciiDoc, every scenario is rendered in its own `[source,gherkin]` + `....` block and no block contains several scenarios;
- every removed case is in `short` mode and every added, changed, or unchanged case is in `full` mode;
- when output is AsciiDoc, every `changed` case is rendered in the `|===` table shape with `a|` content cells, the `Было` cell contains the source reference when available, and the `Стало` cell does not repeat the old case reference or contain the source reference;
- when explicit source-location metadata is available, every `removed`, `changed`, or `unchanged` case has exactly one source reference rendered per `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`;
- when the output is Markdown or AsciiDoc and the artifact output path is explicit or inferable, the source reference uses the human clickable form with visible text `<commit>:<file-name>:<line-num>` and a target resolved relative to the target artifact file directory;
- when the human clickable form cannot be rendered safely, the machine form is used instead of inventing or dropping the source reference;
- when source-location metadata is absent, no source reference is invented;
- no `unchanged` case adds any trailing keep-as-is note after the case body;
- every new or updated case is written as the most abstract correct behavior case and avoids unnecessary concrete values;
- the output contains only the four requested sections.
