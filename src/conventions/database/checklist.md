---
keywords:
  - database
  - checklist
---

# Database checklist

- Are database state-dependent mutations atomic through one operation or explicit transaction locking or isolation instead of application-level read-check-write?
- Do transaction boundaries follow `./transaction-boundaries.md`, including its prohibition on external or potentially long work except explicitly allowed local-broker publication?
