---
title: Automatic Agent Reviews Quickstart
description: Get started with automatic code reviews when using AI assistants. See how kluster.ai reviews code in real-time as your AI generates it.
---

# Automatic Agent Reviews quickstart

Learn how to use [kluster.ai](https://kluster.ai){target=_blank} with your preferred AI assistant to catch bugs, security flaws, and logic errors instantly—as your AI writes code.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/quickstart-prerequisites.md'

## How automatic reviews work

<div class="embed-container">
    <iframe
        src="https://www.youtube.com/embed/-V0VsqgTza8"
        title="Instant Code Reviews with kluster.ai"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
    </iframe>
</div>

The most powerful way to use Code Reviews is to let it work in the background. You don't need to change how you work—just ask your AI assistant for what you need.

1.  **You prompt**: Ask your AI assistant to generate code (e.g., "Create a user login endpoint").
2.  **AI generates**: The AI writes the code.
3.  **kluster.ai verifies**: Code Reviews automatically analyzes the diff in real-time.


In this example, the AI creates an API endpoint but makes a critical security error that kluster.ai intervenes to fix.

=== "VS Code"

    In VS Code, you'll see the review appear directly in the chat. kluster.ai flags the issue (e.g., "Unprotected API Endpoint") and provides a fix.

    ![VS Code Auto Review - Unprotected API](/images/code-reviews/agent-mode/automatic-agent-reviews/vscode-auto-review.webp)

=== "Claude Code"

    In the terminal, Claude Code displays the review results immediately.

    ![Claude Code Auto Review - Unprotected API](/images/code-reviews/agent-mode/automatic-agent-reviews/claude-auto-review.webp)

## Compatible with

- Cursor
- VS Code (with Copilot)
- Windsurf
- Antigravity
- Claude Code
- Codex CLI

## Configuration

You can customize how automatic reviews work in your [configuration options](/code-reviews/configuration/options/):

- **Enabled tools**: Toggle Code Review and Dependency Analysis on/off.
- **Sensitivity**: Adjust how strictly issues are flagged (Low → Critical).
- **Bug check types**: Select which issue types to check (Security, Logic, Performance, etc.).

## Next steps

- **[Dependency checks](/code-reviews/agent-mode/automatic-agent-reviews/dependency-checks/)**: Learn about package validation.
- **[Manual agent reviews](/code-reviews/agent-mode/manual-agent-reviews/)**: On-demand reviews for existing code.
