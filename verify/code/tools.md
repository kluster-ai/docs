---
title: Tools
description: Detailed reference for kluster.ai Code verification MCP tools including parameters, responses, and issue types.
---

# Tools

Code verification provides two specialized MCP tools for checking AI-generated code.

## Bug Check Tool

Performs comprehensive code security, quality, and compliance verification.

### Tool Name
`kluster_bug_check_tool`

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code_diff` | string | Yes | Unified diff format showing code changes |
| `user_requests` | string | Yes | User messages with current request marked as `>>> CURRENT REQUEST:` |
| `modified_files_path` | string | Yes | Absolute paths of modified files separated by `;` |

### Response Format

```json
{
  "isCodeCorrect": boolean,
  "explanation": "Summary of issues found",
  "issues": [...],
  "priority_instructions": "Execution rules for fixes",
  "agent_todo_list": ["Ordered list of fixes"]
}
```

### Issue Types

| Type | Description |
|------|-------------|
| `intent` | Code doesn't match user's request |
| `semantic` | Logic errors (e.g., missing error handling) |
| `knowledge` | Best practice violations |
| `performance` | Performance issues |
| `quality` | Code quality problems |
| `logical` | Logic errors |
| `security` | Security vulnerabilities |

### Priority Levels

- **P0-P1**: Intent issues (highest priority)
- **P2**: Critical severity issues
- **P3**: High severity issues
- **P4**: Medium severity issues
- **P5**: Low severity issues

## Frameworks Check Tool

Validates security and compliance of packages and dependencies.

### Tool Name
`kluster_frameworks_check_tool`

### Parameters

Same as Bug Check Tool.

### Focus Areas

- Outdated dependencies
- Security vulnerabilities in packages
- License compliance issues
- Malicious package detection

### Response Format

Same structure as Bug Check Tool, focused on dependency-specific issues.