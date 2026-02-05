---
title: Code Reviews
description: Learn how to use kluster.ai's Code Reviews to validate your code in real time—detecting bugs, security issues, and quality problems so you can ship safely.
categories: Basics
---

# Code Reviews

Code Reviews analyzes your code for bugs, security vulnerabilities, and quality issues. It works for **human-written code**, **AI-generated code**, and **repo reviews**, with review modes tailored to each workflow.

For in-editor reviews, the service integrates directly into your IDE or CLI (Cursor, VS Code, Windsurf, Claude Code, and others), analyzing code as you work. For system-wide analysis, repo reviews scan your entire repository through the web dashboard.

## Key features

- **Flexible review modes**: Reviews for human-written code, AI-generated code, and system-wide repo analysis.
- **Comprehensive issue detection**: Analyzes 7 issue types — *Semantic, Intent, Logical, Security, Knowledge, Performance,* and *Quality*.
- **Customizable sensitivity**: Configure detection sensitivity from *Low* to *Critical*.
- **Dual analysis tools**: Real-time Code Review and Dependency Analysis for complete coverage.
- **Instant fixes**: Apply suggested fixes with one click, or let your AI assistant handle them automatically.

## Human-written code

**For direct, in-editor reviews without AI.**

Review code you write yourself with on-demand reviews—no AI assistant needed. Available features include:

- **Code block review**: Review selected code snippets.
- **Current file review**: Analyze the file you're working on.
- **Uncommitted changes review**: Check all modified files before committing.

**Compatible with**: Cursor, VS Code, Windsurf, Antigravity (IDEs only)

[:octicons-arrow-right-24: Get started with human-written code reviews](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/quickstart/)

## AI-generated code

**For AI-assisted coding workflows.**

When your AI coding assistant generates or modifies code, kluster.ai automatically reviews it in real-time. You can also ask your AI to review existing files on demand.

**AI-generated code reviews also verify *intent*—ensuring your AI actually did what you asked**, not just that the code works. This context-aware check is only possible when kluster.ai sees your original prompt.

- **Automatic reviews**: Triggered automatically when AI generates code.
- **On-demand reviews**: Triggered when you ask your AI to review existing code.

**Compatible with**: Cursor, VS Code, Windsurf, Antigravity (IDEs) and Claude Code, Codex CLI (CLIs)

[:octicons-arrow-right-24: Get started with AI-generated code reviews](/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/quickstart/)

## Repo reviews

**For system-wide codebase analysis.**

Repo reviews analyze your entire repository as a system, uncovering bugs and risks that don't belong to any single change or PR. These issues only emerge when multiple parts of the code interact—problems that survive individual code reviews because they're invisible in isolation.

Common issues found by repo reviews include:

- **Cross-module bugs**: Code paths that look safe in isolation but break when exercised together.
- **Silent error propagation**: Errors that propagate silently across modules and only surface in production.
- **State inconsistencies**: State that becomes inconsistent under retries, partial failures, or restarts.
- **Bypassed validation**: Security or validation checks applied in one place but bypassed in another.
- **Assumption violations**: Logic that relies on assumptions enforced elsewhere in the codebase.

Repo reviews complement PR-level reviews by revealing problems that already exist in your system—issues that would remain hidden until something breaks.

**Available on**: Web dashboard only (requires GitHub/GitLab connection)

[:octicons-arrow-right-24: Get started with repo reviews](/code-reviews/repo-reviews/quickstart/)

!!! tip "Need help choosing?"
    See [Pick your workflow](/code-reviews/get-started/pick-your-workflow/) for a detailed comparison and decision guide.



## Next steps

- **[Installation](/code-reviews/get-started/installation/)**: Install kluster.ai in your IDE or CLI tool.
- **[Human-written code](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/quickstart/)**: Get started with in-editor reviews.
- **[AI-generated code](/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/quickstart/)**: Set up automatic and on-demand reviews.
- **[Repo reviews](/code-reviews/repo-reviews/quickstart/)**: Analyze your entire codebase for system-wide issues.
- **[Pick your workflow](/code-reviews/get-started/pick-your-workflow/)**: Compare modes and find the right fit.
