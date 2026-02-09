---
title: CLI Reference
description: Learn about all kluster-cli commands, flags, exit codes, severity levels, and issue types in one place.
categories: CLI, Reference
---

# CLI reference

## Quick reference

```
# Authentication
kluster login                           # Authenticate with API key
kluster logout                          # Remove stored credentials

# Code review
kluster review staged                   # Review staged changes
kluster review staged --mode deep       # Deep analysis
kluster review diff main                # Review diff against branch
kluster review diff HEAD~3..HEAD        # Review commit range
kluster review file src/app.go          # Review specific file(s)

# History
kluster log                             # List recent reviews
kluster log --limit 5                   # Limit results
kluster show <review-id>                # View review details

# Git hooks
kluster hooks install pre-push          # Install a hook
kluster hooks install all               # Install all hooks
kluster hooks install pre-push --block-on critical
kluster hooks install pre-push --warn-only
kluster hooks uninstall all             # Remove all hooks
kluster hooks status                    # Show hook status

# Utility
kluster version                         # Print version info
kluster update                          # Update to latest version
kluster update --check                  # Check for updates
kluster completion bash                 # Generate shell completions
```

## Commands

### Authentication

| Command | Description |
|---------|-------------|
| `kluster login` | Authenticate with your kluster.ai API key |
| `kluster login --api-key <key>` | Authenticate with key directly (non-interactive) |
| `kluster logout` | Remove stored credentials |

### Review

| Command | Description |
|---------|-------------|
| `kluster review staged` | Review staged git changes |
| `kluster review diff <target>` | Review diff against branch or commit range |
| `kluster review file <path> [paths...]` | Review one or more files |

**Review flags:**

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--mode` | `instant`, `deep` | `instant` | Analysis depth |

### History

| Command | Description |
|---------|-------------|
| `kluster log` | List recent reviews |
| `kluster show <review-id>` | Show full review details |

**Log flags:**

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--limit` | `1`–`100` | `20` | Maximum reviews to display |

### Git hooks

| Command | Description |
|---------|-------------|
| `kluster hooks install <hook>` | Install a git hook |
| `kluster hooks uninstall <hook>` | Remove a git hook |
| `kluster hooks status` | Show installed hooks |

Hook values: `pre-commit`, `pre-push`, `all`

**Install flags:**

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--block-on` | `critical`, `high`, `medium`, `low` | `high` | Minimum severity to block |
| `--warn-only` | — | `false` | Show issues but don't block |
| `--force` | — | `false` | Overwrite existing hook |

### Utility

| Command | Description |
|---------|-------------|
| `kluster version` | Print version, commit, build date, platform |
| `kluster update` | Download and install the latest version |
| `kluster update --check` | Check for updates without installing |
| `kluster completion <shell>` | Generate shell completion script |

Shell values: `bash`, `zsh`, `fish`, `powershell`

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

## Severity levels

| Level | Color | Priority range | Action |
|-------|-------|:--------------:|--------|
| `critical` | Bold red | P0–P2 | Fix immediately |
| `high` | Red | P3 | Fix before merging |
| `medium` | Yellow | P4 | Should fix |
| `low` | Cyan | P5 | Optional improvement |

## Issue types

| Type | Description | Example |
|------|-------------|---------|
| `intent` | Code doesn't match the original request | Asked for sorting, got filtering |
| `semantic` | Meaning and type errors | Wrong variable type used |
| `logical` | Control flow errors | Off-by-one, wrong conditions |
| `security` | Security vulnerabilities | SQL injection, XSS |
| `knowledge` | Best practice violations | Not following conventions |
| `performance` | Performance issues | N+1 queries, inefficient loops |
| `quality` | Code quality problems | High complexity, poor naming |

## Environment variables

| Variable | Description |
|----------|-------------|
| `KLUSTER_API_KEY` | API authentication key |
| `KLUSTER_API_URL` | API endpoint (default: `https://api.kluster.ai`) |
| `KLUSTER_OUTPUT` | Default output format (`table`, `json`, `text`) |
| `PAGER` | System pager for long output (`less`, `more`, `most`) |

See [Configuration](/code-reviews/cli/configuration/) for details on config file and precedence.

## Supported platforms

| OS | Architectures | Installer |
|----|---------------|-----------|
| Linux | amd64, arm64 | `curl ... \| sh` |
| macOS | amd64 (Intel), arm64 (Apple Silicon) | `curl ... \| sh` |
| Windows | amd64, arm64 | `irm ... \| iex` |

## Next steps

- **[Quickstart](/code-reviews/cli/quickstart/)**: Get started in under 2 minutes.
- **[Review commands](/code-reviews/cli/review-commands/)**: Detailed usage and examples.
- **[Git hooks](/code-reviews/cli/git-hooks/)**: Automate reviews in your workflow.
