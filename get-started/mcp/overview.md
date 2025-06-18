---
title: MCP Integration
description: Connect AI applications to kluster.ai services using the Model Context Protocol for seamless development workflow integration with verification tools and automated reliability checking.
---

# MCP integration

[Model Context Protocol](https://modelcontextprotocol.io/introduction){target=\_blank} or MCP, is an open standard for connecting AI assistants to specialized tools. Think of it as "USB-C for AI" - one protocol that works everywhere, enabling seamless integration between AI applications and external capabilities.

[kluster.ai](https://www.kluster.ai/){target=\_blank} provides MCP servers that bring AI services directly into your development workflow. This documentation covers self-hosted implementations for local development, tools overview and client integration.

## What is MCP?

MCP lets AI applications access external capabilities:

- **Local tools**: Files, databases, custom functions
- **Remote services**: APIs, web services, cloud resources
- **Specialized features**: Like kluster.ai's verification technology

Switch between AI providers while keeping the same tools - just like USB-C devices.

## MCP through kluster.ai services

Instead of managing API calls and integrations, access kluster.ai's AI capabilities as native tools in Claude desktop, VS Code, and other MCP-compatible platforms.

The kluster.ai MCP offers the [Verify service](/get-started/verify/reliability/overview) through two deployment options designed for different use cases and platforms.

### Self-hosted MCP

Local implementation using the stdio protocol, perfect for development environments and native MCP clients:

**`verify`**: Validates claims against reliable sources

**`verify_document`**: Verifies claims about uploaded documents

Deploy locally with Docker or Node.js for seamless integration into Claude desktop, VS Code, and other stdio-based MCP clients with the [self-hosted MCP server](/get-started/mcp/self-hosted/get-started/){target=_self}.

### Stream HTTP MCP

Cloud-based implementation using JSON-RPC over HTTP, ideal for workflow automation and no-code platforms:

**Same verification tools** with managed infrastructure - no servers to maintain, just enable and integrate. Perfect for platforms like Dify, n8n, and any HTTP-compatible automation tool.

Access through simple API management - enable your endpoint, get your API key, and start verifying with the [Stream HTTP MCP](/get-started/mcp/stream-http/platform/).

## How to integrate MCP

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Self-hosted MCP server__

    ---

    Run the Verify MCP server locally with Docker or Nodejs. Use it with Claude desktop, VS Code or your preferred MCP Client.

    [:octicons-arrow-right-24: Five-minute setup](/get-started/mcp/self-hosted/get-started/){target=_self}

-   <span class="badge integration">Integration</span> __Stream HTTP MCP__

    ---

    Enable managed MCP endpoints with API key authentication. Connect to Dify, n8n, and HTTP-based platforms without infrastructure setup.

    [:octicons-arrow-right-24: Platform setup](/get-started/mcp/stream-http/platform/){target=_self}

</div>

## Additional resources

- **MCP protocol**: [Official MCP documentation](https://modelcontextprotocol.io/docs){target=\_blank}
- **Verify service**: [Complete reliability verification guide](/get-started/verify/reliability/overview){target=_self}
- **API reference**: [kluster.ai API documentation](/api-reference/reference/){target=_self}