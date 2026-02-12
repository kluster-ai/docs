---
title: CLI Installation
description: Install kluster-cli on macOS, Linux, or Windows. Set up shell completions, configure your PATH, and keep the CLI up to date.
categories: Basics, CLI
---

# Installation

[kluster.ai](https://kluster.ai){target=_blank}'s CLI is available for macOS, Linux, and Windows. The installer downloads a single binary, adds it to your `PATH`, and you're ready to go. This page covers installation, updates, shell completions, and uninstalling.

## Install kluster-cli

=== "macOS / Linux / WSL"
    
    Run the following command in your terminal:

    ```bash
    curl -fsSL https://cli.kluster.ai/install.sh | sh
    ```

    --8<-- 'code/code-reviews/cli/install-macos.md'

    The installer places the binary at `~/.kluster/cli/bin/kluster` and adds it to your `PATH`.

    **Installer options**:

    | Flag | Description |
    |------|-------------|
    | `-b <dir>` | Custom install directory (default: `~/.kluster/cli/bin`). |
    | `-d` | Enable debug logging. |
    | `-q` | Quiet mode (errors only). |
    | `-n` | Dry run (no changes). |

=== "Windows PowerShell"

    Run the following command in PowerShell:

    ```powershell
    irm https://cli.kluster.ai/install.ps1 | iex
    ```

    --8<-- 'code/code-reviews/cli/install-windows.md'

    The installer places the binary at `%USERPROFILE%\.kluster\cli\bin\kluster.exe` and adds it to your `PATH`.

### Verify installation

After installation, verify the CLI is working:

```bash
kluster version
```

--8<-- 'code/code-reviews/cli/version-output.md'

If you get `command not found: kluster`, your `PATH` likely wasn't updated. See [Troubleshooting](/code-reviews/troubleshooting/#command-not-found-kluster).

### Login

Authenticate the CLI with your API key:

```bash
kluster login
```

--8<-- 'code/code-reviews/cli/login.md'

Get your API key from the [CLI setup page](https://platform.kluster.ai/cli){target=_blank}.

To authenticate non-interactively (useful for CI/CD):

```bash
kluster login --api-key kl_your_key_here
```

To remove stored credentials:

```bash
kluster logout
```

## Supported platforms

| OS | Architectures |
|----|---------------|
| Linux | amd64, arm64 |
| macOS | amd64 (Intel), arm64 (Apple Silicon) |
| Windows | amd64, arm64 |

## Update

The CLI can update itself to the latest version:

```bash
kluster update
```

--8<-- 'code/code-reviews/cli/update-example.md'

To check if an update is available without installing:

```bash
kluster update --check
```

--8<-- 'code/code-reviews/cli/update-check.md'

The update process downloads the latest binary, verifies its SHA256 checksum, and replaces the current installation.

## Uninstall

To remove kluster-cli, delete the installation directory:

=== "macOS / Linux / WSL"

    ```bash
    rm -rf ~/.kluster/cli
    ```

=== "Windows PowerShell"

    ```powershell
    Remove-Item -Recurse -Force "$env:USERPROFILE\.kluster\cli"
    ```

## Shell completions (optional) { #shell-completions }

Enable tab completion for commands, flags, and git branches.

=== "Bash"

    ```bash
    # Current session only
    source <(kluster completion bash)

    # Permanent (Linux, requires sudo)
    kluster completion bash | sudo tee /etc/bash_completion.d/kluster > /dev/null

    # Permanent (macOS with Homebrew)
    kluster completion bash > "$(brew --prefix)/etc/bash_completion.d/kluster"
    ```

=== "Zsh"

    ```zsh
    # Enable completions if not already
    echo "autoload -U compinit; compinit" >> ~/.zshrc

    # Add completion
    kluster completion zsh > "${fpath[1]}/_kluster"

    # Or source directly
    echo 'source <(kluster completion zsh)' >> ~/.zshrc
    ```

=== "Fish"

    ```fish
    # Current session only
    kluster completion fish | source

    # Permanent
    kluster completion fish > ~/.config/fish/completions/kluster.fish
    ```

=== "PowerShell"

    ```powershell
    # Current session only
    kluster completion powershell | Out-String | Invoke-Expression

    # Permanent (add to profile)
    kluster completion powershell >> $PROFILE
    ```

## Next steps

- **[Quickstart](/code-reviews/cli/quickstart/)**: Run your first review from the terminal.
- **[Review commands](/code-reviews/cli/review-commands/)**: All review options and output formats.
- **[Reference](/code-reviews/cli/reference/)**: Configuration, exit codes, and full command reference.
