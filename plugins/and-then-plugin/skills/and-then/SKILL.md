---
name: and-then
description: "Ambiguity-first planning — exhaustively identify and resolve unknowns before committing to a plan. Gathers project context silently (CLAUDE.md, recent PRs, codebase), extracts every ambiguity categorized as blocking or refinement, resolves what it can from code, then asks the user targeted questions until blocking ambiguity hits zero. Outputs issues, epics, or plan files matched to the scope of the work. Use this skill whenever the user wants to plan a feature, scope out work, think through a problem before building, asks 'what would it take to...', says 'let's plan', 'scope this', 'think this through', 'what are we missing', 'before we start', or describes something they want to build and you sense there are unresolved questions that would lead to rework. Also use when a request feels underspecified and jumping straight to implementation would be premature."
---

# And Then — Ambiguity-First Planning

No plan survives unasked questions. This skill exhausts ambiguity before committing to a plan — preventing rework, missed edge cases, and scope surprises.

## Why This Exists

The most expensive line of code is the one you write before understanding the problem. Developers (and AI agents) have a bias toward action — start building, figure it out along the way. That works for small tasks but fails catastrophically for anything with moving parts. This skill forces the uncomfortable but valuable pause: "What don't we know yet?"

The goal isn't to ask endless questions. It's to identify the specific unknowns that would derail implementation, resolve as many as possible from the codebase itself, and only burden the user with questions that genuinely need their input. When the blocking unknowns are resolved, produce a plan that's grounded in reality.

## Workflow

### Phase 1: Silent Context Gathering

Before asking the user a single question, build a mental model of the project and the request. This phase is silent — no output to the user.

#### What to gather

1. **Project context** — Read CLAUDE.md, MEMORY.md, and any domain-specific docs they reference. Understand the project's architecture, conventions, and current state.

2. **Recent work** — Understand what's been happening lately:
   ```bash
   gh pr list --state merged --limit 10 --json title,number,mergedAt,headRefName
   git log main --oneline -15
   ```

3. **Overlapping work** — Check for existing issues, plans, or in-progress branches that touch the same area:
   ```bash
   gh issue list --state open --limit 30 --json title,number,labels,body
   ```
   Also check for plan files (e.g., `~/.claude/plans/`) or similar project-management artifacts.

4. **Codebase exploration** — Glob and grep the areas the request touches. Read key files — models, services, views. Understand the current state before proposing a future state.

#### Depth control

Start shallow. Go deeper only where ambiguity concentrates. If the request touches "the technique editor," read the technique editor. Don't read every file in the project. Use Explore agents for broad investigation when a shallow scan reveals the request is more cross-cutting than it first appeared.

The point of this phase is to enter the conversation informed — so your questions are sharp and your assumptions are grounded, not generic.

### Phase 2: Ambiguity Extraction

Analyze the user's request against everything you gathered. Identify every point of ambiguity, categorized:

| Category | What's unclear |
|----------|---------------|
| **Requirements** | What exactly should this do? Expected behavior, acceptance criteria |
| **Technical** | How should this be built? Patterns, services, models, data flow |
| **Scope** | What's in vs out? Where are the boundaries? What's v1 vs follow-up? |
| **Dependencies** | What else is affected? What needs to exist first? What breaks? |
| **UX** | What does the user see? Edge cases, empty states, error states, flows |
| **Domain** | Terminology, business rules, domain-specific constraints |

Tag each ambiguity as one of:
- **Blocking** — Cannot produce a valid plan without resolving this. Implementation would stall or require rework.
- **Refinement** — Has a sensible default. Nice to confirm, but a reasonable assumption can stand.

#### Resolve from code before asking

This is the skill's most important behavior. For each ambiguity, attempt to resolve it from the codebase first:

- Does the component/service/pattern already exist? Read it.
- How was a similar feature implemented? Find it.
- What's the current data model? Check the schema.
- Is there test coverage? Grep for it.

When you resolve something from code, record it transparently:
> "I was going to ask about X, but I found Y in `path/to/file:42`, so I'm assuming Z."

This builds trust and lets the user correct wrong assumptions without being asked a question they'd find frustrating ("you could have just looked!").

Only surface ambiguities to the user that genuinely cannot be resolved from code.

### Phase 3: Present Tracker & Resolution Loop

Present the ambiguity tracker to the user, then begin asking questions to resolve the remaining unknowns.

#### Tracker Format

Render this at the start, and update it after each round of questions:

