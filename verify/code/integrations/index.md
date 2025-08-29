---
title: IDE Integrations for kluster.ai Verify Code
description: Choose your IDE integration method for kluster.ai Verify Code with native one-click installation or manual MCP configuration.
---

# Integrations

The [kluster.ai](https://www.kluster.ai/){target=\_blank} Verify Code service integrates directly into your IDE workflow, providing real-time code analysis as you develop. Choose the integration method that best fits your development environment.

## Choose your integration type

<div class="grid cards" markdown>

-   __Native IDE integration__

    ---

    One-click installation with custom extensions, specialized AI prompts, and seamless UI integration.
    
    **Supported IDEs:**
    
    - Cursor
    - VS Code  
    - Claude Code
    
    [:octicons-arrow-right-24: Set up Native IDEs](/verify/code/integrations/native/){target=\_blank}

-   __MCP compatible__

    ---

    Manual configuration for any MCP-compatible IDE using the standard protocol.
    
    **Supported IDEs:**
    
    - Windsurf
    - Cline
    - Roo Code
    - Kilo Code
    - Other MCP clients
    
    [:octicons-arrow-right-24: Set up MCP IDEs](/verify/code/integrations/mcp/){target=\_blank}

</div>

!!! tip "Not sure which to choose?"
    If you're using Cursor, VS Code, or Claude Code, choose the [Native IDE integration](/verify/code/integrations/native/){target=\_blank} for the best experience.
    For all other IDEs, use the [MCP compatible setup](/verify/code/integrations/mcp/){target=\_blank}.

## How it works

Regardless of your integration type, Verify Code operates the same way:

1. **Monitors code generation**: Watches as AI assistants generate code.
2. **Analyzes changes**: Evaluates code diffs in real-time.
3. **Detects issues**: Identifies bugs, security flaws, and quality problems.
4. **Provides fixes**: Suggests specific corrections with priority levels.
5. **Enables auto-fix**: AI incorporates feedback to fix issues immediately.

## Available tools

Both integration types provide access to the same verification tools:

- **`kluster_code_review_auto`**: For code security and quality verification.
- **`kluster_dependency_validator`**: For dependency validation.

Learn more about these tools in the [Tools reference](/verify/code/tools/){target=\_blank} page.