---
title: Integrations for Code Verify
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
- **Windsurf**: AI coding assistant with Cascade and MCP integration.
- **Kilo Code**: AI coding assistant with streamlined MCP configuration.
- **Claude Code**: Manual MCP configuration via `.claude/mcp.json`.
- **Cline**: Open-source AI coding agent for VS Code with MCP marketplace.
- **Roo Code**: AI-powered dev team extension with dual configuration support.
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

    One-click installation (recommended):
    
    For the fastest setup, use our one-click installation process described in the [Get started with Verify Code](/verify/quickstart/code/){target=\_blank} guide.
    
    Manual configuration:
    
    1. Open **Cursor Settings** by clicking the gear icon on the top right corner.
    
    2. Navigate to **Tools & Integrations** in the left sidebar.
    
    3. Under **MCP Tools**, click **Add Custom MCP**.
    
        ![Cursor Settings - Tools & Integrations](/images/verify/code/integrations/cursor/cursor-integration-1.webp)
    
    4. This opens the `mcp.json` configuration file. Add the `Kluster-Verify-Code-MCP` server configuration:
    
        ![MCP Configuration File](/images/verify/code/integrations/cursor/cursor-integration-2.webp)
    
    5. Save the configuration file and return to **Cursor Settings**.
    
    The **Kluster-Verify-Code-MCP** server will now appear with both tools enabled:

    - **`kluster_bug_check_tool`**: For code security and quality verification.
    - **`kluster_frameworks_check_tool`**: For dependency validation.
      
    ![Active MCP Tools](/images/verify/code/integrations/cursor/cursor-integration-3.webp)

=== "Windsurf"

    1. Open Settings by clicking the gear icon or using the command palette.

    2. Click **Windsurf Settings**.
    
        ![Windsurf Settings](/images/verify/code/integrations/windsurf/windsurf-integration-1.webp)
    
    3. Navigate to **Cascade** in the left sidebar. 
    
    4. Select **Manage MCPs** to access the MCP configuration.
    
        ![Cascade MCP Settings](/images/verify/code/integrations/windsurf/windsurf-integration-2.webp)
        
    5. Click **View raw config** to access the MCP configuration file.
    
        ![Manage MCP Servers](/images/verify/code/integrations/windsurf/windsurf-integration-3.webp)

    6. Add the `Kluster-Verify-Code-MCP` configuration to your `mcp_config.json`:
    
        ![MCP Configuration](/images/verify/code/integrations/windsurf/windsurf-integration-4.webp)
    
    7. Save the configuration and refresh. 
      
    The **Kluster-Verify-Code-MCP** will appear with both tools enabled:
      
    - **`kluster_bug_check_tool`**: For code security and quality verification.
    - **`kluster_frameworks_check_tool`**: For dependency validation.
    
    ![Active MCP Tools](/images/verify/code/integrations/windsurf/windsurf-integration-5.webp)

=== "Kilo Code"

    1. Open Settings and navigate to **MCP Servers**.
    
    2. Select the **Installed** tab.

    3. Click **Edit Project MCP** to open the MCP configuration.

    4. Paste the content of the MCP config shown above with your API key.
        
      ![MCP Servers Settings](/images/verify/code/integrations/kilo/kilo-integration-1.webp)
    
    Then you should see the installed **Kluster-Verify-Code-MCP** server with both tools enabled:

       - **`kluster_bug_check_tool`**: For code security and quality verification.
       - **`kluster_frameworks_check_tool`**: For dependency validation.
    
    ![Kluster MCP Tools](/images/verify/code/integrations/kilo/kilo-integration-2.webp)

=== "Claude Code"

    1. Create or edit `.claude/mcp.json` in your project.
    2. Add the Code MCP server configuration shown above with your API key.
    3. Restart Claude Code and the tools will be available immediately.
    4. Run the command `/mcp` to check the status of the tools. 

    ![MCP Code Verify installed in claude code](/images/verify/code/integrations/claudecode/claudecode-integration-1.webp)

=== "Cline"

    1. Open Cline and click **MCP Servers** in the left sidebar.
    
    2. Select the **Installed** tab.
    
    3. Click on **Configure MCP Servers**, which will open the `cline_mcp_settings.json` configuration file. Add the `Kluster-Verify-Code-MCP` server configuration.

        ![Cline MCP Settings](/images/verify/code/integrations/cline/cline-integration-1.webp)
    
    4. Save the configuration.
    
    The **Kluster-Verify-Code-MCP** server will now appear with both tools enabled:

    - **`kluster_bug_check_tool`**: For code security and quality verification.
    - **`kluster_frameworks_check_tool`**: For dependency validation.

    ![MCP Configuration File](/images/verify/code/integrations/cline/cline-integration-2.webp)

=== "Roo Code"

    1. Open Roo Code and click on **MCP Servers** in the left sidebar.
    
    2. Click **Edit Project MCP** to open the MCP configuration for your project.
    
        ![MCP Servers Menu](/images/verify/code/integrations/roocode/roocode-integration-1.webp)
    
    3. The configuration file will open at `.roo/mcp_settings.json`. Add the `Kluster-Verify-Code-MCP` server configuration shown above.
    
    4. Save the file.
    
    The **Kluster-Verify-Code-MCP** server will appear with both tools enabled:

    - `kluster_bug_check_tool`: For code security and quality verification.
    - `kluster_frameworks_check_tool`: For dependency validation.
    
    ![Active MCP Tools](/images/verify/code/integrations/roocode/roocode-integration-2.webp)    

=== "Other MCP Clients"

    For any other MCP-compatible IDE or client:
    
    1. Locate your MCP configuration file (varies by client).
    2. Add the Code MCP server configuration shown above.
    3. Restart your IDE if required by the client.
    4. The tools should now be available in your AI assistant.

## Available tools

For detailed information about each tool, see our [Tools reference](/verify/code/tools/).

