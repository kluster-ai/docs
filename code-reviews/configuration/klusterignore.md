---
title: .klusterignore
description: Exclude files and folders from kluster.ai Code Reviews with a .gitignore-compatible .klusterignore file, using patterns, wildcards, and negation.
categories: Basics, Configuration
---

# .klusterignore

Use a `.klusterignore` file to exclude files and folders from **kluster.ai Code Reviews**.

The syntax and matching behavior are intentionally the same as `.gitignore` (patterns, wildcards, negation rules, and comments).

!!! info "Already respects .gitignore"
    If your repository contains a `.gitignore`, kluster.ai automatically excludes anything ignored by git.
    Use `.klusterignore` to add review-specific exclusions (or to keep your review scope strict even when your `.gitignore` is minimal).

## Supported workflows

`.klusterignore` is currently available on:

| Tool | Workflow | Reference |
|---|---|---|
| IDE | On-demand reviews (human-written code) | [On-demand reviews quickstart](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/quickstart/) |
| IDE | Background reviews (human-written code) | [Background reviews quickstart](/code-reviews/ide-reviews/human-written-code/automatic-background-reviews/quickstart/) |
| CLI | kluster.ai CLI | [Review commands](/code-reviews/cli/review-commands/) |

!!! note "Not yet supported"
    `.klusterignore` is currently **not** applied to AI assistant-triggered automatic reviews (the "AI-generated code" automatic review flow) or AI agent reviews (for example, reviews triggered by an AI assistant tool call).

## Quickstart

1. Create a file named `.klusterignore` in the **root of your repository**.
2. Add ignore patterns for paths you never want to send for review.

Example:

```gitignore
# Dependencies
node_modules/
vendor/

# Build output
dist/
build/

# Local config and secrets
.env
*.pem

# Logs
*.log

# Re-include one file
!.gitkeep
```

## Syntax

Most teams can copy patterns directly from their `.gitignore`.

Common rules:

- Blank lines are ignored.
- Lines starting with `#` are comments.
- `*`, `?`, and `[]` work as wildcards.
- `**` can match across directory boundaries.
- A trailing `/` matches directories.
- A leading `/` anchors the pattern to the repository root.
- Prefix a pattern with `!` to re-include paths previously excluded.
- If multiple patterns match a path, the **last matching rule wins** (same as `.gitignore`).

## How it affects reviews

When a file matches `.klusterignore`, it is excluded from the review input:

- Excluded files are not reviewed, even if they are staged or part of a diff.
- Excluding a directory excludes everything under it (unless you re-include specific files with `!`).

## Next steps

- **[On-demand reviews quickstart](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/quickstart/)**: Run manual reviews in your IDE and verify changes on your terms.
- **[Background reviews quickstart](/code-reviews/ide-reviews/human-written-code/automatic-background-reviews/quickstart/)**: Enable automatic reviews that trigger after you stop typing.
- **[Review commands (CLI)](/code-reviews/cli/review-commands/)**: Review staged changes, diffs, or specific files from the terminal.

## Troubleshooting

- If something is still being reviewed, double-check that your pattern matches the path **relative to the repository root**.
- If you use negation (`!`), ensure the re-include pattern appears **after** the exclude rule.
