---
title: Integrations
description: Set up kluster.ai code checks in your IDE via MCP. One-click install for Cursor, or manually configure Claude Code & other MCP-compatible tools.
---

# Integrations

The [kluster.ai](https://www.kluster.ai/){target=_blank} Code verification service is designed to integrate directly into your IDE workflow, providing real-time code analysis as you develop. By leveraging MCP, Code verification works seamlessly with AI coding assistants to catch issues before they reach your codebase.

For Cursor users, a one-click installation process is available that handles all setup automatically. See the [Code Quick Start guide](/verify/quickstart/code/){target=_blank} for the fastest way to get started.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## Supported IDEs

Code verification works with any MCP-compatible client, including:

- **Cursor**: One-click installation with automatic MCP server setup (most popular).
- **Claude Code**: Manual MCP configuration required.
- **Any MCP-compatible IDE**: Manual configuration using the MCP server details below.

## MCP configuration

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

## Setup instructions

=== "Cursor"

    **One-click installation (recommended)**
    
    For the fastest setup, use our one-click installation process described in the [Code Quick Start guide](/verify/quickstart/code/){target=\_blank}.
    
    **Manual configuration**
    
    If you prefer manual setup:
    
    1. Open Cursor settings.
    2. Navigate to MCP configuration.
    3. Add the Code MCP server configuration shown above.
    4. Restart Cursor to load the tools.

=== "Claude Code"

    1. Create or edit `.claude/mcp.json` in your project.
    2. Add the Code MCP server configuration shown above.
    3. Restart Claude Code, tools will be available immediately.

=== "Other MCP Clients"

    For any other MCP-compatible IDE or client:
    
    1. Locate your MCP configuration file (varies by client).
    2. Add the Code MCP server configuration shown above.
    3. Restart your IDE if required by the client.
    4. The tools should now be available in your AI assistant.

## Available tools

Once configured, you'll have access to:

- `kluster_bug_check_tool` - Detect bugs and quality issues.
- `kluster_packages_check_tool` - Validate dependencies.

For detailed information about each tool, see our [Tools reference](/verify/code/tools/){target=\_blank}.

