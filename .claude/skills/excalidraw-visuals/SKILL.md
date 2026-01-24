---
name: generating-excalidraw-visuals
description: Generates hand-drawn style visuals from video scripts by creating Excalidraw JSON files programmatically, then importing into Excalidraw for visual validation. Use when creating diagrams, flowcharts, infographics, or illustrations for YouTube videos, educational content, or presentations.
---

# Excalidraw Visual Generation

Create professional hand-drawn style visuals by generating `.excalidraw` JSON files programmatically, then validating them visually in the browser.

## Prerequisites

- **Required**: Playwright MCP server for visual validation. See [reference/playwright-setup.md](reference/playwright-setup.md).
- **Required**: Read [reference/excalidraw-json-schema.md](reference/excalidraw-json-schema.md) before generating JSON.
- **Required**: Read [reference/Presenting_Information_Visually.pdf](reference/Presenting_Information_Visually.pdf) for design principles.

## Approach: JSON-First

**Why JSON-first instead of browser automation?**
- Precise control over element positioning and styling
- Reproducible results
- Faster iteration
- Browser only used for validation, not drawing

## Workflow Overview

```
1. Analyze script → Identify visual moments
2. Design layout → Plan element positions
3. Create task plan → Break JSON generation into chunks (avoids token limits)
4. Generate JSON incrementally → Build .excalidraw file piece by piece
5. Validate JSON → Run validation script
6. Import to browser → Drag & drop file
7. Visual check → Screenshot and review
8. Iterate → Adjust JSON if needed
9. Export → Save final visuals
```

## Defaults

- **One scene per request**: Create exactly ONE `.excalidraw` file containing all visual moments, unless user explicitly requests multiple
- **Output location**: Save files to project root or user-specified location
- **Naming**: Use descriptive names like `context-engineering-diagram.excalidraw`

---

## Step-by-Step Workflow

### Step 1: Analyze Script for Visual Segments

Read the script and identify moments that benefit from visuals:

| Script Pattern | Visual Type | JSON Approach |
|----------------|-------------|---------------|
| "Today we'll learn about X" | Concept introduction | Central rectangle with radiating elements |
| "First... then... finally" | Process/Flow | Connected rectangles with arrows |
| "X vs Y" or "compared to" | Comparison | Side-by-side rectangles |
| "There are 3 types..." | Categories | Grouped containers |
| "The architecture includes..." | System diagram | Boxes with connecting arrows |
| Statistics or percentages | Data visual | Large text with supporting shapes |

### Step 2: Design Layout

Before writing JSON, plan your layout:

**Canvas**: 1920 x 1080 (YouTube optimized)
**Safe area**: Keep content within 100-1820 x, 100-980 y

Sketch mentally or note:
- Main elements and their approximate positions
- Connection flow (arrows)
- Color coding scheme
- Text content for labels

### Step 3: Create Task Plan

**CRITICAL**: Before generating JSON, create a task plan to avoid hitting token limits. Large diagrams with many elements can exceed output limits if generated all at once.

**Why plan first?**
- Excalidraw JSON is verbose (each element requires 15+ fields)
- A diagram with 10+ elements can easily exceed token limits
- Breaking work into chunks ensures complete, valid output

**How to plan:**

1. Review the visual segments identified in Step 1
2. Create a TODO task for each logical chunk of work
3. Each task should represent a manageable piece of JSON generation

**Guidance for chunking (flexible, not rigid rules):**

| Approach | When to Use |
|----------|-------------|
| One task per visual segment | Default approach - each scene/moment gets its own task |
| One task per element group | When a single segment has many related elements (e.g., a flowchart with 8 boxes) |
| One task per element type | When building systematically (all rectangles, then all text, then all arrows) |

**Example task plan for a flowchart diagram:**

```
TODO 1: Create base file structure and canvas setup
TODO 2: Generate main process boxes (rectangles for steps 1-4)
TODO 3: Generate decision diamond and branch boxes
TODO 4: Generate text labels for all shapes
TODO 5: Generate arrow connectors between elements
TODO 6: Final assembly and validation
```

**Example task plan for a multi-scene video:**

```
TODO 1: Create base file structure
TODO 2: Scene 1 - Introduction concept diagram (central box + radiating elements)
TODO 3: Scene 2 - Comparison chart (side-by-side boxes)
TODO 4: Scene 3 - Process flow (connected rectangles)
TODO 5: Final validation and positioning adjustments
```

**Task creation tips:**
- Use the TaskCreate tool to track progress
- Each task should produce a defined set of elements
- Include element IDs in task descriptions for cross-referencing
- Mark tasks complete as you generate each chunk

