---
title: MCP Tools Reference
description: Learn how kluster.ai Code MCP tools work: parameters, response formats, issue categories, and settings for real-time code reviews.
---

# MCP Tools Reference

The [kluster.ai](https://www.kluster.ai/){target=_blank} Code MCP server provides review tools for checking code quality and security. These tools enable real-time code reviews directly within your IDE through MCP integration.

## Available tools

- **`kluster_code_review_auto`**: Automatically reviews code quality and detects bugs, including logic errors, security issues, and performance problems. Triggers automatically when code is generated or modified. Best for real-time reviews during active coding sessions, analyzing changes in context of the full conversation and related files.
- **`kluster_dependency_validator`**: Validates the security and compliance of packages and dependencies. Triggers automatically before package installations or when package files are updated. Best for preventing vulnerable or non-compliant third-party libraries from entering your codebase before installation.
- **`kluster_code_review_manual`**: Manually reviews specific files when explicitly requested by the user (e.g., "review this file", "check for bugs"). Best for auditing existing code, reviewing specific modules, or getting fix recommendations for individual files.

This page documents the parameters and response formats you'll see when using these tools in Cursor, Claude Code, or any MCP-compatible client.

## Parameters

=== "Auto Review and Dependency Validator"

    These tools analyze code changes and dependencies to detect bugs, security vulnerabilities, and other quality issues.

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

## Response format

All code review tools return the same response structure. See the [Response Schema](/code-reviews/reference/response-schema/) for complete details.

## Next steps

- **[Response Schema](/code-reviews/reference/response-schema/)**: Understand the response format in detail
- **[Configure settings](/code-reviews/configuration/options/)**: Customize review behavior for your needs
- **[Installation](/code-reviews/get-started/installation/)**: Set up kluster.ai in your IDE
