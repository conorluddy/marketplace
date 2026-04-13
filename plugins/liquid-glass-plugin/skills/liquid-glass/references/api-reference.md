# Liquid Glass API Reference

Complete API surface for iOS 26 Liquid Glass, sourced from WWDC 2025 and Apple documentation.

## Table of Contents

1. [Core API](#core-api)
2. [Glass Types](#glass-types)
3. [Shapes](#shapes)
4. [GlassEffectContainer](#glasseffectcontainer)
5. [Morphing & Transitions](#morphing--transitions)
6. [Button Styles](#button-styles)
7. [Toolbar Integration](#toolbar-integration)
8. [TabView Integration](#tabview-integration)
9. [Sheet Presentations](#sheet-presentations)
10. [UIKit Bridge](#uikit-bridge)
11. [Platform Differences](#platform-differences)
12. [Performance](#performance)
13. [Accessibility](#accessibility)
14. [Backward Compatibility](#backward-compatibility)
15. [Known Issues](#known-issues)
16. [Design Principles](#design-principles)
17. [Anti-Patterns](#anti-patterns)

---

## Core API

### glassEffect

```swift
func glassEffect<S: Shape>(
    _ glass: Glass = .regular,
    in shape: S = DefaultGlassEffectShape,
    isEnabled: Bool = true
) -> some View
```

Applies liquid glass material to a view. The view becomes part of the navigation layer with translucent, light-bending treatment.

```swift
Text("Hello, Liquid Glass!")
    .padding()
    .glassEffect()
```

### glassEffectID

```swift
func glassEffectID<ID: Hashable>(
    _ id: ID,
    in namespace: Namespace.ID
) -> some View
```

Assigns an identity for morphing transitions. Elements with shared namespace IDs in the same `GlassEffectContainer` morph between states.

### glassEffectUnion

```swift
func glassEffectUnion<ID: Hashable>(
    id: ID,
    namespace: Namespace.ID
) -> some View
```

Manually combines glass effects that are too distant for spacing-based merging in a container.

### glassEffectTransition

```swift
func glassEffectTransition(
    _ transition: GlassEffectTransition,
    isEnabled: Bool = true
) -> some View
```

Controls transition type between glass states:

```swift
enum GlassEffectTransition {
    case identity           // No transition
    case matchedGeometry    // Morph between positions/sizes
    case materialize        // Gradual light modulation appearance
}
```

---

## Glass Types

```swift
struct Glass {
    static var regular: Glass    // Medium transparency (default)
    static var clear: Glass      // High transparency, for media-rich backgrounds
    static var identity: Glass   // Conditional disable (no glass rendered)
    
    func tint(_ color: Color) -> Glass    // Semantic tinting
    func interactive() -> Glass           // Enables press scaling, bounce, shimmer
}
```

- **regular**: Default. Medium transparency suitable for most navigation elements.
- **clear**: High transparency. Use over media-rich content (photos, videos, maps).
- **identity**: Disables glass. Use for conditional rendering without layout changes.
- **tint()**: Conveys meaning (primary action = blue, destructive = red). Not decorative.
- **interactive()**: Adds iOS touch feedback: scaling on press, bounce animation, shimmer, touch-point illumination.

---

## Shapes

Supported shapes for the `in:` parameter:

| Shape | Usage |
|-------|-------|
| `.capsule` | Default shape |
| `.circle` | Circular elements |
| `RoundedRectangle(cornerRadius:)` | Custom corner radius |
| `.rect(cornerRadius: .containerConcentric)` | Auto-aligns corners with container |
| `.ellipse` | Elliptical shape |

Container-concentric corners (`.containerConcentric`) maintain perfect alignment across device sizes. Prefer this over hard-coded radii.

---

## GlassEffectContainer

Combines multiple glass shapes into a unified composition. Required for:
- Morphing transitions between elements
- Performance (shares sampling region)
- Visual grouping

```swift
GlassEffectContainer {
    // Glass elements compose together
}

GlassEffectContainer(spacing: 40.0) {
    // Elements within 40 points morph together
}
```

Glass cannot sample other glass. The container provides the shared sampling region that all child glass effects draw from.

---

## Morphing & Transitions

Morphing requires:
1. Elements in the same `GlassEffectContainer`
2. Shared namespace IDs via `.glassEffectID()`
3. Conditional visibility (e.g., `if isExpanded`)
4. Applied animations (`withAnimation`)

```swift
@Namespace private var namespace

GlassEffectContainer(spacing: 30) {
    Button("Expand") {
        withAnimation { isExpanded.toggle() }
    }
    .glassEffect()
    .glassEffectID("toggle", in: namespace)
    
    if isExpanded {
        Button("Action 1") { }
            .glassEffectID("action1", in: namespace)
        
        Button("Action 2") { }
            .glassEffectID("action2", in: namespace)
    }
}
```

Symbol effects integrate smoothly:
```swift
.contentTransition(.symbolEffect(.replace))
```

---

## Button Styles

| Style | Usage |
|-------|-------|
| `.glass` | Translucent, secondary actions |
| `.glassProminent` | Opaque, primary actions |

```swift
Button("Cancel") { }
    .buttonStyle(.glass)

Button("Save") { }
    .buttonStyle(.glassProminent)
    .tint(.blue)
```

Control sizes: `.mini`, `.small`, `.regular`, `.large`, `.extraLarge`

---

## Toolbar Integration

Toolbars automatically receive Liquid Glass treatment in iOS 26.

```swift
.toolbar {
    ToolbarItem(placement: .confirmationAction) {
        Button("Done", systemImage: "checkmark") { }
    }
}
```

- Prioritize SF Symbols over text labels
- Group related items with visual separation
- Use `ToolbarSpacer(.fixed, spacing:)` and `ToolbarSpacer(.flexible)` for layout

---

## TabView Integration

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    Tab("Search", systemImage: "magnifyingglass", role: .search) {
        SearchView()
    }
}
.tabBarMinimizeBehavior(.onScrollDown)
```

- **Search role**: Creates floating search button at bottom-right for reachability
- **Minimization behaviors**: `.automatic`, `.onScrollDown`, `.never`
- **Bottom accessory**: `.tabViewBottomAccessory { }` for persistent controls

---

## Sheet Presentations

Sheets automatically receive inset Liquid Glass backgrounds in iOS 26.

Use matched transition sources for morphing from toolbar buttons into sheets:
```swift
Button("Settings", systemImage: "gear") { showSettings = true }
    .matchedTransitionSource(id: "settings", in: namespace)

.sheet(isPresented: $showSettings) {
    SettingsView()
        .navigationTransition(.zoom(sourceID: "settings", in: namespace))
}
```

---

## UIKit Bridge

```swift
let glassEffect = UIGlassEffect(glass: .regular, isInteractive: true)
let effectView = UIVisualEffectView(effect: glassEffect)
effectView.frame = CGRect(x: 0, y: 0, width: 200, height: 50)
view.addSubview(effectView)
```

---

## Platform Differences

| Platform | Specifics |
|----------|-----------|
| **iOS** | Floating tab bars, bottom search placement |
| **iPadOS** | Floating sidebars, ambient reflection |
| **macOS Tahoe** | Concentric window corners, taller controls |
| **watchOS** | Location-aware widgets |
| **tvOS** | Focused glass effects, directional highlights |
| **visionOS** | Full 3D glass material |

---

## Performance

iOS 26 glass rendering costs significantly more than previous blur effects:
- **Battery**: ~13% drain vs ~1% in iOS 18 (iPhone 16 Pro Max benchmark)
- **Older devices**: iPhone 11-13 may show lag with many glass elements

Optimization strategies:
1. Always use `GlassEffectContainer` for multiple elements
2. Use `.identity` for conditional glass (avoids layout changes)
3. Limit continuous animations on glass elements
4. Profile with Instruments (Core Animation template)
5. Test on oldest supported device in your target range

---

## Accessibility

Glass automatically adapts to:
- **Reduce Transparency**: Falls back to opaque backgrounds
- **Increase Contrast**: Stronger borders and fills
- **Reduce Motion**: Disables morphing and spring animations

Environment values for conditional behavior:
```swift
@Environment(\.accessibilityReduceTransparency) var reduceTransparency
@Environment(\.accessibilityReduceMotion) var reduceMotion
```

Maintain **4.5:1 minimum contrast ratio** for text on glass. Use system colors — they adjust for vibrancy automatically.

---

## Backward Compatibility

- Recompiling with Xcode 26 automatically adopts Liquid Glass for standard components
- Temporary opt-out via Info.plist flag (not recommended long-term)
- Older devices receive frosted glass fallback with reduced effects
- Use `#available(iOS 26, *)` for new APIs in mixed-deployment targets

```swift
if #available(iOS 26, *) {
    content.glassEffect()
} else {
    content.background(.ultraThinMaterial)
}
```

---

## Known Issues

1. **Interactive shape mismatch**: Fix by using `.buttonStyle(.glass)` instead of raw `.glassEffect(.regular.interactive())`
2. **`.glassProminent` circle artifacts**: Add explicit `.clipShape(Circle())`
3. **Glass-on-glass rendering**: Not supported — use layering model instead

---

## Design Principles

### Three-layer model
1. **Content layer** (bottom): App content, no glass
2. **Navigation layer** (middle): Liquid Glass controls
3. **Overlay layer** (top): Vibrancy, fills, system overlays

### When to use glass
- Navigation bars, toolbars, tab bars
- Bottom accessories, floating action buttons
- Sheets, popovers, menus
- Context-sensitive controls, system alerts

### When NOT to use glass
- Content views or backgrounds
- Full-screen backgrounds
- Scrollable content areas
- Stacked on other glass
- Every UI element indiscriminately

---

## Anti-Patterns

### Visual
- Overusing glass on every element
- Stacking glass on glass
- Applying glass to content layers
- Tinting everything (use sparingly for semantic meaning)
- Breaking container-concentric corner alignment

### Technical
- Custom opacity that bypasses accessibility adaptations
- Ignoring safe areas
- Hard-coded colors (use system colors for vibrancy)
- Mixing glass variants without purpose
- Multiple separate glass effects without a container

### Usability
- Busy backgrounds without dimming layer
- Insufficient contrast (below 4.5:1)
- Excessive continuous animations
- Breaking platform conventions
- Prioritizing aesthetics over legibility

### Complex backgrounds
When glass overlaps busy content:
- Add gradient fades at control edges
- Use strategic tinting with opacity
- Add background dimming layers
- Never add more glass to "fix" readability
