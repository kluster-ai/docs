---
title: GitLab PR Reviews Setup
description: Connect the kluster.ai bot to GitLab to automatically review every merge request. Set up the integration with an API key in a few steps.
categories: PR Reviews
---

# GitLab

Connect the [kluster.ai](https://www.kluster.ai/){target=\_blank} bot to your GitLab projects to automatically review every merge request. The setup uses an API key-based integration: provide a GitLab personal access token, select the projects to monitor, and the bot begins reviewing your merge requests.

Once connected, the bot reviews every new merge request and every new commit pushed to an open merge request. No additional configuration is needed.

## Prerequisites

Before getting started, ensure you have:

- A [kluster.ai](https://platform.kluster.ai/signup){target=\_blank} account
- A GitLab account with at least **Developer** access to the projects you want to review
- A GitLab personal access token with the `api` scope. You can generate one from **GitLab > User Settings > Access Tokens**

!!! tip "Use a dedicated service account"
    Reviews posted by the bot are attributed to the token owner. To avoid reviews appearing under a personal account, create a dedicated GitLab service account for kluster and generate the token from that account.

## Connect GitLab

You can set up the GitLab integration from the [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} page on the kluster.ai platform.

1. Navigate to [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} in the kluster.ai platform. The PR Bot Installation page displays the available integrations, including GitLab.

    <!-- TODO: add proper image - PR Bot Installation page showing GitLab integration option -->
    ![PR Bot Installation page showing GitLab integration option](/images/code-reviews/pr-reviews/pr-reviews-gitlab-01.webp)

2. Click **Connect** next to GitLab. A dialog appears prompting you to enter your GitLab API token.

    <!-- TODO: add proper image - GitLab API token input dialog -->
    ![Dialog prompting for GitLab API token](/images/code-reviews/pr-reviews/pr-reviews-gitlab-02.webp)

3. Generate a personal access token in GitLab if you have not already. Go to **User Settings > Access Tokens**, create a token with the `api` scope, and set an expiration date. Copy the token and paste it into the API token field on the kluster.ai platform. Click **Connect**.

    <!-- TODO: add proper image - GitLab personal access token creation page -->
    ![GitLab personal access token creation page](/images/code-reviews/pr-reviews/pr-reviews-gitlab-03.webp)

4. After the token is validated, select the GitLab group or individual projects you want the bot to monitor. Click **Confirm** to save your selection.

    <!-- TODO: add proper image - Project selection screen for GitLab -->
    ![Project selection screen showing available GitLab groups and projects](/images/code-reviews/pr-reviews/pr-reviews-gitlab-04.webp)

5. The GitLab integration shows as **Connected** and is ready to review your merge requests automatically.

    <!-- TODO: add proper image - GitLab integration showing Connected status -->
    ![GitLab integration showing Connected status on kluster.ai](/images/code-reviews/pr-reviews/pr-reviews-gitlab-05.webp)

!!! note "Group access tokens"
    If you are on GitLab Premium or Ultimate, you can use a group access token instead of a personal access token. Group access tokens are scoped to a specific group and automatically create a bot user for the reviews.

## What happens after setup

Once the integration is connected, the kluster.ai bot begins reviewing merge requests automatically. No further action is required.

### On new merge requests

When a merge request is opened, the bot analyzes all changes using ultra-deep analysis and posts its feedback:

- A **summary comment** titled **kluster.ai PR Review Summary**, which includes a description of the changes, the review result (**All Clear** or a list of detected issues), and a prior review warning if no IDE or CLI reviews were performed on the branch
- **Inline comments** on specific lines where issues were found. Each inline comment includes a severity badge (for example, `knowledge · critical`), a description, a detailed explanation, a recommended action, and quick issue actions to ignore the finding or copy an AI prompt for fixing it

### On new commits

When new commits are pushed to an open merge request, the bot re-runs its analysis on the updated changes and updates its comments accordingly.

### Prior review detection

If kluster was used during development on the branch (via IDE or CLI), the bot's summary comment includes review statistics, such as the number of reviews performed, issues found, and issues left unfixed. If no prior reviews were detected, the bot includes a note encouraging earlier use of kluster in the development workflow.

!!! note "Limited access"
    PR Reviews is in limited access. Not all users see the **PR Reviews** menu item in the platform sidebar. If you do not see it, [contact us](https://www.kluster.ai/contact){target=\_blank} for access.

## Next steps

- **[PR Reviews overview](/code-reviews/pr-reviews/)**: Learn how the bot works across all supported platforms.
- **[GitHub integration](/code-reviews/pr-reviews/github/)**: Connect the kluster.ai bot to GitHub via OAuth and the GitHub App.
- **[Bitbucket integration](/code-reviews/pr-reviews/bitbucket/)**: Connect the kluster.ai bot to Bitbucket via API key.
- **[Review modes](/code-reviews/review-modes/)**: Understand all available review types.
