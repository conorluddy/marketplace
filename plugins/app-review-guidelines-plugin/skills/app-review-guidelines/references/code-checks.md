# Code checks

Scan for these signals. "Risk" describes what would worry a reviewer; every item is advisory. Cite `file:line` for anything found.

## Always (every app)

| Look at | Guideline | Risk |
|---|---|---|
| `Info.plist` `NS*UsageDescription` vs. framework imports (`AVFoundation`, `CoreLocation`, `Photos`, `Contacts`, `HealthKit`, `CoreBluetooth`, `LocalAuthentication`, `Speech`, `EventKit`, `MediaPlayer`) | 5.1.1(ii), 2.1 | API used with no purpose string (crash on first access) or vague string ("needed for app") |
| Purpose strings with no matching code | 5.1.1(iii) | Requested access the app doesn't use |
| `PrivacyInfo.xcprivacy` exists; declares collected data, tracking, required-reason APIs (`UserDefaults`, file timestamp, disk space, system boot time) | 5.1.1, 5.1.2 | Missing manifest, or required-reason API used without declared reason; third-party SDKs missing their own manifests |
| `UIBackgroundModes` | 2.5.4 | Modes declared (`audio`, `location`, `voip`, `fetch`, `processing`) without matching functionality |
| `UIDeviceFamily` / iPad support | 2.4.1 | iPhone-only is allowed, but note it; layout breakage on iPad is a common 2.1 crash |
| Private API signals: `dlopen`, `NSClassFromString` on `_UI*`/`LSApplicationWorkspace`, `performSelector` with private selectors | 2.5.1 | Non-public API use |
| Downloaded executable code: `JSContext` evaluating remote scripts that change features, `dlopen` of downloaded dylibs | 2.5.2 | Runtime feature changes via downloaded code |
| `NSAppTransportSecurity` `NSAllowsArbitraryLoads` | 1.6 | Blanket ATS exemption needs justification |
| Placeholder content: `lorem ipsum`, `TODO`, `example.com`, `test@`, debug menus reachable in release (`#if DEBUG` leaks) | 2.1(a) | Incomplete build |
| `WKWebView`/`SFSafariViewController` as the whole app UI | 4.2 | Repackaged website |
| Custom review prompts (alerts asking for ratings) instead of `SKStoreReviewController`/`requestReview` | 5.6.1, 3.2.2(x) | Non-sanctioned review prompting, or gating features on a rating |
| Hidden or obfuscated features, remote-config flags that enable unreviewed features | 2.5.19, 2.3.1 | Features not described to review |
| Screen recording / mic / camera with no visible indicator or consent | 2.5.14 | Recording without clear consent |
| Alternate browser engine use (not WebKit) | 2.5.6 | Needs the regional entitlement |

## IAP / subscriptions

| Look at | Guideline | Risk |
|---|---|---|
| Unlock paths not backed by StoreKit: license keys, promo codes entered in-app, web-checkout buttons, Stripe/PayPal SDK for digital goods | 3.1.1, 3.1.1(a) | Digital goods sold outside IAP; external purchase links need the matching entitlement and eligible storefront |
| `Transaction.updates` / `SKPaymentTransactionObserver` registered at launch | 2.3.2, 3.1.1 | Purchases not completed on launch |
| Restore flow: `AppStore.sync()` or `restoreCompletedTransactions` reachable from UI | 3.1.1 | No restore mechanism |
| `.storekit` config / product definitions: subscription period ≥ 7 days, groups for variants | 3.1.2(a)–(b) | Short periods; overlapping subscriptions to the same thing |
| Paywall copy: price, period, auto-renew and cancel wording shown before purchase; links to Terms and Privacy | 3.1.2(c), 4.9 | Missing subscription disclosure |
| Content gated behind "rate us", "share", "check in" | 3.1.2(a), 3.2.2(x) | Unlock by task rather than purchase |
| Consumable credits that expire; loot boxes without odds | 3.1.1 | Expiring purchased credits; undisclosed odds |
| Crypto/wallet/mining code | 3.1.5 | Mining on device; wallet needs org account |
| Ads SDKs (AdMob, AppLovin, Meta Audience Network) in extensions/widgets/App Clips | 2.5.18, 4.4 | Ads outside the main app binary |

