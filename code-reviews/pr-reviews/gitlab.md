---
title: GitLab PR Reviews Setup
description: Connect the kluster.ai bot to GitLab to automatically review every merge request. Use a personal or group access token to set up.
categories: PR Reviews
---

# GitLab

Connect the [kluster.ai](https://www.kluster.ai/){target=\_blank} bot to your GitLab projects to automatically review every merge request. The setup uses a token-based integration. Provide a GitLab personal or group access token, select the projects to monitor, and the bot begins reviewing your merge requests.

Once connected, the bot reviews every new merge request and every new commit pushed to an open merge request. No additional configuration is needed.

--8<-- 'text/code-reviews/pr-reviews-enterprise.md'

--8<-- 'text/code-reviews/pr-reviews-tip.md'

## Prerequisites

Before getting started, ensure you have:

- A [kluster.ai](https://platform.kluster.ai/signup){target=\_blank} account.
- A GitLab account with at least **Developer** access to the projects you want to review.
- A GitLab **Personal** or **Group** access token with the `api` scope. See [Create an access token](#create-an-access-token) for instructions.

!!! warning "Verify account permissions"
    The account that generates the access token must have at least **Developer** role in the target project or group. Having the correct token scopes (such as `api`) is not enough. The account itself needs Developer-level permissions. If the account only has Guest access, webhook installation will fail silently and PR reviews will not appear. After fixing the account's role, click **Re-install** on the PR Reviews page in the kluster.ai platform to complete the setup.

## Create an access token

The kluster.ai bot requires a GitLab personal or group access token with the `api` scope to read merge requests and post review comments.

!!! warning "Project access tokens are not supported"
    kluster requires a **Personal access token** or a **Group access token**. Do not use a **Project access token**. These look similar in the GitLab UI but do not provide the permissions kluster needs to install webhooks across your projects. If you previously configured kluster with a project access token and reviews are not appearing, generate a new personal or group access token, then click **Re-install** on the PR Reviews page in the kluster.ai platform.

!!! tip "Use a dedicated service account"
    Reviews posted by the bot are attributed to the token owner. To avoid reviews appearing under a personal account, create a dedicated GitLab service account for kluster and generate the token from that account.

=== "Personal access token"

    kluster uses a **Legacy** personal access token. GitLab now shows two options when you create a token: **Legacy token** and **Fine-grained token (Beta)**. Select **Legacy token** to follow the recommended setup below; it includes all the permissions kluster needs by default.

    1. Sign in to the GitLab account that will be associated with the kluster.ai bot reviews.
    2. Open the [Personal access tokens](https://gitlab.com/-/user_settings/personal_access_tokens){target=\_blank} page and click **Add new token**.
    3. When prompted to choose a token type, select **Legacy token**.
    4. Enter a descriptive name (for example, "kluster.ai PR Reviews"), set an expiration date, and select the following scopes: `api`, `read_api`, and `read_user`.
    5. Click **Generate token**, then copy the token immediately. The token value is only displayed once and cannot be retrieved later.

    ??? note "Alternative: fine-grained personal access token (Beta)"
        If you want to restrict kluster to specific repositories, you can use a fine-grained personal access token instead. Fine-grained tokens let you choose exactly which projects kluster can access, but you must manually enable every required permission.

        To create a fine-grained token:

        1. On the [Personal access tokens](https://gitlab.com/-/user_settings/personal_access_tokens){target=\_blank} page, click **Add new token** and select **Fine-grained token (Beta)**.
        2. Enter a descriptive name and set an expiration date.
        3. Under **Group and project permissions**, enable the following scopes:

            | Category | Scope | Access |
            |:---:|:---:|:---:|
            | Projects | Page | Read |
            | Repository | Code Download | Read |
            | Repository | Commit | Read |
            | Repository | Merge Request Approval Rule | Create, Read, Update |
            | Repository | Merge Request Approval Status | Read |
            | Repository | Merge Request Approval | Read |
            | Repository | Repository | Create, Read, Update |
            | System Migration and Integration | Webhook | Create, Delete, Read, Update |
            | System Migration and Integration | Webhook Log | Read |
            | System Migration and Integration | Webhook Subscription | Read |
            | System Migration and Integration | Webhook Event | Create |
            | System Migration and Integration | Webhook URL variable | Create, Read, Update |

        4. Under **User permissions**, enable the following scopes:

            | Scope | Access |
            |:---:|:---:|
            | Merge Request | Read |
            | User | Read |
            | Project | Read |

        5. Click **Generate token**, then copy the token immediately.

        !!! tip
            The Legacy token is recommended for most users because it includes all required permissions by default. Use a fine-grained token only if limiting repository access is a priority for your organization.

=== "Group access token"

    Group access tokens are available on GitLab Premium or Ultimate. They are scoped to a specific group and automatically create a bot user for reviews.

    1. Navigate to the group, then go to **Settings > Access Tokens**.
    2. Create a token with the `api` scope and **Developer** access.

    Each group requires its own token.

## Connect GitLab

You can set up the GitLab integration from the [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} page on the kluster.ai platform.

1. Navigate to [PR Reviews](https://platform.kluster.ai/pr-bot-installation){target=\_blank} in the kluster.ai platform. The PR Bot Installation page displays the available integrations, including GitLab. Click **Connect GitLab**.

2. A dialog appears prompting you to enter your GitLab API token. Enter your credentials and click **Save & Install**.

    ![Dialog prompting for GitLab API token](/images/code-reviews/pr-reviews/pr-reviews-gitlab-01.webp)

3. After the credentials are validated, a message confirms the GitLab integration as **Installed** and lists the registered workspaces. By default, kluster has access to all groups associated with the API token owner.

    ![GitLab integration showing Installed status on kluster.ai](/images/code-reviews/pr-reviews/pr-reviews-gitlab-02.webp)

## What happens after setup

Once the integration is connected, the kluster.ai bot begins reviewing merge requests automatically. No further action is required.

### On new merge requests

When a merge request is opened, the bot triggers a pipeline that analyzes all changes using ultra-deep analysis. Once the pipeline completes, the bot posts its feedback:

- A **summary comment** titled **kluster.ai PR Review Summary**, which includes a description of the changes, the review result (All Clear or a list of detected issues), and a prior review warning if no IDE or CLI reviews were performed on the branch.

    ![Example of a kluster.ai PR Review Summary comment on a GitLab merge request](/images/code-reviews/pr-reviews/pr-reviews-gitlab-03.webp)

- **Inline comments** on specific lines where issues were found. Each inline comment includes a severity badge (for example, `security · critical`), a description, a detailed explanation, a recommended action, and quick issue actions to ignore the finding or copy an AI prompt for fixing it.

    ![Example of a kluster.ai inline comment on a GitLab merge request](/images/code-reviews/pr-reviews/pr-reviews-gitlab-04.webp)

    When clicking **Ignore issue** or **Copy AI prompt**, you are taken to the kluster.ai platform. From there, you can access the ignore menu to dismiss the finding or view the prompt needed to feed an AI agent for fixing the issue, which is automatically copied to your clipboard.

!!! warning "Bot comments appear under the token owner's name"
    In GitLab, the bot's comments are attributed to the user who created the access token. This is why a dedicated service account is recommended in the [Create an access token](#create-an-access-token) section.

### On new commits

When new commits are pushed to an open merge request, the bot re-runs its analysis on the updated changes and updates its comments accordingly.

### Prior review detection

If kluster was used during development on the branch (via IDE or CLI), the bot's summary comment includes review statistics, such as the number of reviews performed, issues found, and issues left unfixed. If no prior reviews were detected, the bot includes a note encouraging earlier use of kluster in the development workflow.

## Next steps

- **[PR Reviews quickstart](/code-reviews/pr-reviews/quickstart/)**: Learn how the bot works across all supported platforms.
- **[GitHub integration](/code-reviews/pr-reviews/github/)**: Connect the kluster.ai bot to GitHub via OAuth and the GitHub App.
- **[Bitbucket integration](/code-reviews/pr-reviews/bitbucket/)**: Connect the kluster.ai bot to Bitbucket via API token.
- **[Azure DevOps integration](/code-reviews/pr-reviews/azure-devops/)**: Connect the kluster.ai bot to Azure DevOps via personal access token.
- **[Review modes](/code-reviews/review-modes/)**: Understand all available review types.
