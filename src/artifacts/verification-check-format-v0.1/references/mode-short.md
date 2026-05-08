# Short Mode

Use this mode for concise requirement checklists and other intentionally non-executable check lists.

Output only `SUT`, `Check`, and optional `Variant`.
An optional source reference line may appear immediately under `Check` or after its `Variant` per `references/source-reference.md`.
Do not output `Given`, `When`, `Then`, or `And`.

Name `Check` by the property being verified.
Use `Variant` only for materially distinct input or context classes of the same `Check`.
Choose variants that would expose one-case, hard-coded, or overfit implementations.
Prefer semantic classes over literals: default/non-default, empty/non-empty, present/missing, matching/non-matching, boundary/ordinary, valid/invalid.
Prefer the smallest complete variant set.
Do not preserve example detail unless dropping it would lose contract meaning.
