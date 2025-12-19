---
title: Instant IDE Mode
description: Review code directly from your IDE without AI assistance. Right-click, use shortcuts, or click sidebar buttons for instant feedback.
---

# Instant IDE Mode

Instant IDE Mode gives you direct access to kluster.ai code reviews through your IDE interface. No AI assistant needed—just select code and get instant feedback.

## How Instant IDE Mode works

Review code on demand using your IDE's native interface:

1. **Select or open code**: Highlight a block or open a file
2. **Trigger review**: Right-click, use a shortcut, or click a sidebar button
3. **View results**: See issues with explanations and fix suggestions
4. **Apply fixes**: Click "Fix with AI" or fix manually

## Three ways to trigger reviews

<div class="grid cards" markdown>

-   :material-mouse: **Right-Click Menu**

    ---

    Select any code in your editor, right-click, and choose **Review with kluster.ai**.

    Best for reviewing specific functions or code blocks.

-   :material-keyboard: **Keyboard Shortcut**

    ---

    Press `Ctrl+Shift+K` (or `Cmd+Shift+K` on Mac) to instantly review selected code.

    Best for quick reviews while actively coding.

-   :material-dock-left: **Extension Sidebar**

    ---

    Open the kluster.ai extension and click **Instant Review** to review the current file or all uncommitted changes.

    Best for reviewing entire files or pre-commit checks.

</div>

## Supported IDEs

Instant IDE Mode is available in kluster.ai IDE extensions:

| IDE | Right-Click | Shortcut | Sidebar |
|-----|-------------|----------|---------|
| VS Code | Yes | Yes | Yes |
| Cursor | Yes | Yes | Yes |
| Windsurf | Yes | Yes | Yes |
| Antigravity | Yes | Yes | Yes |

!!! warning "CLI tools not supported"
    Instant IDE Mode is not available for CLI tools (Claude Code, Codex CLI). Use [Agent Mode](/code-reviews/agent-mode/) instead.

## Quick start

### Prerequisites

--8<-- 'text/quickstart-prerequisites.md'

### Try it now

=== "Right-Click Review"

    1. Select a block of code in your editor
    2. Right-click to open the context menu
    3. Click **Review with kluster.ai**
    4. View results in the sidebar panel

=== "Keyboard Shortcut"

    1. Select a block of code in your editor
    2. Press `Ctrl+Shift+K` (Windows/Linux) or `Cmd+Shift+K` (Mac)
    3. View results in the sidebar panel

=== "Sidebar Review"

    1. Open the kluster.ai extension in your sidebar
    2. Click the **Instant Review** dropdown
    3. Choose:
        - **Review current file**: Reviews only the open file
        - **Review uncommitted changes**: Reviews all uncommitted changes
    4. View results in the panel

## What you can review

| Review Type | How to Access | Scope |
|-------------|---------------|-------|
| **Code block** | Select + right-click or shortcut | Selected code only |
| **Current file** | Sidebar → Instant Review → Current file | Entire open file |
| **Uncommitted changes** | Sidebar → Instant Review → Uncommitted | All staged and unstaged changes |

## Applying fixes

After a review completes, you'll see any issues found with suggested fixes. You have two options:

1. **Fix with AI**: Click the button to have an AI assistant apply the fix automatically
2. **Fix manually**: Review the suggestion and make the change yourself

![Review results showing issues found](/images/code-reviews/quick-start/manual-review-this-code-extension-results.webp)

## When to use Instant IDE Mode

| Scenario | Recommended action |
|----------|-------------------|
| Writing code without AI | Use right-click or shortcut as you go |
| Reviewing a specific function | Select the function → `Ctrl+Shift+K` |
| Before committing | Sidebar → Review uncommitted changes |
| Merge conflict resolution | Select resolved code → right-click review |
| Quick security check | Select sensitive code → review |

## Comparison with Agent Mode

| Aspect | Instant IDE Mode | Agent Mode |
|--------|------------------|------------|
| **Trigger** | You click/shortcut | Automatic or AI prompt |
| **AI required** | No | Yes |
| **Best for** | Manual coding | AI-assisted coding |
| **CLI support** | No | Yes |
| **Uncommitted changes** | Yes (sidebar) | Via AI prompt |

## Next steps

- **[Instant Actions Quickstart](/code-reviews/instant-ide-mode/instant-actions/)**: Detailed walkthrough of all instant actions
- **[Configuration](/code-reviews/configuration/options/)**: Customize review sensitivity
- **[Agent Mode](/code-reviews/agent-mode/)**: Learn about AI-assisted reviews
