# Current Acceptance Criteria

Use this only when the user asks to write current acceptance criteria from existing tests, especially `020-sut-acceptance-criteria-current.adoc`.
Keep the skill's evidence, selector, and source-order rules.

## Output

Write AsciiDoc:
- document title exactly `= Текущие критерии приёмки`;
- then one `== <SUT>` section per recovered SUT;
- inside each SUT section, use a nested unordered list;
- first list level is `Бизнес-требования` or `Технические/контрактные требования`;
- second list level is check text without `Check:`;
- source references, when included, are metadata under the check item, not separate checks.

Use the raw SUT text as the section heading, without `SUT:`.
Do not render `SUT:`, `Check:`, `Variant:`, `Given`, `When`, `Then`, or `And`.

## Source Cases

Use one check item per direct source test method from a `*Test` class.
Use helpers, clients, fixtures, and schemas only as supporting evidence; never emit them as check items or source references.
Do not split one source method into several check items because it checks several result properties.
Summarize several assertions from one method as one concise obligation.
Preserve source order inside each requirement group.

Assign a case to one requirement group by its dominant obligation:
- `Бизнес-требования` for domain outcome, selection, ordering, cardinality, rule, or allowed exceptional state;
- `Технические/контрактные требования` for HTTP status, schema, envelope, field representation, or transport contract.
