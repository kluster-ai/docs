---
title: Quick Start
description: Learn how to use Code Reviews in your daily workflow. Trigger reviews automatically or manually, interpret results, and apply fixes.
---

# Quick Start

<div class="embed-container">
    <iframe
        src="https://www.youtube.com/embed/-V0VsqgTza8"
        title="Instant Code Reviews with kluster.ai"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
    </iframe>
</div>

**Code Reviews verifies your code for security, quality, and correctness.** Whether you're using AI-assisted code generation or writing code yourself, Code Reviews catches issues before they reach production.

This guide shows you how to integrate Code Reviews into your workflow—automatically when using AI assistants, or on-demand when you want control.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/quickstart-prerequisites.md'

## How Code Reviews Works

Code Reviews provides multiple ways to verify your code:

1. **[Auto Review](#auto-review)**: Automatic verification after every code change when working with AI assistants.
2. **[Manual Review](#manual-review)**: On-demand verification you trigger yourself—review selected code, files, or uncommitted changes.
3. **[Dependency Analysis](#dependency-analysis)**: Validates packages before installation.

See the **[Tools Reference](/code-reviews/tools/)** for complete MCP tools documentation.


### Auto Review 

The most powerful way to use Code Reviews is to let it work in the background. You don't need to change how you work—just ask your AI assistant for what you need.

**How it works:**

1.  **You prompt**: Ask your AI assistant to generate code (e.g., "Create a user login endpoint").
2.  **AI generates**: The AI writes the code.
3.  **kluster.ai verifies**: Code Reviews automatically analyzes the diff in real-time.


In this example, the AI creates an API endpoint but makes a critical security error that kluster.ai intervenes to fix.

=== "VS Code"

    In VS Code, you'll see the review appear directly in the chat. kluster.ai flags the issue (e.g., "Unprotected API Endpoint") and provides a fix.

    ![VS Code Auto Review - Unprotected API](/images/code-reviews/quick-start/vscode-auto-review.webp)

=== "Claude Code"

    In the terminal, Claude Code displays the review results immediately.

    ![Claude Code Auto Review - Unprotected API](/images/code-reviews/quick-start/claude-auto-review.webp)

### Dependency Analysis

Code Reviews also protects you when starting new projects or adding libraries.

**How it works:**

1.  **You prompt**: Ask your AI to start a project (e.g., "Scaffold a Next.js app with Auth.js").
2.  **AI suggests**: The AI lists the necessary dependencies.
3.  **kluster.ai verifies**: The Dependency Validator checks every package for security vulnerabilities and license compliance before you install them.


When the AI suggests a package version with a known vulnerability, kluster.ai alerts you immediately, preventing the risk from entering your codebase.

![Dependency Analysis Example](/images/code-reviews/quick-start/dependency-analysis.webp)

### Manual Review

When you write code directly in your editor and want to verify it on your own terms, Code Reviews provides three manual options in your IDE.

#### Code Block Review

Select any code in your editor, right-click, and choose **Review with kluster.ai** (or press ++ctrl+shift+k++). This is useful for:

- Verifying a specific function or block you just wrote
- Checking code during merge conflict resolution
- Getting a quick security check before moving on

![Right-click to review selected code](/images/code-reviews/quick-start/manual-review-this-code.webp)

#### Review Current File

Open the kluster.ai sidebar and click **Review current file** to verify the entire active file.

#### Review Uncommitted Changes

Click **Review uncommitted changes** in the sidebar to verify all staged and unstaged changes before committing.

![Manual review buttons in the kluster.ai sidebar](/images/code-reviews/quick-start/manual-review-this-code-extension.webp)

After the review completes, kluster.ai displays any issues found. You can click **Fix with AI** to automatically resolve them.

![Review results showing issues found](/images/code-reviews/quick-start/manual-review-this-code-extension-3.webp)

!!! warning "Compatibility"
    Code block review (right-click context menu) is not yet available in Cursor. The sidebar review buttons work in all VS Code-based IDEs.

## Next steps

- **[Tools Reference](/code-reviews/tools/)**: Deep dive into all issue types and parameters.
- **[Configuration Options](/code-reviews/configuration/options/)**: Customize Code Reviews behavior for your workflow.
