# Excalidraw Keyboard Shortcuts

Quick reference for browser automation via `browser_press_key`.

## Tool Selection

| Key | Tool |
|-----|------|
| `v` or `1` | Selection |
| `h` | Hand (pan) |
| `r` | Rectangle |
| `d` | Diamond |
| `o` | Ellipse |
| `a` | Arrow |
| `l` | Line |
| `p` | Pencil (freedraw) |
| `t` | Text |
| `i` | Image |
| `e` | Eraser |

## Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl+a` | Select all |
| `Ctrl+d` | Duplicate |
| `Ctrl+c` | Copy |
| `Ctrl+v` | Paste |
| `Ctrl+x` | Cut |
| `Delete` or `Backspace` | Delete selected |
| `Ctrl+z` | Undo |
| `Ctrl+y` or `Ctrl+Shift+z` | Redo |

## Grouping & Layers

| Shortcut | Action |
|----------|--------|
| `Ctrl+g` | Group selected |
| `Ctrl+Shift+g` | Ungroup |
| `Ctrl+]` | Bring forward |
| `Ctrl+[` | Send backward |
| `Ctrl+Shift+]` | Bring to front |
| `Ctrl+Shift+[` | Send to back |

## View

| Shortcut | Action |
|----------|--------|
| `Ctrl++` | Zoom in |
| `Ctrl+-` | Zoom out |
| `Ctrl+0` | Reset zoom |
| `Shift+1` | Zoom to fit all |
| `Ctrl+f` | Find text |

## File Operations

| Shortcut | Action |
|----------|--------|
| `Ctrl+o` | Open file |
| `Ctrl+s` | Save to disk |
| `Ctrl+Shift+e` | Export |

## Element Properties

While an element is selected:

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+f` | Toggle fill |
| `Ctrl+Shift+s` | Toggle stroke |

## Text Editing

| Shortcut | Action |
|----------|--------|
| Double-click | Edit text / Add text to shape |
| `Escape` | Finish editing text |
| `Ctrl+Enter` | Finish editing text |
| `Enter` (with shape selected) | Edit text in shape |

## Canvas Navigation

| Shortcut | Action |
|----------|--------|
| `Space` + drag | Pan canvas |
| Scroll wheel | Zoom |
| `h` then drag | Pan with hand tool |

## Flowchart Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Arrow` | Create flowchart node |
| `Tab` (while creating) | Cycle shape (rectangle → diamond → ellipse) |
| `Alt+Arrow` | Move selected element |

## Usage with Playwright MCP

```
// Select rectangle tool
browser_press_key: key="r"

// Duplicate selected
browser_press_key: key="Control+d"

// Undo last action
browser_press_key: key="Control+z"

// Group selected elements
browser_press_key: key="Control+g"

// Export dialog
browser_press_key: key="Control+Shift+e"
```

Note: Use "Control" not "Ctrl" in Playwright MCP key names.
