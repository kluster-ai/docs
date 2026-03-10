---
title: Bitbucket PR Reviews Setup
description: Connect the kluster.ai bot to Bitbucket to automatically review every pull request. Set up the integration with an API key in a few steps.
categories: PR Reviews
---

# Bitbucket

Connect the [kluster.ai](https://www.kluster.ai/){target=\_blank} bot to your Bitbucket repositories to automatically review every pull request. The setup uses an API key-based integration: provide a Bitbucket app password, select the repositories to monitor, and the bot begins reviewing your pull requests.

Once connected, the bot reviews every new pull request and every new commit pushed to an open pull request. No additional configuration is needed.

## Prerequisites

Before getting started, ensure you have:

- A [kluster.ai](https://platform.kluster.ai/signup){target=\_blank} account
- A Bitbucket account with **developer** access to the repositories you want to review
- A Bitbucket app password with the following permissions: **Repositories: Read**, **Pull requests: Read and Write**, and **Webhooks: Read and Write**. You can create one from **Bitbucket > Personal Settings > App passwords**

!!! tip "Use a dedicated service account"
    Reviews posted by the bot are attributed to the app password owner. To avoid reviews appearing under a personal account, create a dedicated Bitbucket account for kluster and generate the app password from that account.

## Connect Bitbucket

You can set up the Bitbucket integration from the [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} page on the kluster.ai platform.

1. Navigate to [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} in the kluster.ai platform. The PR Bot Installation page displays the available integrations, including Bitbucket.

    <!-- TODO: add proper image - PR Bot Installation page showing Bitbucket integration option -->
    ![PR Bot Installation page showing Bitbucket integration option](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-01.webp)

2. Click **Connect** next to Bitbucket. A dialog appears prompting you to enter your Bitbucket API credentials.

    <!-- TODO: add proper image - Bitbucket API credentials input dialog -->
    ![Dialog prompting for Bitbucket API credentials](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-02.webp)

3. Create an app password in Bitbucket if you have not already. Go to **Personal Settings > App passwords**, click **Create app password**, and enable the following permissions: **Repositories: Read**, **Pull requests: Read and Write**, and **Webhooks: Read and Write**. Copy the app password and paste it into the credentials field on the kluster.ai platform. Click **Connect**.

    <!-- TODO: add proper image - Bitbucket app password creation page -->
    ![Bitbucket app password creation page](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-03.webp)

4. After the credentials are validated, select the Bitbucket workspace or individual repositories you want the bot to monitor. Click **Confirm** to save your selection.

    <!-- TODO: add proper image - Repository selection screen for Bitbucket -->
    ![Repository selection screen showing available Bitbucket workspaces and repositories](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-04.webp)

5. The Bitbucket integration shows as **Connected** and is ready to review your pull requests automatically.

    <!-- TODO: add proper image - Bitbucket integration showing Connected status -->
    ![Bitbucket integration showing Connected status on kluster.ai](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-05.webp)

## What happens after setup

Once the integration is connected, the kluster.ai bot begins reviewing pull requests automatically. No further action is required.

### On new pull requests

When a pull request is opened, the bot analyzes all changes using ultra-deep analysis and posts its feedback:

- A **summary comment** titled **kluster.ai PR Review Summary**, which includes a description of the changes, the review result (**All Clear** or a list of detected issues), and a prior review warning if no IDE or CLI reviews were performed on the branch
- **Inline comments** on specific lines where issues were found. Each inline comment includes a severity badge (for example, `knowledge · critical`), a description, a detailed explanation, a recommended action, and quick issue actions to ignore the finding or copy an AI prompt for fixing it

### On new commits

When new commits are pushed to an open pull request, the bot re-runs its analysis on the updated changes and updates its comments accordingly.

### Prior review detection

If kluster was used during development on the branch (via IDE or CLI), the bot's summary comment includes review statistics, such as the number of reviews performed, issues found, and issues left unfixed. If no prior reviews were detected, the bot includes a note encouraging earlier use of kluster in the development workflow.

!!! note "Limited access"
    PR Reviews is in limited access. Not all users see the **PR Reviews** menu item in the platform sidebar. If you do not see it, [contact us](https://www.kluster.ai/contact){target=\_blank} for access.

## Next steps

- **[PR Reviews overview](/code-reviews/pr-reviews/)**: Learn how the bot works across all supported platforms.
- **[GitHub integration](/code-reviews/pr-reviews/github/)**: Connect the kluster.ai bot to GitHub via OAuth and the GitHub App.
- **[GitLab integration](/code-reviews/pr-reviews/gitlab/)**: Connect the kluster.ai bot to GitLab via API key.
- **[Review modes](/code-reviews/review-modes/)**: Understand all available review types.
