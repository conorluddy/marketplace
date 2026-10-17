# Guidelines 1–2: Safety and Performance (condensed snapshot)

Snapshot taken 2026-10-17 from https://developer.apple.com/app-store/review/guidelines/ — paraphrased, not verbatim. Verify against the live page for anything borderline. `[CODE]` checkable in source/plists, `[HUMAN]` judgement or App Store Connect work, `[BOTH]` partly each.

## 1. Safety
- **1.1** Objectionable content [HUMAN]. Sub-rules: 1.1.1 discriminatory; 1.1.2 realistic violence; 1.1.3 weapons; 1.1.4 sexual content; 1.1.5 inflammatory religious commentary; 1.1.6 false information/prank features (a "for entertainment" disclaimer doesn't exempt); 1.1.7 exploiting current events.
- **1.2** User-generated content [BOTH]: content filtering, report mechanism with timely response, block abusive users, published contact info.
  - **1.2.1** Creator content [HUMAN]: moderated; must not change core app features. **(a)** age-gate/flag content above the app's rating [BOTH].
- **1.3** Kids Category [BOTH]: no external links, purchase prompts or distractions outside a parental gate; no personal/device data to third parties; generally no third-party analytics or ads.
- **1.4** Physical harm [HUMAN]: 1.4.1 medical apps (disclose methodology, remind users to consult a doctor); 1.4.2 dosage calculators need an approved source; 1.4.3 no encouraging tobacco/vape/drugs/excess alcohol; 1.4.4 DUI checkpoints only from law enforcement; 1.4.5 no risky challenges.
- **1.5** Developer information [HUMAN]: easy, accurate contact method in app and Support URL.
- **1.6** Data security [BOTH]: appropriate protection of user data (ATS, Keychain, data protection).
- **1.7** Crime reporting apps [HUMAN]: local law-enforcement involvement.

## 2. Performance
- **2.1(a)** App completeness [HUMAN]: final build, no placeholder content, working URLs, demo credentials with live backend, no crashes.
- **2.1(b)** IAP completeness [BOTH]: items complete, visible and functional for the reviewer; explain hidden ones in review notes.
- **2.2** Beta testing [HUMAN]: no demos/betas/trials on the store; use TestFlight.
- **2.3** Accurate metadata [HUMAN]: matches real core experience.
  - 2.3.1 describe new features in review notes, no unavailable-feature promises; hidden/undocumented features violate it.
  - 2.3.2 say which items need extra purchase; handle payment observer so purchases complete at launch [BOTH].
  - 2.3.3 screenshots show the app in use; 2.3.4 previews are app captures; 2.3.5 category; 2.3.6 honest age rating; 2.3.7 name ≤30 chars, no keyword stuffing or prices; 2.3.8 4+-appropriate imagery, "For Kids" reserved for Kids Category; 2.3.9 rights to assets, fictional account data; 2.3.10 no references to other mobile platforms; 2.3.11 pre-orders; 2.3.12 What's New accuracy; 2.3.13 in-app events; 2.3.14 creative assets.
- **2.4.1** iPad: iPhone apps should run on iPad where possible [CODE].
- **2.4.2** Power/heat [BOTH]: no battery drain, excessive writes, or unrelated background work (e.g. crypto mining).
- **2.4.4** Never suggest restarting the device or changing unrelated system settings.
- **2.4.5** Mac App Store requirements [CODE]: sandbox, no auto-launch without consent, no root/setuid, no license screens, current OS.
- **2.5.1** Public APIs only, on the current OS; frameworks used for their intended purpose [CODE].
- **2.5.2** Self-contained bundle; no downloading/executing code that changes features [CODE].
- **2.5.3** No harmful code [HUMAN].
- **2.5.4** Background services only for intended purposes [CODE] (`UIBackgroundModes`).
- **2.5.5** Must work on IPv6-only networks [HUMAN].
- **2.5.6** Web browsing apps use WebKit unless holding the alternative-engine entitlement (EU/Japan) [CODE].
- **2.5.8** No alternate desktop/home-screen environments.
- **2.5.9** Don't alter hardware switches or native UI behaviour [BOTH].
- **2.5.11** SiriKit/Shortcuts: register only intents you can fulfil; no ads in responses [BOTH].
- **2.5.12** CallKit/SMS filters block only confirmed spam; describe blocking in marketing text [BOTH].
- **2.5.13** Face recognition auth: prefer LocalAuthentication; under-13s need an alternative [BOTH].
- **2.5.14** Recording needs explicit consent and a visible/audible indicator [BOTH].
- **2.5.15** File-browsing apps include Files app and iCloud documents [CODE].
- **2.5.16** Widgets, extensions, notifications relate to app content; App Clip features in the main binary; no ads in App Clips [BOTH].
- **2.5.17** Matter pairing via Apple's Matter framework [CODE].
- **2.5.18** Display ads only in the main binary (not extensions, widgets, App Clips, keyboards, watchOS); ads suit the age rating, labelled, closable, reportable [BOTH].
- **2.5.19** No hidden, dormant or undocumented features; no obfuscation to hide them [BOTH].
- 2.5.7 and 2.5.10 are intentionally omitted by Apple.
