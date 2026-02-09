---
title: Repo Reviews Quickstart
description: Run your first system-wide codebase analysis to find bugs that emerge from interactions across modules.
categories: Basics, Repo reviews
---

# Repo Reviews quickstart

Learn how to run system-wide codebase analysis with [kluster.ai](https://kluster.ai){target=_blank} Repo Reviews. Connect your repository, wait for the deep scan to complete, and review cross-module bugs that slip through PR-level reviews.

## Prerequisites

Before getting started, ensure you have:

- **A kluster.ai account**: Sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you don't have one.
- **A connected repository**: You'll need to connect your GitHub, GitLab, or Bitbucket repository through the dashboard.

## How repo reviews work

Repo reviews analyze your entire codebase as a system instead of reviewing individual changes. When multiple parts of your code interact, issues emerge that don't show up in PR-level reviews.

1. **Connect your repository**: Link your GitHub, GitLab, or Bitbucket repository to kluster.ai.
2. **Scan starts automatically**: Wait for the deep analysis to complete.
3. **Review the findings**: Examine issues grouped by severity and type.

This catches cross-module bugs, state inconsistencies, bypassed validation checks, and other system-wide problems that slip through regular code reviews.

## Running your first repo review

### 1. Connect your repository

Go to the [Repo Reviews dashboard](https://platform.kluster.ai/repo-reviews){target=_blank} and click **Connect Repository**.

![Repo Reviews dashboard with Connect Repository button](/images/code-reviews/repo-reviews/repo-reviews-setup-1.webp)

Select your Git provider (GitHub, GitLab, or Bitbucket):

![Select Git provider modal](/images/code-reviews/repo-reviews/repo-reviews-setup-2.webp)

Then choose the repository you want to analyze:

![Select repository from dropdown](/images/code-reviews/repo-reviews/repo-reviews-setup-3.webp)

### 2. Scan repo

Once your repository is connected, the analysis starts automatically and shows **"Review in progress..."**. The scan runs a deep analysis of your codebase. Depending on repository size, this takes several minutes. You'll receive an email notification once it's done.

You can close the page and come back later.

### 3. Review the results

When the scan finishes, you'll see a list of issues found in your codebase:

![Repo review results showing list of issues](/images/code-reviews/repo-reviews/repo-reviews-setup-4.webp)

Each issue displays:

- **Description**: Summary of the problem.
- **Severity**: High, Medium, or Low (shown with color badges).
- **Type**: The category of issue (Security, Logical, Performance, Knowledge, etc.).
- **Priority**: P0-P5 ranking for triage.

### 4. Examine issue details

Click a given bug or issue to learn more. The detail view includes:

- **Description**: What the problem is.
- **Explanation**: Why this is a problem and how it impacts your system.
- **Recommended Actions**: Steps to fix the issue.

![Issue detail view with description, explanation, and recommended actions](/images/code-reviews/repo-reviews/repo-reviews-setup-5.webp)

### 5. Take action

For each issue, you have three options:

- **Copy**: Copy the issue details to share or save.
- **Fix with AI**: Get a prompt to paste into your AI assistant (Claude, Cursor, etc.) to fix it automatically.
- **Dismiss**: Mark as false positive or accepted risk.

![Take action on the bugs found by clicking one of the available options](/images/code-reviews/repo-reviews/repo-reviews-setup-6.webp)


## Next steps

- **[Pick your workflow](/code-reviews/get-started/pick-your-workflow/)**: Learn when to use repo reviews vs. other review modes.
- **[Review modes](/code-reviews/review-modes/)**: Understand all available review types.
- **[FAQ](/code-reviews/faq/)**: Common questions about kluster.ai code reviews.
