---
title: GitHub PR Reviews Setup
description: Connect the kluster.ai bot to GitHub to automatically review every pull request. Authorize via OAuth and install the GitHub App in two steps.
categories: PR Reviews
---

# GitHub

Connect the [kluster.ai](https://www.kluster.ai/){target=\_blank} bot to your GitHub repositories to automatically review every pull request. The setup takes two steps: authorize with GitHub, then install the kluster.ai GitHub App on your organization or account.

Once connected, the bot reviews every new PR and every new commit pushed to an open PR. No additional configuration is needed.

!!! tip "Use PR Reviews as your last line of defense"
    For the best results, use kluster in your [IDE](/code-reviews/ide/) or [CLI](/code-reviews/cli/) during development. Catching issues early reduces review cycles and keeps PRs clean. PR Reviews then acts as a safety net for anything missed before merging.

## Prerequisites

Before getting started, ensure you have:

- A [kluster.ai](https://platform.kluster.ai/signup){target=\_blank} account.
- Admin access to the GitHub organization or account where you want to install the bot.

## Connect GitHub

You can set up the GitHub integration from the [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} page on the kluster.ai platform.

1. Navigate to [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} in the kluster.ai platform. The PR Bot Installation page displays the GitHub integration with two setup steps: **Authorize** and **Install**. First, click on **Authorize**. 

    ![PR Bot Installation page showing GitHub setup steps](/images/code-reviews/pr-reviews/pr-reviews-github-01.webp)

2. You are redirected to GitHub to sign in. Enter your GitHub credentials. Next, select the organization/account you want to target and click **Authorize**.

    ![GitHub OAuth page showing Authorize kluster.ai prompt](/images/code-reviews/pr-reviews/pr-reviews-github-02.webp)

3. You are redirected back to the kluster.ai platform. The authorization step shows as complete. Click **Install** next to **Install GitHub App**.

    ![kluster.ai platform showing completed authorization and Install button](/images/code-reviews/pr-reviews/pr-reviews-github-03.webp)

4. Select your organization or your personal account. Then, choose whether to grant access to **All repositories** or **Only select repositories**. Review the requested permissions and click **Install**.

    ![GitHub App installation page with organization and repository selection](/images/code-reviews/pr-reviews/pr-reviews-github-04.webp)

5. You are redirected back to the kluster.ai platform. The GitHub integration shows as **Installed** and is ready to review your pull requests automatically.

    ![GitHub integration showing Installed status on kluster.ai](/images/code-reviews/pr-reviews/pr-reviews-github-05.webp)

!!! tip "Limit access to specific repositories"
    If your organization has many repositories, select only the ones you want the bot to review. You can update repository access at any time from your GitHub organization settings under **Installed GitHub Apps**.

## What Happens After Setup

Once the GitHub App is installed, the kluster.ai bot begins reviewing pull requests automatically. No further action is required.

### On New Pull Requests

When a pull request is opened, the bot analyzes all changes using ultra-deep analysis and posts its feedback:

- A **summary comment** titled **kluster.ai PR Review Summary**, which includes a description of the changes (PR Summary), the review result (**All Clear** or a list of detected issues), and a prior review warning if no IDE or CLI reviews were performed on the branch.

    ![Example of a kluster.ai PR Review Summary comment on a GitHub pull request](/images/code-reviews/pr-reviews/pr-reviews-github-06.webp)

- **Inline comments** on specific lines where issues were found. Each inline comment includes a severity badge (for example, `knowledge · critical`), a description, a detailed explanation, a recommended action, and quick issue actions to ignore the finding or copy an AI prompt for fixing it.

    ![Example of a kluster.ai inline comment on a specific code line in a pull request](/images/code-reviews/pr-reviews/pr-reviews-github-07.webp)

    When clicking **Ignore issue** or **Copy AI prompt**, you are taken to the kluster.ai platform. From there, you can access the ignore menu to dismiss the finding or view the prompt needed to feed an AI agent for fixing the issue, which is automatically copied to your clipboard.

### On New Commits

When new commits are pushed to an open PR, the bot re-runs its analysis on the updated changes and updates its comments accordingly.

### Prior Review Detection

If kluster was used during development on the branch (via IDE or CLI), the bot's summary comment includes review statistics, such as the number of reviews performed, issues found, and issues left unfixed. If no prior reviews were detected, the bot includes a note encouraging earlier use of kluster in the development workflow.

## Next Steps

- **[PR Reviews overview](/code-reviews/pr-reviews/)**: Learn how the bot works across all supported platforms.
- **[GitLab integration](/code-reviews/pr-reviews/gitlab/)**: Connect the kluster.ai bot to GitLab via access token.
- **[Bitbucket integration](/code-reviews/pr-reviews/bitbucket/)**: Connect the kluster.ai bot to Bitbucket via API token.
- **[Review modes](/code-reviews/review-modes/)**: Understand all available review types.
