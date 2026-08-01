# spec-speak

Convert rough subject matter — feature ideas, brain-dumps, Slack threads, loose PRDs — into rigorous, testable specs written to industry requirements standards.

```bash
/plugin install spec-speak-plugin
```

Then ask Claude to "spec this out", "turn these notes into a spec", "make this testable", or "tighten this doc".

## What it does

Give it messy input, get back a structured spec: narrative prose where the author is reasoning, machine-grade precision where the system is being defined. Undecided questions get put to you as interactive prompts with options — not silently guessed, and not dumped as a wall of TBDs.

**Input:**

> Users keep getting logged out randomly which is annoying. We should keep them logged in longer, maybe with refresh tokens or something, but obviously log them out if they're inactive for ages or if something looks suspicious.

**Output (fragment):**

> **REQ-1:** While a session is active, the auth service MUST extend the session by issuing a refresh token on each authenticated request.
>
> **OQ-1:** What counts as "suspicious activity" that forces logout? (Options: new device fingerprint, impossible-travel IP change, credential-stuffing signals — needs a product decision.)

The hedged reasoning survives in the problem statement, the vague words become numbers, and the unmade product decision is surfaced instead of invented.

## The core idea: two zones, two dialects

A spec is not one genre, and the single most damaging thing a "clarity" tool can do is apply requirement-grade strictness everywhere:

- **Exploratory zones** (problem, context, rationale, open questions) are written in narrative prose where hedging is *desirable* — "we believe", "the risk is" express calibrated uncertainty the author genuinely has. Stripping it out manufactures false confidence.
- **Normative zones** (requirements, acceptance criteria, contracts) get full strictness — every statement shaped, keyworded, quantified, and verifiable, because these statements exist to be tested and every ambiguity becomes a defect downstream.

## The rules, and where they come from

Each rule is cherry-picked from an established standard rather than invented:

| Rule | Source |
|---|---|
| Every requirement takes one of five sentence templates: ubiquitous, `When` (event), `While` (state), `If…then` (unwanted behaviour), `Where` (optional feature) | **EARS** (Mavin et al., Rolls-Royce, RE'09 — used by Airbus, Bosch, Intel, NASA) |
| Exactly one capitalized modal keyword per requirement — MUST / MUST NOT / SHOULD / SHOULD NOT / MAY; lowercase elsewhere is ordinary prose | **RFC 2119 / RFC 8174** (BCP 14) |
| One thought per requirement; active voice with a named actor; no pronoun openers; self-contained statements; purpose moved to rationale | **INCOSE Guide to Writing Requirements v4** (R2, R18–R24) |
| Weak-word ban in normative zones: *adequate, appropriate, fast, robust, seamless, as appropriate, etc., eventually…* — each is a verifiability hole | **INCOSE R7–R9** + **ISO/IEC/IEEE 29148** "requirements smells" |
| Quantify: numbers, units, tolerances; "each" not "all"; no unachievable absolutes; explicit time | **INCOSE R26, R32–R35** |
| A Given/When/Then acceptance scenario per requirement — writing it *is* the verifiability test | **Gherkin / BDD** |
| Explicit appetite (time-box) and out-of-scope sections | **Shape Up** (Basecamp) |
| Summary-first progressive disclosure; don't mix normative and explanatory modes | **ISO 24495-1 (Plain Language)** + **Diátaxis** |
| One word, one meaning; every term of art in a glossary | **ASD-STE100** principles + **INCOSE R4/R36** |

The full survey behind these choices — including licensing constraints, conflicts between the standards and how each was resolved — lives in [`skills/spec-speak/references/standards-research.md`](skills/spec-speak/references/standards-research.md).

## Ambiguity handling: ask, don't invent

The highest-value rule in the skill. Every gap in the source material is triaged:

- **Product decisions** (scope, gating, behaviour under conflict) — only the author can make these. In an interactive session the skill puts them to you as a single batched round of multiple-choice questions with a recommended default; declined or deferred ones land in an **Open questions** section with the options laid out. They are never silently guessed, because spec ambiguity usually signals a decision nobody has made.
- **Engineering parameters** (latency targets, retry counts, retention windows) — defaulted to sensible values flagged inline as `[ASSUMPTION — confirm]`, so the doc stays buildable without pretending the numbers are settled.

## Why use it

The empirical case (detail and caveats in the [research doc](skills/spec-speak/references/standards-research.md)): requirements defects are the cheapest defects to fix at spec time and the most expensive to fix later — the NASA/INCOSE escalation data puts operations-phase fixes at 29–1500× spec-phase cost, and roughly half of product defects trace back to requirements errors. The direction is well-supported even where the exact multipliers are contested. More practically: a spec written this way is directly consumable by both engineers and AI agents — EARS shapes and RFC 2119 keywords are mechanically checkable, and every requirement arrives with its own acceptance test.

Benchmarked against a no-skill baseline on three conversion tasks: 88% assertion pass rate with the skill vs 62% without — the gap entirely in requirement rigor (EARS shape, keyword discipline, acceptance criteria), which baselines produced zero of.

## Contents

```
spec-speak-plugin/
├── README.md                     # This file
└── skills/spec-speak/
    ├── SKILL.md                  # The skill: workflow, templates, rules
    ├── references/
    │   └── standards-research.md # Full standards survey and rule pedigrees
    └── evals/
        └── evals.json            # Test prompts + assertions
```
