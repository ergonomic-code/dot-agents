# Shared context-fix workflow

Use this workflow for `$fix-framework-context` and `$fix-project-context`.
Each concrete skill defines its own role, editable roots, redirect rules, file scope, and layer values.

## Required input

- `codex session id`
- `problem`
- `target behavior`

If any required input is missing, ask only for the missing items and stop.
Treat `codex session id` as mandatory.
If the session cannot be found from the id, say so and ask for the session file path or the missing evidence.

## Evidence

Use the session as primary evidence.
Look under `~/.codex/sessions/` and `~/.cache/JetBrains/IntelliJIdea*/aia/codex/sessions/`.
Read only material turns and files.

## Common classification rules

Treat current files as the source of truth.
Classify each candidate by operation (`delete` | `shorten` | `merge` | `move` | `split` | `add`) and breadth (`single-file` | `cross-file`).
Prefer `delete`, `shorten`, `merge`, `move`, or `split` before `add`.
Do not infer deltas unsupported by the session and files.
Before adding, scan the smallest target set for overlap and prefer reuse, merge, move, or replacement.
If one file seems enough, double-check linked files for contradiction, stale refs, or missing enforcement, but do not expand without concrete need.

## Analysis

Identify symptom, likely root cause, current context gap, and target behavior.
Base root cause on the session and current files.

## Options

Always propose at least these options:
- `minimal`
- `systemic`
- `optimal`

Add extras only when materially different.
Do not restate the same solution with cosmetic wording changes.
Each option must include candidate files or areas, classification summary, delta, why it fits its class, benefits, and risks.

## Long-file rule

When an option adds rules to an existing file longer than `50` lines, justify why it belongs there instead of deleting, shortening, merging, extracting a small file, or moving detail to `references/`.
Treat unexplained growth as a defect.

## Implementation

Recommend one option and why it wins on correctness, maintainability, and size.
If the user has not chosen yet, stop and ask.
Do not edit files before explicit choice.
After the user chooses an option, implement only that option.
Keep to the smallest file set consistent with the chosen option.
Before editing, check whether linked layers, references, sibling metadata, wrappers, or role-routing docs need synchronized updates.
Update them only to avoid contradiction, orphan references, or stale behavior.
If new evidence makes the chosen option invalid, explain it and ask whether to reopen the choice.
Carry any `>50`-line-file justification into the final report.
Validate the changed files or relevant checks before finishing.

## Output

Before choice, return `Resolved role`, `Editable roots`, `Case summary`, `Root cause`, `Classification`, `Options`, `Recommendation`, and `Choice needed`.
`Case summary` must include the session-backed evidence, the current context gap, and the target behavior.
In `Options`, keep the order `minimal`, `systemic`, `optimal`, then any extras.
After implementation, return `Implemented option`, `Changed files`, `Validation`, `Impact check`, and optional `Long-file justifications` or `Notes`.
Do not invent missing evidence.
