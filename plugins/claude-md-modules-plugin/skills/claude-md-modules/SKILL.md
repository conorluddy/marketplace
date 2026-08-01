---
name: claude-md-modules
description: Compose or extend a project's CLAUDE.md from a library of stack-agnostic, composable prompt-segment modules (naming, error handling, testing, agentic patterns, a condensed spec-speak, etc.) stored as standalone files under references/. Use this skill whenever the user wants to bootstrap a new CLAUDE.md, add a specific convention module to an existing one, or audit a CLAUDE.md against the standard module set. Also use when the user says "compose a CLAUDE.md", "give me a starter CLAUDE.md", "add the [topic] module", or "what conventions are we missing".
---

# CLAUDE.md Modules

A library of short, stack-agnostic prompt segments — each one a self-contained `.md` file under `references/` covering one convention (naming, error handling, testing, etc.). Modules work two ways: paste one directly into a project's `CLAUDE.md`, or ask this skill to assemble several into a coherent file.

## Module conventions

- One file per convention area, named `<topic>.md` (e.g. `naming.md`, `error-handling.md`).
- Stack/language agnostic — no framework-specific advice.
- Short enough to paste directly into a CLAUDE.md section (guideline: under ~40 lines each).
- Phrased as direct instructions to the agent ("Follow these conventions…", "Use `Result<T, E>` for…"), not as passive documentation of rules.
- No frontmatter — plain markdown, since these are meant for direct copy-paste as well as programmatic composition.

## Workflow

1. Read the target project's existing `CLAUDE.md` (if any) and note what's already covered, and identify its language/stack (package manifests, file extensions, etc.).
2. List available modules from `references/README.md`. Ask the user which to include via `AskUserQuestion` — a single `multiSelect: true` question, one option per module, its description as the option description. Pre-select nothing; let inferred relevance (from step 1's gaps) inform the recommended option, not silently decide it.
3. Ask how selected modules should be applied via `AskUserQuestion` (single-select, one question):
   - **Adapt to this stack (Recommended)** — rewrite each module's examples, type names, and idioms to match the project's actual language/framework/tooling while preserving the underlying rule.
   - **Paste verbatim** — keep each module's generic wording unchanged.
   - **Decide per module** — ask a follow-up, one option-set per module (batched up to 4 per `AskUserQuestion` call), since some modules may warrant adapting and others don't.
4. Write the chosen modules into the target file under sensible section headings. When adapting, keep the rule intact and only translate stack-specific surface details — e.g. `Result<T, E>` becomes the target language's idiomatic equivalent (Go's `(value, error)`, Rust's `Result<T, E>`, a discriminated-union return in TypeScript); don't weaken or drop the underlying constraint.
5. Flag any module whose advice conflicts with something already in the project's CLAUDE.md rather than silently overwriting it.

## Available modules

See `references/README.md` for the current list (written and planned).
