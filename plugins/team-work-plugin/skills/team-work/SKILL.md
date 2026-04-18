---
name: team-work
description: Decompose the current session's jobs-to-be-done into a parallelizable task plan for an agent team. Assigns each task a model tier (haiku / sonnet / opus) and a specialist subagent when one fits. Organises work into dependency waves with no shared-file edits inside a wave to avoid merge conflicts. Use this skill whenever the user says "team this up", "use a team", "use agent teams", "delegate this", "split this work", "parallelize this", "fan this out", "divide and conquer", or otherwise asks to coordinate multiple agents on work already discussed in the session. Also trigger when the user says a task is big and wants help farming it out, or when they explicitly invoke /team-work.
---

# team-work

Turn what's been discussed in the current session into a clean, shareable plan for a team of agents — then run it.

## When to use

Trigger on phrases like:
- "team this up", "use a team", "use agent teams", "use teams"
- "delegate this", "split this work", "parallelize this", "fan this out"
- "divide and conquer", "hand this off to agents"

Also trigger when the user is clearly about to hand off a pile of discussed work and wants it organised.

The **source of truth** for jobs-to-be-done is the **current conversation**. If the user points at a GitHub issue, plan file, or branch, layer that in — but don't go hunting for it uninvited.

## What the skill produces

A single markdown plan with two things:

1. **Task graph** — every atomic task with: id, one-sentence goal, complexity tier, assigned model, assigned subagent (if any), file scope, and prerequisites.
2. **Execution waves** — tasks grouped so everything in a wave can run in parallel without touching the same files or depending on each other.

Then: confirm → spawn the agents.

## Operating modes

Pick based on how confident the plan is:

| Situation | Mode |
|---|---|
| Plan is obvious, small, low-risk (≤3 tasks, no shared files, clear scope) | **Act** — build plan, show it briefly, spawn immediately |
| Plan has ambiguity, >3 tasks, shared files, or destructive steps | **Confirm** — present the plan, ask for sign-off, then spawn |
| User explicitly says "just plan it" / "don't spawn yet" | **Plan only** — write the plan, stop |

When in doubt, confirm. Cost of pausing is a sentence; cost of a bad fan-out is wasted runs.

## Step 1 — Extract the JTBD

Read the conversation and list everything the user has expressed a desire to get done. Be concrete: each item should name a deliverable, not a theme.

Bad: "Improve the dashboard"
Good: "Add empty-state card to Base tab streak section"

If the session is vague, ask **one** clarifying question before drafting. Don't interrogate.

## Step 2 — Decompose into atomic tasks

A task is atomic if:
- A single agent can own it start-to-finish
- It has a clear "done" signal (file saved, test passes, answer returned)
- It doesn't require coordination mid-flight with another task

If a task isn't atomic, split it. If two tasks are both tiny and touch the same area, merge them — the overhead of spawning an agent isn't free.

## Step 3 — Assign complexity and model

Use this heuristic. Set `thinking`/effort to match.

| Tier | Model | Thinking | Use for |
|---|---|---|---|
| **S** | `haiku` | low | Lookups, single-file reads, mechanical renames, file moves, simple find/replace, formatting, running a known command and reporting output, summarising a file |
| **M** | `sonnet` | medium | Typical feature work, multi-file edits, focused refactors, writing tests for existing code, implementing a well-specified component, fixing a known bug |
| **L** | `opus` | high | Architecture decisions, cross-cutting refactors, ambiguous or novel problems, tricky debugging with unclear root cause, design of new systems, security-sensitive review |

Bias toward the cheaper tier when genuinely uncertain — haiku failing fast is cheaper than opus doing trivial work. But don't send opus-shaped problems to sonnet.

## Step 4 — Pick the right subagent

Before defaulting to `general-purpose`, check if a specialist fits. Specialists carry domain context that would otherwise need to be re-derived.

