---
name: derive-endpoint-rules-from-feature-brief
description: Derive endpoint-scoped business rules from a feature brief and optional acceptance test cases, then render them in `formal-requirements-format-v0.1` in `short` mode by default. Use when the input is a feature brief, subfeature brief, or other business requirements for one or more API endpoints and you need a complete, non-contradictory requirement set before implementation, review, or test writing.
---

# Derive Endpoint Rules From Feature Brief

Read `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/layout.md` before rendering.
Read `../../artifacts/formal-requirements-format-v0.1/references/mode-short.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/requirements-coverage-checklist.md` only before final self-check.

## Mode

Default to `short`.

If the user explicitly asks for executable or test-like detail, switch to `full`.
Then read `../../artifacts/formal-requirements-format-v0.1/references/mode-full.md`.

## Source Priority

Prefer explicit brief statements first.
Prefer user-named authority sources next.
Treat external user test cases and examples as lower-priority draft evidence only.

## Workflow

1. Resolve the concrete endpoint set from the brief.
2. Extract explicit contract requirements from the brief.
3. Separate stable endpoint obligations from transition notes such as rollout-stage allowances, temporary permissions, migration-only constraints, phase-bound exceptions, workaround notes, and other explicitly time-bounded statements.
4. If the brief contains acceptance tests or the user provides external test cases, including plain Gherkin acceptance cases, convert them into candidate rules.
5. Reconcile all candidate rules by source precedence.
6. Build the smallest complete non-contradictory stable rule set per endpoint.
7. Render the result in the selected artifact mode.

## Scope Rules

Extract only externally observable endpoint requirements.
Keep only stable contract obligations for the requested target behavior.
Keep atomic rules for request interpretation, authoritative data sources, decision logic, scope and selection of results, required response properties, ordering and cardinality, state changes, side effects, rejection conditions, explicit invariants, and representation of contract-visible values.
Treat statements explicitly limited to the current phase, rollout step, migration window, temporary workaround, current implementation stage, or a later follow-up feature as transition notes rather than rules.
Treat permissions, allowances, and exceptions phrased as temporary or stage-bound as non-rule scope notes unless the user explicitly asks for interim or phase-specific contract behavior.
Name `Feature`, `Rule`, and `Scenario` in domain language, not by raw API symbol names.
For endpoint features, keep the domain name first and add the HTTP method and route in parentheses.
Write each endpoint `Rule` so `Feature` + `Rule` states the endpoint, relevant data/request conditions, expected response, persistent state changes, and outbound interactions.
When a request parameter, header, field, flag, enum value, or other wire symbol has a stable domain meaning, rewrite it into that meaning instead of copying the literal name.
Prefer wording that keeps the contract role visible, such as request source, selected value, or controlled business concept, without mirroring the transport-level identifier.
Keep the literal symbol only when it is itself the stable public contract term, there is no clear domain equivalent, or removing it would make the rule ambiguous.
Do not create a rule whose only obligation is support for a value set, mode set, scope set, or context set.
Use representative variants as `Scenario` branches under the obligations they can falsify.
Name scenarios by semantic class when the literal identity is incidental.
Use external user test cases only as draft evidence.
Add missing brief-backed rules.
Drop unsupported candidate rules.
Drop transition notes even if they are observable in the current brief scope, unless the user explicitly asked to capture the interim contract.
Do not invent routes, statuses, defaults, validation, fallback behavior, or internal design.
In `short` mode, keep scenario headers only.
In `full` mode, add steps only when the user explicitly asked for executable or test-like detail.

## Stop Conditions

Stop and report issues instead of guessing when:
- the covered endpoint set cannot be identified confidently;
- a rule is materially ambiguous;
- sources materially conflict;
- a candidate rule is supported only by lower-priority examples and not by the brief;
- a materially important behavior is described only as a transition note and the user did not ask for an interim contract artifact.

## Before Finishing

Check that:
- each `Feature` names one concrete endpoint or other concrete API surface;
- each `Rule` states one material data/request condition set and all response, persistent-state, and outbound-interaction obligations for it;
- the selected mode matches the user request;
- `short` mode contains no steps;
- `full` mode adds steps only under `Scenario`;
- all brief-backed behavior is covered;
- unsupported example-derived rules were dropped;
- no surviving rules contradict each other;
- no surviving rule encodes a temporary allowance, phase-bound permission, migration exception, or other transition-scoped note unless the user explicitly requested interim behavior;
- raw parameter, header, field, flag, and enum names were replaced with stable domain wording wherever that does not lose meaning;
- scenario sets use minimal semantic representatives instead of enumerating interchangeable literals;
- all wording stays domain-based and implementation-light.

## Output

Return only the artifact text.
If a stop condition is hit, return only a short issue list.
