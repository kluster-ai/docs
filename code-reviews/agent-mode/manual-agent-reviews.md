---
title: Manual Agent Reviews
description: Ask your AI assistant to review existing code on demand. Audit files, check for security issues, or verify code quality.
---

# Manual Agent Reviews

Manual agent reviews let you ask your AI assistant to review existing code—not just newly generated code. This is useful for auditing files, checking security, or verifying code you didn't write.

## How it works

Instead of waiting for the AI to generate code, you explicitly ask it to review something:

1. **You ask**: Tell your AI to review a file or code block
2. **AI triggers review**: The assistant calls kluster.ai's manual review tool
3. **Analysis runs**: kluster.ai analyzes the code
4. **Results returned**: Issues are reported with suggested fixes
5. **AI can fix**: Your assistant can apply the fixes automatically

## When to use manual reviews

| Scenario | Example prompt |
|----------|----------------|
| **Audit existing code** | "Review `src/auth/login.ts` for issues" |
| **Security check** | "Check this file for security vulnerabilities" |
| **Code you inherited** | "Review the utils folder for bugs" |
| **Pre-commit verification** | "Review my changes before I commit" |
| **Learning from codebase** | "Review this file and explain any problems" |

## Example prompts

Here are effective ways to ask your AI for a manual review:

### Basic review
```
Review this file for issues
```

```
Check src/api/users.ts for bugs
```

### Security-focused
```
Review this authentication code for security vulnerabilities
```

```
Check this endpoint for SQL injection or other security issues
```

### Specific concerns
```
Review this function for performance problems
```

```
Check this code for proper error handling
```

### With fix requests
```
Review this file and fix any issues you find
```

```
Check src/utils.js for bugs and apply the fixes
```

## What happens during a manual review

When you ask for a manual review, your AI assistant:

1. Reads the file or code you specified
2. Calls the `kluster_code_review_manual` tool
3. Sends the code to kluster.ai for analysis
4. Receives a detailed report of issues found
5. Presents the results to you
6. Optionally applies fixes if you requested them

### Example interaction

**You**: "Review src/api/admin.ts for security issues"

**AI Assistant**: "I'll review that file for security issues."

*[Calls kluster.ai manual review]*

**AI Assistant**: "kluster.ai found 2 issues:

1. **Critical - Hardcoded API key** (line 15): The admin API key is hardcoded in the source file. Move this to an environment variable.

2. **High - Missing rate limiting** (line 42): The admin endpoint has no rate limiting, making it vulnerable to brute force attacks.

Would you like me to fix these issues?"

## Comparison with automatic reviews

| Aspect | Automatic Reviews | Manual Reviews |
|--------|-------------------|----------------|
| **Trigger** | AI generates code | You ask explicitly |
| **Scope** | New/modified code only | Any existing code |
| **Use case** | Real-time protection | On-demand auditing |
| **Requires prompt** | No | Yes |

## Tips for effective manual reviews

### Be specific when needed
Instead of "review everything", target specific files or concerns:
```
Review the authentication middleware for security issues
```

### Combine with fixes
Ask for fixes in the same prompt to save time:
```
Review src/database.ts and fix any SQL injection vulnerabilities
```

### Review before committing
Make it a habit to ask for a review before major commits:
```
Review all my uncommitted changes for issues
```

### Use for code you didn't write
Manual reviews are great for understanding inherited code:
```
Review this legacy payment module and explain any problems
```

## Compatible with

Manual agent reviews work with all Agent Mode compatible platforms:

- **IDE Extensions**: Cursor, VS Code, Windsurf, Antigravity
- **CLI Tools**: Claude Code, Codex CLI

## Next steps

- **[Automatic agent reviews](/code-reviews/agent-mode/automatic-agent-reviews/)**: Learn about automatic real-time reviews
- **[Configuration](/code-reviews/configuration/options/)**: Customize what issues get flagged
- **[Examples](/code-reviews/agent-mode/examples/cursor-firebase-nextjs/)**: See Agent Mode in action
