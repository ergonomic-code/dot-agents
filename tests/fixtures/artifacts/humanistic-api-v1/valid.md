# API

## Method POST /users/{userId}

```text
* Method POST /users/{userId=String:UUID}?
    notify={Boolean}

>
  Body:
    <UserUpdate>

<
* 200
    <User>

  404
    none

Rules:
  - The user must exist.
```

```text
+ Model User =

  {
    "id": String:UUID,
+   "state": <UserState>
  }
```

```text
Enum UserState =

  ACTIVE
  DISABLED
```
