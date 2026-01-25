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

### Algorithms & Data Structures
Arrays, matrices, trees, linked lists, and algorithm visualization components.
**Contains**: Array blocks, tree nodes, matrix grids, linked list elements, and connecting arrows.
**Use for**: Algorithm tutorials, data structure education, CS concept explanations.
**Location**: `libraries/algorithms-and-data-structures-arrays-matrices-trees.excalidrawlib`

### Architecture Diagram Components
System and software architecture building blocks.
**Contains**: Components, containers, connectors, and system boundaries.
**Use for**: System architecture diagrams, component design, technical documentation.
**Location**: `libraries/architecture-diagram-components.excalidrawlib`

### Artem's Icons
Minimalist line-based icon collection.
**Contains**: 22 custom icons with clean line-based design.
**Use for**: Adding stylized icons to diagrams, UI mockups, visual decoration.
**Location**: `libraries/artem-s-icons.excalidrawlib`

### Awesome Icons
Rich icon set with diverse symbols and status indicators.
**Contains**: Cancel, checkmarks, status badges, and various UI icons.
**Use for**: UI mockups, status indicators, interface elements.
**Location**: `libraries/awesome-icons.excalidrawlib`

### AWS Architecture Icons
Cloud infrastructure and service icons for AWS diagrams.
**Contains**: EC2, S3, Lambda, RDS, CloudFront, CloudSearch, and 50+ other AWS service icons with proper branding.
**Use for**: Architecture diagrams, cloud infrastructure visuals, AWS service flows, system design presentations.
**Location**: `libraries/aws-architecture-icons.excalidrawlib`

### Basic Shapes
Primitive geometric shapes for building diagrams.
**Contains**: Lines, circles, rectangles, and basic geometric primitives.
**Use for**: Foundation drawing, simple wireframes, basic diagram building blocks.
**Location**: `libraries/basic-shapes.excalidrawlib`

### Basic UX Wireframing Elements
UI/UX wireframing components.
**Contains**: Buttons, inputs, dropdowns, checkboxes, and 69 UI elements.
**Use for**: Website wireframes, app mockups, user interface design, lo-fi prototypes.
**Location**: `libraries/basic-ux-wireframing-elements.excalidrawlib`

### Bubbles
Speech bubbles and dialogue elements.
**Contains**: Speech bubbles, thought bubbles, and communication shapes.
**Use for**: Conversation flows, storytelling, dialogue diagrams, chat UI mockups.
**Location**: `libraries/bubbles.excalidrawlib`

### Cloud
Cloud service icons and infrastructure components.
**Contains**: Cloud service icons, server symbols, and 19 infrastructure elements.
**Use for**: Cloud infrastructure diagrams, platform architecture, service integration flows.
**Location**: `libraries/cloud.excalidrawlib`

### Cloud Design Patterns
Cloud architecture patterns and distributed system components.
**Contains**: Pattern diagrams, data flow arrows, service blocks, and labeled components.
**Use for**: AWS/Cloud architecture patterns, distributed system visualization, design pattern docs.
**Location**: `libraries/cloud-design-patterns.excalidrawlib`

### Data Sources
Database and data system icons.
**Contains**: Database symbols, data pipelines, ETL components, and storage icons.
**Use for**: Data pipeline diagrams, database visualization, ETL flows, data architecture.
**Location**: `libraries/data-sources.excalidrawlib`

### Data Viz
Data visualization components for charts and dashboards.
**Contains**: Bar charts, line graphs, pie charts, metrics displays, and 32 visualization elements.
**Use for**: Charts, graphs, dashboards, analytics mockups, KPI displays.
**Location**: `libraries/data-viz.excalidrawlib`

### Database Engineering
Database schema and table design elements.
**Contains**: Table structures, relationships, keys, and schema components.
**Use for**: Database schema design, ER diagrams, data model documentation.
**Location**: `libraries/db-eng.excalidrawlib`

### Decision Flow Control
Flowchart and decision tree elements.
**Contains**: Decision diamonds, flow arrows, conditional branches, and process paths.
**Use for**: Flowcharts, decision trees, algorithm visualization, business workflows.
**Location**: `libraries/decision-flow-control.excalidrawlib`

### DevOps
DevOps and infrastructure components.
**Contains**: CI/CD pipeline stages, containers, deployment elements, and monitoring icons.
**Use for**: CI/CD pipeline diagrams, infrastructure architecture, deployment workflows.
**Location**: `libraries/dev_ops.excalidrawlib`

### Drwnio
General purpose diagramming elements.
**Contains**: Standard shapes, connectors, and general diagram components.
**Use for**: General-purpose diagrams, flowcharts, basic technical diagrams.
**Location**: `libraries/drwnio.excalidrawlib`

### Emojis
Colored folder and file icons.
**Contains**: Folders in gray, red, pink, purple, blue, teal, green, yellow, orange colors.
**Use for**: File structure diagrams, folder organization visuals, system hierarchy.
**Location**: `libraries/emojis.excalidrawlib`

### Forms
UI form controls and input elements.
**Contains**: Buttons (default and blue), input fields, form controls.
**Use for**: UI/UX wireframing, form layout design, web interface mockups.
**Location**: `libraries/forms.excalidrawlib`

