# HTTP JSON API error response body format

- Canonical HTTP JSON API error bodies follow Problem Details for HTTP APIs.
- Use the standard members `type`, `title`, `status`, `detail`, and `instance` when they apply.
- `timestamp` may be added as an ISO 8601 error occurrence time.
- Project context may define a custom or legacy error body type for this pattern.
- If project context defines such a type, treat it as the project error response body type and do not migrate it unless requested.
