# Layout

Use this layout for every `formal-requirements-format-v0.1` output.

- `Feature` starts at column `0`.
- Put one blank line after `Feature` before its first `Rule`.
- Put one blank line after `Rule` before its first `Scenario`.
- Indent `Rule` by `2` spaces under its `Feature`.
- Indent `Scenario` by `4` spaces under its `Rule`.
- Indent source references and full-mode steps by `6` spaces under their `Scenario`.
- Put source references and full-mode steps immediately under `Scenario`, without a blank line.
- Separate sibling `Scenario`, `Rule`, and `Feature` blocks with one blank line.
- If the chat format requires a role prefix, put the artifact on the next line and keep `Feature` at column `0`.

```gherkin
Feature: <concrete surface or SUT element>

  Rule: <obligation>

    Scenario: <branch or case>
      # <commit>:<relative-file-path>:<line-number>
      Given <relevant condition>
      When <action on the surface or SUT>
      Then <observable result>
```
