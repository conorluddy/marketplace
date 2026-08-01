---
name: spec-speak
description: Convert any subject matter — rough feature ideas, brain-dumps, meeting notes, loose PRDs, existing docs — into a rigorous, testable spec written to industry requirements standards (EARS templates, RFC 2119 keywords, INCOSE/ISO 29148 rules, Gherkin acceptance criteria). Use this skill whenever the user wants to write, rewrite, tighten, or formalize a PRD, technical spec, requirements document, or acceptance criteria, or says things like "spec this out", "formalize this", "turn these notes into a spec", "write requirements for", "make this testable", "tighten this doc", or shares loose product thinking that needs to become an unambiguous document. Also use it to audit an existing spec for ambiguity, weak words, and untestable requirements.
---

# Spec-Speak

Convert subject matter into a disciplined spec: narrative where the author is reasoning, machine-grade precision where the system is being defined. The rules below are distilled from EARS (Rolls-Royce), INCOSE Guide to Writing Requirements v4, ISO/IEC/IEEE 29148, RFC 2119/8174, ASD-STE100, and Shape Up — see `references/standards-research.md` for the full survey and rule pedigrees.

## The governing principle: two zones, two dialects

A spec is not one genre. Every passage belongs to one of two zones, and applying the wrong dialect to a zone damages the document:

- **Exploratory zones** (problem statement, context, rationale, solution outline, open questions): narrative prose, complete sentences. Hedging is *desirable* here — "we believe", "this may", "the risk is" express calibrated uncertainty the author genuinely has. Never strip it out.
- **Normative zones** (requirements, acceptance criteria, interface contracts, constraints): full strictness. EARS shape, one capitalized RFC 2119 keyword per statement, weak words banned, every statement testable.

Why this matters: requirements exist to be verified, so ambiguity there becomes defects downstream. But a problem statement exists to convey the author's reasoning, and false certainty there hides unmade decisions. Classify the zone first, then apply the right dialect.

## Workflow

1. **Ingest.** Read the source material. Identify: what system is being specified, who reads this doc, and whether it's a PRD (solution-free, "what") or a technical spec (implementation is in scope, "how").
2. **Sort into zones.** Separate the author's reasoning (problem, context, trade-offs) from the system's obligations (behaviours, constraints, criteria). Rough notes usually interleave them — untangle before rewriting.
3. **Structure the document** using the template below.
4. **Write the normative zone** as numbered requirements, each in an EARS shape with one capitalized keyword.
5. **Attach acceptance criteria** — a Given/When/Then scenario per requirement. If you can't write the scenario, the requirement isn't verifiable yet; fix the requirement.
6. **Lint pass** over normative zones with the blacklist below.
7. **Resolve ambiguity — ask, don't invent.** This is the highest-value rule in the skill. When the source material is ambiguous, decide: is it a *wording* problem (rewrite it) or a *genuine gap* (nobody has chosen yet)? Never silently pick an answer to an unmade decision. How to handle each gap is covered in the next section.

## Resolving ambiguity

Triage every gap in the source material into one of two kinds — they get different treatment:

- **Product decisions** — choices only the author can make: scope (is CSV in v1?), gating (premium only?), behaviour under conflict (last-write-wins vs block?). Guessing these silently is the cardinal sin; a wrong guess ships the wrong product.
- **Engineering parameters** — values a competent engineer can default sensibly: latency targets, retry counts, retention windows, rate limits. Leaving *every* one of these as a blank makes the doc unbuildable; a doc with twelve `[TBD]`s is barely more useful than the vague original.

**When you can ask the author (interactive session with the AskUserQuestion tool): ask.** Batch the highest-impact gaps into one AskUserQuestion call — up to 4 questions, each with 2–4 concrete options and a recommended default marked where you have a view. Put product decisions first; include an engineering parameter only when it materially shapes the design (e.g. sync vs async export). One round of questions for the big calls — don't interrogate the author with a question per blank. Answers go straight into the requirements as settled values; anything the author declines or defers becomes an Open Question.

