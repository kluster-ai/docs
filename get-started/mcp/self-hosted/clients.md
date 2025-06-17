---
title: Clients
description: Configure kluster.ai's self-hosted MCP server with Claude desktop, VS Code, and other MCP-compatible platforms for seamless development workflow integration.
---

# Clients

Configure [kluster.ai](https://www.kluster.ai/){target=\_blank}'s self-hosted MCP server with MCP-compatible clients to integrate verification tools directly into your development environment. The server supports multiple client platforms including Claude desktop, VS Code, and HTTP-based integrations.

This guide covers setup procedures for each supported platform, from Docker-based deployment to Node.js development environments and SSE server configurations for workflow automation. 

## Claude desktop

Claude desktop provides the most seamless MCP integration with automatic tool discovery and document parsing capabilities to easily test the `verify_document`tool

### Docker (recommended) 

1. Build the MCP server: Clone the GitHub repository and use Docker to build the server:
   ```bash
   git clone https://github.com/kluster-ai/verify-mcp
   cd verify-mcp
   docker build -t kluster-verify-mcp .
   ```

2. Configure Claude desktop:
   
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
                "INSERT_YOUR_API_KEY"
            ]
        }
    }
}
```

3. Restart Claude desktop to load the server.

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
                "KLUSTER_API_KEY": "INSERT_YOUR_API_KEY"
            }
        }
    }
}
```

## VS Code

Visual Studio Code allows the use of MCP servers in your development workflow.
In [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers){target=\_blank}, MCP support enhances GitHub Copilot's agent mode by allowing you to connect any MCP-compatible server to your agentic coding workflow.

### Docker (recommended) 

1. Build the MCP server (if not already built):
   ```bash
   git clone https://github.com/kluster-ai/verify-mcp
   cd verify-mcp
   docker build -t kluster-verify-mcp .
   ```

2. Create `.vscode/mcp.json` in your workspace root:

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

### Node.js

For development or when Docker isn't available:

1. Build the MCP server (if not already built):
   ```bash
   git clone https://github.com/kluster-ai/verify-mcp
   cd verify-mcp
   npm install
   npm run build
   ```

2. Create `.vscode/mcp.json`** in your workspace root:

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

!!! tip "Alternative setup"
    Run `MCP: Add Server` from the Command Palette and choose `Workspace Settings`. Restart VS Code to activate the integration.

## Additional resources

- **Quick start**: Get running in [five minutes](/get-started/mcp/self-hosted/get-started/).
- **Tools reference**: Detailed [parameter documentation](/get-started/mcp/self-hosted/tools/).
- **Workflow integrations**: HTTP-based [workflow templates](/get-started/verify/reliability/workflow-integrations/).