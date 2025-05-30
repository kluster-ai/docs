---
title: MCP (Model Context Protocol)
description: Integrate kluster.ai's hallucination detection capabilities directly into MCP-compatible applications using our production-ready MCP server with fact-checking and document verification tools.
---

# MCP (Model Context Protocol)

The **Hallucination Detection Agent MCP Server** provides seamless integration of hallucination detection capabilities into MCP-compatible applications through a production-ready Model Context Protocol implementation. Access powerful fact-checking and document verification tools directly within your favorite AI development environments.

## Prerequisites

Before getting started with MCP integration, ensure the following requirements are met:

- **kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you do not have one
- **kluster.ai API key** - after signing in, go to the [API Keys](https://platform.kluster.ai/apikeys){target=_blank} section and create a new key. For detailed instructions, see the [Get an API key](https://docs.kluster.ai/get-started/get-api-key/){target=_blank} guide
- **Docker** installed on your system (for containerized deployment)
- **MCP-compatible client** such as Claude Desktop, VS Code, n8n, or Dify

## How it works

The Hallucination Detection Agent MCP server integrates with your applications by:

1. **Exposing specialized tools** through the Model Context Protocol standard
2. **Processing verification requests** using kluster.ai's advanced hallucination detection API
3. **Returning structured responses** with detailed explanations and search results
4. **Supporting multiple deployment methods** for different client environments

## Available Tools

The MCP server provides two powerful tools designed for different verification scenarios:

### Fact Check Tool

**Purpose**: Verify standalone claims against reliable sources using AI-powered analysis.

**Use cases**:

- **Real-time fact-checking** - verification of statements as they are made
- **General knowledge validation** - checking claims against established facts  
- **Content moderation** - automated verification before publication

**Example usage**:
```json
{
  "claim": "The Eiffel Tower is located in Rome",
  "return_search_results": true
}
```

**Response format**:
```json
{
  "claim": "The Eiffel Tower is located in Rome",
  "is_hallucination": true,
  "explanation": "This claim is factually incorrect. The Eiffel Tower is located in Paris, France, not Rome, Italy.",
  "usage": {
    "completion_tokens": 150,
    "prompt_tokens": 50,
    "total_tokens": 200
  },
  "search_results": [
    {
      "title": "Eiffel Tower - Official Site",
      "snippet": "The Eiffel Tower is located in Paris, France...",
      "link": "https://www.toureiffel.paris/en"
    }
  ]
}
```

### Document Claim Verification Tool

**Purpose**: Verify if claims accurately reflect the content of source documents.

**Use cases**:

- **Academic research** - verification of research paper interpretations
- **Legal documents** - checking understanding of contracts and legal texts
- **News analysis** - verifying claims about article content
- **Data extraction** - confirming extracted facts match sources

**How it works**:
1. Upload or paste a document into your MCP client
2. Make a claim about the document's content
3. The tool automatically verifies your interpretation against the source

**Example usage**:
```json
{
  "claim": "This research paper proves coffee reduces cancer risk by 25%",
  "document_content": "[Full document text provided by client]",
  "return_search_results": true
}
```

**Response format**:
```json
{
  "claim": "This research paper proves coffee reduces cancer risk by 25%",
  "document_verification": {
    "is_accurate": false,
    "explanation": "The document states coffee may reduce cancer risk by 15-20%, not 25%. The claim overstates the findings.",
    "confidence_assessment": {
      "completion_tokens": 180,
      "prompt_tokens": 1200,
      "total_tokens": 1380
    }
  },
  "search_results": [
    {
      "title": "Coffee and Cancer Research Review",
      "snippet": "Recent studies show coffee consumption linked to reduced cancer risk...",
      "link": "https://example.com/coffee-cancer-study"
    }
  ]
}
```

## Installation and Setup

The kluster.ai MCP server supports multiple deployment methods to accommodate different client environments and use cases.

### Docker Deployment (Recommended)

**Best for**: Claude Desktop, VS Code, and general MCP client integration

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kluster-ai/mcp-server
   cd mcp-server
   ```

2. **Build the Docker image**:
   ```bash
   npm run docker:build
   ```

3. **Configure your MCP client**:
   
   **For Claude Desktop**:
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

   **For VS Code Copilot Chat**:
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

4. **Replace the API key** with your actual kluster.ai API key

5. **Restart your MCP client** to load the new server

### Node.js Deployment

**Best for**: Development environments and custom integrations

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Build the TypeScript project**:
   ```bash
   npm run build
   ```

3. **Run the server**:
   ```bash
   npm start -- --api-key YOUR_KLUSTER_AI_API_KEY
   ```

### SSE Server Deployment

**Best for**: n8n, Dify, and other platforms requiring HTTP endpoints

The SSE (Server-Sent Events) server provides HTTP endpoints for platforms that don't support native MCP protocol.

1. **Start the SSE server**:
   ```bash
   npm run sse:start -- --api-key YOUR_KLUSTER_AI_API_KEY
   ```

2. **Configure your platform**:
   - **Endpoint**: `http://localhost:3000/mcp/fact_check`
   - **Method**: POST
   - **Headers**: `Content-Type: application/json`

**n8n Integration**:
- Use the HTTP Request node
- Configure with the SSE server endpoints
- Enable real-time event streaming for live updates

**Dify Integration**:
- Add as a custom tool
- Use HTTP tool configuration
- Connect to local SSE endpoints

## Supported Clients

### Claude Desktop

- **Full MCP support** - automatic tool selection
- **Document content parsing** - claim verification capability
- **Real-time fact-checking** - verification during conversations

### VS Code Copilot Chat

- **Agent Mode support** - secure API key input
- **Inline verification** - verification within code comments and documentation
- **Development workflow integration** - seamless integration with coding workflows

### n8n Workflows

- **Native MCP tool integration** - integration via SSE server
- **Workflow automation** - content verification pipelines
- **Real-time processing** - event broadcasting capabilities

### Dify Applications

- **Custom tool integration** - integration through SSE endpoints
- **Application-level fact-checking** - verification for AI assistants
- **Production deployment ready** - support for cloud platforms

### Other MCP Clients
The server follows standard MCP protocol specifications and should work with any MCP-compatible client.

## Configuration Options

### Command Line Arguments

| Argument | Description | Required |
| :---: | :---: | :---: |
| `--api-key` | Your kluster.ai API key | Yes |
| `--base-url` | API base URL (default: https://api-r.klusterai.dev/v1) | No |

### Environment Variables

| Variable | Description |
| :---: | :---: |
| `KLUSTER_AI_API_KEY` | Alternative method to provide API key |
| `KLUSTER_AI_BASE_URL` | Alternative method to provide base URL |

### Tool Parameters

Both tools support the following parameters:

| Parameter | Type | Required | Description |
| :---: | :---: | :---: | :---: |
| `claim` | string | Yes | The statement or claim to verify |
| `return_search_results` | boolean | No | Include search results in response (default: true) |
| `document_content` | string | No* | Source document content (*required for document verification) |

## Troubleshooting

### Common Issues

**Authentication Errors**:

- **API key verification** - ensure your API key is correct and active
- **Permissions check** - ensure the API key has proper permissions for hallucination detection

**Connection Issues**:

- **Docker status** - check that Docker is running for containerized deployment
- **Base URL verification** - verify the base URL is set correctly
- **Network connectivity** - ensure your network allows connections to kluster.ai API

**Tool Not Available**:

- **Client restart** - restart your MCP client after configuration changes
- **Configuration verification** - verify the server configuration in your client settings
- **Log analysis** - check server logs for initialization errors

### Debug Mode

Enable debug logging by setting environment variables:

```bash
DEBUG=true npm start -- --api-key YOUR_API_KEY
```

## Performance and Limits

- **Response time** - typically two to five seconds depending on claim complexity
- **Concurrent requests** - no artificial limits imposed by the MCP server
- **API rate limits** - subject to your kluster.ai subscription plan limits
- **Document size** - supports documents up to 100MB for verification

## Additional Resources

- **Question/Answer detection** - Learn how to [verify individual question-answer pairs](/get-started/hallucination-agent/question-answer/){target=_self}
- **Chat Completion detection** - Discover how to [validate responses in conversations](/get-started/hallucination-agent/chat-completion/){target=_self}
- **Practical examples** - Explore our [Tutorials](/tutorials/klusterai-api/hallucination-detection-agent){target=_blank} for hallucination detection
- **API reference** - Review the complete [API documentation](/api-reference/reference/){target=_blank} for all hallucination detection endpoints