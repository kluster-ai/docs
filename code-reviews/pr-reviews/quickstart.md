---
title: PR Reviews Quickstart
description: Automatically review every pull request with the kluster.ai bot. Get summary reports and inline comments on GitHub, GitLab, Bitbucket, and Azure DevOps.
categories: PR Reviews
---

# PR Reviews

PR Reviews connects a [kluster.ai](https://www.kluster.ai/){target=\_blank} bot to your source control platform. The bot automatically reviews every pull request and each subsequent commit, posting detailed feedback directly in the PR. No manual steps are needed once the integration is set up.

The bot acts as a last line of defense. It catches issues that were missed during development, whether you used IDE reviews, CLI checks, or no kluster tooling at all. Every PR gets an ultra-deep analysis that examines your changes for bugs, security vulnerabilities, and quality problems before they reach your main branch.

!!! tip "Best used as a safety net"
    PR Reviews is most effective when combined with earlier review stages. Install the [kluster.ai extension](/code-reviews/get-started/installation/) in your IDE or set up [CLI hooks](/code-reviews/cli/git-hooks/) to catch issues while you code. The PR bot then confirms nothing was missed.

## How it works

Once installed, the kluster.ai bot triggers automatically in two situations:

- **New pull request**: When you open a PR, the bot analyzes all changes and posts its review.
- **New commits**: When you push additional commits to an open PR, the bot re-analyzes the updated changes.

Each review produces two types of feedback:

### Summary comment

The bot posts a top-level **kluster.ai PR Review Summary** comment on the pull request.

![Example of a kluster.ai PR Review Summary comment on a GitHub pull request](/images/code-reviews/pr-reviews/pr-reviews-github-06.webp)

This comment includes:

- **PR Summary**: A description of what the pull request changes.
- **Review result**: Either All Clear (no issues detected) or a list of issues found, grouped by severity.
- **Prior review warning**: If no IDE or CLI reviews were performed on the branch, the summary includes a warning encouraging you to use kluster earlier in your workflow.

### Inline comments

When the bot detects an issue, it posts an inline comment directly on the affected lines of code.

![Example of a kluster.ai inline comment on a specific code line in a pull request](/images/code-reviews/pr-reviews/pr-reviews-github-07.webp)

Each inline comment includes:

- **Severity badge**: The issue category and severity level (for example, `knowledge · critical` or `security · high`).
- **Description**: A summary of the issue.
- **Explanation**: A detailed technical analysis of why the code is problematic.
- **Recommended Action**: A concrete suggestion for how to fix the issue.
- **Issue Actions**: Quick actions to manage the finding.
    - **Ignore issue**: Dismiss the finding if it is not relevant.
    - **Copy AI prompt**: Copy a pre-built prompt to your clipboard that you can paste into an AI assistant to help fix the issue.

Every PR review runs at the **ultra-deep** analysis level automatically. This is a deeper analysis than the "deep" mode available in IDE and CLI reviews, optimized for pull request workflows where thoroughness matters more than speed. The analysis depth is not configurable.

!!! tip "Enforce reviews before merging"
    The kluster.ai bot posts its findings as pull request conversations. You can require all conversations to be resolved before a pull request can be merged. This turns the bot's inline comments into a gating mechanism that ensures detected issues are addressed.

## Get started

<div class="grid cards" markdown>

-   :simple-github: **GitHub**

    ---

    Connect via OAuth and install the kluster.ai GitHub App on your organization. Select all repositories or specific ones.

    [:octicons-arrow-right-24: Set up GitHub](/code-reviews/pr-reviews/github/)

-   :simple-gitlab: **GitLab**

    ---

    Connect using a GitLab personal access token with the `api` scope. Select the groups or projects to monitor.

    [:octicons-arrow-right-24: Set up GitLab](/code-reviews/pr-reviews/gitlab/)

-   :simple-bitbucket: **Bitbucket**

    ---

    Connect using a Bitbucket API token with repository and pull request permissions. Select the workspaces or repositories to monitor.

    [:octicons-arrow-right-24: Set up Bitbucket](/code-reviews/pr-reviews/bitbucket/)

-   :material-microsoft-azure-devops: **Azure DevOps**

    ---

    Connect using an Azure DevOps personal access token. An admin must first grant consent on the Azure site.

    [:octicons-arrow-right-24: Set up Azure DevOps](/code-reviews/pr-reviews/azure-devops/)

</div>