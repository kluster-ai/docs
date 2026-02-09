---
title: Troubleshooting
description: Solutions for common issues with kluster.ai Code Reviews across all supported IDEs and CLI tools.
categories: Basics
---

# Troubleshooting

If you encounter issues with [kluster.ai Code Reviews](https://www.kluster.ai/){target=\_blank}, check the following common errors.

## Installation

### Cannot find module './constants'

<div id="termynal" data-termynal>
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

### Claude Code MCP server shows "failed"

In Claude Code, the MCP server may show `✘ failed` on the first connection attempt. This happens because Claude Code has a 10-second timeout for MCP startup, and the initial npx download can take longer when there's no cache.

Simply restart Claude Code. The second attempt will use the cached package and connect successfully. Run `/mcp` to verify the MCP server is connected:

![Claude Code MCP server status showing connected](/images/code-reviews/get-started/installation/troubleshooting/troubleshooting-1.webp)

### Debugging CLI installation issues

If you're experiencing installation problems, add the `--verbose` flag to the installer command for more detailed output:

```bash
npx -y @klusterai/ide-installer YOUR_API_KEY claude --verbose
```

This helps identify where the installation process is failing.

## kluster-cli (standalone CLI)

### Command not found: kluster

<div id="termynal" data-termynal>
  <span data-ty="input">kluster version</span>
  <span data-ty>bash: kluster: command not found</span>
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

<div id="termynal" data-termynal>
  <span data-ty="input">kluster review staged</span>
  <span data-ty style="color: #ff6b6b;">Error: not authenticated. Please run 'kluster login' first</span>
</div>

Your API key may be missing or invalid. Run `kluster login` to re-authenticate with a valid key from [platform.kluster.ai/cli](https://platform.kluster.ai/cli){target=_blank}.

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

## Need help?

If your issue isn't listed here or you need additional support, join our [Discord community](https://discord.com/invite/klusterai){target=\_blank}.
