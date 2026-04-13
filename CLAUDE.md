# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo is a reference library for the **Agent Skills** specification and **Claude Code plugin marketplace** format. It contains no executable code — only documentation.

## Key Files

- `SKILLS.md` — Complete Agent Skills specification: directory structure, `SKILL.md` frontmatter format (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`), body content guidelines, optional directories (`scripts/`, `references/`, `assets/`), progressive disclosure strategy, and validation via `skills-ref`.
- `MARKETPLACE.md` — Guide to creating and distributing Claude Code plugin marketplaces: `marketplace.json` catalog format, `plugin.json` manifests, hosting, and the `/plugin marketplace` CLI commands.

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
