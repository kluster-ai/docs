---
title: kluster Code Reviews Changelog
description: A chronological record of kluster.ai Code Reviews product updates, including new features, bug fixes, and improvements across all releases.
categories: Changelog
---

# Product changelog

Stay up to date with the latest changes to kluster.ai Code Reviews. This page lists new features, improvements, and bug fixes in reverse chronological order. Entries are grouped by month so you can quickly find what changed and when.

## April 2026

::timeline::

- title: Custom AI rules support for code reviews
  sub_title: "2026-04-06"
  content: Added the ability to include project and global AI rules (such as AGENTS.md and CLAUDE.md) as part of code review. Supported in VS Code-based IDEs, MCP integrations, and JetBrains.

::/timeline::

## March 2026

::timeline::

- title: Azure DevOps support for PR bot
  sub_title: "2026-03-31"
  content: Added Azure DevOps support for PR bot.

- title: Azure DevOps support for repository reviews
  sub_title: "2026-03-31"
  content: Added Azure DevOps support for repository reviews.

- title: Pause reviews during AI-assisted workflows
  sub_title: "2026-03-25"
  content: Added the ability to pause kluster reviews during AI-assisted workflows.

- title: Cleaner GitHub comment threads
  sub_title: "2026-03-25"
  content: Improved GitHub comment-thread handling so outdated kluster review threads are resolved or updated more cleanly.

- title: Expanded review context for GitHub and GitLab
  sub_title: "2026-03-23"
  content: Improved review quality for GitHub and GitLab by expanding the context available during analysis.

- title: Improved Claude Code review reliability in Cursor
  sub_title: "2026-03-19"
  content: Improved reliability for Claude Code review workflows used through Cursor.

- title: Released JetBrains plugin
  sub_title: "2026-03-18"
  content: Released the JetBrains plugin for kluster.ai Code Reviews.

- title: Expanded context for VS Code-based IDE reviews
  sub_title: "2026-03-16"
  content: Improved review quality in VS Code-based IDEs by expanding context for manual and background reviews.

- title: PR bot support for GitLab and Bitbucket
  sub_title: "2026-03-10"
  content: Expanded PR bot support to GitLab and Bitbucket. Added Ignore and Fix with AI actions for PR bot findings.

- title: Jira integration and new manual review UI
  sub_title: "2026-03-02"
  content: Added Jira as an external knowledge source for reviews and released a new manual review results UI for VS Code-based IDEs.

::/timeline::

## February 2026

::timeline::

- title: Ignore and Snooze for repository reviews
  sub_title: "2026-02-18"
  content: Added Ignore and Snooze controls to repository reviews.

- title: Ignore and Snooze for IDE review findings
  sub_title: "2026-02-12"
  content: Added Ignore and Snooze controls for review findings in the IDE workflow.

- title: Branch selection for repository reviews
  sub_title: "2026-02-11"
  content: Added branch selection for repository reviews and changed the default review cadence to once per month.

- title: Added .klusterignore support
  sub_title: "2026-02-10"
  content: Added .klusterignore support so teams can exclude files and folders from reviews using gitignore-style rules.

- title: Team admin review history
  sub_title: "2026-02-06"
  content: Added team-admin visibility into team review history.

- title: Bitbucket support for project rules and repo reviews
  sub_title: "2026-02-06"
  content: Released Bitbucket support for project rules and repository reviews.

- title: Released kluster CLI
  sub_title: "2026-02-06"
  content: Released the kluster CLI for terminal-based code reviews.

- title: Improved first-time install for Codex users
  sub_title: "2026-02-05"
  content: Improved first-time install reliability for Codex users.

- title: Released repository reviews
  sub_title: "2026-02-03"
  content: Released repository reviews for full-project scanning.

- title: Improved VS Code and Cursor extension behavior
  sub_title: "2026-02-03"
  content: Improved extension behavior in VS Code and Cursor, including more reliable Fix with AI behavior and better handling of non-code files.

- title: Improved support for large Claude Code changes
  sub_title: "2026-02-02"
  content: Improved support for larger Claude Code changes during review.

::/timeline::

## January 2026

::timeline::

- title: Separate Instant and Deep review actions
  sub_title: "2026-01-22"
  content: Updated the extension UI to support separate Instant and Deep manual review actions.

- title: Increased maximum review size
  sub_title: "2026-01-15"
  content: Increased the maximum review size for manual reviews and improved handling of oversized or minified files.

::/timeline::

## December 2025

::timeline::

- title: Stability fixes for diff highlighting
  sub_title: "2025-12-29"
  content: Released stability fixes for diff highlighting and manual review stats.

- title: Improved Windows auto-review reliability
  sub_title: "2025-12-16"
  content: Improved Windows auto-review reliability and error handling.

- title: Auto reviews for enterprise users
  sub_title: "2025-12-11"
  content: Released auto reviews for enterprise users.

- title: Instant Review tabs in VS Code
  sub_title: "2025-12-09"
  content: Added Instant Review tabs to the main IDE view and SCM view in VS Code-based IDEs.

- title: Improved extension performance and usability
  sub_title: "2025-12-05"
  content: Improved extension performance and usability, including smoother navigation between tabs and better handling of large highlighted code blocks.

- title: New review-actions UI
  sub_title: "2025-12-04"
  content: Released a new review-actions UI for current file, uncommitted changes, and review launch from the extension.

- title: Code block review from VS Code
  sub_title: "2025-12-03"
  content: Added the ability to review a selected code block directly from VS Code-based IDEs.

::/timeline::

## November 2025

::timeline::

- title: Claude Code custom commands
  sub_title: "2025-11-28"
  content: Added support for Claude Code custom commands.

