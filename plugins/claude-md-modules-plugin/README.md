# claude-md-modules

Composable, stack-agnostic prompt segments for CLAUDE.md files. Each module is a standalone `.md` file covering one convention area (naming, error handling, testing, agentic patterns, a condensed spec-speak, etc.) — paste one directly into a project's CLAUDE.md, or ask Claude to assemble several into a starter file.

```bash
/plugin install claude-md-modules-plugin
```

**Status: scaffold.** The plugin structure is in place; the module library itself is still empty — see [`skills/claude-md-modules/references/README.md`](skills/claude-md-modules/references/README.md) for the planned list.

## Contents

```
claude-md-modules-plugin/
├── README.md                        # This file
└── skills/claude-md-modules/
    ├── SKILL.md                     # The skill: module conventions + composition workflow
    └── references/
        └── README.md                # Planned module list (empty for now)
```