**When you can't ask** (no AskUserQuestion tool, headless run, or the long tail of smaller gaps):

- Engineering parameters: write a sensible proposed value into the requirement, flagged inline — "MUST return the file within 3 s (p95) `[ASSUMPTION — confirm]`" — and collect all assumptions in a short list the author can sweep through. The requirement's shape is settled; only the number awaits confirmation.
- Product decisions: never default these. List each under **Open questions** with the options you see and what each implies, and write requirements only for the decided scope.

Either way, no unflagged guess ever lands in a normative statement.

## Document template

Use this skeleton for a full spec. When the user asks for only a fragment (e.g. "rewrite these three requirements"), produce just that fragment under the same rules.

```markdown
# <Title>

## Summary            <!-- 3–5 sentences: what, for whom, why now -->
## Problem            <!-- narrative prose; hedging welcome -->
## Appetite           <!-- explicit time-box or effort budget -->
## Solution outline   <!-- narrative; opinionated, not exhaustive -->
## Out of scope       <!-- explicit no-gos; prevents scope ambiguity -->
## Open questions     <!-- undecided product questions, with options -->
## Requirements       <!-- normative zone starts here -->
## Acceptance criteria
## Rabbit holes & risks
## Glossary           <!-- every term of art, one meaning each -->
```

Summary comes first because readers decide relevance in the first ten lines (progressive disclosure). "Out of scope" and "Appetite" are structural guards against the two commonest spec failures: unbounded scope and unbounded time.

## Writing requirements (normative zone)

### EARS templates

Every requirement takes one of five shapes. Clause order is fixed: `While <state>, When <trigger>, the <system> KEYWORD <response>`.

| Pattern | Shape | Example |
|---|---|---|
| Ubiquitous | The `<system>` MUST `<response>` | The API MUST log every authentication decision. |
| Event-driven | When `<trigger>`, the `<system>` MUST `<response>` | When a request exceeds the rate limit, the API MUST return HTTP 429 with a `Retry-After` header. |
| State-driven | While `<state>`, the `<system>` MUST `<response>` | While the cache is cold, the service MUST serve reads from the primary database. |
| Unwanted behaviour | If `<failure condition>`, then the `<system>` MUST `<response>` | If the payment provider times out, then the checkout MUST queue the order and notify the user. |
| Optional feature | Where `<feature is present>`, the `<system>` MUST `<response>` | Where SSO is configured, the login page MUST hide the password form. |

Negative *conditions* are fine in the trigger clause ("If the token is invalid…"); the *response* clause must state positive, observable behaviour — "MUST reject with 401", not "MUST NOT allow access".

A requirement that needs more than ~3 preconditions, or that enumerates many combinations, is fighting the sentence form. Say so, and use a decision table or state diagram instead of forcing the template.

### Modal keywords

Adopt RFC 2119 wholesale: **MUST / MUST NOT / SHOULD / SHOULD NOT / MAY**. Exactly one capitalized keyword per requirement; capitalized means normative, lowercase "must/should" elsewhere is ordinary prose. Don't use "shall". This single convention makes requirements mechanically countable and frees the rest of the doc to read naturally. Watch for a second keyword creeping into the same statement — "MUST retain the file … and MAY delete it thereafter", or a semicolon chaining two MUSTs — that's two requirements wearing one ID; split them.

### The rules

- **One thought per requirement.** No "and/or/unless/but/however" joining obligations — split them. Multiple conditions are fine if the AND/OR logic is explicit.
- **Active voice, named actor.** "The scheduler MUST retry…", never "retries will be performed". Every requirement names who does what.
- **No pronoun openers.** Repeat the noun. "It must validate…" — which component is "it"?
- **Self-contained.** A requirement makes sense without its section heading and doesn't lean on "as described above".
- **Purpose lives in rationale, not the statement.** Strip "in order to…" / "so that…" into a rationale line beneath the requirement.
- **Quantify.** Replace "fast/reliable/scalable" with a number, a unit, and a tolerance: "p99 latency MUST be ≤ 200 ms at 1,000 req/s". Use "each" rather than "all/any" for universal claims. No unachievable absolutes ("never", "100%") — bounded targets.
- **Explicit time.** No "eventually", "soon", "as soon as possible" — give a deadline, interval, or ordering.
- **Sentence caps.** ≤ 25 words per requirement statement as a working ceiling; if you exceed it, the requirement is probably plural.
- **One word, one meaning.** Pick one term per concept ("user" vs "account" vs "member" — choose) and put every term of art in the Glossary.
- **PRDs stay solution-free.** State what the system does, not how it's built — unless the doc *is* the technical spec, where implementation choices belong and should be recorded with their rationale.

