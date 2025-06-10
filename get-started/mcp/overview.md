---
title: MCP Integration
description: Connect AI applications to external tools and data sources using the Model Context Protocol, with kluster's ready-to-use MCP servers.
---

# MCP Integration

The Model Context Protocol (MCP) is an open standard for connecting AI assistants to external tools and data sources. Think of it as the "USB-C port for AI applications" – a universal way to plug different capabilities into your AI workflows.

## What is MCP?

MCP standardizes how AI applications access:

- **Local data**: Files, databases, and services on your computer
- **Remote services**: APIs, web services, and cloud resources  
- **Custom tools**: Specialized functions for your specific needs

With MCP, you can switch between AI providers while keeping the same tool integrations, similar to how USB-C works across different devices.

## Why kluster Supports MCP

kluster embraces MCP to help developers build more capable AI applications. By providing pre-built MCP servers, kluster makes it easy to add specialized capabilities to any MCP-compatible environment like Claude Desktop, VS Code, or automation platforms.

## Example: kluster verify MCP Server

As an example of MCP in action, kluster offers a verify MCP server that adds reliability checking capabilities to your AI assistant. This server provides two specialized tools:

**`fact_check`**: Verify any statement against reliable sources
**`document_claim_check`**: Verify claims about uploaded documents

This is just one example of how MCP can extend AI capabilities. The protocol supports any type of tool or data integration you need.

## How MCP Works

MCP follows a client-server architecture:

1. **MCP Hosts**: Your AI application (Claude Desktop, VS Code, etc.)
2. **MCP Servers**: Programs that expose specific capabilities
3. **Protocol**: Standardized communication between hosts and servers
4. **Tools**: Functions that servers provide to AI assistants

## Available MCP Implementations

kluster currently offers the verify MCP server, with more implementations planned:

### kluster verify MCP Server

The verify MCP server adds reliability checking to your AI workflows:

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Self-hosted verify MCP__

    ---

    Run the verify MCP server locally with Docker or Node.js. Perfect for developers who want full control over reliability checking.

    [:octicons-arrow-right-24: Setup self-hosted](/get-started/mcp/self-hosted/quick-start/){target=\_self}

-   <span class="badge integration">Integration</span> __Platform verify MCP__

    ---

    Cloud-hosted verify MCP endpoints for no-code platforms. Coming soon.

    [:octicons-arrow-right-24: Learn more](/get-started/mcp/platform/){target=\_self}

</div>

## Getting Started with MCP

To use any MCP server with your AI application:

1. **Choose an MCP-compatible client** (Claude Desktop, VS Code, etc.)
2. **Select an MCP server** that provides the tools you need
3. **Configure the connection** in your client settings
4. **Start using the tools** in your AI conversations

## Learn More

- **MCP Protocol**: Read the [official MCP documentation](https://modelcontextprotocol.io/docs){target=\_blank} by Anthropic
- **kluster verify**: Explore the [reliability checking service](/get-started/verify/reliability/){target=\_blank}
- **API Reference**: Review the [kluster.ai API documentation](/api-reference/reference/){target=\_blank}