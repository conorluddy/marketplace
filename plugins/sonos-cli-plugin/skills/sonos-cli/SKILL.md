---
name: sonos-cli
description: >
  Control Sonos speakers from the CLI using the `sonos` command. Translates
  natural language requests into sonos CLI commands for playback, volume,
  grouping, queue management, and music search. Use this skill whenever the
  user mentions Sonos, asks to play music on a speaker, control volume on a
  room, group or ungroup speakers, manage their Sonos queue, or references
  speaker names like "Kitchen" or "TV". Trigger phrases: "play X on Sonos",
  "turn up the kitchen speaker", "pause Sonos", "what's playing on Sonos",
  "group my speakers", "play my Sonos favorites", "Sonos volume", "skip track
  on Sonos", "add to Sonos queue".
---

# Sonos CLI Skill

Control Philips Hue lights via the `sonos` CLI command-line interface installed at `/opt/homebrew/bin/sonos` (v0.1.1+).

## Known Speakers

Two speakers are configured in this household:

| Speaker | IP Address | Notes |
|---------|-----------|-------|
| Kitchen | 192.168.68.61 | Primary speaker, default target |
| TV | 192.168.68.60 | Secondary speaker |

To re-discover speakers or add new ones, run:
```bash
sonos discover
```

If a speaker becomes unreachable, check network connectivity and re-run `discover`.

---

## Core Workflow

When the user mentions Sonos or a speaker name:

1. **Identify the target speaker** — infer from context ("kitchen", "tv", "living room"), or default to **Kitchen** if ambiguous.
2. **Map intent to command** — use the command map below to translate natural language into CLI syntax.
3. **Execute the command** — run `sonos <cmd> --name "<Room>"` (unless a defaultRoom is configured).
4. **Confirm or display output** — for status/volume queries, show the parsed result; for mutations (play, pause, set), confirm what was done with a short message.
5. **Handle errors gracefully** — if the speaker is unreachable, suggest running `sonos discover` or checking network status.

---

## Command Reference

### Status & Info

| User Intent | CLI Command | Output |
|---|---|---|
| What's playing? | `sonos status --name "<Room>"` | Current track, artist, duration, playback state |
| Get volume | `sonos volume get --name "<Room>"` | Current volume (0–100) |
| List speakers | `sonos discover` | All speakers on network with IPs |
| Show queue | `sonos queue list --name "<Room>" --format json` | Full playlist (JSON) |
| List favorites | `sonos favorites list --name "<Room>" --format json` | Saved favorites (JSON) |

### Playback Control

| User Intent | CLI Command |
|---|---|
| Play / resume | `sonos play --name "<Room>"` |
| Pause | `sonos pause --name "<Room>"` |
| Stop | `sonos stop --name "<Room>"` |
| Skip / next | `sonos next --name "<Room>"` |
| Previous track | `sonos prev --name "<Room>"` |

### Volume Control

| User Intent | CLI Command |
|---|---|
| Set volume to N (0–100) | `sonos volume set <N> --name "<Room>"` |
| Mute | `sonos mute on --name "<Room>"` |
| Unmute | `sonos mute off --name "<Room>"` |
| Toggle mute | `sonos mute toggle --name "<Room>"` |
| Increase by N | `sonos volume +<N> --name "<Room>"` |
| Decrease by N | `sonos volume -<N> --name "<Room>"` |

### Music Playback

#### Spotify via SMAPI (Preferred — no credentials)

```bash
sonos play spotify "<query>" --name "<Room>"
```

- `--category tracks|albums|playlists` — filter search type (default: all)
- `--index N` — pick Nth result (0-based; default: 0 for top result)

Examples:
- `sonos play spotify "jazz" --name "Kitchen"` — play jazz mix
- `sonos play spotify "norah jones" --category tracks --index 2 --name "Kitchen"` — play 3rd track by Norah Jones

#### Spotify via Web API (if SPOTIFY_CLIENT_ID / SPOTIFY_CLIENT_SECRET are set)

```bash
sonos search spotify "<query>" --type track --open --name "<Room>"
```

