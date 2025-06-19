---
title: Tools reference
description: Reference guide for kluster.ai's MCP verification tools - verify claims and documents with detailed parameters and response formats.
---

# Tools reference

The [kluster.ai's](https://www.kluster.ai/){target=\_blank} MCP server provides two verification tools that work identically whether deployed [self-hosted](/get-started/mcp/self-hosted/){target=\_blank} or via [Cloud MCP](/get-started/mcp/cloud/platform/){target=\_blank}. These tools enable real-time reliability verification directly within your AI assistant conversations.

This page documents the tool parameters and response formats you'll see when using these tools in any MCP-compatible client.

## Tool overview


The following tools are available through the kluster.ai MCP server:

| Tool | Purpose | Best For |
|:---|:---|:---|
| `verify` | Verify standalone claims | General statements, trivia, current events, news |
| `verify_document` | Verify claims about documents | Quotes, data extraction, RAG hallucination checking |

### Verify

The verify tool allows you to check any statement against reliable online sources.

**Parameters:**

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | The statement to verify |
| `returnSearchResults` | boolean | No | Include source citations (default: true) |


### Verify document

The verify document tool checks that claims accurately reflect the content of the uploaded document.

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

An example can be seen below:

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
- **Use cloud version**: Enable [Cloud MCP](/get-started/mcp/cloud/platform/) for managed deployment.