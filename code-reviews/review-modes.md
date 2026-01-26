---
title: Code Reviews
description: Learn how to use kluster.ai's Code Reviews to validate your code in real time—detecting bugs, security issues, and quality problems so you can ship safely.
---

# Code Reviews

Code Reviews analyzes your code for bugs, security vulnerabilities, and quality issues. It works for both **human-written code** and **AI-generated code**, with review modes tailored to each workflow.

The service integrates directly into your IDE or CLI (Cursor, VS Code, Windsurf, Claude Code, and others), analyzing code as you work.

## Key features

- **Flexible review modes**: Reviews for human-written code and AI-generated code.
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

[:octicons-arrow-right-24: Get started with human-written code reviews](/code-reviews/human-written-code/on-demand-reviews/quickstart/)

## AI-generated code

**For AI-assisted coding workflows.**

When your AI coding assistant generates or modifies code, kluster.ai automatically reviews it in real-time. You can also ask your AI to review existing files on demand.

**AI-generated code reviews also verify *intent*—ensuring your AI actually did what you asked**, not just that the code works. This context-aware check is only possible when kluster.ai sees your original prompt.

- **Automatic reviews**: Triggered automatically when AI generates code.
- **On-demand reviews**: Triggered when you ask your AI to review existing code.

**Compatible with**: Cursor, VS Code, Windsurf, Antigravity (IDEs) and Claude Code, Codex CLI (CLIs)

[:octicons-arrow-right-24: Get started with AI-generated code reviews](/code-reviews/ai-generated-code/automatic-reviews/quickstart/)

!!! tip "Need help choosing?"
    See [Pick your workflow](/code-reviews/get-started/pick-your-workflow/) for a detailed comparison and decision guide.



## Next steps

- **[Installation](/code-reviews/get-started/installation/)**: Install kluster.ai in your IDE or CLI tool.
- **[Human-written code](/code-reviews/human-written-code/on-demand-reviews/quickstart/)**: Get started with in-editor reviews.
- **[AI-generated code](/code-reviews/ai-generated-code/automatic-reviews/quickstart/)**: Set up automatic and on-demand reviews.
- **[Pick your workflow](/code-reviews/get-started/pick-your-workflow/)**: Compare modes and find the right fit.
