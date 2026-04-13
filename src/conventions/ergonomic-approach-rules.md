# Ergonomic Approach rules

## General rules

- Write code for new functionality or a bug fix only after adding a failing test that defines the expected behavior or reproduces the bug, and implement only the minimal change needed to make it pass.
- Extract duplication immediately after the second occurrence, except for test-case-local setup or assertions that improve test readability.
- Prefer boundary tests for behavior observable through an external entry point.
- Add a component test only when a boundary test cannot verify the behavior, or when the component test materially simplifies verification relative to the boundary alternative.
