---
title: Integration
description: Add fact-checking to your LLM applications using kluster verify's MCP server with automated claim verification and document validation tools.
---

# Integration

LLM applications generate convincing but false information. This breaks user trust and creates liability. The **kluster verify MCP server** solves this by adding real-time fact-checking to any MCP-compatible environment.

## Why kluster verify Built an MCP Server

**The problem**: Your LLM applications work great until they confidently state wrong facts. Users lose trust. You lose credibility.

**Our solution**: Two specialized tools that catch false claims before users see them.

**Why MCP**: Works across Claude Desktop, VS Code, n8n, and other platforms you already use. No API changes to your existing code.

## Prerequisites

Before getting started with MCP integration, ensure the following requirements are met:

- **kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you do not have one
- **kluster.ai API key** - after signing in, go to the [API Keys](https://platform.kluster.ai/apikeys){target=_blank} section and create a new key. For detailed instructions, see the [Get an API key](https://docs.kluster.ai/get-started/get-api-key/){target=_blank} guide
- **Docker** installed on your system
- **MCP-compatible client** such as Claude Desktop, VS Code, n8n, or Dify

## What You Get

Two tools that integrate directly into your workflow:

**`fact_check`** - Verify any statement against reliable sources
```json
Input: "The Eiffel Tower is in Rome"
Output: "False. Located in Paris, France. [Sources included]"
```

**`document_claim_check`** - Verify claims about uploaded documents  
```json
Input: "This contract allows remote work"
Output: "False. Section 4.2 requires office presence. [Exact quotes]"
```

Both tools return structured responses with explanations and source citations.

## Choose Your Setup

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Quick Start__

    ---

    Get running in five minutes with Docker. Perfect for testing and development environments.

    [:octicons-arrow-right-24: Start here](/get-started/hallucination-agent/mcp/quick-start/){target=_self}

-   <span class="badge reference">Reference</span> __Tools Reference__

    ---

    Deep dive into fact_check and document_claim_check tools with examples and parameters.

    [:octicons-arrow-right-24: See tools](/get-started/hallucination-agent/mcp/tools/){target=_self}

-   <span class="badge integration">Integration</span> __Client Setup__

    ---

    Integrate with Claude Desktop, VS Code, n8n, Dify, and other MCP-compatible platforms.

    [:octicons-arrow-right-24: Setup clients](/get-started/hallucination-agent/mcp/clients/){target=_self}

</div>

## How it Works

The server integrates with your applications by:

1. **Exposing tools** through the standard MCP protocol
2. **Processing claims** using kluster.ai's verification API  
3. **Returning results** with explanations and source citations
4. **Working everywhere** MCP is supported

## Learn More About MCP

New to Model Context Protocol? Learn more in the [official MCP documentation](https://modelcontextprotocol.io/docs){target=_blank} by Anthropic.

## Additional Resources

- **Question/Answer detection** - Learn how to [verify individual question-answer pairs](/get-started/hallucination-agent/question-answer/){target=_self}
- **Chat Completion detection** - Discover how to [validate responses in conversations](/get-started/hallucination-agent/chat-completion/){target=_self}
- **Practical examples** - Explore our [Tutorials](/tutorials/klusterai-api/hallucination-detection-agent){target=_blank} for kluster verify
- **API reference** - Review the complete [API documentation](/api-reference/reference/){target=_blank} for all hallucination detection endpoints