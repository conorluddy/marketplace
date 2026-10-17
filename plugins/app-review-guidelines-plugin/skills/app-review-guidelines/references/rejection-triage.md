# Rejection triage patterns

Common causes behind frequently cited guidelines, and whether the fix needs a new binary. These come from the guideline text plus common App Review practice; treat "typical cause" as a lead to verify, not a diagnosis.

| Cited | Typical cause | Fix | New binary? |
|---|---|---|---|
| **2.1(a)** App completeness — crash / bug | Crash on a device or iOS version the reviewer used (often iPad or latest OS); reviewer couldn't log in | Reproduce with the reviewer's device class; fix crash; attach symbolicated log if provided | Usually yes |
| **2.1(a)** — demo account | No credentials, expired credentials, or backend down/geo-blocked | Supply working demo account in App Review Information; keep the backend live during review | No |
| **2.1(a)** — can't find feature | Feature hidden behind a hardware requirement or flow the reviewer couldn't trigger | Add numbered steps or a short screen recording in review notes | No |
| **2.1(b)** IAP not found | IAP products not attached to the version, in "Missing Metadata", or hidden behind a state | Attach products to the submission; explain how to reach them in notes | Sometimes |
| **2.3.x** Accurate metadata | Screenshots show non-app content; description promises features that don't exist; wrong age rating; competitor/other-platform references | Correct metadata in App Store Connect | No |
| **2.3.1** hidden features | Remote flags enable unreviewed functionality | Disclose in notes or remove | Maybe |
| **3.1.1** IAP | Digital goods unlocked by external payment, code entry, or links to a website | Move unlock to StoreKit, or qualify for a specific exception and cite it | Yes |
| **3.1.1** — restore | No Restore Purchases control | Add `AppStore.sync()` button in settings/paywall | Yes |
| **3.1.2** Subscriptions | Missing price/period/renewal/cancel text or Terms/Privacy links on the paywall | Add disclosures before the purchase button | Yes |
| **4.0 / 4.2** Minimum functionality | App is a thin web wrapper or single-feature trivial app | Add native functionality, or explain unique value with evidence | Usually yes |
| **4.3(a)/(b)** Spam | Multiple near-identical bundle IDs, or clone of a saturated category | Consolidate; show meaningful differentiation | Maybe |
| **4.8** Login services | Third-party login without an equivalent privacy-preserving option | Add Sign in with Apple (or a compliant equivalent), or document an exemption | Yes |
| **5.1.1(i)** Privacy policy | Missing or unreachable policy URL, or policy lacks required content | Fix URL in App Store Connect and in-app | Maybe |
| **5.1.1(ii) / (iv)** Permissions | Vague purpose string; permission requested before context; feature blocked when declined | Rewrite purpose strings to say *why*; defer prompt to first use; add a fallback | Yes |
| **5.1.1(v)** Account deletion | Account creation but no in-app deletion | Add deletion flow that deletes the account and data (not just deactivation) | Yes |
| **5.1.2** ATT / tracking | Tracking SDKs without ATT prompt, or manifest mismatches reality | Add ATT or remove tracking; reconcile privacy labels and `PrivacyInfo.xcprivacy` | Yes |
| **1.2** UGC | No report/block/filter/contact path | Add report + block, moderation process, support contact | Yes |
| **1.3 / 5.1.4** Kids | Third-party analytics/ads or external links without parental gate | Remove SDKs; add parental gate | Yes |
| **2.5.1** Non-public API | Private selector or API from an SDK | Identify offending symbol (often in a third-party SDK); update or remove | Yes |
| **ITMS-9xxxx** emails | Not a review rejection: validation warnings (missing purpose string, required-reason API without manifest entry) | Fix the plist/manifest; usually blocks the next upload | Yes |

## Reading the message
- Apple often quotes **what the reviewer saw** ("we were unable to locate...", "your app crashed on iPad Air running iOS ..."). Reproduce that exact context first.
- Look for **"Next Steps"**: sometimes the message says metadata-only, sometimes requires a new binary.
- Multiple guidelines in one rejection are common. Address all of them in the reply.

## Drafting the Resolution Center reply
Short, specific, polite. Structure:
1. One-line acknowledgement referencing the guideline number.
2. What changed (build number if new) or where to find the feature (numbered steps).
3. Anything the reviewer needs: demo credentials, hardware caveat, region restrictions.
4. For a disputed rejection: a calm, evidence-based explanation. Mention that you are happy to provide more information; the App Review Board appeal exists but do not threaten it.

Template:
```
Hello,

Thank you for the feedback on Guideline <n.n.n>.

<What was changed / where to find it:>
1. Open <screen> …
2. Tap <control> …

<Build N.N (M) addresses this by … / No binary change is needed; we updated <metadata item>.>

Demo account: <username> / <password> (backend is live).

Please let us know if anything else is needed.
```
