---
title: Background Auto Reviews - How It Works
description: Understand when background reviews trigger, what changes are included, and how results appear in your IDE.
categories: Human-written code, Automatic review
---

# Background reviews: how it works

Background reviews run in the background while you code. The extension periodically checks your diff and resets an idle timer each time it changes. When the timer runs out, [kluster.ai](https://kluster.ai){target=_blank} scans your uncommitted changes and notifies you only if it finds issues.

## What gets reviewed

Background reviews include staged, unstaged, untracked, and unsaved editor changes—basically everything that would show up in `git status` plus your current unsaved work.

Only text files are reviewed. Binary files and common generated files (like `node_modules` or build outputs) are filtered out automatically.

!!! note "Large changesets"
    If your changes are very large, the review may skip context or fail. Use [on-demand reviews](/code-reviews/human-written-code/on-demand-reviews/quickstart/) to review smaller chunks instead.

## Where results appear

Results show up in three places:

- **Inline comments**: Collapsed by default, expand to see details.
- **Gutter icons**: Visual markers next to flagged lines.
- **Problems panel**: All issues listed in one place.

Background review results are appended to any existing on-demand reviews results—they don't replace them.

## Branch switching

When you switch git branches, kluster.ai resets its tracking state. This prevents stale results from a previous branch showing up in your current work.
