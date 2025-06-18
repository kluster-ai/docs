---
title: API Usage
description: Complete guide to using kluster.ai's Stream HTTP MCP API with JSON-RPC requests. How to check status, enable, disable and test it. 
---

# API usage

Stream HTTP MCP provides managed verification endpoints using JSON-RPC over HTTP. This guide covers enabling MCP via API calls, the API structure, available tools, and integration examples for various platforms and programming languages.

You can enable your MCP endpoint through API calls or through the [platform UI](/get-started/mcp/stream-http/platform/).

## Prerequisites

Before getting started with MCP via API, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## Enable MCP endpoint

### Check endpoint status

First, check if your MCP endpoint is already enabled:

```bash
curl -X GET https://api.kluster.ai/v1/mcp/status \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response shows current status:
```json
{
  "enabled": false,
  "url": null
}
```

### Enable your endpoint

Enable the MCP endpoint:

```bash
curl -X POST https://api.kluster.ai/v1/mcp/enable \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response with your MCP token:
```json
{
  "enabled": true,
  "url": "https://api.kluster.ai/v1/mcp",
  "token": "MCP_xxxxxxxxxxxx"
}
```

!!! warning "Save your MCP token"
    Store the `token` securely - you'll need it for all MCP requests. Use this MCP token (not your original API key) for verification calls.

### Disable endpoint (optional)

To revoke access and disable your MCP endpoint:

```bash
curl -X POST https://api.kluster.ai/v1/mcp/disable \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response:
```json
{
  "success": true
}
```

## API overview

Stream HTTP MCP uses JSON-RPC 2.0 with streaming support:

- **Management endpoints**: Use your main API key with `Authorization: Bearer YOUR_API_KEY`
- **MCP endpoint**: `https://api.kluster.ai/v1/mcp`
- **Method**: `POST`
- **Authentication**: `Authorization: Bearer YOUR_MCP_TOKEN` (uses the MCP token from enable response)
- **Content-Type**: `application/json`
- **Accept**: `application/json, text/event-stream` (required for streaming support)

## Request structure

All requests use the MCP tools/call format:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "tool_name",
    "arguments": {
      // Tool-specific parameters
    }
  },
  "id": 1
}
```

## Available tools

### Verify tool

Validates claims against reliable online sources.

**Tool name**: `verify`

**Arguments**:

- `claim` (string, required): The statement to verify.
- `returnSearchResults` (boolean, optional): Include source citations (default: true).

**Example request**:
```bash
curl -X POST https://api.kluster.ai/v1/mcp \
  -H "Authorization: Bearer YOUR_MCP_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "verify",
      "arguments": {
        "claim": "The Great Wall of China is visible from space",
        "returnSearchResults": true
      }
    },
    "id": 1
  }'
```

**Example response**:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"claim\": \"The Great Wall of China is visible from space\", \"is_accurate\": false, \"explanation\": \"This is a common myth. The Great Wall is not visible to the naked eye from space without aid. Astronauts have confirmed that it requires telescopic lenses to see the wall from low Earth orbit.\", \"confidence\": {\"prompt_tokens\": 892, \"completion_tokens\": 67, \"total_tokens\": 959}, \"search_results\": []}"
      }
    ]
  }
}
```

### Verify document tool

Checks if claims accurately reflect document content.

**Tool name**: `verify_document`

**Arguments**:

- `claim` (string, required): Your interpretation of the document.
- `documentContent` (string, required): Full document text.
- `returnSearchResults` (boolean, optional): Include external sources (default: true).

**Example request**:

```bash
curl -X POST https://api.kluster.ai/v1/mcp \
  -H "Authorization: Bearer YOUR_MCP_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "verify_document",
      "arguments": {
        "claim": "The contract allows remote work",
        "documentContent": "Section 3: All employees must work from the office...",
        "returnSearchResults": false
      }
    },
    "id": 2
  }'
```

## Response format

Responses follow JSON-RPC format with nested verification results:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"claim\": \"...\", \"is_accurate\": false, \"explanation\": \"...\", \"confidence\": {...}, \"search_results\": []}"
      }
    ]
  }
}
```
**Verification result fields**:

- `claim`: The verified claim.
- `is_accurate`: Boolean indicating if claim is accurate.
- `explanation`: Detailed reasoning for the verdict.
- `confidence`: Token usage statistics.
- `search_results`: Source citations (if requested).

## Authentication flow summary

1. **Enable MCP**: Use your main API key with `/v1/mcp/enable` → Get MCP token.
2. **Use MCP**: Use the MCP token with `/v1/mcp` → Make verification calls.
3. **Manage MCP**: Use your main API key with `/v1/mcp/status` or `/v1/mcp/disable`.

## Next steps

- **Platform management**: Learn about [enabling and managing endpoints](/get-started/mcp/stream-http/platform/).
- **Self-hosted option**: Explore [local MCP deployment](/get-started/mcp/self-hosted/get-started/).
- **API reference**: View the [complete API documentation](/api-reference/reference/).