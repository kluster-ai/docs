---
title: Verify Code — Overview
description: Learn how to use kluster.ai’s Verify Code to validate AI-generated code in real time—detecting bugs, security issues, and quality problems so you can ship safely.
---

# Verify Code

LLMs can produce non-factual or irrelevant output (hallucinations). In software development, that translates into risky code changes and extra engineering overhead:

- Difficulty programmatically trusting AI-generated code.
- Increased complexity in error handling and QA.
- Potential for cascading failures in chained AI operations.
- Manual review cycles that slow development and deployment.

**Verify Code** is part of kluster.ai trust layer, and its goal is to validate AI-generated code in real time so you can deploy AI at scale where accuracy and security matter most.

With Verify Code, you can ship confidently: potential issues are surfaced (and can be auto-corrected) before they reach production. The service works seamlessly with AI coding assistants in your IDE (Cursor, VS Code, Claude Code and others), analyzing diffs as code is generated.

## How Verify Code works

Verify Code analyzes AI-generated code (typically in diff format) and returns a structured assessment with actionable fixes. It combines the following MCP tools:

--8<-- 'text/verify/code-tools.md'

The service responds with the following fields:

- **`isCodeCorrect`**: Indicates whether the code has issues.
- **`issues`**: Array of detected problems with type, severity, and priority.
- **`explanation`**: Summary of all issues found.
- **`agent_todo_list`**: Prioritized list of fixes to apply.

## Key features

- **Real-time code review**: Monitors AI-generated code as it’s written.
- **Comprehensive issue detection**: Analyzes 7 issue types — *Semantic, Intent, Logical, Security, Knowledge, Performance,* and *Quality*.
- **Customizable sensitivity levels**: Configure detection sensitivity from *Low* to *Critical*.
- **Dual analysis tools**: Real-time **Code Review** and **Dependency Analysis** for complete coverage.
- **Automatic correction**: AI incorporates feedback to fix issues immediately.

## Configuration options

Tailor Verify Code to your workflow:

- **Sensitivity settings**: Set minimum sensitivity to report (*Low → Critical*).
- **Bug check types**: Select which issue types to check: *Semantic, Security, Quality, Intent, Knowledge, Logical, Performance*.
- **Enabled tools**: Choose which MCP tools are active (bug check tool, packages check tool).

These settings can be configured directly in your IDE integration.

## Target applications and use cases

- AI coding assistants and IDE integrations.
- Automated code review pipelines.
- CI/CD security scanning for AI-generated code.
- Development workflow automation.
- Code quality assurance systems.

## When to use Verify Code

- **AI code validation**: Verify AI-generated code before production use.
- **Security scanning**: Detect potential vulnerabilities early.
- **Quality assurance**: Enforce best practices automatically.
- **Dependency checking**: Validate that new packages are secure and up-to-date.

## Integrations

Verify Code is available as a native extension for IDEs such as Cursor, VS Code and Claude Code, and through MCP-compatible IDEs such as Windsurf, Kilo Code and others.

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Cursor, VS Code and Claude Code__

    ---

    Enable real-time analysis during development by setting up Verify Code with Cursor, VS Code and Claude Code.

    [:octicons-arrow-right-24: Code with Cursor](/verify/integrations/ide#setup-instructions)

-   <span class="badge guide">Guide</span> __Other MCP-compatible IDEs__

    ---

    Integrate Verify Code with other MCP-compatible IDEs, including Windsurf and Kilo Code.

    [:octicons-arrow-right-24: Setup guide](/verify/integrations/mcp#setup-by-ide)

-   <span class="badge guide">Guide</span> __Tools reference__

    ---

    Use Verify Code tools directly in your IDE via MCP.

    [:octicons-arrow-right-24: View tools reference](/verify/tools/)


</div>

## Additional resources

- **[Get started](/verify/quickstart/)**: Run Verify Code in minutes.
- **[See real examples](/verify/examples/cursor-firebase-nextjs/)**: Walk through a complete Firebase migration case study.
