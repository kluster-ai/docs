---
title: Tools reference
description: Technical reference for the Verify service tools in kluster.ai's MCP server implementation, including parameters, examples, and integration guides.
---

# Tools reference

The MCP Verify server exposes kluster.ai's [Verify service](/get-started/verify/reliability/overview) as native tools for AI assistants. These tools enable real-time reliability verification directly within your development workflow without requiring manual API integration.

This page documents two verification tools: `verify` for validating standalone claims against online sources, and `verify_document` for checking claims about uploaded document content.

## Tool overview

| Tool | Purpose | Best For |
|:---|:---|:---|
| `verify` | Verify standalone claims. | General statements, trivia, current events, news. |
| `verify_document` | Verify claims about documents. | Quotes, data extraction, RAG hallucination checking. |

## Verify tool

Verifies any statement against reliable online sources.

**Parameters:**

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | The statement to verify. |
| `return_search_results` | boolean | No | Include source citations. (default: true) |

**Request example:**

```json
{
  "claim": "The Eiffel Tower is located in Rome",
  "return_search_results": true
}
```

**Response format:**

```json
{
  "claim": "The Eiffel Tower is located in Rome",
  "is_accurate": false,
  "explanation": "The response provides a wrong location for the Eiffel Tower.\n"
                 "The Eiffel Tower is actually located in Paris, France, not in Rome.\n"
                 "The response contains misinformation as it incorrectly states the tower's location.",
  "confidence": {
    "completion_tokens": 343,
    "prompt_tokens": 939,
    "total_tokens": 1282
  },
  "search_results": []
}
```

## Verify document tool

Verifies if claims accurately reflect uploaded document content.

**Parameters:**

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | Your interpretation of the document |
| `document_content` | string | Yes | Full document text (auto-provided by MCP client) |
| `return_search_results` | boolean | No | Include external sources (default: true) |

**Request example:**

```json
{
  "claim": "This employment contract allows unlimited remote work",
  "document_content": "Section 4.2: Employee must maintain primary
                       residence within 50 miles of headquarters and work on-site minimum 3 days per week...",
  "return_search_results": true
}
```

**Response format:**

```json
{
  "claim": "This employment contract allows unlimited remote work",
  "is_accurate": false,
  "explanation": "The claim is incorrect. Section 4.2 explicitly requires
                 on-site work minimum 3 days per week and residence within 50 miles of headquarters.",
  "confidence": {
    "completion_tokens": 156,
    "prompt_tokens": 890,
    "total_tokens": 1046
  },
  "search_results": []
}
```
## Additional resources

- **Get started**: Get up and running with the [five-minute setup guide](/get-started/mcp/self-hosted/get-started/).
- **Client setup**: Configure [different MCP clients](/get-started/mcp/self-hosted/clients/).
- **API reference**: Complete [API documentation](/api-reference/reference/).