---
title: Clients
description: Configure kluster verify's MCP server with Claude Desktop, VS Code, and other MCP-compatible platforms.
---

# Clients

Configure the kluster verify MCP server with MCP-compatible clients that support the Model Context Protocol.

## Claude Desktop

Full MCP support with automatic tool selection and document parsing.

### Docker Setup (Recommended)

1. **Build the server**:
   ```bash
   # TODO: Define MCP repository URL
   git clone https://github.com/kluster-ai/hallucination-mcp-server
   cd verify-mcp-server  # TODO: Update folder name when repo is renamed
   npm run docker:build
   ```

2. **Configure Claude Desktop**:
   
   Edit your configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

   ```json
   {
     "mcpServers": {
       "kluster-verify": {
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

3. **Restart Claude Desktop** to load the server

### Node.js Setup

Alternative to Docker for development environments:

```json
{
  "mcpServers": {
    "kluster-verify": {
      "command": "node",
      "args": ["/path/to/verify-mcp-server/dist/index.js"],
      "env": {
        "KLUSTER_API_KEY": "api_key"
      }
    }
  }
}
```

### Features

- **Real-time fact-checking** - Verify statements as you type
- **Document verification** - Check claims against uploaded documents  
- **Contextual integration** - Works seamlessly within conversations

## VS Code

Integrate reliability checking directly into your development workflow.

### MCP Extension Setup

1. **Install MCP Extension** from VS Code marketplace
2. **Configure server** in VS Code settings:
   ```json
   {
     "mcp.servers": {
       "kluster-verify": {
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

3. **Restart VS Code** to activate the integration

### Features

- **Code comment verification** - Fact-check claims in documentation
- **Inline fact-checking** - Verify statements while coding
- **Agent Mode support** - Secure API key handling

## SSE Connection Type

For platforms that don't support native MCP but need HTTP endpoints, the server provides SSE (Server-Sent Events) support.

### SSE Server Setup

The SSE server provides HTTP endpoints for non-MCP platforms:

1. **Start the SSE server**:
   ```bash
   npm run sse:start -- --api-key YOUR_KLUSTER_AI_API_KEY
   ```

2. **Server runs on**: `http://localhost:3000`

### Available Endpoints

- **Fact Check**: `POST http://localhost:3000/mcp/fact_check`
- **Document Check**: `POST http://localhost:3000/mcp/document_claim_check`

### Request Format

```json
{
  "claim": "Statement to verify",
  "return_search_results": true
}
```

!!! info "Workflow Integrations"
    For platforms like Dify, n8n, and Zapier that use HTTP requests, see [Workflow Integrations](/get-started/verify/reliability/workflow-integrations/){target=_self}

## Additional Resources

- **Quick Start** - Get running in [5 minutes](/get-started/verify/reliability/mcp/quick-start/){target=_self}
- **Tools Reference** - Detailed [parameter documentation](/get-started/verify/reliability/mcp/tools/){target=_self}
- **MCP Integration** - Return to the [main guide](/get-started/verify/reliability/mcp/){target=_self}
- **Workflow Integrations** - HTTP-based [workflow templates](/get-started/verify/reliability/workflow-integrations/){target=_self}