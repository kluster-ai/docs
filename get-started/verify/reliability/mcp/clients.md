---
title: Client Setup
description: Configure kluster verify's MCP fact-checking server with Claude Desktop, VS Code, n8n, Dify, and other MCP-compatible platforms.
---

# Client Setup

Configure the kluster verify MCP server across different development environments and platforms.

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
       "kluster-hallucination": {
         "command": "docker",
         "args": [
           "run", "-i", "--rm",
           "kluster-mcp-server",
           "--api-key", "YOUR_KLUSTER_AI_API_KEY"
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
    "kluster-hallucination": {
      "command": "node",
      "args": [
        "/path/to/hallucination-mcp-server/dist/index.js",
        "--api-key", "YOUR_KLUSTER_AI_API_KEY"
      ]
    }
  }
}
```

### Features

- **Automatic tool selection** - Claude picks the right verification tool
- **Document integration** - Upload files for claim verification
- **Real-time fact-checking** - Works during conversations
- **Source citations** - Complete with links and explanations

## VS Code Copilot Chat

Integrate fact-checking into your development workflow.

### Setup

1. **Install the MCP extension** (if available)
2. **Configure the server** in VS Code settings:

   ```json
   {
     "mcp": {
       "servers": {
         "kluster-hallucination": {
           "command": "docker",
           "args": [
             "run", "-i", "--rm", 
             "kluster-mcp-server",
             "--api-key", "YOUR_KLUSTER_AI_API_KEY"
           ]
         }
       }
     }
   }
   ```

3. **Restart VS Code** to activate the server

### Features

- **Code comment verification** - Fact-check claims in documentation
- **Inline fact-checking** - Verify statements while coding
- **Agent Mode support** - Secure API key handling

## n8n Workflows

Automate fact-checking in your n8n workflows using the SSE server.

### SSE Server Setup

The SSE (Server-Sent Events) server provides HTTP endpoints for platforms that don't support native MCP.

1. **Start the SSE server**:
   ```bash
   npm run sse:start -- --api-key YOUR_KLUSTER_AI_API_KEY
   ```

2. **Server runs on**: `http://localhost:3000`

### n8n Configuration

1. **Add HTTP Request node** to your workflow
2. **Configure the request**:
   - **URL**: `http://localhost:3000/mcp/fact_check`
   - **Method**: POST
   - **Headers**: `Content-Type: application/json`
   - **Body**:
     ```json
     {
       "claim": "{% raw %}{{ $json.statement }}{% endraw %}",
       "return_search_results": true
     }
     ```

### Workflow Examples

**Content Moderation Pipeline**:
```
Webhook → Extract Claims → Fact Check → Filter → Publish
```

**Document Processing**:
```
File Upload → Parse Text → Verify Claims → Generate Report
```

### Features

- **Real-time processing** - Event streaming for live updates
- **Workflow automation** - Integrate with content pipelines  
- **Batch processing** - Handle multiple claims simultaneously

## Dify Applications

Add fact-checking to your Dify AI applications.

### Configuration

1. **Start the SSE server** (same as n8n setup)
2. **Add Custom Tool** in Dify:
   - **Name**: Kluster Fact Check
   - **Endpoint**: `http://localhost:3000/mcp/fact_check`
   - **Method**: POST
   - **Schema**:
     ```json
     {
       "type": "object",
       "properties": {
         "claim": {"type": "string"},
         "return_search_results": {"type": "boolean"}
       },
       "required": ["claim"]
     }
     ```

### Features

- **Application-level verification** - Built into your AI assistants
- **Custom tool integration** - Native Dify tool experience
- **Production ready** - Scales with cloud deployment

## Other MCP Clients

The server follows standard MCP protocol and works with any compatible client.

### Generic Configuration

Most MCP clients support this format:

```json
{
  "servers": {
    "kluster-hallucination": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "kluster-mcp-server", 
        "--api-key", "YOUR_API_KEY"
      ]
    }
  }
}
```

### Environment Variables

Alternative to command-line arguments:

```bash
export KLUSTER_AI_API_KEY="your_api_key"
export KLUSTER_AI_BASE_URL="https://api-r.klusterai.dev/v1"
```

## Configuration Options

### Command Line Arguments

| Argument | Description | Required |
| :---: | :---: | :---: |
| `--api-key` | Your kluster.ai API key | Yes |
| `--base-url` | API endpoint (default: https://api-r.klusterai.dev/v1) | No |

### Environment Variables

| Variable | Description |
| :---: | :---: |
| `KLUSTER_AI_API_KEY` | Alternative to --api-key |
| `KLUSTER_AI_BASE_URL` | Alternative to --base-url |

## Troubleshooting

### Server Not Starting

- **Check Docker** is running and accessible
- **Verify API key** is correct and has active credits
- **Confirm base URL** if using custom endpoint

### Tools Not Available

- **Restart your client** after configuration changes
- **Check server logs** for initialization errors
- **Verify MCP support** in your client application

### Performance Issues

- **Monitor token usage** in your kluster.ai dashboard
- **Check network latency** to API endpoints
- **Consider local caching** for repeated claims

## Production Deployment

### Scaling Considerations

- **Multiple instances** - Run multiple server containers
- **Load balancing** - Distribute requests across instances
- **API rate limits** - Monitor usage in your kluster.ai account

### Security

- **API key management** - Use environment variables in production
- **Network security** - Restrict access to internal networks
- **Logging** - Monitor fact-checking requests for audit trails

## Additional Resources

- **Quick Start** - Get running in [5 minutes](/get-started/hallucination-agent/mcp-quick-start/){target=_self}
- **Tools Reference** - Detailed [parameter documentation](/get-started/hallucination-agent/mcp-tools/){target=_self}
- **MCP Integration** - Return to the [main guide](/get-started/hallucination-agent/mcp/){target=_self}
- **Support** - Contact kluster.ai support for enterprise deployment assistance