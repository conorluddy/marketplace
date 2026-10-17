# Guideline 5: Legal (condensed snapshot)

Snapshot taken 2026-10-17 from https://developer.apple.com/app-store/review/guidelines/ — paraphrased. Verify borderline items live.

## 5.1 Privacy
- **5.1.1(i)** Privacy policy linked in App Store Connect and in-app; states what is collected, how, all uses; confirms third parties give equal protection; covers retention, deletion, consent revocation. [BOTH]
- **5.1.1(ii)** Consent before collecting any user/usage data, even anonymous; paid functionality must not depend on granting access; easy withdrawal; clear and complete purpose strings. [BOTH]
- **5.1.1(iii)** Data minimization: request only what core functionality needs; prefer pickers/share sheets over full Photos or Contacts access. [CODE]
- **5.1.1(iv)** Don't trick or force unnecessary permissions; offer alternatives when permission is declined (e.g. manual address entry). [BOTH]
- **5.1.1(v)** Account sign-in [BOTH]: without significant account features, allow use without login. If account creation is supported, **in-app account deletion is required**. Don't require personal info unless core/legal. Social-network-tied core features justify login; profile pulls, sharing and invites are not core. Provide in-app revocation of social credentials; don't store social tokens off-device.
- **5.1.1(vi)** No surreptitious password/private-data discovery.
- **5.1.1(vii)** SafariViewController must be visible, not hidden, and must not track without consent. [BOTH]
- **5.1.1(viii)** Don't compile personal info from other sources without explicit consent, even public databases.
- **5.1.1(ix)** Regulated fields (banking, healthcare, gambling, legal cannabis, air travel, crypto exchanges) must be submitted by a legal entity; cannabis geo-restricted.
- **5.1.1(x)** Name and email requests must be optional; features not conditional on them. [BOTH]
- **5.1.2(i)** Permission before using/sharing personal data; disclose third-party sharing including third-party AI and get explicit permission; use App Tracking Transparency for tracking; don't require enabling push, location or tracking to use the app. [BOTH]
- **5.1.2(ii)** No repurposing of data without further consent. **(iii)** No covert profiling or re-identifying anonymized data.
- **5.1.2(iv)** No contact databases from Contacts/Photos; no collecting installed-app lists for analytics/ads. [CODE]
- **5.1.2(v)** Messaging from Contacts/Photos only on explicit individual initiative: no Select All, no default selections, preview the message and sender.
- **5.1.2(vi)** HomeKit, HealthKit, Clinical Health Records, MovementDisorder, ClassKit and depth/face-mapping data may not be used for marketing, advertising or data mining. [BOTH]
- **5.1.2(vii)** Apple Pay data shared only to facilitate or improve delivery of goods/services.
- **5.1.3 Health** [BOTH]: (i) health/fitness/medical research data not to third parties or ads/marketing/data mining, except to improve health management or research with permission; disclose specific data collected. (ii) don't write false data to HealthKit; no personal health info in iCloud. (iii) research needs informed consent (parent/guardian for minors). (iv) independent ethics review approval.
- **5.1.4 Kids** [BOTH]: (a) follow COPPA/GDPR; birthdate/parent contact only as law requires; kid-focused apps have no third-party analytics or advertising; useful regardless of age. (b) exceptions only per 1.3; Kids Category or minors' data need a privacy policy; a parental gate is not parental consent; no "For Kids" wording outside the Kids Category.
- **5.1.5 Location** [BOTH]: only when directly relevant; not for emergency services or autonomous vehicle control (small drones/toys excepted); consent and in-app purpose explanation.

## 5.2 Intellectual property [HUMAN unless noted]
5.2.1 own or license all content; no copycat names/metadata. 5.2.2 third-party service content must be permitted by that service's terms. 5.2.3 no facilitating illegal file sharing or unauthorized media downloading (YouTube, SoundCloud, Vimeo, Apple Music) [BOTH]. 5.2.4 don't imply Apple endorsement. 5.2.5 don't resemble Apple products/interfaces or use Apple ad themes; no Apple emoji in apps/keyboards/sticker packs; Activity rings must not visualize Move/Exercise/Stand data confusingly; WeatherKit attribution. [BOTH]

## 5.3 Gaming, gambling, lotteries
Regulated; vet laws everywhere you ship. 5.3.1 sweepstakes sponsored by the developer. 5.3.2 official rules in-app, Apple not a sponsor. 5.3.3 no IAP for real-money gaming credits. 5.3.4 real-money gaming/lotteries need licensing, geo-restriction and a free download. [BOTH]

## 5.4 VPN apps / 5.5 MDM [BOTH]
Use `NEVPNManager`; organization accounts only; clear in-app data declaration before purchase/use; no selling or disclosing data; MDM capability must be requested from Apple and limited to enterprises, schools and government (plus narrow parental-control/security uses).

## 5.6 Developer Code of Conduct
Respect everyone; no manipulation or fraud; no deceptive pricing or charging for undelivered features. 5.6.1 use the provided review-prompt API; custom review prompts disallowed [BOTH]. 5.6.2 accurate developer identity. 5.6.3 no discovery fraud. 5.6.4 excessive complaints, bad reviews or refunds can count against standing.
