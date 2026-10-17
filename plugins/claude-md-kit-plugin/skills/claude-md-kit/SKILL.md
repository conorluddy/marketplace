---
name: claude-md-kit
description: Compose or extend a project's agent instructions file (AGENTS.md, or CLAUDE.md for Claude Code) from a library of stack-agnostic, composable prompt-segment modules (naming, error handling, testing, agentic patterns, a condensed spec-speak, etc.) stored as standalone files under references/. Use this skill whenever the user wants to bootstrap a new CLAUDE.md or AGENTS.md, add a specific convention module to an existing one, or audit one against the standard module set. Also use when the user says "compose a CLAUDE.md", "compose an AGENTS.md", "give me a starter CLAUDE.md", "add the [topic] module", or "what conventions are we missing".
---

# Agent Instructions Kit (CLAUDE.md / AGENTS.md)

A library of short, stack-agnostic prompt segments — each one a self-contained `.md` file under `references/` covering one convention (naming, error handling, testing, etc.). Modules work two ways: paste one directly into a project's `AGENTS.md` or `CLAUDE.md`, or ask this skill to assemble several into a coherent file.

## Module conventions

- One file per convention area, named `<topic>.md` (e.g. `naming.md`, `error-handling.md`).
- Stack/language agnostic — no framework-specific advice.
- Short enough to paste directly into an AGENTS.md or CLAUDE.md section (guideline: under ~40 lines each).
- Phrased as direct instructions to the agent ("Follow these conventions…", "Use `Result<T, E>` for…"), not as passive documentation of rules.
- No frontmatter — plain markdown, since these are meant for direct copy-paste as well as programmatic composition.

## Workflow

1. Read the target project's existing `AGENTS.md` / `CLAUDE.md` (if any) and note what's already covered, and identify its language/stack (package manifests, file extensions, etc.).
2. List available modules from `references/README.md`. Ask the user which to include with a structured question tool if one is available (Claude Code: `AskUserQuestion`), otherwise a plain numbered list — a single multi-select question, one option per module, its description as the option description. Pre-select nothing; let inferred relevance (from step 1's gaps) inform the recommended option, not silently decide it.
3. Ask how selected modules should be applied (single-select, one question):
   - **Adapt to this stack (Recommended)** — rewrite each module's examples, type names, and idioms to match the project's actual language/framework/tooling while preserving the underlying rule.
   - **Paste verbatim** — keep each module's generic wording unchanged.
   - **Decide per module** — ask a follow-up, one option-set per module (batched up to 4 per question call), since some modules may warrant adapting and others don't.
4. Write the chosen modules into the target file under sensible section headings. Default target: `AGENTS.md` (read by Codex and most agents). If the project uses Claude Code and has no `CLAUDE.md`, also create one containing only `@AGENTS.md`. If the project already has a `CLAUDE.md` and no `AGENTS.md`, extend `CLAUDE.md`. When adapting, keep the rule intact and only translate stack-specific surface details — e.g. `Result<T, E>` becomes the target language's idiomatic equivalent (Go's `(value, error)`, Rust's `Result<T, E>`, a discriminated-union return in TypeScript); don't weaken or drop the underlying constraint.
5. Flag any module whose advice conflicts with something already in the project's instructions file rather than silently overwriting it.

## Available modules

See `references/README.md` for the current list (written and planned).
