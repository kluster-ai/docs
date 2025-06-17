---
title: MCP Integration
description: Connect AI applications to kluster.ai services using the Model Context Protocol for seamless development workflow integration with verification tools and automated reliability checking.
---

# MCP integration

[Model Context Protocol](https://modelcontextprotocol.io/introduction){target=\_blank} or MCP, is an open standard for connecting AI assistants to specialized tools. Think of it as "USB-C for AI" - one protocol that works everywhere, enabling seamless integration between AI applications and external capabilities.

[kluster.ai](https://www.kluster.ai/){target=\_blank} provides MCP servers that bring AI services directly into your development workflow. This documentation covers self-hosted implementations for local development, tools overview and client integration.

## What is MCP?

MCP lets AI applications access external capabilities:

- **Local tools**: Files, databases, custom functions.
- **Remote services**: APIs, web services, cloud resources.
- **Specialized features**: Like kluster.ai's verification technology.

Switch between AI providers while keeping the same tools - just like USB-C devices.

## MCP through kluster.ai services

Instead of managing API calls and integrations, access kluster.ai's AI capabilities as native tools in Claude desktop, VS Code, and other MCP-compatible platforms.

You can integrate kluster.ai services via MCP in two ways: self-hosted for local developlment, or platform managed services for simplified deployment.

### Self-hosted MCP

Example implementation showcasing kluster.ai's [Verify service](/get-started/verify/reliability/overview) capabilities through two tools:

**`verify`**: Validates claims against reliable sources.

**`verify_document`**: Verifies claims about uploaded documents.

This demonstrates how kluster.ai services can integrate seamlessly into development environments via MCP with the [self-hosted MCP server](/get-started/mcp/self-hosted/get-started/).

### Platform MCP

Coming soon - managed MCP endpoints that eliminate setup complexity while providing the same verification capabilities and access to more tools.

## How to integrate MCP

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Self-hosted MCP server__

    ---

    Run the Verify MCP server locally with Docker or Nodejs. Use it with Claude desktop, VS Code or your preferred MCP Client.

    [:octicons-arrow-right-24: Five-minute setup](/get-started/mcp/self-hosted/get-started/)

-   <span class="badge integration">Integration</span> __Platform MCP__

    ---

    Coming soon.

    [:octicons-arrow-right-24: Learn more](/get-started/mcp/platform/)

</div>

## Additional resources

- **MCP protocol**: [Official MCP documentation](https://modelcontextprotocol.io/docs){target=\_blank}
- **Verify service**: [Complete reliability verification guide](/get-started/verify/reliability/overview)
- **API reference**: [kluster.ai API documentation](/api-reference/reference/)