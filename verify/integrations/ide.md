---
title: Native IDEs Integration for Verify Code
description: One-click installation for Cursor, VS Code, and Claude Code with enhanced Verify Code features and custom extensions.
---

# Native IDE integration

Get the best Verify Code experience with native IDE integrations. These IDEs offer one-click installation, custom extensions, and enhanced AI behavior for seamless code verification.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## Setup instructions

=== "Cursor"
    
    1. Click the **Add to Cursor** button below.
        
         --8<-- 'text/install-button-cursor.md'
    
    2. Cursor will open and prompt for extension installation.
    
    3. Click **Install** to add the extension into Cursor.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/cursor/cursor-integration-1.webp)
    
    4. Now that the extension is active, click on **Install** on the bottom left corner to install the MCP tools.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/cursor/cursor-integration-2.webp)
    
    5. To finish the setup, click on **Install** to confirm the MCP settings. 

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/cursor/cursor-integration-3.webp)

    Once installed, you can verify the setup:

    1. Open **Cursor Settings**. You can use the gear icon in the top right corner to do so.
    2. Navigate to **Tools & Integrations** → **MCP Tools**.
    3. You should see **Kluster-Verify-Code-MCP** with both tools enabled:

        --8<-- 'text/verify/code-tools.md'

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/cursor/cursor-integration-4.webp)

=== "VS Code"
   
    1. Click the **Add to VS Code** button below: 
        
         --8<-- 'text/install-button-vscode.md'
    
    2. VS Code will open and display the extension.
    
    3. Click **Install** to get the extension.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-0.webp)

    4. Select **Trust Publisher & Install**.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-1.webp)

    Now that the extension is installed, you need to login with your kluster.ai account:
       
    1. Click on **Sign in** in the bottom right corner.
       ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-2.webp)

    2. Choose **Open**. A browser pop-up window will take you to your kluster.ai account. 

        ![Pop up](/images/verify/code/integrations/vscode/vscode-integration-3.webp)
          
    3. Click **Open Visual Studio Code**.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-4.webp)

    4. Click **Open** to install the MCP with your kluster.ai API key.
        
        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-5.webp)

    5. To complete the setup, click **Install** to accept the MCP configuration for Verify Code. 
    
         ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-6.webp)
    6. Press **Trust** to Install the MCP server.
    ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-7.webp)
        
    Once installed, verify the setup:
    
    1. Open a Copilot chat window and select the **Tools** button on the bottom right corner.
    2. Scroll down the list and **Kluster-Verify-Code-MCP** should appear. Make sure both tools enabled.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-8.webp)

=== "Claude Code"

    **Terminal installation**
    
    Copy and paste this command in your terminal. Replace `your-api-key-here` with your actual API key from the [kluster.ai platform](https://platform.kluster.ai){target=_blank}.
    
    --8<-- 'text/install-command-claude.md'
    
    This command will:

    - Download the kluster.ai MCP server.
    - Configure Claude Code settings.
    - Set up your API key.
    - Enable both verification tools.

    --8<-- 'code/verify/integrations/claudecode/integration-1.md'
      
    Once installed, verify the setup:
    
    1. Run the `/mcp` command in Claude Code.

        --8<-- 'code/verify/integrations/claudecode/integration-2.md'

    2. Select **kluster-verify** in the MCP menu list and press enter to **View tools**.

        --8<-- 'code/verify/integrations/claudecode/integration-3.md'

    3. Select **View tools** to see the tools for **kluster-verify** listed, including:
        
        --8<-- 'text/verify/code-tools.md'

        --8<-- 'code/verify/integrations/claudecode/integration-4.md'

## Next steps

- **[Learn about the tools](/verify/tools/)**: Understand issue types and priorities.
- **[View examples](/verify/examples/cursor-firebase-nextjs/)**: See real-world case studies.