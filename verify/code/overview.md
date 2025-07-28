---
title: Code by Verify
description: Learn how to use kluster.ai code verification to detect bugs and security issues in AI-generated code using kluster.ai's specialized Verify.
---

# Code by Verify

Code is one of the features offered by Verify, providing specialized tools to identify bugs in AI-generated code and verify the security of frameworks and libraries.

With Code verification, you can ship AI-generated code confidently, knowing potential issues are caught before they reach production.

The service works seamlessly with AI coding assistants in your IDE, analyzing code changes in real-time as they're generated.

## How Code works

The service evaluates AI-generated code by:

1. Analyzing the code changes in diff format
2. Understanding the user's original request
3. Detecting various types of issues (bugs, security vulnerabilities, performance problems)
4. Providing detailed explanations and actionable fixes

The service evaluates code to identify issues, with the following fields:

- `isCodeCorrect=true/false`: Indicates whether the code has issues
- `issues`: Array of detected problems with type, severity, and priority
- `explanation`: Summary of all issues found
- `agent_todo_list`: Prioritized list of fixes to apply

## Configuration options

Code verification offers flexible configuration to match your development workflow:

- **Severity settings** - Configure minimum severity level for reporting (Low to Critical)
- **Bug check types** - Select which issue types to check: Semantic, Security, Quality, Intent, Knowledge, Logical, Performance
- **Enabled tools** - Choose which MCP tools are active (Bug Check Tool, Packages Check Tool)

These settings can be configured directly in your IDE integration.

## When to use Code

The Code service is ideal for scenarios where you need:

- **AI code validation**: Verify AI-generated code before production use
- **Security scanning**: Detect potential vulnerabilities in generated code
- **Quality assurance**: Ensure code follows best practices
- **Dependency checking**: Validate that new packages are secure and up-to-date

## How to integrate Code

Code is currently available through MCP (Model Context Protocol) integrations:

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Tools__

    ---

    Use Code verification tools directly in your IDE through MCP integration.

    [:octicons-arrow-right-24: View tools reference](/verify/code/tools/){target=\_blank}

-   <span class="badge integration">Integration</span> __Integrations__

    ---

    Set up Code verification in Cursor or Claude Code using MCP.

    [:octicons-arrow-right-24: Setup guide](/verify/code/integrations/){target=\_blank}

</div>

## Additional resources

- **Quick Start**: Get [Code verification running in minutes](/verify/quickstart/code/){target=\_blank}.
- **MCP Tools**: Explore the [detailed tools reference](/verify/code/tools/){target=\_blank}.