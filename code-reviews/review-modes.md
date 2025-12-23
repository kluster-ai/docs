---
title: Review Modes
description: Learn about kluster.ai's two review modes—Agent Mode for AI-assisted workflows and Instant IDE Mode for direct in-editor reviews.
---

# Review Modes

Code Reviews offers two distinct modes to fit how you work. Whether you're coding with an AI assistant or reviewing code directly in your editor, kluster.ai adapts to your workflow.

## Agent Mode

**For AI-assisted coding workflows.**

Agent Mode works alongside your AI coding assistant. When the AI generates or modifies code, kluster.ai automatically reviews it in real-time. You can also ask your AI to review existing files on demand.

- **Automatic agent reviews**: Triggered automatically when AI generates code
- **Manual agent reviews**: Triggered when you ask your AI to review existing code

**Supported tools**: Cursor, VS Code, Windsurf, Antigravity, Claude Code, Codex CLI

[:octicons-arrow-right-24: Learn about Agent Mode](/code-reviews/agent-mode/)

---

## Instant IDE Mode

**For direct, in-editor reviews without AI.**

Instant IDE Mode gives you immediate code reviews through your IDE's interface. Right-click any code, use a keyboard shortcut, or click a button in the extension sidebar—no AI assistant needed.

- **Right-click menu**: Select code and review instantly
- **Keyboard shortcut**: `Ctrl+Shift+K` for quick access
- **Extension sidebar**: Review current file or all uncommitted changes

**Supported IDEs**: Cursor, VS Code, Windsurf, Antigravity

[:octicons-arrow-right-24: Learn about Instant IDE Mode](/code-reviews/instant-ide-mode/)

---

## Comparison

| Feature | Agent Mode | Instant IDE Mode |
|---------|------------|------------------|
| **How it works** | AI assistant triggers reviews | You trigger reviews directly |
| **Automatic reviews** | Yes, while AI codes | No |
| **On-demand reviews** | Yes, ask your AI | Yes, click or shortcut |
| **IDE extensions** | Yes | Yes |
| **CLI tools** | Yes (Claude Code, Codex) | No |
| **Requires AI assistant** | Yes | No |

## Which mode should I use?

**Use Agent Mode if:**

- You code with AI assistants (Cursor, Copilot, Claude Code, etc.)
- You want automatic reviews as code is generated
- You prefer asking your AI to review files for you

**Use Instant IDE Mode if:**

- You write code directly without AI assistance
- You want quick reviews via right-click or keyboard shortcut
- You need to review uncommitted changes before committing

**Use both!** Most developers use both modes. Agent Mode catches issues during AI-assisted coding, while Instant IDE Mode provides quick checks when you're writing code yourself.

## Next steps

<div class="grid cards" markdown>

-   :material-robot: **Agent Mode**

    ---

    Set up automatic and manual agent reviews with your AI assistant.

    [:octicons-arrow-right-24: Get started](/code-reviews/agent-mode/)

-   :material-cursor-default-click: **Instant IDE Mode**

    ---

    Review code directly from your editor interface.

    [:octicons-arrow-right-24: Get started](/code-reviews/instant-ide-mode/)

-   :material-download: **Installation**

    ---

    Install kluster.ai in your IDE or CLI tool.

    [:octicons-arrow-right-24: Install now](/code-reviews/get-started/installation/)

</div>
