# Apple Metadata Rules (English U.S., 2025–2026)

The full ruleset for App Name, Subtitle, Keywords, Description, Promotional Text, and review compliance. Consolidated from Apple's `developer.apple.com/app-store/search/`, `developer.apple.com/app-store/product-page/`, App Store Connect Help, App Review Guidelines (last meaningful update Nov 2025), and the major ASO platforms.

## The 160-character searchable surface

| Field | Limit | Indexed | Updatable without build |
|---|---|---|---|
| App Name | 30 | **Yes — heaviest** | No |
| Subtitle | 30 | **Yes — second** | No |
| Keywords | 100 | **Yes — medium, hidden** | No |
| Promotional Text | 170 | No | **Yes** |
| Description | 4,000 | No (but feeds App Store Tags AI) | No |
| What's New | 4,000 | No | Required per version |
| IAP Display Name | 30 | Yes (separate IAP search) | No |
| IAP Description | 45 | No | No |
| Primary Category | enum | Yes (text-relevance signal) | No |
| Secondary Category | enum | Browse only | No |

## Keywords field rules (hard rules)

1. **No spaces after commas.** Apple counts spaces toward the 100. `photo,editor,filter` not `photo, editor, filter`.
2. **Apple combines words across Title + Subtitle + Keywords within a locale to form search phrases.** Tokens recombine. Pick single words, not phrases.
3. **Never repeat words across Name + Subtitle + Keywords.** Apple's docs: "Don't repeat any words included in your app name, subtitle, or category." Repetition wastes characters.
4. **No plurals of words used elsewhere.** `climb` and `climbs` are duplicates in English. (Stemming is reliable in English; less so in some other locales — not relevant for this English-only skill.)
5. **Don't include the primary category name.** It's auto-indexed via the category field.
6. **Drop common stop words.** Apple's stop-word list (observed): `a`, `an`, `and`, `app`, `apps`, `are`, `as`, `at`, `be`, `but`, `by`, `for`, `free`, `from`, `game`, `i`, `if`, `in`, `is`, `it`, `me`, `my`, `not`, `of`, `on`, `or`, `our`, `she`, `so`, `that`, `the`, `their`, `then`, `there`, `they`, `this`, `to`, `was`, `we`, `what`, `when`, `where`, `which`, `with`, `you`. App Store Connect's Metadata Editor flags these as "not recommended."
7. **Avoid generic catch-alls.** `best`, `top`, `awesome`, `new`, `cool`, `super`. Apple's docs flag these as wasted characters.
8. **Single words only.** Phrases form by recombination; multi-word entries waste chars.
9. **Compound words:** In the Title, capital-case auto-splits (`AppStoreConnect` → `app`, `store`, `connect`, `appstoreconnect`). In the Keywords field, treat as single tokens.

## Competitor / brand names

- **Bidding** on competitor names in Apple Search Ads is allowed and routine.
- **Including** competitor brand names in the organic Keywords field violates guideline 2.3.7 ("trademarked terms, popular app names, pricing information, or other irrelevant phrases just to game the system"). November 2025 enforcement is meaningfully tighter post the copycat crackdown.
- **Default:** exclude. Surface as a flagged opt-in choice in the research notes if the developer wants to take the risk.

## App Name rules

- 30 chars max. 2-char minimum (the historical X / Twitter exception is not generally available).
- Heaviest-weighted ranking field.
- Recommended structures, in order of efficiency:
  1. `Brand: Keyword Phrase` (colon = 2 chars)
  2. `Brand - Keyword Phrase` (3 chars)
  3. `Brand — Keyword Phrase` (em-dash, 1 char but visually heavy)
  4. `Brand, Keyword Phrase` (comma)
  5. Brand-only — only justified for established brands with strong organic brand-search demand
- Forbidden / rejection-risky in the Title:
  - 4+ generic keywords with no brand → 2.3.7
  - Trademarks not owned (`Photoshop`, `Spotify`, `Notion`, `Figma`, `ChatGPT`)
  - Pricing language (`Free`, `50% Off`, `$0.99`)
  - Superlatives (`Best`, `#1`, `Top`, `World's Best`, `Award-Winning`) without verifiable proof
  - Emojis — technically allowed, increase scrutiny, do not index. Default exclude.
  - "Pro" and "Lite" *are* allowed when they describe a tier of your own app

## Subtitle rules

- 30 chars max.
- Indexed slightly lower than Title, higher than Keywords.
- Should read as a sentence, not a comma-separated dump (2.3.7 forbids stuffing).
- 2–3 keyword tokens, distinct from Title and Keywords.
- Avoid superlatives (`best`, `#1`, `world's #1`).
- Quirk: a fully-packed 30-char subtitle may have its last word fail to index occasionally. Leaving 1–2 chars headroom is anecdotally safer.

## Description rules

