# ASO.md Output Template

Use this skeleton verbatim when writing the final `ASO.md`. Every section is required. Fill placeholders in `[brackets]`. Char counts go in parentheses next to each value.

```markdown
# ASO.md — App Store Listing Metadata
*English (U.S.) — generated [YYYY-MM-DD]. Re-run the skill after major feature ships.*

## TL;DR — paste-ready

- **App Name (30):** `[Brand: Keyword Phrase]` ([N]/30)
- **Subtitle (30):** `[Subtitle sentence]` ([N]/30)
- **Keywords (100):** `keyword1,keyword2,...` ([N]/100)
- **Primary Category:** [Category]
- **Secondary Category:** [Category]
- **Promotional Text (170):** `[Hook]` ([N]/170)

## 1. App Name (≤30)

**Final:** `[value]` ([N]/30)
**Alternates:**
- `[alt 1]` ([N]/30)
- `[alt 2]` ([N]/30)

*Why this choice:* [reasoning grounded in codebase evidence]

## 2. Subtitle (≤30)

**Final:** `[value]` ([N]/30)
**Alternates:**
- `[alt 1]` ([N]/30)
- `[alt 2]` ([N]/30)

*Why this choice:* [reasoning]

## 3. Keywords Field (≤100, comma-separated, NO spaces after commas)

```
keyword1,keyword2,keyword3,...
```

- **Character count:** [N]/100
- **Word count:** [N]
- **Phrase combinations enabled** (across Title + Subtitle + Keywords):
  - `[recombined phrase 1]`
  - `[recombined phrase 2]`
  - …
- **Words explicitly excluded (and why):**
  - `app`, `the`, `for` — Apple stop words
  - `[category-name]` — auto-indexed via category field
  - `[word in Title]` — already in Name
  - `[plural]` — singular form already used

## 4. Promotional Text (≤170, updatable anytime)

**Final:** `[value]` ([N]/170)

*Use this field for:* launch announcements, time-bound promos, new-feature ships, season starts. Refresh every 30–90 days.

## 5. Description

### Hook (first 170 chars — appears above the "more" fold)

[opening hook: one-sentence value prop + the single most compelling differentiator]

### Body

[5–10 benefit-led feature bullets]
- [Benefit 1]
- [Benefit 2]
- …

[optional: 2–3 lines of social proof — press, awards, user counts]

[required if applicable: subscription disclosures — length, price, auto-renewal, links to Privacy Policy and Terms of Use]

[optional: support email, social handles — no raw URLs]

## 6. What's New / Release Notes (template)

```
This release:
• [user-visible win]
• [bug fix]

Thanks for using [App Name]!
```

## 7. In-App Purchase Display Names & Descriptions

| Product ID | Display Name (≤30) | Description (≤45) |
|---|---|---|
| `[product_id]` | `[name]` | `[description]` |

## 8. Category Recommendations

**Primary:** [Category]
*Why:* [evidence: entitlements detected, Core Data entities, dependencies]

**Secondary:** [Category]
*Why:* [evidence]

## 9. Screenshot Caption Suggestions

Per WWDC25, screenshot captions feed Apple's LLM-driven App Store Tags. Recommended captions for the 6.9″ iPhone screenshot set (1320×2868):

1. `[Caption 1 — reinforces keyword X]`
2. `[Caption 2 — reinforces keyword Y]`
3. `[Caption 3 — reinforces keyword Z]`
4. `[Caption 4]`
5. `[Caption 5]`

**Note:** Only the first 3 screenshots appear in search results.

## 10. Optional: Cross-Localization Expansion

For an additional ~160 chars of keyword space per locale, add these locales with **non-overlapping** English keywords. Words don't combine across locales, but each unique word adds index coverage.

- **English (U.K.)** — keywords: `[non-overlapping list]`
- **English (Australia)** — keywords: `[non-overlapping list]`
- **English (Canada)** — keywords: `[non-overlapping list]`
- **Spanish (Mexico)** — (cross-indexed for U.S. users) — English keywords: `[non-overlapping list]`

## 11. Custom Product Pages (post-launch follow-up)

After the default listing is live, set up keyword-targeted CPPs (Apple supports up to 70 since WWDC25). Each CPP keyword must already exist in your Keywords field.

- **CPP 1** — target keyword `[X]` — screenshots emphasize [feature A]
- **CPP 2** — target keyword `[Y]` — screenshots emphasize [feature B]

## 12. Apple Search Ads — Seed Keywords

The keyword tokens above also work as the seed for an ASA Discovery campaign. Run Discovery, promote winners to exact-match, feed learnings back into the Keywords field.

## 13. Pre-Submission Checklist

- [ ] App Name ≤30 chars, no trademarks, no superlatives
- [ ] Subtitle ≤30 chars, reads as a sentence, no `best`/`#1`
- [ ] Keywords field ≤100 chars, no spaces after commas, no plurals of words used elsewhere, no competitor brands
- [ ] Description: hook in first 170 chars, no prices, no marketing URLs, subscription disclosure if applicable
- [ ] Screenshots in 1320×2868 (iPhone 6.9″) and 2064×2752 (iPad 13″ if iPad-supported)
- [ ] Privacy nutrition label completed in App Store Connect
- [ ] Age rating questionnaire completed
- [ ] Support URL and Privacy Policy URL set
- [ ] Contact info accurate

## 14. Research Notes

**Brand source:** [where the brand was found in the codebase]

**App archetype inferred:** [e.g., "fitness tracking with social comparison"] — based on:
- [evidence: HealthKit entitlement at `path/to/file.entitlements`]
- [evidence: Core Data entities `Workout`, `Run` in `path/to/Model.xcdatamodeld`]
- [evidence: `RevenueCat` dependency → subscription model]
- [evidence: `NSHealthShareUsageDescription` = "..."]

**Per-keyword rationale (top 10):**
| Keyword | Evidence | Rationale |
|---|---|---|
| `[word]` | `[file]:[line]` × N occurrences | [why it earned a slot] |

**Flagged choices the developer should review:**
- [e.g., "Did NOT include `runkeeper` (competitor brand). 2.3.7 risk. Flip if you accept the rejection risk."]
- [e.g., "Mentioned `AI` in Subtitle. Verify mainland-China rollout strategy — mentioning AI without certification can result in removal."]

## 15. Iteration Plan

1. Submit this as v1 metadata.
2. Wait 4 weeks; track keyword rankings in App Store Connect → App Analytics.
3. Replace bottom-quartile keywords with alternates from the Candidate Pool (§16).
4. Refresh Promotional Text every 30–90 days.
5. After v1 stabilizes, set up Custom Product Pages for the strongest 2–3 ranking keywords.

## 16. Candidate Pool (not used in v1)

Keywords the skill considered but did not use, retained for iteration. Each cites the codebase evidence that surfaced it.

| Keyword | Evidence | Reason not used |
|---|---|---|
| `[word]` | `[source]` | [e.g., "redundant with `tracker`", "high difficulty — top 5 results dominated by Apple Fitness", "outside core archetype"] |
```
