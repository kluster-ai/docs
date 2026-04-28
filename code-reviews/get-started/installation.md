---
title: Install kluster.ai Code Reviews for Your IDE or CLI
description: Set up kluster.ai Code Reviews in minutes. Scan code for errors, vulnerabilities, and performance issues in Cursor, VS Code, JetBrains, and more.
categories: Basics
---

# Get started with Code Reviews

Fast-moving development introduces risk. Code may contain logic errors, security flaws, or performance issues that slip through and reach production.

The [kluster.ai](https://www.kluster.ai/){target=\_blank} Code Reviews service integrates directly into your development workflow, scanning code in real-time. It catches potential issues instantly within your IDE, allowing you to ship code confidently.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## Setup instructions

### IDE extensions

=== "VS Code / Codex VS Code"

    **Install**

    1. Click the **Add to VS Code** button below:

         --8<-- 'text/install-button-vscode.md'

    2. VS Code will open and display the extension.

    3. Click **Install** to get the extension.

        ![Install Extension](/images/code-reviews/get-started/installation/vscode/vscode-integration-1.webp)

    **Log in**

    Now that the extension is installed, you need to log in with your kluster.ai account:

    1. Click on **Sign in** in the bottom right corner.
       ![Sign In](/images/code-reviews/get-started/installation/vscode/vscode-integration-2.webp)

    2. Choose **Open**. A browser pop-up window will take you to your kluster.ai account.

        ![Open Pop-up](/images/code-reviews/get-started/installation/vscode/vscode-integration-3.webp)

    3. Click **Open Visual Studio Code**.

        ![Open Visual Studio Code](/images/code-reviews/get-started/installation/vscode/vscode-integration-4.webp)

    4. Click **Open** to install the MCP with your kluster.ai API key.

        ![Open and Install MCP](/images/code-reviews/get-started/installation/vscode/vscode-integration-5.webp)

    **Enable**

    Once signed in, to enable kluster.ai in the VS Code agent chat window, take the following steps:

    1. Open a Copilot chat window and select the **Tools** button on the bottom right corner.
    2. Search for **kluster** or scroll down the list until you find **Kluster-Verify-Tool**.
    3. Check the **Kluster-Verify-Tool** box.

    ![Active MCP Tools in VS Code](/images/code-reviews/get-started/installation/vscode/vscode-integration-6.webp)

    **Uninstall**

    To remove kluster.ai from VS Code, open the Extensions panel, find **Kluster Code Reviews**, and click **Uninstall**.

=== "Cursor"

    **Install**

    1. Click the **Add to Cursor** button below.

         --8<-- 'text/install-button-cursor.md'

    2. Cursor will open and prompt for extension installation.

    3. Click **Install** to add the extension into Cursor.

        ![Extension Installation Prompt in Cursor](/images/code-reviews/get-started/installation/cursor/cursor-integration-1.webp)

    Once installed, you can verify the setup:

    1. Open **Cursor Settings**. You can use the gear icon in the top right corner to do so.
    2. Navigate to **Tools & Integrations** → **MCP Tools**.
    3. You should see **extension-Kluster-Code-Reviews** with all tools enabled:

        --8<-- 'text/code-reviews/code-tools.md'

        ![Active MCP Tools in Cursor](/images/code-reviews/get-started/installation/cursor/cursor-integration-2.webp)

    **Uninstall**

    To remove kluster.ai from Cursor, open **Settings** > **Extensions**, find **Kluster Code Reviews**, and click **Uninstall**.

=== "JetBrains"

    !!! warning "AI coding agent support"
        kluster.ai MCP integration in JetBrains requires the **Junie** AI agent. Install Junie separately from **Settings** :material-cog: → **Plugins** → **Marketplace** by searching for **Junie**. Other JetBrains AI agents are not supported.

    **Install**

    kluster.ai supports JetBrains IDEs such as IntelliJ IDEA and WebStorm. Open the JetBrains IDE of your choice, and go to **Settings** :material-cog: → **Plugins** → **Marketplace**.
    
    1. Search for **kluster**.
    2. Click **Install**.
    3. Click **Accept** when the third-party plugin notice appears, then restart the IDE if prompted.

        ![Install kluster.ai plugin from JetBrains Marketplace](/images/code-reviews/get-started/installation/jetbrains/jetbrains-integration-1.webp)

    !!! tip "Alternative: install from the JetBrains Marketplace website"
        You can also install the plugin from the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/30646-kluster-ai){target=\_blank} website. Click **Install** on the plugin page and follow the prompts to open your IDE.

    **Log in**

    Now that the plugin is installed, you need to log in with your kluster.ai account:

    1. Click **Sign in to kluster** in the plugin panel.

        ![Sign in to kluster in JetBrains](/images/code-reviews/get-started/installation/jetbrains/jetbrains-integration-2.webp)

    2. A browser window opens and takes you to your kluster.ai account. Once you authorize, a success notification appears.

        ![Browser authorization success for kluster.ai](/images/code-reviews/get-started/installation/jetbrains/jetbrains-integration-3.webp)

    3. Return to your IDE. You are now logged in.

        ![Successfully logged in to kluster.ai in JetBrains](/images/code-reviews/get-started/installation/jetbrains/jetbrains-integration-4.webp)

    **Alternative login: with an API key**

    If the browser sign-in flow is unavailable, you can log in using an API key. Retrieve your key from the [kluster.ai platform](https://platform.kluster.ai){target=\_blank} and paste it into the API key field in the plugin panel.

    Once installed, verify the setup:

    1. Open the kluster.ai plugin panel from the right sidebar.
    2. Confirm that your account is connected and the plugin is active.

        ![Active kluster.ai plugin in JetBrains](/images/code-reviews/get-started/installation/jetbrains/jetbrains-integration-5.webp)

    **Uninstall**

    To remove kluster.ai from your JetBrains IDE, go to **Settings** > **Plugins**, find **kluster.ai**, and click **Uninstall**. Restart the IDE when prompted.

=== "Visual Studio"

    !!! warning "Prerequisites"
        - **Windows x64**: The kluster.ai Visual Studio extension is only available for Windows x64. macOS and Linux are not supported.
        - **Node.js**: The Kluster-Verify-Code MCP package runs through `npx`. Install [Node.js](https://nodejs.org/){target=\_blank} before installing the extension.

    **Install**

    kluster.ai supports Visual Studio 2026 (the full IDE, not Visual Studio Code).

    1. Open Visual Studio. From the menu bar, choose **Extensions** → **Manage Extensions**.
    2. In the **Browse** tab, search for `kluster`.
    3. Select **kluster.ai** in the results, then click **Install**.

        ![Install kluster.ai extension from Visual Studio Marketplace](/images/code-reviews/get-started/installation/visualstudio/visualstudio-integration-1.webp)

    4. A notification prompts you to close Visual Studio so the installation can complete. Close Visual Studio.

    5. The **VSIX Installer** dialog opens. Click **Modify** to apply the scheduled installation.

        ![VSIX Installer Modify dialog](/images/code-reviews/get-started/installation/visualstudio/visualstudio-integration-2.webp){ width="50%" }

    6. When the **Modifications Complete** dialog appears, click **Close**.

        ![VSIX Installer Modifications Complete dialog](/images/code-reviews/get-started/installation/visualstudio/visualstudio-integration-3.webp){ width="50%" }

    7. Reopen Visual Studio.

    !!! tip "If the kluster.ai panel does not appear automatically"
        Most users see the kluster.ai tool window automatically after restart. If it does not appear, open it manually one time: from the menu bar, choose **View** → **Other Windows** → **kluster.ai**. Once shown, the panel docks like any other tool window.

        ![Open the kluster.ai panel manually from the View menu](/images/code-reviews/get-started/installation/visualstudio/visualstudio-integration-4.webp)

    **Log in**

    Now that the extension is installed, you need to log in with your kluster.ai account:

    1. Click **Sign in** in the kluster.ai panel.
    2. A browser window opens. Authorize with your kluster.ai account.
    3. Return to Visual Studio. The panel shows "Signed in as `<your-email>`."

    **Alternative login: with an API key**

    If the browser sign-in flow is unavailable, you can log in using an API key:

    1. Open the [kluster.ai platform](https://platform.kluster.ai){target=\_blank} and sign in.
    2. Click your user menu in the top-right corner.
    3. Select **Manual IDE login**.
    4. Copy the displayed key.
    5. Paste the key into the API key field in the Visual Studio panel.

    **Enable**

    To enable kluster tools in Copilot Chat:

    1. Open the **GitHub Copilot Chat** panel from **View** → **GitHub Copilot Chat** (or use Ctrl+\\, C).
    2. Click the **Filter tools** icon (wrench/funnel) in the chat input area.
    3. Under **Added**, check **Kluster-Verify-Code**. The badge should show **4/4** sub-tools enabled.

        ![Enable Kluster-Verify-Code tools in GitHub Copilot Chat](/images/code-reviews/get-started/installation/visualstudio/visualstudio-integration-5.webp)

    4. Close the popup. The Copilot Chat agent can now invoke kluster reviews.

    !!! info "Why this step is required"
        Microsoft requires manual opt-in for newly added tools in GitHub Copilot Chat. There is no way for kluster.ai to enable itself automatically.

    **Uninstall**

    To remove kluster.ai from Visual Studio, open **Extensions** → **Manage Extensions** → **Installed**, find **kluster.ai**, then click **Uninstall**. Close Visual Studio so the **VSIX Installer** can complete the removal.

=== "Windsurf"

    **Install**

    1. Click the **Add to Windsurf** button below.

         --8<-- 'text/install-button-windsurf.md'

    2. Windsurf will open and prompt for extension installation.

    3. Click **Install** to add the extension into Windsurf.

        ![Extension Installation Prompt in Windsurf](/images/code-reviews/get-started/installation/windsurf/windsurf-integration-1.webp)

    4. Select **Trust Publisher & Install**.

        ![Trust publisher](/images/code-reviews/get-started/installation/windsurf/windsurf-integration-2.webp)

    **Log in**

    Now that the extension is installed, you need to log in with your kluster.ai account:

    1. Click on **Sign in** in the bottom left corner.

        ![Sign In](/images/code-reviews/get-started/installation/windsurf/windsurf-integration-3.webp)

    2. Choose **Open**. A browser pop-up window will take you to your kluster.ai account.

        ![Open Pop-up](/images/code-reviews/get-started/installation/windsurf/windsurf-integration-4.webp)

    3. Click **Open Windsurf**.

        ![Open Windsurf](/images/code-reviews/get-started/installation/windsurf/windsurf-integration-5.webp)

    4. Click **Open** to install the MCP with your kluster.ai API key.

        ![Open and Install MCP](/images/code-reviews/get-started/installation/windsurf/windsurf-integration-6.webp)

    Once installed, verify the setup:

    1. Navigate to **Options** → **Windsurf Settings** → **MCP Servers** → **Open MCP Marketplace**.
    2. You should see **Kluster-Verify-Code** with all tools enabled.

        ![Active MCP Tools in Windsurf](/images/code-reviews/get-started/installation/windsurf/windsurf-integration-7.webp)

    **Uninstall**

    To remove kluster.ai from Windsurf, open the Extensions panel, find **Kluster Code Reviews**, and click **Uninstall**.

=== "Antigravity"

    **Install**

    1. Click the **Add to Antigravity** button below.

         --8<-- 'text/install-button-antigravity.md'

    2. Antigravity will open and prompt for extension installation.

    3. Click **Install** to add the extension into Antigravity.

        ![Extension Installation Prompt in Antigravity](/images/code-reviews/get-started/installation/antigravity/antigravity-integration-1.webp)

    **Log in**

    Now that the extension is installed, you need to log in with your kluster.ai account:

    1. Click **Sign in** in the bottom left corner.

        ![Sign In](/images/code-reviews/get-started/installation/antigravity/antigravity-integration-2.webp)

    2. Choose **Open**. A browser pop-up window will take you to your kluster.ai account.

        ![Open Pop-up](/images/code-reviews/get-started/installation/antigravity/antigravity-integration-3.webp)

    3. Click **Open Antigravity**.

        ![Open Antigravity](/images/code-reviews/get-started/installation/antigravity/antigravity-integration-4.webp)

    4. Click **Open** to install the MCP with your kluster.ai API key.

        ![Open and Install MCP](/images/code-reviews/get-started/installation/antigravity/antigravity-integration-5.webp)

    Once installed, verify the setup:

    1. Navigate to **Settings** → **MCP Settings** → **Manage MCP Servers**.
    2. Verify that **Kluster-Verify-Code** appears with all tools enabled.

        ![Active MCP Tools in Antigravity](/images/code-reviews/get-started/installation/antigravity/antigravity-integration-6.webp)

    **Uninstall**

    To remove kluster.ai from Antigravity, open the Extensions panel, find **Kluster Code Reviews**, and click **Uninstall**.

### Terminal tools

=== "Claude Code"

    **Terminal installation**

    Log in to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank}, and copy the Claude Code configuration snippet. This will include your API key.

    The command is similar to:

    --8<-- 'text/install-command-claude.md'

    This command will:

    - Download the kluster.ai MCP server.
    - Configure Claude Code settings.
    - Set up your API key.
    - Enable all review tools.

    --8<-- 'code/code-reviews/integrations/claudecode/integration-1.md'

    Once installed, verify the setup:

    1. Run the `/mcp` command in Claude Code.

        --8<-- 'code/code-reviews/integrations/claudecode/integration-2.md'

    2. Select **kluster-code-reviews** in the MCP menu list and press enter to **View tools**.

        --8<-- 'code/code-reviews/integrations/claudecode/integration-3.md'

    3. Select **View tools** to see the tools for **kluster-code-reviews** listed, including:

        --8<-- 'text/code-reviews/code-tools.md'

        --8<-- 'code/code-reviews/integrations/claudecode/integration-4.md'

    ![Claude Code Installation Demo](/images/code-reviews/get-started/installation/claudecode/claude.gif)

    **Uninstall**

    To remove kluster.ai from Claude Code, run:

    ```bash
    npx -y @klusterai/ide-installer@latest uninstall claude
    ```

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

    ![Codex CLI Installation Demo](/images/code-reviews/get-started/installation/codex-cli/codex-cli.gif)

    **Uninstall**

    To remove kluster.ai from Codex CLI, run:

    ```bash
    npx -y @klusterai/ide-installer@latest uninstall codex
    ```

=== "CLI (Standalone)"

    **Terminal installation**

    kluster-cli is a standalone command-line tool that works without an IDE or AI assistant. Install it directly on macOS, Linux, or Windows.

    === "macOS / Linux / WSL"

        ```bash
        curl -fsSL https://cli.kluster.ai/install.sh | sh
        ```

    === "Windows PowerShell"

        ```powershell
        irm https://cli.kluster.ai/install.ps1 | iex
        ```

    After installing, authenticate with your API key:

    ```bash
    kluster login
    ```

    For shell completions, updates, and more, see the full [CLI installation guide](/code-reviews/cli/installation/).

    [:octicons-arrow-right-24: CLI quickstart](/code-reviews/cli/quickstart/)

    **Uninstall**

    To remove the kluster CLI, see the [CLI installation guide](/code-reviews/cli/installation/) for platform-specific uninstall instructions.

## Next steps

- **[Human-written code](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/)**: Learn about on-demand reviews in your editor.
- **[AI-generated code](/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/)**: Learn about automatic reviews for AI-assisted coding.
- **[Pick your workflow](/code-reviews/get-started/pick-your-workflow/)**: Decide which mode fits your workflow.
