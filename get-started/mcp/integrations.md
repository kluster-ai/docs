---
title: MCP client integrations
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

=== "Claude desktop (.dxt file)"

    The easiest way to add kluster Verify to Claude desktop is using the .dxt extension file:

    1. **Download** the extension: 
       
        [Download kluster-verify-mcp.dxt](/get-started/mcp/downloads/kluster-verify-mcp.dxt){ .md-button .md-button--primary }

    2. **Install** in Claude desktop: Drag and drop the .dxt file onto Claude desktop, then click **Install**.

        ![](/images/get-started/mcp/integrations/integrations-3.webp){ style="width:80%;" }

    3. **Add** your API key: When prompted, enter your kluster.ai API key (get one from [Get an API key guide](/get-started/get-api-key/)).

        ![](/images/get-started/mcp/integrations/integrations-4.webp){ style="width:80%;" }

    4. **Enable** extension and start using: The kluster Verify tools will be available immediately in your conversations.

        ![](/images/get-started/mcp/integrations/integrations-5.webp){ style="width:80%;" }

=== "Claude desktop (JSON config)"

    If you prefer manual configuration, you can add kluster Verify by editing Claude desktop's configuration file:

    1. Locate the configuration file:
        - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
        - **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

    2. **Add** the MCP server configuration:
    
        ```json
        --8<-- 'code/get-started/mcp/get-started/get-started-1.json'
        ```

    3. **Replace** YOUR_MCP_TOKEN with your actual MCP token (obtained after [enabling MCP](/get-started/mcp/cloud/platform/)).

    4. **Save** the file and **restart** Claude desktop to load the kluster Verify tools.

        ![](/images/get-started/mcp/get-started/get-started-1.webp){ style="width:80%;" }

=== "VS Code"

    1. Install [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot){target=\_blank} extension.
    2. Open the Chat view and click on the tools icon.

        ![](/images/get-started/mcp/integrations/integrations-1.webp){ style="width:50%;" }

    3. Choose **Add More Tools...** and click on **Add MCP Server...**.
    4. Select **Command (stdio)** and enter the following command, replacing `YOUR_MCP_TOKEN` with your actual MCP token:

        ```bash
        npx mcp-remote https://api.kluster.ai/v1/mcp \
        --header "Authorization: Bearer YOUR_MCP_TOKEN"
        ```

    5. Restart VS Code.

=== "Cursor"

    Open Cursor settings and:
    
    1. Select **Tools & Integrations**.

    2. To add your first MCP, click **Add Custom MCP**. To add additional MCPs later, use **New MCP Server**. Then enter the following configuration:
            
        ```json
        {
            "mcpServers": {
                "kluster-verify-mcp": {
                    "url": "https://api.kluster.ai/v1/mcp",
                    "headers": {
                        "Authorization": "Bearer YOUR_MCP_TOKEN"
                    }
                }
            }
        }
        ```

    3. Restart Cursor.

    ![](/images/get-started/mcp/integrations/integrations-2.webp){ style="width:80%;" }

=== "Claude code"

    Run this command in your terminal:

    ```bash
    claude mcp add kluster-verify-mcp \
      npx mcp-remote https://api.kluster.ai/v1/mcp \
      --header "Authorization: Bearer YOUR_MCP_TOKEN"
    ```

## Available tools

--8<-- 'text/get-started/mcp/overview/overview-1.md'
<!-- Commenting this for safekeeping -->
<!--See [Tools reference](/get-started/mcp/tools/){target=\_blank} for parameters and examples.-->

## SDK integrations

Looking to integrate MCP tools into your own applications? Check out our SDK integration guides:

- **[OpenAI Agents SDK](/get-started/mcp/integrations/openai-agents/)**: Build Python agents with built-in verification capabilities using OpenAI's Agents framework.

## Next steps

- [Complete setup guide](/get-started/mcp/get-started/) with usage examples.
- [Self-hosted deployment](/get-started/mcp/self-hosted/) for local development.