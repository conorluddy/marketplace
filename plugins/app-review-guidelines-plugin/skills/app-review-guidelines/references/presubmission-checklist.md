# Pre-submission checklist (things code can't prove)

Walk the groups with the user; ask for confirmation rather than assuming. Skip groups that don't apply. Guideline numbers in brackets.

## App Review Information
- [ ] Demo account credentials work today, and the backend will stay live during review [2.1(a)]
- [ ] Review notes explain non-obvious flows, hardware requirements, hidden or region-specific features, and how to reach IAP items [2.1, 2.3.1]
- [ ] Contact details for the reviewer are current

## Metadata
- [ ] Screenshots and previews show the app in use, match the real experience, and suit the age rating [2.3.3, 2.3.4, 2.3.8]
- [ ] Description, name and keywords make no unavailable-feature claims, price mentions, keyword stuffing, or other-platform references [2.3.1, 2.3.7, 2.3.10]
- [ ] Age rating questionnaire answered honestly; category is the most appropriate [2.3.5, 2.3.6]
- [ ] What's New describes significant changes [2.3.12]
- [ ] Support URL works and gives a real way to reach you; privacy policy URL works [1.5, 5.1.1(i)]

## Privacy
- [ ] App Privacy ("nutrition") labels match what the app and its SDKs actually collect [5.1.1, 5.1.2]
- [ ] `PrivacyInfo.xcprivacy` present for the app and every third-party SDK that requires one
- [ ] Privacy policy covers collection, use, third parties, retention, deletion, and consent revocation [5.1.1(i)]
- [ ] If tracking: ATT prompt and `NSUserTrackingUsageDescription` present; labels declare tracking [5.1.2(i)]

## Payments
- [ ] IAP products are attached to this version, have review screenshots, and are in a reviewable state [2.1(b)]
- [ ] Subscription paywall shows price, period, auto-renew, how to cancel, and Terms/Privacy links [3.1.2, 4.9]
- [ ] Restore Purchases is reachable [3.1.1]
- [ ] No external payment calls to action unless covered by an entitlement and eligible storefront [3.1.1(a)]

## Accounts and content
- [ ] In-app account deletion exists if accounts can be created [5.1.1(v)]
- [ ] Sign in with Apple or equivalent offered when a third-party login is primary, unless exempt [4.8]
- [ ] UGC apps: report, block, filtering, moderation process, visible contact info [1.2]
- [ ] Kids / health / medical apps: reviewed against 1.3, 1.4.1, 5.1.3, 5.1.4 with the user

## Build
- [ ] Tested on a physical device on the latest iOS, including iPad if the app runs there [2.1, 2.4.1]
- [ ] No placeholder text, dead links, debug menus or test data in the release build [2.1(a)]
- [ ] Release build matches what the notes describe; no remote flag enables unreviewed features [2.3.1, 2.5.19]
- [ ] Export compliance / encryption questions answered
- [ ] Regional or legal obligations checked for every storefront you ship to [5]
