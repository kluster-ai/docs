---
title: Azure DevOps PR Reviews Setup
description: Connect the kluster.ai bot to Azure DevOps to automatically review every pull request. Set up the integration with a personal access token in a few steps.
categories: PR Reviews
---

# Azure DevOps

Connect the [kluster.ai](https://www.kluster.ai/){target=\_blank} Code Review solution to your Azure DevOps repositories to automatically review every pull request. The setup uses a token-based integration that requires a personal access token and your organization URL before the bot can begin reviewing your pull requests.

Before connecting, an administrator in your Azure DevOps organization must complete a one-time consent step directly from the kluster.ai platform. After that, any member of **Project Collection Administrators** can generate a token and finish the setup.

Once connected, the bot reviews every new pull request and every new commit pushed to an open pull request. No additional configuration is needed.

--8<-- 'text/code-reviews/pr-reviews-enterprise.md'

--8<-- 'text/code-reviews/pr-reviews-tip.md'

## Prerequisites

Before getting started, ensure you have:

- A [kluster.ai](https://platform.kluster.ai/signup){target=\_blank} account.
- An Azure DevOps account that is a member of **Project Collection Administrators** in your organization.

    !!! warning "Verify account permissions"
        The account used for setup must have sufficient organization-level permissions to install webhooks. If the account has insufficient permissions, webhook installation will fail silently and pull request reviews will not appear. To fix this, navigate to **Organization Settings** > **Security** > **Permissions**, find the user, and add them to **Project Collection Administrators**. After updating permissions, click **Re-install** on the PR Reviews page in the kluster.ai platform.

- A personal access token with the required scopes. See [Create a personal access token](#create-a-personal-access-token) for instructions.

## Admin consent

Before anyone in your organization can connect kluster to Azure DevOps, an administrator or organization owner must grant consent. This is a one-time step per organization that applies to both PR reviews and repo reviews.

The admin consent step appears as step 1 when you begin the Azure DevOps connection flow on the kluster.ai platform (see [Connect Azure DevOps](#connect-azure-devops)). If you are the organization admin, click **Open** to review and accept the required permissions. If you are not, click **Copy link** and share it with your organization admin to complete the consent.

!!! note
    Admin consent only needs to be completed once. After the admin accepts, any member of **Project Collection Administrators** in the organization can connect projects without repeating the consent step. See [Prerequisites](#prerequisites) for the required role. Note that [custom rules](/code-reviews/configuration/rules/) — including learned rules — are not currently supported for Azure DevOps.

## Create a personal access token

The kluster.ai bot requires an Azure DevOps personal access token to access your repositories and post review comments. Tokens are created through your Azure DevOps user settings.

!!! tip "Use a dedicated service account"
    Reviews posted by the bot are attributed to the token owner. To avoid reviews appearing under a personal account, create a dedicated Azure DevOps account for kluster and generate the personal access token from that account.

1. Sign in to the Azure DevOps account that will be associated with the kluster.ai bot reviews.
2. Click your profile icon in the top-right corner and select **Personal access tokens** under the Security section. Alternatively, navigate directly to `https://dev.azure.com/{organization}/_usersSettings/tokens`.
3. Click **New Token**. Enter a descriptive name (for example, "kluster.ai PR Reviews"), select your organization, and set an expiration date that aligns with your security policy.
4. Under **Scopes**, select **Custom defined** and enable the following permissions:

    |       Category       |         Scope          |                    Description                    |
    |:--------------------:|:----------------------:|:-------------------------------------------------:|
    |         Code         | **Read, write & manage** | Access repository content for code review.      |
    |      Work Items      | **Read, write & manage** | Access work items linked to pull requests.      |

    !!! tip
        If you prefer not to configure individual scopes, you can select **Full access** instead.

5. Click **Create**, then copy the token immediately. The token value is only displayed once and cannot be retrieved later.

## Connect Azure DevOps

With a [personal access token](#create-a-personal-access-token) ready, you can set up the Azure DevOps integration from the [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} page on the kluster.ai platform.

1. Navigate to [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} in the kluster.ai platform. The PR Bot Installation page displays the Azure DevOps integration with two setup steps: **Admin consent required** and **Enter your Azure DevOps credentials**.

2. **Complete admin consent** (one-time per organization). If you are the organization admin, click **Open** to review and accept the required permissions on the Azure DevOps site. If you are not an admin, click **Copy link** and share it with your organization admin. Once consent is granted, proceed to the next step.

3. **Enter your Azure DevOps credentials**. Provide your organization URL (for example, `https://dev.azure.com/kluster-ai`) and your personal access token. Click **Save & Install**.

    ![PR Bot Installation page showing Azure DevOps setup with Save & Install button](/images/code-reviews/pr-reviews/pr-reviews-azure-devops-01.webp)

4. After the credentials are validated, a confirmation banner shows the Azure DevOps integration with the **Installed** status, indicating that it is ready to review your pull requests automatically.

    ![Azure DevOps integration showing Installed status on kluster.ai](/images/code-reviews/pr-reviews/pr-reviews-azure-devops-02.webp)

## What happens after setup

Once the integration is connected, the kluster.ai bot begins reviewing pull requests automatically. No further action is required.

### On new pull requests

When a pull request is opened, the bot analyzes all changes using ultra-deep analysis and posts its feedback:

- A **summary comment** titled **kluster.ai PR Review Summary**, which includes a description of the changes, the review result (All Clear or a list of detected issues), and a prior review warning if no IDE or CLI reviews were performed on the branch.

    ![Example of a kluster.ai PR Review Summary comment on an Azure DevOps pull request](/images/code-reviews/pr-reviews/pr-reviews-azure-devops-04.webp)

- **Inline comments** on specific lines where issues were found. Each inline comment includes a severity badge (for example, `semantic · high`), a description, a detailed explanation, a recommended action, and quick issue actions to ignore the finding or copy an AI prompt for fixing it.

    ![Example of a kluster.ai inline comment on an Azure DevOps pull request](/images/code-reviews/pr-reviews/pr-reviews-azure-devops-03.webp)

    When clicking **Ignore issue** or **Copy AI prompt**, you are taken to the kluster.ai platform. From there, you can access the ignore menu to dismiss the finding or view the prompt needed to feed an AI agent for fixing the issue, which is automatically copied to your clipboard.

!!! warning "Bot comments appear under the token owner's name"
    In Azure DevOps, the bot's comments are attributed to the user who created the personal access token. This is why a dedicated service account is recommended in the [Create a personal access token](#create-a-personal-access-token) section.

### On new commits

When new commits are pushed to an open pull request, the bot re-runs its analysis on the updated changes and updates its comments accordingly.

### Prior review detection

If kluster was used during development on the branch (via IDE or CLI), the bot's summary comment includes review statistics, such as the number of reviews performed, issues found, and issues left unfixed. If no prior reviews were detected, the bot includes a note encouraging earlier use of kluster in the development workflow.

## Next steps

- **[PR Reviews quickstart](/code-reviews/pr-reviews/quickstart/)**: Learn how the bot works across all supported platforms.
- **[GitHub integration](/code-reviews/pr-reviews/github/)**: Connect the kluster.ai bot to GitHub via OAuth and the GitHub App.
- **[GitLab integration](/code-reviews/pr-reviews/gitlab/)**: Connect the kluster.ai bot to GitLab via access token.
- **[Bitbucket integration](/code-reviews/pr-reviews/bitbucket/)**: Connect the kluster.ai bot to Bitbucket via API token.
- **[Review modes](/code-reviews/review-modes/)**: Understand all available review types.
