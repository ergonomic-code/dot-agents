# Pair mode multipart request

## Method POST /users/{userId}/avatar

### Before

```text
  Method POST /users/{userId=String:UUID}/avatar

  >
    Body:
      multipart/form-data
        file: Binary
        meta: <AvatarMeta>

  <
*   200
      none
```

### After

```text
  Method POST /users/{userId=String:UUID}/avatar

  >
    Body:
      multipart/form-data
        file: Binary
        meta: <AvatarMeta>

  <
*   200
      none
```
