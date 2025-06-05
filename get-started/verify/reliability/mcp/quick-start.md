---
title: Quick Start
description: Get kluster verify's MCP fact-checking server running in five minutes with Docker and test it with a working example.
---

# Quick Start

Get fact-checking working in your MCP client in five minutes.

## Prerequisites

Before getting started with MCP integration, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'
- **Docker** installed and running (see [Node.js setup](/get-started/verify/reliability/mcp/clients/#nodejs-setup){target=\_blank} for alternative)
- **Claude Desktop** for testing (or another MCP client)

## Setup

### Step 1: Get the Server

```bash
# TODO: Define MCP repository URL
git clone https://github.com/kluster-ai/hallucination-mcp-server
cd hallucination-mcp-server
npm run docker:build
```

### Step 2: Configure Claude Desktop

Add this to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "kluster-hallucination": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "kluster-mcp-server",
        "--api-key", "api_key"
      ]
    }
  }
}
```

**Replace `api_key`** with your actual API key.

### Step 3: Restart Claude Desktop

Close and reopen Claude Desktop to load the new server.

## Test It Works

Ask Claude to fact-check something obviously wrong:

> "Can you fact-check this claim: The Eiffel Tower is located in Rome"

Claude should automatically use the `fact_check` tool and return:
- **Result**: False
- **Explanation**: Why it's wrong
- **Sources**: Supporting evidence

## Test Document Verification

Upload any document to Claude, then ask:

> "This document says X. Can you verify if that's accurate?"

Claude should use the `document_claim_check` tool to verify your claim against the actual document content.

## Troubleshooting

**Tool not available**: 
- Verify Docker is running
- Check your API key is correct
- Restart Claude Desktop

**Authentication errors**:
- Confirm your kluster.ai API key has active credits
- Check the key has permissions for hallucination detection

## Next Steps

- **Learn the tools** - See [Tools Reference](/get-started/hallucination-agent/mcp-tools/){target=\_blank} for detailed parameters and examples
- **Setup other clients** - Check [Client Setup](/get-started/hallucination-agent/mcp-clients/){target=\_blank} for VS Code, n8n, and Dify integration
- **Production deployment** - Contact support for scaling recommendations

## Additional Resources

- **MCP Integration overview** - Return to the [main MCP guide](/get-started/hallucination-agent/mcp/){target=\_blank}
- **API documentation** - Review the complete [API reference](/api-reference/reference/){target=\_blank}
- **Tutorials** - Explore [practical examples](/tutorials/klusterai-api/hallucination-detection-agent){target=\_blank}