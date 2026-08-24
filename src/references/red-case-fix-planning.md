# Red Case Fix Planning

Read `framework_checkout_root/src/conventions/tests.md`.
Read `framework_checkout_root/src/conventions/ergonomic-approach-rules.md`.
Read `framework_checkout_root/src/conventions/process/production-code-development.md`.
Read `framework_checkout_root/src/conventions/code-implementation.md`.
Read `framework_checkout_root/src/artifacts/structure-chart-v1/ARTIFACT.md`.

Use this phase only for one selected Kotlin JUnit case created or aligned by `$code-test-case` and proven red.
Do not edit source, test, task, or configuration files during this phase.

## Current failure

Reproduce or inspect the selected failing test and identify the current failure cause.

## Reuse an existing plan

1. Accept the plan only when its request or task artifact identifies the selected case, specifies a production fix sufficiently to implement, includes the required `structure-chart/v1`, and contains no unresolved implementation choice.
2. Check it against the current failure, task design when present, and the selection constraints below.
   If its applicability is unclear or it conflicts with that evidence, report the unresolved question or blocker instead of replacing the plan.
3. Preserve its implementation decisions and complete only missing plan-contract fields from current evidence.
4. Do not run `Create a plan` for an accepted plan.

## Create a plan

1. Read the selected case, task design when present, nearby production code, and the smallest evidence set needed to plan the fix.
2. Derive the selected behavior boundary from the failing test's entry point, endpoint, operation, scenario, and task design when present.
3. Treat task design as the source for behavior intent and production value sources; use the selected case only to choose the current slice and checks.
4. Select the smallest coherent production fix that implements the selected behavior slice and is consistent with the selected case and task design when they exist.
5. Represent the selected fix with a `structure-chart/v1` whose first two structure levels include the behavior's orchestration operation and every immediate production callee required by the selected increment, with a call edge from the operation to each callee.
6. Add deeper callees only when the selected increment requires them; do not design later behavior to complete the chart.
7. Keep investigation and the selected fix inside that boundary, except for compile-only call-site propagation forced by the selected change.
8. If the next necessary step would inspect or change a sibling endpoint, operation, mode, or scenario to justify the fix, stop and report the boundary instead of widening the plan.
9. If selecting the fix depends on an ambiguous requirement or implementation choice, report the unresolved question instead of guessing.
10. If the test contradicts task design, requires test edits, or cannot be fixed within production code, stop and report the blocker.

## Selection constraints

- Preserve the red case as the contract; do not plan to weaken, skip, rewrite, or delete it.
- Keep scope to the selected failing case and the nearest production change points.
- A constant implementation is valid when it is contract-correct for the whole selected behavior class and does not degrade behavior outside that class.
- Do not select fixture-specific, test-shaped, bypass, or degraded behavior in existing production code or existing call paths.
- If the selected test uses stale database setup after a production migration, select the normal migration path used by the test; do not plan production schema-existence branches.
- Do not include refactoring, redesign, or behavior beyond what the case and task design require.

## Plan contract

A reusable production-fix plan contains:

- the selected case, failure evidence, diagnosed cause, and design context used or absent;
- the selected behavior boundary, smallest coherent production fix, and target production areas;
- a valid `structure-chart/v1` covering at least the orchestration operation and its immediate production callees required by the selected increment;
- the command that verifies the selected case;
- unresolved questions or blockers.
