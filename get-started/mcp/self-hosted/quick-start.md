---
title: Quick Start
description: Get kluster verify's MCP reliability verification server running in five minutes with Docker and test it with a working example.
---

# Quick Start

Self-hosted MCP lets you run the kluster verify MCP server on your own infrastructure. Perfect for developers who need local development, full control, and data privacy.

## Why Self-hosted?

- **Developer-friendly**: Test and debug locally before production
- **Full control**: Customize configuration and deployment
- **Data privacy**: Keep sensitive information within your infrastructure
- **No external dependencies**: Works offline once configured

## Prerequisites

Before getting started with MCP integration, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'
- **[Docker Desktop](https://www.docker.com/products/docker-desktop/){target=_blank}** installed and running
- **[Git](https://git-scm.com/){target=_blank}** for cloning the repository
- **[Claude Desktop](https://claude.ai/download){target=_blank}** for testing (or another MCP client)

## Setup

### Step 1: Build the MCP Server

```bash
git clone https://github.com/kluster-ai/verify-mcp
cd verify-mcp
docker build -t kluster-verify-mcp .
```

### Step 2: Configure Claude Desktop

Add this to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "kluster-verify": {
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

## Test It Works

Ask Claude to verify something obviously wrong:

> "Can you verify this claim: The Eiffel Tower is located in Rome"

Claude should automatically use the `verify` tool and return:
- **Result**: False
- **Explanation**: Why it's wrong
- **Sources**: Supporting evidence

## Test Document Verification

Upload any document to Claude, then ask:

> "This document says X. Can you verify if that's accurate?"

Claude should use the `verify_document` tool to verify your claim against the actual document content.

## Troubleshooting

**Tool not available**: 
- Verify Docker is running
- Check your API key is correct
- Restart Claude Desktop

**Authentication errors**:
- Confirm your kluster.ai API key has active credits
- Check the key has permissions for verify service

## Next Steps

- **Learn the tools**: See [Tools Reference](/get-started/mcp/self-hosted/tools/){target=\_self} for detailed parameters and examples
- **Setup other clients**: Check [Client Setup](/get-started/mcp/self-hosted/clients/){target=\_self} for VS Code, n8n, and Dify integration
- **Production deployment**: Contact support for scaling recommendations

## Additional Resources

- **API documentation**: Review the complete [API reference](/api-reference/reference/){target=\_blank}
- **Tutorials**: Explore [practical examples](/tutorials/klusterai-api/reliability-check){target=\_blank}