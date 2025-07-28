---
title: Code tools reference
description: Reference guide for kluster.ai's Code verification MCP tools - verify AI-generated code quality and framework security with detailed parameters and response formats.
---

# Tools reference

The kluster.ai Code MCP server provides two verification tools for checking AI-generated code quality and security. These tools enable real-time code verification directly within your IDE through MCP integration.

This page documents the tool parameters and response formats you'll see when using these tools in Cursor, Claude Code, or any MCP-compatible client.

## Tool overview

The following tools are available through the kluster.ai Code MCP server:

| Tool | Purpose | Best For |
|:---|:---|:---|
| `kluster_bug_check_tool` | Verify code quality and detect bugs | Logic errors, security issues, performance problems |
| `kluster_frameworks_check_tool` | Verify frameworks and dependencies | Package security, outdated libraries, license compliance |

### Bug Check Tool

The bug check tool analyzes AI-generated code to detect bugs, security vulnerabilities, and quality issues.

???+ interface "Parameters"

    `code_diff` ++"string"++ <span class="required" markdown>++"required"++</span>

    Unified diff format showing the actual code changes.

    ---

    `user_requests` ++"string"++ <span class="required" markdown>++"required"++</span>

    Chronological sequence of user messages with current request marked as `>>> CURRENT REQUEST:`.

    ---

    `modified_files_path` ++"string"++ <span class="required" markdown>++"required"++</span>

    Full absolute paths of modified files separated by `;`.

### Frameworks Check Tool  

The frameworks check tool validates the security and compliance of packages and dependencies in your code.

???+ interface "Parameters"

    Uses the same parameters as Bug Check Tool.

## Response fields

All Code verification tools return the same response structure:

- **`isCodeCorrect`**: Boolean indicating if the code has issues.
- **`explanation`**: Summary of all issues found.
- **`issues`**: Array of detected problems with:
  - `type`: Issue category (intent, semantic, knowledge, performance, quality, logical, security)
  - `severity`: Impact level (critical, high, medium, low)
  - `priority`: Execution priority (P0-P5)
  - `description`: Brief issue summary
  - `explanation`: Detailed issue explanation
  - `actions`: Recommended fixes
- **`priority_instructions`**: Execution rules for addressing issues.
- **`agent_todo_list`**: Prioritized list of fixes to apply.

## Issue types

| Type | Description | Example |
|:---|:---|:---|
| `intent` | Code doesn't match user request | User asked for sorting, got filtering |
| `semantic` | Logic errors | Missing error handling |
| `knowledge` | Best practice violations | Not following conventions |
| `performance` | Performance issues | Inefficient algorithms |
| `quality` | Code quality problems | Poor naming, complexity |
| `logical` | Logic errors | Off-by-one errors |
| `security` | Security vulnerabilities | SQL injection risks |

## Priority system

- **P0-P1**: Intent issues (highest priority) - code doesn't match request
- **P2**: Critical severity - must fix immediately  
- **P3**: High severity - should fix soon
- **P4**: Medium severity - nice to fix
- **P5**: Low severity - optional improvements

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

## Next steps

- **Set up integrations**: Configure [IDE integrations](/verify/code/integrations/) to use these tools.
- **Quick start**: Follow the [quickstart guide](/verify/quickstart/code/) for immediate setup.