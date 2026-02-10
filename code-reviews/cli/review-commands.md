---
title: Review Commands
description: Review staged changes, diffs, branches, and individual files with kluster-cli. Choose between instant and deep analysis modes.
categories: CLI, Review
---

# Review commands

[kluster.ai](https://kluster.ai){target=_blank}'s CLI provides three ways to review code from the terminal — staged changes, diffs against branches or commits, and individual files — each suited to a different stage of your workflow. All commands support instant and deep analysis modes.

| Command | What it reviews | Requires git? |
|---------|----------------|:-------------:|
| `kluster review staged` | Staged changes (`git add`) | Yes |
| `kluster review diff <target>` | Diff against a branch or commit range | Yes |
| `kluster review file <path>` | One or more files | No |

## Review staged changes

Review everything you have staged before committing:

```bash
kluster review staged
```

--8<-- 'code/code-reviews/cli/review-staged-example.md'

!!! info "No staged changes?"
    If nothing is staged, the CLI will prompt you to `git add` files first.

## Review a diff

Compare your current work against a branch or between commits:

**Against a branch:**

```bash
kluster review diff main
```

--8<-- 'code/code-reviews/cli/review-diff-branch.md'

**Between commits:**

```bash
kluster review diff HEAD~3..HEAD
```

--8<-- 'code/code-reviews/cli/review-diff-range.md'

Shell completions autocomplete branch names when available. See [Installation](/code-reviews/cli/installation/#shell-completions) to set this up.

## Review files

Review specific files without needing a git repository:

```bash
kluster review file src/auth.go src/middleware.go
```

--8<-- 'code/code-reviews/cli/review-file.md'

This is useful for reviewing standalone scripts, config files, or code outside a git repository.

!!! tip "Exclude files with .klusterignore"
    If your repository contains folders you want to exclude from review (for example `dist/`, `vendor/`, or generated files), add them to a [`.klusterignore`](/code-reviews/configuration/klusterignore/) file. CLI review commands respect `.klusterignore`.

## Analysis modes

All review commands support two analysis modes via the `--mode` flag:

--8<-- 'text/code-reviews/instant-vs-deep.md'

Use the `--mode` flag to select:

```bash
kluster review staged --mode deep
```

--8<-- 'code/code-reviews/cli/review-deep.md'

The default mode is `instant`.

## CI/CD and scripting

For automation, prefer machine-readable output and check the command exit code.

Example (JSON output via environment variable):

```bash
KLUSTER_OUTPUT=json kluster review staged
```

See [CLI reference](/code-reviews/cli/reference/#exit-codes) for exit codes and [Output formats](/code-reviews/cli/reference/#output-formats) for configuration options.

## Review history

### List recent reviews

```bash
kluster log
```

--8<-- 'code/code-reviews/cli/log-output.md'

Use `--limit` to control how many reviews are shown (default: 20, max: 100):

```bash
kluster log --limit 5
```

### View review details

Use the review ID from `kluster log` to see the full report:

```bash
kluster show <review-id>
```

--8<-- 'code/code-reviews/cli/show-output.md'

Long output is automatically paged using your system pager (`less`, `more`, or `most`).

## Next steps

- **[Git hooks](/code-reviews/cli/git-hooks/)**: Automate reviews on every commit or push.
- **[Reference](/code-reviews/cli/reference/)**: Configuration, exit codes, and full command reference.
