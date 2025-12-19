---
title: Response Schema
description: Understand the response format from kluster.ai Code Reviews—issue structure, severity levels, priority system, and suggested fixes.
---

# Response Schema

All kluster.ai code review tools return the same response structure. This page documents the fields you'll see in review responses.

## Response fields

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

## Example response

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

## Issue types

| Type | Description | Example |
|------|-------------|---------|
| `intent` | Code doesn't match user request | Asked for sorting, got filtering |
| `semantic` | Meaning and type errors | Wrong variable type used |
| `knowledge` | Best practice violations | Not following conventions |
| `performance` | Performance issues | Inefficient algorithms |
| `quality` | Code quality problems | Poor naming, complexity |
| `logical` | Control flow errors | Off-by-one errors |
| `security` | Security vulnerabilities | SQL injection risks |

## Severity levels

| Level | Meaning | Action |
|-------|---------|--------|
| `critical` | Security vulnerability or breaking issue | Fix immediately |
| `high` | Significant bug or security concern | Fix before production |
| `medium` | Quality issue or minor bug | Should fix |
| `low` | Style or minor improvement | Optional fix |

## Priority system

Code review assigns priority levels to detected issues, helping you focus on the most critical problems first. The system automatically prioritizes based on issue type and severity.

| Priority | Meaning |
|----------|---------|
| **P0-P1** | Intent issues (highest priority) - code doesn't match request |
| **P2** | Critical severity - must fix immediately |
| **P3** | High severity - should fix soon |
| **P4** | Medium severity - nice to fix |
| **P5** | Low severity - optional improvements |

## Next steps

- **[MCP Tools Reference](/code-reviews/reference/mcp-tools/)**: Learn about tool parameters
- **[Configure settings](/code-reviews/configuration/options/)**: Customize what issues get flagged
- **[Agent Mode](/code-reviews/agent-mode/)**: Learn how reviews work with AI assistants
