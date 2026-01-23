# Playwright MCP Setup

## Prerequisites

The Excalidraw visual generation skill requires the Microsoft Playwright MCP server for browser automation.

## Installation

### Claude Code

Add to your MCP configuration:

```bash
claude mcp add playwright npx @playwright/mcp@latest
```

Or add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

### Recommended Configuration

For visual work, run **headed** (not headless) so you can see the browser:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--browser", "chrome"
      ]
    }
  }
}
```

### With Vision Capability

For coordinate-based clicking (useful if accessibility snapshots miss elements):

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--browser", "chrome",
        "--caps", "vision"
      ]
    }
  }
}
```

## Key Playwright MCP Tools

### Navigation
- `browser_navigate` - Go to URL
- `browser_navigate_back` - Go back

### Interaction
- `browser_click` - Click element by ref
- `browser_type` - Type text into element
- `browser_press_key` - Press keyboard key
- `browser_drag` - Drag and drop
- `browser_hover` - Hover over element

### Inspection
- `browser_snapshot` - Get accessibility tree (for finding refs)
- `browser_take_screenshot` - Capture current view
- `browser_console_messages` - Get console output

### Window Management
- `browser_resize` - Change viewport size
- `browser_tabs` - Manage browser tabs

## Excalidraw-Specific Tips

### Authentication
The first time you navigate to your Excalidraw+ workspace, you may need to log in. Since Playwright runs headed by default, you can manually log in while Claude waits.

### Canvas Interaction
Excalidraw is a canvas-based app, so standard accessibility refs may be limited. Use:
1. Keyboard shortcuts (most reliable)
2. Vision mode for coordinate clicking
3. `browser_evaluate` for direct JavaScript if needed

### Viewport Size
Set a consistent viewport for YouTube-friendly dimensions:

```
browser_resize: width=1920, height=1080
```

## Troubleshooting

### Browser not visible
Ensure you're not passing `--headless` flag. Default is headed mode.

### Can't find elements
Canvas elements don't appear in accessibility snapshots. Use:
- Keyboard shortcuts to select tools
- Screenshots to see current state
- Vision mode (`--caps vision`) for coordinate clicking

### Authentication issues
Playwright preserves session by default. Log in once and sessions persist.