### Gantt
Gantt charts and timeline components.
**Contains**: Timeline bars, team rows, month headers, task status indicators (Done, Delayed, Pending, Critical).
**Use for**: Project timelines, Gantt charts, team capacity planning, roadmaps.
**Location**: `libraries/gantt.excalidrawlib`

### Google Icons
Google Material Design icons.
**Contains**: Material Design icons for navigation, actions, and communication.
**Use for**: Modern UI mockups, Material Design interfaces, Android-style designs.
**Location**: `libraries/google-icons.excalidrawlib`

### Icons
General purpose icon library.
**Contains**: Business icons, professional symbols, various visual elements.
**Use for**: General diagramming, business process visualization, documentation.
**Location**: `libraries/icons.excalidrawlib`

### Information Architecture
Site map and navigation structure elements.
**Contains**: Page blocks, navigation structures, hierarchy elements.
**Use for**: Website information architecture, site maps, content structure planning.
**Location**: `libraries/information-architecture.excalidrawlib`

### IT Logos
Technology company and software logos.
**Contains**: Tech company logos, software vendor icons, platform identifiers.
**Use for**: Technology stack visualization, enterprise software diagrams, tool integration.
**Location**: `libraries/it-logos.excalidrawlib`

### Lo-Fi Wireframing Kit
Low-fidelity wireframe components.
**Contains**: Text labels, buttons, inputs, navigation bars, basic UI placeholders.
**Use for**: Quick UI sketching, rapid prototyping, layout brainstorming.
**Location**: `libraries/lo-fi-wireframing-kit.excalidrawlib`

### Post-it
Sticky notes and Kanban-style elements.
**Contains**: Sticky notes, colored task cards, list items.
**Use for**: Brainstorming sessions, Kanban boards, agile sprint planning, idea organization.
**Location**: `libraries/post-it.excalidrawlib`

### Robots
Hand-drawn robot figures.
**Contains**: Robot characters in various poses (sitting, standing, active).
**Use for**: Tech/automation infographics, AI content, robotics illustrations.
**Location**: `libraries/robots.excalidrawlib`

### Software Architecture
Software architecture diagram components.
**Contains**: Colored diamonds, containers, decision points, system boundaries.
**Use for**: Software architecture diagrams, system design, API visualization.
**Location**: `libraries/software-architecture.excalidrawlib`

### Some Hand-Drawn Signs
Checkmarks and crosses.
**Contains**: Hand-drawn checkmarks and crosses in red/green colors.
**Use for**: Success/failure indicators, form validation visuals, approval workflows.
**Location**: `libraries/some-handdrawn-signs.excalidrawlib`

### Stick Figures
Stick figure people in various poses.
**Contains**: Stick figures with different postures and expressions.
**Use for**: User flows, process diagrams, storytelling, educational content.
**Location**: `libraries/stick-figures.excalidrawlib`

### Stick People
Stick people variations.
**Contains**: Additional stick people designs and poses.
**Use for**: User journey mapping, scenario illustrations, presentation visuals.
**Location**: `libraries/stick-people.excalidrawlib`

### Storytelling
Narrative and storytelling elements.
**Contains**: Character shapes, scene elements, narrative components.
**Use for**: Visual storytelling, presentation narratives, educational illustrations.
**Location**: `libraries/storytelling.excalidrawlib`

### System Design
System design components with labeled elements.
**Contains**: Application servers, databases, clients, and labeled system blocks.
**Use for**: System design interviews, architecture diagrams, distributed systems.
**Location**: `libraries/system-design.excalidrawlib`

### System Icons
Simple system UI icons.
**Contains**: Colored status circles (purple, red, green), status indicators.
**Use for**: Dashboard designs, status indicator systems, interface mockups.
**Location**: `libraries/system-icons.excalidrawlib`

### Systems Design Components
System design building blocks.
**Contains**: Server components, load balancers, caches, and infrastructure elements.
**Use for**: System design diagrams, scalability patterns, infrastructure planning.
**Location**: `libraries/systems-design-components.excalidrawlib`

### Technology Logos
Technology and programming logos.
**Contains**: Tech logos with colored backgrounds (purple, various colors).
**Use for**: Tech stack visualization, portfolio showcases, integration diagrams.
**Location**: `libraries/technology-logos.excalidrawlib`

### UML-ER Library
UML and Entity-Relationship diagram elements.
**Contains**: Diamonds, rectangles, ellipses, and 21 UML/ER components.
**Use for**: Database schemas, class diagrams, entity relationships, UML designs.
**Location**: `libraries/UML-ER-library.excalidrawlib`

### Universal UI Kit
Comprehensive UI component library.
**Contains**: Status boxes (attention, error, success), alert dialogs, pricing cards, web templates.
**Use for**: Complete UI mockups, website prototypes, SaaS pricing pages, error message templates.
**Location**: `libraries/universal-ui-kit.excalidrawlib`

### Web Kit
Professional web template components.
**Contains**: Navigation bars, hero sections, CTAs, statistics counters, pricing tiers.
**Use for**: Website design mockups, landing page prototypes, portfolio templates.
**Location**: `libraries/web-kit.excalidrawlib`


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
NOTE:  Read [reference/keyboard-shortcuts.md](reference/keyboard-shortcuts.md) if you have trouble viewing / taking screenshot of full canvas.

Fix any visual bugs found and revalidate (Do Phase 4-5 again)

When your excalidraw looks fine, you should clean up the valiation app by running below script:
```bash
python3 scripts/clean_validation_app.py
```


