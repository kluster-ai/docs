---
title: Frequently Asked Questions
description: Find answers to common questions about kluster.ai Code Review, covering setup, supported IDEs, review modes, security, and troubleshooting topics.
---

# Frequently Asked Questions

## General

### When should I use Agent Mode vs Instant IDE Mode?

- **[Agent Mode](/code-reviews/agent-mode/automatic-agent-reviews/quickstart/)**: Use this mode when coding with an AI assistant. Reviews trigger automatically.
- **[Instant IDE Mode](/code-reviews/instant-ide-mode/instant-actions/quickstart/)**:  Use this mode when writing code yourself or reviewing existing code. You trigger reviews manually.

### I mostly write code without AI—is kluster.ai useful for me?

Yes. Instant IDE Mode is built for this. Right-click any code or press `Ctrl+Shift+K` to trigger a review. No AI assistant needed. See [Instant IDE Mode](/code-reviews/instant-ide-mode/instant-actions/quickstart/) for setup.

### When should I run a manual review?

Run a manual review before pushing changes. Use **Review uncommitted changes** for staged files, or **Review all branch changes** to review all changes made since the branch was created.

### Do the two modes ever conflict or overlap?

No. Agent Mode runs when AI generates code. Instant IDE Mode runs when you trigger it. They work independently.

### What IDEs and CLI tools are supported?

- **IDE Extensions**: Cursor, VS Code, Windsurf, Antigravity
- **CLI Tools**: Claude Code, Codex CLI

See [Installation](/code-reviews/get-started/installation/) for setup instructions.

### What programming languages are supported?

kluster.ai is language agnostic and can review code in any programming language, including Python, TypeScript, JavaScript, Java, Go, Rust, C++, C#, Ruby, PHP, and more.

### Can I review a full codebase?

Yes, using [Instant IDE Mode](/code-reviews/instant-ide-mode/instant-actions/quickstart/). You can review individual files, selected code blocks, or all uncommitted changes. For large codebases, we recommend reviewing file-by-file or focusing on changed files.

### Can I use kluster.ai with any AI model?

Yes. When using an AI coding assistant, Code Reviews works with any model available in supported IDEs, including Claude, GPT, Gemini, and others.

### Can I exclude files or folders from reviews?

Currently, exclusion rules are configured at the project level through the kluster.ai platform. See [Custom Rules](/code-reviews/configuration/rules/) for setting up project-specific configurations.

### How can I invite a team member?

Team management is available on Team and Enterprise plans. Log in to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank} and navigate to your team settings to invite members.

### How do activation codes work?

Activation codes provide promotional credits for kluster.ai plans. See our detailed guide: [How to use activation codes](/code-reviews/activation-codes/).

### How frequently does kluster.ai update its vulnerability detection?

kluster.ai sources vulnerability data from public CVE databases that are continuously updated. Detection coverage improves as new CVEs are published and ingested, rather than following a fixed update schedule.

### How can I provide feedback about issues detected by kluster.ai?

Each time a code review is done, a feedback option is available from the extension or in the platform. Your feedback helps improve detection accuracy and reduce false positives.

### Do kluster.ai reviews improve over time?

Yes. When you connect your GitHub repositories, kluster.ai learns rules from your repo and applies project-specific configurations. See [Custom Rules](/code-reviews/configuration/rules/) for more details.

We also continuously improve our engine to perform deeper reviews, optimizing for common issues our users encounter. If you have suggestions for improvement, contact us at [support@kluster.ai](mailto:support@kluster.ai).

## Agent Mode

### What triggers an automatic review?

In Agent Mode, reviews trigger automatically when your AI coding assistant generates or modifies code. This happens without any action from you. The code diff is sent to kluster.ai, and the results appear in your chat or terminal.

### How does Agent Mode handle intent verification differently than Instant IDE Mode?

Agent Mode sees your original prompt to the AI, so it can verify the AI did what you asked—not just that the code runs. If you asked for Firebase auth but the AI used localStorage, Agent Mode catches it. Instant IDE Mode cannot check intent because it only sees the code, not your request. See [this example](/code-reviews/agent-mode/examples/cursor-firebase-nextjs/) for a real case.

### Does kluster.ai apply changes automatically?

No. kluster.ai identifies issues and suggests fixes, but doesn't modify your code directly. In Agent Mode, the AI assistant decides whether to apply them—in most cases, it will automatically incorporate the fixes. In Instant IDE Mode, you apply fixes yourself using the **Fix with AI** button or manually. Either way, you remain in control.

### Can I disable automatic reviews temporarily?

Yes. You can disable automatic reviews from [Options](/code-reviews/configuration/options/) in the kluster.ai platform. Alternatively, you can disable the kluster.ai extension in your IDE, or for CLI tools, disable the MCP server.

### Does it work with multi-file edits?

Yes. Agent Mode analyzes diffs across multiple files in a single review, understanding the context of changes that span your codebase.

### How does dependency checking work?

The Dependency Validator automatically checks packages before installation. When your AI assistant suggests adding a dependency, kluster.ai validates it for known vulnerabilities before the install command runs.

### How do I rollback changes made based on kluster.ai feedback?

The changes are made by your AI assistant, not kluster.ai itself. You can revert changes in the file using your IDE undo functionality, Git commands, or simply ask the AI assistant to revert the changes.

## Instant IDE Mode

### What is the fastest way to check code I just wrote?

Select the code, press **Ctrl+Shift+K** (or right-click → **Review with kluster.ai**). Results appear in seconds with issues and one-click fixes.

### Can I use kluster.ai for code reviews in pull requests?

Yes. Check out the PR locally and either:

1. Use **Review uncommitted changes** to scan all modifications.
2. Select specific code and review it.

### How do I trigger a Manual Review?

You can trigger a Manual Review in three ways:

1. **Right-click** selected code → "Review with kluster.ai."
2. Use the extension sidebar. Open the **Instant Review** dropdown and choose a file or uncommitted changes.
3. Select code and use the **hint** button. This option is not available in Cursor yet.

### Can I review code I didn't write?

Yes. Manual Review works on any code, including your own code, AI-generated code, or code from colleagues. This is useful for auditing existing codebases or reviewing pull requests.

### Can I review a specific code block vs whole file?

Yes. Select the code you want to review, then right-click and choose **Review with kluster.ai**. You can review anything from a single function to an entire file.

### Can I review uncommitted changes?

Yes. In the kluster.ai extension sidebar, click **Instant Review** and select **Review uncommitted changes**. This reviews all staged and unstaged changes across your repository.

### What's the difference between instant actions and background reviews?

- **Instant actions**: On-demand reviews triggered by clicking a button or using a shortcut.
- **Ambient background reviews (Beta, Enterprise plan)**: Automatically review your code for issues and suggestions as you work, without requiring you to trigger anything. Enable it from the **Enabled Tools** section in [Options](/code-reviews/configuration/options/).