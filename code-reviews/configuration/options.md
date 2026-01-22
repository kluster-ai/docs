---
title: Options
description: Configure kluster.ai Code Review settings, from sensitivity levels to issue types and enabled tools used to verify code across your workflow.
categories: Basics
---

# Options

You can customize the [kluster.ai](https://www.kluster.ai/){target=_blank} Code Reviews behavior through the platform settings or directly in your IDE. This allows you to tailor the review process to your specific needs, such as configuring sensitivity levels for issue reporting, selecting which types of bug checks to perform, and enabling or disabling specific MCP tools to match your development workflow.

![Code Review Options interface showing three numbered sections: Sensitivity Settings, Code Review Scope, and Enabled Tools](/images/code-reviews/configuration/configuration-1.webp)

## 1. Sensitivity settings

Configure the minimum sensitivity level for Code Reviews issue reporting. Set your threshold based on your team's needs:

- `Low`: Detects even the smallest potential issues.
- `Medium`: Suitable for projects requiring strong security and high code quality.
- `High`: (Recommended) Strong protection against security and quality issues while maintaining good performance.
- `Critical`: Focuses only on critical issues for faster iteration and smoother coding experience.

The ideal setting depends on your use case. For example, a **High** level is a good starting point, but you might want to set it to **Medium** for production code.

## 2. Code review scope

Select which types of issues Code Reviews detects during code analysis. You have full control over which bug types to check for through simple on/off toggles.

|     Type      |           Description           |                Example                |
|:-------------:|:-------------------------------:|:-------------------------------------:|
|   `intent`    | Code doesn't match user request | User asked for sorting, got filtering |
|  `semantic`   |    Meaning and type errors      |        Wrong variable type used       |
|  `knowledge`  |    Best practice violations     |       Not following conventions       |
| `performance` |       Performance issues        |        Inefficient algorithms         |
|   `quality`   |      Code quality problems      |        Poor naming, complexity        |
|   `logical`   |     Control flow errors         |           Off-by-one errors           |
|  `security`   |    Security vulnerabilities     |          SQL injection risks          |

## 3. Enabled tools

Control which review tools run in your development environment. Enable or disable each tool based on your project's specific needs and workflow.

- `Real-time Code Review`: For code quality reviews.
- `Dependency Analysis`: For package and dependency security.
- `Ambient Background Reviews (Beta, Enterprise plan)`: Automatic reviews that run in the background after you pause typing.

## Next steps

- [Create custom rules](/code-reviews/configuration/rules/): Add project-specific development standards.
- [View MCP tools reference](/code-reviews/reference/mcp-tools/): Understand the technical API details.
- [Installation guide](/code-reviews/get-started/installation/): Set up Code Reviews in your IDE.
