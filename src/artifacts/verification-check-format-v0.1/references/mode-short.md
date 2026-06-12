# Short Mode

Use this mode for concise requirement checklists and other intentionally non-executable check lists.

Output only `Feature`, `Rule`, and optional named `Example`.
If a `Rule` has exactly one unnamed `Example` in `full`, omit that `Example` in `short`.
An optional source reference line may appear immediately under `Rule` when no `Example` is rendered, or immediately after its named `Example` per `references/source-reference.md`.
Do not output `Given`, `When`, `Then`, or `And`.

Name `Rule` by the property being verified.
Use `Example` only for materially distinct input or context classes of the same `Rule`.
Choose examples that would expose one-case, hard-coded, or overfit implementations.
Prefer semantic classes over literals: default/non-default, empty/non-empty, present/missing, matching/non-matching, boundary/ordinary, valid/invalid.
Prefer the smallest complete example set.
Do not preserve example detail unless dropping it would lose contract meaning.
