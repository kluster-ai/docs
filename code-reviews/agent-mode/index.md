---
title: Agent Mode
description: Use kluster.ai Code Reviews with AI coding assistants. Automatic reviews when AI generates code, plus on-demand reviews when you ask.
---

# Agent Mode

Agent Mode integrates kluster.ai directly into your AI-assisted coding workflow. Code is reviewed automatically as your AI assistant generates it, catching issues before they become problems.

## How Agent Mode works

When you use an AI coding assistant, kluster.ai monitors the code being generated and reviews it in real-time:

1. **You prompt**: Ask your AI assistant for what you need
2. **AI generates**: The assistant writes code
3. **kluster.ai reviews**: Code is automatically analyzed for issues
4. **Issues fixed**: Problems are caught and resolved immediately

No manual steps required—protection happens automatically in the background.

## Two types of reviews

Agent Mode offers two ways to review code:

<div class="grid cards" markdown>

-   :material-lightning-bolt: **Automatic Agent Reviews**

    ---

    Triggered automatically when AI generates or modifies code. Issues are caught in real-time as you work.

    [:octicons-arrow-right-24: Learn more](/code-reviews/agent-mode/automatic-agent-reviews/)

-   :material-account-voice: **Manual Agent Reviews**

    ---

    Triggered when you ask your AI to review existing code. Perfect for auditing files or security checks.

    [:octicons-arrow-right-24: Learn more](/code-reviews/agent-mode/manual-agent-reviews/)

</div>

## Supported tools

Agent Mode works with any AI coding assistant that supports MCP (Model Context Protocol):

### IDE Extensions

| IDE | Automatic Reviews | Manual Reviews |
|-----|-------------------|----------------|
| Cursor | Yes | Yes |
| VS Code (with Copilot) | Yes | Yes |
| Windsurf | Yes | Yes |
| Antigravity | Yes | Yes |

### CLI Tools

| Tool | Automatic Reviews | Manual Reviews |
|------|-------------------|----------------|
| Claude Code | Yes | Yes |
| Codex CLI | Yes | Yes |

## What gets reviewed

Agent Mode detects the same issue types as all kluster.ai reviews:

- **Intent**: Code doesn't match what you asked for
- **Security**: Vulnerabilities like SQL injection, XSS, hardcoded secrets
- **Logical**: Control flow errors, off-by-one bugs
- **Semantic**: Type mismatches, wrong variable usage
- **Performance**: Inefficient algorithms, N+1 queries
- **Quality**: Poor naming, excessive complexity
- **Knowledge**: Best practice violations

## Quick start

### Prerequisites

--8<-- 'text/quickstart-prerequisites.md'

### Try it now

1. Open your AI assistant (Cursor, Claude Code, etc.)
2. Ask it to generate some code:
   ```
   Create a function that fetches user data from an API
   ```
3. Watch kluster.ai automatically review the generated code
4. If issues are found, your AI will fix them automatically

## Examples

See Agent Mode in action with real-world case studies:

- **[Cursor: Firebase Authentication](/code-reviews/agent-mode/examples/cursor-firebase-nextjs/)** - How kluster.ai caught 4 critical issues during a Firebase migration
- **[VS Code: Secure Admin Endpoints](/code-reviews/agent-mode/examples/vscode-admin-endpoint/)** - Preventing hardcoded credentials in admin APIs

## Next steps

- **[Automatic agent reviews](/code-reviews/agent-mode/automatic-agent-reviews/)**: Deep dive into automatic reviews
- **[Manual agent reviews](/code-reviews/agent-mode/manual-agent-reviews/)**: Learn to trigger reviews on demand
- **[Configuration](/code-reviews/configuration/options/)**: Customize review sensitivity and scope
