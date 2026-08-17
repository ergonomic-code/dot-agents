---
name: prepare-task-workdir
description: Prepare a new or existing Lightweight SDD task workdir through a guided dialogue that completes the task brief, optionally collects verified code anchors, develops and compares solution options with the user, records the explicitly selected approach in the solution brief, and synchronizes preparation progress in todo.md. Use when the user asks to prepare, elaborate, specify, or design a task before implementation rather than only scaffold its files.
---

# Prepare Task Workdir

Read `framework_checkout_root/src/conventions/process/tasks.md`.
Read `framework_checkout_root/src/skills/init-task-workdir/SKILL.md`.
Read `framework_checkout_root/src/skills/collect-code-anchors/SKILL.md`.
Read `framework_checkout_root/src/references/task-brief-template.md`.
Read `framework_checkout_root/src/references/solution-brief-template.md`.

## Scope

- Prepare one new or existing task workdir through requirements clarification, optional current-code research, and solution selection.
- Limit writes to the resolved task workdir and its preparation artifacts.
- Do not change product code, tests, project configuration, or unrelated task artifacts.
- Preserve confirmed content and unrelated user changes.

## Resolve the task workdir

1. Resolve an existing task directory through `framework_checkout_root/src/conventions/process/tasks.md`.
2. When an existing task directory resolves, require `010-task-brief.md`, `030-solution-brief.md`, and `todo.md` and read their current content.
3. When no existing task directory resolves, require an explicit task id and slug and follow `$init-task-workdir` only to validate the target and create the standard files.
4. If required input is missing or conflicting, ask only for that input and stop.
5. If a standard file is missing, stop and report its exact path.

## Interaction contract

- Work through the stages in order and keep the user informed of the active stage.
- Reuse information already present in the prompt or task artifacts.
- Ask the smallest compact set of questions needed to resolve the current decision boundary.
- Do not infer requirements or decisions whose alternatives would materially change scope, observable behavior, or solution direction.
- Update an artifact only from explicit user input or verified code evidence within that artifact's responsibility.
- Stop after asking a blocking question and resume the same stage from the user's answer.

## 1. Complete the task brief

1. Compare the prompt and current `010-task-brief.md` with the task-brief template.
2. Identify only missing or ambiguous information that affects the task initiator, current state, task driver, intended outcome, relevant consequences, terms, scope, observable changes, scenarios, boundaries, or errors.
3. Interview the user until those gaps are resolved.
4. When requirements interact, restate their conditions, guarantees, and resulting behavior together and require explicit confirmation before drafting.
5. Treat domain concepts and their configured or example values separately; do not replace one with the other.
6. Before updating the artifact, check the draft against confirmed evidence and across sections for consistent causality, actors, terms, qualifiers, units, values, and formulas; ask about mismatches instead of guessing.
7. Update `010-task-brief.md` with confirmed requirements in the user's domain language.
8. Keep solution and implementation choices out of the task brief.
9. When a capability may use an API, capture only its actor, observable behavior, and contract-independent constraints.
10. Present a compact summary and require the user to confirm that the task brief is sufficient before solution design.

If later research or solution discussion exposes a requirement ambiguity or changes scope, return to this stage and update the task brief only after user confirmation.

## 2. Decide whether to collect code anchors

1. State whether code anchors are needed before comparing solutions.
2. Collect them when the user requests them or when the solution depends on current implementation boundaries, reuse points, integrations, persistence, migration, or existing tests.
3. Skip them when the task is independent of existing code or the confirmed brief already provides enough evidence for the solution decision.
4. When anchors are needed, follow `$collect-code-anchors`, using `010-task-brief.md` as the source and `020-code-anchors.md` as the output.
5. If no concrete code starting point is available, ask the user for one or more and stop as required by `$collect-code-anchors`.
6. Resume this workflow after the anchor artifact passes its own checks.
7. Report findings that materially constrain the solution before proposing options.

Do not turn observed current behavior into a requirement without user confirmation.

## 3. Select and record the solution

1. Derive solution options from the confirmed task brief and verified anchors, when present.
2. Present at least two materially different viable options when the evidence permits them.
3. If the constraints leave only one viable option, explain why instead of inventing alternatives.
4. For each option, state the affected surface, core mechanism, benefits, risks, and meaningful tradeoffs.
5. Recommend one option and explain why it best balances task fit, maintainability, and change size.
6. Discuss and revise the options with the user until the material decision boundaries are resolved.
7. Require the user to select the final option explicitly.
8. Do not design an API contract before the final option is selected.
9. After selection, design only API details required to make the selected approach coherent; defer the rest until the first implementation case for which that API is the SUT.
10. Do not record a selected approach while the choice is unresolved.
11. Write the resulting context, selected approach, non-blocking open questions, and rejected alternatives to `030-solution-brief.md`.
12. Do not finalize the solution brief while an open question can materially change the selected approach.

## Finish

- Update only preparation items in `todo.md` whose completion is supported by the resulting artifacts and decisions.
- Mark skipped optional research explicitly as not required instead of implying that it was performed.
- Preserve implementation tasks and unrelated progress.
- Verify that the task brief contains the confirmed task, the solution brief names the explicit choice, and referenced anchor artifacts exist.
- Report the task directory, completed stages, changed artifacts, selected solution, skipped optional artifacts, and remaining open questions.
