---
name: reverse-engineer-test-case
description: "Reconstruct one or more verification checks from test code and return them in `verification-check-format-v0.1` in `full` mode. Use when the input points to a concrete test, one or more test classes, or another unambiguous test-code anchor, and you need to recover the behavioral checks: non-default conditions, checked result aspects, checked side effects, checked or strongly implied absence of side effects, and other materially verified guarantees."
---

# Reverse Engineer Test Case

Read `../../artifacts/verification-check-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/verification-check-format-v0.1/references/layout.md` before rendering.
Read `../../artifacts/verification-check-format-v0.1/references/mode-full.md`.
Read `../../artifacts/verification-check-format-v0.1/references/source-reference.md`.
Read `../../artifacts/verification-check-format-v0.1/references/full-mode-checklist.md` only before final self-check.

Accept exactly one selector set: one concrete test selector, one repo-relative test class path, or several repo-relative test class paths.
A concrete selector is `path:line`, `path:testName`, or a unique test name.
Resolve class input to all real test methods in source order.
If resolution is ambiguous, stop and return only the candidates.

For each resolved method, identify the action under test, preferring the call under `// When`.
Otherwise infer the action phase and exclude setup, assertions, and cleanup.
Read only code needed for that method.
Open helpers, fixtures, builders, stubs, and verification helpers only when they change recovered behavior.
Keep the source test method declaration line for the check source reference.
For the source reference commit, prefer an explicitly provided source revision; otherwise use the current checked-out `HEAD` short hash.

Recover only evidenced behavior.
Assume the baseline is valid parameters, healthy DB, valid stored state, and working integrations; write only deviations from it.
Prefer explicit assertions over names and verified final state over setup intent.
Recover only checked outcomes and guarantees.
Do not invent broader guarantees.

Treat human-readable test names as authoritative anchors before behavioral recovery.
Resolve simple annotation text before using it; concatenate literal string parts and trim code-layout whitespace.
If class `@DisplayName` or another human-readable class name is valid and semantically suitable as `SUT`, copy it verbatim.
For each method, collect enclosing human-readable group names from outermost to innermost; use class-level names only for `SUT`.
For method anchors, prefer method `@DisplayName`, then a Kotlin backticked method name, then another human-readable method name.
If the method anchor uses `<check> :: <variant>` with whitespace around `::`, split mechanically on that separator and trim only separator-adjacent whitespace.
If the method anchor has no separator and the nearest enclosing non-class group name is valid and semantically suitable, copy that group name as `Check` and the method anchor as `Variant`.
If no group anchor is valid, copy the method anchor as `Check`.
Copy literal `SUT`, `Check`, and `Variant` anchors after the allowed annotation-resolution and separator-trim steps; do not paraphrase, reorder, or translate them.
If literal anchors are absent, invalid, or semantically unsuitable, recover `SUT`, `Check`, and optional `Variant` conservatively from the name and code evidence.
If `SUT` or `Check` cannot be recovered confidently, stop to avoid guessing.

Write reverse-engineered steps in domain language, following the artifact shared content rules.
When reverse-engineered steps, assertions, or helpers expose raw technical symbols, translate them to their evidenced contract meaning unless the check is specifically about that named contract member or value.
Preserve concrete values, identifiers, attributes, boundaries, and other materially distinguishing literals.
Before returning, scan the reverse-engineered wording for copied code, helper, parameter, field, flag, timestamp, and storage names.
Translate each to domain wording or stop with the unresolved symbols.

When several assertions exist, keep only outcomes produced by the same conditions and the same action.
Omit ordinary valid setup.
Keep exceptional-but-allowed setup.
Include side-effect details only when checked.

Under each recovered `Check`, emit exactly one machine-form source reference as defined in `../../artifacts/verification-check-format-v0.1/references/source-reference.md`.
If the check has a `Variant`, put the source reference after `Variant`.
Use the source test method declaration line.
Use the source file path relative to the target artifact file only when that path is explicitly known.
Otherwise use the repo-relative source file path.

Group output by recovered `SUT`.
Preserve source order of classes and methods.
Render repeated `SUT` once per group.
Render each recovered `Check` block in source order.

Return only the artifact text.
If the selector is ambiguous, unresolved, or `SUT` or `Check` cannot be recovered confidently, return only a short error stating what could not be recovered and that the skill stopped to avoid guessing.
