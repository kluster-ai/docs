---
title: MCP integration overview
description: Connect AI apps to kluster.ai services using MCP for seamless development workflow integration with verification tools and automated reliability checking.
---

# MCP integration

[Model Context Protocol](https://modelcontextprotocol.io/introduction){target=\_blank} (MCP) is an open standard for connecting AI assistants to specialized tools. Think of it as "USB-C for AI" - one protocol that works everywhere, enabling seamless integration between AI applications and external capabilities.

[kluster.ai](https://www.kluster.ai/){target=\_blank} provides MCP servers that bring AI services directly into your development workflow. Choose between a managed cloud endpoint or self-hosted deployment for seamless integration across platforms.

## What is MCP?

MCP lets AI applications access external capabilities:

- **Local tools**: Files, databases, custom functions.
- **Remote services**: APIs, web services, cloud resources.
- **Specialized features**: Like kluster.ai's verification technology.

## MCP through kluster.ai services

Instead of managing API calls and integrations, access kluster.ai's AI capabilities as native tools in Claude desktop, VS Code, and other MCP-compatible platforms.

The kluster.ai MCP offers the [Verify service](/verify/reliability/overview){target=\_blank} through two deployment options designed for different use cases and platforms.

### Cloud MCP

Managed cloud implementation - no infrastructure to maintain:

--8<-- 'text/verify/mcp/overview/overview-1.md'

Enable your endpoint through the kluster.ai platform, get your MCP token, and start verifying. Works with any MCP client using standard connection patterns.

### Self-hosted MCP

Same verification tools running on your infrastructure with full control. Deploy locally with Docker or Node.js.

## Integrate MCP

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Get started with MCP__

    ---

    Quick start guide using Cloud MCP as the default path. Enable your endpoint and connect Claude Desktop in five minutes.

    [:octicons-arrow-right-24: Five-minute setup](/verify/mcp/get-started/){target=_self}

-   <span class="badge guide">Guide</span> __Cloud MCP__

    ---

    Enable managed MCP endpoints with MCP token authentication. There is no infrastructure to maintain, just enable and integrate.

    [:octicons-arrow-right-24: Platform setup](/verify/mcp/cloud/platform/){target=_self}

-   <span class="badge guide">Guide</span> __Self-hosted MCP__

    ---

    Deploy the MCP server locally with Docker or Node.js. Perfect for development and testing with full control.

    [:octicons-arrow-right-24: Local deployment](/verify/mcp/self-hosted/){target=_self}

</div>

## Additional resources

- **MCP protocol**: [Official MCP documentation](https://modelcontextprotocol.io/docs){target=\_blank}.
- **Verify service**: [Complete reliability verification guide](/verify/reliability/overview).
- **API reference**: [kluster.ai API documentation](/api-reference/reference/).