# WWDC25 / iOS 26 Era Context (mid-2025 → 2026)

What changed in App Store discovery in the past year. Load this when the developer asks about App Store Tags, Custom Product Pages, screenshot sizes, the SAP collapse, the iOS 26 SDK deadline, or any "what's new in ASO" question.

## App Store Tags (WWDC25, June 2025)

AI-generated, human-reviewed tags now surface alongside categories in search and on app pages.

- **Inputs:** app metadata + description + category + screenshots + (likely) icon
- **Developer control:** can deselect tags via App Store Connect; cannot add custom tags
- **Implication:** the description and screenshot text should be written for an LLM to extract semantic features. State features clearly and unambiguously.

This is the headline reason the description matters for discovery in 2026 even though it's not directly indexed for keyword search.

## Custom Product Pages (CPP) — organic search keywords (July 30, 2025)

- CPPs can now be assigned keywords from the existing Keywords field
- When the app ranks for those keywords, the CPP can replace the default product page in search results
- Cap raised from 35 to 70 CPPs per app
- Currently U.S.- and U.K.-focused, expanding
- **Implication:** the Keywords field has become *more* important — it now feeds two surfaces (default page + CPPs). Recommend CPP setup as a post-launch follow-up after the default listing stabilizes.

## App Review Summaries (March 2025, iOS 18.4 → expanded 2025)

AI-generated 100–300 character summaries of user reviews. U.S. English first, expanded through 2025. Not directly an ASO surface but affects conversion. The skill doesn't generate these.

## Apple Search Ads "Search Popularity" collapse (Sept 29, 2025)

The 0–100 SAP score that the ASO industry retrofitted from Apple Ads as a search-volume proxy stopped working:
- ~77% of U.S. keywords with SAP > 5 collapsed to "5"
- Apple introduced a beta **Monthly Search Term Rank Report** in Apple Ads Insights, but it only surfaces keywords with legacy SAP ≥ 35 and uses a non-comparable monthly methodology

**Implication:** the skill must NOT rely on legacy 1–5 / 0–100 SAP scores. Free fallbacks:
- App Store autocomplete (Apple-direct, reliable)
- App Store search-results-count + which apps rank for a term (use as a difficulty heuristic)
- APPlyzer's independent search-score model (survived the collapse because it doesn't use Apple's API)

## Screenshot sizes (current 2025–2026 requirements)

| Device | Resolution | Required? |
|---|---|---|
| iPhone 6.9″ (15/16/17 Pro Max) | 1320 × 2868 | **Primary required since Sept 2024** |
| iPhone 6.5″ (XS Max class) | 1242 × 2688 | Alternative to 6.9″ |
| iPhone 6.7″ (14/15/16 Plus, 14 Pro Max) | 1290 × 2796 | Optional, recommended |
| iPad 13″ (M4) | 2064 × 2752 | Required if iPad-supported |
| iPad 12.9″ | 2048 × 2732 | Fallback |
| Apple Watch (Series 10/11) | 416 × 496 | Required if watchOS target |

Up to 10 screenshots per device per locale. **Only the first 3 appear in search results** — highest-leverage assets in the entire listing.

## Screenshot caption text — is it indexed?

Per WWDC25, screenshot text is read by Apple's AI to generate App Store Tags (browse-discovery, semantic). This is **not** the same as the rumored OCR-keyword indexing some third parties (Appfigures) initially claimed.

**Treat screenshot text as a semantic signal:** write captions in plain English that reinforce 3–5 core keywords. Don't keyword-stuff captions.

## Keyword field display change (WWDC25)

During WWDC25 demos Apple showed keyword fields with 107 characters instead of 100. Was *not* officially confirmed as a limit increase; some interpret it as Apple no longer counting commas (which would functionally extend the field). **As of May 2026 the official Apple App Store Connect Help still documents 100 characters.** The skill respects 100 chars as the safe limit and flags the ambiguity in research notes if relevant.

## Offer codes expanded (2025)

Now available for consumables, non-consumables, and non-renewing subscriptions (previously subscriptions only). Up to 10 active offers per IAP, up to 1M codes per app per quarter. Not an ASO field.

## App Analytics expansion (2025)

100+ new metrics added including cohort tracking, MRR, source-attribution breakdowns. Use these for the 4-week iteration cycle described in the output template's Iteration Plan section.

## Games app (iOS 26)

Separate pre-installed games discovery app with Home, Play Together, Library, Arcade, Search sections. Games-category apps get an additional discovery surface. Non-game apps unaffected.

## iOS 26 SDK requirement

**Mandatory for new App Store submissions starting April 28, 2026** (Xcode 26 SDK). Apps can opt out of Liquid Glass aesthetics via `UIDesignRequiresCompatibility` in `Info.plist` temporarily — this is a transitional flag, not a permanent solution.

**Not an ASO metadata field.** Mention in research notes if relevant to the developer's submission window.

## Apple Intelligence / on-device LLM in discovery

- App Store Tags is the headline AI feature in discovery
- Apple has not (publicly) replaced keyword-search ranking with an LLM, but the **browse** surface is increasingly LLM-driven
- The **Foundation Models framework** (iOS 26) gives third-party apps access to a 3B-parameter on-device LLM. This is a developer feature, not an ASO field. If an app uses it, `Apple Intelligence`, `on-device AI`, `private AI` are fair keyword candidates — but only if the app meaningfully uses these technologies. Apple Review may push back on metadata that name-drops Apple's tech without genuine integration.

## "Liquid Glass" / iOS 26 keywords

`Liquid Glass`, `iOS 26`, `Apple Intelligence` are NOT keywords the skill should automatically include unless the app meaningfully showcases those technologies. Treat them as opt-in flags surfaced in research notes only when codebase signals (e.g., Foundation Models framework usage, glass effect adoption) justify them.

## ASA ↔ organic ASO interaction (2026 best practice)

Apple's official position: ASA does not directly influence organic ranking.

Empirical reality (AppTweak, App Radar, SplitMetrics, Phiture, ASOMobile case studies):
- ASA drives downloads + tap-through-rate on specific keywords
- Downloads + TTR + conversion ARE organic ranking signals
- Therefore ASA *indirectly* lifts organic ranking on bid-on keywords
- Cannibalization risk: paid traffic can eat what would have been free organic traffic

**Workflow:** Build ASO foundation first → run an ASA Discovery campaign to surface match-discovered keywords → promote winners to exact-match → feed learnings back into the Keywords field. The same keyword set the skill produces is the ASA Discovery seed.