## Accounts / social

| Look at | Guideline | Risk |
|---|---|---|
| Third-party login SDKs (`GoogleSignIn`, `FBSDKLoginKit`, `TwitterKit`, LinkedIn, WeChat) without `AuthenticationServices`/`ASAuthorizationAppleIDProvider` | 4.8 | Equivalent privacy-preserving login option may be required unless an exemption applies |
| Account creation present but no deletion flow (look for delete-account UI and a backend call) | 5.1.1(v) | Missing in-app account deletion |
| Login wall before any content, where login isn't central | 5.1.1(v) | Account required without significant account features |
| Mandatory name/email/phone fields | 5.1.1(x) | Optional basic info made required |
| Social tokens persisted to backend; no in-app way to revoke | 5.1.1(v) | Social credential handling |
| UGC: posting, comments, chat, uploads, but no report / block / filter / contact info | 1.2 | Missing UGC safeguards |
| Creator-content or hosted mini-app features | 1.2.1, 4.7 | Extra moderation and age-gating rules |
| Push: required for core function, promotional pushes without opt-in/opt-out, sensitive data in payloads | 4.5.4 | Push rules |
| Contacts/Photos used to message people with default selection or Select All | 5.1.2(v) | Bulk messaging from contacts |
| Contact upload / address-book harvesting | 5.1.2(iv) | Building contact databases |

## Sensitive data (health, kids, tracking, location)

| Look at | Guideline | Risk |
|---|---|---|
| `HealthKit`, `ClinicalHealthRecords`, `CoreMotion` data flowing to analytics/ads SDKs or your backend for marketing | 5.1.3(i), 5.1.2(vi) | Health data to third parties/marketing |
| Writes to HealthKit of unverified values; health data in iCloud/CloudKit/`NSUbiquitousKeyValueStore` | 5.1.3(ii) | Inaccurate writes; health data in iCloud |
| Medical/diagnostic claims in UI strings without disclaimer to consult a doctor | 1.4.1 | Medical accuracy scrutiny |
| `AppTrackingTransparency` import, `NSUserTrackingUsageDescription`, tracking domains in manifest, IDFA use without prompt | 5.1.2(i) | Tracking without ATT, or ATT prompt shown but features gated on it |
| Analytics/ad SDK list (Firebase Analytics, Amplitude, Mixpanel, Meta SDK, AppsFlyer, Adjust, Branch) in a Kids Category or kid-directed app | 1.3, 5.1.4 | Third-party analytics/ads in kids apps |
| Parental gate before external links or purchases in kids apps | 1.3 | Links/purchases outside a parental gate |
| Birthdate/parent email collection in kid-directed app | 5.1.4(a) | Only as required by law |
| Location: `CoreLocation` always-authorisation, `NSLocationAlwaysAndWhenInUseUsageDescription`, background location, location used for non-relevant purposes | 5.1.5, 2.5.4 | Always-on location without need |
| Face/biometric: ARKit face tracking for auth, no `LocalAuthentication` fallback | 2.5.13 | Use LocalAuthentication |
| Sharing data to third-party AI services (OpenAI, Anthropic, Google) | 5.1.2(i) | Disclosure and explicit permission needed |

## Extensions and special entitlements

| Look at | Guideline | Risk |
|---|---|---|
| Custom keyboard: `RequestsOpenAccess`, works without network, next-keyboard key | 4.4.1 | Keyboard rules |
| Safari extension permissions broader than needed | 4.4.2 | Over-broad host permissions |
| Widgets/Live Activities/App Clips with unrelated content, ads, or IAP | 2.5.16, 4.4 | Extension content rules |
| `NetworkExtension`/`NEVPNManager`, MDM entitlements, CallKit block lists | 5.4, 5.5, 2.5.12 | Org-account and data-use rules |
| MusicKit usage: playback not user-initiated, music behind paywall | 4.5.2 | Apple Music rules |
| Game Center IDs displayed or stored | 4.5.5 | ID handling |
| Real-money gaming/gambling code, in-app currency for gambling | 5.3 | Licensing and geo-restriction |
