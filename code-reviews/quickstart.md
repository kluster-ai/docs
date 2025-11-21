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

**Code Reviews verifies AI-generated code.** It sits between your AI assistant and your codebase, verifying every line of generated code in real-time to ensure security, correctness, and quality.

This guide shows you how to integrate Code Reviews into your daily workflow to catch issues before they happen.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/quickstart-prerequisites.md'

## How Code Reviews Works

Code Reviews provides **three verification tools** that work seamlessly with your AI assistant:

1. **[Auto Review](/code-reviews/tools/#__tabbed_1_1)**: Automatically verifies every code change in real-time (default).
2. **[Manual Review](/code-reviews/tools/#__tabbed_1_2)**: On-demand verification when you ask for it.
3. **[Dependency Analysis](/code-reviews/tools/#__tabbed_1_1)**: Validates packages before installation.

See the **[Tools Reference](/code-reviews/tools/)** for complete documentation on all verification capabilities.


### Auto Review 

The most powerful way to use Code Reviews is to let it work in the background. You don't need to change how you work—just ask your AI assistant for what you need.

**How it works:**

1.  **You prompt**: Ask your AI assistant to generate code (e.g., "Create a user login endpoint").
2.  **AI generates**: The AI writes the code.
3.  **kluster.ai verifies** - Code Reviews automatically analyzes the diff in real-time.


In this example, the AI creates an API endpoint but makes a critical security error that kluster.ai intervenes to fix.

=== "VS Code"

    In VS Code, you'll see the review appear directly in the chat. kluster.ai flags the issue (e.g., "Unprotected API Endpoint") and provides a fix.

    ![VS Code Auto Review - Unprotected API](/images/code-reviews/quick-start/vscode-auto-review.webp)

=== "Claude Code"

    In the terminal, Claude Code displays the review results immediately.

    ![Claude Code Auto Review - Unprotected API](/images/code-reviews/quick-start/claude-auto-review.webp)

!!! tip "Manual Review"
    You can also trigger a review manually any time by just asking your AI to "review this code".

### Dependency Analysis

Code Reviews also protects you when starting new projects or adding libraries.

**How it works:**

1.  **You prompt** - Ask your AI to start a project (e.g., "Scaffold a Next.js app with Auth.js").
2.  **AI suggests** - The AI lists the necessary dependencies.
3.  **kluster.ai verifies** - The Dependency Validator checks every package for security vulnerabilities and license compliance before you install them.


When the AI suggests a package version with a known vulnerability, kluster.ai alerts you immediately, preventing the risk from entering your codebase.

![Dependency Analysis Example](/images/code-reviews/quick-start/dependency-analysis.webp)

## Next steps

- **[Tools Reference](/code-reviews/tools/)**: Deep dive into all issue types and parameters.
- **[Configuration Options](/code-reviews/configuration/options/)**: Customize Code Reviews behavior for your workflow.
