---
title: API usage
description: Complete guide to using kluster.ai's Cloud MCP API with JSON-RPC requests. How to check status, enable, disable and test it. 
---

# API usage

Manage your Cloud MCP endpoint using API calls. This guide covers checking status, enabling/disabling your endpoint, obtaining MCP tokens, and testing verification tools. Use this as an alternative to the [platform UI](/get-started/mcp/cloud/platform/){target=\_blank}.

## Prerequisites

Before getting started with MCP via API, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## Manage your MCP endpoint

### Check status

First, check if your MCP endpoint is already enabled:

```bash
curl -X GET https://api.kluster.ai/v1/mcp/status \
  -H "Authorization: Bearer YOUR_API_KEY"
```

If disabled, response shows:
```json
{
    "enabled": false,
    "url": "",
    "apiKey": ""
}
```

### Enable endpoint

If not enabled, activate your MCP endpoint:

```bash
curl -X POST https://api.kluster.ai/v1/mcp/enable \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response includes your MCP token:
```json
{
  "enabled": true,
  "url": "https://api.kluster.ai/v1/mcp",
  "token": "MCP_TOKENxxxxxxxxxxxx"
}
```

Your MCP token is a specialized authentication token used specifically for MCP verification calls, separate from your main API key. Use this token when using all MCP verification tools.

!!! warning "Store the token securely"
    Store the token securely as it provides access to your MCP verification services.
        
### Disable endpoint (optional)

You may want to disable your MCP endpoint. This option prevents any further MCP calls using that token until you enable the endpoint again.

To revoke access:

```bash
curl -X POST https://api.kluster.ai/v1/mcp/disable \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## API overview

Cloud MCP uses JSON-RPC 2.0 with streaming support:

- **Management endpoints**: Use your main API key with `Authorization: Bearer YOUR_API_KEY`.
- **MCP endpoint**: `https://api.kluster.ai/v1/mcp`.
- **Method**: `POST`.
- **Authentication**: `Authorization: Bearer YOUR_MCP_TOKEN` (uses the MCP token from enable response).
- **Content-Type**: `application/json`.
- **Accept**: `application/json, text/event-stream` (required for streaming support).

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

## Test MCP tools

The following request is an example using the `verify` tool:

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
        "claim": "The Great Wall of China is visible from space"
      }
    },
    "id": 1
  }'
```

The response includes verification results nested in JSON-RPC format. See [Tools reference](/get-started/mcp/tools/) for complete tool parameters and response details.


## Next steps

- [Client integrations](/get-started/mcp/integrations/) to configure your AI clients.
- [Tools reference](/get-started/mcp/tools/) for complete tool documentation.