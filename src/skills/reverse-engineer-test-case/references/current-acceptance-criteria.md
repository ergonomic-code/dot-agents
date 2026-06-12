# Current Acceptance Criteria

Use this only when the user asks to write current acceptance criteria from existing tests, especially `020-sut-acceptance-criteria-current.adoc`.
Keep the skill's evidence, selector, and source-order rules.

## Output

Write AsciiDoc:
- document title exactly `= Текущие критерии приёмки`;
- then one `== <Feature>` section per recovered `Feature`;
- inside each `Feature` section, use a nested unordered list;
- first list level is `Бизнес-требования` or `Технические/контрактные требования`;
- second list level is rule text without `Rule:`;
- source references, when included, are metadata under the rule item, not separate items.

Use the raw `Feature` text as the section heading, without `Feature:`.
Do not render `Feature:`, `Rule:`, `Example:`, `Given`, `When`, `Then`, or `And`.

## Source Cases

Group source methods by recovered `Rule`.
Emit one rule item per recovered `Rule`, not per source test method.
Treat each direct source test method from a `*Test` class as evidence for that rule.
Use helpers, clients, fixtures, and schemas only as supporting evidence; never emit them as rule items or source references.
Do not split one source method into several rule items because it checks several result properties.
Do not duplicate one recovered `Rule` into several rule items only because several source methods cover different examples of it.
Summarize several assertions from one method as one concise obligation.
Preserve source order of rules inside each requirement group.

Assign a case to one requirement group by its dominant obligation:
- `Бизнес-требования` for domain outcome, selection, ordering, cardinality, rule, or allowed exceptional state;
- `Технические/контрактные требования` for HTTP status, schema, envelope, field representation, or transport contract.
