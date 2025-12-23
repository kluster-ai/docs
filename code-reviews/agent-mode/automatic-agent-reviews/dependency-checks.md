---
title: Dependency Checks
description: Learn how kluster.ai validates packages and dependencies before installation, catching vulnerabilities and license issues automatically.
---

# Dependency Checks

Code Reviews protects you when starting new projects or adding libraries by validating dependencies before installation.

## How dependency checks work

**How it works:**

1.  **You prompt**: Ask your AI to start a project (e.g., "Scaffold a Next.js app with Auth.js").
2.  **AI suggests**: The AI lists the necessary dependencies.
3.  **kluster.ai verifies**: The Dependency Validator checks every package for security vulnerabilities and license compliance before you install them.


When the AI suggests a package version with a known vulnerability, kluster.ai alerts you immediately, preventing the risk from entering your codebase.

![Dependency Analysis Example](/images/code-reviews/agent-mode/automatic-agent-reviews/dependency-analysis.webp)

## What gets checked

The dependency validator analyzes:

| Check | Description |
|-------|-------------|
| **Known vulnerabilities** | CVEs and security advisories |
| **License compliance** | Compatibility with your project's license |
| **Maintenance status** | Is the package actively maintained? |
| **Version issues** | Outdated or deprecated versions |

## When dependency checks trigger

Dependency validation runs automatically when your AI assistant:

- Suggests installing new packages (`npm install`, `pip install`, etc.)
- Creates or modifies package files (`package.json`, `requirements.txt`, etc.)
- Scaffolds new projects with dependencies

## Example workflow

**You**: "Create a new Express API with JWT authentication"

**AI**: "I'll set up the project. First, let me install the dependencies..."

```bash
npm install express jsonwebtoken bcrypt
```

**kluster.ai** (automatically): "Dependency check complete:

- ✅ `express@4.18.2` - No known vulnerabilities
- ⚠️ `jsonwebtoken@8.5.1` - Known vulnerability (CVE-2022-23529). Recommend upgrading to `9.0.0`
- ✅ `bcrypt@5.1.1` - No known vulnerabilities

Updating installation command to use safe versions..."

## Supported package managers

| Package Manager | Support |
|-----------------|---------|
| npm / yarn / pnpm | Yes |
| pip | Yes |
| cargo | Yes |
| go mod | Yes |
| composer | Yes |
| bundler | Yes |

## Configuration

You can enable or disable dependency checking in your [configuration options](/code-reviews/configuration/options/):

- **Enabled tools**: Toggle "Dependency Analysis" on/off
- **Sensitivity**: Adjust how strictly vulnerabilities are flagged

## Next steps

- **[Automatic agent reviews](/code-reviews/agent-mode/automatic-agent-reviews/)**: Learn about code reviews
- **[Manual agent reviews](/code-reviews/agent-mode/manual-agent-reviews/)**: Review existing code on demand
- **[Configuration](/code-reviews/configuration/options/)**: Customize dependency check behavior