- title: Antigravity integration
  sub_title: "2025-11-26"
  content: Released the Antigravity integration.

- title: New get started experience
  sub_title: "2025-11-26"
  content: Added a new Get Started experience in the extension.

- title: Improved Claude Code setup on Windows
  sub_title: "2025-11-24"
  content: Improved Claude Code setup on Windows.

- title: Manual review for uncommitted changes
  sub_title: "2025-11-20"
  content: Added manual review for uncommitted changes and the open file directly from VS Code, Cursor, and Windsurf extensions.

- title: Improved Claude Code support on Windows
  sub_title: "2025-11-14"
  content: Improved Claude Code support on Windows.

- title: Improved diff generation and embeddings quality
  sub_title: "2025-11-13"
  content: Improved diff generation and embeddings quality.

- title: Improved extension networking reliability
  sub_title: "2025-11-06"
  content: Improved extension networking reliability.

- title: Windsurf integration
  sub_title: "2025-11-04"
  content: Released Windsurf integration.

- title: Improved extension discovery and issue visibility
  sub_title: "2025-11-04"
  content: Improved extension discovery and issue visibility with automatic panel expansion, login reminders, and related UI fixes.

- title: Agent rules support for Windsurf
  sub_title: "2025-11-03"
  content: Added agent rules support for Windsurf.

- title: Improved billing visibility
  sub_title: "2025-11-03"
  content: Improved billing visibility in the platform UI and fixed a team-billing edge case.

::/timeline::

## October 2025

::timeline::

- title: Improved AI fix explanations
  sub_title: "2025-10-28"
  content: Improved how Claude Code and Codex explain findings before applying fixes.

- title: Fixed installation and Windows path issues
  sub_title: "2025-10-28"
  content: Fixed installation and Windows path issues affecting VS Code and Cursor reliability.

- title: Improved support for older VS Code versions
  sub_title: "2025-10-27"
  content: Improved support for older VS Code versions and environments without Node.js installed.

- title: Codex support in VS Code
  sub_title: "2025-10-27"
  content: Released Codex support inside VS Code.

- title: GitLab authentication and project rules
  sub_title: "2025-10-23"
  content: Added GitLab authentication and project-rules support.

- title: Codex CLI support
  sub_title: "2025-10-23"
  content: Released Codex CLI support.

- title: Automatic setup for VS Code
  sub_title: "2025-10-22"
  content: Released automatic setup for the VS Code integration.

- title: Automatic sign-in from website
  sub_title: "2025-10-21"
  content: Added automatic sign-in to the extension when installation starts from the website.

- title: Improved setup checks and Windows Claude Code support
  sub_title: "2025-10-16"
  content: Improved setup checks in the extension and Windows support for Claude Code installation.

- title: Improved Cursor integration
  sub_title: "2025-10-15"
  content: Improved Cursor integration with more reliable session handling and multi-session support.

- title: Fixed startup issue in VS Code and Cursor
  sub_title: "2025-10-14"
  content: Fixed a startup issue that could affect VS Code and Cursor after launch or project switching.

- title: Team Rules experience
  sub_title: "2025-10-14"
  content: Released the Team Rules experience.

- title: Improved Windows support for Claude Code
  sub_title: "2025-10-13"
  content: Improved Windows support for Claude Code installation.

- title: Fixed Windows setup issue
  sub_title: "2025-10-10"
  content: Fixed a Windows setup issue that could block code review integration from running.

- title: Simplified Claude Code installation
  sub_title: "2025-10-09"
  content: Simplified installing the Claude Code integration from the website.

- title: Extension version 0.0.31
  sub_title: "2025-10-03"
  content: Released extension version 0.0.31 with review-card and review-details improvements.

- title: Improved Cursor history extraction
  sub_title: "2025-10-01"
  content: Improved Cursor history extraction.

::/timeline::

## September 2025

::timeline::

- title: Local context generation
  sub_title: "2025-09-30"
  content: Released local context generation behind a feature flag to improve review context.

- title: Updated Windows IDE login redirect
  sub_title: "2025-09-22"
  content: Updated the Windows IDE login-redirect experience.

- title: Post-trial tool access
  sub_title: "2025-09-22"
  content: Allowed users whose trial had ended to continue running kluster tools while reviewing results manually.

- title: Improved VS Code prompt stability
  sub_title: "2025-09-19"
  content: Improved VS Code prompt stability after an IDE update.

- title: Rules management and GitHub connection in extensions
  sub_title: "2025-09-18"
  content: Released rules management and GitHub connection support in the VS Code and Cursor extensions.

- title: Improved VS Code extension setup
  sub_title: "2025-09-08"
  content: Improved setup flow in the VS Code extension with a dedicated kluster tab and better install-state handling.

- title: Improved Claude Code installation
  sub_title: "2025-09-05"
  content: Improved Claude Code installation for environments with multiple aliases and fixed an extension setup issue that could leave new users stuck during installation.

- title: Updated VS Code and Cursor extension builds
  sub_title: "2025-09-04"
  content: Released updated VS Code and Cursor extension builds.

- title: New Cursor extension with automatic setup
  sub_title: "2025-09-03"
  content: Released a new Cursor extension with automatic setup.

- title: Rules management in platform UI
  sub_title: "2025-09-03"
  content: Released rules management in the platform UI, improved prompts for VS Code and Claude Code, and added support for Stripe coupon codes and subscriptions without an attached payment method.

- title: Fixed Claude Code rules-file handling
  sub_title: "2025-09-01"
  content: Fixed Claude Code rules-file handling and released a new Cursor project-rules prompt with better review reliability.

::/timeline::
