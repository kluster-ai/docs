---
title: Dependency Checks
description: Learn how kluster.ai validates packages and dependencies before installation, catching vulnerabilities and license issues automatically.
---

# Dependency Checks

Code Reviews protects you when starting new projects or adding libraries by validating dependencies before installation.

## How dependency checks work

1.  **You prompt**: Ask your AI to start a project (e.g., "Scaffold a Next.js app with Auth.js").
2.  **AI suggests**: The AI lists the necessary dependencies.
3.  **kluster.ai verifies**: The Dependency Validator checks every package for security vulnerabilities and license compliance before you install them.


When the AI suggests a package version with a known vulnerability, kluster.ai alerts you immediately, preventing the risk from entering your codebase.

![Dependency Analysis Example](/images/code-reviews/agent-mode/automatic-agent-reviews/dependency-analysis.webp)


## Next steps

- **[Manual Reviews](/code-reviews/agent-mode/manual-agent-reviews/)**: Review existing code on demand.
- **[Configuration](/code-reviews/configuration/options/)**: Customize dependency check behavior.
