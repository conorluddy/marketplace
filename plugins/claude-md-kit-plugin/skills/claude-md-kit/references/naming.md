## Naming

Follow these naming conventions throughout the codebase:

- Be specific — `activeUsers` not `users`, `httpTimeoutMs` not `timeout`.
- Include units in the name — `delayMs`, `maxRetries`.
- Spell words out — no abbreviations: `customer` not `cust`, `configuration` not `cfg`.
- Prefer domain language over technical abstractions.
- Prefix booleans with `is`/`has`/`can`/`should` — `isValid`, `hasPermission`, `canEdit`, `shouldRetry`.
- Name functions with verbs that describe the action — `validateEmailFormat()` not `checkEmail()`.
