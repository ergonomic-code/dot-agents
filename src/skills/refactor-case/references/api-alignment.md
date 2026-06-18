# API-driven test alignment

- If a production refactor changes a production API used by tests inside the target boundary, update the affected tests to the new API in the same iteration.
- Keep those test changes minimal and limited to API-alignment fallout from the approved production refactor.
- Do not add compatibility branches, alias files, adapter layers, or legacy entrypoints just to avoid updating affected tests.
- After production changes and the required API-alignment test updates are in place, stop for review instead of continuing with more test or production refactoring.