---

### Step 4: Generate Excalidraw JSON

**CRITICAL**: Read [reference/excalidraw-json-schema.md](reference/excalidraw-json-schema.md) first.

Create the `.excalidraw` file with this structure:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    // Your elements here
  ],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": null,
    "theme": "light"
  },
  "files": {}
}
```

#### Incremental Generation Strategy

Follow your task plan from Step 3. For each task:

1. **First task**: Create the base file with empty `elements` array
2. **Subsequent tasks**: Read the file, add new elements to the array, write back
3. **Use Edit tool**: Append elements to the `elements` array rather than rewriting the entire file

**Example incremental workflow:**

```
Task 1: Write base structure
  → Write file with "elements": []

Task 2: Add main boxes
  → Edit file: insert rectangle elements into array

Task 3: Add text labels
  → Edit file: append text elements to array

Task 4: Add arrows
  → Edit file: append arrow elements to array
```

This approach keeps each operation within token limits and produces a complete, valid file.

#### Element Creation Checklist

For each element, ensure:
- [ ] Unique `id` (21 alphanumeric chars)
- [ ] Correct `type` (rectangle, ellipse, diamond, text, arrow, line, frame)
- [ ] Position: `x`, `y` coordinates
- [ ] Size: `width`, `height`
- [ ] Style: `strokeColor`, `backgroundColor`, `fillStyle`, `strokeWidth`, `roughness`
- [ ] All required fields from schema

#### Quick Reference: Common Elements

**Rectangle (process box):**
```json
{
  "id": "box_001",
  "type": "rectangle",
  "x": 100, "y": 100,
  "width": 200, "height": 80,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#a5d8ff",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "angle": 0,
  "groupIds": [],
  "frameId": null,
  "index": "a0",
  "roundness": { "type": 3 },
  "seed": 123456789,
  "version": 1,
  "versionNonce": 987654321,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1704067200000,
  "link": null,
  "locked": false
}
```

**Text label:**
```json
{
  "id": "label_001",
  "type": "text",
  "x": 120, "y": 125,
  "width": 160, "height": 30,
  "text": "Process Step",
  "fontSize": 24,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "angle": 0,
  "groupIds": [],
  "frameId": null,
  "index": "a1",
  "roundness": null,
  "seed": 234567890,
  "version": 1,
  "versionNonce": 876543210,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1704067200000,
  "link": null,
  "locked": false,
  "containerId": null,
  "originalText": "Process Step",
  "autoResize": true,
  "lineHeight": 1.25
}
```

**Arrow connector:**
```json
{
  "id": "arrow_001",
  "type": "arrow",
  "x": 300, "y": 140,
  "width": 100, "height": 0,
  "points": [[0, 0], [100, 0]],
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "startBinding": null,
  "endBinding": null,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "angle": 0,
  "groupIds": [],
  "frameId": null,
  "index": "a2",
  "roundness": { "type": 2 },
  "seed": 345678901,
  "version": 1,
  "versionNonce": 765432109,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1704067200000,
  "link": null,
  "locked": false,
  "elbowed": false
}
```

### Step 5: Validate JSON

Run the validation script before importing:

```bash
python scripts/validate_excalidraw.py your_file.excalidraw
```

Fix any errors reported.

### Step 6: Import to Excalidraw

Use Playwright to import and validate:

```
1. browser_navigate to: https://excalidraw.com
2. Wait for canvas to load
3. Use browser_file_upload or drag-drop simulation to import the .excalidraw file
4. browser_take_screenshot to capture result
```

**Import method - File Upload:**
```javascript
// The file input accepts .excalidraw files
// Navigate to excalidraw.com, then use Ctrl+O or menu to open file
```

**Alternative - Direct URL with data:**
For quick testing, you can also copy-paste JSON directly into excalidraw.com using the import feature.

### Step 7: Visual Validation

After importing, take a screenshot:

```
browser_take_screenshot
```

Check for:
- [ ] All elements visible and positioned correctly
- [ ] Text readable and not overlapping
- [ ] Colors match design intent
- [ ] Arrows connecting properly
- [ ] Overall composition balanced

### Step 8: Iterate if Needed

If visual check reveals issues:
1. Identify problem in JSON (position, size, color, etc.)
2. Edit the `.excalidraw` file
3. Re-validate with script
4. Re-import and screenshot

### Step 9: Export Final Visuals

Once satisfied:
- Scene auto-saves if using excalidraw.com account
- Export as PNG: `Ctrl+Shift+E` → PNG
- Export as SVG: For scalable graphics

---

## Style Guidelines

**CRITICAL**: Follow [reference/Presenting_Information_Visually.pdf](reference/Presenting_Information_Visually.pdf) principles.

### Color Palette (Quick Reference)

**Backgrounds:**
| Purpose | Color | Hex |
|---------|-------|-----|
| Information/Process | Light Blue | `#a5d8ff` |
| Success/Positive | Light Green | `#b2f2bb` |
| Decision/Question | Light Yellow | `#ffec99` |
| Warning/Important | Light Pink | `#ffc9c9` |
| Action/Energy | Light Orange | `#ffd8a8` |
| Creative/Special | Light Violet | `#d0bfff` |

