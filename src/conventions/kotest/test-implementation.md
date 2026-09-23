---
keywords:
  - kotest
  - tests
---

# Kotest test implementation

- Use Kotest inspectors (`forAll`/`forOne`/`forNone`) to verify that collection elements match a property.
- Avoid `shouldBe <boolean const>`; prefer an assertion that states the checked property.
- Do not use `Thread.sleep` to wait for events or async completion; use Kotest `eventually` instead.
