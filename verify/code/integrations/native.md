---
title: Native IDE Integration
description: One-click installation for Cursor, VS Code, and Claude Code with enhanced Verify Code features and custom extensions.
---

# Native IDE integration

Get the best Verify Code experience with native IDE integrations. These IDEs offer one-click installation, custom extensions, and enhanced AI behavior for seamless code verification.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## Setup instructions

=== "Cursor"
    
    1. Click **Add to Cursor** button below.
        
         --8<-- 'text/install-button-cursor.md'
    
    2. Cursor will open and prompt for extension installation.
    
    3. Click **Install** to add the extension into Cursor.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/cursor/cursor-integration-1.webp)
    
    4. Now that the extension is active. Click on **Install** MCP on the bottom left corner.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/cursor/cursor-integration-2.webp)
    
    5. To finish the setup, click on **Install** to confirm the MCP settings. 

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/cursor/cursor-integration-3.webp)

    Once installed, you can verify the setup:

    1. Open **Cursor Settings** (gear icon → Settings).
    2. Navigate to **Tools & Integrations** → **MCP Tools**.
    3. You should see **Kluster-Verify-Code-MCP** with both tools enabled:
        - `kluster_code_review_auto`: For code security and quality verification.
        - `kluster_dependency_validator`: For dependency validation.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/cursor/cursor-integration-4.webp)

=== "VS Code"
   
    1. Click **Add to VS Code** button below: 
        
         --8<-- 'text/install-button-vscode.md'
    
    2. VS Code will open with the extension installation.
    
    3. Click **Install** to get the extension.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-0.webp)

    4. Select **Trust Publisher & Install**.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-1.webp)

    Now the extension is installed, we need to login with our kluster.ai account:
       
    1. Click on **Login** on the bottom right corner.
       
    2. Choose **Open**. A browser pop up window will take you to your kluster.ai account. 

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-2.webp)
          
    3. Click **Open Visual Studio Code**

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-3.webp)

    4. To complete the setup now click on **Open**. This will install the MCP with your kluster.ai API key.  
        
        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-4.webp)

    5. For the last step, click on Install to accept the MCP configuration for Verify Code. 
    
         ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-5.webp)
        
    Once installed, verify the setup:
    
    1. Select the **Tools** button on the bottom right corner in the Copilot chat window.
    2. Scroll down the list and **Kluster-Verify-Code-MCP** should appear with both tools enabled.

        ![Active MCP Tools in Cursor](/images/verify/code/integrations/vscode/vscode-integration-6.webp)

=== "Claude Code"

    **Terminal installation**
    
    Copy and paste this command on your terminal. Replace `your-api-key-here` with your actual API key from the [kluster.ai platform](https://platform.kluster.ai){target=_blank}.
    
    --8<-- 'text/install-command-claude.md'
    
    This command will:

    - Download the kluster.ai MCP server.
    - Configure Claude Code settings.
    - Set up your API key.
    - Enable both verification tools.

    ![MCP Code Verify installed in Claude Code](/images/verify/code/integrations/claudecode/claudecode-integration-1.webp)
      
    Once installed, verify the setup:
    
    1. Run the `/mcp` command in Claude Code.

        ![MCP Code Verify installed in Claude Code](/images/verify/code/integrations/claudecode/claudecode-integration-2.webp)

    2. Select kluster-verify in the MCP menu list and press enter to **View tools**.

        ![MCP Code Verify installed in Claude Code](/images/verify/code/integrations/claudecode/claudecode-integration-3.webp)

    3. You should see tools for **kluster-verify** listed with:
        - `kluster_code_review_auto`
        - `kluster_dependency_validator`
    
        ![MCP Code Verify installed in Claude Code](/images/verify/code/integrations/claudecode/claudecode-integration-4.webp)


## Next steps

- **[Learn about the tools](/verify/code/tools/)**: Understand issue  types and priorities.
- **[View examples](/verify/code/examples/cursor-firebase-nextjs/)**: See real-world case studies.