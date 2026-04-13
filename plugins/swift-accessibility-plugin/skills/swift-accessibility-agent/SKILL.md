---
name: swift-accessibility-agent
description: Audit, fix, and initialise SwiftUI accessibility modifiers so your app is navigable by both VoiceOver users and AI agents. Use this skill whenever a user mentions accessibility audit, accessibility modifiers, making an iOS app navigable by agents, adding VoiceOver support, or coordinate tracking for SwiftUI.
compatibility: Requires Xcode project with SwiftUI views
allowed-tools: Bash(find:*) Read Write Edit Glob Grep
---

# Swift Accessibility Agent

Make SwiftUI apps fully navigable by VoiceOver, XCTest, and AI agents by ensuring every
interactive element carries the five accessibility properties: **identifier**, **label**,
**hint**, **value**, and **traits**.

## Why this matters

Most AI agents navigate iOS apps via screenshots — slow (~2-5s per step), expensive
(~1,600 image tokens per screenshot), and fragile. A fully populated accessibility tree
lets agents query structured text (~200-400 tokens), tap by identifier (deterministic),
and verify via logs — no vision model needed. The same work also makes the app properly
accessible to humans using VoiceOver, Switch Control, and Voice Control.

## Three modes

The user will tell you what they want, or you can suggest the right mode based on context.

### 1. `init` — Scaffold CoordinateTracker

Creates the `CoordinateTracker.swift` file in the project. This is the infrastructure
that lets agents query exact screen coordinates for any tracked element without screenshots.

**When to use**: First time setting up a project for agent navigation, or when the user
says "init", "set up tracking", or "add coordinate tracker".

**Steps**:

1. Ask the user where Swift source files live (e.g. `Sources/`, `App/`, etc.) — or detect
   the most likely location by looking for existing `.swift` files
2. Check if `CoordinateTracker.swift` already exists anywhere in the project
3. If not, create it using the CoordinateTracker reference implementation below
4. Confirm the file location with the user

### 2. `audit` — Report accessibility gaps

Scans SwiftUI files and reports which interactive elements are missing accessibility
modifiers, without changing any code.

**When to use**: The user wants to understand current coverage before making changes,
or says "audit", "check accessibility", "what's missing".

**Steps**:

1. Identify the target scope — a single file, a directory, or a glob pattern
2. Find all `.swift` files in scope
3. For each file, scan for interactive SwiftUI elements (see "What to scan for" below)
4. For each element, check which of the five properties are present
5. Produce a structured report:

```
## Accessibility Audit Report

### file: Views/SessionTimerView.swift

| Line | Element | Type | identifier | label | hint | value | traits |
|------|---------|------|:---:|:---:|:---:|:---:|:---:|
| 23   | "Save"  | Button | — | — | — | n/a | auto |
| 45   | HStack  | List row | — | — | — | — | — |
| 67   | Toggle  | Toggle | — | OK | — | — | auto |

### Summary
- Files scanned: 12
- Interactive elements found: 34
- Fully accessible: 8 (24%)
- Missing identifiers: 26
- Missing labels: 18
- Missing hints: 22
- Missing values: 14 (of elements that carry state)
```

**Important**: `value` only applies to elements that carry state (Toggle, Picker,
Slider, Stepper, list rows with data, progress indicators). Don't flag buttons or
navigation links as missing `value` unless they have dynamic state. `traits` are
often inferred automatically by SwiftUI (Button gets `.button`, etc.) — only flag
when traits are ambiguous or missing (e.g. a tappable HStack that should be marked
as a button).

### 3. `fix` — Add missing accessibility modifiers

Reads each file, identifies gaps, and adds the appropriate modifiers. This is the
main workhorse mode.

**When to use**: The user wants to actually improve their code, or says "fix",
"add modifiers", "make accessible", "augment".

**Steps**:

1. Run the audit logic first to identify gaps
2. For each element with gaps, add the missing modifiers
3. Follow the naming convention and modifier patterns below
4. If `--track` or "with tracking" is mentioned, also add `.trackElement()` calls
   (requires `init` to have been run first — check for CoordinateTracker.swift)
5. Show the user what changed before applying (or apply directly if they've asked
   for that)

## What to scan for

These SwiftUI elements need accessibility modifiers when interactive or informational:

### Always needs full coverage
- `Button` / `Button(action:)` / `.onTapGesture`
- `NavigationLink`
- `Toggle`
- `Picker` / `DatePicker`
- `Slider`
- `Stepper`
- `TextField` / `SecureField` / `TextEditor`
- `Link`
- `Menu`

### Needs coverage when tappable or informational
- `HStack` / `VStack` / `ZStack` used as list rows (look for `onTapGesture`,
  `NavigationLink` wrapping, or `List { ... }` context)
- `Image` that conveys meaning (not decorative)
- `Label` when used standalone
- `Text` that displays dynamic state
- Custom view structs used as interactive components

### Should be hidden (`.accessibilityHidden(true)`)
- Decorative `Image(systemName: "chevron.right")` disclosure indicators
- Decorative shapes (circles, dividers used purely for visual effect)
- Redundant text already represented by a parent element's label

### View-level identifiers
- `ScrollView`, `List`, `Form`, `NavigationStack` — the top-level container of each
  screen should have `.accessibilityIdentifier("screen_name_view")` so agents can
  orient themselves

