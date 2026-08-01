# claude-md-kit

Composable, stack-agnostic prompt segments for CLAUDE.md files. Each module is a standalone `.md` file covering one convention area (naming, error handling, testing, agentic patterns, a condensed spec-speak, etc.) — paste one directly into a project's CLAUDE.md, or ask Claude to assemble several into a starter file.

```bash
/plugin install claude-md-kit-plugin
```

See [`skills/claude-md-kit/references/README.md`](skills/claude-md-kit/references/README.md) for the full module list.

## Contents

```
claude-md-kit-plugin/
├── README.md                        # This file
└── skills/claude-md-kit/
    ├── SKILL.md                     # The skill: module conventions + composition workflow
    └── references/
        ├── README.md                # Module list (written + planned)
        └── *.md                     # The modules themselves
```
