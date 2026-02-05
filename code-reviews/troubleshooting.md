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

## Need help?

If your issue isn't listed here or you need additional support, join our [Discord community](https://discord.com/invite/klusterai){target=\_blank}.
