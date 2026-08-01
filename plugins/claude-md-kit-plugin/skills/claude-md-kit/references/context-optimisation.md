## Context Optimisation

Every token your code or docs consume in an agent's context window is a token unavailable for reasoning. Optimize accordingly:

- Semantic compression — consolidate related tools/functions behind a single dispatcher routed by intent, instead of N granular ones.
- Layered context loading — surface summaries first, drill into detail on demand; never dump full project state upfront.
- Token-aware docs — dense and scannable, no filler prose. `"JWT auth with refresh rotation"`, not `"The authentication module is responsible for handling all aspects of user authentication within our application."`
- Structured output — functions consumed by agents return typed objects, not human-readable prose strings.
- Context boundaries as architecture — design modules so an agent can work within one without loading adjacent ones; co-locate types, minimize cross-module imports.
- Paginate by default — any function that could return a large result set supports `limit`/`offset`.
