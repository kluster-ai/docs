---
title: Automatic Agent Reviews
description: Real-time code reviews that trigger automatically when AI generates or modifies code. Catch issues instantly as you work.
---

# Automatic Agent Reviews

Automatic agent reviews happen in real-time as your AI assistant generates code. No manual intervention required—kluster.ai monitors code changes and flags issues instantly.

## How automatic reviews work

<div class="embed-container">
    <iframe
        src="https://www.youtube.com/embed/-V0VsqgTza8"
        title="Instant Code Reviews with kluster.ai"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
    </iframe>
</div>

When you're coding with an AI assistant, automatic reviews work silently in the background:

1. **You prompt**: Ask your AI assistant to generate code
2. **AI generates**: The assistant writes or modifies code
3. **kluster.ai intercepts**: The code diff is automatically sent for review
4. **Issues flagged**: Problems are identified with severity and fix suggestions
5. **AI fixes**: Your assistant applies the recommended fixes

This cycle repeats with every code change, providing continuous protection.

## What triggers an automatic review

Automatic reviews trigger whenever your AI assistant:

- Creates new files with code
- Modifies existing code
- Adds new functions or classes
- Changes logic in existing functions
- Updates configuration files

The review analyzes the **diff** (what changed), not the entire file, making it fast and focused.

## Example workflow

**You**: "Create a user login endpoint with email and password"

**AI Assistant**: *Creates the endpoint code*

**kluster.ai** (automatically): "Found 1 critical issue:

- **P2 Critical - Security**: Password stored in plain text. Use bcrypt or argon2 for password hashing."

**AI Assistant**: *Applies the fix, using bcrypt for password hashing*

You never had to ask for the review—it happened automatically.

## Issue types detected

Automatic reviews check for all standard issue types:

| Type | Description | Example |
|------|-------------|---------|
| Intent | Code doesn't match request | Asked for sorting, got filtering |
| Security | Vulnerabilities | SQL injection, XSS, hardcoded secrets |
| Logical | Control flow errors | Off-by-one, infinite loops |
| Semantic | Type/meaning errors | Wrong variable type |
| Performance | Efficiency issues | N+1 queries, O(n²) when O(n) possible |
| Quality | Code quality | Poor naming, high complexity |
| Knowledge | Best practices | Outdated patterns, missing error handling |

## Dependency checking

Automatic reviews also include dependency validation when your AI suggests installing packages:

1. AI suggests: `npm install some-package`
2. kluster.ai checks the package for:
   - Known vulnerabilities (CVEs)
   - License compliance
   - Maintenance status
3. Issues flagged before installation

[:octicons-arrow-right-24: Learn more about dependency checks](/code-reviews/agent-mode/automatic-agent-reviews/dependency-checks/)

## Supported tools

Automatic agent reviews work with:

| Tool | Support |
|------|---------|
| Cursor | Yes |
| VS Code (with Copilot) | Yes |
| Windsurf | Yes |
| Antigravity | Yes |
| Claude Code | Yes |
| Codex CLI | Yes |

## Configuration

You can customize automatic review behavior:

- **Sensitivity level**: Set minimum severity to report (Low → Critical)
- **Issue types**: Enable/disable specific check categories
- **Tools**: Toggle automatic reviews on/off

[:octicons-arrow-right-24: Configure options](/code-reviews/configuration/options/)

## Next steps

- **[Quickstart](/code-reviews/agent-mode/automatic-agent-reviews/quickstart/)**: Step-by-step setup guide
- **[Dependency checks](/code-reviews/agent-mode/automatic-agent-reviews/dependency-checks/)**: Learn about package validation
- **[Manual agent reviews](/code-reviews/agent-mode/manual-agent-reviews/)**: On-demand reviews for existing code
