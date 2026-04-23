# Source Reference

Use this reference when a scenario must preserve the source location of a test or another evidence line.

Attach at most one source reference to one `Scenario`.
If the source location is unknown, omit the reference.

## Fields

- `<commit>`: the concrete source revision. Prefer an explicitly provided revision. Otherwise prefer the current checked-out `HEAD` short hash.
- `<relative-file-path>`: the source file path relative to the target artifact file directory when that directory is known. Otherwise use the repo-relative source file path.
- `<file-name>`: the basename of `<relative-file-path>`.
- `<line-number>`: the source test method declaration line or another explicitly provided stable source line.

## Machine Form

Use machine form in plain artifact text and whenever a safe clickable link cannot be rendered.

```text
# <commit>:<relative-file-path>:<line-number>
```

## Human Form

Use human form only when the output container supports clickable links and the target artifact file path is known.

Markdown:

```md
[<commit>:<file-name>:<line-number>](<relative-file-path>)
```

AsciiDoc:

```adoc
link:<relative-file-path>[<commit>:<file-name>:<line-number>]
```

Keep the link target equal to `<relative-file-path>`.
Keep the visible text basename-only: `<commit>:<file-name>:<line-number>`.
When human form cannot be rendered safely, fall back to machine form instead of inventing or dropping the source reference.
