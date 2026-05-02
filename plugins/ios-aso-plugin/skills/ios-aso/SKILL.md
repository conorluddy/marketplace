---
name: ios-aso
description: Generate a paste-ready English (U.S.) App Store Optimization metadata file (ASO.md) for an iOS app by scanning its Swift/SwiftUI codebase. Produces App Name (30), Subtitle (30), Keywords (100), Promotional Text, Description, category recommendations, screenshot caption suggestions, IAP names, and a research-notes appendix grounded in the codebase. Use this skill whenever the user mentions ASO, App Store Optimization, App Store metadata, app store listing, app name, app subtitle, keywords field, App Store Connect copy, App Store keywords, app store description, promotional text, custom product pages, or wants help writing/auditing/improving the metadata for an iOS App Store submission — even if they don't say "ASO" explicitly. Also trigger when the user asks to prepare an app for submission, audit a listing for rejection risk, pick a category, or extract keywords from a codebase.
---

# iOS App Store Optimization (ASO) Generator

This skill scans an iOS Swift/SwiftUI codebase and emits a single English-only `ASO.md` at the repo root containing paste-ready App Store metadata plus a research-notes appendix. It encodes Apple's 2025–2026 metadata rules, WWDC25 changes (App Store Tags, CPP organic keywords, SAP collapse), and a codebase-signal extraction taxonomy.

The whole searchable surface on the App Store is **160 characters total**: App Name (30) + Subtitle (30) + Keywords (100). Everything else exists for conversion or browse — not search ranking. Get those 160 right and the rest follows.

## When this skill applies

Trigger when the user wants to:
- Generate ASO metadata for a new iOS app
- Audit or improve an existing App Store listing
- Pick keywords from their codebase
- Choose a category, write a subtitle, draft a description, or prepare for submission
- Check metadata for rejection risk (2.3.7)

The skill assumes English (U.S.) primary locale. Cross-localization expansion (en-GB, en-AU, en-CA, es-MX) is offered as an optional appendix in the output.

## Workflow

### Step 1 — Confirm iOS project and find the brand

Confirm the working directory is an iOS project: look for `*.xcodeproj`, `*.xcworkspace`, or a `Package.swift` declaring an iOS platform.

Find the brand name in this precedence order:
1. `fastlane/metadata/en-US/name.txt` (if present, the developer has already drafted metadata — treat existing files as the source of truth and propose refinements rather than rewrites)
2. `CFBundleDisplayName` in the primary target's `Info.plist`
3. `CFBundleName`
4. The Xcode target name
5. The repo's README first heading

### Step 2 — Scan the codebase for signals

Read `references/codebase-signals.md` for the full extraction taxonomy. Build a feature inventory by union-ing signals across the Tier 1–4 sources:
- Tier 1: `Info.plist` (especially `NS*UsageDescription` strings), `Localizable.strings` / `.xcstrings`, `fastlane/metadata`, README
- Tier 2: `*.entitlements`, `PrivacyInfo.xcprivacy`, Xcode capabilities (widgets, Live Activities, App Clips, Background Modes)
- Tier 3: App Intents (`AppIntent`, `AppShortcut`), StoreKit IAPs, SwiftUI/UIKit view + module names, Core Data / SwiftData entities, `Package.swift` / Podfile dependencies (each SDK maps to a capability — see the dependency→capability table in `codebase-signals.md`)
- Tier 4: Snapshot test names, accessibility identifiers

Tokenize all user-facing strings, frequency-rank after stop-word filtering, and produce a candidate keyword pool of 30–50 single words.

### Step 3 — Synthesize the metadata

**Pick the keyword set, not phrases.** Choose 10–20 single-word tokens that *recombine* across Title + Subtitle + Keywords into the highest-relevance 2- and 3-word phrases. Apple combines words across those three fields within a locale to form search phrases. Tokens multiply; phrases don't.

Draft fields in this order:
1. **App Name (≤30 chars):** `Brand: Keyword Phrase` (colon is the most efficient separator at 2 chars). For new/indie apps put 1–2 of your strongest keywords here. For established brands, brand-only is acceptable.
2. **Subtitle (≤30 chars):** A readable mini-sentence with 2–3 keyword tokens *not* used in the Name. Avoid superlatives. Some practitioners leave 1–2 chars headroom because the last word of a fully-packed subtitle occasionally fails to index.
3. **Keywords field (≤100 chars):** Comma-separated, NO spaces after commas. Single words only. Exclude every word already in Name, Subtitle, primary category, and Apple's stop-word list. Never include plurals of words used elsewhere.
4. **Primary category:** Drives browse placement AND is a text-relevance signal in search. Pick the most accurate fit; if two fit, pick the lower-competition one.
5. **Secondary category:** Browse only. Minimal search impact.
6. **Promotional Text (≤170):** Updatable anytime without a build. Use for time-bound promos, new features, social proof.
7. **Description:** First 170 chars are the hook (above the "more" fold). Then 5–10 benefit-led bullets. Then required subscription disclosures if applicable. Apple's LLM reads this for App Store Tags so write semantically clearly.
8. **What's New:** Template only — the skill cannot know what shipped.
9. **IAP names (≤30) and descriptions (≤45)** for each detected StoreKit product.
10. **Screenshot caption suggestions** — per WWDC25, captions feed Apple's AI tagging. Write plain-English captions that reinforce 3–5 core keywords.

