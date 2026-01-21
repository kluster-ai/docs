---
title: Pick your workflow
description: Choose between human-written code and AI-generated code reviews based on how you write code. Or use both.
---

# Pick your workflow

Code Reviews offers two distinct modes that adapt to how you work. Whether you're coding with an AI assistant or writing code directly, this guide helps you understand which mode fits your workflow—and why most developers use both.

## Choose your mode

<div class="grid cards" markdown>

-   **Human-written code**

    ---

    For developers writing code directly. Review any code on-demand with a right-click, keyboard shortcut, or sidebar button. No AI assistant needed—just you and your editor.

    [:octicons-arrow-right-24: Learn more](#human-written-code)

-   **AI-generated code**

    ---

    For developers using AI coding assistants. Your code is reviewed automatically every time your AI generates or modifies code—no manual steps required.

    [:octicons-arrow-right-24: Learn more](#ai-generated-code)

</div>

## Human-written code

Human-written code reviews give you direct control over when reviews happen. Select any code in your editor and trigger a review instantly—no AI assistant required. This mode is built into the kluster.ai extension and provides three ways to review: right-click menu, keyboard shortcut, or the extension sidebar.

Use it to review code you wrote yourself, audit files before committing, or check legacy code you inherited. The reviews run the same comprehensive analysis as AI-generated code reviews, just triggered manually instead of automatically.

**Compatible with**: Cursor, VS Code, Windsurf, Antigravity (IDEs only).

!!! info "Not available for CLI tools"
    Human-written code reviews require an IDE extension. For CLI tools like Claude Code or Codex CLI, use AI-generated code reviews instead.

[:octicons-arrow-right-24: Get started with human-written code reviews](/code-reviews/human-written-code/on-demand-reviews/quickstart/)


## AI-generated code

AI-generated code reviews integrate directly with your AI coding assistant. When the AI generates or modifies code, [kluster.ai](https://kluster.ai){target=_blank} automatically analyzes the changes in real-time. You can also ask your AI to review existing files on demand—just say "review this file" and the AI triggers an on-demand review.

This mode is designed for developers who code with AI assistants like Claude Code, Cursor, or Copilot. The review happens seamlessly in the background, catching security vulnerabilities, logic errors, and quality issues before they become problems.

**Compatible with**:

- **IDE extensions**: Cursor, VS Code, Windsurf, Antigravity.
- **CLI tools**: Claude Code, Codex CLI.

[:octicons-arrow-right-24: Get started with AI-generated code reviews](/code-reviews/ai-generated-code/automatic-reviews/quickstart/)


## Using both modes

If you use Cursor, VS Code, Windsurf, or Antigravity, you get the best of both worlds. Install kluster.ai once and both modes are available—switch seamlessly between AI-assisted coding and manual reviews without changing tools.

Use AI-generated code reviews when pair-programming with AI, switch to human-written code reviews when writing code yourself, and run **Review uncommitted changes** before every commit to catch anything missed.

## Next steps

- **[Human-written code quickstart](/code-reviews/human-written-code/on-demand-reviews/quickstart/)**: Set up on-demand reviews in your editor.
- **[AI-generated code quickstart](/code-reviews/ai-generated-code/automatic-reviews/quickstart/)**: Set up automatic reviews for AI-assisted coding.
