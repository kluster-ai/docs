---
title: Clients
description: Configure kluster verify's MCP server with Claude Desktop, VS Code, and other MCP-compatible platforms.
---

# Clients

Configure the kluster verify MCP server with MCP-compatible clients that support the Model Context Protocol.

## Claude Desktop

Full MCP support with automatic tool selection and document parsing.

### Docker Setup (Recommended)

1. **Build the MCP server**:
   ```bash
   git clone https://github.com/kluster-ai/verify-mcp
   cd verify-mcp
   docker build -t kluster-verify-mcp .
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

3. **Restart Claude Desktop** to load the server

### Node.js Setup

For development or when Docker isn't available:

```bash
git clone https://github.com/kluster-ai/verify-mcp
cd verify-mcp
npm install
npm run build
```

Configure with direct Node.js execution:

```json
{
  "mcpServers": {
    "kluster-verify": {
      "command": "node",
      "args": ["./dist/index.js"],
      "cwd": "/path/to/verify-mcp",
      "env": {
        "KLUSTER_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

**Custom Base URL**: For self-hosted kluster instances:

```json
{
  "mcpServers": {
    "kluster-verify": {
      "command": "node", 
      "args": ["./dist/index.js", "--api-key", "YOUR_API_KEY", "--base-url", "https://your-instance.com/v1"],
      "cwd": "/path/to/verify-mcp"
    }
  }
}
```

### Features

- **Real-time verification**: Verify statements as you type
- **Document verification**: Check claims against uploaded documents  
- **Contextual integration**: Works seamlessly within conversations

## VS Code

Integrate reliability checking directly into your development workflow.

### MCP Extension Setup

1. **Install MCP Extension** from VS Code marketplace
2. **Configure server** in VS Code settings:
   ```json
   {
     "mcp.servers": {
       "kluster-verify": {
         "command": "node",
         "args": ["./dist/index.js", "--api-key", "YOUR_API_KEY"],
         "cwd": "/path/to/verify-mcp"
       }
     }
   }
   ```

3. **Restart VS Code** to activate the integration

### Features

- **Code comment verification**: Verify claims in documentation
- **Inline reliability checking**: Verify statements while coding
- **Agent Mode support**: Secure API key handling

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
    For platforms like Dify, n8n, and Zapier that use HTTP requests, see [Workflow Integrations](/get-started/verify/reliability/workflow-integrations/){target=\_blank}

## Additional Resources

- **Quick Start**: Get running in [five minutes](/get-started/mcp/self-hosted/quick-start/){target=\_self}
- **Tools Reference**: Detailed [parameter documentation](/get-started/mcp/self-hosted/tools/){target=\_self}
- **Workflow Integrations**: HTTP-based [workflow templates](/get-started/verify/reliability/workflow-integrations/){target=\_blank}