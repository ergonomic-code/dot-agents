# Short Mode

Use this mode for concise formal requirements and other intentionally non-executable case lists.

Output only `Feature`, `Rule`, and `Scenario`.
Do not output `Given`, `When`, `Then`, or `And`.

Name `Scenario` by the branch or case being represented.
Keep one `Scenario` per one materially distinct branch of one `Rule`.
Prefer the smallest complete scenario set.
Do not preserve example detail unless dropping it would lose contract meaning.
