---
keywords:
  - resources
  - lifetimes
---

# Resource lifetimes

- Unless an API explicitly transfers ownership, keep the complete acquire-use-cleanup lifecycle of a resource in one method.
- That method must clean up through `finally`, or delegate the complete lifecycle, including acquisition and cleanup, to a scoped helper.
- Callees inside the lifecycle may use the resource but must not clean it up.
