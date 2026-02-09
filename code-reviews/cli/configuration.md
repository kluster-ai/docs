---
title: CLI Configuration
description: Learn how to configure kluster-cli with config files and environment variables. Set output format, API endpoint, and authentication options.
categories: CLI, Configuration
---

# Configuration

kluster-cli uses a YAML config file with optional environment variable overrides. Configure output format, API endpoint, and authentication. Environment variables and command-line flags take precedence over the config file.

## Config file

The config file is created automatically on first use:

| OS | Location |
|----|----------|
| macOS / Linux | `~/.kluster/cli/config.yaml` |
| Windows | `%USERPROFILE%\.kluster\cli\config.yaml` |

### Available settings

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

## Environment variables

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

## Output formats

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

## Configuration priority

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

## Next steps

- **[Review commands](/code-reviews/cli/review-commands/)**: Run reviews with different modes and formats.
- **[Git hooks](/code-reviews/cli/git-hooks/)**: Automate reviews in your git workflow.
- **[Reference](/code-reviews/cli/reference/)**: Full command reference with all flags.
