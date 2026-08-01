## Agentic Patterns

Design APIs and operations for both human and agent callers:

- Idempotent operations — use `ensure*` naming, and make every mutation safely repeatable.
- Explicit state machines — model distinct phases as discriminated unions, never implicit boolean flags.
- Machine-parseable errors — discriminated unions with `code`, `message`, `retryable` fields, not bare strings.
- Atomic changes — make each function/commit independently testable without understanding the whole system.
- Convention over configuration — consistent naming (`*.test.ts`, `*.types.ts`), predictable directory structure, standard CRUD patterns.
- Contract-first design — define types before implementation; types are the cheapest documentation.
- Observable side effects — return `{ data, changes[], warnings[] }` from mutations so callers (including agents) can verify what happened.
