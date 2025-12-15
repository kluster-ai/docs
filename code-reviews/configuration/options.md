---
title: Options
description: Configure kluster.ai Code Review settings, from sensitivity levels to issue types and enabled tools used to verify code across your workflow.
---

# Options

You can customize the [kluster.ai](https://www.kluster.ai/){target=\_blank} Code Review behavior through the platform settings or directly in your IDE. The Options page is available from the left-hand menu under **Review option**, where you can configure sensitivity levels for issue reporting, select which types of bug checks to perform, and enable or disable specific MCP tools to match your development workflow.

![Code Review Options interface](/images/code-reviews/code/configuration/configuration-01.webp)

## Sensitivity settings

Configure the minimum sensitivity level for the real-time Code Review issue reporting. Set your threshold based based on your team requirements:

- **Low**: Detects even the smallest potential issues.
- **Medium**: Suitable for projects requiring strong security and high code quality.
- **High**: (Recommended) Balances strong protection against LLM hallucination and security issues with performance.
- **Critical**: Focuses only on critical issues for faster iteration and smoother coding experience.

!!! info "Choosing a sensitivity level"
    The ideal setting depends on your use case. In general, a **High** level is a good starting point, but you might want to set it to **Medium** for production workflows.

## Code review scope

Select which types of issues real-time Code Review detects during analysis. Each type specifies a category of issues the system can identify.

|     Type      |           Description           |                Example                |
|:-------------:|:-------------------------------:|:-------------------------------------:|
|   **intent**    | Code doesn't match user request | User asked for sorting, got filtering |
|  **semantic**   |    Meaning and type errors      |        Wrong variable type used       |
|  **knowledge**  |    Best practice violations     |       Not following conventions       |
| **performance** |       Performance issues        |        Inefficient algorithms         |
|   **quality**   |      Code quality problems      |        Poor naming, complexity        |
|   **logical**   |     Control flow errors         |           Off-by-one errors           |
|  **security**   |    Security vulnerabilities     |          SQL injection risks          |

## Enabled tools

Control which review tools run in your development environment. Enable or disable each tool based on the specific needs and workflow of your project.

- **Real-time Code Review**: For code quality reviews.
- **Dependency Analysis**: For package and dependency security.
- **Ambient Background Reviews (Beta, Enterprise plan)**: Automatically review your code for issues and suggestions as you work, without requiring you to trigger anything.

## Next steps

- [Create custom rules](/code-reviews/configuration/rules/): Add project-specific development standards.
- [View tools reference](/code-reviews/tools/): Understand the technical API details.
- [Set up integrations](/code-reviews/quickstart/): Configure IDE integrations.