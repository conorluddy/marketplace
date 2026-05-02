# Codebase Signal Extraction

How to mine an iOS Swift/SwiftUI codebase for ASO signal. Sources are ranked by signal density.

## Tier 1 — Direct user-facing copy and explicit metadata

### `fastlane/metadata/en-US/`
If this directory exists, the developer already drafted ASO. Files:
- `name.txt`, `subtitle.txt`, `keywords.txt`, `description.txt`, `release_notes.txt`, `promotional_text.txt`

**Action:** Treat existing values as the source of truth. Propose refinements with a diff, not a rewrite.

### `Info.plist` and merged build settings
Highest-signal keys:
- `CFBundleDisplayName` — home-screen label, often the cleanest brand token
- `CFBundleName` — fallback brand
- `NSHumanReadableCopyright` — sometimes contains a tagline
- `NS*UsageDescription` strings — these explain to the user *why* the app needs each permission. Goldmine for feature/use-case keywords:
  - `NSCameraUsageDescription`, `NSMicrophoneUsageDescription`, `NSPhotoLibraryUsageDescription`, `NSLocationWhenInUseUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription`, `NSHealthShareUsageDescription`, `NSHealthUpdateUsageDescription`, `NSContactsUsageDescription`, `NSCalendarsUsageDescription`, `NSRemindersUsageDescription`, `NSMotionUsageDescription`, `NSBluetoothAlwaysUsageDescription`, `NSFaceIDUsageDescription`, `NSAppleMusicUsageDescription`, `NSSpeechRecognitionUsageDescription`, `NSUserTrackingUsageDescription`, `NSNearbyInteractionUsageDescription`
- `CFBundleURLTypes` — deep-link handlers, often mirror feature areas
- `UIApplicationShortcutItems` — quick action labels (verbatim feature names)
- `UTExportedTypeDeclarations` / `UTImportedTypeDeclarations` — supported document types (`.gpx`, `.usdz`, `.heic` → category signal)
- `LSApplicationQueriesSchemes` — apps the app integrates with (`whatsapp`, `tg`, etc.)
- `NSAppTransportSecurity` — exception domains reveal third-party services
- `WKAppBundleIdentifier` — watchOS support

### `Localizable.strings`, `Localizable.stringsdict`, String Catalogs (`*.xcstrings`)
The single highest-density source of user-facing copy. Every button label, navigation title, onboarding line, empty-state, paywall string is here.

**Action:**
1. Tokenize all values in `en` / `en-US` / Base locales
2. Apply standard NLP stop-word filter PLUS Apple's stop-word list (see `rules.md`)
3. Frequency-rank
4. Surface top 30–50 as keyword candidates
5. Strings tagged for onboarding, paywall, or empty states are especially high-signal — they describe what the app does *for new users*

### README.md, CHANGELOG.md, marketing/
README usually has a "What is this app?" pitch in the first paragraph. CHANGELOG describes feature evolution.

## Tier 2 — Capabilities and platform integrations

Each capability is itself a keyword candidate.

### Entitlements (`*.entitlements`)
| Entitlement | Keyword candidates |
|---|---|
| `com.apple.developer.healthkit` | health, fitness, workout, activity, heart, steps |
| `com.apple.developer.homekit` | smart home, automation, homekit |
| `com.apple.developer.icloud-services` (CloudKit) | sync, backup, cloud, cross-device |
| `com.apple.developer.applesignin` | sign in with apple, login |
| `com.apple.developer.in-app-payments` (Apple Pay) | payments, checkout, pay |
| `com.apple.developer.associated-domains` | universal links, web |
| `com.apple.developer.networking.wifi-info` | wifi, network |
| `com.apple.developer.contacts.notes` | contacts, address |
| `com.apple.developer.weatherkit` | weather, forecast |
| `com.apple.developer.shared-with-you` | messages, sharing |
| `aps-environment` | notifications, alerts, reminders |
| `com.apple.developer.maps` | maps, location, navigation |
| `com.apple.security.application-groups` | (architecture only — not a keyword) |
| `com.apple.developer.driverkit` | accessory, hardware |
| `com.apple.developer.car-play` | carplay, driving |
| `com.apple.developer.matter.allow-setup-payload` | matter, smart home |
| `com.apple.developer.media-device-discovery-extension` | cast, airplay, media |

