---
title: Git Hooks
description: Learn how to automate kluster.ai code reviews with git hooks. Install pre-commit or pre-push hooks to catch issues before they reach your repository.
categories: CLI, Git, Automation
---

# Git hooks

Git hooks let you run kluster.ai reviews automatically as part of your git workflow. Issues are caught before code is committed or pushed, without any manual step.

## Hook types

| Hook | When it runs | What it reviews |
|------|-------------|-----------------|
| `pre-commit` | Before each `git commit` | Staged changes |
| `pre-push` | Before each `git push` | Commits being pushed |

**Which one should I use?**

- Use **pre-commit** for fast feedback on every commit. Best for individual workflows.
- Use **pre-push** to review the full set of changes before they leave your machine. Best for team workflows.
- Use **both** for maximum coverage.

## Install hooks

Install a single hook:

```bash
kluster hooks install pre-push
```

--8<-- 'code/code-reviews/cli/hooks-install.md'

Or install all hooks at once:

```bash
kluster hooks install all
```

--8<-- 'code/code-reviews/cli/hooks-install-all.md'

!!! info "Existing hooks"
    If a hook file already exists, the CLI will warn you. Use `--force` to overwrite it.

## Configure blocking severity

By default, hooks block on `high` severity or above. Use `--block-on` to change the threshold:

```bash
kluster hooks install pre-push --block-on critical
```

| Threshold | Blocks on |
|-----------|-----------|
| `critical` | Critical issues only |
| `high` (default) | High and critical issues |
| `medium` | Medium, high, and critical issues |
| `low` | Any issue blocks |

### Warn-only mode

To show review results without blocking, use `--warn-only`:

```bash
kluster hooks install pre-push --warn-only
```

In this mode, the review runs and displays any issues found, but the git operation always proceeds.

## How hooks work

When a hook triggers, the CLI runs a review and checks the results against your severity threshold.

**If issues meet the threshold — the operation is blocked:**

--8<-- 'code/code-reviews/cli/hooks-triggered-block.md'

**If no issues meet the threshold — the operation proceeds:**

--8<-- 'code/code-reviews/cli/hooks-triggered-pass.md'

### Pre-push details

The pre-push hook:

1. Reads the commits being pushed.
2. Skips branch deletions.
3. For new branches, finds the merge base against the default branch.
4. Gets the diff between commits.
5. Runs the review and checks the severity threshold.

### Pre-commit details

The pre-commit hook:

1. Checks for staged changes.
2. Gets the staged diff.
3. Runs the review and checks the severity threshold.

## Check hook status

See which hooks are installed:

```bash
kluster hooks status
```

--8<-- 'code/code-reviews/cli/hooks-status.md'

## Bypass hooks

In an emergency, you can skip hooks with git's `--no-verify` flag:

```bash
git commit --no-verify -m "hotfix: urgent production fix"
git push --no-verify
```

!!! note "Use sparingly"
    Bypassing hooks skips the code review entirely. Reserve this for urgent hotfixes and follow up with a manual review.

## Uninstall hooks

Remove hooks when no longer needed:

```bash
kluster hooks uninstall all
```

--8<-- 'code/code-reviews/cli/hooks-uninstall.md'

You can also uninstall a specific hook:

```bash
kluster hooks uninstall pre-commit
```

The CLI only removes hooks it installed (identified by the `KLUSTER_HOOK_START` marker). Other hooks are left untouched.

## Custom hook paths

The CLI respects git's `core.hooksPath` configuration. If you use a custom hooks directory:

```bash
git config core.hooksPath .githooks
kluster hooks install pre-push
# Hook is installed at .githooks/pre-push
```

If `core.hooksPath` is not set, hooks are installed in `.git/hooks/`.

## Next steps

- **[Review commands](/code-reviews/cli/review-commands/)**: Run reviews manually when you need them.
- **[Configuration](/code-reviews/cli/configuration/)**: Customize CLI behavior and output.
- **[Reference](/code-reviews/cli/reference/)**: Exit codes and full command reference.
