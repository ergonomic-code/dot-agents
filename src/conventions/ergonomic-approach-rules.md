---
keywords:
  - ergonomic-approach
---

# Ergonomic Approach rules

## General rules

- For new functionality or a bug fix, keep test and production steps in one implementation plan: start by adding and running a failing test that defines the expected behavior or reproduces the bug, then make the minimal production change needed to pass it; implement in that order.
- When the same responsibility is implemented a second time, immediately centralize its complete shared behavior rather than only a common inner fragment, including when separate code paths express it differently, except for test-case-local setup or assertions that improve test readability.
- Design non-trivial operations in balanced form: read with queries, calculate with I/O-free pure queries over logical inputs, then write with commands.
- Prefer boundary tests for behavior observable through an external entry point.
- Add a component test only when a boundary test cannot verify the behavior, or when the component test materially simplifies verification relative to the boundary alternative.
