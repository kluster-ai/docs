---
title: Code Reviews — Overview
description: Learn how to use kluster.ai's Code Reviews to validate your code in real time—detecting bugs, security issues, and quality problems so you can ship safely.
---

# Code Reviews

Shipping code with undetected issues creates risk and overhead. Common problems include:

- Difficulty ensuring code correctness before deployment.
- Increased complexity in error handling and QA.
- Potential for cascading failures in production.
- Review cycles that slow development and deployment.

**Code Reviews** is part of kluster.ai trust layer, validating code in real time so you can ship with confidence where accuracy and security matter most.

With Code Reviews, you can ship confidently: potential issues are surfaced (and can be auto-corrected) before they reach production. The service integrates directly into your IDE or CLI (Cursor, VS Code, Windsurf, Claude Code, and others), analyzing code as you work.

## How Code Reviews works

Code Reviews analyzes your code (typically in diff format) and returns a structured assessment with actionable fixes. It combines the following MCP tools:

--8<-- 'text/code-reviews/code-tools.md'

The service responds with the following fields:

- **`isCodeCorrect`**: Indicates whether the code has issues.
- **`issues`**: Array of detected problems with type, severity, and priority.
- **`explanation`**: Summary of all issues found.
- **`agent_todo_list`**: Prioritized list of fixes to apply.

## Key features

- **Real-time code review**: Monitors code changes as they happen.
- **Comprehensive issue detection**: Analyzes 7 issue types — *Semantic, Intent, Logical, Security, Knowledge, Performance,* and *Quality*.
- **Customizable sensitivity levels**: Configure detection sensitivity from *Low* to *Critical*.
- **Dual analysis tools**: Real-time **Code Review** and **Dependency Analysis** for complete coverage.
- **Automatic correction**: Issues can be fixed immediately with one-click remediation.

## Configuration options

Tailor Code Reviews to your workflow:

- **Sensitivity settings**: Set minimum sensitivity to report (*Low → Critical*).
- **Bug check types**: Select which issue types to check: *Semantic, Security, Quality, Intent, Knowledge, Logical, Performance*.
- **Enabled tools**: Select which analysis tools to activate: *Real-time Code Review* and *Dependency Analysis*.

These settings can be configured directly in your IDE integration.

## Target applications and use cases

- IDE integrations for AI-assisted and manual development.
- Automated code review pipelines.
- CI/CD security scanning.
- Development workflow automation.
- Code quality assurance systems.

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

    Cursor, VS Code, Windsurf, Antigravity—install directly from the marketplace.

    [:octicons-arrow-right-24: View all IDEs](/code-reviews/installation/#__tabbed_1_2){target=\_blank}

-   :material-console: __CLI Tools__
    ---

    Claude Code, Codex CLI—run a simple command to set up.

    [:octicons-arrow-right-24: View CLI setup](/code-reviews/installation/#__tabbed_1_5){target=\_blank}

</div>

## Additional resources

- **[Get started](/code-reviews/installation/)**: Run Code Reviews in minutes.
- **[See real examples](/code-reviews/examples/cursor-firebase-nextjs/)**: Walk through a complete Firebase migration case study.
