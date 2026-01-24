# Excalidraw JSON Schema Reference

Complete guide for programmatically creating `.excalidraw` files.

## File Structure

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [...],
  "appState": {...},
  "files": {}
}
```

### Top-Level Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Always `"excalidraw"` |
| `version` | integer | Yes | Schema version, use `2` |
| `source` | string | No | Origin URL |
| `elements` | array | Yes | Array of element objects |
| `appState` | object | Yes | Canvas state and settings |
| `files` | object | No | Image data (base64) for image elements |

### Minimal Valid File

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": null
  },
  "files": {}
}
```

---

## Element Types

### Common Properties (All Elements)

Every element requires these fields:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier (use nanoid or UUID) |
| `type` | string | Yes | Element type name |
| `x` | number | Yes | X coordinate (left edge) |
| `y` | number | Yes | Y coordinate (top edge) |
| `width` | number | Yes* | Width in pixels (*not for text) |
| `height` | number | Yes* | Height in pixels (*not for text) |
| `angle` | number | Yes | Rotation in radians (0 = no rotation) |
| `strokeColor` | string | Yes | Stroke/border color (hex) |
| `backgroundColor` | string | Yes | Fill color (hex or `"transparent"`) |
| `fillStyle` | string | Yes | Fill pattern |
| `strokeWidth` | number | Yes | Stroke thickness (1, 2, or 4) |
| `strokeStyle` | string | Yes | Line style |
| `roughness` | number | Yes | Hand-drawn effect (0, 1, or 2) |
| `opacity` | number | Yes | 0-100 |
| `groupIds` | array | Yes | Array of group IDs (empty if ungrouped) |
| `frameId` | string/null | Yes | Parent frame ID or null |
| `index` | string | Yes | Z-order index (use "a0", "a1", etc.) |
| `roundness` | object/null | Yes | Corner rounding config |
| `seed` | number | Yes | Random seed for hand-drawn rendering |
| `version` | number | Yes | Element version (start at 1) |
| `versionNonce` | number | Yes | Random nonce for versioning |
| `isDeleted` | boolean | Yes | Soft delete flag (use `false`) |
| `boundElements` | array | Yes | Elements bound to this one |
| `updated` | number | Yes | Timestamp (milliseconds) |
| `link` | string/null | Yes | Hyperlink or null |
| `locked` | boolean | Yes | Lock state |

### Generating IDs and Seeds

```javascript
// Generate unique ID (21 chars, alphanumeric + underscore/hyphen)
function generateId() {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-';
  let id = '';
  for (let i = 0; i < 21; i++) {
    id += chars[Math.floor(Math.random() * chars.length)];
  }
  return id;
}

// Generate random seed
function generateSeed() {
  return Math.floor(Math.random() * 2147483647);
}

// Generate version nonce
function generateVersionNonce() {
  return Math.floor(Math.random() * 2147483647);
}
```

---

## Element Type Specifications

### Rectangle

```json
{
  "id": "rect_001",
  "type": "rectangle",
  "x": 100,
  "y": 100,
  "width": 200,
  "height": 100,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#a5d8ff",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "groupIds": [],
  "frameId": null,
  "index": "a0",
  "roundness": { "type": 3 },
  "seed": 1234567890,
  "version": 1,
  "versionNonce": 987654321,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1704067200000,
  "link": null,
  "locked": false
}
```

**Roundness types:**
- `null` - Sharp corners
- `{ "type": 3 }` - Rounded corners (adaptive)
- `{ "type": 2 }` - Used for lines/arrows

### Ellipse

Same as rectangle but `"type": "ellipse"`. The width/height define the bounding box.

```json
{
  "type": "ellipse",
  "x": 100,
  "y": 100,
  "width": 150,
  "height": 150,
  "roundness": null,
  ...
}
```

### Diamond

Same as rectangle but `"type": "diamond"`. Creates a rotated square shape.

```json
{
  "type": "diamond",
  "x": 100,
  "y": 100,
  "width": 120,
  "height": 120,
  ...
}
```

### Text

```json
{
  "id": "text_001",
  "type": "text",
  "x": 100,
  "y": 100,
  "width": 150,
  "height": 25,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "groupIds": [],
  "frameId": null,
  "index": "a1",
  "roundness": null,
  "seed": 1234567890,
  "version": 1,
  "versionNonce": 987654321,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1704067200000,
  "link": null,
  "locked": false,
  "text": "Hello World",
  "fontSize": 20,
  "fontFamily": 1,
  "textAlign": "left",
  "verticalAlign": "top",
  "containerId": null,
  "originalText": "Hello World",
  "autoResize": true,
  "lineHeight": 1.25
}
```

