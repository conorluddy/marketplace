# Code Style Guide

> **Core Principle**: Context is finite. Every token — code, comment, structure — competes for limited attention. Maximize signal, minimize noise. Write for two audiences: humans with limited working memory and AI agents with bounded context windows.

## Philosophy

The optimal code is the minimum necessary to solve the problem correctly. Every additional line is debt.

- **Progressive Disclosure**: Structure code layer-by-layer. Readers grasp high-level flow immediately, drilling into details only when needed.
- **Self-Documenting**: Names eliminate need for comments. Comments explain "why," never "what."
- **Aggressive Minimalism**: Simplest correct solution. No speculative abstractions.
- **AHA Over DRY**: Avoid Hasty Abstractions. Wait for the 3rd duplication before extracting.

## Progressive Disclosure

Code should work like a map: zoom out for the big picture, zoom in for street-level detail. Each zoom level should be self-sufficient.

- **Level 0**: Directory structure tells you what exists
- **Level 1**: Index/module file tells you what it can do (exports only)
- **Level 2**: Function signature tells you the contract
- **Level 3**: Implementation tells you how

**File-level**: Every file answers "what is this?" in its first 10 lines. Order: doc comment → types → public API → private helpers.

**Anti-patterns**:
- Premature depth: implementation details in README
- Flat disclosure: 500-line files with no hierarchy
- Inverted disclosure: helpers at top, public API buried
- Missing levels: jumping from directory listing to inline comments

## Naming

1. **Be specific**: `activeUsers` not `users`, `httpTimeoutMs` not `timeout`
2. **Include units**: `delayMs`, `maxRetries`
3. **No abbreviations**: `customer` not `cust`, `configuration` not `cfg`
4. **Domain language** over technical abstractions
5. **Boolean prefixes**: `isValid`, `hasPermission`, `canEdit`, `shouldRetry`
6. **Verbs for functions**: `validateEmailFormat()` not `checkEmail()`, `fetchActiveUsers()` not `getUsers()`

## Function Design

- **Single responsibility** — describable in one sentence
- **Explicit dependencies** — all inputs as parameters, no hidden global state
- **Type everything** — strict mode, no `any`
- **Guard clauses over nesting** — happy path unindented and visible
- **50-line guideline** — refactoring trigger, not hard limit

```ts
// Guard clauses — happy path clear
function processOrder(order: Order): Result<Receipt, ProcessError> {
  if (!order) return err('missing_order');
  if (order.items.length === 0) return err('empty_order');
  if (order.total <= 0) return err('invalid_total');
  return ok(completePayment(order));
}
```

## Error Handling

- **`Result<T, E>` types** for expected failures — errors belong in signatures, not hidden behind `throw`
- **Exceptions** only for truly unrecoverable situations (OOM, corrupted state)
- **Branded types** (`ValidatedEmail`, `UserId`) to validate at boundaries and carry proof through the type system
- **Never silently swallow** — log or propagate
- **Fail fast at boundaries** — validate inputs immediately
- **Actionable messages**: what failed, expected vs actual, how to fix

## File & Module Organization

1. Group by **feature/domain**, not file type (`authentication/`, `orders/`, `payments/`)
2. **Public API first**, helpers at bottom
3. **One major export per file** — `UserService.ts` exports `UserService`
4. **Co-locate tests** — `UserService.test.ts` next to `UserService.ts`
5. **300-line guideline** per file
6. **Minimal cross-module dependencies** — each module is a clean context boundary
7. Use **section comments** (`// === PUBLIC API ===`) for visual hierarchy

## Testing (Testing Trophy)

1. **Static Analysis** (foundation): strict types, lint
2. **Unit Tests** (narrow): pure functions, complex algorithms
3. **Integration Tests** (widest — most tests here): how pieces work together
4. **E2E Tests** (top): critical user journeys only

Rules:
- Test **behavior, not implementation**
- **One concept per test**
- **Clear names**: `test('user can add items to cart')`
- **80% coverage** on critical paths

## Observability

