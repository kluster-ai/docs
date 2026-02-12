---
title: CLI Quickstart
description: Install kluster-cli, authenticate, and run your first code review from the terminal.
categories: Basics, CLI
---

# Quickstart

Run [kluster.ai](https://kluster.ai){target=_blank} code reviews straight from your terminal. Install kluster-cli, authenticate with your API key, and review your first changes. No IDE or CI pipeline required.

## Prerequisites

You need:

- **A kluster.ai account**: Sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you don't have one.
- **An API key**: Get your API key from the [CLI setup page](https://platform.kluster.ai/cli){target=_blank}.

## 1. Install

=== "macOS / Linux / WSL"
    
    Run the following command in your terminal:


    ```bash
    curl -fsSL https://cli.kluster.ai/install.sh | sh
    ```

    --8<-- 'code/code-reviews/cli/install-macos.md'

=== "Windows PowerShell"
    
    Run the following command in PowerShell:

    ```powershell
    irm https://cli.kluster.ai/install.ps1 | iex
    ```

    --8<-- 'code/code-reviews/cli/install-windows.md'

For installer options, supported platforms, and troubleshooting, see [Installation](/code-reviews/cli/installation/).

## 2. Login

Authenticate the CLI with your API key:

```bash
kluster login
```

--8<-- 'code/code-reviews/cli/login.md'

When prompted, paste the API key from [platform.kluster.ai/cli](https://platform.kluster.ai/cli){target=_blank}.

## 3. Review your code

Stage some changes and run your first review:

```bash
kluster review staged
```

--8<-- 'code/code-reviews/cli/review-staged-example.md'

That's it. kluster.ai analyzes your code and flags issues with severity levels, explanations, and suggested fixes.

Want a deeper scan? Re-run the same command with `--mode deep`.

The CLI can do more than review staged changes—you can also [review diffs against branches](/code-reviews/cli/review-commands/#review-a-diff), [review individual files](/code-reviews/cli/review-commands/#review-files), or set up [git hooks](/code-reviews/cli/git-hooks/) to automate reviews on every commit or push.

## Next steps

- **[Installation](/code-reviews/cli/installation/)**: Shell completions, update system, and advanced install options.
- **[Review commands](/code-reviews/cli/review-commands/)**: Review diffs, branches, and individual files.
- **[Git hooks](/code-reviews/cli/git-hooks/)**: Automate reviews on every commit or push.
- **[Reference](/code-reviews/cli/reference/)**: Configuration, exit codes, and full command reference.