**Text-specific properties:**

| Property | Type | Values | Description |
|----------|------|--------|-------------|
| `text` | string | - | The displayed text |
| `fontSize` | number | 16, 20, 28, 36+ | Font size in pixels |
| `fontFamily` | number | 1, 2, 3, 5 | Font family ID |
| `textAlign` | string | `"left"`, `"center"`, `"right"` | Horizontal alignment |
| `verticalAlign` | string | `"top"`, `"middle"`, `"bottom"` | Vertical alignment |
| `containerId` | string/null | - | Parent shape ID if text is inside a shape |
| `originalText` | string | - | Original text (same as `text`) |
| `autoResize` | boolean | - | Auto-resize container |
| `lineHeight` | number | 1.2, 1.25 | Line height multiplier |

**Font Family IDs:**

| ID | Font | Use Case |
|----|------|----------|
| 1 | Virgil | Hand-drawn style (legacy) |
| 2 | Helvetica | Clean, professional |
| 3 | Cascadia | Monospace, code |
| 5 | Excalifont | Hand-drawn style (current default) |

**Calculating text dimensions:**
- Width: Approximate `fontSize * 0.6 * characterCount`
- Height: `fontSize * lineHeight * lineCount`

### Arrow

```json
{
  "id": "arrow_001",
  "type": "arrow",
  "x": 100,
  "y": 100,
  "width": 200,
  "height": 50,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "groupIds": [],
  "frameId": null,
  "index": "a2",
  "roundness": { "type": 2 },
  "seed": 1234567890,
  "version": 1,
  "versionNonce": 987654321,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1704067200000,
  "link": null,
  "locked": false,
  "points": [
    [0, 0],
    [200, 50]
  ],
  "startBinding": null,
  "endBinding": null,
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "elbowed": false
}
```

**Arrow-specific properties:**

| Property | Type | Description |
|----------|------|-------------|
| `points` | array | Array of [x, y] coordinates relative to element x, y |
| `startBinding` | object/null | Binding to start element |
| `endBinding` | object/null | Binding to end element |
| `startArrowhead` | string/null | `null`, `"arrow"`, `"triangle"`, `"dot"`, `"bar"` |
| `endArrowhead` | string/null | Same options as startArrowhead |
| `elbowed` | boolean | Use elbow connector style |

**Binding object structure:**
```json
{
  "elementId": "rect_001",
  "focus": 0,
  "gap": 5
}
```

### Line

Same as arrow but `"type": "line"` and typically no arrowheads.

```json
{
  "type": "line",
  "points": [
    [0, 0],
    [100, 0],
    [100, 100]
  ],
  "startArrowhead": null,
  "endArrowhead": null,
  ...
}
```

### Frame

Frames group elements visually.

```json
{
  "id": "frame_001",
  "type": "frame",
  "x": 50,
  "y": 50,
  "width": 400,
  "height": 300,
  "angle": 0,
  "strokeColor": "#bbb",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 0,
  "opacity": 100,
  "groupIds": [],
  "frameId": null,
  "index": "a0",
  "roundness": null,
  "seed": 1234567890,
  "version": 1,
  "versionNonce": 987654321,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1704067200000,
  "link": null,
  "locked": false,
  "name": "Slide 1"
}
```

Elements inside a frame should have `"frameId": "frame_001"`.

---

## Styling Options

### Fill Styles

| Value | Description |
|-------|-------------|
| `"solid"` | Solid fill color |
| `"hachure"` | Diagonal line hatching |
| `"cross-hatch"` | Cross-hatched pattern |

### Stroke Styles

| Value | Description |
|-------|-------------|
| `"solid"` | Continuous line |
| `"dashed"` | Dashed line |
| `"dotted"` | Dotted line |

### Roughness

| Value | Description |
|-------|-------------|
| `0` | Architect (clean lines) |
| `1` | Artist (slight hand-drawn effect) |
| `2` | Cartoonist (very sketchy) |

### Stroke Width

| Value | Description |
|-------|-------------|
| `1` | Thin |
| `2` | Regular (default) |
| `4` | Bold |

---

## Color Palette (Open Colors)

