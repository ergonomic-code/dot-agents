# Tasks

## Overview

Framework work is organized around tasks.

Resolve the task number primarily from explicit user input.
If the user gave exactly one output path, task dir, or file inside a task dir, use that task dir.
If cwd is inside devlog/<task-id>-<slug>, use that ancestor.
Valid explicit signals include a dangling number, number in parentheses at the end of a line, a line that contains only the number, or a number placed after a skill reference.

If the user did not explicitly name a task number, compare the request meaning with the current git branch and the current task slug in the devlog.
If they match with high confidence, state in chat that you inferred the active task implicitly and continue within that task.

If an explicit task number is known and no task directory was given, search direct children of ./devlog for a basename equal to <task-id> or starting with <task-id>-.
If exactly one match exists, use it as the active task directory.
If zero matches exist, state that no active task directory was resolved and continue without an active task unless the current skill requires one.
If several matches exist, stop and ask which task directory to use.

If no task directory can be resolved with high confidence, state that in chat and continue without an active task.

## Task Memory

Task memory is stored under `./devlog` relative to the repository root.

Active task memory directories use the `<task-num>-<slug>` naming pattern.

Completed and paused tasks live under `done` and `on-hold` respectively.

Unless the prompt explicitly says otherwise, add new task documentation and context files to the task directory.

### File Codes

Each file in a task directory should have a filename prefix that identifies its artifact type:

- 010 - task statement.
  Requirements in brief form, additional resources with examples, datasets, and similar inputs.
- 020 - current-state description.
  Artifacts that describe the current state, such as current API, current test cases, current architecture, and similar context.
- 030 - target-state description.
  Artifacts that describe the target solution, such as the solution brief, target API, new test cases, target architecture, and similar design context.
- 040 - implementation working files.

### Standard Task Files

Every task should have at least these three files:

- 010-task-brief.md - task statement.
- 030-solution-brief.md - brief for the overall solution direction.
- todo.md - list of completed and pending subtasks.

Depending on the task type and nature, a task may also have:

- 020-code-anchors.md - links to relevant source-code files.
  Target source files to change, example files, tests for the changed code, files for adding new tests, and similar code anchors.
- 020-api-current.md - current REST API in Human-Readable REST API Format.
- 020-test-cases-current.md - current relevant test cases.
- 030-api-new.adoc - target REST API.
- 030-test-cases-new.md - new test cases.
