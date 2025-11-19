---
title: Quick Start
description: Learn how to use Code Reviews in your daily workflow. Trigger reviews automatically or manually, interpret results, and apply fixes.
---

# Quick Start

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin-bottom: 2rem;">
    <iframe src="https://www.youtube.com/embed/V0VsqgTza8" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Now that you have [installed the extension](/code-reviews/installation/), this guide will show you how to use Code Reviews in your daily workflow.

**Code Reviews acts as your "Trust Layer" for AI-generated code.** It sits between your AI assistant and your codebase, verifying every line of generated code in real-time to ensure it's secure, correct, and high-quality before you accept it.

## 1. Auto Review (Default)

The most powerful way to use Code Reviews is to let it work in the background. You don't need to change how you work—just ask your AI assistant for what you need.

**How it works:**
1.  **You Prompt**: Ask your AI assistant to generate code (e.g., "Create a user login endpoint").
2.  **AI Generates**: The AI writes the code.
3.  **Kluster Verifies**: Code Reviews automatically analyzes the diff in real-time.
4.  **Feedback Loop**: If issues are found, Kluster provides immediate feedback to the AI to correct them.

### Example: The Feedback Loop in Action

Imagine you ask your AI to create an API endpoint. If the AI generates code that misses a critical security check (like an unprotected database query), Kluster intervenes.

=== "Cursor"

    In Cursor, you'll see the review appear directly in the chat. Kluster flags the issue (e.g., "Unprotected API Endpoint") and provides a fix.

    ![Cursor Auto Review - Unprotected API](/images/code-reviews/code/examples/cursor/example-cursor-2.webp)
    *Code Reviews detects the missing authentication and guides the AI to fix it.*

=== "Claude Code"

    In the terminal, Claude Code displays the review results immediately.

    ![Claude Code Auto Review - Unprotected API](/images/code-reviews/quick-start/claude-auto-review-placeholder.png)
    *Code Reviews warns about the insecure endpoint, preventing the vulnerability from entering your codebase.*

**The Result:**
Instead of accepting insecure code, the AI receives the feedback and regenerates the code with the necessary protection (e.g., adding session validation). You get the speed of AI with the security of expert review.

## 2. Manual Review

Sometimes you have existing code that hasn't been reviewed yet. For example, you might have 7 files in your project that were written before you installed Kluster.

### How to trigger

=== "Cursor / VS Code"

    1.  Open the **Chat** (Cmd+L / Ctrl+L).
    2.  Ask the AI to review the files:
        ```
        @Code Reviews please review these 7 files for security issues
        ```
    3.  The agent will scan the specified files and report back with a list of issues and fixes.

=== "Claude Code"

    1.  Run Claude Code in your terminal.
    2.  Use the `/review` command or ask naturally:
        ```
        /review src/components/*.tsx
        ```
    3.  Claude will use the `kluster_code_review_manual` tool to analyze the files.

## 3. Interpret the results

Whether triggered automatically or manually, the output always follows the same structure:

*   **Status**: `isCodeCorrect` (True/False)
*   **Issues**: A list of problems found, categorized by type (Intent, Security, Logic, etc.).
*   **Agent Todo List**: A prioritized set of instructions for the AI to fix the code.

!!! tip "Agent Todo List"
    The **Agent Todo List** is the key to fixing issues fast. You don't need to implement the fixes manually—just tell the AI to "Execute the Todo List," and it will apply the corrections for you.

## Next steps

*   **[Tools Reference](/code-reviews/tools/)**: Deep dive into all issue types and parameters.
*   **[Examples](/code-reviews/examples/)**: See more real-world scenarios.
