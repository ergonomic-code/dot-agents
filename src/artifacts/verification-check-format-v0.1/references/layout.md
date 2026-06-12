# Layout

Use this layout for every `verification-check-format-v0.1` output.

- `Feature` starts at column `0`.
- Put one blank line after `Feature` before its first `Rule`.
- Indent `Rule` by `2` spaces under its `Feature`.
- Indent `Example` and `Rule`-owned source references by `4` spaces under their `Rule`.
- Indent `Example`-owned source references and full-mode steps by `6` spaces under their `Example`.
- Use `Rule`-owned source references only when no `Example` is rendered.
- Render unnamed full-mode examples as `Example`.
- If a `Rule` has an unnamed `Example`, that unnamed example must be the only `Example` under that `Rule`.
- Put `Example` immediately under `Rule`.
- Put source references and full-mode steps immediately under their owner, without a blank line.
- Separate sibling `Rule` and `Feature` blocks with one blank line.
- If the chat format requires a role prefix, put the artifact on the next line and keep `Feature` at column `0`.

```text
Feature: <concrete surface or operation>

  Rule: <required property>
    Example: <optional semantic input or context class, or empty>
      # <commit>:<relative-file-path>:<line-number>
      Given <relevant condition>
      When <action on the Feature>
      Then <observable result>
```
