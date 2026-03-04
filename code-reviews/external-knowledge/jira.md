---
title: Jira Integration for Code Reviews
description: Connect Jira to kluster.ai to review code against ticket requirements. Set up Jira Cloud or self-hosted Jira and learn how ticket context flows into reviews.
---

# Jira integration

The Jira integration connects your Jira project to [kluster.ai](https://www.kluster.ai/){target=\_blank} Code Reviews, allowing kluster to use ticket details as context during code reviews. When connected, kluster can verify whether your code matches the requirements defined in a Jira ticket, catching gaps between the specification and the implementation.

For example, if a Jira ticket specifies that a function must accept command-line arguments and support multiple algorithms, kluster flags missing requirements in your code. This turns code review into a requirements-aware process rather than a purely syntactic or security-focused check.

## Connect Jira

You can connect Jira from the [External Knowledge](https://platform.kluster.ai/external-knowledge){target=\_blank} page on the kluster.ai platform. The setup process depends on whether you use cloud-hosted Jira or a self-hosted (IT-managed) instance.

### Jira Cloud (OAuth)

For Jira Cloud instances, kluster uses an OAuth wizard for authentication.

1. Navigate to [External Knowledge](https://platform.kluster.ai/external-knowledge){target=\_blank} in the kluster.ai platform. Jira appears as an available source.

    ![External Knowledge page showing Jira as a source option](/images/code-reviews/external-knowledge/external-knowledge-jira-01.webp)

2. Click **Connect** next to Jira. This launches the Jira OAuth authorization wizard.

    ![Jira OAuth wizard connection notification](/images/code-reviews/external-knowledge/external-knowledge-jira-02.webp)

3. Accept the connection notification in the wizard to grant kluster access to your Jira instance.

4. Once the authorization completes, the Jira integration status changes to **Connected**. A list of Jira projects from your instance appears. Enable or disable specific projects to control which ticket data kluster can access during code reviews.

    ![Jira integration showing as Connected, select project](/images/code-reviews/external-knowledge/external-knowledge-jira-03.webp)

!!! tip "Restrict access to sensitive projects"
    If your Jira instance contains internal security, IT, or HR projects, disable them from the project list. This prevents their ticket details from being included in code review context.

### Self-hosted Jira (API token)

For self-hosted or IT-managed Jira instances that do not support OAuth, you can connect using an API token instead.

1. Navigate to [External Knowledge](https://platform.kluster.ai/external-knowledge){target=\_blank} in the kluster.ai platform.

2. Click the **Connect Jira** dropdown, and select **Connect via API token**.

    ![Connecting via API token](/images/code-reviews/external-knowledge/external-knowledge-jira-04.webp)

3. Fill in the self-hosted or IT-managed Jira instance details. Click **Connect** to complete the setup.

    ![Self-hosted Jira API token connection screen](/images/code-reviews/external-knowledge/external-knowledge-jira-05.webp)

## How Jira context flows into reviews

Once connected, kluster identifies Jira tickets by their **ticket ID** (e.g., `KAN-2`). The ticket context is automatically included in a code review when any of the following conditions are met:

- **Branch name contains the ticket ID**: for example, a branch named `feature/KAN-2` triggers kluster to pull in the requirements from ticket `KAN-2`.
- **Ticket ID is mentioned in the chat prompt**: including the ticket ID in your message to the AI assistant (e.g., "Create a Python script that prints Pi (Ticket KAN-2)") links the review to that ticket.

How kluster detects the ticket depends on your tool:

| Tool | How the ticket is detected |
|------|---------------------------|
| Cursor, VS Code, Windsurf | Branch name is detected automatically — check out a branch like `feat/KAN-2` and kluster picks it up. |
| Claude Code, Codex CLI | Branch is not detected automatically — include the ticket ID in your prompt or paste the ticket link. |

!!! note "When Jira context is not included"
    If your branch has a generic name like `main` or `develop` and the ticket ID is not mentioned anywhere in the prompt, kluster does not include Jira context in the review. To ensure ticket requirements are checked, reference the ticket ID explicitly in the branch name or in the prompt.

Once kluster starts a code review process, it will check the intent of the Jira ticket associated with the request. It will then suggest the intent of the Jira ticket to the AI tool being used, so that it is automatically applied.

## Example workflow

The following example illustrates how kluster uses Jira ticket context to validate code against requirements.

Assume a Jira ticket **KAN-2** specifies the following requirements:

```text
- Output must be formatted as `The PI: {number}`.
- At least two methods of calculating Pi must be implemented.
- The script must accept command-line arguments to select the algorithm.
```

A developer creates a branch named `feat/KAN-2` and asks their AI assistant (Claude in this example) to "write code that returns pi in Python." 

--8<-- 'code/code-reviews/external-knowledge/jira/claude-code-example-1.md'

The AI generates a basic script that prints Pi using a single method.

Because kluster has access to the Jira ticket, it compares the generated code against the ticket requirements and flags the following gaps:

- The output format does not match `The PI: {number}`.
- Only one calculation method is implemented instead of two.
- No argument parsing is included.

kluster then asks the developer whether to fix the code to comply with the Jira ticket requirements. This prevents under-implemented features from being committed without review.

--8<-- 'code/code-reviews/external-knowledge/jira/claude-code-example-2.md'

After the AI coding agent finishes the implementation, kluster performs a follow-up review to verify that the code matches the intent from the Jira ticket requirements. If it does, kluster states that no issues were found in the code.

## Next steps

- **[Configuration options](/code-reviews/configuration/options/)**: Adjust sensitivity, analysis depth, and enabled tools.
- **[Custom rules](/code-reviews/configuration/rules/)**: Define additional project-specific review standards.
- **[Automatic reviews quickstart](/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/quickstart/)**: Set up real-time reviews for AI-generated code.