- **Structured logging only** — JSON with `request_id`, `user_id`, `duration_ms`, entity IDs
- Log at critical boundaries: external APIs, DB ops, auth decisions, errors
- One structured event per operation

## Agentic Coding Patterns

### Idempotent Operations
Agents retry. Every mutation should be safely repeatable. Prefer `ensure*` patterns.

### Explicit State Machines
Model distinct phases with discriminated unions, not implicit status flags.

```ts
type OrderState =
  | { status: 'draft'; items: Item[] }
  | { status: 'submitted'; items: Item[]; submittedAt: DateTime }
  | { status: 'paid'; items: Item[]; submittedAt: DateTime; paymentId: string };
```

### Machine-Parseable Errors
```ts
type AppError = {
  code: 'VALIDATION_FAILED' | 'NOT_FOUND' | 'CONFLICT' | 'UPSTREAM_TIMEOUT';
  message: string;
  field?: string;
  retryable: boolean;
};
```

### Atomic, Independently-Verifiable Changes
Structure work so each change is validated in isolation. Small commits, small PRs, small functions.

### Convention Over Configuration
Consistent patterns reduce search space. `UserService.ts` / `UserService.test.ts` / `UserService.types.ts`. Follow existing conventions; if none exist, establish and document one.

### Contract-First Design
Define types before implementation. Types are the cheapest, most scannable documentation.

### Observable Side Effects
Mutations return `{ data, changes[], warnings[] }` so callers (and agents) can audit what happened.

## Context Optimisation & Token Economics

Every token an agent reads is a token it can't use for reasoning.

- **Semantic compression**: N granular tools → 1 dispatcher routed by intent
- **Layered context loading**: summaries first, drill-down on demand
- **Token-aware docs**: dense and scannable, no filler prose, no repetition
- **Structured output**: parseable types, not prose
- **Context boundaries as architecture**: each module works without loading siblings
- **Paginate by default**: any large result set supports `limit`/`offset`

### Compression reference

| Strategy | Savings |
|---|---|
| Semantic dispatchers (N tools → 1) | ~(N-1)k tokens |
| Layered loading (full dump → summary + on-demand) | ~48k idle tokens |
| Dense docs vs narrative | ~50% |
| Co-located types | fewer file loads |
| Summary-first returns | 60-90% per call |
| Discriminated union errors | eliminates string parsing |

## Project Navigation

1. **CLAUDE.md / README.md at root** — system overview, entry points, setup (<200 lines)
2. **README.md per major module** — purpose, key decisions, gotchas
3. **Section comments** in files — group related code
4. **Function/class docs** — purpose, non-obvious APIs
5. **Inline comments** — only for "why" decisions

## Anti-Patterns (fast reference for review)

- Premature optimization — measure first
- Hasty abstractions — wait for 3rd duplication
- Clever code — simple beats compact
- Silent failures — log and propagate, never swallow
- Vague interfaces — `process(data: any): any`
- Hidden dependencies — globals, singletons, ambient imports
- Nested conditionals — use guard clauses
- Comments describing *what* — rename things instead
- Premature generalization — build for today's requirements
- Token bloat — functions returning everything when callers need summaries
- Inverted disclosure — helpers at top, public API buried
- Flat files — 500 lines with no visual hierarchy
- Leaky context boundaries — modules importing heavily from siblings
- Eager context loading — full project dumps when summaries suffice

## Review Checklist (fast pass)

- Solves stated problem with minimal code?
- Understandable without extensive context?
- Errors actionable, never swallowed?
- Names specific, unambiguous, with units where applicable?
- Functions single-responsibility?
- Dependencies explicit in signatures?
- Critical paths tested?
- Mutations idempotent where applicable?
- Types define contracts before implementation?
- Works well with ~200 lines of surrounding context?
- Module understandable without loading siblings?
- Public APIs scannable in under 50 lines?
- Tool/function outputs structured, not prose?
- Docs token-dense, no filler?
- File follows progressive disclosure (types → public API → helpers)?
