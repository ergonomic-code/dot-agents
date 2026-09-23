---
keywords:
  - kotest
  - checklist
---

# Kotest checklist

- Do collection-property checks use Kotest inspectors when appropriate instead of manual iteration?
- Are property-specific assertions used instead of `shouldBe <boolean const>`?
- Does async waiting use `eventually` rather than `Thread.sleep`?
