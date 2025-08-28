---
title: MCP Compatible IDEs for Verify Code
description: Manual setup guide for Windsurf, Cline, Roo Code, Kilo Code and other MCP-compatible IDEs to use kluster.ai Verify Code.
---

# MCP compatible IDEs

Configure kluster.ai Verify Code in any MCP-compatible IDE with manual setup. While these IDEs don't have native Kluster extensions, they provide full verification capabilities through the standard MCP protocol.

!!! tip "Consider Native IDEs"
    For the best experience, consider using [Cursor, VS Code, or Claude Code](/verify/code/integrations/native/) which offer enhanced features and one-click installation.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## MCP configuration

Add the following to your IDE's MCP configuration file:

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

!!! warning "API Key Required"
    Replace `your-api-key-here` with your actual API key from the [kluster.ai platform](https://platform.kluster.ai){target=_blank}.

## Setup by IDE

=== "Windsurf"

    **Configuration steps**
    
    1. Open Settings by clicking the gear icon or using the command palette.
    
    2. Click **Windsurf Settings**.
    
    3. Navigate to **Cascade** in the left sidebar.
    
    4. Select **Manage MCPs** to access the MCP configuration.
    
    5. Click **View raw config** to open `mcp_config.json`.
    
    6. Add the Kluster MCP configuration shown above.
    
    7. Save the configuration and refresh.
    
    **Verification**
    
    The **Kluster-Verify-Code-MCP** will appear with both tools enabled:

    - `kluster_code_review_auto`: For code security and quality verification.
    - `kluster_dependency_validator`: For dependency validation.
    
    ![Active MCP Tools in Windsurf](/images/verify/code/integrations/windsurf/windsurf-integration-5.webp)

=== "Kilo Code"

    **Configuration steps**
    
    1. Open Settings and navigate to **MCP Servers**.
    
    2. Select the **Installed** tab.
    
    3. Click **Edit Project MCP** to open the MCP configuration.
    
    4. Add the Kluster MCP configuration shown above with your API key.
    
    5. Save and restart Kilo Code.
    
    **Verification**
    
    You should see the **Kluster-Verify-Code-MCP** server with both tools enabled:

    - `kluster_code_review_auto`: For code security and quality verification.
    - `kluster_dependency_validator`: For dependency validation.
    
    ![Kluster MCP Tools in Kilo Code](/images/verify/code/integrations/kilo/kilo-integration-2.webp)

=== "Cline"

    **Configuration steps**
    
    1. Open Cline and click **MCP Servers** in the left sidebar.
    
    2. Select the **Installed** tab.
    
    3. Click **Configure MCP Servers** to open `cline_mcp_settings.json`.
    
    4. Add the Kluster MCP configuration shown above.
    
    5. Save the configuration.
    
    **Verification**
    
    The **Kluster-Verify-Code-MCP** server will appear with both tools enabled:

    - `kluster_code_review_auto`: For code security and quality verification.
    - `kluster_dependency_validator`: For dependency validation.
    
    ![MCP Configuration in Cline](/images/verify/code/integrations/cline/cline-integration-2.webp)

=== "Roo Code"

    **Configuration steps**
    
    1. Open Roo Code and click **MCP Servers** in the left sidebar.
    
    2. Click **Edit Project MCP** to open the MCP configuration.
    
    3. The configuration file will open at `.roo/mcp_settings.json`.
    
    4. Add the Kluster MCP configuration shown above.
    
    5. Save the file.
    
    **Verification**
    
    The **Kluster-Verify-Code-MCP** server will appear with both tools enabled:

    - `kluster_code_review_auto`: For code security and quality verification.
    - `kluster_dependency_validator`: For dependency validation.
    
    ![Active MCP Tools in Roo Code](/images/verify/code/integrations/roocode/roocode-integration-2.webp)

=== "Other IDEs"

    **Generic MCP setup**
    
    For any other MCP-compatible IDE:
    
    1. Locate your IDE's MCP configuration file.
    2. Add the Kluster MCP configuration shown above.
    3. Replace `your-api-key-here` with your actual API key.
    4. Save and restart your IDE if required.
    5. The tools should now be available in your AI assistant.
    

## Next steps

- **[Learn about the tools](/verify/code/tools/)**: Understand what each tool does.
- **[See examples](/verify/code/examples/cursor-firebase-nextjs/)**: Walk through real-world scenarios.
- **[Check Native IDEs](/verify/code/integrations/native/)**: Explore IDEs with enhanced integration.