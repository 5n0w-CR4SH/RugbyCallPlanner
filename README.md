# Rugby Call Planner

A visual rugby play planner built with Python and Pyglet. Animate player movements on a pitch by loading pre-defined plays from a JSON file.

## Requirements

- Python 3.x
- [Pyglet](https://pyglet.org/)

```bash
pip install pyglet
```

## Setup

1. Clone or download the repository
2. Ensure `calls.json` is in the same directory as the script (see format below)
3. Run the script:

```bash
python main.py
```

## Usage

| Input | Action |
|---|---|
| Press `1` | Trigger the `Reverse_67` play |
| Left click | Place a marker on the pitch |
| Right click | Remove a marker |

## calls.json Format

Plays are stored in a JSON file. Each play contains a list of target positions for the 5 blue team players.

```json
{
  "Reverse_67": [
    { "tx": 300, "ty": 200 },
    { "tx": 320, "ty": 220 },
    { "tx": 340, "ty": 240 },
    { "tx": 360, "ty": 260 },
    { "tx": 380, "ty": 280 }
  ]
}
```

## Project Structure

```
.
├── main.py        # Main application
└── calls.json     # Play definitions
```

## Current Limitations

- 5 players per side (full 15-a-side not yet supported)
- One play keybind (`1` → `Reverse_67`)
- No reset/replay functionality
- No on-screen UI or play selector
