---
name: openhue
description: Control Philips Hue lights from the CLI. Use this skill whenever the user wants to control smart lights, adjust brightness or color, manage lighting scenes, or automate lighting. Examples include turning lights on/off, setting brightness levels, changing colors, controlling multiple lights/rooms at once, discovering light bridges, or configuring Hue bridge connections. Works with individual lights, entire rooms, or batch operations across multiple devices.
compatibility: openhue CLI installed and configured
---

# openhue Skill

Control Philips Hue lighting systems via CLI. Execute lighting commands, query state, and manage batch operations.

## Core Commands

### Discovery & Setup
```bash
openhue discover              # Find Hue Bridge on network
openhue setup                 # Automatic configuration
openhue config                # Manual setup
```

### Query Lights & Rooms
```bash
openhue get lights            # List all lights with status/brightness
openhue get rooms             # List all rooms with status/brightness
openhue get scenes            # List available scenes
```

### Control Lights (Individual or Batch)

**Turn on/off:**
```bash
openhue set light <id-or-name> --on              # Turn on single light
openhue set light <id-or-name> --off             # Turn off single light
openhue set light Light1 Light2 Light3 --on      # Batch: turn on multiple
```

**Set brightness (0-100):**
```bash
openhue set light <id-or-name> --on --brightness 75
openhue set light Kitchen1 Kitchen2 --on --brightness 50  # Batch
```

**Set color by name:**
```bash
openhue set light <id-or-name> --on --color powder_blue
# Available: white, lime, green, blue, purple, pink, red, yellow, orange, etc.
```

**Set color by RGB hex:**
```bash
openhue set light <id-or-name> --on --rgb #FF5733
```

**Set color in CIE space:**
```bash
openhue set light <id-or-name> --on -x 0.675 -y 0.322
```

**Set color temperature (Mirek, 153-500):**
```bash
openhue set light <id-or-name> --on --temperature 250
# Lower = warmer (3000K), Higher = cooler (6500K)
```

**Transition effect:**
```bash
openhue set light <id-or-name> --on --brightness 50 --transition-time 2s
```

### Control Rooms (All lights in room at once)

Same flags as individual lights, but affects entire room:
```bash
openhue set room Kitchen --on --brightness 100
openhue set room "Living room" --off
openhue set room Bedroom Kitchen --on --brightness 30  # Batch rooms
```

### Scene Management
```bash
openhue set scene <name> --activate        # Activate a scene
openhue get scenes                         # List all available scenes
```

## Batch Operations

The CLI supports up to 10 lights/rooms simultaneously:

```bash
# Turn on multiple lights
openhue set light Light1 Light2 Light3 Light4 --on

# Set multiple lights to same brightness
openhue set light Kitchen1 Kitchen2 Kitchen3 --on --brightness 75

# Turn off all lights in multiple rooms
openhue set room Kitchen "Living room" Bedroom --off

# Mix light IDs and names
openhue set light 12345678-1234-1234-1234-c8cfbd9a99ea "Kitchen 1" --on
```

## Usage Patterns

### Turning off all lights
Get all rooms and turn off in one command:
```bash
openhue set room Kitchen Garden Driveway Office "Living room" Bedroom --off
```

### Discovering bridge
If lights aren't responding, rediscover and reconfigure:
```bash
openhue discover
openhue setup
```

### Checking current state
Before making changes, query state to see names and current brightness:
```bash
openhue get lights
openhue get rooms
```

## Implementation Notes

- **Light selection**: Use light name (exact match, case-insensitive) or UUID
- **Room selection**: Use room name (exact match) or UUID; quote multi-word names like "Living room"
- **Batch limit**: Maximum 10 lights/rooms per command
- **Colors**: Brightness must use --on flag. Color and brightness can be set together
- **Transition**: Optional timing for smooth transitions (e.g., `--transition-time 1s`)
- **Error handling**: Command returns list of affected lights on success, or error message with available names if light/room not found

## When to Use This Skill

✓ User wants to turn lights on/off
✓ User wants to adjust brightness
✓ User wants to change light color
✓ User wants to control multiple lights at once
✓ User wants to create or activate lighting scenes
✓ User needs to discover or configure Hue bridge
✓ User wants to add transition effects

## Example Interactions

**"Turn off all the lights"**
→ Run `openhue get rooms` to get room list
→ Run `openhue set room [all-rooms] --off`

**"Set the kitchen to 50% brightness"**
→ Run `openhue set room Kitchen --on --brightness 50`

**"Make the eatery lights warm and dim"**
→ Run `openhue set room Eatery --on --brightness 30 --temperature 450`

**"Turn on lights in kitchen, living room, and bedroom to 75%"**
→ Run `openhue set room Kitchen "Living room" Bedroom --on --brightness 75`

**"Set the three kitchen spots to different brightness levels"**
→ Run three separate commands:
  - `openhue set light "Kitchen 1" --on --brightness 50`
  - `openhue set light "Kitchen 2" --on --brightness 75`
  - `openhue set light "Kitchen 3" --on --brightness 100`
