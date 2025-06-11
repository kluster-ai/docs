---
title: Clients
description: Configure kluster.ai's example MCP server with Claude Desktop, VS Code, and other MCP-compatible platforms.
---

# Clients

Configure kluster.ai's Self-hosted MCP server with compatible clients. 

## Claude Desktop

Full MCP support with automatic tool selection and document parsing.

### Docker (Recommended)

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

3. **Restart Claude Desktop** to load the server.

### Node.js

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
    "kluster-verify-mcp": {
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
## VS Code

Visual Studio Code allows the use of MCP servers in your development workflow.
In [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers){target=_blank}, MCP support enhances GitHub Copilot's agent mode by allowing you to connect any MCP-compatible server to your agentic coding workflow.

### Docker (Recommended)

1. **Build the MCP server** (if not already built):
   ```bash
   git clone https://github.com/kluster-ai/verify-mcp
   cd verify-mcp
   docker build -t kluster-verify-mcp .
   ```

2. **Create `.vscode/mcp.json`** in your workspace root:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "kluster-api-key",
      "description": "kluster.ai API Key",
      "password": true
    }
  ],
  "servers": {
    "kluster-verify": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "--interactive",
        "kluster-verify-mcp",
        "--api-key",
        "${input:kluster-api-key}"
      ]
    }
  }
}
```

#### Node.js

For development or when Docker isn't available:

1. **Build the MCP server** (if not already built):
   ```bash
   git clone https://github.com/kluster-ai/verify-mcp
   cd verify-mcp
   npm install
   npm run build
   ```

2. **Create `.vscode/mcp.json`** in your workspace root:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "kluster-api-key",
      "description": "kluster.ai API Key",
      "password": true
    }
  ],
  "servers": {
    "kluster-verify": {
      "type": "stdio",
      "command": "node",
      "args": ["./dist/index.js"],
      "cwd": "/path/to/verify-mcp",
      "env": {
        "KLUSTER_API_KEY": "${input:kluster-api-key}"
      }
    }
  }
}
```

!!! tip "Alternative Setup"
    Run `MCP: Add Server` from the Command Palette and choose `Workspace Settings`. Restart VS Code to activate the integration.

## SSE Server

For platforms that don't support native MCP but need HTTP endpoints, the verify-mcp repository includes an SSE (Server-Sent Events) server that provides standard HTTP API access to the verification tools.

### SSE Server Setup

1. **Start the SSE server**:
   ```bash
   git clone https://github.com/kluster-ai/verify-mcp
   cd verify-mcp
   npm run sse:start -- --api-key YOUR_KLUSTER_AI_API_KEY --port 3001
   ```

2. **Server runs on**: `http://localhost:3001` (default port).

### Available Endpoints

- **Tools List**: `GET http://localhost:3001/tools`
- **Health Check**: `GET http://localhost:3001/health`
- **SSE Connection**: `GET http://localhost:3001/sse`
- **Verify Tool**: `POST http://localhost:3001/tools/verify`
- **Verify Document Tool**: `POST http://localhost:3001/tools/verify_document`

### Request Format

**Verify Tool**:
```json
{
  "claim": "Statement to verify",
  "return_search_results": true
}
```

**Verify Document Tool**:
```json
{
  "claim": "This document says X",
  "document_content": "Full document text content...",
  "return_search_results": true
}
```

### Response Format

```json
{
  "success": true,
  "result": {
    "tool": "verify",
    "claim": "Statement to verify",
    "is_hallucination": false,
    "explanation": "Detailed verification explanation...",
    "usage": {
      "completion_tokens": 124,
      "prompt_tokens": 67,
      "total_tokens": 191
    },
    "search_results": []
  },
  "timestamp": "2025-06-11T10:30:00.000Z"
}
```

### Configuration Options

- `--api-key`: Your kluster.ai API key (or use `KLUSTER_API_KEY` env var)
- `--base-url`: kluster.ai base URL (default: `https://api.kluster.ai/v1`)
- `--port`: HTTP server port (default: `3001`)

### Usage Example

```bash
# Test verify tool
curl -X POST http://localhost:3001/tools/verify \
  -H "Content-Type: application/json" \
  -d '{"claim": "The Earth is flat", "return_search_results": true}'

# Check server health
curl http://localhost:3001/health
```

!!! info "Workflow Integrations"
    For platforms like Dify, n8n, and Zapier that use HTTP requests, see [Workflow Integrations](/get-started/verify/reliability/workflow-integrations/){target=\_blank}.

## Additional Resources

- **Quick Start**: Get running in [five minutes](/get-started/mcp/self-hosted/quick-start/){target=\_self}.
- **Tools Reference**: Detailed [parameter documentation](/get-started/mcp/self-hosted/tools/){target=\_self}.
- **Workflow Integrations**: HTTP-based [workflow templates](/get-started/verify/reliability/workflow-integrations/){target=\_blank}.