Process:
1. Check the agent list available in this environment (Agent tool's `subagent_type` param).
2. For each task, match on domain keywords: BJJ content → `bjj-*` family; iOS/SwiftUI → `ios-swift-expert` / `bjj-ios-engineer-inherit`; data pipeline → `bjj-data-engineer-*`; UI review → `grapla-ui-reviewer`; Swift navigation → `swift-navigation-expert`; typography → `typography-grapla-expert`; broad codebase exploration → `Explore`; planning only → `Plan`.
3. **Simple tasks don't need specialists.** A haiku-tier lookup runs fine on `general-purpose`. Specialists earn their seat when domain nuance matters.
4. Respect the agent's own model preference if its definition pins one — only override when the task clearly warrants it.

If no specialist fits, use `general-purpose` with the chosen model tier.

## Step 5 — Build dependency waves

Group tasks into waves. Rules inside a wave:

1. **No task depends on another task in the same wave.**
2. **No two tasks edit the same file.** If they do, split across waves — even if they're logically independent. Merge conflicts from parallel agents are painful.
3. **Read-only tasks are always safe to parallelize** with each other and with writes (as long as they don't need the write's output).

A wave can be a single task — that's fine when a blocker must land first.

## Step 6 — Present the plan

Use this template:

```markdown
# Team plan: <short title>

## Tasks
- **T1** — <goal>. Tier: S/M/L. Model: haiku/sonnet/opus. Agent: <subagent_type>. Files: <paths/globs>. Deps: none | T?, T?
- **T2** — ...

## Waves
- **Wave 1** (parallel): T1, T3, T5
- **Wave 2** (after W1): T2, T4
- **Wave 3** (after W2): T6

## Notes
<anything the user should flag or override before spawning>
```

Keep it tight. This is a briefing, not a dissertation.

## Step 7 — Spawn

Unless in plan-only mode:

- Spawn every task in a wave in **one message**, parallel `Agent` tool calls.
- Wait for the wave to complete before starting the next (foreground is fine; if tasks are truly independent and long, background is OK).
- Each agent's prompt must be **self-contained** — it won't see the conversation. Include: what to do, why it matters in context, file paths with line numbers when you have them, constraints from CLAUDE.md / CODESTYLE.md that apply, expected output shape, length cap when useful.
- Don't write "based on your research, implement it." — push concrete instructions, not synthesis.

After each wave, briefly report what landed and any surprises before kicking the next wave.

## Guardrails

- **Never spawn destructive actions in parallel without confirmation** — DB migrations, `git push`, force-pushes, deletions, external API calls with side effects. Those go in their own wave with user sign-off.
- **Respect the project's git flow** — per Grapla CLAUDE.md, no pushes to main; fan-outs land on feature branches or `develop`.
- **If agents need to write to the same area, serialize them.** Parallel edits to overlapping files end in tears.
- **Don't spawn agents for trivial work you can do inline faster.** A single-file edit doesn't need a subagent — the cold-start cost outweighs the parallelism.
- **Stay inside available agent types.** The Agent tool lists them; don't invent names.

## Example

User has spent the session discussing: adding an empty state to the Base tab streak card, renaming `StreakService` → `StreakTracker` across the iOS code, and writing a data-pipeline validator for a new position field.

Plan:

```markdown
# Team plan: Base tab streak + data validator

## Tasks
- **T1** — Rename StreakService → StreakTracker across grapla/. Tier: S. Model: haiku. Agent: general-purpose. Files: grapla/**/*.swift. Deps: none.
- **T2** — Add EmptyStateCard to Base tab streak section when no sessions logged. Tier: M. Model: sonnet. Agent: bjj-ios-engineer-inherit. Files: grapla/Features/App/Views/BaseTab*.swift. Deps: T1.
- **T3** — Add Zod validator for new `lever_points` field in position schema. Tier: M. Model: sonnet. Agent: bjj-data-engineer-inherit. Files: data/schemas/seed-models/position/enrichment-fields.ts, data/sources/positions/*.json sample. Deps: none.

## Waves
- **Wave 1** (parallel): T1, T3
- **Wave 2** (after W1): T2

## Notes
T2 waits on T1 because the streak view references the renamed type. T3 is fully independent of the iOS work.
```

Then confirm and spawn Wave 1 as two parallel Agent calls.
