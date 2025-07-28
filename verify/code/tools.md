---
title: Code tools reference
description: Reference guide for kluster.ai's Code verification MCP tools - verify AI-generated code quality and framework security with detailed parameters and response formats.
---

# Tools reference

The [kluster.ai](https://www.kluster.ai/){target=_blank} Code MCP server provides two verification tools for checking AI-generated code quality and security. These tools enable real-time code verification directly within your IDE through MCP integration.

This page documents the tool parameters and response formats you'll see when using these tools in Cursor, Claude Code, or any MCP-compatible client.

## Tool overview

The kluster.ai Code MCP server offers two tools:

- **`kluster_bug_check_tool`**: Verifies code quality and detects bugs, including logic errors, security issues, and performance problems.
- **`kluster_packages_check_tool`**: Validates the security and compliance of packages and dependencies in your code.

Both tools share the same set of parameters.

### Parameters

These tools analyze AI-generated code and its dependencies to detect bugs, security vulnerabilities, and other quality issues.

???+ interface "Parameters"

    `code_diff` ++"string"++ <span class="required" markdown>++"required"++</span>

    Unified diff format showing the actual code changes.

    ---

    `user_requests` ++"string"++ <span class="required" markdown>++"required"++</span>

    Chronological sequence of user messages with current request marked as `>>> CURRENT REQUEST:`.

    ---

    `modified_files_path` ++"string"++ <span class="required" markdown>++"required"++</span>

    Full absolute paths of modified files separated by `;`.

## Response fields

All Code verification tools return the same response structure:

- **`isCodeCorrect`**: Boolean indicating if the code has issues.
- **`explanation`**: Summary of all issues found.
- **`issues`**: Array of detected problems with:
  - `type`: Issue category (intent, semantic, knowledge, performance, quality, logical, security).
  - `severity`: Impact level (critical, high, medium, low).
  - `priority`: Execution priority (P0-P5).
  - `description`: Brief issue summary.
  - `explanation`: Detailed issue explanation.
  - `actions`: Recommended fixes.
- **`priority_instructions`**: Execution rules for addressing issues.
- **`agent_todo_list`**: Prioritized list of fixes to apply.

## Issue types

| Type | Description | Example |
|:---:|:---:|:---:|
| `intent` | Code doesn't match user request | User asked for sorting, got filtering |
| `semantic` | Logic errors | Missing error handling |
| `knowledge` | Best practice violations | Not following conventions |
| `performance` | Performance issues | Inefficient algorithms |
| `quality` | Code quality problems | Poor naming, complexity |
| `logical` | Logic errors | Off-by-one errors |
| `security` | Security vulnerabilities | SQL injection risks |

## Priority system

- **P0-P1**: Intent issues (highest priority) - code doesn't match request.
- **P2**: Critical severity - must fix immediately.
- **P3**: High severity - should fix soon.
- **P4**: Medium severity - nice to fix.
- **P5**: Low severity - optional improvements.

## Response example

```json
{
  "isCodeCorrect": false,
  "explanation": "Found 3 issues. 1 critical issue needs immediate attention.",
  "issues": [
    {
      "type": "security",
      "severity": "critical",
      "priority": "P2",
      "description": "SQL injection vulnerability",
      "explanation": "User input is directly concatenated into SQL query without sanitization.",
      "actions": "Use parameterized queries or prepared statements."
    }
  ],
  "priority_instructions": "Fix P2 issues before deploying code.",
  "agent_todo_list": [
    "P2.1: Fix SQL injection vulnerability by using parameterized queries"
  ]
}
```

## Configuration settings

You can customize the Code verification behavior through the settings page in your IDE. This allows you to tailor the verification process to your specific needs, such as configuring severity levels for issue reporting, selecting which types of bug checks to perform, and enabling or disabling specific MCP tools to match your development workflow.

![Screenshot of Code verification settings interface showing severity levels and enabled tools configuration options](/images/verify/code/configuration-settings.webp)

### Severity Settings

Configure the minimum severity level for issue reporting:

- **Low, Medium, High, Critical** - Set your threshold based on team needs.
- The ideal setting depends on your use case. For example, a `Medium` level is a good starting point, but you might want to set it to `High` or `Critical` for production code.

### Enabled Tools

Choose which MCP tools are active:

- **Bug Check Tool** - For code quality verification.
- **Packages Check Tool** - For dependency security.

## Next steps

- **Set up integrations**: Configure [IDE integrations](/verify/code/integrations/){target=_blank} to use these tools.
- **Quick start**: Follow the [quickstart guide](/verify/quickstart/code/){target=_blank} for immediate setup.