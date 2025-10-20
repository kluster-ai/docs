---
title: Code MCP Tools for Code Reviews 
description: Learn how kluster.ai Code MCP tools work: parameters, response formats, issue categories, and settings for real-time code reviews.
---

# Tools reference

The [kluster.ai](https://www.kluster.ai/){target=_blank} Code MCP server provides review tools for checking AI-generated code quality and security. These tools enable real-time code reviews directly within your IDE through MCP integration.

It includes:

- **`kluster_code_review_auto`**: Automatically reviews code quality and detects bugs, including logic errors, security issues, and performance problems. Triggers automatically when code is generated or modified. Best for real-time reviews during active coding sessions, analyzing changes in context of the full conversation and related files.
- **`kluster_dependency_validator`**: Validates the security and compliance of packages and dependencies. Triggers automatically before package installations or when package files are updated. Best for preventing vulnerable or non-compliant third-party libraries from entering your codebase before installation.
- **`kluster_code_review_manual`**: Manually reviews specific files when explicitly requested by the user (e.g., "review this file", "check for bugs"). Best for auditing existing code, reviewing specific modules, or getting fix recommendations for individual files.

This page documents the parameters and response formats you'll see when using these tools in Cursor, Claude Code, or any MCP-compatible client.

## Parameters

=== "Auto Review and Dependency Validator"

    These tools analyze AI-generated code and dependencies to detect bugs, security vulnerabilities, and other quality issues.

    ???+ interface "Parameters"

        `code_diff` ++"string"++ <span class="required" markdown>++"required"++</span>

        Unified diff format showing the actual changes (additions and subtractions) made to files. Use standard diff format with `--- filename` and `+++ filename` headers, followed by `@@ line numbers @@`, and `+` for additions, `-` for deletions. In MCP environments, this is often auto-extracted from IDE history.

        ---

        `user_requests` ++"string"++ <span class="required" markdown>++"required"++</span>

        A chronological sequence of all user messages and requests in this conversation thread, with the current request (that triggered this assistant turn) clearly marked. Format: Previous requests as numbered list, then current request marked with `>>> CURRENT REQUEST: [request text]`. In MCP environments, this is often auto-extracted from conversation history.

        ---

        `modified_files_path` ++"string"++ <span class="required" markdown>++"required"++</span>

        Full absolute paths of modified files separated by `;`.

        ---

        `chat_id` ++"string"++ <span class="optional" markdown>++"optional"++</span>

        Session identifier returned by previous tool calls. Used to maintain context across multiple review requests.

=== "Manual Review"

    The manual review tool is triggered only when explicitly requested by the user.

    ???+ interface "Parameters"

        `user_requests` ++"string"++ <span class="required" markdown>++"required"++</span>

        Chronological sequence of user messages with current request marked as `>>> CURRENT REQUEST:`. Unlike auto review, this parameter is NOT auto-extracted in MCP environments and must be explicitly provided.

        ---

        `modified_file_path` ++"string"++ <span class="required" markdown>++"required"++</span>

        Full absolute path of the single file to review. This tool can only check one file per call.
        
        ---

        `need_fixes` ++"boolean"++ <span class="required" markdown>++"required"++</span>

        Set to `true` if user requested fixes, `false` if only requesting issue detection.

        ---

        `chat_id` ++"string"++ <span class="optional" markdown>++"optional"++</span>

        Session identifier returned by previous tool calls. Used to maintain context across multiple review requests.

## Response fields

All code review tools return the same response structure:

- **`isCodeCorrect`**: Boolean indicating if the code has issues.
- **`explanation`**: Summary of all issues found.
- **`issues`**: Array of detected problems with:
  - **`type`**: Issue category (intent, semantic, knowledge, performance, quality, logical, security).
  - **`severity`**: Impact level (critical, high, medium, low).
  - **`priority`**: Execution priority (P0-P5).
  - **`description`**: Brief issue summary.
  - **`explanation`**: Detailed issue explanation.
  - **`actions`**: Recommended fixes.
- **`priority_instructions`**: Execution rules for addressing issues.
- **`agent_todo_list`**: Prioritized list of fixes to apply.
- **`chat_id`**: Session identifier for maintaining context across requests.

### Example response

```json
{
    "isCodeCorrect": false,
    "explanation": "Found 1 issue. 1 critical issue needs immediate attention.\n\nTODO:\n1. [CRITICAL] The implementation introduces a critical SQL injection vulnerability.",
    "issues": [
        {
            "type": "intent",
            "severity": "critical",
            "priority": "P0",
            "description": "The implementation introduces a critical SQL injection vulnerability, which is an unacceptable security risk.",
            "explanation": "The code constructs an SQL query using string concatenation with user input, which is the classic pattern for SQL injection. A function designed for database interaction should use parameterized queries.",
            "actions": "Use parameterized queries or prepared statements to safely handle user input. For example: db.query('SELECT * FROM users WHERE id = ?', [userId])"
        }
    ],
    "priority_instructions": "**PRIORITY EXECUTION RULES:**\n1. **INTENT Critical/High (P0-P1) get special priority**\n2. **All other issues sorted by severity** - Critical (P2) > High (P3) > Medium (P4) > Low (P5)\n3. **Never let lower priority issues override higher priority changes**",
    "agent_todo_list": [
        "**EXECUTE IN THIS EXACT ORDER:**",
        "",
        "**Priority P0 - INTENT CRITICAL (HIGHEST PRIORITY):**",
        "P0.1: The implementation introduces a critical SQL injection vulnerability - Use parameterized queries or prepared statements."
    ],
    "chat_id": "i8ct930591"
}
```

## Priority system

Code review assigns priority levels to detected issues, helping you focus on the most critical problems first. The system automatically prioritizes based on issue type and severity.

- **P0-P1**: Intent issues (highest priority) - code doesn't match request.
- **P2**: Critical severity - must fix immediately.
- **P3**: High severity - should fix soon.
- **P4**: Medium severity - nice to fix.
- **P5**: Low severity - optional improvements.


## Next steps

- **[Configure settings](/code-reviews/configuration/)**: Customize review behavior for your needs.
- **[Set up integrations](/code-reviews/quickstart/)**: Configure IDE integrations to use these tools.
- **[Get started](/code-reviews/quickstart/)**: Follow the quickstart guide for immediate setup.