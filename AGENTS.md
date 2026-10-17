# AGENTS.md

Guidance for coding agents (Claude Code, Codex) working in this repository. `CLAUDE.md` imports this file.

## Purpose

This repo is a plugin marketplace of **Agent Skills**, installable from both Claude Code and Codex, plus reference docs for the formats. Skills are markdown; the only code is `scripts/sync-codex-manifests.py`.

## Key Files

- `SKILLS.md` — Complete Agent Skills specification: directory structure, `SKILL.md` frontmatter format (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`), body content guidelines, optional directories (`scripts/`, `references/`, `assets/`), progressive disclosure strategy, and validation via `skills-ref`.
- `MARKETPLACE.md` — Claude Code-specific guide to creating and distributing Claude Code plugin marketplaces: `marketplace.json` catalog format, `plugin.json` manifests, hosting, and the `/plugin marketplace` CLI commands.

## Agent Skills Format (Quick Reference)

A skill is a directory with a required `SKILL.md` containing YAML frontmatter + markdown instructions:

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources
```

Key constraints: `name` must be lowercase alphanumeric + hyphens, match parent directory name, max 64 chars. `SKILL.md` body should stay under 500 lines / ~5000 tokens. Validate with `skills-ref validate ./my-skill`.

## Plugin Marketplace Structure

```
marketplace/
├── .claude-plugin/
│   └── marketplace.json    # Catalog listing plugins
└── plugins/
    └── plugin-name/
        ├── .claude-plugin/
        │   └── plugin.json # Plugin manifest (name, description, version)
        └── skills/         # Skills provided by the plugin
```

## Dual-tool layout

Skills are shared; only the manifests differ per tool.

```
.claude-plugin/marketplace.json          # Claude Code catalog (source of truth)
.agents/plugins/marketplace.json         # Codex catalog (generated)
plugins/<name>-plugin/
├── .claude-plugin/plugin.json           # Claude Code manifest (source of truth)
├── plugin.json                          # Codex manifest (generated)
└── skills/<skill>/SKILL.md              # shared by both
```

- Edit the Claude files, then run `python3 scripts/sync-codex-manifests.py` to regenerate the Codex ones. `--check` fails if they drift.
- Write skills tool-neutrally: say "ask the user" or "spawn a sub-agent", not `AskUserQuestion` or the Agent tool. Where a Claude or Codex specific is unavoidable, put it in a short "Tool mapping" note.
- Keep `description` short and specific. Codex caps the skill list at roughly 2% of context and truncates long descriptions first.
