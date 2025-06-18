---
title: Tools reference
description: Reference guide for kluster.ai's MCP verification tools - verify claims and documents with detailed parameters and response formats.
---

# Tools reference

The [kluster.ai's](https://www.kluster.ai/){target=\_blank} MCP server provides two verification tools that work identically whether deployed [self-hosted](/get-started/mcp/self-hosted/) or via [Stream HTTP MCP](/get-started/mcp/stream-http/platform/). These tools enable real-time reliability verification directly within your AI assistant conversations.

This page documents the tool parameters and response formats you'll see when usisng these tools in any MCP-compatible client.

## Tool overview

| Tool | Purpose | Best For |
|:---|:---|:---|
| `verify` | Verify standalone claims | General statements, trivia, current events, news |
| `verify_document` | Verify claims about documents | Quotes, data extraction, RAG hallucination checking |

### Verify

Verifies any statement against reliable online sources.

**Parameters:**

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | The statement to verify |
| `returnSearchResults` | boolean | No | Include source citations (default: true) |


### Verify document

Verifies if claims accurately reflect uploaded document content.

**Parameters:**

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | Your interpretation of the document |
| `documentContent` | string | Yes | Full document text (auto-provided by MCP client) |
| `returnSearchResults` | boolean | No | Include external sources (default: true) |


## Response fields

All verification tools return the same response structure:

- **`claim`**: The verified claim.
- **`is_accurate`**: Boolean indicating if claim is accurate.
- **`explanation`**: Detailed reasoning for the verdict.
- **`confidence`**: Token usage statistics.
- **`search_results`**: Source citations (if requested).

**Response format example:**

```json
{
  "claim": "This employment contract allows unlimited remote work",
  "is_accurate": false,
  "explanation": "The claim is incorrect. Section 4.2 explicitly requires on-site work minimum 3 days per week and residence within 50 miles of headquarters.",
  "confidence": {
    "completion_tokens": 156,
    "prompt_tokens": 890,
    "total_tokens": 1046
  },
  "search_results": []
}
```

## Next steps

- **Set up integrations**: Configure [client applications](/get-started/mcp/integrations/) to use these tools.
- **Deploy locally**: Set up [self-hosted MCP server](/get-started/mcp/self-hosted/) for local development.
- **Use cloud version**: Enable [Stream HTTP MCP](/get-started/mcp/stream-http/platform/) for managed deployment.