Excalidraw uses the [Open Color](https://yeun.github.io/open-color/) palette. Use shade 6 for strokes, shade 2-3 for backgrounds.

### Recommended Colors for Diagrams

**Backgrounds (Light shades - use for fills):**

| Color | Hex | Use For |
|-------|-----|---------|
| Light Red | `#ffc9c9` | Warnings, errors, problems |
| Light Pink | `#fcc2d7` | Highlights, attention |
| Light Yellow | `#ffec99` | Decisions, questions |
| Light Orange | `#ffd8a8` | Actions, energy |
| Light Green | `#b2f2bb` | Success, completion, positive |
| Light Teal | `#96f2d7` | Secondary positive |
| Light Blue | `#a5d8ff` | Information, processes |
| Light Cyan | `#99e9f2` | Secondary info |
| Light Violet | `#d0bfff` | Creative, special |
| Light Grape | `#eebefa` | Alternative highlight |

**Strokes (Dark shades):**

| Color | Hex | Use For |
|-------|-----|---------|
| Near Black | `#1e1e1e` | Default stroke |
| Dark Red | `#e03131` | Error indicators |
| Dark Green | `#2f9e44` | Success indicators |
| Dark Blue | `#1971c2` | Links, interactive |
| Dark Orange | `#e8590c` | Warnings |

**Special:**

| Color | Hex | Use For |
|-------|-----|---------|
| White | `#ffffff` | Canvas background |
| Transparent | `"transparent"` | No fill |

### Complete Open Colors Reference

```
Gray:   #f8f9fa #f1f3f5 #e9ecef #dee2e6 #ced4da #adb5bd #868e96 #495057 #343a40 #212529
Red:    #fff5f5 #ffe3e3 #ffc9c9 #ffa8a8 #ff8787 #ff6b6b #fa5252 #f03e3e #e03131 #c92a2a
Pink:   #fff0f6 #ffdeeb #fcc2d7 #faa2c1 #f783ac #f06595 #e64980 #d6336c #c2255c #a61e4d
Grape:  #f8f0fc #f3d9fa #eebefa #e599f7 #da77f2 #cc5de8 #be4bdb #ae3ec9 #9c36b5 #862e9c
Violet: #f3f0ff #e5dbff #d0bfff #b197fc #9775fa #845ef7 #7950f2 #7048e8 #6741d9 #5f3dc4
Indigo: #edf2ff #dbe4ff #bac8ff #91a7ff #748ffc #5c7cfa #4c6ef5 #4263eb #3b5bdb #364fc7
Blue:   #e7f5ff #d0ebff #a5d8ff #74c0fc #4dabf7 #339af0 #228be6 #1c7ed6 #1971c2 #1864ab
Cyan:   #e3fafc #c5f6fa #99e9f2 #66d9e8 #3bc9db #22b8cf #15aabf #1098ad #0c8599 #0b7285
Teal:   #e6fcf5 #c3fae8 #96f2d7 #63e6be #38d9a9 #20c997 #12b886 #0ca678 #099268 #087f5b
Green:  #ebfbee #d3f9d8 #b2f2bb #8ce99a #69db7c #51cf66 #40c057 #37b24d #2f9e44 #2b8a3e
Lime:   #f4fce3 #e9fac8 #d8f5a2 #c0eb75 #a9e34b #94d82d #82c91e #74b816 #66a80f #5c940d
Yellow: #fff9db #fff3bf #ffec99 #ffe066 #ffd43b #fcc419 #fab005 #f59f00 #f08c00 #e67700
Orange: #fff4e6 #ffe8cc #ffd8a8 #ffc078 #ffa94d #ff922b #fd7e14 #f76707 #e8590c #d9480f
```

Shades go 0-9 (left to right, lightest to darkest).

---

## AppState Configuration

```json
{
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": null,
    "theme": "light"
  }
}
```

| Property | Type | Description |
|----------|------|-------------|
| `viewBackgroundColor` | string | Canvas background color |
| `gridSize` | number/null | Grid spacing (null = no grid) |
| `theme` | string | `"light"` or `"dark"` |

---

## Layout & Positioning Best Practices

### Canvas Dimensions

For YouTube-optimized visuals:
- **Canvas**: 1920 x 1080 (16:9)
- **Safe area**: 1720 x 880 (center)
- **Margins**: 100px from edges

### Spacing Guidelines

| Use Case | Spacing |
|----------|---------|
| Between related elements | 20-40px |
| Between sections | 60-100px |
| Inside containers (padding) | 20px |
| Arrow gap from shapes | 5-10px |

### Z-Index (index field)

Elements are rendered in order of their `index` field. Use alphabetical sorting:
- `"a0"`, `"a1"`, `"a2"` ... (background to foreground)
- Later indices render on top

### Grouping Elements

To group elements, give them the same group ID:

```json
{
  "id": "rect_001",
  "groupIds": ["group_001"],
  ...
},
{
  "id": "text_001",
  "groupIds": ["group_001"],
  ...
}
```

---

## Common Diagram Patterns

### Flowchart Node

```json
[
  {
    "id": "node_rect",
    "type": "rectangle",
    "x": 100,
    "y": 100,
    "width": 150,
    "height": 60,
    "backgroundColor": "#a5d8ff",
    "strokeColor": "#1e1e1e",
    "fillStyle": "solid",
    "strokeWidth": 2,
    "roughness": 1,
    "roundness": { "type": 3 },
    ...
  },
  {
    "id": "node_text",
    "type": "text",
    "x": 115,
    "y": 118,
    "width": 120,
    "height": 25,
    "text": "Process Step",
    "fontSize": 20,
    "fontFamily": 1,
    "textAlign": "center",
    "containerId": null,
    ...
  }
]
```

### Decision Diamond

```json
{
  "id": "decision",
  "type": "diamond",
  "x": 100,
  "y": 100,
  "width": 120,
  "height": 80,
  "backgroundColor": "#ffec99",
  "strokeColor": "#1e1e1e",
  ...
}
```

### Connected Arrow

```json
{
  "id": "connector",
  "type": "arrow",
  "x": 250,
  "y": 130,
  "width": 80,
  "height": 0,
  "points": [[0, 0], [80, 0]],
  "startBinding": {
    "elementId": "node_rect",
    "focus": 0,
    "gap": 5
  },
  "endBinding": {
    "elementId": "next_node",
    "focus": 0,
    "gap": 5
  },
  "endArrowhead": "arrow",
  ...
}
```

### Title with Highlight Box

```json
[
  {
    "id": "highlight_bg",
    "type": "rectangle",
    "x": 95,
    "y": 45,
    "width": 210,
    "height": 50,
    "backgroundColor": "#fcc2d7",
    "strokeColor": "transparent",
    "fillStyle": "solid",
    "roundness": { "type": 3 },
    "index": "a0",
    ...
  },
  {
    "id": "title_text",
    "type": "text",
    "x": 100,
    "y": 50,
    "text": "MAIN TITLE",
    "fontSize": 36,
    "fontFamily": 1,
    "strokeColor": "#1e1e1e",
    "index": "a1",
    ...
  }
]
```

---

## Validation Checklist

Before importing, verify:

- [ ] `type` is `"excalidraw"`
- [ ] `version` is `2`
- [ ] `elements` is an array
- [ ] `appState` is an object with `viewBackgroundColor`
- [ ] Every element has unique `id`
- [ ] Every element has `type`, `x`, `y`
- [ ] Arrows have `points` array with at least 2 points
- [ ] All colors are valid hex codes or `"transparent"`
- [ ] `isDeleted` is `false` for visible elements

Use the validation script:
```bash
python scripts/validate_excalidraw.py your_file.excalidraw
```

---

## Template: Empty Canvas

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": null,
    "theme": "light"
  },
  "files": {}
}
```

## Template: Single Rectangle

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "example_rect",
      "type": "rectangle",
      "x": 100,
      "y": 100,
      "width": 200,
      "height": 100,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "#a5d8ff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "index": "a0",
      "roundness": { "type": 3 },
      "seed": 1234567890,
      "version": 1,
      "versionNonce": 987654321,
      "isDeleted": false,
      "boundElements": [],
      "updated": 1704067200000,
      "link": null,
      "locked": false
    }
  ],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": null,
    "theme": "light"
  },
  "files": {}
}
```

---

## Sources

- [Excalidraw JSON Schema](https://docs.excalidraw.com/docs/codebase/json-schema)
- [Creating Elements Programmatically](https://docs.excalidraw.com/docs/@excalidraw/excalidraw/api/excalidraw-element-skeleton)
- [Open Color Palette](https://yeun.github.io/open-color/)
- [Excalidraw Constants](https://docs.excalidraw.com/docs/@excalidraw/excalidraw/api/constants)
