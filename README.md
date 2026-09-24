# Hex Workshop

X-Seti - September 2026 - standalone build of the IMG Factory 1.6 hex editor.

Hex editor for any file, with RenderWare section tools in the style of Steve M's RW Analyze.

## Run

```
pip install -r requirements.txt
python3 launch.py [file]
```

Requires Python 3.10+ and PyQt6.

Also docked inside IMG Factory 1.6 (right button bar: Hex, or the Intro page).

## Features

- Hex / ASCII editing, overwrite or insert mode, undo / redo, modified bytes highlighted
- Big files open instantly (painted on demand)
- Find, find all, replace: hex, ASCII, UTF-16, integers, floats (LE / BE)
- Go to offset: hex, decimal, relative (+/-), from end
- Bookmarks, insert / fill / delete bytes, import / export bytes
- Data inspector: int8-64, float, COL fixed point, RW version stamp
- Compare with another file, difference ranges highlighted
- Hashes: CRC32, MD5, SHA1, SHA256
- Safe saves: timestamped backup, atomic write

## Structure tree

- RenderWare streams (.dff .txd .rws ...): blue complex, green data, orange empty, red faulty
- Validate, recompute sizes, change RW version, append a file, texture names
- Per section: export, import, copy, paste, clear, delete (parent sizes kept right)
- COL models, IMG v2 entries, .dir listings, SA binary IPL
- Convert DFF / TXD / COL between GTA III, VC and SA (single or batch)

## Shortcuts

| Key | Action |
|-----|--------|
| Ctrl+O / Ctrl+S | Open / Save |
| Ctrl+F, F3, Shift+F3 | Find, next, previous |
| Ctrl+G | Go to offset |
| Ctrl+B | Bookmark |
| Ctrl+Z / Ctrl+Y | Undo / Redo |
| Insert | Toggle insert mode |

## Settings

Stored in `~/.config/imgfactory/` (`hex_workshop.json`, ribbon and splitter layout).

## Layout

- `apps/components/Hex_Editor/` - Hex Workshop; tool-only code in `depends/`
- `apps/methods/` - shared IMG Factory methods (kept identical to IMG Factory)
- `apps/themes/`, `apps/utils/` - global themes and settings
