---
title: Pick Your Workflow
description: Choose between Agent Mode and Instant IDE Mode based on how you write code. Or use both.
---

# Pick Your Workflow

kluster.ai Code Reviews offers two modes designed for different workflows. This guide helps you choose the right one—or use both.

## Quick decision guide

```
Do you use AI coding assistants?
│
├─ YES → Use Agent Mode
│        (Reviews happen automatically as AI generates code)
│
└─ NO  → Use Instant IDE Mode
         (Review code with right-click or keyboard shortcut)

Using both AI and manual coding?
→ Use both modes! They complement each other.
```

## Agent Mode

**Best for**: Developers using AI coding assistants

Agent Mode integrates with your AI assistant to review code as it's generated. No manual intervention needed—issues are caught and fixed in real-time.

### How it works

1. You prompt your AI assistant (e.g., "Create a user login endpoint")
2. The AI generates code
3. kluster.ai automatically reviews the code
4. Issues are flagged and fixed before you continue

### Two types of agent reviews

| Type | Trigger | Use case |
|------|---------|----------|
| **Automatic** | AI generates/modifies code | Continuous protection while coding |
| **Manual** | You ask the AI to review | Audit existing files on demand |

### Supported tools

- **IDE extensions**: Cursor, VS Code, Windsurf, Antigravity
- **CLI tools**: Claude Code, Codex CLI

[:octicons-arrow-right-24: Set up Agent Mode](/code-reviews/agent-mode/)

---

## Instant IDE Mode

**Best for**: Developers who write code directly without AI assistance

Instant IDE Mode provides on-demand reviews through your IDE interface. Select code, right-click, and get instant feedback.

### How it works

1. Write or select code in your editor
2. Trigger a review (right-click, shortcut, or sidebar button)
3. View issues and apply fixes

### Three ways to trigger reviews

| Method | Action | Best for |
|--------|--------|----------|
| **Right-click** | Select code → Right-click → "Review with kluster.ai" | Reviewing specific functions |
| **Keyboard shortcut** | `Ctrl+Shift+K` | Quick reviews while coding |
| **Extension sidebar** | Click "Instant Review" button | Reviewing files or uncommitted changes |

### Supported IDEs

- Cursor, VS Code, Windsurf, Antigravity

!!! info "CLI tools"
    Instant IDE Mode is not available for CLI tools (Claude Code, Codex CLI). Use Agent Mode instead.

[:octicons-arrow-right-24: Set up Instant IDE Mode](/code-reviews/instant-ide-mode/)

---

## Using both modes

Most developers benefit from using both modes:

- **Agent Mode** catches issues automatically during AI-assisted coding sessions
- **Instant IDE Mode** provides quick checks when you're writing code manually

The modes don't conflict—they complement each other. Install kluster.ai once and both modes are available.

### Example workflow

1. Morning: Use **Agent Mode** while pair-programming with Claude Code
2. Afternoon: Use **Instant IDE Mode** to review code you wrote manually
3. Before commit: Use **Instant IDE Mode** → "Review uncommitted changes" to catch anything missed

## Comparison table

| Feature | Agent Mode | Instant IDE Mode |
|---------|------------|------------------|
| Automatic reviews | Yes | No |
| On-demand reviews | Yes (ask AI) | Yes (click/shortcut) |
| Works with AI assistants | Required | Optional |
| IDE extensions | All | All |
| CLI tools | Yes | No |
| Review uncommitted changes | Via AI prompt | Yes (sidebar button) |
| Keyboard shortcut | N/A | `Ctrl+Shift+K` |

## Next steps

<div class="grid cards" markdown>

-   :material-robot: **Agent Mode**

    ---

    Automatic reviews for AI-assisted coding.

    [:octicons-arrow-right-24: Get started](/code-reviews/agent-mode/)

-   :material-cursor-default-click: **Instant IDE Mode**

    ---

    Direct reviews from your editor.

    [:octicons-arrow-right-24: Get started](/code-reviews/instant-ide-mode/)

</div>
