---
keywords:
  - spring
  - checklist
---

# Spring test checklist

- Are Spring bean override mocks and spies absent?
- When a class-level double is required, is its graph built from real application-context collaborators with only the simulated dependency substituted?
- Are collaborators resolved locally through the inherited application-context helper rather than injected into the test class?
- If the shared test superclass lacks that helper, is it added there?
- If framework proxies are required, is the explicit graph registered through existing test infrastructure without overriding beans?
