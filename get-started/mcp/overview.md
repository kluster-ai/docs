---
title: MCP Integration
description: Connect AI applications to kluster.ai services using the Model Context Protocol for seamless development workflow integration.
---

# MCP integration

[Model Context Protocol](https://modelcontextprotocol.io/introduction){target=_blank} or MCP, is an open standard for connecting AI assistants to specialized tools. 

Think of it as "USB-C for AI" - one protocol that works everywhere.

kluster.ai provides MCP servers that bring AI services directly into your development workflow.

## What is MCP?

MCP lets AI applications access external capabilities:

- **Local tools**: Files, databases, custom functions.
- **Remote services**: APIs, web services, cloud resources.
- **Specialized features**: Like kluster.ai's verification technology.

Switch between AI providers while keeping the same tools - just like USB-C devices.

## Why MCP for kluster.ai services?

Instead of managing API calls and integrations, access kluster.ai's AI capabilities as native tools in Claude Desktop, VS Code, and other MCP-compatible platforms.

## Self-hosted MCP server

Example implementation showcasing kluster.ai's [Verify service](/get-started/verify/reliability/overview){target=self} capabilities through two tools:

**`verify`**: Validates claims against reliable sources.

**`verify_document`**: Verifies claims about uploaded documents.

This demonstrates how kluster.ai services can integrate seamlessly into development environments via MCP with the [Self-hosted MCP server](/get-started/mcp/self-hosted/quick-start/){target=self}.



## Get started

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Self-hosted MCP Server__

    ---

    Run the Verify MCP server locally with Docker or nodejs. Use it with Claude Desktop, VS Code or your preferred MCP Client.

    [:octicons-arrow-right-24: Five-minute setup](/get-started/mcp/self-hosted/quick-start/){target=\_self}

-   <span class="badge integration">Integration</span> __Platform MCP__

    ---

    Coming soon.

    [:octicons-arrow-right-24: Learn more](/get-started/mcp/platform/){target=\_self}

</div>

## Additional resources

- **MCP Protocol**: [Official MCP documentation](https://modelcontextprotocol.io/docs){target=\_blank}
- **Verify service**: [Complete reliability verification guide](/get-started/verify/reliability/overview){target=\_blank}
- **API Reference**: [kluster.ai API documentation](/api-reference/reference/){target=\_blank}