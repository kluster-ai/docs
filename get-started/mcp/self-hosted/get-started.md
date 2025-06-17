---
title: Get started with MCP
description: Get kluster.ai's self-hosted MCP server running in five minutes with Docker to integrate Verify service tools into your development workflow.
---

# Get started

This example MCP server demonstrates how kluster.ai services can integrate into development workflows through the Model Context Protocol. The implementation showcases the [Verify service](/get-started/verify/reliability/overview) with two reliability verification tools that enable real-time claim validation directly within AI assistant conversations.

This guide walks through the complete setup process, from building the Docker container to configuring Claude desktop integration. You'll learn how to deploy the MCP server locally, test the verification tools, and integrate them into your development workflow.

## About this implementation

This self-hosted MCP server is an **example implementation** designed to:

- **Demonstrate MCP integration**: Show how kluster.ai services work as AI tools.
- **Showcase Verify service**: Experience [Reliability check](/get-started/verify/reliability/overview/) in your workflow.
- **Enable local development**: Run privately with full control.

*This represents one example of kluster.ai's MCP capabilities, focusing on [Verify service](/get-started/verify/overview){target=\_blank} tools.*

## Prerequisites

Before getting started with MCP integration, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'
- **[Docker Desktop](https://www.docker.com/products/docker-desktop/){target=\_blank}** installed and running.
- **[Git](https://git-scm.com/){target=\_blank}** for cloning the repository.
- **[Claude desktop](https://claude.ai/download){target=\_blank}** for testing (or another MCP client).

## Setup

### Step 1: Build the MCP server

Clone the [MCP Verify server](https://github.com/kluster-ai/verify-mcp){target=\_blank} and build the Docker image.

```bash
git clone https://github.com/kluster-ai/verify-mcp
cd verify-mcp
docker build -t kluster-verify-mcp .
```

### Step 2: Configure Claude desktop

Open your Claude desktop configuration file and update and add the MCP server:

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
                "INSERT_YOUR_API_KEY"
            ]
        }
    }
}
```

**Replace `INSERT_YOUR_API_KEY`** with your actual API key.

### Step 3: Restart Claude desktop

Close and reopen Claude desktop to load the new server.

![List tools on Claude desktop](/images/get-started/mcp/self-hosted/quick-start/quick-start-1.webp)

## How to use

Once you have reopened the MCP client (Claude desktop), you should be able to see the tools listed under `kluster-verify-mcp`.

### Verify 

Ask Claude to verify something obviously wrong:

> "Use the Verify tool and tell me if The Eiffel Tower is located in Rome".

Claude should automatically use the `verify` tool and provide:

- **Verification result**: Whether the claim is accurate.
- **Detailed explanation**: Why it's wrong with supporting reasoning.
- **Source citations**: Search results used for verification.

![Verify MCP tool demo](/images/get-started/mcp/self-hosted/quick-start/quick-start-2.webp)

### Verify document

Ideal for detecting hallucinations or false claims from documents. Upload any document to Claude, then ask to verify against a statement:

> "This document says X. Use the verify_document tool and check if that's accurate."

Claude should use the `verify_document` tool to verify your claim against the actual document content.

## Next steps

- **Learn the tools**: See [Tools Reference](/get-started/mcp/self-hosted/tools/) for detailed parameters and examples.
- **Setup other clients**: Check [Client Setup](/get-started/mcp/self-hosted/clients/) for VS Code, n8n, and Dify integration.
- **Reliability check tutorial**: Follow the [reliability check notebook](/tutorials/klusterai-api/reliability-check){target=\_blank} tutorial with code examples.

