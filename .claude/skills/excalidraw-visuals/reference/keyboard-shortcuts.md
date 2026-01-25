# Excalidraw Keyboard Shortcuts

Complete reference for browser automation via `browser_press_key`.

> **Important**: Use `Control` not `Ctrl` in Playwright MCP key names.

## Tool Selection

| Key | Tool | Alternative |
|-----|------|-------------|
| `V` | Selection | `1` |
| `H` | Hand (pan) | |
| `R` | Rectangle | `2` |
| `D` | Diamond | `3` |
| `O` | Ellipse | `4` |
| `A` | Arrow | `5` |
| `L` | Line | `6` |
| `P` | Pencil (freedraw) | `7` |
| `T` | Text | `8` |
| `9` | Insert image | |
| `E` | Eraser | `0` |
| `F` | Frame tool | |
| `K` | Laser pointer | |

## Editing & Manipulation

| Shortcut | Action |
|----------|--------|
| `Control+A` | Select all |
| `Control+D` | Duplicate |
| `Control+C` | Copy |
| `Control+V` | Paste |
| `Control+X` | Cut |
| `Control+Shift+V` | Paste as plaintext |
| `Delete` or `Backspace` | Delete selected |
| `Control+Z` | Undo |
| `Control+Y` or `Control+Shift+Z` | Redo |
| `Alt+drag` | Duplicate while dragging |
| `Shift+drag` | Constrain proportions (squares, circles) |
| `Shift+Arrow` | Move element by 5px |

## Grouping & Layers

| Shortcut | Action |
|----------|--------|
| `Control+G` | Group selected |
| `Control+Shift+G` | Ungroup |
| `Control+]` | Bring forward |
| `Control+[` | Send backward |
| `Control+Shift+]` | Bring to front |
| `Control+Shift+[` | Send to back |
| `Control+Shift+L` | Lock/unlock selection |

## Alignment

| Shortcut | Action |
|----------|--------|
| `Control+Shift+Up` | Align top |
| `Control+Shift+Down` | Align bottom |
| `Control+Shift+Left` | Align left |
| `Control+Shift+Right` | Align right |

## View & Canvas

| Shortcut | Action |
|----------|--------|
| `Control++` | Zoom in |
| `Control+-` | Zoom out |
| `Control+0` | Reset zoom |
| `Shift+1` | Zoom to fit all |
| `Shift+2` | Zoom to selection |
| `Control+'` | Toggle grid (20px alignment) |
| `Alt+S` | Toggle snap to objects |
| `Alt+Z` | Zen mode |
| `Alt+R` | View mode |
| `Alt+Shift+D` | Toggle dark/light theme |
| `Alt+/` | Stats for nerds (element dimensions) |
| `Control+F` | Find text |
| `PgUp/PgDn` | Move page up/down |
| `Shift+PgUp/PgDn` | Move page left/right |

## Canvas Navigation

| Shortcut | Action |
|----------|--------|
| `Space` + drag | Pan canvas |
| Scroll wheel | Zoom |
| `H` then drag | Pan with hand tool |

## Text Editing

| Shortcut | Action |
|----------|--------|
| Double-click | Edit text / Add text to shape |
| `Enter` (with shape selected) | Edit text in shape |
| `Escape` | Finish editing text |
| `Control+Enter` | Finish editing text |
| `Control+Shift+<` | Decrease font size |
| `Control+Shift+>` | Increase font size |

## Shape & Element Properties

| Shortcut | Action |
|----------|--------|
| `S` | Stroke color picker |
| `G` | Background color picker |
| `Control+Alt+C` | Copy styles |
| `Control+Alt+V` | Paste styles |
| `Shift+H` | Flip horizontal |
| `Shift+V` | Flip vertical |

## Lines & Arrows

| Shortcut | Action |
|----------|--------|
| `Control+Enter` | Edit line/arrow points |
| `A` + click × 3 | Curved arrow |
| `L` + click × 3 | Curved line |
| `Control` (while connecting) | Prevent arrow binding |

## Flowchart Creation

| Shortcut | Action |
|----------|--------|
| `Control+Arrow` | Create connected flowchart node |
| `Tab` (while creating) | Cycle shape (rectangle → diamond → ellipse) |

## Links & Search

| Shortcut | Action |
|----------|--------|
| `Control+K` | Add/update link |
| `Control+F` | Find text in scene |
| `Control+P` | Find scene (in Excalidraw+ workspace) |
| `Control+/` | Command palette |
| `?` or `Shift+/` | Show shortcuts help |

## File Operations

| Shortcut | Action |
|----------|--------|
| `Control+O` | Open file |
| `Control+S` | Save to disk |
| `Control+Shift+E` | Export dialog |
| `Shift+Alt+C` | Copy as PNG |

## Selection Techniques

| Shortcut | Action |
|----------|--------|
| Click + drag | Box select |
| `Shift+click` | Add to selection / Deep select in box |
| `Control+click` | Deep select (select within group) |

---

## Usage with Playwright MCP

```javascript
// Select rectangle tool
browser_press_key: key="R"

// Duplicate selected
browser_press_key: key="Control+D"

// Undo last action
browser_press_key: key="Control+Z"

// Group selected elements
browser_press_key: key="Control+G"

// Toggle grid
browser_press_key: key="Control+'"

// Toggle snap to objects
browser_press_key: key="Alt+S"

// Zoom to fit all
browser_press_key: key="Shift+1"

// Export dialog
browser_press_key: key="Control+Shift+E"

// Copy styles from element
browser_press_key: key="Control+Alt+C"

// Paste styles to element
browser_press_key: key="Control+Alt+V"
```

## Mac vs Windows

| Windows | Mac |
|---------|-----|
| `Control` | `Command` (Meta) |
| `Alt` | `Option` |

When using Playwright MCP on Mac, use `Meta` instead of `Control` for command shortcuts.

---