---
title: Integrations
description: Set up kluster.ai Code verification in Cursor and Claude Code using MCP.
---

# Integrations

Code verification is available through MCP (Model Context Protocol) in supported IDEs.

## Supported IDEs

- **Cursor**: Full MCP support with Code verification tools
- **Claude Code**: Native integration with Code verification

## MCP Configuration

Add the following to your MCP configuration file:

```json
{
  "mcpServers": {
    "Kluster-Verify-Code-MCP": {
      "command": "npx",
      "args": [
        "@klusterai/kluster-verify-code-mcp@latest"
      ],
      "env": {
        "KLUSTER_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Setup Instructions

### Cursor

1. Open Cursor settings
2. Navigate to MCP configuration
3. Add the Code MCP server configuration
4. Restart Cursor to load the tools

### Claude Code

1. Create or edit `.claude/mcp.json` in your project
2. Add the Code MCP server configuration
3. The tools will be available immediately

## Available Tools

Once configured, you'll have access to:

- `kluster_bug_check_tool` - Detect bugs and quality issues
- `kluster_frameworks_check_tool` - Validate dependencies

## Getting Your API Key

To use Code verification, you'll need a kluster.ai API key:

1. Visit [kluster.ai](https://kluster.ai)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Generate a new key for Code verification