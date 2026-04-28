---
title: Troubleshooting
description: Fix common problems with kluster.ai Code Reviews—from extension issues to CLI errors—across all supported IDEs and workflows.
categories: Troubleshooting
---

# Troubleshooting

If you encounter issues with [kluster.ai Code Reviews](https://www.kluster.ai/){target=\_blank}, check the following common errors.

## Installation

### Cannot find module './constants'

<div data-termynal>
  <span data-ty>[info] Starting new stdio process with command: npx -y @klusterai/kluster-verify-code-mcp@latest</span>
  <span data-ty style="color: #ff6b6b;">[error] node:internal/modules/cjs/loader:1247</span>
  <span data-ty style="color: #ff6b6b;">  throw err;</span>
  <span data-ty style="color: #ff6b6b;">  ^</span>
  <span data-ty style="color: #ff6b6b;">Error: Cannot find module './constants'</span>
  <span data-ty style="color: #ff6b6b;">Require stack:</span>
  <span data-ty style="color: #ff6b6b;">- /Users/.../.npm/_npx/abc123/node_modules/@klusterai/kluster-verify-code-mcp/dist/index.js</span>
</div>

This error occurs when npx caches a broken or incomplete package download. Clear the cache and restart your IDE:

=== "macOS / Linux"

    ```bash
    rm -rf ~/.npm/_npx
    ```

=== "Windows"

    ```powershell
    Remove-Item -Recurse -Force "$env:LOCALAPPDATA\npm-cache\_npx"
    ```

After clearing the cache, restart your IDE or CLI tool.

### Auto-update fails with npm cache error

<div data-termynal>
  <span data-ty>[info] Starting new stdio process with command: npx -y @klusterai/kluster-verify-node-mcp@latest</span>
  <span data-ty style="color: #ff6b6b;">npm error ENOTEMPTY: directory not empty, rename '/Users/.../.npm/_npx/.../node_modules/@klusterai/...' -> '...'</span>
</div>

The npm client sometimes fails to update cached packages when temporary directories or lock files from a previous run are left behind. This typically produces `ENOTEMPTY`, `EEXIST`, or `EPERM` errors. When the auto-update fails, the MCP server cannot start because the package download is interrupted.

Run the following command to clear the npm cache:

```bash
npm cache clean --force
```

After clearing the cache, restart your IDE or CLI tool. The next MCP invocation downloads a fresh copy of the package.

If the error persists, remove the npx cache directory manually (same step as for the [Cannot find module](#cannot-find-module-constants) error, but here it serves as a fallback after `npm cache clean`):

=== "macOS / Linux"

    ```bash
    rm -rf ~/.npm/_npx
    ```

=== "Windows"

    ```powershell
    Remove-Item -Recurse -Force "$env:LOCALAPPDATA\npm-cache\_npx"
    ```

### Claude Code MCP server shows "failed"

In Claude Code, the MCP server may show `✘ failed` on the first connection attempt. This happens because Claude Code has a 10-second timeout for MCP startup, and the initial npx download can take longer when there's no cache.

Restart Claude Code. The second attempt will use the cached package and connect successfully. Run `/mcp` to verify the MCP server is connected:

--8<-- 'code/code-reviews/troubleshooting/mcp-connected.md'

### Debugging CLI installation issues

If you're experiencing installation problems, add the `--verbose` flag to the installer command for more detailed output:

```bash
npx -y @klusterai/ide-installer YOUR_API_KEY claude --verbose
```

This helps identify where the installation process is failing.

## kluster-cli (standalone CLI)

### Command not found: kluster

<div data-termynal>
  <span data-ty  ="input"> kluster version</span>
  <span data-ty>bash: command not found: kluster</span>
</div>

The `kluster` binary is not in your `PATH`. Add the install directory:

=== "macOS / Linux"

    ```bash
    export PATH="$HOME/.kluster/cli/bin:$PATH"
    ```

    To make this permanent, add the line to your `~/.bashrc`, `~/.zshrc`, or `~/.profile`.

=== "Windows PowerShell"

    The installer should add `%USERPROFILE%\.kluster\cli\bin` to your user `PATH` automatically. If not, add it manually through **System Properties** > **Environment Variables**.

### Authentication failed

<div data-termynal>
  <span data-ty  ="input"> kluster review staged</span>
  <span data-ty style="color: #ff6b6b;">Error: not authenticated. Please run 'kluster login' first</span>
</div>

Your API key may be missing or invalid. Run `kluster login` to re-authenticate with a valid key from [platform.kluster.ai/cli](https://platform.kluster.ai/cli){target=\_blank}.

### Git hook not triggering

If a git hook doesn't run:

1. Check it's installed: `kluster hooks status`
2. Check file permissions (macOS/Linux): `ls -la .git/hooks/pre-push`
3. Fix permissions if needed: `chmod +x .git/hooks/pre-push`
4. If using a custom hooks path, check that `core.hooksPath` is set correctly.

### Review times out on large diffs

Deep mode has a 5-minute timeout. For large diffs, use instant mode instead:

```bash
kluster review staged --mode instant
```

Or split the review by reviewing individual files:

```bash
kluster review file src/large-file.go
```

## PR Reviews

### Azure DevOps PR Reviews not appearing

After connecting Azure DevOps, pull request reviews may not appear if the account used to generate the personal access token lacks the required permissions to install webhooks.

To fix this:

1. Navigate to **Azure DevOps** > **Organization Settings** > **Security** > **Permissions**.
2. Find the user account that generated the personal access token.
3. Open the **Member of** tab and add the user to **Project Collection Administrators**.
4. Return to the [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} page in the kluster.ai platform and click **Re-install** on the Azure DevOps integration.

After re-installing, each new pull request should receive review comments from the kluster.ai bot.

For more details on the required permissions, see the [Azure DevOps setup guide](/code-reviews/pr-reviews/azure-devops/).

## Need help?

If your issue isn't listed here or you need additional support, join our [Discord community](https://discord.com/invite/klusterai){target=\_blank}.
