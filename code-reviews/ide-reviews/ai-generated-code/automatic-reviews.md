---
title: Automatic reviews for AI-generated code
description: Set up automatic code reviews and dependency checks for AI-generated code. Reviews run in real-time as your AI writes code.
categories: Basics, IDE Reviews
---

# Automatic reviews

Learn how to use [kluster.ai](https://www.kluster.ai/){target=\_blank} with your preferred AI assistant to catch bugs, security flaws, and logic errors instantly—as your AI writes code.

!!! note ".klusterignore is not applied in this flow (yet)"
    Automatic reviews triggered by AI assistants currently do **not** use [`.klusterignore`](/code-reviews/configuration/klusterignore/) to exclude files.

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

    ![VS Code Auto Review - Unprotected API](/images/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/vscode-auto-review.webp)

=== "Claude Code"

    In the terminal, Claude Code displays the review results immediately.

    ![Claude Code Auto Review - Unprotected API](/images/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/claude-auto-review.webp)

## Compatible with

--8<-- 'text/code-reviews/compatible-ides-all.md'

## Configuration

You can customize how automatic reviews work in your [configuration options](/code-reviews/configuration/options/):

- **Enabled tools**: Toggle Code Review and Dependency Analysis on/off.
- **Sensitivity**: Adjust how strictly issues are flagged (Low → Critical).
- **Bug check types**: Select which issue types to check (Security, Logic, Performance, etc.).

## Dependency checks

Code Reviews protects you when starting new projects or adding libraries by validating dependencies before installation.

!!! note ".klusterignore is not applied in this flow (yet)"
    Automatic dependency checks triggered by AI assistants currently do **not** use [`.klusterignore`](/code-reviews/configuration/klusterignore/) to exclude files.

### How dependency checks work

1.  **You prompt**: Ask your AI to start a project (e.g., "Scaffold a Next.js app with Auth.js").
2.  **AI suggests**: The AI lists the necessary dependencies.
3.  **kluster.ai verifies**: The `kluster_dependency_check` tool checks every package for security vulnerabilities and license compliance before you install them.


When the AI suggests a package version with a known vulnerability, kluster.ai alerts you immediately, preventing the risk from entering your codebase.

![Dependency Analysis Example](/images/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/dependency-analysis.webp)

## Pause reviews

--8<-- 'text/code-reviews/ide-reviews/ide-pause.md'

--8<-- 'text/code-reviews/ide-reviews/cli-pause.md'

## Next steps

- **[On-demand reviews](/code-reviews/ide-reviews/ai-generated-code/on-demand-reviews/)**: Review existing code on demand.
- **[Configuration](/code-reviews/configuration/options/)**: Customize dependency check behavior.
