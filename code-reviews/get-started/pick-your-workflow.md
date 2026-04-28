---
title: Pick Your Code Review Workflow
description: Compare the supported Code Reviews modes—human-written, AI-generated, CLI, and repo-wide—and pick the workflow that fits how you write code.
categories: Basics
---

# Pick your workflow

Code Reviews offers four distinct modes that adapt to how you work. Whether you're coding with an AI assistant, writing code directly, reviewing from the terminal, or analyzing your entire codebase, this guide helps you understand which mode fits your workflow—and why many developers use more than one.

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

-   **CLI**

    ---

    For terminal-based workflows and automation. Review code from the command line, automate with git hooks, or integrate into CI/CD pipelines.

    [:octicons-arrow-right-24: Learn more](#cli)

-   **Repo Reviews**

    ---

    For analyzing your entire codebase. Find bugs that emerge from interactions across modules—issues that survive individual PR reviews because they're only visible at the system level.

    [:octicons-arrow-right-24: Learn more](#repo-reviews)

</div>

## Human-written code

Human-written code reviews give you direct control over when reviews happen. Select any code in your editor and trigger a review instantly—no AI assistant required. This mode is built into the kluster.ai extension and provides three ways to review: right-click menu, keyboard shortcut, or the extension sidebar.

Use it to review code you wrote yourself, audit files before committing, or check legacy code you inherited. The reviews run the same comprehensive analysis as AI-generated code reviews, just triggered manually instead of automatically.

**Compatible with**: Cursor, VS Code, Visual Studio, Windsurf, Antigravity, JetBrains (IDEs only).

!!! info "Not available for CLI tools"
    Human-written code reviews require an IDE extension. For CLI tools like Claude Code or Codex CLI, use AI-generated code reviews instead.

[:octicons-arrow-right-24: Get started with human-written code reviews](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/)


## AI-generated code

AI-generated code reviews integrate directly with your AI coding assistant. When the AI generates or modifies code, [kluster.ai](https://www.kluster.ai/){target=\_blank} automatically analyzes the changes in real-time. You can also ask your AI to review existing files on demand—just say "review this file" and the AI triggers an on-demand review.

This mode is designed for developers who code with AI assistants like Claude Code, Cursor, or Copilot. The review happens seamlessly in the background, catching security vulnerabilities, logic errors, and quality issues before they become problems.

**Compatible with**:

- **IDE extensions**: Cursor, VS Code, Visual Studio, Windsurf, Antigravity, JetBrains.
- **CLI tools**: Claude Code, Codex CLI.

[:octicons-arrow-right-24: Get started with AI-generated code reviews](/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/)


## CLI

The kluster-cli tool brings code reviews to your terminal. Review staged changes, diffs against branches, or individual files—all without opening an IDE. Install git hooks to automate reviews on every commit or push, or use JSON output to integrate reviews into scripts and CI/CD pipelines.

Use it when you prefer terminal workflows, need to automate reviews in git hooks, or want to integrate code reviews into CI/CD.

**Available on**: macOS, Linux, Windows.

[:octicons-arrow-right-24: Get started with CLI](/code-reviews/cli/quickstart/)


## Repo Reviews

Repo Reviews take a fundamentally different approach: instead of reviewing individual changes, it analyzes your entire repository as a complete system. This reveals bugs and risks that don't belong to any single PR or file—issues that only become visible when you examine how multiple parts of your code interact.

Use Repo Reviews to catch problems that slip through PR-level reviews:

- **Cross-module interactions**: Code paths that work in isolation but break when components interact.
- **System-wide vulnerabilities**: Security checks that exist in some code paths but are bypassed in others.
- **State management issues**: State that becomes inconsistent under edge cases like retries or partial failures.
- **Assumption violations**: Logic that depends on constraints enforced elsewhere in the codebase.

Repo Reviews complement your existing review workflow. Run them periodically to surface issues that already exist in your codebase—problems that would otherwise remain hidden until they cause production incidents.

**Available on**: Web dashboard and `kluster-cli` (requires GitHub, GitLab, Bitbucket, or Azure DevOps connection).

!!! note "Usage limits"
    Pro plans include 1 repo review per month. Enterprise plans include higher limits. [Contact us](https://www.kluster.ai/contact){target=\_blank} to learn more.

[:octicons-arrow-right-24: Get started with Repo Reviews](/code-reviews/repo-reviews/quickstart/)


## Using multiple modes

Most teams combine multiple review modes:

- **Human-written code reviews**: For reviewing code you write directly in your editor.
- **AI-generated code reviews**: For catching issues as your AI assistant generates code.
- **CLI**: For terminal workflows, git hook automation, and CI/CD integration.
- **Repo Reviews**: For periodic system-wide analysis to catch cross-module bugs.

If you use Cursor, VS Code, Visual Studio, Windsurf, Antigravity, or JetBrains, you get both human-written and AI-generated code reviews in a single installation—switch seamlessly between AI-assisted coding and manual reviews without changing tools.

Add CLI hooks to enforce reviews on every push, and run Repo Reviews periodically as a safety net to catch system-wide issues that survive individual code reviews.

## Enrich reviews with External Knowledge

Connect kluster to external tools like Jira so your code reviews include project requirements and ticket specifications. When kluster knows what you're building, it can verify that your implementation matches the spec — not just that the code is correct.

[:octicons-arrow-right-24: Set up External Knowledge](/code-reviews/external-knowledge/quickstart/)

## Next steps

- **[Human-written code](/code-reviews/ide-reviews/human-written-code/on-demand-reviews/)**: Set up on-demand reviews in your editor.
- **[AI-generated code](/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/)**: Set up automatic reviews for AI-assisted coding.
- **[CLI quickstart](/code-reviews/cli/quickstart/)**: Review code from the terminal.
- **[Repo Reviews quickstart](/code-reviews/repo-reviews/quickstart/)**: Run your first system-wide codebase analysis.
- **[External Knowledge quickstart](/code-reviews/external-knowledge/quickstart/)**: Connect kluster to Jira for context-aware reviews.
