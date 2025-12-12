---
title: Code Reviews — Overview
description: Learn how to use kluster.ai's Code Reviews to validate your code in real time—detecting bugs, security issues, and quality problems so you can ship safely.
---

# Code Reviews

Code Reviews analyzes your code for bugs, security vulnerabilities, and quality issues. It works in two modes: automatically when using AI coding assistants, or on-demand when you trigger a Manual Review.

The service integrates directly into your IDE or CLI (Cursor, VS Code, Windsurf, Claude Code, and others), analyzing code as you work.

## How Code Reviews works

Whether you're working with an AI assistant or writing code yourself, Code Reviews adapts to your workflow. It offers two ways to validate your code:

- **Auto Review**: Triggers automatically when AI generates or modifies code. Issues are caught and fixed in real-time as you work with your AI assistant.
- **Manual Review**: On-demand reviews you trigger yourself. Right-click any code, use a shortcut, or review all uncommitted changes at once.

Both modes detect the same issue types and return actionable fixes you can apply immediately. See the [Quick Start](/code-reviews/quickstart/) to try it out.

## Key features

- **Flexible review modes**: Auto Reviews for AI-assisted workflows, Manual Reviews for any code you want to check.
- **Comprehensive issue detection**: Analyzes 7 issue types — *Semantic, Intent, Logical, Security, Knowledge, Performance,* and *Quality*.
- **Customizable sensitivity levels**: Configure detection sensitivity from *Low* to *Critical*.
- **Dual analysis tools**: Real-time **Code Review** and **Dependency Analysis** for complete coverage.
- **Instant fixes**: Apply suggested fixes with one click, or let your AI assistant handle them automatically.

## Configuration options

Not all projects have the same requirements. Code Reviews gives you full control over what gets flagged and how sensitive the detection should be:

- **Sensitivity settings**: Set minimum sensitivity to report (*Low → Critical*).
- **Bug check types**: Select which issue types to check: *Semantic, Security, Quality, Intent, Knowledge, Logical, Performance*.
- **Enabled tools**: Select which analysis tools to activate: *Real-time Code Review* and *Dependency Analysis*.

See [Options](/code-reviews/configuration/options/) for full configuration details.

## When to use Code Reviews

- **Code validation**: Review code before production use.
- **Security scanning**: Detect potential vulnerabilities early.
- **Quality assurance**: Enforce best practices automatically.
- **Dependency checking**: Validate that new packages are secure and up-to-date.

## Setup instructions

Code Reviews is available as a native extension for IDEs and CLI tools. Get started in under 30 seconds:

<div class="grid cards" markdown>

-   :material-code-tags: __IDE Extensions__

    ---

    Cursor, VS Code, Windsurf, Antigravity—Manual Reviews or Auto Reviews.

    [:octicons-arrow-right-24: View all IDEs](/code-reviews/installation/#__tabbed_1_2){target=\_blank}

-   :material-console: __CLI Tools__
    
    ---

    Claude Code, Codex CLI—AI-assisted reviews only.

    [:octicons-arrow-right-24: View CLI](/code-reviews/installation/#__tabbed_1_5){target=\_blank}

</div>

## Additional resources

- **[Get started](/code-reviews/installation/)**: Run Code Reviews in minutes.
- **[See real examples](/code-reviews/examples/cursor-firebase-nextjs/)**: Walk through a complete Firebase migration case study.
