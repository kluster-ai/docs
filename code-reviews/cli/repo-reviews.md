---
title: Repo Reviews from CLI
description: Trigger and monitor system-wide repo reviews from your terminal using kluster-cli, with a terminal-first workflow for codebase analysis.
categories: Repo reviews, CLI
---

# Repo reviews from CLI

You can trigger and monitor repo reviews directly from `kluster-cli`. This gives you a terminal-first workflow for system-wide analysis without opening the dashboard.

## Prerequisites

Before using repo review commands from CLI, make sure you have:

- **kluster-cli installed and authenticated**: See [CLI quickstart](/code-reviews/cli/quickstart/).
- **A connected repository**: Connect your repository in the [Repo Reviews dashboard](https://platform.kluster.ai/repo-reviews){target=\_blank}.
- **An open shell in that repository**: Run commands from the repository root.

## Start a repo review

Use this command to start a new repo-wide analysis:

```bash
kluster review repo start
```

--8<-- 'code/code-reviews/cli/review-repo-start.md'

The review runs asynchronously. You'll get an email when analysis is complete.

## Check review status and results

Use this command to see the latest review output any time:

```bash
kluster review repo show
```

--8<-- 'code/code-reviews/cli/review-repo-show.md'

This output shows the last review timestamp and findings grouped by severity and category.

## Next steps

- **[Repo Reviews quickstart](/code-reviews/repo-reviews/quickstart/)**: Learn the full dashboard workflow and issue actions.
- **[CLI quickstart](/code-reviews/cli/quickstart/)**: Install and authenticate kluster-cli.
- **[Review modes](/code-reviews/review-modes/)**: Compare repo reviews with other review workflows.
