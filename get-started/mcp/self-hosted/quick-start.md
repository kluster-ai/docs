---
title: Quick Start
description: Get kluster.ai's example MCP server running in five minutes with Docker to experience Verify service integration.
---

# Quick Start

This example MCP server demonstrates how kluster.ai services can integrate into development workflows. It showcases the [Verify service](/get-started/verify/reliability/overview){target=self} through two reliability verification tools.

## About This Implementation

This self-hosted MCP server is an **example implementation** designed to:

- **Demonstrate MCP integration**: Show how kluster.ai services work as AI tools.
- **Showcase Verify service**: Experience [Reliability check](/get-started/verify/reliability/overview/){target=self} in your workflow.
- **Enable local development**: Run privately with full control.

*This represents one example of kluster.ai's MCP capabilities, focusing on [Verify service](/get-started/verify/overview){target=_blank} tools.*

## Prerequisites

Before getting started with MCP integration, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'
- **[Docker Desktop](https://www.docker.com/products/docker-desktop/){target=_blank}** installed and running.
- **[Git](https://git-scm.com/){target=_blank}** for cloning the repository.
- **[Claude Desktop](https://claude.ai/download){target=_blank}** for testing (or another MCP client).

## Setup

### Step 1: Build the MCP server

Clone the [MCP Verify server](https://github.com/kluster-ai/verify-mcp) and build the Docker image.

```bash
git clone https://github.com/kluster-ai/verify-mcp
cd verify-mcp
docker build -t kluster-verify-mcp .
```

### Step 2: Configure Claude Desktop

Open your Claude Desktop configuration file and update and add the MCP server:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "kluster-verify-mcp": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "--interactive",
        "kluster-verify-mcp",
        "--api-key",
        "YOUR_API_KEY"
      ]
    }
  }
}
```

**Replace `YOUR_API_KEY`** with your actual API key.

### Step 3: Restart Claude Desktop

Close and reopen Claude Desktop to load the new server.

## How to use

Once you have reopened the MCP client (Claude Desktop), you should be able to see the tools listed under `kluster-verify-mcp`.

### Verify 

Ask Claude to verify something obviously wrong:

> "Use the Verify tool and tell me if The Eiffel Tower is located in Rome".

Claude should automatically use the `verify` tool and provide:

- **Verification result**: Whether the claim is accurate.
- **Detailed explanation**: Why it's wrong with supporting reasoning.
- **Source citations**: Search results used for verification.

![Verify MCP tool demo](/images/get-started/mcp/claude_desktop_verify_claim.webp)

### Verify document

Ideal for detecting hallucinations or false claims from documents. Upload any document to Claude, then ask to verify against a statement:

> "This document says X. Use the verify_document tool and check if that's accurate."

Claude should use the `verify_document` tool to verify your claim against the actual document content.

## Next Steps

- **Learn the tools**: See [Tools Reference](/get-started/mcp/self-hosted/tools/){target=\_self} for detailed parameters and examples.
- **Setup other clients**: Check [Client Setup](/get-started/mcp/self-hosted/clients/){target=\_self} for VS Code, n8n, and Dify integration.
- **Reliability check tutorial**: Follow the [reliability check notebook](/tutorials/klusterai-api/reliability-check){target=\_blank} tutorial with code examples.

