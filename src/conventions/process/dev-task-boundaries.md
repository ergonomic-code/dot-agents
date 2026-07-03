# Development task boundaries

Each coding slice has two independent axes:

- change mode: development or refactoring;
- write set: production code or tests.

Before editing, classify the request on both axes.

Load and apply exactly one matching rule file:

- test development -> `./tests-development.md`
- test refactoring -> `./tests-refactoring.md`
- production code development -> `./production-code-development.md`
- production code refactoring -> `./production-code-refactoring.md`
