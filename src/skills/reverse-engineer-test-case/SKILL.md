---
name: reverse-engineer-test-case
description: "Reconstruct one or more Gherkin test cases from test code and return them in `formal-requirements-format-v0.1` in `full` mode. Use when the input points to a concrete test, one or more test classes, or another unambiguous test-code anchor, and you need to recover the behavioral cases: non-default conditions, checked result aspects, checked side effects, checked or strongly implied absence of side effects, and other materially verified guarantees."
---

# Reverse Engineer Test Case

Read `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/mode-full.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`.

Accept exactly one selector set: one concrete test selector, one repo-relative test class path, or several repo-relative test class paths. A concrete selector is `path:line`, `path:testName`, or a unique test name. Resolve class input to all real test methods in source order. If resolution is ambiguous, stop and return only the candidates.

For each resolved method, identify the action under test, preferring the call under `// When`; otherwise infer the action phase and exclude setup, assertions, and cleanup. Read only code needed for that method. Open helpers, fixtures, builders, stubs, and verification helpers only when they change recovered behavior. Keep the source test method declaration line for the scenario source reference. For the source reference commit, prefer an explicitly provided source revision; otherwise use the current checked-out `HEAD` short hash.

Recover only evidenced behavior. Assume the baseline is valid parameters, healthy DB, valid stored state, and working integrations; write only deviations from it. Prefer explicit assertions over names and verified final state over setup intent. Recover only checked outcomes and guarantees. Do not invent broader guarantees.

Recover `Feature` from one concrete SUT element. Recover `Rule` as one concrete observable behavior property in the configured `artifact_language`. If either cannot be recovered confidently from the test name and code evidence, stop to avoid guessing.
Recover at least one `Scenario` for each recovered `Rule`.

For method names in the formal shape `<rule> :: <scenario>`, split mechanically on ` :: `: left side is `Rule`, right side is `Scenario`. Do not paraphrase either side. Group sibling methods with the same left side under one shared `Rule`.

If a method name does not use that formal shape, recover `Rule` and `Scenario` conservatively from the name and code evidence. When the name already gives a complete conditional rule, keep that order instead of rewriting it.

Keep `Given` in business language unless technical terms are part of the stable contract or no business equivalent exists. Preserve concrete values, identifiers, attributes, boundaries, and other materially distinguishing literals.

When several assertions exist, keep only outcomes produced by the same conditions and the same action. Omit ordinary valid setup. Keep exceptional-but-allowed setup. Include side-effect details only when checked.

Under each recovered `Scenario`, emit exactly one machine-form source reference as defined in `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`.
Use the source test method declaration line.
Use the source file path relative to the target artifact file only when that path is explicitly known. Otherwise use the repo-relative source file path.

Group output by recovered `Feature`, then by recovered `Rule`. Preserve source order of classes, methods, and first appearance of each `Feature` and `Rule`. Render repeated `Feature` or `Rule` once per group.

Return only the artifact text. If the selector is ambiguous, unresolved, or `Feature` or `Rule` cannot be recovered confidently, return only a short error stating what could not be recovered and that the skill stopped to avoid guessing.
