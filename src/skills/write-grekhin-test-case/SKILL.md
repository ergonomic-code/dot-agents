---
name: write-grekhin-test-case
description: Write or normalize one or more Gherkin-style requirements in `formal-requirements-format-v0.1` in `full` mode. Use when a user or another skill needs `Feature` / `Rule` / `Scenario` / `Given` / `When` / `Then` text rendered as concise, contract-based, implementation-light prose.
---

# Write Grekhin Test Case

Read `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/mode-full.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/full-mode-checklist.md`.

## Core Rules

- Return `formal-requirements-format-v0.1` in `full` mode.
- Keep one `Scenario` per materially distinct branch unless the calling skill explicitly narrows the branch set.
- Do not mention test code, mocks, fixtures, helper names, or internal implementation details.
- Do not copy request-local numbering, ticket ids, checklist markers, or similar bookkeeping tokens into `Feature`, `Rule`, or `Scenario` names unless they are part of the public contract.

## Domain Language Rule

Name behaviors in the domain language of the user-visible contract.
Prefer business concepts, user-visible entities, public API concepts, and documented terms over code symbols.
Do not mention class names, method names, field names, enum constants, table names, flag names, builder names, or helper names unless they are themselves part of the public contract or there is no stable domain equivalent.
If code uses technical names but the behavior is domain-facing, rewrite them into domain wording.
If several code symbols map to one domain concept, use the single domain concept instead of mirroring the code structure.

## Abstraction Rule

Write scenarios as abstractly as the evidence allows.
Prefer generalized contract wording over concrete sample data.
Prefer domain wording over technical wording.
Avoid concrete parameter values, attribute values, identifiers, dates, statuses, error texts, and entity names unless they are required to:
- distinguish one behavior branch from another;
- name the public contract element being validated;
- express an observed result that would otherwise be ambiguous;
- preserve a material boundary, ordering, exact match, or cardinality guarantee.
- preserve a public contract term that users or integrators actually see.

When a concrete example is not essential, replace it with abstract wording such as `поддерживаемое значение параметра`, `неподдерживаемое значение параметра`, `значение на границе`, `значение вне допустимого диапазона`, or `сущность с признаком ...`.
When the exact input value is not behaviorally relevant, describe it by role so downstream test code can bind it through a semantic helper, factory, or fixture instead of inventing an incidental sample value.
When a code symbol is not essential, replace it with domain wording such as `получатель уведомления`, `признак архивности`, `внешний идентификатор`, or `запрос на создание`.
If several concrete examples exercise the same behavior, merge them into one abstract scenario instead of copying literal values.
