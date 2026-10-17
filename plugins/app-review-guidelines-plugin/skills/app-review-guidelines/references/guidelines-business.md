# Guideline 3: Business (condensed snapshot)

Snapshot taken 2026-10-17 from https://developer.apple.com/app-store/review/guidelines/ — paraphrased. Payments rules vary by storefront and entitlement and change often; verify against the live page before asserting anything about external links.

## 3.1 Payments
- **3.1.1 In-App Purchase** [BOTH]: unlocking features, currency, levels or premium content uses IAP — not license keys, AR markers, QR codes or crypto. Tipping via IAP is allowed. Purchased credits must not expire. A restore mechanism is required. Loot-box odds disclosed before purchase. Digital gift cards sold in-app use IAP. Free trials: Non-Consumable at tier 0 named "XX-day Trial", with duration and lost access disclosed. NFT ownership must not unlock features.
- **3.1.1(a)** Links to other purchase methods [BOTH]: allowed only with the StoreKit External Purchase Link entitlement (or Music Streaming entitlement) in permitted storefronts/platforms. Elsewhere, no buttons or calls to action pointing to other purchase methods. Misuse of the entitlement can get the app removed. *Highly region- and date-sensitive: always verify.*
- **3.1.2 Subscriptions** [BOTH]:
  - (a) ongoing value, at least 7 days, works on all the user's devices; no extra tasks (posts, check-ins) required; existing buyers keep functionality when moving to subscriptions.
  - (b) seamless upgrade/downgrade; no accidentally subscribing to several variants (use subscription groups).
  - (c) before asking for a subscription, clearly describe what the price buys [HUMAN].
- **3.1.3 Other purchase methods** [HUMAN]: (a) Reader apps (previously purchased content; informational link needs the External Link Account entitlement outside the US); (b) multiplatform services, only if the same items are also sold via IAP; (c) enterprise services sold to organizations; (d) person-to-person real-time services, one-to-one may use non-IAP, one-to-few/many must use IAP; (e) physical goods/services consumed outside the app use Apple Pay or cards; (f) free stand-alone companion apps; (g) advertising management apps.
- **3.1.4** Hardware-specific content may unlock without IAP; optional physical add-ons need an IAP alternative.
- **3.1.5** Cryptocurrencies [HUMAN, mining partly CODE]: wallets from organizations only; no on-device mining; exchanges where licensed; ICOs only via established institutions; no currency for completing tasks.

## 3.2 Other business
- **3.2.1 Acceptable** [HUMAN]: promoting your own apps, curated third-party collections with editorial content, rental expiry, Wallet passes, free insurance apps, approved nonprofit fundraising with Apple Pay, optional person-to-person gifts (100% to recipient), financial apps submitted by the institution.
- **3.2.2 Unacceptable**: (i) App Store-like storefronts; (iii) inflating ad impressions; (iv) in-app charity fundraising unless approved nonprofit; (v) arbitrary location/carrier restrictions [BOTH]; (vii) manipulating visibility/rank on other services; (viii) binary options, unlicensed CFD/FOREX; (ix) personal loans must disclose all terms, max APR ≤36%, no repayment in ≤60 days; (x) forcing ratings, reviews or downloads to unlock functionality [BOTH] (incentives like completing a level or watching an ad are fine).
- 3.2.2(ii) and (vi) are intentionally omitted by Apple.
