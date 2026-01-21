---
title: On-demand reviews quickstart
description: Write code, verify on your terms. Three ways to trigger reviews in your IDE—right-click any selection, use hint buttons, or scan uncommitted changes before you commit.
---

# On-demand reviews quickstart

With [kluster.ai](https://kluster.ai){target=_blank}, you can trigger reviews three ways: right-click any selection, use hint buttons, or scan uncommitted changes.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/quickstart-prerequisites.md'

<div class="embed-container">
    <iframe
        src="https://www.youtube.com/embed/rpWt9sXAqWY"
        title="Human-written code reviews with kluster.ai"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
    </iframe>
</div>

## How on-demand reviews work

1.  **You write code**: Work in your editor as usual.
2.  **You trigger review**: Right-click, use a hint button, or click in the sidebar.
3.  **kluster.ai analyzes**: Results appear with issues and suggested fixes.

## Instant review

Open the kluster.ai extension to access the **Instant Review** section in the sidebar. Click the dropdown button to choose:

- **Review current file**: Verifies only the file currently open in the editor.
- **Review uncommitted changes**: Verifies all uncommitted changes across multiple files.

![Instant Review section in the kluster.ai sidebar](/images/code-reviews/human-written-code/on-demand-reviews/manual-review-this-code-extension.webp)

!!! info "Accessing Instant Review"
    You can also access Instant Review from the **Home** and **Git** tabs. Expand the kluster.ai section if collapsed.

After the review completes, kluster.ai displays any issues found. You can click **Fix with AI** to automatically resolve them.

![Review results showing issues found](/images/code-reviews/human-written-code/on-demand-reviews/manual-review-this-code-extension-results.webp)

## Code block review

Select any code in your editor, right-click, and choose **Review with kluster.ai** (or press `Ctrl+Shift+K`). This is useful for:

- Verifying a specific function or block you just wrote.
- Checking code during merge conflict resolution.
- Getting a quick security check before moving on.

![Right-click to review selected code](/images/code-reviews/human-written-code/on-demand-reviews/manual-review-this-code.webp)

!!! info "Hint button"
    When you select code, a hint button also appears next to your selection to trigger the review. This hint button is not yet available in Cursor—use the right-click menu or keyboard shortcut instead.

## Compatible with

- Cursor
- VS Code
- Windsurf
- Antigravity

## Configuration

You can customize how on-demand reviews work in your [configuration options](/code-reviews/configuration/options/):

- **Enabled tools**: Toggle Code Review and Dependency Analysis on/off.
- **Sensitivity**: Adjust how strictly issues are flagged (Low → Critical).
- **Bug check types**: Select which issue types to check (Security, Logic, Performance, etc.).

## Next steps

- **[MCP Tools Reference](/code-reviews/reference/mcp-tools/)**: Deep dive into all MCP tools and parameters.
- **[Configuration Options](/code-reviews/configuration/options/)**: Customize Code Reviews behavior for your workflow.
