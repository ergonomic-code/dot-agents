# Red Case Fix Selection

Use this phase only for one selected Kotlin JUnit case created or aligned by `$code-test-case` and proven red.
Do not edit source, test, or configuration files during this phase.

## Select the fix

1. Reproduce or inspect the selected failing test and identify the current failure cause.
2. Read the selected case, supplied design context when present, nearby production code, and the smallest evidence set needed to select the fix.
3. Derive the selected behavior boundary from the failing test's entry point, endpoint, operation, scenario, and supplied design context when present.
4. Treat supplied design context as the source for behavior intent and production value sources; use the selected case only to choose the current slice and checks.
5. Select the smallest coherent production fix that implements the selected behavior slice and is consistent with the selected case and supplied design context when they exist.
6. Keep investigation and the selected fix inside that boundary, except for compile-only call-site propagation forced by the selected change.
7. If the next necessary step would inspect or change a sibling endpoint, operation, mode, or scenario to justify the fix, stop and report the boundary instead of widening the selection.
8. If selecting the fix depends on an ambiguous requirement or implementation choice, report the unresolved question instead of guessing.
9. If the test contradicts supplied design context, requires test edits, or cannot be fixed within production code, stop and report the blocker.

## Selection constraints

- Preserve the red case as the contract; do not weaken, skip, rewrite, or delete it.
- Keep scope to the selected failing case and the nearest production change points.
- A constant implementation is valid when it is contract-correct for the whole selected behavior class and does not degrade behavior outside that class.
- Do not select fixture-specific, test-shaped, bypass, or degraded behavior in existing production code or existing call paths.
- If the selected test uses stale database setup after a production migration, select the normal migration path used by the test; do not select production schema-existence branches.
- Do not include refactoring, redesign, or behavior beyond what the case and supplied design context require.