### Xcode capabilities
- Widgets (WidgetKit) → `widget`, `home screen`, `lock screen`
- Live Activities (ActivityKit) → `live activity`, `dynamic island`
- App Clips → `app clip`, `instant`
- Background Modes:
  - background audio → `podcast`, `audiobook`, `music`, `meditation`
  - location updates → `tracking`, `gps`
  - VoIP → `calls`, `voip`
  - BLE central → `bluetooth`, `device`

### `PrivacyInfo.xcprivacy`
The `NSPrivacyCollectedDataTypes` array describes the app's domain. Values like `Health & Fitness`, `Financial Info`, `Location`, `Messages`, `Browsing History`, `Audio Data`, `Photos or Videos` map directly to keyword categories.

## Tier 3 — Feature surface area

### App Intents
- `AppIntent` — `title`, `description`, `predictionConfiguration` strings are explicitly user-facing labels for Siri/Spotlight/Shortcuts. Pure ASO gold.
- `AppShortcutsProvider` registered phrases — verbatim user actions ("Log a workout in Slopes")
- Intent parameter names — nouns the app cares about (`trail`, `run`, `transaction`, `recipe`)

### StoreKit (`*.storekit`, `Products.plist`)
- IAP product IDs and titles (`pro_yearly`, `unlock_pro`, `tip_jar`) reveal monetization model
- Subscription group names hint at premium feature areas
- The IAP titles themselves become the IAP Display Names in the output (≤30 chars each); descriptions cap at 45

### SwiftUI / UIKit views and module structure
- `Sources/Workouts/`, `Modules/AIChat/`, `Features/Mapping/` — module names ARE feature names
- Top-level view names: `WorkoutLogView`, `RecipeFinderView`, `MapNavigationView` → tokenize the camelCase

### Core Data / SwiftData entities
- Entity names like `Workout`, `Run`, `Trail`, `Recipe`, `Transaction`, `Highlight`, `Bookmark`, `Habit`, `Goal` describe domain objects directly
- Attribute names add nuance: `distance`, `pace`, `vertical`, `caloriesBurned`

### `Package.swift` / Podfile / SPM dependencies
SDK → capability mapping:

| Dependency | Implies |
|---|---|
| RevenueCat | subscriptions, paywall |
| Superwall | paywall |
| PostHog, Amplitude, Mixpanel, Segment | analytics (do NOT use as keywords) |
| Sentry, Crashlytics, Bugsnag | crash reporting (not keywords) |
| Stripe | payments (digital-goods caveat with Apple IAP rules) |
| Firebase | backend, messaging, analytics |
| Supabase, PocketBase | backend |
| Mapbox, MapLibre | maps, navigation |
| KeychainAccess | security, password |
| HealthKit (system) | fitness, health, workout |
| WatchConnectivity (system) | apple watch |
| MusicKit | music, apple music |
| WeatherKit | weather, forecast |
| Vision, CoreML, MLX | ai, image recognition, on-device |
| OpenAI, Anthropic, LangChain.swift | ai, chat, assistant |
| ARKit, RealityKit | ar, augmented reality, 3d |
| AVFoundation (with camera) | video, recorder |
| PhotosUI / PHPicker | photos, library |
| MessageUI | email, sms |
| LiveKit, Agora, Twilio | calls, video chat, real-time |
| WidgetKit (system) | widgets |

### Asset catalog (`Assets.xcassets`)
Image set names — onboarding illustrations are often named after the feature they illustrate (`onboarding_workout_tracking`).

### XCConfig / build settings
- `MARKETING_VERSION`, `PRODUCT_BUNDLE_IDENTIFIER`, deployment target

## Tier 4 — Tests and accessibility

- Snapshot test names: `test_recordingScreen_whenSessionActive_showsLiveStats`
- UI test selectors / accessibility identifiers — user-facing labels

## Synthesis

After scanning, build:

1. **Feature inventory** = union of (Localizable strings + entitlements + IAP names + intent titles + dependency capabilities + Core Data entities + module names)
2. **Keyword candidate pool** = tokenize all the above, frequency-rank after stop-word filter
3. **App archetype** (fitness / productivity / social / finance / AI / photo / game-genre / etc.) inferred from the dominant signal cluster — drives category
4. **Target audience** inferred from intent phrasing, IAP pricing tier, onboarding copy
5. **Brand name** by precedence: fastlane > `CFBundleDisplayName` > `CFBundleName` > Xcode target name > README first heading
