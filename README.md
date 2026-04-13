# conors-skills

A Claude Code plugin marketplace for distributing reusable skills.

## Plugins

| Plugin | Description |
|--------|-------------|
| **github-labels** | Structured GitHub issue labels — priority, clarity, risk, blast radius, size, parallelism, sequencing, and type |
| **swift-accessibility** | Audit, fix, and scaffold SwiftUI accessibility modifiers for VoiceOver and AI agents |
| **liquid-glass** | iOS 26 Liquid Glass effects in SwiftUI and UIKit — API reference, design rules, and patterns |
| **sonos-cli** | Control Sonos speakers — playback, volume, grouping, queue management, and music search |
| **openhue** | Control Philips Hue lights — brightness, color, scenes, and automation |
| **and-then** | Ambiguity-first planning — resolve unknowns before committing to implementation |

## Install

Add the marketplace, then install individual plugins:

```bash
/plugin marketplace add https://github.com/conorluddy/Skills

/plugin install github-labels-plugin
/plugin install swift-accessibility-plugin
/plugin install liquid-glass-plugin
/plugin install sonos-cli-plugin
/plugin install openhue-plugin
/plugin install and-then-plugin
```

## Adding a plugin

Each plugin follows this structure:

```
plugins/<name>-plugin/
├── .claude-plugin/
│   └── plugin.json       # name, description, version
└── skills/
    └── <skill-name>/
        └── SKILL.md      # Skill definition (frontmatter + instructions)
```

After creating the plugin directory, add an entry to `.claude-plugin/marketplace.json`.