## Naming convention

Use this structured pattern for identifiers:

```
{category}_{context}_{element}_{modifier?}
```

- **category**: The domain area (`technique`, `session`, `position`, `settings`, `navigation`)
- **context**: The screen or section (`editor`, `list`, `detail`, `timer`, `tab_bar`)
- **element**: The UI type (`button`, `row`, `textfield`, `toggle`, `picker`)
- **modifier** (optional): Disambiguator (`save`, `delete`, `name`, `filter`)

Examples:
```swift
"technique_editor_save_button"
"position_list_row_\(position.id)"
"session_timer_start_button"
"navigation_tab_bar_training"
"form_textfield_technique_name"
"settings_notifications_toggle"
```

Infer `category` and `context` from the file name, containing view struct, and
surrounding code. The identifier should be self-describing — someone reading
`"technique_editor_save_button"` in a log should immediately know the domain,
screen, and element without looking up code.

## How to write good labels, hints, and values

### Labels (`.accessibilityLabel()`)
- Describe **what the element is**, not how it looks
- Read it as if you're using the app without a screen
- Good: `"Save technique"`, `"Guard position"`, `"Session duration"`
- Bad: `"Button"`, `"MarqueeText"`, `"Blue circle"`

### Hints (`.accessibilityHint()`)
- Describe **what happens** when you interact
- Use present tense, describe the consequence
- Good: `"Validates and stores the current technique"`
- Bad: `"Tap to save"` (VoiceOver already tells users to tap)

### Values (`.accessibilityValue()`)
- The **current state** of the element
- Only for elements with state (toggles, pickers, counters, list rows with data)
- Good: `"3 of 5 selected"`, `"On"`, `"Page 2 of 4"`, `"\(position.transitionCount) transitions"`
- Bad: (omit entirely if the element has no state — don't set an empty value)

## Modifier placement pattern

Add modifiers directly after the element, before any layout modifiers like `.padding()`
or `.frame()`. Group accessibility modifiers together:

```swift
Button("Save") {
    saveTechnique()
}
.accessibilityIdentifier("technique_editor_save_button")
.accessibilityLabel("Save technique")
.accessibilityHint("Validates and stores the current technique")
.padding()
.frame(maxWidth: .infinity)
```

For list rows, apply modifiers to the outermost container and hide decorative children:

```swift
HStack(spacing: 12) {
    Circle().fill(.blue).frame(width: 8)
        .accessibilityHidden(true)
    VStack(alignment: .leading) {
        Text(position.name)
        Text("\(position.transitionCount) transitions")
            .foregroundStyle(.secondary)
    }
    Spacer()
    Image(systemName: "chevron.right")
        .accessibilityHidden(true)
}
.accessibilityIdentifier("position_list_row_\(position.id)")
.accessibilityLabel(position.name)
.accessibilityHint("Opens detailed information for \(position.name)")
.accessibilityValue("\(position.transitionCount) transitions")
```

## `.trackElement()` (opt-in)

Only add `.trackElement()` when the user explicitly opts in (says "with tracking",
passes `--track`, or has run `init`). When adding it, use the same string as the
`accessibilityIdentifier`:

```swift
Button("Start session") { startSession() }
    .accessibilityIdentifier("session_timer_start_button")
    .accessibilityLabel("Start training session")
    .accessibilityHint("Begins a new timed training session")
    .trackElement("session_timer_start_button")
```

## CoordinateTracker reference implementation

Drop this into your project as `CoordinateTracker.swift` during `init` mode:

```swift
import SwiftUI

@MainActor
final class CoordinateTracker: ObservableObject {
    static let shared = CoordinateTracker()
    private init() {}

    struct TrackedElement {
        let id: String
        let frame: CGRect
        var center: CGPoint { CGPoint(x: frame.midX, y: frame.midY) }
    }

    private(set) var elements: [String: TrackedElement] = [:]
    private(set) var currentView: String?
    private(set) var viewMetadata: [String: String] = [:]

    func track(id: String, frame: CGRect) {
        elements[id] = TrackedElement(id: id, frame: frame)
    }

    func tapPoint(for id: String) -> CGPoint? {
        elements[id]?.center
    }

    func updateViewContext(viewName: String, metadata: [String: String] = [:]) {
        currentView = viewName
        viewMetadata = metadata
    }
}

extension View {
    func trackElement(_ id: String) -> some View {
        background(
            GeometryReader { geo in
                Color.clear.onAppear {
                    CoordinateTracker.shared.track(
                        id: id,
                        frame: geo.frame(in: .global)
                    )
                }
            }
        )
    }
}
```

Update view context on screen appear:

```swift
.onAppear {
    CoordinateTracker.shared.updateViewContext(
        viewName: "SessionTimerView",
        metadata: ["sessionId": session.id]
    )
}
```

## Quality checks

After fixing a file, verify:

1. Every interactive element has at least `identifier` + `label`
2. Every element with an action has `hint`
3. Every element with state has `value`
4. Decorative elements are hidden
5. View-level containers have identifiers
6. Identifiers follow the naming convention
7. Labels describe meaning, not appearance
8. No duplicate identifiers within the same view
