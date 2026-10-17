#!/usr/bin/env python3
"""Generate Codex manifests from the Claude Code ones, or verify they match.

Claude Code files are the source of truth:
  .claude-plugin/marketplace.json
  plugins/<name>/.claude-plugin/plugin.json

Generated for Codex:
  .agents/plugins/marketplace.json
  plugins/<name>/plugin.json

Usage: sync-codex-manifests.py [--check]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
CATEGORY = "Productivity"  # only value shown in OpenAI's docs; full enum is unpublished


def build_expected() -> dict[Path, dict]:
    claude_marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    expected: dict[Path, dict] = {}
    entries = []
    for entry in claude_marketplace["plugins"]:
        plugin_dir = ROOT / entry["source"]
        claude_manifest = json.loads((plugin_dir / ".claude-plugin/plugin.json").read_text())
        expected[plugin_dir / "plugin.json"] = {
            "$schema": SCHEMA,
            "name": claude_manifest["name"],
            "version": claude_manifest["version"],
            "description": claude_manifest["description"],
            "author": {"name": claude_marketplace["owner"]["name"]},
        }
        entries.append({
            "name": entry["name"],
            "source": {"source": "local", "path": entry["source"]},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": CATEGORY,
        })
    expected[ROOT / ".agents/plugins/marketplace.json"] = {
        "name": claude_marketplace["name"],
        "interface": {"displayName": "Conor's Skills"},
        "plugins": entries,
    }
    return expected


def main() -> int:
    check_only = "--check" in sys.argv
    stale = []
    for path, content in build_expected().items():
        rendered = json.dumps(content, indent=2, ensure_ascii=False) + "\n"
        if path.exists() and path.read_text() == rendered:
            continue
        stale.append(path.relative_to(ROOT))
        if not check_only:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered)
    if stale and check_only:
        print("Out of sync with Claude manifests (run scripts/sync-codex-manifests.py):")
        print("\n".join(f"  {p}" for p in stale))
        return 1
    print(f"{'Would update' if check_only else 'Updated'} {len(stale)} file(s)" if stale else "Codex manifests in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