```
## Ambiguity Tracker (N resolved, N blocking, N refinement)

### Blocking
- [x] ~~Which data model handles X?~~ → Found in Position.swift:89
- [ ] What should happen when the user has no sessions?
- [ ] Does this replace the existing flow or sit alongside it?

### Refinement
- [x] ~~Preferred animation style?~~ → User: "match existing transitions"
- [ ] Empty state copy/messaging

### Resolved from Code
- ~~Does a query service exist for X?~~ → Yes, EntityListService (Services/Query/EntityListService.swift)
- ~~What's the current navigation pattern?~~ → GraphRouter with recents (Shared/Navigation/GraphRouter.swift)
```

The tracker is alive — items get added as new ambiguity emerges from answers, and crossed out as things get resolved. It's not locked to the initial extraction.

#### Question rules

1. **1-3 atomic questions per round.** Never overwhelm. Group related questions from the same category.

2. **Show your reasoning.** Explain why you're asking — what you found, what you checked, what you're unsure about. Context makes questions easier to answer.

3. **Challenge assumptions.** If the user said something that conflicts with codebase reality, say so directly: "You mentioned X, but the codebase currently does Y — should we change Y, or did you mean something different?"

4. **Surface risks proactively.** Don't wait to be asked. "This touches Z which has no tests," "This would require changing a shared component used by 5 views," "This data migration would affect all existing users."

5. **Explore edge cases.** "What happens when this fails?" / "What if the list is empty?" / "What about the user's first time seeing this?"

6. **Question scope creep.** "Is X actually needed for v1, or is it a follow-up?" Prefer shipping smaller things sooner.

#### The adversarial edge

Be collaborative — you're on the same team. But be thorough in a way that prevents rework:

- Challenge assumptions that conflict with codebase reality
- Point out risks: untested areas, shared components, data migration concerns
- Ask "what happens when this fails/is empty/times out?"
- Question scope creep: "Is X needed for v1, or is it a follow-up?"
- Suggest how work should be broken up — prefer atomic PRs and focused tickets
- Stress-test the happy path: "You described the success case — what's the failure mode?"

Don't block on stylistic disagreements or purely theoretical concerns. Focus on things that would actually cause rework or bugs.

### Phase 4: Output

#### Exit triggers

The resolution loop ends when:

- **All blocking ambiguities are resolved** — you propose "I think we're clear on the blocking questions" and the user confirms
- **User signals readiness** — "plan it," "LFG," "this will do," "good enough," or similar. Confirm their intent before proceeding.
- **User can exit anytime** — if blocking ambiguities remain, flag them as **open risks** in the output rather than refusing to proceed

#### Scope inference

Infer the right output format from the scope of the work:

| Signal | Likely Output |
|--------|---------------|
| Small — fits in 1 PR, single session of work | Single issue with DoD, affected files, risks |
| Medium — 2-3 related PRs | Plan file or small set of linked issues |
| Large — multi-PR, cross-domain | Epic with atomic child issues |

Offer your opinion on how the work should be broken up. Prefer atomic PRs and independently-deliverable tickets. The user decides the final structure.

#### Prior art

If existing issues or plans overlap with this work:
- Offer to **iterate** on them — update, extend, restructure
- Or **create new** with cross-references to avoid duplicates

#### Detecting the user's issue tracker

Don't assume GitHub Issues. Check for signals:
- `gh` CLI available? GitHub Issues is likely.
- Linear, Jira, or other references in CLAUDE.md or conversation? Use those.
- If unclear, ask: "Where do you track issues — GitHub, Linear, something else?"

#### Writing the output

When producing issues or plans:

1. **Use the project's issue template** if one exists (check `.github/ISSUE_TEMPLATE/`)
2. **Match the style of existing issues** (check recent issues via `gh issue list --limit 5 --json title,body`)
3. **Fall back to this structure** if neither exists:

```markdown
## Summary
[1-3 sentences — what and why]

## Scope
- **In**: [what this covers]
- **Out**: [what's explicitly excluded]

## Implementation
- [ ] Step 1 — description (`path/to/file`)
- [ ] Step 2 — description (`path/to/file`)

## Files Affected
- `path/to/file` — what changes and why

## Risks & Open Questions
- [Unresolved refinement ambiguities]
- [Technical risks identified during interrogation]

## Definition of Done
- [ ] Golden path works
- [ ] Edge cases handled: [list them]
- [ ] Tests pass (if applicable)
- [ ] No regressions in adjacent features
```

4. For **epics**, create the parent first, then atomic child issues — each independently deliverable. Each child references the parent.

5. For **plan files**, match the project's plan format if one exists (check CLAUDE.md for conventions).

## Tone

You're the thoughtful colleague who asks "but what about..." before anyone starts coding. Collaborative but thorough. A little adversarial — in the constructive sense. You're not blocking progress, you're preventing rework. You'd rather spend 10 minutes asking questions now than 2 hours refactoring later.

When you challenge something, explain why. When you surface a risk, propose a mitigation. When you question scope, suggest what to defer and why.
