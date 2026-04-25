# Short Mode

Use this mode for concise formal requirements and other intentionally non-executable case lists.

Output only `Feature`, `Rule`, and `Scenario`.
An optional source reference line may appear immediately under `Scenario` per `references/source-reference.md`.
Do not output `Given`, `When`, `Then`, or `And`.

Name `Scenario` by the branch or case being represented.
Keep one `Scenario` per one materially distinct branch of one `Rule`.
Treat `Scenario`s as the minimal property-test-like example set for the `Rule`.
Choose representatives that would expose one-case, hard-coded, or overfit implementations.
Prefer semantic classes over literals: default/non-default, empty/non-empty, present/missing, matching/non-matching, boundary/ordinary, valid/invalid.
Prefer the smallest complete representative set.
Do not preserve example detail unless dropping it would lose contract meaning.
