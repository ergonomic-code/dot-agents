# Test Development

In this mode, change only tests and test-supporting code.
This includes test cases, object mothers, test APIs, HTTP APIs, fixtures, and fixture presets.

Production code is outside this mode unless the invoking workflow explicitly grants a bounded compile-only production write set for one selected test.
Under that exception, change only the production surface required for that test to compile and do not add or change production behavior.

Test semantics may change when required by the task.
This includes adding cases, removing cases, tightening verification, or changing existing verification.

Constraints:

- Without that explicit authorization, stop if the task requires production edits.
- If the selected test cannot compile without production behavior, stop and leave that behavior to production code development.
