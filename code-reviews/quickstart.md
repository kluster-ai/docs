---
title: Get started with Code Reviews
description: Set up kluster.ai Code Reviews in minutes. Scan AI-generated code for errors, vulnerabilities, and performance issues with Cursor and AI assistants.
---

# Get started with Code Reviews

Modern developers increasingly rely on AI coding assistants to accelerate development, but this speed comes with risks. Generated code may contain logic errors, security flaws, or performance issues that compromise application quality and security.

The [kluster.ai](https://www.kluster.ai/){target=\_blank} Code Reviews service integrates directly into your development workflow, automatically scanning AI-generated code in real-time. It catches potential issues instantly within your IDE, allowing you to ship code confidently while maintaining the speed benefits of AI-assisted development.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## Setup instructions

=== "Cursor"
    
    1. Click the **Add to Cursor** button below.
        
         --8<-- 'text/install-button-cursor.md'
    
    2. Cursor will open and prompt for extension installation.
    
    3. Click **Install** to add the extension into Cursor.

        ![Extension Installation Prompt in Cursor](/images/code-reviews/code/integrations/cursor/cursor-integration-1.webp)

    Once installed, you can verify the setup:

    1. Open **Cursor Settings**. You can use the gear icon in the top right corner to do so.
    2. Navigate to **Tools & Integrations** → **MCP Tools**.
    3. You should see **extension-Kluster-Code-Reviews** with all tools enabled:

        --8<-- 'text/code-reviews/code-tools.md'

        ![Active MCP Tools in Cursor](/images/code-reviews/code/integrations/cursor/cursor-integration-2.webp)

=== "VS Code / Codex VS Code"
   
    1. Click the **Add to VS Code** button below: 
        
         --8<-- 'text/install-button-vscode.md'
    
    2. VS Code will open and display the extension.
    
    3. Click **Install** to get the extension.

        ![Install Extension](/images/code-reviews/code/integrations/vscode/vscode-integration-0.webp)

    4. Select **Trust Publisher & Install**.

        ![Trust publisher](/images/code-reviews/code/integrations/vscode/vscode-integration-1.webp)

    Now that the extension is installed, you need to log in with your kluster.ai account:
       
    1. Click on **Sign in** in the bottom right corner.
       ![Sign In](/images/code-reviews/code/integrations/vscode/vscode-integration-2.webp)

    2. Choose **Open**. A browser pop-up window will take you to your kluster.ai account. 

        ![Open Pop-up](/images/code-reviews/code/integrations/vscode/vscode-integration-3.webp)
          
    3. Click **Open Visual Studio Code**.

        ![Open Visual Studio Code](/images/code-reviews/code/integrations/vscode/vscode-integration-4.webp)

    4. Click **Open** to install the MCP with your kluster.ai API key.
        
        ![Open and Install MCP](/images/code-reviews/code/integrations/vscode/vscode-integration-5.webp)

    5. To complete the setup, click **Install** to accept the MCP configuration for Code Reviews. 
    
         ![Install MCP](/images/code-reviews/code/integrations/vscode/vscode-integration-6.webp)
    6. Press **Trust** to Install the MCP server.
    ![MCP Server Trust Installation in VS Code](/images/code-reviews/code/integrations/vscode/vscode-integration-7.webp)
        
    Once installed, verify the setup:
    
    1. Open a Copilot chat window and select the **Tools** button on the bottom right corner.
    2. Scroll down the list and **Kluster-Code-Reviews-MCP** should appear. Make sure both tools enabled.

        ![Active MCP Tools in VS Code](/images/code-reviews/code/integrations/vscode/vscode-integration-8.webp)

=== "Windsurf"
    
    1. Click the **Add to Windsurf** button below.
        
         --8<-- 'text/install-button-windsurf.md'
    
    2. Windsurf will open and prompt for extension installation.
    
    3. Click **Install** to add the extension into Windsurf.

        ![Extension Installation Prompt in Windsurf](/images/code-reviews/code/integrations/windsurf/windsurf-integration-1.webp)

    4. Select **Trust Publisher & Install**.

        ![Trust publisher](/images/code-reviews/code/integrations/windsurf/windsurf-integration-2.webp)

    Now that the extension is installed, you need to log in with your kluster.ai account:
       
    1. Click on **Sign in** in the bottom left corner.
    
        ![Sign In](/images/code-reviews/code/integrations/windsurf/windsurf-integration-3.webp)

    2. Choose **Open**. A browser pop-up window will take you to your kluster.ai account. 

        ![Open Pop-up](/images/code-reviews/code/integrations/windsurf/windsurf-integration-4.webp)
          
    3. Click **Open Windsurf**.

        ![Open Windsurf](/images/code-reviews/code/integrations/windsurf/windsurf-integration-5.webp)

    4. Click **Open** to install the MCP with your kluster.ai API key.
        
        ![Open and Install MCP](/images/code-reviews/code/integrations/windsurf/windsurf-integration-6.webp)
        
    Once installed, verify the setup:
    
    1. Navigate to **Options** → **Windsurf Settings** → **MCP Servers** → **Open MCP Marketplace**.
    2. You should see **Kluster-Verify-Code** with all tools enabled.

        ![Active MCP Tools in Windsurf](/images/code-reviews/code/integrations/windsurf/windsurf-integration-7.webp)

=== "Claude Code"

    **Terminal installation**
    
    Log in to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank}, and copy the Claude Code configuration snippet. This will include your API key.

    The command is similar to:
    
    --8<-- 'text/install-command-claude.md'
    
    This command will:

    - Download the kluster.ai MCP server.
    - Configure Claude Code settings.
    - Set up your API key.
    - Enable both review tools.

    --8<-- 'code/code-reviews/integrations/claudecode/integration-1.md'
      
    Once installed, verify the setup:
    
    1. Run the `/mcp` command in Claude Code.

        --8<-- 'code/code-reviews/integrations/claudecode/integration-2.md'

    2. Select **kluster-code-reviews** in the MCP menu list and press enter to **View tools**.

        --8<-- 'code/code-reviews/integrations/claudecode/integration-3.md'

    3. Select **View tools** to see the tools for **kluster-code-reviews** listed, including:
        
        --8<-- 'text/code-reviews/code-tools.md'

        --8<-- 'code/code-reviews/integrations/claudecode/integration-4.md'

    ![Claude Code Installation Demo](/images/code-reviews/quick-start/claude.gif)

=== "Codex CLI"

    **Terminal installation**

    Log in to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank}, and copy the Codex CLI configuration snippet. This will include your API key.

    Run this command to install and configure kluster.ai for Codex CLI:

    ```bash
    npx -y @klusterai/ide-installer YOUR_API_KEY codex
    ```

    This command will:

    - Download the kluster.ai MCP server.
    - Configure Codex CLI settings.
    - Set up your API key.
    - Enable all review tools (auto, manual, and dependency check).

    --8<-- 'code/code-reviews/integrations/codex/integration-1.md'

    You can verify successful installation with the following command:

    ```bash
    codex /tools
    ```

    --8<-- 'code/code-reviews/integrations/codex/integration-2.md'

    Upon successful installation, all kluster review tools will appear in the tools list, including auto, manual, and dependency check.

    ![Codex CLI Installation Demo](/images/code-reviews/quick-start/codex-cli.gif)

## Next steps

- **[Cursor example](/code-reviews/examples/cursor-firebase-nextjs/)**: See a real-world case study using Cursor.
- **[VS-Code example](/code-reviews/examples/vscode-admin-endpoint/)**: See a real-world case study using VS-Code.