### Step 4 — Validate against the rules

Before writing the file, run every draft field through this checklist. The full ruleset and rejection-pattern catalog lives in `references/rules.md`; load it if any check is non-obvious.

**Hard rules (always):**
- App Name ≤30 chars; Subtitle ≤30; Keywords ≤100
- Keywords field has **no spaces after commas** — Apple counts them
- **No word appears in more than one of Name/Subtitle/Keywords** (or in the primary category, or in Apple's stop-word list)
- **No plurals** of singular forms used elsewhere (Apple stems English reliably; `climb` and `climbs` are duplicates)
- Single words only in the Keywords field — phrases are formed by recombination
- Multi-word phrases like `Real Estate` only if Apple won't recombine them from singles in another field

**Apple Review 2.3.7 rejection triggers (default-exclude):**
- Trademarks the developer doesn't own (`Photoshop`, `Spotify`, `Notion`, `Figma`, `ChatGPT`)
- Competitor brand names in the Keywords field (post-November 2025 enforcement is tight; default exclude, surface as a flagged opt-in choice)
- Superlatives without proof: `#1`, `Best`, `Top`, `World's Best`, `Award-Winning`
- Pricing language anywhere in metadata: `Free`, `50% Off`, `$0.99`
- Generic catch-alls: `app`, `the`, `for`, `of`, `game`, `best`, `top`
- The primary category name (auto-indexed via the category field)
- Emojis in App Name / Subtitle (allowed but increases scrutiny; default exclude)
- "AI" claims without genuine AI integration (2025–2026 enforcement is tight, especially for mainland-China rollout)

**Compound-word rule:** In the Title field, capitalized compounds auto-split (`AppStoreConnect` indexes as `app`, `store`, `connect`, *and* `appstoreconnect`). In the Keywords field, treat compounds as single tokens.

### Step 5 — Write `ASO.md`

Use the template in `references/output-template.md` verbatim — it has all 16 sections (TL;DR, App Name, Subtitle, Keywords, Promotional Text, Description, What's New, IAPs, Categories, Screenshot Captions, Cross-Localization, Custom Product Pages, ASA seed, Pre-Submission Checklist, Research Notes, Candidate Pool).

The **Research Notes** section is where the skill explains *why* each choice was made, citing specific codebase evidence (file paths, entitlements, dependencies, intent titles, etc.). This is what the developer reads to iterate. Be concrete: "Picked `workout` because it appears 47× across `Localizable.strings` and the project depends on `HealthKit`" beats "common fitness term."

The **Candidate Pool** section retains every keyword the skill considered but didn't use, with codebase evidence for each, so the developer can iterate after 4 weeks of analytics.

Write the output to `ASO.md` at the repo root unless the user specifies otherwise. If `ASO.md` already exists, read it first and propose a diff/refinement rather than overwriting blindly.

## Reference files (load on demand)

- **`references/codebase-signals.md`** — Load whenever scanning a codebase. Has the full Tier 1–4 file/pattern list including the dependency→capability mapping (RevenueCat, HealthKit, Mapbox, OpenAI, ARKit, etc. → keyword candidates).
- **`references/rules.md`** — Load when validating drafts or any rule above is non-obvious. Has the full §2 keyword ruleset, §3 title/subtitle conventions, §10 rejection-trigger catalog with 2.3.7 enforcement notes, the stop-word list, and the cross-localization mechanics.
- **`references/output-template.md`** — Load before writing the file. The full 16-section `ASO.md` skeleton with placeholder syntax.
- **`references/wwdc25-context.md`** — Load when the developer asks about App Store Tags, Custom Product Pages, screenshot sizes, the SAP collapse, iOS 26 SDK deadline, or any "what changed in 2025/2026" question.

## Notes on the post-September-2025 keyword research landscape

The legacy Apple Search Ads "Search Popularity" 1–5 / 0–100 score collapsed on Sept 29, 2025 — ~77% of U.S. keywords now floor to "5". Do not rely on it. Free signals the skill *can* trust:
- App Store autocomplete (Apple-direct)
- App Store search results count + which apps rank for a term (use as a difficulty heuristic: if the top 5 are all million-download apps with the keyword in their Name, it's high-difficulty)
- Apple Ads' beta Monthly Search Term Rank Report (limited to legacy SAP ≥ 35 terms)

If the developer has access to AppTweak / Sensor Tower / MobileAction / Appfigures / App Radar / APPlyzer / ASO.dev, recommend they cross-validate the skill's picks. The skill itself does not assume any paid tool.

## Iteration

ASO is iterative. The skill produces a v1; the developer should submit, wait ~4 weeks, track keyword rankings in App Store Connect Analytics, and replace bottom-quartile keywords with alternates from the Candidate Pool section. Promotional Text refreshes every 30–90 days. The skill can be re-run after major feature ships.
