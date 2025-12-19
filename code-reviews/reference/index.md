---
title: Reference
description: Technical reference documentation for kluster.ai Code Reviews—MCP tools, response schemas, and API details.
---

# Reference

Technical documentation for developers who want to understand kluster.ai Code Reviews at a deeper level. This section covers MCP tools, response formats, and integration details.

## MCP Tools

kluster.ai Code Reviews operates through MCP (Model Context Protocol) tools that integrate with AI assistants and IDEs.

<div class="grid cards" markdown>

-   :material-tools: **MCP Tools Reference**

    ---

    Complete documentation of all kluster.ai MCP tools:

    - `kluster_code_review_auto` - Automatic reviews
    - `kluster_code_review_manual` - On-demand reviews
    - `kluster_dependency_validator` - Dependency checking

    [:octicons-arrow-right-24: View tools reference](/code-reviews/reference/mcp-tools/)

</div>

## Response Schema

Understand the structure of kluster.ai review responses:

- Issue format and fields
- Severity levels (Critical, High, Medium, Low)
- Priority system (P0-P5)
- Suggested fix format

[:octicons-arrow-right-24: View response schema](/code-reviews/reference/response-schema/)

## Quick reference

### Tool selection guide

| Tool | Trigger | Use case |
|------|---------|----------|
| `kluster_code_review_auto` | Automatic when AI modifies code | Real-time protection during AI coding |
| `kluster_code_review_manual` | User asks AI or clicks in IDE | Auditing existing code |
| `kluster_dependency_validator` | Before package installation | Checking dependencies for vulnerabilities |

### Severity levels

| Level | Meaning | Action |
|-------|---------|--------|
| Critical | Security vulnerability or breaking issue | Fix immediately |
| High | Significant bug or security concern | Fix before production |
| Medium | Quality issue or minor bug | Should fix |
| Low | Style or minor improvement | Optional fix |

### Priority system

| Priority | Meaning |
|----------|---------|
| P0-P1 | Intent issues (highest) - code doesn't match request |
| P2 | Critical severity issues |
| P3 | High severity issues |
| P4 | Medium severity issues |
| P5 | Low severity issues |

## Additional resources

- **[Configuration options](/code-reviews/configuration/options/)**: Customize review behavior
- **[Custom rules](/code-reviews/configuration/rules/)**: Define project-specific standards
- **[FAQ](/code-reviews/faq/)**: Common questions answered
