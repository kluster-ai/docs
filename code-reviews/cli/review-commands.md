---
title: Review Commands
description: Learn how to review staged changes, diffs, branches, and individual files with kluster-cli. Choose between instant and deep analysis modes.
categories: CLI, Review
---

# Review commands

kluster-cli provides three ways to review code, each suited to a different stage of your workflow.

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

## Analysis modes

All review commands support two analysis modes via the `--mode` flag:

--8<-- 'text/code-reviews/instant-vs-deep.md'

Use the `--mode` flag to select:

```bash
kluster review staged --mode deep
```

--8<-- 'code/code-reviews/cli/review-deep.md'

The default mode is `instant`.

## Understanding the output

Every review starts with a progress bar and completion message, followed by the review ID and issue count:

```
→ Reviewing code [████████████████████████████████████████] 100%
✓ Reviewing code complete!

Review: 507f1f77bcf86cd799439011

Found 2 issue(s)
```

Each issue includes:

- **Severity and priority**: `#1 CRITICAL [P0] security` — issue number, severity level, priority, and type.
- **Description**: A summary of the problem.
- **Location**: File path and line range (`at src/db/queries.go:45-52`).
- **More details**: Extended explanation of why this is a problem.
- **Fix**: Suggested fix or remediation steps.

Issues are separated by a horizontal line (`────────────`). When no issues are found, the output shows:

```
✓ Code review complete - no issues found!
```

### Issue types

| Type | Description |
|------|-------------|
| `intent` | Code doesn't match the original request |
| `semantic` | Meaning and type errors |
| `logical` | Control flow errors (off-by-one, wrong conditions) |
| `security` | Security vulnerabilities |
| `knowledge` | Best practice violations |
| `performance` | Performance issues |
| `quality` | Code quality problems |

### Severity levels

| Level | Meaning | Exit code |
|-------|---------|:---------:|
| `critical` | Security vulnerability or breaking issue | 4 |
| `high` | Significant bug or security concern | 3 |
| `medium` | Quality issue or minor bug | 2 |
| `low` | Style or minor improvement | 1 |

When no issues are found, the exit code is `0`. See [Reference](/code-reviews/cli/reference/) for the full exit code table.

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
- **[Configuration](/code-reviews/cli/configuration/)**: Customize output format, API endpoint, and more.
- **[Reference](/code-reviews/cli/reference/)**: Full command reference with all flags and exit codes.
