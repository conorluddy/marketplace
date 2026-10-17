My plugin marketplace for distributing reusable skills. Works with Claude Code and Codex.

```bash
# Claude Code
/plugin marketplace add https://github.com/conorluddy/marketplace

# Codex
codex plugin marketplace add conorluddy/marketplace
```


## Plugins

| Plugin | Description |
|--------|-------------|
| **github-labels** | Structured GitHub issue labels — priority, clarity, risk, blast radius, size, parallelism, sequencing, and type |
| **swift-accessibility** | Audit and fix SwiftUI accessibility for VoiceOver and AI agents, including the modifiers that silently remove it |
| **liquid-glass** | iOS 26 Liquid Glass effects in SwiftUI and UIKit — API reference, design rules, and patterns |
| **sonos-cli** | Control Sonos speakers — playback, volume, grouping, queue management, and music search |
| **openhue** | Control Philips Hue lights — brightness, color, scenes, and automation |
| **team-work** | Decompose a session's JTBD into a parallelizable agent-team plan — tiered models (fast/balanced/deep), specialist subagents, dependency waves |
| **and-then** | Ambiguity-first planning — resolve unknowns before committing to implementation  |
| **code-review** | Review code against a style guide focused on progressive disclosure, explicit contracts, agentic patterns, and token economics — severity-grouped findings with file:line refs and concrete fixes |
| **ios-aso** | Generate paste-ready English (U.S.) App Store Optimization metadata (ASO.md) for an iOS app by scanning its Swift/SwiftUI codebase — App Name, Subtitle, Keywords, category, screenshot captions, and research notes |
| **claude-md-kit** | Composable, stack-agnostic prompt segments for project instructions files (CLAUDE.md / AGENTS.md) — copy-paste modules, or let the skill assemble one |
| **app-review-guidelines** | Audit an iOS codebase against Apple's App Store Review Guidelines, triage rejections into fixes and Resolution Center replies, and run a pre-submission checklist — advisory REVIEW-RISK.md with guideline numbers |
| **[spec-speak](plugins/spec-speak-plugin/README.md)** | Convert rough notes into rigorous, testable specs — EARS requirement templates, RFC 2119 keywords, INCOSE/ISO 29148 rules, Gherkin acceptance criteria, and interactive prompts for undecided product questions |

![69cf40c1-9f3a-4a06-9ea2-eb3097b9c6c6_text](https://github.com/user-attachments/assets/382b940d-f95d-44f7-8498-44205ab64861)

## Install

### Claude Code

Add the marketplace, then install individual plugins:

```bash
/plugin marketplace add https://github.com/conorluddy/marketplace

/plugin install github-labels-plugin
/plugin install swift-accessibility-plugin
/plugin install liquid-glass-plugin
/plugin install sonos-cli-plugin
/plugin install openhue-plugin
/plugin install and-then-plugin
/plugin install team-work-plugin
/plugin install code-review-plugin
/plugin install ios-aso-plugin
/plugin install app-review-guidelines-plugin
/plugin install spec-speak-plugin
/plugin install claude-md-kit-plugin
```

Invoke a skill with `/skill-name`.

### Codex

Add the marketplace, then open `/plugins` in the Codex CLI (or use the ChatGPT desktop app) to install, and start a new session:

```bash
codex plugin marketplace add conorluddy/marketplace
```

Invoke a skill with `$skill-name`. Without plugin support, copy or symlink any `plugins/<name>-plugin/skills/<skill>` folder into `~/.agents/skills/` (user) or `.agents/skills/` (project).

## Adding a plugin

Each plugin follows this structure:

```
plugins/<name>-plugin/
├── .claude-plugin/
│   └── plugin.json       # Claude Code manifest: name, description, version
├── plugin.json           # Codex manifest (generated, don't edit)
└── skills/
    └── <skill-name>/
        └── SKILL.md      # Skill definition (frontmatter + instructions)
```

After creating the plugin directory, add an entry to `.claude-plugin/marketplace.json`, then generate the Codex manifests:

```bash
python3 scripts/sync-codex-manifests.py          # regenerate
python3 scripts/sync-codex-manifests.py --check  # verify nothing drifted
```

Write skills tool-neutrally (see `AGENTS.md`) so they run in both tools.
