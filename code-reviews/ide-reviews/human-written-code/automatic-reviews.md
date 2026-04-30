---
title: Automatic reviews for human-written code
description: Enable automatic reviews to scan uncommitted changes after you stop typing. Learn how kluster.ai detects idle time and surfaces results.
categories: Basics, IDE Reviews
---

# Automatic reviews

Automatic reviews watch your uncommitted changes and run in the background. You do not need to click anything.

!!! tip "Exclude files with .klusterignore"
    Add a [`.klusterignore`](/code-reviews/configuration/klusterignore/) file to exclude files and folders from automatic reviews (syntax is the same as `.gitignore`).

## Prerequisites

--8<-- 'text/quickstart-prerequisites.md'

## Turn it on

1.  Open [Options](/code-reviews/configuration/options/) in the kluster.ai platform or IDE.
2.  In **Enabled Tools**, toggle **Ambient Background Reviews (Beta, Enterprise plan)** on.
3.  Keep coding. Reviews run automatically once enabled.

!!! note
    Automatic reviews appear as **Ambient Background Reviews** in the platform UI.

![Background reviews enabled in Options](/images/code-reviews/ide-reviews/human-written-code/background-reviews/background-reviews.webp)

## How it works

Automatic reviews run in the background while you code. The extension periodically checks your diff and resets an idle timer each time it changes. When the timer runs out, [kluster.ai](https://www.kluster.ai/){target=\_blank} scans your uncommitted changes and notifies you only if it finds issues.

## What gets reviewed

Automatic reviews include staged, unstaged, untracked, and unsaved editor changes—basically everything that would show up in `git status` plus your current unsaved work.

Only text files are reviewed. Binary files and common generated files (like `node_modules` or build outputs) are filtered out automatically.

!!! note "Large changesets"
    If your changes are very large, the review may skip context or fail. Use [on-demand reviews](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/) to review smaller chunks instead.

## Where results appear

Results show up in three places:

- **Inline comments**: Collapsed by default, expand to see details.
- **Gutter icons**: Visual markers next to flagged lines.
- **Problems panel**: All issues listed in one place.

Automatic review results are appended to any existing on-demand review results—they don't replace them.

## Branch switching

When you switch git branches, kluster.ai resets its tracking state. This prevents stale results from a previous branch showing up in your current work.

## Compatible with

--8<-- 'text/code-reviews/compatible-ides-extensions.md'

## Next steps

- **[On-demand reviews](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/)**: Run reviews manually in your editor.
- **[Configuration options](/code-reviews/configuration/options/)**: Adjust sensitivity and issue types.
