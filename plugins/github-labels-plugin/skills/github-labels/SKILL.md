---
name: github-labels
description: Set up structured GitHub issue labels for any repository. Installs curated label groups (priority, clarity, risk, blast radius, size, parallelism, sequencing, type, and special labels) using the GitHub CLI. Use this skill when a user mentions "set up labels", "github labels", "label taxonomy", or wants to organise their issue tracker.
compatibility: Requires gh CLI installed and authenticated with write access to target repo
allowed-tools: Bash(gh:*) Bash(git:*)
---

## Prerequisites

- `gh` CLI installed and authenticated (`gh auth status` should succeed)
- Write access to the target repository

## How it works

1. Detect or ask for the target repository (owner/repo format)
2. Present available label groups and let the user pick
3. Create each label via `gh label create` with `--force` (idempotent — safe to re-run)

## Label Groups

Present these groups to the user. Let them pick individually or say "all".

### 1. Priority (`priority`)

| Label | Color | Description |
|-------|-------|-------------|
| `P1` | `b60205` | Must ship first, blocks other work |
| `P2` | `d93f0b` | Core features, ship after P1 |
| `P3` | `e99695` | Polish and low-urgency items |
| `P4` | `f9d0c4` | Post-launch polish and enhancements |
| `P5` | `fef2c0` | Nice to have, no pressure |

### 2. Clarity (`clarity`)

| Label | Color | Description |
|-------|-------|-------------|
| `clarity:1` | `5319e7` | Vague idea — no spec, no definition of done, needs discussion |
| `clarity:2` | `7b61ff` | Problem defined, solution unclear — needs a design spike |
| `clarity:3` | `a78bfa` | Direction known, details TBD — can start with questions |
| `clarity:4` | `c4b5fd` | Clear spec, minor ambiguities — AI-shippable with light review |
| `clarity:5` | `ddd6fe` | Crystal clear, full definition of done — just execute |

### 3. Risk (`risk`)

| Label | Color | Description |
|-------|-------|-------------|
| `risk:1` | `0e8a16` | Isolated change, well-tested area, hard to break |
| `risk:2` | `53d353` | Small surface area, existing patterns, minor regression chance |
| `risk:3` | `fbca04` | Touches shared code, some edge cases, needs careful testing |
| `risk:4` | `e99695` | Cross-domain impact, state management, concurrency concerns |
| `risk:5` | `b60205` | Data model migration, navigation architecture, or seed data changes |

### 4. Blast Radius (`blast`)

| Label | Color | Description |
|-------|-------|-------------|
| `blast:1` | `bfdadc` | Single file — one view or one service, no ripple effects |
| `blast:2` | `7ec8cb` | Single domain — 2-5 files within one feature folder |
| `blast:3` | `3bb3b8` | Cross-domain — touches shared code or 2+ feature domains |
| `blast:4` | `1d7a7e` | Architectural — services, navigation, data flow changes |
| `blast:5` | `0e4f52` | Full-stack — data pipeline + app, or schema changes |

### 5. Size (`size`)

| Label | Color | Description |
|-------|-------|-------------|
| `size:XS` | `c5def5` | Trivial change, single file |
| `size:S` | `85c1e9` | Straightforward, few files |
| `size:M` | `5dade2` | Moderate scope, some design needed |
| `size:L` | `2e86c1` | Significant feature, many files |
| `size:XL` | `1a5276` | Epic-level, major cross-cutting work |

### 6. Parallelism (`parallelism`)

| Label | Color | Description |
|-------|-------|-------------|
| `parallel:1` | `f0e68c` | Lane 1 work stream |
| `parallel:2` | `daa520` | Lane 2 work stream |
| `parallel:3` | `cd853f` | Lane 3 work stream |
| `parallel:4` | `b8860b` | Lane 4 work stream |
| `parallel:5` | `8b6914` | Lane 5 work stream |
| `serial` | `6c757d` | Cross-cutting — touches 2+ lanes, run alone |

### 7. Sequencing (`sequencing`)

| Label | Color | Description |
|-------|-------|-------------|
| `seq:01` | `006b75` | Sequence step 1 |
| `seq:02` | `006b75` | Sequence step 2 |
| `seq:03` | `006b75` | Sequence step 3 |
| `seq:04` | `006b75` | Sequence step 4 |
| `seq:05` | `006b75` | Sequence step 5 |
| `seq:06` | `006b75` | Sequence step 6 |
| `seq:07` | `006b75` | Sequence step 7 |
| `seq:08` | `006b75` | Sequence step 8 |
| `seq:09` | `006b75` | Sequence step 9 |
| `seq:10` | `006b75` | Sequence step 10 |

### 8. Type (`type`)

| Label | Color | Description |
|-------|-------|-------------|
| `type:bug` | `d73a4a` | Something isn't working correctly |
| `type:feature` | `0075ca` | New functionality or capability |
| `type:refactor` | `cfd3d7` | Code improvement, no behaviour change |
| `type:chore` | `ededed` | Maintenance — deps, CI, config, docs |
| `type:spike` | `d4c5f9` | Research or time-boxed exploration |

### 9. Special (`special`)

| Label | Color | Description |
|-------|-------|-------------|
| `ai-shippable` | `1d76db` | Delegatable to AI agents — clarity:4+ and risk:2 or lower |
| `needs-design` | `d4c5f9` | Requires design work before implementation |

## Execution

For each selected group, run:

```bash
gh label create "<name>" --color "<hex>" --description "<description>" --repo "<owner/repo>" --force
```

## Interaction Flow

1. **Detect repo**: Run `gh repo view --json nameWithOwner -q .nameWithOwner`. If it works, offer as default. Otherwise ask.

2. **Present groups**: Show numbered list:
   ```
   Available label groups:
     1. Priority (P1-P5) — triage priority
     2. Clarity (clarity:1-5) — issue definition quality
     3. Risk (risk:1-5) — change danger level
     4. Blast Radius (blast:1-5) — scope of impact
     5. Size (size:XS-XL) — effort estimation
     6. Parallelism (parallel:1-5 + serial) — lane assignment
     7. Sequencing (seq:01-10) — implementation order
     8. Type (type:bug, feature, refactor, chore, spike) — work category
     9. Special (ai-shippable, needs-design) — workflow flags

   Enter numbers (e.g. "1,3,4"), "all", or ask me about any group.
   ```

3. **Confirm**: Show total label count and target repo, ask for confirmation.

4. **Execute**: Create labels, reporting progress grouped by category.

5. **Summary**: Report what was created/updated, note any failures.
