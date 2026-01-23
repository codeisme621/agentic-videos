---
name: generating-excalidraw-visuals
description: Generates hand-drawn style visuals from video scripts using Excalidraw in the browser. Use when creating diagrams, flowcharts, infographics, or illustrations for YouTube videos, educational content, or presentations. Requires Playwright MCP server for browser automation.
---

# Excalidraw Visual Generation

Create professional hand-drawn style visuals from video scripts using browser-based Excalidraw automation.

## Prerequisites

**Required**: Playwright MCP server must be configured. See [reference/playwright-setup.md](reference/playwright-setup.md).

## Quick Start

1. Parse script for visual moments
2. Open Excalidraw workspace in browser
3. Create visuals using browser automation
4. Take screenshots to verify work
5. Export/save completed scenes

## Workflow

Copy this checklist and track progress:

```
Visual Generation Progress:
- [ ] Step 1: Analyze script for visual segments
- [ ] Step 2: Navigate to Excalidraw workspace
- [ ] Step 3: Create new scene for each visual
- [ ] Step 4: Build diagram using browser tools
- [ ] Step 5: Screenshot to verify appearance
- [ ] Step 6: Iterate based on visual feedback
- [ ] Step 7: Export final visuals
```

### Step 1: Analyze Script for Visual Segments

Read the script and identify moments that benefit from visuals:

| Script Pattern | Visual Type | Excalidraw Approach |
|----------------|-------------|---------------------|
| "Today we'll learn about X" | Concept introduction | Central title with branching ideas |
| "First... then... finally" | Process/Flow | Flowchart with arrows |
| "X vs Y" or "compared to" | Comparison | Side-by-side boxes |
| "There are 3 types..." | Categories | Grouped containers |
| "The architecture includes..." | System diagram | Boxes with connections |
| Statistics or percentages | Data visual | Simple charts or callouts |

### Step 2: Navigate to Excalidraw Workspace

```
Use Playwright MCP to navigate:
browser_navigate to: https://app.excalidraw.com/w/9sxW7DF3QzC/dashboard
```

If authentication is needed, the user can log in manually while browser is visible.

### Step 3: Create New Scene

From the dashboard:
1. Click "New Scene" or use keyboard shortcut
2. Name the scene descriptively (e.g., "01_intro_concept")

### Step 4: Build Diagram Using Browser Tools

**Core Excalidraw keyboard shortcuts** (use browser_press_key):
- `R` - Rectangle tool
- `O` - Ellipse tool  
- `A` - Arrow tool
- `L` - Line tool
- `T` or double-click - Text tool
- `V` or `1` - Selection tool
- `H` - Hand/pan tool
- `Ctrl+D` - Duplicate selected
- `Ctrl+G` - Group selected
- `Ctrl+Shift+G` - Ungroup

**Element creation pattern**:
1. Press key for tool (e.g., `R` for rectangle)
2. Click and drag on canvas to create
3. Double-click to add text inside shapes
4. Use arrow tool to connect elements

### Step 5: Screenshot to Verify Appearance

**CRITICAL**: After making changes, take a screenshot to see what you created:

```
browser_take_screenshot
```

This allows you to:
- Verify element placement
- Check text readability
- Assess overall composition
- Identify needed adjustments

### Step 6: Iterate Based on Visual Feedback

After each screenshot:
1. Assess if the visual follows style guidelines (see below)
2. Adjust colors, spacing, or text as needed
3. Screenshot again to verify changes
4. Repeat until satisfied

### Step 7: Export Final Visuals

**Export options**:
- `Ctrl+Shift+E` - Export dialog
- Menu → Export image → PNG (for video overlays)
- Menu → Export image → SVG (for scaling)
- Scene auto-saves to workspace

---

## Style Guidelines

Follow these principles from visual communication best practices:

### Visual Processing Advantage
Visuals are processed 60,000x faster than text. Keep diagrams simple and scannable.

### Gestalt Principles
- **Closure**: Viewers mentally complete incomplete shapes
- **Continuity**: Use arrows/lines to guide the eye
- **Proximity**: Group related items close together
- **Similarity**: Use consistent colors for related concepts

### Color Usage

**Warm colors** (positive/active concepts):
- Light red/pink: `#ffc9c9`
- Light yellow: `#ffec99`
- Light orange: `#ffd8a8`

**Cool colors** (neutral/passive concepts):
- Light blue: `#a5d8ff`
- Light green: `#b2f2bb`
- Light purple: `#d0bfff`

**Stroke color**: Near black `#1e1e1e` for contrast

### Typography Hierarchy
- **Titles**: 36-48px, bold weight
- **Labels**: 24-28px, regular weight
- **Details**: 16-20px, lighter or smaller

### Diagram Types

**Flowcharts** (for processes):
- Use rectangles for actions
- Use diamonds for decisions
- Use rounded rectangles for start/end
- Connect with arrows showing flow direction

**Comparison Charts** (for A vs B):
- Side-by-side boxes with VS divider
- Consistent sizing for both sides
- Color code each side differently

**Concept Maps** (for ideas):
- Central concept in larger shape
- Branches radiate outward
- Related items grouped by color

**Infographics** (for data/stats):
- Large numbers as focal point
- Icons to reinforce meaning
- Minimal text, maximum visual

### Keep It Simple
- Use clear, concise labels
- Limit to 5-7 elements per visual
- Maintain consistent spacing
- Use visual hierarchy to prioritize content
- Avoid cluttering with too many elements

---

## Browser Automation Reference

### Playwright MCP Tools for Excalidraw

**Navigation**:
```
browser_navigate: url="https://app.excalidraw.com/..."
```

**Click elements**:
```
browser_click: element="New Scene button", ref="[from snapshot]"
```

**Type text**:
```
browser_type: element="text input", ref="[from snapshot]", text="Your text"
```

**Press keys**:
```
browser_press_key: key="r"  // Select rectangle tool
browser_press_key: key="Control+d"  // Duplicate
```

**Take screenshot** (essential for visual verification):
```
browser_take_screenshot
```

**Get page snapshot** (for finding element refs):
```
browser_snapshot
```

### Workflow Pattern

1. `browser_snapshot` → Understand current page state
2. `browser_click` or `browser_press_key` → Perform action
3. `browser_take_screenshot` → Verify visual result
4. Repeat as needed

---

## Import/Export JSON

To start from an existing template:

1. Have user provide `.excalidraw` JSON file
2. In Excalidraw: Menu → Open (Ctrl+O)
3. Select and upload the file
4. Modify as needed
5. Export when complete

To save work:
1. Menu → Save to disk (Ctrl+S)
2. Or Menu → Export → select format

---

## Error Handling

**If Excalidraw workspace requires login**:
- Pause and ask user to authenticate in the visible browser
- Continue once logged in

**If element not found in snapshot**:
- Take a fresh `browser_snapshot`
- Look for updated element references

**If visual doesn't look right**:
- Take screenshot to assess
- Identify specific issue (color, position, size)
- Make targeted adjustment
- Screenshot again to verify

**If browser is headless/not visible**:
- Playwright MCP should run headed by default
- If issues, suggest user check Playwright MCP config
