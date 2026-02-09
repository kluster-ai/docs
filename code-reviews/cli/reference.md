---
title: CLI Reference
description: All kluster-cli commands, configuration options, exit codes, and environment variables in one place.
categories: CLI, Reference
---

# CLI reference

Complete reference for all kluster-cli commands, configuration options, and exit codes. Use this page for quick lookups on commands, flags, config file settings, and environment variables.

## Commands

=== "Review"

    | Command | Description |
    |---------|-------------|
    | `kluster review staged` | Review staged changes |
    | `kluster review staged --mode deep` | Deep analysis mode |
    | `kluster review diff <target>` | Review diff against branch or commit range |
    | `kluster review file <path> [paths...]` | Review one or more files |

=== "History"

    | Command | Description |
    |---------|-------------|
    | `kluster log` | List recent reviews (default: 20) |
    | `kluster log --limit <n>` | Limit results (max: 100) |
    | `kluster show <review-id>` | View full review details |

=== "Hooks"

    | Command | Description |
    |---------|-------------|
    | `kluster hooks install <hook>` | Install a hook (`pre-commit`, `pre-push`, `all`) |
    | `kluster hooks install <hook> --block-on <level>` | Set blocking severity (`critical`, `high`, `medium`, `low`) |
    | `kluster hooks install <hook> --warn-only` | Show issues without blocking |
    | `kluster hooks uninstall <hook>` | Remove a hook |
    | `kluster hooks status` | Show installed hooks |

=== "Auth"

    | Command | Description |
    |---------|-------------|
    | `kluster login` | Authenticate with API key |
    | `kluster login --api-key <key>` | Authenticate non-interactively |
    | `kluster logout` | Remove stored credentials |

=== "Utility"

    | Command | Description |
    |---------|-------------|
    | `kluster version` | Print version info |
    | `kluster update` | Update to latest version |
    | `kluster update --check` | Check for updates without installing |
    | `kluster completion <shell>` | Generate shell completions (`bash`, `zsh`, `fish`, `powershell`) |

## Configuration

kluster-cli uses a YAML config file with optional environment variable overrides.

### Config file

The config file is created automatically on first use:

| OS | Location |
|----|----------|
| macOS / Linux | `~/.kluster/cli/config.yaml` |
| Windows | `%USERPROFILE%\.kluster\cli\config.yaml` |

**Available settings:**

| Key | Default | Description |
|-----|---------|-------------|
| `api_key` | — | Your kluster.ai API key (set by `kluster login`) |
| `api_url` | `https://api.kluster.ai` | API endpoint |
| `output` | `table` | Default output format |

Example config file:

```yaml
api_key: kl_your_api_key_here
api_url: https://api.kluster.ai
output: table
```

### Environment variables

Environment variables override config file values. All variables use the `KLUSTER_` prefix:

| Variable | Overrides | Example |
|----------|-----------|---------|
| `KLUSTER_API_KEY` | `api_key` | `export KLUSTER_API_KEY=kl_abc123` |
| `KLUSTER_API_URL` | `api_url` | `export KLUSTER_API_URL=https://custom.endpoint` |
| `KLUSTER_OUTPUT` | `output` | `export KLUSTER_OUTPUT=json` |

This is useful for CI/CD pipelines where you don't want to store a config file:

```bash
KLUSTER_API_KEY=kl_abc123 kluster review staged
```

### Output formats

The CLI supports three output formats, configurable globally or per command:

=== "Table (default)"

    Human-readable format with colors and borders. Best for interactive use.

    ```bash
    kluster log --output table
    ```

=== "JSON"

    Machine-readable format. Best for scripts and CI/CD integration.

    ```bash
    kluster log --output json
    ```

=== "Text"

    Simple pipe-separated format. Easy to parse with standard Unix tools.

    ```bash
    kluster log --output text
    ```

Set the default format globally:

```yaml
# ~/.kluster/cli/config.yaml
output: json
```

Or override per command with the `--output` flag:

```bash
kluster log --output json
```

### Configuration priority

When the same setting is defined in multiple places, the CLI uses this order (highest priority first):

1. **Command-line flags** — `--output json`
2. **Environment variables** — `KLUSTER_OUTPUT=json`
3. **Config file** — `output: json` in `config.yaml`
4. **Built-in defaults** — `table`

## Authentication

Your API key is stored in the config file and managed through the `login` and `logout` commands:

```bash
# Save your API key
kluster login

# Remove your API key
kluster logout
```

Get your API key from the [CLI setup page](https://platform.kluster.ai/cli){target=_blank}.

You can also provide the API key directly without the interactive prompt:

```bash
kluster login --api-key kl_your_key_here
```

## Exit codes

### Review commands

| Code | Meaning |
|:----:|---------|
| `0` | No issues found |
| `1` | Low severity issues found |
| `2` | Medium severity issues found |
| `3` | High severity issues found |
| `4` | Critical severity issues found |

The exit code reflects the **highest** severity issue found. This makes it easy to use in scripts:

```bash
kluster review staged
if [ $? -ge 3 ]; then
  echo "High or critical issues found"
fi
```

### Git hooks

| Code | Meaning |
|:----:|---------|
| `0` | Allow the git operation |
| `1` | Block the git operation |

### General errors

| Code | Meaning |
|:----:|---------|
| `1` | Command error (authentication failure, invalid arguments, etc.) |

## Next steps

- **[Quickstart](/code-reviews/cli/quickstart/)**: Get started in under 2 minutes.
- **[Review commands](/code-reviews/cli/review-commands/)**: Detailed usage and examples.
- **[Git hooks](/code-reviews/cli/git-hooks/)**: Automate reviews in your workflow.
