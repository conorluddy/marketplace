---
name: app-review-guidelines
description: Audit an iOS app against Apple's App Store Review Guidelines, triage a rejection message, or prepare for submission. Scans Info.plist, entitlements, PrivacyInfo.xcprivacy, StoreKit and Swift/SwiftUI source for likely review risks (in-app purchase, subscriptions, Sign in with Apple, account deletion, UGC moderation, privacy and ATT, Kids Category, health data, minimum functionality, background modes, private APIs) and writes an advisory REVIEW-RISK.md citing guideline numbers. Also maps a pasted App Review rejection to the guideline, likely cause, fix and a drafted Resolution Center reply. Use this skill whenever the user mentions App Review, App Store review, review guidelines, rejection, rejected build, Guideline 2.1 / 3.1.1 / 4.8 / 5.1.1 (or any guideline number), Resolution Center, submission readiness, "will Apple reject this", "can I do X on the App Store", TestFlight external review, or is about to submit an iOS app — even if they never say "guidelines".
---

# App Review Guidelines

Helps an iOS developer avoid and recover from App Review rejections. Three modes, picked from what the user asks:

| Mode | Trigger | Output |
|---|---|---|
| **Audit** | "check my app", "will this get rejected", about to submit | `REVIEW-RISK.md` at repo root |
| **Triage** | user pastes a rejection message or guideline number | Inline: cause, fix, drafted reply |
| **Pre-submission** | "ready to submit?", "what do I need for review" | Inline checklist of what code can't show |

If the user's intent is ambiguous, default to Audit, then offer Pre-submission.

## Ground rules

- **Findings are advisory.** App Review is partly subjective and Apple revises the guidelines several times a year. Frame every finding as a *risk to consider* with the guideline number, never as a verdict. Do not use blocker/pass/fail language.
- **Say how you know.** Tag each finding `detected in code` (you saw it in a file, cite `file:line`) or `needs human judgement` (metadata, content, business model). Overclaiming on judgement calls erodes trust in the whole report.
- **Verify before asserting on borderline rules.** The bundled references are a condensed snapshot (see the date in each file). When a finding hinges on exact wording, a recently changed rule, or a region-specific exception (3.1.1(a) external links, 4.8 exemptions, EU/Japan entitlements), fetch https://developer.apple.com/app-store/review/guidelines/ and state which text you checked. If you cannot fetch it, say the snapshot is unverified.
- **Standalone.** Cover metadata (2.3) and accessibility only at checklist depth; do not require other skills. Mention that a deeper pass is possible if the user has tooling for it.

## Mode 1 — Audit

1. **Confirm an iOS project**: `*.xcodeproj`, `*.xcworkspace`, or `Package.swift` with an iOS platform. If several targets exist, audit the app target plus its extensions, since extensions have their own rules (4.4, 2.5.16, 2.5.18).
2. **Classify the app** so you load only relevant references. Scan once, then pick categories (an app can match several):
   - Sells anything or has paywalls/subscriptions → IAP
   - Has accounts, login, or user-visible content from other users → Accounts/social
   - Uses HealthKit, collects minors' data, targets children, or tracks users → Sensitive data
   - None of the above → Generic utility
3. **Run the code checks** in `references/code-checks.md` for the matching categories. Each row gives the file or API to look for, the guideline, and what a risk looks like. Prefer `rg`/`fd` over reading whole files.
4. **Load guideline detail only when needed** to explain a finding or settle a doubt: `references/guidelines-safety-performance.md` (1–2), `guidelines-business.md` (3), `guidelines-design.md` (4), `guidelines-legal.md` (5).
5. **Write `REVIEW-RISK.md`** using `references/output-template.md`. Order findings by likelihood-and-impact, high to low, but label them as risks, not blockers. End with the human-judgement items the code cannot answer.
6. **Offer next steps**: turn the top items into GitHub issues, or run Pre-submission.

Keep the report short enough to act on. Ten well-evidenced risks beat forty speculative ones; omit checks that came back clean (list them in one line under "Checked, nothing found").

## Mode 2 — Rejection triage

Input is Apple's message (often "Guideline 2.1 - Performance - App Completeness") plus optional screenshots or notes.

1. **Extract the guideline number(s)** and the specifics Apple quoted: what screen, feature, or metadata they flagged.
2. **Explain in plain terms** what the reviewer most likely saw. Read `references/rejection-triage.md` for the common patterns behind each frequently cited guideline; it saves you rediscovering them.
3. **Check the code** for the specific cause when the rejection is code-detectable (missing purpose string, no restore button, no account deletion). Cite `file:line`.
4. **Propose the fix**, smallest change first, and say whether it needs a new binary or only a metadata/reply change. Many rejections (2.1 missing demo account, 2.3 metadata) resolve without a rebuild.
5. **Draft a Resolution Center reply**: polite, specific, short. State what changed or point to where the feature lives (steps to find it). Never argue tone or accuse the reviewer; if you believe the rejection is mistaken, draft a respectful clarification with evidence and mention the App Review Board appeal as an option.

## Mode 3 — Pre-submission

Walk `references/presubmission-checklist.md`. These are items code can't prove: demo credentials and live backend, review notes, privacy nutrition labels versus actual SDK behaviour, screenshots, age rating answers, support/privacy URLs, IAP items attached and reviewable. Ask the user to confirm each group rather than assuming. Note which of these the audit already touched.

## Quick answers (design-time questions)

For "can I do X?" questions, answer directly from the references, cite the guideline, fetch the live page if the rule is nuanced, and keep it to a few sentences. Do not run a full audit unless asked.

## Reference map

- `references/code-checks.md` — what to scan, per app category
- `references/guidelines-safety-performance.md` — sections 1–2
- `references/guidelines-business.md` — section 3
- `references/guidelines-design.md` — section 4
- `references/guidelines-legal.md` — section 5
- `references/rejection-triage.md` — common rejection patterns and reply patterns
- `references/presubmission-checklist.md` — human-side checklist
- `references/output-template.md` — `REVIEW-RISK.md` format
