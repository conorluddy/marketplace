# Guideline 4: Design (condensed snapshot)

Snapshot taken 2026-10-17 from https://developer.apple.com/app-store/review/guidelines/ — paraphrased. Verify borderline items live.

- **4.1** (a) copycats: be original, no cosmetic re-skins; (b) impersonation; (c) don't use another developer's icon, brand or product name without approval. [HUMAN]
- **4.2 Minimum functionality** [HUMAN]: must go beyond a repackaged website; useful, unique or app-like.
  - 4.2.1 AR must be rich and integrated. 4.2.2 not primarily marketing/aggregator/link collections (catalogs excepted). 4.2.3 (i) must work standalone; (ii) first-launch downloads need disclosed size and a prompt [BOTH]. 4.2.6 template/generated apps rejected unless submitted by the content provider. 4.2.7 remote desktop client rules.
- **4.3 Spam**: (a) no multiple bundle IDs for one app (per city/team); use one app with IAP variants; (b) no near-duplicates; saturated categories (dating, flashlight, sound effects, wallpaper, simple timers, fortune-telling) need a meaningfully different experience. [HUMAN]
- **4.4 Extensions** [BOTH]: follow extension docs; disclose accurately; no marketing, ads or IAP inside extensions.
  - 4.4.1 Keyboards [CODE]: real keyboard input, next-keyboard control, works without Full Access/network; collect activity only to improve the keyboard; don't launch other apps or repurpose keys.
  - 4.4.2 Safari extensions [CODE]: current Safari, no interference with system/Safari UI, minimal site access.
- **4.5 Apple sites and services**:
  - 4.5.1 [CODE] approved RSS feeds only; no scraping Apple sites.
  - 4.5.2 MusicKit [BOTH]: user-initiated playback with standard controls; no payment gating or indirect monetization of Apple Music; purpose string must disclose playlist/favorites access; data only to support/improve the app.
  - 4.5.3 no spam via Game Center, push or Live Activities.
  - 4.5.4 Push [BOTH]: not required for function; no sensitive data in payloads; promotional push needs in-app opt-in and opt-out.
  - 4.5.5 Game Center Player IDs [CODE]: don't display or share.
  - 4.5.6 Apple emoji [CODE]: fine in-app and metadata, not embedded in binary or used on other platforms.
- **4.7 Mini apps, games, chatbots, emulators** [HUMAN/BOTH]: hosted software is your responsibility. Requires privacy compliance (5.1), content filtering/reporting/blocking, digital goods via 3.1 (4.7.1); no exposing native APIs without permission (4.7.2); consent per instance for sharing data/permissions (4.7.3); index with universal links (4.7.4); age-restriction mechanism (4.7.5).
- **4.8 Login services** [BOTH]: if a third-party or social login sets up or authenticates the primary account, also offer an equivalent option that limits data to name and email, lets users keep email private, and doesn't collect app interactions for ads without consent. Exemptions: only your own company's sign-in; alternative marketplaces; education/enterprise/business apps requiring an existing account; government or industry digital ID; clients for a specific third-party service where users sign in directly. *Check exemptions on the live page before flagging.*
- **4.9 Apple Pay** [BOTH]: disclose material purchase info before sale; correct Apple Pay branding; recurring payments disclose renewal term, per-period benefits, charges and how to cancel.
- **4.10** Don't charge for built-in hardware/OS capabilities or Apple services (push, camera, gyroscope, Apple Music access, iCloud storage, Screen Time APIs). [BOTH]
- Intentionally omitted by Apple: 4.2.4, 4.2.5, 4.4.3, 4.6.
