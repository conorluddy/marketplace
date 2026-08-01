## Error Handling

- Use `Result<T, E>` types for expected failures (API calls, I/O, validation). Reserve exceptions for truly unrecoverable situations.
- Use branded types (`ValidatedEmail`, `UserId`) to validate at boundaries and carry proof through the type system.
- Never silently swallow an error — log it or propagate it.
- Fail fast at boundaries — validate inputs immediately.
- Write actionable error messages: what failed, expected vs actual, how to fix.
