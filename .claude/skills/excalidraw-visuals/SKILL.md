---
name: generating-excalidraw-visuals
description: Generates hand-drawn style visuals from video scripts by creating Excalidraw JSON files programmatically, then importing into Excalidraw for visual validation. Use when creating diagrams, flowcharts, infographics, or illustrations for YouTube videos, educational content, or presentations.
---

# Excalidraw Visual Generation

Create professional hand-drawn style visuals by generating `.excalidraw` JSON files programmatically, then validating them visually in the browser.

---

## Guidelines of Phased based approach for creating Excalidraw json files


### Phase 1: Analyze Script for Visual Segments

Read the script and identify moments that benefit from visuals:

| Script Pattern | Visual Type | JSON Approach |
|----------------|-------------|---------------|
| "Today we'll learn about X" | Concept introduction | Central rectangle with radiating elements |
| "First... then... finally" | Process/Flow | Connected rectangles with arrows |
| "X vs Y" or "compared to" | Comparison | Side-by-side rectangles |
| "There are 3 types..." | Categories | Grouped containers |
| "The architecture includes..." | System diagram | Boxes with connecting arrows |
| Statistics or percentages | Data visual | Large text with supporting shapes |


### Phase 2: Create Task Plan and intial empty Excalidraw json file.

**Initial Excalidraw JSON**: Create the intial Excalidraw json file in the output directory.  Give it a unqiue descriptive name with .excalidraw extension.  Format output/<Unique descriptive name>.excalidraw

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

### Phase 3: Generate Excalidraw JSON
In this phase you should be filling the output/<Unique descriptive name>.excalidraw with json from the task list identfied in Phase 2.

**CRITICAL**: Read [reference/Presenting_Information_Visually.pdf](reference/Presenting_Information_Visually.pdf) principles to understand design best practices

**CRITICAL**: Read [reference/excalidraw-json-schema.md](reference/excalidraw-json-schema.md) to understand the excalidraw json schema.

**CRITICAL**: Reuse Excalidraw library visuals whenever possible. You can reuse as is Or you can extend / modify the library visual.  Below are the available libraries, read only into context window when needed

## Available Libraries

### AWS Architecture Icons
Cloud infrastructure and service icons for AWS diagrams.
**Contains**: EC2, S3, Lambda, RDS, CloudFront, CloudSearch, and 50+ other AWS service icons with proper branding.
**Use for**: Architecture diagrams, cloud infrastructure visuals, AWS service flows, system design presentations.
**Location**: `libraries/aws-architecture-icons.excalidrawlib`


### Phase 4: Validate JSON

Run the validation script before importing:

```bash
python3 scripts/validate_excalidraw.py output/your_file.excalidraw
```

Fix any errors reported.

### Phase 5: Visual Validation

Use Playwright MCP to validate output/your_file.excalidraw visually:

First, copy your validated excalidraw from phase 4 to the validation-app using below script:
```bash
python3 scripts/copy_to_validation.py your_file.excalidraw
```

Next, start the validation app and use playwright MCP to take a screenshot so you can visually validate your work.
```
1. Start the local validation app: cd validation-app && pnpm run dev
2. Use Playwright MCP to navigate to: http://localhost:3000
3. browser_take_screenshot to capture result
```

Fix any visual bugs found and revalidate (Do Phase 4-5 again)

When your excalidraw looks fine, you should clean up the valiation app by running below script:
```bash
python3 scripts/clean_validation_app.py
```


