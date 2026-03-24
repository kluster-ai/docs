---
title: External Knowledge Quickstart for Reviews
description: Connect external sources like Jira to kluster.ai so code reviews can verify your code against real project requirements and specifications.
categories: Basics, External Knowledge
---

# Quickstart

External Knowledge lets [kluster.ai](https://www.kluster.ai/){target=\_blank} Code Reviews pull context from the tools your team already uses. Instead of reviewing code in isolation, kluster uses requirements, specifications, and ticket details from connected sources to make its analysis more accurate and actionable.

## Connecting to external tools

1. **Connect an integration**: Go to the [External Knowledge](https://platform.kluster.ai/external-knowledge){target=\_blank} page on the kluster.ai platform and connect your tool. [Jira](/code-reviews/external-knowledge/jira/) is the available integration.

2. **Make sure the ticket ID is reachable by kluster**: How you do this depends on your tool:

    | Tool | What to do |
    |------|------------|
    | Cursor, VS Code, Windsurf, JetBrains, Antigravity | Check out a branch with the ticket ID in the name (e.g., `feat/KAN-2`) — kluster detects it automatically. |
    | Claude Code, Codex CLI | Include the ticket ID in your prompt (e.g., "...Ticket KAN-2"). |

3. **Ask your AI assistant to write code as usual**: kluster automatically includes the ticket requirements in the review and flags any gaps between the specification and the generated code.

!!! tip
    If your branch is named something generic like `main` and you do not reference a ticket in your prompt, kluster will not include any External Knowledge context. Always reference the ticket when it matters.

## Available integrations

<div class="grid cards" markdown>

-   :simple-jira: **Jira**

    ---

    Pull ticket requirements into code reviews to verify your implementation matches specifications.

    [:octicons-arrow-right-24: Set up Jira](/code-reviews/external-knowledge/jira/)

</div>
