---
title: Frequently Asked Questions
description: Find answers to common questions about kluster.ai Code Review, covering setup, supported IDEs, review modes, security, and troubleshooting topics.
---

# Frequently Asked Questions

## General

## What's the difference between Auto Review and Manual Review?

- **Auto Review**: Triggers automatically when AI generates or modifies code via MCP integration. Works with Claude Code, Codex CLI, Cursor, VS Code, and other AI assistants.
- **Manual Review**: Is on-demand, you trigger it yourself by right-clicking code, and using keyboard shortcuts or clicking buttons in the extension. Review any code, whether you wrote it or not.

## What IDEs and CLI tools are supported?

- **IDE Extensions**: Cursor, VS Code, Windsurf, Antigravity
- **CLI Tools**: Claude Code, Codex CLI

See [Installation](/code-reviews/installation/) for setup instructions.

## What programming languages are supported?

kluster.ai is language agnostic and can review code in any programming language, including Python, TypeScript, JavaScript, Java, Go, Rust, C++, C#, Ruby, PHP, and more.

## Is my code sent to kluster servers?

Yes, code diffs are sent to kluster.ai servers for analysis. All communication is end-to-end encrypted with TLS 1.3. The analysis happens in real-time and results are returned immediately.

## Can I use kluster.ai with any AI model?

Yes. When using an AI coding assistant, Code Reviews works with any model available in supported IDEs, including Claude, GPT, Gemini, and others.

## Can I review a full codebase?

Yes, using Manual Review. You can review individual files, selected code blocks, or all uncommitted changes. For large codebases, we recommend reviewing file-by-file or focusing on changed files.

## Can I exclude files or folders from reviews?

Currently, exclusion rules are configured at the project level through the kluster.ai platform. See [Custom Rules](/code-reviews/configuration/rules/) for setting up project-specific configurations.

## How can I invite a team member?

Team management is available on Team and Enterprise plans. Log in to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank} and navigate to your team settings to invite members.

## How do activation codes work?

Activation codes provide promotional credits for kluster.ai plans. See our detailed guide: [How to use activation codes](/code-reviews/activation-codes/).

## How frequently does kluster.ai update its vulnerability detection?

We source vulnerability data from frequently updated public CVE databases. Our vulnerability detection updates as new CVEs are published and ingested by those sources, so coverage improves continuously rather than on a fixed schedule.

## How can I provide feedback about issues detected by kluster.ai?

Each time a code review is done, a feedback option is available from the extension or in the platform. Your feedback helps improve detection accuracy and reduce false positives.

## Do kluster.ai reviews improve over time?

Yes. When you connect your GitHub repositories, kluster.ai learns rules from your repo and applies project-specific configurations. See [Custom Rules](/code-reviews/configuration/rules/) for more details.

We also continuously improve our engine to perform deeper reviews, optimizing for common issues our users encounter. If you have suggestions for improvement, contact us at [support@kluster.ai](mailto:support@kluster.ai).

## Auto Review

## What triggers an automatic review?

Auto Review triggers when your AI coding assistant generates or modifies code. This happens automatically, so you do not need to take any action. The code diff is sent to kluster.ai, and the results appear in your chat or terminal.

## Does kluster.ai apply changes automatically?

No. kluster.ai identifies issues and suggests fixes, but doesn't modify your code directly. In Auto Review mode, the AI assistant decides whether to apply them—in most cases, it will automatically incorporate the fixes. In Manual Review mode, you apply fixes yourself using the "Fix with AI" button or manually. Either way, you remain in control.

## Can I disable Auto Reviews temporarily?

Yes. You can disable Auto Reviews from [Options](/code-reviews/configuration/options/) in the kluster.ai platform. Alternatively, you can disable the kluster.ai extension in your IDE, or for CLI tools, disable the MCP server.

## Does it work with multi-file edits?

Yes. Auto review analyzes diffs across multiple files in a single review, understanding the context of changes that span your codebase.

## How does dependency checking work?

The Dependency Validator automatically checks packages before installation. When your AI assistant suggests adding a dependency, kluster.ai validates it for known vulnerabilities and license compliance before the install command runs.

## How do I rollback changes made based on kluster.ai feedback?

The changes are made by your AI assistant, not kluster.ai itself. You can revert changes in the file using your IDE undo functionality, Git commands, or simply ask the AI assistant to revert the changes.

## Manual Review

## How do I trigger a Manual Review?

You can trigger a Manual Review in three ways:

1. **Right-click** selected code → "Review with kluster.ai"
2. Use the extension sidebar. Open the **Instant Review** dropdown and choose a file or uncommitted changes.
3. Select code and use the **hint** button. This option is not available in Cursor yet.

## Can I review code I didn't write?

Yes. Manual Review works on any code, including your own code, AI-generated code, or code from colleagues. This is useful for auditing existing codebases or reviewing pull requests.

## Can I review a specific code block vs whole file?

Yes. Select the code you want to review, then right-click and choose **Review with kluster.ai**. You can review anything from a single function to an entire file.

## Can I review uncommitted changes?

Yes. In the kluster.ai extension sidebar, click **Instant Review** and select **Review uncommitted changes**. This reviews all staged and unstaged changes across your repository.

## What's the difference between instant actions and background reviews?

- **Instant actions**: Are on-demand—you click a button or use a shortcut to trigger a review.
- **Ambient Background Reviews (Beta, Enterprise plan)**: Automatically review your code for issues and suggestions as you work, without requiring you to trigger anything. Enable it from the "Enabled Tools" section in [Options](/code-reviews/configuration/options/).