- 4,000 chars. NOT indexed for App Store search (but Google indexes it for web search; and Apple's LLM reads it for App Store Tags).
- First 170 chars = the hook (above the "more" fold). Design in tandem with Promotional Text.
- Apple forbids in description:
  - Specific prices (shown elsewhere; may be region-inaccurate)
  - Marketing/promotional URLs (use the Marketing URL field)
  - Personal contact info (use Support URL)
  - Keyword stuffing
- Recommended structure:
  1. Hook (≤170 chars) — value prop + differentiator
  2. 5–10 benefit-led feature bullets
  3. Optional social proof (press, awards, user counts)
  4. Subscription disclosures if applicable (length, price, auto-renewal, Privacy Policy link, Terms of Use link — mandatory for auto-renewing subscriptions)
  5. Optional contact / social handles (no raw URLs)
- Length: 1,000–2,000 chars is plenty. Only ~2.5% of visitors tap "more."

## Promotional Text rules

- 170 chars. Not indexed. **Updatable anytime** — the only metadata field that is.
- Same 2.3.7 rules apply (lightweight review on update).
- Best uses: time-bound promos, new-feature announcements, seasonal hooks, social-proof snapshots, pre-release teasers.
- Refresh cadence: 30–90 days for most apps; monthly for high-velocity consumer apps.

## What's New rules

- 4,000 chars. Required per version after 1.0. Not indexed.
- Recency-of-update is a small organic ranking signal (active apps > abandoned apps).
- Best practice: short, human, 3–6 lines. Lead with user-visible wins, not engineering details.

## App Review Guideline 2.3.x rejection triggers

The skill must avoid generating any of these:

- **2.3.7 — Metadata stuffing (Nov 2025 update):** Names ≤30; metadata cannot include trademarked terms, popular app names, pricing info, or irrelevant phrases. Subtitles cannot reference other apps or make unverifiable claims.
- **2.3.8 — Age-appropriate metadata:** Metadata must be appropriate for 4+ even if the app's age rating is higher.
- **2.3.10 — Copycats (Nov 2025 update):** Targets metadata that leverages another developer's branding.

Top patterns to avoid:
1. Keyword stuffing in Title / Subtitle (`Photo Editor Filter Pic Camera Beauty Selfie`)
2. Trademarks not owned (`Photoshop`, `Spotify`, `Notion`, `Figma`, `ChatGPT` — last is heavily enforced 2025–2026)
3. Competitor app names in keywords
4. Superlatives without proof
5. Pricing language anywhere
6. Misleading metadata (claimed features the app doesn't have; "AI" claims without genuine AI integration — China rollout is especially strict)
7. Wrong category (mismatch with app function)
8. Prices in screenshot captions
9. Language placeholders left in non-primary locales
10. Emojis in App Name / Subtitle (allowed but scrutinized)

## Cross-localization (en-GB, en-AU, en-CA, es-MX)

Still effective in 2026 but with caveats:

- For the U.S. App Store, cross-indexed locales include English (Mexico/Spanish-MX), Arabic, Simplified Chinese, Traditional Chinese, French, Korean, Brazilian Portuguese, Russian, Vietnamese (the list shifts; check AppTweak/Sensor Tower current maps).
- **Within a locale, Title + Subtitle + Keywords combine. Across locales, words do NOT combine into phrases.**
- Each unique word counts once. Repeating the same word across locales is wasted budget.
- For an English-only U.S. app, populate **English (U.S.)** primary, then add **English (U.K.)**, **English (Australia)**, **English (Canada)** with *non-overlapping* English keywords. Each adds 30+30+100 = 160 chars of unique-word index. **Spanish (Mexico)** is also commonly used as a "ghost" English-keywords locale because Apple cross-indexes it for U.S. users.
- The skill should generate U.S. primary metadata as the main body and include a "Cross-Localization Expansion" section with non-overlapping keyword candidates for each additional locale.

## IAP rules

- Display name ≤30 chars (Apple's current product-page docs are authoritative; some third-party guides quote the older 35).
- Description ≤45 chars (older guides say 55).
- IAPs surface in App Store search separately when their display names match queries.

## Categories (current 2024–2026 list)

Books · Business · Developer Tools · Education · Entertainment · Finance · Food & Drink · Games (with up to 2 subcategories: Action, Adventure, Arcade, Board, Card, Casino, Casual, Family, Music, Puzzle, Racing, Role Playing, Simulation, Sports, Strategy, Trivia, Word) · Graphics & Design · Health & Fitness · Kids (age bands ≤5, 6–8, 9–11) · Lifestyle · Magazines & Newspapers · Medical · Music · Navigation · News · Photo & Video · Productivity · Reference · Shopping · Social Networking · Sports · Stickers · Travel · Utilities · Weather

Notes:
- Kids requires Made for Kids checkbox; restricts third-party analytics and ads.
- Games is the only category with developer-selectable subcategories (up to 2).
- Magazines & Newspapers requires auto-renewing subscriptions.
- Medical apps face heightened review for unverifiable health claims.

## Category strategy

- Primary drives browse placement, category-chart eligibility, and is a text-relevance signal in search.
- Secondary is browse-only with negligible search weight.
- Pick primary by (a) accurate fit, (b) lowest competition you genuinely fit. Top-100 chart access is more reachable in lower-competition categories.
