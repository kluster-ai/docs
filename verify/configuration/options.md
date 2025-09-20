---
title: Options
description: Configure kluster.ai Verify code settings including sensitivity levels, bug types, and enabled tools for AI-generated code verification.
---

# Options

You can customize the [kluster.ai](https://www.kluster.ai/){target=_blank} Verify code behavior through the platform settings or directly in your IDE. This allows you to tailor the verification process to your specific needs, such as configuring sensitivity levels for issue reporting, selecting which types of bug checks to perform, and enabling or disabling specific MCP tools to match your development workflow.

![Code Review Options interface showing three numbered sections: Sensitivity Settings, Code Review Scope, and Enabled Tools](/images/verify/code/configuration/configuration-1.webp)

## 1. Sensitivity settings

Configure the minimum sensitivity level for the Real-time Code Review tool's issue reporting. Set your threshold based on your team's needs:

- `Low`: Detects even the smallest potential issues.
- `Medium`: Suitable for projects requiring strong security and high code quality.
- `High`: (Recommended) Balances strong protection against LLM hallucination and security issues with performance.
- `Critical`: Focuses only on critical issues for faster iteration and smoother coding experience.

The ideal setting depends on your use case. For example, a **High** level is a good starting point, but you might want to set it to **Medium** for production code.

## 2. Code review scope

Select which types of issues the Real-time Code Review tool detects during code analysis. You have full control over which bug types to check for through simple on/off toggles.

|     Type      |           Description           |                Example                |
|:-------------:|:-------------------------------:|:-------------------------------------:|
|   `intent`    | Code doesn't match user request | User asked for sorting, got filtering |
|  `semantic`   |          Logic errors           |        Missing error handling         |
|  `knowledge`  |    Best practice violations     |       Not following conventions       |
| `performance` |       Performance issues        |        Inefficient algorithms         |
|   `quality`   |      Code quality problems      |        Poor naming, complexity        |
|   `logical`   |          Logic errors           |           Off-by-one errors           |
|  `security`   |    Security vulnerabilities     |          SQL injection risks          |

## 3. Enabled tools

Control which verification tools run in your development environment. Enable or disable each tool based on your project's specific needs and workflow.

- `Real-time Code Review`: For code quality verification.
- `Dependency Analysis`: For package and dependency security.

## Next steps

- [Create custom rules](/verify/configuration/rules/): Add project-specific development standards.
- [View tools reference](/verify/tools/): Understand the technical API details.
- [Set up integrations](/verify/integrations/ide/): Configure IDE integrations.