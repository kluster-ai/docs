---
title: Instant Actions
description: Review code instantly from your IDE with right-click, keyboard shortcuts, or sidebar buttons. No AI assistant required.
---

# Instant Actions

Instant actions let you trigger code reviews directly from your IDE interface. Select code, click a button, or use a keyboard shortcut—get results in seconds.

## Three ways to review

### 1. Right-click menu

The most intuitive way to review code:

1. Select any code in your editor
2. Right-click to open the context menu
3. Click **Review with kluster.ai**
4. View results in the sidebar panel

![Right-click to review selected code](/images/code-reviews/quick-start/manual-review-this-code.webp)

!!! tip "Best for"
    Reviewing specific functions, classes, or code blocks you're working on.

### 2. Keyboard shortcut

The fastest way to review code:

| Platform | Shortcut |
|----------|----------|
| Windows/Linux | `Ctrl+Shift+K` |
| Mac | `Cmd+Shift+K` |

1. Select the code you want to review
2. Press the shortcut
3. View results in the sidebar panel

!!! tip "Best for"
    Quick reviews while actively coding. Muscle memory makes this very fast.

### 3. Extension sidebar

The most comprehensive option:

1. Open the kluster.ai extension in your sidebar
2. Navigate to the **Instant Review** section
3. Click the dropdown and choose:
   - **Review current file**: Analyzes the entire open file
   - **Review uncommitted changes**: Analyzes all staged and unstaged changes

![Instant Review section in the kluster.ai sidebar](/images/code-reviews/quick-start/manual-review-this-code-extension.webp)

!!! tip "Best for"
    Pre-commit reviews, reviewing entire files, or auditing all recent changes.

!!! info "Accessing Instant Review"
    You can also access Instant Review from the **Home** and **Git** tabs. Expand the kluster.ai section if collapsed.

## Review results

After triggering a review, kluster.ai displays:

- **Issue count**: Total issues found by severity
- **Issue list**: Each issue with:
  - Type (Security, Logical, etc.)
  - Severity (Critical, High, Medium, Low)
  - Description of the problem
  - Suggested fix
- **Fix button**: Click "Fix with AI" to apply fixes automatically

![Review results showing issues found](/images/code-reviews/quick-start/manual-review-this-code-extension-results.webp)

## Quick reference

| Action | Method | Scope |
|--------|--------|-------|
| Review selection | Right-click or `Ctrl+Shift+K` | Selected code only |
| Review current file | Sidebar → Current file | Entire open file |
| Review uncommitted | Sidebar → Uncommitted changes | All git changes |

## Common use cases

### Before committing
```
1. Open kluster.ai sidebar
2. Click Instant Review → Review uncommitted changes
3. Review and fix any issues
4. Commit with confidence
```

### Reviewing a specific function
```
1. Select the function code
2. Press Ctrl+Shift+K
3. Review results
4. Click "Fix with AI" or fix manually
```

### During code review
```
1. Open the file being reviewed
2. Select suspicious code blocks
3. Right-click → Review with kluster.ai
4. Get automated analysis to support your review
```

### Merge conflict resolution
```
1. Resolve the merge conflict
2. Select the resolved code
3. Right-click → Review with kluster.ai
4. Verify the resolution doesn't introduce issues
```

## Supported IDEs

| IDE | Right-Click | Shortcut | Sidebar |
|-----|-------------|----------|---------|
| VS Code | Yes | `Ctrl+Shift+K` | Yes |
| Cursor | Yes | `Ctrl+Shift+K` | Yes |
| Windsurf | Yes | `Ctrl+Shift+K` | Yes |
| Antigravity | Yes | `Ctrl+Shift+K` | Yes |

!!! info "Hint button"
    In VS Code, Windsurf, and Antigravity, a hint button appears next to selected code for quick access. This feature is not yet available in Cursor—use the right-click menu or keyboard shortcut instead.

## Next steps

- **[Configuration](/code-reviews/configuration/options/)**: Customize sensitivity and issue types
- **[Agent Mode](/code-reviews/agent-mode/)**: Learn about AI-assisted automatic reviews
- **[FAQ](/code-reviews/faq/)**: Common questions about instant actions
