# Module library

Written:

- `spec-speak-condensed.md` — EARS shapes, RFC 2119 keywords, weak-word blacklist, ask-don't-invent, condensed from the `spec-speak` skill
- `naming.md` — identifier naming conventions
- `function-design.md` — single responsibility, guard clauses, dependency injection
- `error-handling.md` — Result types, branded types, fail-fast boundaries
- `file-organisation.md` — feature-based grouping, public-API-first, co-located tests
- `testing.md` — testing trophy, behaviour-first tests, coverage targets
- `observability.md` — structured logging, critical-boundary logging
- `agentic-patterns.md` — idempotency, state machines, machine-parseable errors, observable side effects
- `context-optimisation.md` — token-aware docs, layered context, semantic compression

Adapted from [conorluddy/Codestyle](https://github.com/conorluddy/Codestyle)'s CLAUDE.md. That source also has Philosophy, Project Navigation, Anti-Patterns, and Checklist sections not yet split into modules here — candidates for later.

Planned (candidates, not committed):

- `philosophy.md`
- `project-navigation.md`
- `git-workflow.md`

Each module is a standalone `.md` file, stack-agnostic, short enough to paste directly into a CLAUDE.md.
