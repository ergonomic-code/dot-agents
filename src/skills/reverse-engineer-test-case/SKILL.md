---
name: reverse-engineer-test-case
description: "Reconstruct one or more Gherkin test cases from test code and return them in `formal-requirements-format-v0.1` in `full` mode. Use when the input points to a concrete test, one or more test classes, or another unambiguous test-code anchor, and you need to recover the behavioral cases: non-default conditions, checked result aspects, checked side effects, checked or strongly implied absence of side effects, and other materially verified guarantees."
---

# Reverse Engineer Test Case

Read `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/layout.md` before rendering.
Read `../../artifacts/formal-requirements-format-v0.1/references/mode-full.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/full-mode-checklist.md` only before final self-check.

Accept exactly one selector set: one concrete test selector, one repo-relative test class path, or several repo-relative test class paths. A concrete selector is `path:line`, `path:testName`, or a unique test name. Resolve class input to all real test methods in source order. If resolution is ambiguous, stop and return only the candidates.

For each resolved method, identify the action under test, preferring the call under `// When`; otherwise infer the action phase and exclude setup, assertions, and cleanup. Read only code needed for that method. Open helpers, fixtures, builders, stubs, and verification helpers only when they change recovered behavior. Keep the source test method declaration line for the scenario source reference. For the source reference commit, prefer an explicitly provided source revision; otherwise use the current checked-out `HEAD` short hash.

Recover only evidenced behavior. Assume the baseline is valid parameters, healthy DB, valid stored state, and working integrations; write only deviations from it. Prefer explicit assertions over names and verified final state over setup intent. Recover only checked outcomes and guarantees. Do not invent broader guarantees.

Treat human-readable test names as authoritative anchors before behavioral recovery.
Resolve simple annotation text before using it; concatenate literal string parts and trim code-layout whitespace.
If class `@DisplayName` or another human-readable class name is valid and semantically suitable as `Feature`, copy it verbatim.
For each method, collect enclosing human-readable group names from outermost to innermost; use class-level names only for `Feature`.
For method anchors, prefer method `@DisplayName`, then a Kotlin backticked method name, then another human-readable method name.
If the method anchor uses `<rule> :: <scenario>` with whitespace around `::`, split mechanically on that separator and trim only separator-adjacent whitespace; left side is `Rule`, right side is `Scenario`.
If the method anchor has no separator and the nearest enclosing non-class group name is valid and semantically suitable, copy that group name as `Rule` and the method anchor as `Scenario`.
Copy literal `Feature`, `Rule`, and `Scenario` anchors after the allowed annotation-resolution and separator-trim steps; do not paraphrase, reorder, or translate them.
Group sibling methods with the same literal `Rule` under one shared `Rule`.
If no method or group anchor gives a valid `Rule`, but the method anchor is valid and semantically suitable only as a one-scenario `Rule`, copy it verbatim as `Rule` and recover the missing `Scenario` conservatively.
If literal anchors are absent, invalid, or semantically unsuitable, recover `Feature`, `Rule`, and `Scenario` conservatively from the name and code evidence.
If `Feature` or `Rule` cannot be recovered confidently, stop to avoid guessing.
Recover at least one `Scenario` for each recovered `Rule`.

Write reverse-engineered steps in domain language, following the artifact shared content rules.
When reverse-engineered steps, assertions, or helpers expose raw technical symbols, translate them to their evidenced contract meaning unless the scenario is specifically about that named contract member or value.
Preserve concrete values, identifiers, attributes, boundaries, and other materially distinguishing literals.
Before returning, scan the reverse-engineered wording for copied code, helper, parameter, field, flag, timestamp, and storage names.
Translate each to domain wording or stop with the unresolved symbols.

When several assertions exist, keep only outcomes produced by the same conditions and the same action. Omit ordinary valid setup. Keep exceptional-but-allowed setup. Include side-effect details only when checked.

Under each recovered `Scenario`, emit exactly one machine-form source reference as defined in `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`.
Use the source test method declaration line.
Use the source file path relative to the target artifact file only when that path is explicitly known. Otherwise use the repo-relative source file path.

Group output by recovered `Feature`, then by recovered `Rule`. Preserve source order of classes, methods, and first appearance of each `Feature` and `Rule`. Render repeated `Feature` or `Rule` once per group.

Return only the artifact text. If the selector is ambiguous, unresolved, or `Feature` or `Rule` cannot be recovered confidently, return only a short error stating what could not be recovered and that the skill stopped to avoid guessing.
