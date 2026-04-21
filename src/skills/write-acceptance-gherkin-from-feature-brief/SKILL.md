---
name: write-acceptance-gherkin-from-feature-brief
description: Write standard acceptance Gherkin test cases from a feature brief, subfeature brief, or similar business requirements. Use when you need concise plain-Gherkin acceptance scenarios before rule extraction, implementation, review, or test coding, and the output must not depend on a project-specific artifact format.
---

# Write Acceptance Gherkin From Feature Brief

Read only the target brief and authority sources the user explicitly names.
If the brief has a terminology section, use it as local term authority.

## Workflow

1. Resolve the covered API surface or user-visible capability set from the brief.
2. Extract explicit observable requirements, invariants, selection rules, ordering, cardinality, rejection conditions, and compatibility constraints.
3. Separate stable target behavior from rollout notes, migration-stage allowances, follow-up work, and other transition-only statements.
4. If the brief already contains acceptance scenarios, normalize them and add only missing brief-backed cases.
5. Build the smallest complete acceptance case set for the stable target behavior.
6. Render it as plain standard Gherkin.

## Writing Rules

Use only `Feature`, `Rule`, `Scenario`, `Given`, `When`, `Then`, and `And`.
Write all human-readable text in the configured `artifact_language`.
Name one concrete API surface or user-visible capability per `Feature`.
Name one observable obligation per `Rule`, in the obligation form of that language.
Use one `Scenario` per materially distinct behavior branch.
Keep only outcome-relevant deviations from the valid default baseline in `Given`.
Put the action under test in `When`.
Put only observable results, side effects, rejections, ordering, and cardinality guarantees in `Then` and following `And`.
Prefer user-facing domain wording over code, DB, transport, integration, and implementation wording.
Keep raw parameter, field, enum, and path names only when they are stable public contract terms or needed to avoid ambiguity.
Prefer abstract contract wording over sample literals.
Keep concrete values only when needed to express a boundary, ordering, cardinality, exact match, or other materially distinct branch.
Cover positive, negative, boundary, fallback, and compatibility behavior only when the brief supports it.
Do not invent endpoints, statuses, defaults, validation, fallback behavior, or internal design.
Do not write scenarios for hidden decision sources, server-side data provenance, internal precedence rules, or other details that a product-level actor cannot vary or observe through the external contract.
If a brief statement explains how the system chooses a result but the user can verify only the resulting behavior, encode only that result-level behavior.
Drop statements that are true only as implementation constraints, debugging guidance, or decomposition notes even when they are written as business rules.
Treat current-stage simplifications, temporary permissions, temporary absences of localization or validation, compatibility-only allowances, and "for now / at this stage / until the next step" behavior as transition notes, not acceptance rules.
Do not write a scenario whose only point is to freeze a temporary fallback that is expected to disappear in a planned follow-up feature.

## Scope Rules

Keep only behavior observable from outside the system.
Keep only behavior that a realistic actor or client can falsify through the product contract.
Drop transition-only notes unless the user explicitly asks for interim behavior.
Treat wording such as `пока`, `на этом этапе`, `в этой сабфиче`, `до следующего шага`, `временно`, `продолжает`, `позже`, and explicit references to later subfeatures as strong evidence of non-acceptance scope.
Keep different surfaces in separate `Feature`s.
Keep different observable properties in separate `Rule`s even when they appear in one paragraph of the brief.
Do not mirror the brief structure mechanically if several statements describe one obligation.
When a statement can be tested only by forcing impossible or product-invalid input combinations, treat it as non-acceptance scope.

## Stop Conditions

Stop and report issues instead of guessing when:
- the covered surface cannot be identified confidently;
- a behavior is materially ambiguous;
- named sources conflict materially;
- a materially important branch cannot be stated without inventing contract details.

## Before Finishing

Check that:
- each `Feature` is concrete;
- each `Rule` states exactly one observable obligation;
- all brief-backed stable behavior is covered;
- no surviving case contradicts another;
- no transition-only note became a stable case unless explicitly requested;
- no case exists only to confirm internal source selection or another non-falsifiable implementation detail;
- no case exists only to freeze a temporary stage-bound fallback, simplification, or deferred feature;
- wording stays domain-based and implementation-light;
- the output is plain Gherkin only.

## Output

Return only the Gherkin text.
If a stop condition is hit, return only a short issue list.
