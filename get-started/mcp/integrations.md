---
title: Client integrations
description: Connect Claude desktop, VS Code, Cursor, and Claude Code to kluster.ai verification tools with ready-to-use configuration examples.
---

# Client integrations

Connect any compatible client to [kluster.ai's](https://www.kluster.ai/){target=\_blank} MCP Verify server. This guide provides configuration examples for popular clients using [Cloud MCP](/get-started/mcp/cloud/platform/).

!!! info "Self-hosted deployment"
    For [self-hosted MCP](/get-started/mcp/self-hosted/){target=\_blank}, replace the URL with `http://localhost:3001/stream` and use your kluster.ai API key.

## Prerequisites
      
Before integrating with any client:
      
1. **Enable MCP**: Follow the [platform guide](/get-started/mcp/cloud/platform/){target=\_blank} to activate the MCP capabilities.
2. **Replace token**: Use your actual MCP token in place of `YOUR_MCP_TOKEN`.

## Configuration by client

=== "Claude desktop"

    Edit your Claude desktop configuration file:
      
    - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`.
    - **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`.

    ```json
    {
      "mcpServers": {
        "kluster-verify-mcp": {
          "command": "npx",
          "args": [
            "mcp-remote",
            "https://api.kluster.ai/v1/mcp",
            "--header",
            "Authorization: Bearer YOUR_MCP_TOKEN"
          ]
        }
      }
    }
    ```

    Restart Claude desktop to load the tools.

=== "VS Code"

    1. Install [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot){target=\_blank} extension.
    2. Open Chat view and click on the tools icon.
    3. Choose "Add More Tools..." and click on "Add MCP Server".
    4. Enter server details:
       - **Command**: `npx`
       - **Args**: `mcp-remote https://api.kluster.ai/v1/mcp --header "Authorization: Bearer YOUR_MCP_TOKEN"`.
    5. Restart VS Code.

=== "Cursor"

    1. Open Cursor settings and click on MCP.
    2. Add server configuration:
       - **Command**: `npx mcp-remote https://api.kluster.ai/v1/mcp --header "Authorization: Bearer YOUR_MCP_TOKEN"`.
    3. Enable verification tools.
    4. Restart Cursor.

=== "Claude code"

    Run this command in your terminal:

    ```bash
    claude mcp add kluster-verify-mcp \
      npx mcp-remote https://api.kluster.ai/v1/mcp \
      --header "Authorization: Bearer YOUR_MCP_TOKEN"
    ```


## Available tools

- **`verify`**: Validates claims against reliable sources.
- **`verify_document`**: Verifies claims about uploaded documents.

See [Tools reference](/get-started/mcp/tools/){target=\_blank} for parameters and examples.

## Next steps

- [Complete setup guide](/get-started/mcp/get-started/) with usage examples.
- [Self-hosted deployment](/get-started/mcp/self-hosted/) for local development.