---
title: Frequently Asked Questions
description: Find answers to common questions about kluster.ai Code Review, covering setup, supported IDEs, review modes, security, and troubleshooting topics.
---

# Frequently Asked Questions

## General

??? question "What's the difference between Agent Mode and Instant IDE Mode?"
   - **Agent Mode**: For AI-assisted workflows. Reviews trigger automatically when AI generates code, or when you ask your AI assistant to review existing code. Works with Claude Code, Codex CLI, Cursor, VS Code, and other AI assistants.

   - **Instant IDE Mode**: Direct editor integration. You trigger reviews yourself by right-clicking code, using keyboard shortcuts, or clicking buttons in the extension sidebar. No AI assistant needed—review any code directly.

??? question "What IDEs and CLI tools are supported?"
    - **IDE Extensions**: Cursor, VS Code, Windsurf, Antigravity

    - **CLI Tools**: Claude Code, Codex CLI

    See [Installation](/code-reviews/get-started/installation/) for setup instructions.

??? question "What programming languages are supported?"
    kluster.ai is language agnostic and can review code in any programming language, including Python, TypeScript, JavaScript, Java, Go, Rust, C++, C#, Ruby, PHP, and more.

??? question "Is my code sent to kluster servers?"
    Yes, code diffs are sent to kluster.ai servers for analysis. All communication is end-to-end encrypted with TLS 1.3. The analysis happens in real-time and results are returned immediately.

??? question "Can I use kluster.ai with any AI model?"
    Yes. When using an AI coding assistant, Code Reviews works with any model available in supported IDEs, including Claude, GPT, Gemini, and others.

??? question "Can I review a full codebase?"
    Yes, using Instant IDE Mode. You can review individual files, selected code blocks, or all uncommitted changes. For large codebases, we recommend reviewing file-by-file or focusing on changed files.

??? question "Can I exclude files or folders from reviews?"
    Currently, exclusion rules are configured at the project level through the kluster.ai platform. See [Custom Rules](/code-reviews/configuration/rules/) for setting up project-specific configurations.

??? question "How can I invite a team member?"
    Team management is available on Team and Enterprise plans. Log in to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank} and navigate to your team settings to invite members.

??? question "How do activation codes work?"
    Activation codes provide promotional credits for kluster.ai plans. See our detailed guide: [How to use activation codes](/code-reviews/activation-codes/).

??? question "How frequently does kluster.ai update its vulnerability detection?"
    We source vulnerability data from frequently updated public CVE databases. Our vulnerability detection updates as new CVEs are published and ingested by those sources, so coverage improves continuously rather than on a fixed schedule.

??? question "How can I provide feedback about issues detected by kluster.ai?"
    Each time a code review is done, a feedback option is available from the extension or in the platform. Your feedback helps improve detection accuracy and reduce false positives.

??? question "Do kluster.ai reviews improve over time?"
    Yes. When you connect your GitHub repositories, kluster.ai learns rules from your repo and applies project-specific configurations. See [Custom Rules](/code-reviews/configuration/rules/) for more details.

    We also continuously improve our engine to perform deeper reviews, optimizing for common issues our users encounter. If you have suggestions for improvement, contact us at [support@kluster.ai](mailto:support@kluster.ai).

## Agent Mode

??? question "What triggers an automatic review?"
    In Agent Mode, reviews trigger automatically when your AI coding assistant generates or modifies code. This happens without any action from you. The code diff is sent to kluster.ai, and the results appear in your chat or terminal.

??? question "Does kluster.ai apply changes automatically?"
    No. kluster.ai identifies issues and suggests fixes, but doesn't modify your code directly. In Agent Mode, the AI assistant decides whether to apply them—in most cases, it will automatically incorporate the fixes. In Instant IDE Mode, you apply fixes yourself using the "Fix with AI" button or manually. Either way, you remain in control.

??? question "Can I disable automatic reviews temporarily?"
    Yes. You can disable automatic reviews from [Options](/code-reviews/configuration/options/) in the kluster.ai platform. Alternatively, you can disable the kluster.ai extension in your IDE, or for CLI tools, disable the MCP server.

??? question "Does it work with multi-file edits?"
    Yes. Agent Mode analyzes diffs across multiple files in a single review, understanding the context of changes that span your codebase.

??? question "How does dependency checking work?"
    The Dependency Validator automatically checks packages before installation. When your AI assistant suggests adding a dependency, kluster.ai validates it for known vulnerabilities and license compliance before the install command runs.

??? question "How do I rollback changes made based on kluster.ai feedback?"
    The changes are made by your AI assistant, not kluster.ai itself. You can revert changes in the file using your IDE undo functionality, Git commands, or simply ask the AI assistant to revert the changes.

## Instant IDE Mode

??? question "How do I trigger an instant review?"
    You can trigger an instant review in three ways:

    1. **Right-click** selected code → "Review with kluster.ai"
    2. Use the extension sidebar. Open the **Instant Review** dropdown and choose a file or uncommitted changes.
    3. Select code and use the **hint** button. This option is not available in Cursor yet.

??? question "Can I review code I didn't write?"
    Yes. Instant IDE Mode works on any code, including your own code, AI-generated code, or code from colleagues. This is useful for auditing existing codebases or reviewing pull requests.

??? question "Can I review a specific code block vs whole file?"
    Yes. Select the code you want to review, then right-click and choose **Review with kluster.ai**. You can review anything from a single function to an entire file.

??? question "Can I review uncommitted changes?"
    Yes. In the kluster.ai extension sidebar, click **Instant Review** and select **Review uncommitted changes**. This reviews all staged and unstaged changes across your repository.

??? question "What's the difference between instant actions and background reviews?"
    - **Instant actions**: Are on-demand—you click a button or use a shortcut to trigger a review.

    - **Ambient Background Reviews (Beta, Enterprise plan)**: Automatically review your code for issues and suggestions as you work, without requiring you to trigger anything. Enable it from the "Enabled Tools" section in [Options](/code-reviews/configuration/options/).
