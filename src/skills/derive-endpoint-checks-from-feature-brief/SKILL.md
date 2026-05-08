---
name: derive-endpoint-checks-from-feature-brief
description: Derive endpoint-scoped verification checks from a feature brief and optional acceptance checks, then render them in `verification-check-format-v0.1` in `short` mode by default. Use when the input is a feature brief, subfeature brief, or other business requirements for one or more API endpoints and you need a complete, non-contradictory requirement check set before implementation, review, or test writing.
---

# Derive Endpoint Checks From Feature Brief

Read `../../artifacts/verification-check-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/verification-check-format-v0.1/references/layout.md` before rendering.
Read `../../artifacts/verification-check-format-v0.1/references/mode-short.md`.
Read `../../artifacts/verification-check-format-v0.1/references/requirements-coverage-checklist.md` only before final self-check.

## Mode

Default to `short`.

If the user explicitly asks for executable or test-like detail, switch to `full`.
Then read `../../artifacts/verification-check-format-v0.1/references/mode-full.md`.

## Source Priority

Prefer explicit brief statements first.
Prefer user-named authority sources next.
Treat external user test cases and examples as lower-priority draft evidence only.

## Workflow

1. Resolve the concrete endpoint set from the brief.
2. Extract explicit contract requirements from the brief.
3. Separate stable endpoint obligations from transition notes such as rollout-stage allowances, temporary permissions, migration-only constraints, phase-bound exceptions, workaround notes, and other explicitly time-bounded statements.
4. If the brief contains acceptance checks or the user provides external test cases, convert them into candidate checks.
5. Reconcile all candidate checks by source precedence.
6. Build the smallest complete non-contradictory stable check set per endpoint.
7. Render the result in the selected artifact mode.

## Scope Rules

Extract only externally observable endpoint requirements.
Keep only stable contract obligations for the requested target behavior.
Keep atomic checks for request interpretation, authoritative data sources, decision logic, scope and selection of results, required response properties, ordering and cardinality, state changes, side effects, rejection conditions, explicit invariants, and representation of contract-visible values.
Treat statements explicitly limited to the current phase, rollout step, migration window, temporary workaround, current implementation stage, or a later follow-up feature as transition notes rather than stable checks.
Treat permissions, allowances, and exceptions phrased as temporary or stage-bound as non-check scope notes unless the user explicitly asks for interim or phase-specific contract behavior.
Name `SUT`, `Check`, and `Variant` in domain language, not by raw API symbol names.
For endpoint SUTs, keep the domain name first and add the HTTP method and route in parentheses only when it is needed to disambiguate.
Write each endpoint `Check` as one required observable property.
When a request parameter, header, field, flag, enum value, or other wire symbol has a stable domain meaning, rewrite it into that meaning instead of copying the literal name.
Prefer wording that keeps the contract role visible, such as request source, selected value, or controlled business concept, without mirroring the transport-level identifier.
Keep the literal symbol only when it is itself the stable public contract term, there is no clear domain equivalent, or removing it would make the check ambiguous.
Do not create a check whose only obligation is support for a value set, mode set, scope set, or context set.
Use representative variants under the checks they can falsify.
Name variants by semantic class when the literal identity is incidental.
Use external user test cases only as draft evidence.
Add missing brief-backed checks.
Drop unsupported candidate checks.
Drop transition notes even if they are observable in the current brief scope, unless the user explicitly asked to capture the interim contract.
Do not invent routes, statuses, defaults, validation, fallback behavior, or internal design.
In `short` mode, keep only `SUT`, `Check`, and optional `Variant` lines.
In `full` mode, add steps only when the user explicitly asked for executable or test-like detail.

## Stop Conditions

Stop and report issues instead of guessing when:
- the covered endpoint set cannot be identified confidently;
- a check is materially ambiguous;
- sources materially conflict;
- a candidate check is supported only by lower-priority examples and not by the brief;
- a materially important behavior is described only as a transition note and the user did not ask for an interim contract artifact.

## Before Finishing

Check that:
- each `SUT` names one concrete endpoint or other concrete API surface;
- each `Check` states one observable required property;
- every `Variant` belongs to its parent `Check`;
- the selected mode matches the user request;
- `short` mode contains no steps;
- `full` mode adds steps only under `Check`;
- all brief-backed behavior is covered;
- unsupported example-derived checks were dropped;
- no surviving checks contradict each other;
- no surviving check encodes a temporary allowance, phase-bound permission, migration exception, or other transition-scoped note unless the user explicitly requested interim behavior;
- raw parameter, header, field, flag, and enum names were replaced with stable domain wording wherever that does not lose meaning;
- variant sets use minimal semantic representatives instead of enumerating interchangeable literals;
- all wording stays domain-based and implementation-light.

## Output

Return only the artifact text.
If a stop condition is hit, return only a short issue list.
