---
title: Bitbucket PR Reviews Setup
description: Connect the kluster.ai bot to Bitbucket to automatically review every pull request. Set up the integration with an API token in a few steps.
categories: PR Reviews
---

# Bitbucket

Connect the [kluster.ai](https://www.kluster.ai/){target=\_blank} bot to your Bitbucket repositories to automatically review every pull request. The setup uses a token-based integration that requires providing a Bitbucket API token and selecting the repositories to monitor before the bot begins reviewing your pull requests.

Once connected, the bot reviews every new pull request and every new commit pushed to an open pull request. No additional configuration is needed.

!!! tip "Use PR Reviews as your last line of defense"
    For the best results, use kluster in your [IDE](/code-reviews/ide-reviews/ai-generated-code/automatic-reviews/) or [CLI](/code-reviews/cli/quickstart/) during development. Catching issues early reduces review cycles and keeps pull requests clean. PR Reviews then acts as a safety net for anything missed before merging.

## Prerequisites

Before getting started, ensure you have:

- A [kluster.ai](https://platform.kluster.ai/signup){target=\_blank} account.
- A Bitbucket account with **developer** access to the repositories you want to review.
- A Bitbucket API token. See [Create an API token](#create-an-api-token) for instructions.

## Create an API token

The kluster.ai bot requires a Bitbucket API token to access your repositories and post review comments. Tokens are created through your Atlassian account settings.

!!! tip "Use a dedicated service account"
    Reviews posted by the bot are attributed to the API token owner. To avoid reviews appearing under a personal account, create a dedicated Atlassian account for kluster and generate the API token from that account.

1. Sign in to the Atlassian account that will be associated with the kluster.ai bot reviews.
2. Open the [API tokens](https://id.atlassian.com/manage-profile/security/api-tokens){target=\_blank} page in your Atlassian account settings.
3. Click **Create token**. Enter a descriptive label (for example, "kluster.ai PR Reviews") and choose an expiration date that aligns with your security policy.
4. When prompted to choose a product, select **Bitbucket**.
5. Grant the token the scopes listed in the following table. All scopes are required for the bot to analyze code, post review comments, and manage webhooks:

    |    Category    |                    Scope                     |                 Description                 |
    |:--------------:|:--------------------------------------------:|:-------------------------------------------:|
    | Account & User |        <pre>```read:account```</pre>         |            View users' profiles.            |
    | Account & User |     <pre>```read:user:bitbucket```</pre>     |               View user info.               |
    |   Repository   |  <pre>```read:repository:bitbucket```</pre>  |           View your repositories.           |
    |   Repository   | <pre>```write:repository:bitbucket```</pre>  |          Modify your repositories.          |
    | Pull Requests  | <pre>```read:pullrequest:bitbucket```</pre>  |          View your pull requests.           |
    | Pull Requests  | <pre>```write:pullrequest:bitbucket```</pre> |         Modify your pull requests.          |
    |     Issues     |    <pre>```read:issue:bitbucket```</pre>     |              View your issues.              |
    |     Issues     |    <pre>```write:issue:bitbucket```</pre>    |             Modify your issues.             |
    |   Workspace    |  <pre>```read:workspace:bitbucket```</pre>   |            View your workspaces.            |
    |   Workspace    |   <pre>```admin:project:bitbucket```</pre>   |          Administer your projects.          |
    |    Webhooks    |   <pre>```read:webhook:bitbucket```</pre>    |             View your webhooks.             |
    |    Webhooks    |   <pre>```write:webhook:bitbucket```</pre>   |            Modify your webhooks.            |
    |   Pipelines    |   <pre>```read:pipeline:bitbucket```</pre>   |            View your pipelines.             |
    |   Pipelines    |    <pre>```read:runner:bitbucket```</pre>    | View your workspaces/repositories' runners. |

    !!! tip "Copy scopes to find them quickly"
        Click the copy button next to each scope in the table and paste it into the search field on the Bitbucket token creation page to locate the permission.

6. Click **Create**, then copy the token immediately. The token value is only displayed once and cannot be retrieved later.

## Connect Bitbucket

With an [API token](#create-an-api-token) created, you can set up the Bitbucket integration from the [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} page on the kluster.ai platform.

1. Navigate to [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} in the kluster.ai platform. The PR Bot Installation page displays the available integrations, including Bitbucket. Click **Connect to Bitbucket**.

2. A dialog appears prompting you to enter your Bitbucket email and API token. Enter your credentials and click **Save & Install**.

    ![Dialog prompting for Bitbucket API credentials](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-01.webp)

3. After the credentials are validated, a message confirms the Bitbucket integration as **Installed** and lists the registered workspaces. By default, kluster has access to all workspaces associated with the API token owner.

    ![Bitbucket integration showing Connected status on kluster.ai](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-02.webp)

## What happens after setup

Once the integration is connected, the kluster.ai bot begins reviewing pull requests automatically. No further action is required.

### On new pull requests

When a pull request is opened, the bot analyzes all changes using ultra-deep analysis and posts its feedback:

- A **summary comment** titled **kluster.ai PR Review Summary**, which includes a description of the changes, the review result (All Clear or a list of detected issues), and a prior review warning if no IDE or CLI reviews were performed on the branch.

    ![Example of a kluster.ai PR Review Summary comment on a Bitbucket pull request](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-04.webp)

- **Inline comments** on specific lines where issues were found. Each inline comment includes a severity badge (for example, `security · high`), a description, a detailed explanation, a recommended action, and quick issue actions to ignore the finding or copy an AI prompt for fixing it.

    ![Example of a kluster.ai inline comment on a Bitbucket pull request](/images/code-reviews/pr-reviews/pr-reviews-bitbucket-03.webp)

    When clicking **Ignore issue** or **Copy AI prompt**, you are taken to the kluster.ai platform. From there, you can access the ignore menu to dismiss the finding or view the prompt needed to feed an AI agent for fixing the issue, which is automatically copied to your clipboard.

!!! warning "Bot comments appear under the token owner's name"
    In Bitbucket, the bot's comments are attributed to the user who created the API token. This is why a dedicated service account is recommended in the [Create an API token](#create-an-api-token) section.

### On new commits

When new commits are pushed to an open pull request, the bot re-runs its analysis on the updated changes and updates its comments accordingly.

### Prior review detection

If kluster was used during development on the branch (via IDE or CLI), the bot's summary comment includes review statistics, such as the number of reviews performed, issues found, and issues left unfixed. If no prior reviews were detected, the bot includes a note encouraging earlier use of kluster in the development workflow.

## Next steps

- **[PR Reviews quickstart](/code-reviews/pr-reviews/quickstart/)**: Learn how the bot works across all supported platforms.
- **[GitHub integration](/code-reviews/pr-reviews/github/)**: Connect the kluster.ai bot to GitHub via OAuth and the GitHub App.
- **[GitLab integration](/code-reviews/pr-reviews/gitlab/)**: Connect the kluster.ai bot to GitLab via access token.
- **[Review modes](/code-reviews/review-modes/)**: Understand all available review types.
