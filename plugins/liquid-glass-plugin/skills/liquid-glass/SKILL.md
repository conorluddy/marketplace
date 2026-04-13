---
name: liquid-glass
description: "Implement iOS 26 Liquid Glass effects in SwiftUI and UIKit. Use this skill whenever the user mentions liquid glass, glass effects, glassEffect, iOS 26 UI design, translucent navigation bars, glass morphing, GlassEffectContainer, or wants to add the new Apple glass material to their app. Also use when migrating an existing app's UI to iOS 26 style, or when the user asks about glass button styles, tab bar minimization, or the new sheet presentations."
---

# iOS 26 Liquid Glass

Liquid Glass is Apple's new design language (WWDC 2025 / iOS 26). It applies translucent, light-bending material to **navigation layers only** — never to content. This skill contains the full API reference and design guidance so you can implement it correctly.

## When you need details

Read `references/api-reference.md` for the complete API surface, code examples, platform differences, performance notes, and anti-patterns. It covers:

- Core modifiers (`.glassEffect()`, `.glassEffectID()`, `.glassEffectUnion()`, `.glassEffectTransition()`)
- Glass types (`.regular`, `.clear`, `.identity`, `.tint()`, `.interactive()`)
- Button styles (`.glass`, `.glassProminent`)
- `GlassEffectContainer` for grouping and morphing
- TabView, toolbar, and sheet integration
- UIKit bridge via `UIGlassEffect` / `UIVisualEffectView`
- Accessibility, performance, and backward compatibility

## Core rules

1. **Navigation layer only.** Glass goes on nav bars, toolbars, tab bars, floating action buttons, sheets, popovers, menus. Never on content, full-screen backgrounds, or scrollable content.

2. **Use `GlassEffectContainer`** whenever you have multiple glass elements. It shares the sampling region (glass cannot sample other glass) and enables morphing between elements.

3. **Tint sparingly.** Tinting conveys semantic meaning (primary action, destructive action), not decoration. Don't tint everything.

4. **Respect accessibility automatically.** Glass adapts to reduced transparency, increased contrast, and reduced motion without code. You can read `@Environment(\.accessibilityReduceTransparency)` and `@Environment(\.accessibilityReduceMotion)` if you need conditional behavior.

5. **Performance awareness.** iOS 26 glass costs ~13% battery vs 1% in iOS 18 (iPhone 16 Pro Max benchmark). Use containers, limit continuous animations, and test on older devices (iPhone 11-13 may lag).

6. **No glass-on-glass.** Never stack glass layers. Use the three-layer model: content (bottom, no glass) → navigation (middle, glass) → overlay (top, vibrancy/fills).

## Quick start

```swift
// Simplest glass effect
Text("Hello")
    .padding()
    .glassEffect()

// Glass buttons
Button("Cancel") { }
    .buttonStyle(.glass)

Button("Save") { }
    .buttonStyle(.glassProminent)
    .tint(.blue)

// Grouped glass with morphing
@Namespace private var ns

GlassEffectContainer(spacing: 30) {
    Button("Toggle") { withAnimation { expanded.toggle() } }
        .glassEffect()
        .glassEffectID("main", in: ns)
    
    if expanded {
        Button("Action") { }
            .glassEffectID("action", in: ns)
    }
}
```

## Common patterns

**Floating action button:**
```swift
Button(action: compose) {
    Image(systemName: "plus")
        .font(.title2)
}
.buttonStyle(.glassProminent)
.tint(.blue)
```

**Tab bar with search and minimization:**
```swift
TabView {
    Tab("Home", systemImage: "house") { HomeView() }
    Tab("Search", systemImage: "magnifyingglass", role: .search) { SearchView() }
}
.tabBarMinimizeBehavior(.onScrollDown)
```

**Custom shape:**
```swift
.glassEffect(.regular, in: RoundedRectangle(cornerRadius: 16))
.glassEffect(.regular, in: .capsule)  // default
.glassEffect(.regular, in: .rect(cornerRadius: .containerConcentric))
```

**UIKit bridge:**
```swift
let effect = UIGlassEffect(glass: .regular, isInteractive: true)
let effectView = UIVisualEffectView(effect: effect)
```

## Anti-patterns to avoid

- Applying `.glassEffect()` to content views or backgrounds
- Stacking glass on glass
- Using custom opacity that bypasses accessibility
- Hard-coded colors on glass (use system colors for vibrancy)
- Separate glass effects without a container (use `GlassEffectContainer`)
- Tinting every glass element
- Breaking container-concentric corner alignment

## Minimum requirements

iOS 26.0+, iPadOS 26.0+, macOS Tahoe 26.0+, watchOS 26.0+, tvOS 26.0+, visionOS 26.0+. Requires iPhone 11 / SE 2nd gen or later. Older devices get frosted glass fallback.
