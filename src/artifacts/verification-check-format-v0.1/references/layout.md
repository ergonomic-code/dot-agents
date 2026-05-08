# Layout

Use this layout for every `verification-check-format-v0.1` output.

- `SUT` starts at column `0`.
- Put one blank line after `SUT` before its first `Check`.
- Indent `Check` by `2` spaces under its `SUT`.
- Indent optional `Variant`, source references, and full-mode steps by `4` spaces under their `Check`.
- If both `Variant` and a source reference are present, put `Variant` first.
- Put `Variant`, source references, and full-mode steps immediately under `Check`, without a blank line.
- Separate sibling `Check` and `SUT` blocks with one blank line.
- If the chat format requires a role prefix, put the artifact on the next line and keep `SUT` at column `0`.

```text
SUT: <concrete surface or operation>

  Check: <required property>
    Variant: <optional semantic input or context class>
    # <commit>:<relative-file-path>:<line-number>
    Given <relevant condition>
    When <action on the SUT>
    Then <observable result>
```
