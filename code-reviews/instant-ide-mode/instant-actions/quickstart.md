---
title: Quickstart
description: Learn how to trigger manual code reviews directly in your IDE using right-click menus, keyboard shortcuts, and the sidebar.
---

# Quickstart

When you write code directly in your editor and want to verify it on your own terms, Code Reviews provides three manual options in your IDE.

## Code block review

Select any code in your editor, right-click, and choose **Review with kluster.ai** (or press `Ctrl+Shift+K`). This is useful for:

- Verifying a specific function or block you just wrote
- Checking code during merge conflict resolution
- Getting a quick security check before moving on

![Right-click to review selected code](/images/code-reviews/quick-start/manual-review-this-code.webp)

!!! info "Hint button"
    When you select code, a hint button also appears next to your selection to trigger the review. This hint button is not yet available in Cursor—use the right-click menu or keyboard shortcut instead.

## Instant review

Open the kluster.ai extension to access the **Instant Review** section in the sidebar. Click the dropdown button to choose:

- **Review current file** - Verifies only the file currently open in the editor
- **Review uncommitted changes** - Verifies all uncommitted changes across multiple files

![Instant Review section in the kluster.ai sidebar](/images/code-reviews/quick-start/manual-review-this-code-extension.webp)

!!! info "Accessing Instant Review"
    You can also access Instant Review from the **Home** and **Git** tabs. Expand the kluster.ai section if collapsed.

After the review completes, kluster.ai displays any issues found. You can click **Fix with AI** to automatically resolve them.

![Review results showing issues found](/images/code-reviews/quick-start/manual-review-this-code-extension-results.webp)

## Next steps

- **[MCP Tools Reference](/code-reviews/reference/mcp-tools/)** - Deep dive into all MCP tools and parameters
- **[Configuration Options](/code-reviews/configuration/options/)** - Customize Code Reviews behavior for your workflow
