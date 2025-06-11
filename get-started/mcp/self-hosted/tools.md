---
title: Tools Reference
description: Technical reference for the Verify service tools in kluster.ai's example MCP server implementation.
---

# Tools Reference

These tools provide access to the [Verify service](/get-started/verify/reliability/overview){target=self} for reliability checking and document verification.

## Tool Overview

| Tool | Purpose | Best For |
|:---|:---|:---|
| `verify` | Verify standalone claims. | General statements, trivia, current events, news. |
| `verify_document` | Verify claims about documents. | Quotes, data extraction, RAG hallucination checking. |

### Verify

Verifies any statement against reliable online sources.

#### Parameters

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | The statement to verify. |
| `return_search_results` | boolean | No | Include source citations. (default: true) |

#### Request Example

```json
{
  "claim": "The Eiffel Tower is located in Rome",
  "return_search_results": true
}
```

#### Response Format

```json
{
  "claim": "The Eiffel Tower is located in Rome",
  "is_hallucination": true,
  "explanation": "The response provides a wrong location for the Eiffel Tower.\n"
                 "The Eiffel Tower is actually located in Paris, France, not in Rome.\n"
                 "The response contains misinformation as it incorrectly states the tower's location.",
  "usage": {
    "completion_tokens": 343,
    "prompt_tokens": 939,
    "total_tokens": 1282
  },
  "search_results": []
}
```

### Verify document

Verifies if claims accurately reflect uploaded document content.

#### Parameters

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | Your interpretation of the document |
| `document_content` | string | Yes | Full document text (auto-provided by MCP client) |
| `return_search_results` | boolean | No | Include external sources (default: true) |

#### Request Example

```json
{
  "claim": "This employment contract allows unlimited remote work",
  "document_content": "Section 4.2: Employee must maintain primary
                       residence within 50 miles of headquarters and work on-site minimum 3 days per week...",
  "return_search_results": true
}
```

#### Response Format

```json
{
  "claim": "This employment contract allows unlimited remote work",
  "is_hallucination": true,
  "explanation": "The claim is incorrect. Section 4.2 explicitly requires
                 on-site work minimum 3 days per week and residence within 50 miles of headquarters.",
  "usage": {
    "completion_tokens": 156,
    "prompt_tokens": 890,
    "total_tokens": 1046
  },
  "search_results": []
}
```
## Additional Resources

- **Quick Start**: Get up and running with the [five-minute setup guide](/get-started/mcp/self-hosted/quick-start/){target=\_self}
- **Client Setup**: Configure [different MCP clients](/get-started/mcp/self-hosted/clients/){target=\_self}
- **API Reference**: Complete [API documentation](/api-reference/reference/){target=\_blank}