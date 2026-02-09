---
title: CLI Quickstart
description: Install kluster-cli, authenticate, and run your first code review from the terminal.
categories: Basics, CLI
---

# CLI quickstart

Run [kluster.ai](https://kluster.ai){target=_blank} code reviews straight from your terminal. Install kluster-cli, authenticate with your API key, and review your first changes. No IDE or CI pipeline required.

## Prerequisites

You need:

- **A kluster.ai account**: Sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you don't have one.
- **An API key**: Get your API key from the [CLI setup page](https://platform.kluster.ai/cli){target=_blank}.

## 1. Install

=== "macOS / Linux / WSL"

    ```bash
    curl -fsSL https://cli.kluster.ai/install.sh | sh
    ```

    --8<-- 'code/code-reviews/cli/install-macos.md'

=== "Windows PowerShell"

    ```powershell
    irm https://cli.kluster.ai/install.ps1 | iex
    ```

    --8<-- 'code/code-reviews/cli/install-windows.md'

## 2. Login

Authenticate the CLI with your API key:

```bash
kluster login
```

--8<-- 'code/code-reviews/cli/login.md'

!!! info "Where to find your API key"
    Go to [platform.kluster.ai/cli](https://platform.kluster.ai/cli){target=_blank}. Your API key is displayed in the setup instructions.

## 3. Review your code

Stage some changes and run your first review:

```bash
kluster review staged
```

--8<-- 'code/code-reviews/cli/review-staged-example.md'

That's it. kluster.ai analyzes your code and flags issues with severity levels, explanations, and suggested fixes.

## Next steps

- **[Installation](/code-reviews/cli/installation/)**: Shell completions, update system, and advanced install options.
- **[Review commands](/code-reviews/cli/review-commands/)**: Review diffs, branches, and individual files.
- **[Git hooks](/code-reviews/cli/git-hooks/)**: Automate reviews on every commit or push.
