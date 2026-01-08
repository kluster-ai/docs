---
title: Background Auto Reviews: How It Works
description: Understand when background reviews trigger, what changes are included, and how results appear in your IDE.
---

# Background auto reviews: how it works

Background auto reviews keep a lightweight watch on your workspace and submit a review only after you stop making changes for a short time.

## Change detection and idle timer

- The extension checks your current diff about every 10 seconds.
- If the diff changes, the idle timer resets.
- A review starts after a short idle period (default about 2 minutes, set by your config).

## What counts as changes

- Staged, unstaged, untracked, and unsaved editor changes are included.
- Only text files are reviewed. Common non-code and generated files are filtered out.
- If your changes are very large, the review may skip context or fail. Use Instant Actions to review smaller chunks.

## Review lifecycle

- Only one background review runs at a time.
- The last reviewed diff is tracked, so unchanged patches are not re-reviewed.
- Switching git branches resets the state to avoid stale results.

## Results and notifications

- If no issues are found, there is no notification.
- If issues are found, a warning notification appears and lets you open the results.
- Results show as inline comments (collapsed by default), gutter icons, and entries in the Problems panel.
- Auto review results are appended to existing Instant Actions results instead of replacing them.

## If you are not seeing reviews

- Confirm you are signed in and **Ambient Background Reviews (Beta, Enterprise plan)** is enabled.
- Make sure you have uncommitted changes in a git repo and then pause for a short time.
- If a review is already running, it will finish before a new one starts.