**Strokes:**
| Purpose | Color | Hex |
|---------|-------|-----|
| Default | Near Black | `#1e1e1e` |
| Transparent | - | `"transparent"` |

### Typography

| Level | Size | Use |
|-------|------|-----|
| Title | 36-48px | Main headings |
| Section | 24-28px | Section labels |
| Body | 20px | Default text |
| Detail | 16px | Annotations |

### Roughness Settings

| Value | Style | Use |
|-------|-------|-----|
| 0 | Clean/Architect | Technical diagrams |
| 1 | Hand-drawn | Default, friendly |
| 2 | Sketchy | Informal, creative |

### DO and DON'T

**DO:**
- Use clear, concise labels (2-4 words max)
- Maintain consistent colors for related concepts
- Leave breathing room between elements (40-60px)
- Use visual hierarchy (size, color, position)
- Keep total elements under 20 for clarity

**DON'T:**
- Overcrowd the canvas
- Use more than 4-5 colors
- Write paragraphs of text
- Mix conflicting color schemes
- Forget accessibility (contrast)

---

## Diagram Patterns

### Flowchart Pattern

```
[Start] ──▶ [Process] ──▶ ◇Decision◇ ──▶ [End]
                              │
                              ▼
                          [Alt Path]
```

- Start/End: Rounded rectangles, green (`#b2f2bb`)
- Process: Rectangles, blue (`#a5d8ff`)
- Decision: Diamonds, yellow (`#ffec99`)

### Comparison Pattern

```
┌─────────────┐     VS     ┌─────────────┐
│   Option A  │            │   Option B  │
│  (details)  │            │  (details)  │
└─────────────┘            └─────────────┘
```

- Left side: One color family
- Right side: Contrasting color family

### Central Concept Pattern

```
            ┌─────────┐
       ┌────│ CENTRAL │────┐
       │    └─────────┘    │
       ▼                   ▼
   [Branch 1]          [Branch 2]
```

- Central: Larger, prominent color
- Branches: Smaller, supporting colors
- Arrows: Radiating outward

### Timeline Pattern

```
●────────●────────●────────●
│        │        │        │
2020    2021    2022    2023
```

- Horizontal line as spine
- Circles as milestones
- Text below for labels

---

## File Management

### Output Structure

```
project/
├── visuals/
│   ├── intro-diagram.excalidraw
│   ├── process-flow.excalidraw
│   └── exports/
│       ├── intro-diagram.png
│       └── process-flow.png
```

### Naming Convention

`{topic}-{type}.excalidraw`

Examples:
- `context-engineering-overview.excalidraw`
- `api-flow-diagram.excalidraw`
- `comparison-chart.excalidraw`

---

## Troubleshooting

### JSON Won't Import

1. Run validation script - check for errors
2. Verify `"type": "excalidraw"` at top level
3. Check all elements have required fields
4. Ensure no duplicate IDs

### Elements Not Visible

1. Check `isDeleted` is `false`
2. Verify `opacity` is 100
3. Check x, y coordinates are within canvas
4. Verify `index` ordering

### Text Not Showing

1. Ensure `text` field is not empty
2. Check `fontSize` is reasonable (16-48)
3. Verify `fontFamily` is valid (1, 2, 3, or 5)
4. Check `strokeColor` is visible (not white on white)

### Arrows Not Connecting

1. Verify `points` array has at least 2 points
2. Check `startBinding`/`endBinding` reference valid element IDs
3. Ensure arrow `x`, `y` plus points reach target elements

---

## References

- [Excalidraw JSON Schema](reference/excalidraw-json-schema.md) - Complete element specifications
- [Style Guide](reference/style-guide.md) - Color and typography guidelines
- [Visual Presentation PDF](reference/Presenting_Information_Visually.pdf) - Design principles
- [Keyboard Shortcuts](reference/keyboard-shortcuts.md) - For manual adjustments
- [Playwright Setup](reference/playwright-setup.md) - Browser automation config