### Weak-word blacklist

Flag (or rewrite away) these in normative zones — each is a verifiability hole:

- **Vague:** adequate, appropriate, sufficient, reasonable, several, some, significant, flexible, robust, seamless, user-friendly, easy, fast, efficient, minimal
- **Escape clauses:** as appropriate, if necessary, as required, where possible, to the extent practical
- **Open-ended:** etc., and so on, including but not limited to, as a minimum
- **Temporal vagueness:** eventually, soon, timely, as soon as possible
- **Absolutes:** always, never, all, every, 100% (unless genuinely bounded and testable)

These words are fine in exploratory prose — "the current flow is slow and the UX feels clunky" is a legitimate problem statement. The ban applies where statements must be verifiable.

## Acceptance criteria

Attach a Gherkin scenario to each requirement. Describe behaviour, not implementation — "Given an unauthenticated user", not "Given I am on /login".

```gherkin
REQ-003 — When a request exceeds the rate limit, the API MUST return
HTTP 429 with a Retry-After header.

  Given a client that has exhausted its rate-limit quota
  When the client sends any further request within the window
  Then the response status is 429
  And the Retry-After header states the seconds until the window resets
```

Writing the scenario is the verifiability test: if no observable Then-clause exists, the requirement is not yet a requirement.

## Example conversion

**Input (typical rough note):**
> Users keep getting logged out randomly which is annoying. We should keep them logged in longer, maybe with refresh tokens or something, but obviously log them out if they're inactive for ages or if something looks suspicious.

**Output (fragment):**

```markdown
## Problem
Users report unexpected session expiry during active use. We believe the
fixed 30-minute session TTL is the cause, though we haven't confirmed the
distribution of expiry complaints against session age.

## Open questions
- OQ-1: What counts as "suspicious activity" that forces logout? (Options:
  new device fingerprint, impossible-travel IP change, credential-stuffing
  signals — needs a product decision.)
- OQ-2: What is the inactivity window? "Ages" needs a number.

## Requirements
- REQ-1: While a session is active, the auth service MUST extend the
  session by issuing a refresh token on each authenticated request.
- REQ-2: When a session receives no authenticated request for 14 days
  [OQ-2: confirm], the auth service MUST expire the session.
  - Rationale: limits exposure of dormant sessions.
```

Note what happened: the hedge in the problem statement survived ("we believe… we haven't confirmed"), the vague words became numbers or open questions, and "something looks suspicious" was *not* silently turned into a requirement — it's an unmade decision. In an interactive session, OQ-1 and OQ-2 are exactly what an AskUserQuestion round should put to the author; here they land in Open questions.

## Auditing an existing spec

Same rules, applied as review instead of rewrite: classify each passage's zone, then report findings grouped by severity — undecided product questions masquerading as requirements first, then unverifiable/plural/weak-worded requirements (cite the statement and the specific rule broken), then structural gaps (missing out-of-scope, missing glossary, mixed zones). Offer the rewritten form for each flagged requirement.

## References

- `references/standards-research.md` — the full standards survey: rule pedigrees (INCOSE R1–R42, ISO 29148 characteristics, STE sections), licensing constraints, conflict resolutions between standards, and the empirical case for why requirement defects are expensive. Read it when you need the authority behind a rule, when the user asks "why", or when tuning strictness (e.g. safety-critical work warrants the full INCOSE treatment; a solo side-project doesn't need R38-level formality).