_Prefer SMAPI above unless the user explicitly says "search."_

### Grouping & Party Mode

| User Intent | CLI Command |
|---|---|
| Group Kitchen + TV | `sonos group join --name "Kitchen" --to "TV"` |
| Ungroup / solo speaker | `sonos group solo --name "<Room>"` |
| Party mode (all rooms join Kitchen) | `sonos group party --to "Kitchen"` |

### Favorites & Scenes

| User Intent | CLI Command |
|---|---|
| Play saved favorite | `sonos favorites open "<favorite-name>" --name "<Room>"` |
| Save current state as scene | `sonos scene save "<scene-name>"` |
| Apply a saved scene | `sonos scene apply "<scene-name>"` |

### Advanced

| User Intent | CLI Command |
|---|---|
| Clear queue | `sonos queue clear --name "<Room>"` |
| TV audio input | `sonos tv --name "TV"` |
| Play radio/stream URL | `sonos play-uri <url> --name "<Room>" --radio --title "<display-name>"` |

---

## Example Interactions

### 1. Play Music on a Speaker

**User:** "Play some jazz on the kitchen"

**Skill:**
- Target: Kitchen
- Intent: play music (Spotify)
- Command: `sonos play spotify "jazz" --name "Kitchen"`
- Response: `Playing jazz on Kitchen speaker`

### 2. Adjust Volume

**User:** "Turn the TV speaker up to 50"

**Skill:**
- Target: TV
- Intent: set volume
- Command: `sonos volume set 50 --name "TV"`
- Response: `TV volume set to 50`

### 3. Check What's Playing

**User:** "What's playing on Sonos?"

**Skill:**
- Target: Kitchen (default)
- Intent: status query
- Command: `sonos status --name "Kitchen"`
- Response: `[Parsed output] Artist - Track Name (2:45 / 5:30) [Playing]`

### 4. Group Speakers

**User:** "Group my speakers together"

**Skill:**
- Infer primary coordinator (Kitchen)
- Intent: party mode (group all)
- Command: `sonos group party --to "Kitchen"`
- Response: `TV grouped with Kitchen`

### 5. Pause Playback

**User:** "Pause the Sonos"

**Skill:**
- Target: Kitchen (default)
- Intent: pause
- Command: `sonos pause --name "Kitchen"`
- Response: `Paused`

---

## Output Handling

**Queries (status, volume, queue, favorites):**
- Run command with `--format json` if available
- Parse JSON output and present cleanly to the user
- Example: `sonos status --format json` → extract `track`, `artist`, `duration`, `playback` and format as human-readable text

**Mutations (play, pause, volume set, grouping):**
- Run command without `--format json`
- Confirm action with a brief message: `"Playing [title] on Kitchen"` or `"Volume set to 50"`

**Errors:**
- If speaker is unreachable: `"Kitchen is offline. Try 'sonos discover' to re-scan the network."`
- If command fails: show CLI error verbatim + suggest fix
- If Spotify search returns no results: `"No tracks found for 'xyz'. Try a different search."`

---

## Skill Trigger

**Only invoke this skill when the user explicitly mentions:**
- `Sonos`, `sonos` (case-insensitive)
- Speaker names: `Kitchen`, `TV`, or other rooms
- Commands tied to those speakers: `"play music on the kitchen speaker"`, `"turn up volume"` in a Sonos context

**Do NOT trigger if** the user says `"play music"` without mentioning Sonos or a specific speaker name. This keeps the skill focused and avoids false positives.

---

## Notes & Troubleshooting

- **Default speaker:** Kitchen is the default if ambiguous (e.g. `"pause Sonos"` → pauses Kitchen)
- **Multi-speaker commands:** Always target explicitly or confirm with the user which speaker to control
- **Network issues:** If speakers go offline, run `sonos discover` to re-scan
- **Spotify setup:** SMAPI (via `sonos play spotify`) doesn't require credentials; use Web API (via `sonos search spotify`) only if user has Spotify API keys configured
- **Favorites:** User must have saved favorites in their Sonos app first; the CLI can then reference them by name

