---
name: code-review
description: Review code against Conor's style guide — naming, progressive disclosure, function design, error handling, agentic patterns, and token economics. Use this skill whenever the user asks for a code review, says things like "review this", "check my code", "look over this PR", "roast this", asks for feedback on a diff/branch/file, or after finishing an implementation and wants a pass before commit. Also trigger proactively after substantial code changes where a self-review would catch issues. Produces a structured findings report grouped by severity (blocker / major / minor / nit) with file:line references and concrete suggested fixes — not generic platitudes.
---

# Code Review

Review code against the style guide in `references/style-guide.md`. Produce a structured, severity-tagged findings report that a human can skim in 30 seconds and an agent can act on directly.

## What gets reviewed

Default scope, in order of preference:
1. **Explicit target** — if the user names a file, PR, branch, or diff, review exactly that
2. **Current branch vs `main`** — `git diff main...HEAD` when reviewing "my changes" / "this branch"
3. **Uncommitted changes** — `git diff HEAD` + `git diff --staged` when reviewing "what I just wrote"
4. **Ask** — only if genuinely ambiguous. Don't ping-pong.

Skim the diff first, then read surrounding context for any file with non-trivial changes. A review that misses the calling context misses half the bugs.

## Output format

Always use this structure. Omit sections that are empty — don't pad with "no issues found".

```
# Code Review — <what was reviewed>

**Summary**: <1-2 sentences. What changed, overall shape of the feedback.>

## Blockers
<Bugs, security issues, broken contracts, data loss risks. Must fix before merge.>

- **<file>:<line>** — <what's wrong>. <why it matters>. <concrete fix>.

## Major
<Style-guide violations with real cost: hidden dependencies, swallowed errors, leaky boundaries, wrong abstraction.>

## Minor
<Naming, guard clauses, section ordering, missing types. Worth fixing, not urgent.>

## Nits
<Taste-level preferences. Author may ignore.>

## Praise
<1-3 specific things done well. Not filler — skip if there's nothing genuine.>
```

Each finding is **one bullet, one issue, one fix**. If you're writing a paragraph, split it.

## What to look for

Work through these lenses. Not every lens applies to every review — skip ones that aren't relevant rather than manufacture findings.

### 1. Correctness (blocker-tier)
- Off-by-one, null/undefined handling, race conditions, unawaited promises
- Silent error swallowing — `catch {}`, discarded `Result.error`, ignored rejections
- Mutations on shared/aliased state
- Idempotency: will a retry duplicate work or corrupt state?
- Boundary validation: is untrusted input validated before it enters the type system?

### 2. Style-guide adherence
Cross-reference `references/style-guide.md`. The high-value checks:
- **Naming**: vague (`data`, `result`, `temp`), missing units (`timeout` vs `timeoutMs`), abbreviations (`cfg`, `cust`), booleans without prefix (`valid` vs `isValid`), nouns where verbs belong (`email()` vs `sendEmail()`)
- **Guard clauses**: nested conditionals that could be flattened, happy path buried >2 levels deep
- **Progressive disclosure**: helpers above public API, types scattered instead of grouped, file that doesn't answer "what is this?" in first 10 lines
- **Explicit dependencies**: globals, singletons, ambient imports; things a function uses that aren't in its signature
- **Error handling**: `throw` where `Result` fits, `any`/`unknown` leaking, opaque messages (`"Validation failed"`)
- **Single responsibility**: functions doing two things, `and` in the name, >50 lines without a clear reason

### 3. Agentic / context hygiene
This is where most reviews miss things:
- **Leaky context boundaries**: module imports from 4+ siblings to do one job
- **Token bloat**: functions returning the kitchen sink when callers want a summary
- **Unstructured outputs**: prose where a discriminated union or typed object belongs
- **Missing machine-parseable errors**: error strings instead of `{ code, retryable }`
- **Convention drift**: new code that doesn't match established patterns in the same module

### 4. Minimalism
- Premature abstraction (1-2 call sites, not 3+)
- Speculative generality (options/flags nothing uses)
- Dead code, unused exports, commented-out blocks
- Comments that explain *what* instead of *why* (rename the thing instead)
- Backwards-compat shims for code that isn't shipped yet

### 5. Testing
- Missing tests on new behaviour; tests that assert implementation not behaviour
- Tests coupled to internals (mocking private methods, asserting call counts)
- One test doing five things
- Golden-path-only: no failure case coverage

### 6. Security & side effects (blocker if present)
- SQL/command/template injection, unescaped user input reaching a sink
- Secrets in code, logs, or commit
- Auth/authz checks missing or bypassable
- Broad `catch` that hides security-relevant failures
- Unintended network calls, file writes, or process spawns

### 7. Commit & PR hygiene (if reviewing a branch/PR)
- Multiple unrelated concerns in one commit/PR
- Commit messages that say *what* not *why*
- Drive-by refactors mixed with the core change

## Calibrating severity

Err toward **fewer, sharper findings** over exhaustive lists. A 40-item review gets ignored; a 6-item review gets acted on.

- **Blocker**: ship this and something breaks — data, auth, contracts, runtime
- **Major**: real maintenance cost, will bite within weeks
- **Minor**: cumulative drag — worth a cleanup pass
- **Nit**: preference, subjective, author's call

If you find yourself marking everything Major, recalibrate. If everything is Nit, you're not looking hard enough.

## What NOT to do

- **Don't rewrite the code yourself** unless the user asked. Point at the problem and suggest the fix direction — let the author own the edit.
- **Don't file-by-file walk** through everything. Group findings by severity, not by file.
- **Don't invent issues** to pad the review. Empty sections are fine. "Looks good" is a valid outcome.
- **Don't quote huge blocks** of the reviewed code back at the author. They wrote it. A `file:line` ref is enough.
- **Don't moralize**. "This is bad practice because..." reads worse than "This will break when X happens — do Y instead."
- **Don't review stylistic preferences outside the guide** as if they were rules. Mark taste items as Nits and move on.

## Process

1. **Establish scope**: which files/diff. If unclear, default to `git diff main...HEAD`.
2. **Skim the full diff once** before forming opinions. Avoid first-impression tunnel vision.
3. **Read surrounding context** for any file with meaningful changes — the call sites, the types, the tests.
4. **Consult `references/style-guide.md`** when a finding touches a specific principle; cite the section so the author can drill in.
5. **Draft findings**, then cut by 30% — remove anything that wouldn't survive the author asking "so what?".
6. **Output the report** in the format above.

The goal: the author reads the review, knows exactly what to do next, and feels the reviewer actually understood the code.
