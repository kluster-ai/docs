---
title: Tools Reference
description: Complete technical reference for fact_check and document_claim_check tools including parameters, responses, and error handling.
---

# Tools Reference

Technical documentation for the two reliability verification tools available through the kluster verify MCP server.

## Tool Overview

| Tool | Purpose | Best For |
|:---|:---|:---|
| `fact_check` | Verify standalone claims | General statements, trivia, current events |
| `document_claim_check` | Verify claims about documents | Quotes, data extraction, legal interpretation |

## fact_check Tool

Verifies any statement against reliable online sources.

### Parameters

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | The statement to verify |
| `return_search_results` | boolean | No | Include source citations (default: true) |

### Request Example

```json
{
  "claim": "OpenAI was founded in 2015",
  "return_search_results": true
}
```

### Response Format

```json
{
  "claim": "OpenAI was founded in 2015",
  "is_hallucination": false,
  "explanation": "OpenAI was indeed founded in December 2015 by Sam Altman, Elon Musk, and others as a non-profit AI research company.",
  "usage": {
    "completion_tokens": 124,
    "prompt_tokens": 67,
    "total_tokens": 191
  },
  "search_results": [
    {
      "title": "OpenAI - Wikipedia",
      "snippet": "OpenAI is an AI research laboratory founded in December 2015...",
      "link": "https://en.wikipedia.org/wiki/OpenAI"
    }
  ]
}
```

### Use Cases

- **Current events**: "The 2024 Olympics were held in Paris"
- **Historical facts**: "World War II ended in 1945" 
- **Scientific claims**: "Water boils at 100°C at sea level"
- **Company information**: "Microsoft was founded by Bill Gates"

## document_claim_check Tool

Verifies if claims accurately reflect uploaded document content.

### Parameters

| Parameter | Type | Required | Description |
|:---|:---|:---|:---|
| `claim` | string | Yes | Your interpretation of the document |
| `document_content` | string | Yes | Full document text (auto-provided by MCP client) |
| `return_search_results` | boolean | No | Include external sources (default: true) |

### Request Example

```json
{
  "claim": "This employment contract allows unlimited remote work",
  "document_content": "Section 4.2: Employee must maintain primary residence within 50 miles of headquarters and work on-site minimum 3 days per week...",
  "return_search_results": true
}
```

### Response Format

```json
{
  "claim": "This employment contract allows unlimited remote work",
  "document_verification": {
    "is_accurate": false,
    "explanation": "The claim is incorrect. Section 4.2 explicitly requires on-site work minimum 3 days per week and residence within 50 miles of headquarters.",
    "confidence_assessment": {
      "completion_tokens": 156,
      "prompt_tokens": 890,
      "total_tokens": 1046
    }
  },
  "search_results": [
    {
      "title": "Remote Work Employment Law",
      "snippet": "Standard employment contracts typically specify work location requirements...",
      "link": "https://example.com/employment-law"
    }
  ]
}
```

### Use Cases

- **Legal documents**: Contract terms, policy interpretation
- **Research papers**: Data claims, methodology verification  
- **Financial reports**: Revenue figures, growth claims
- **Technical specifications**: Feature descriptions, requirements

## Error Handling

### Common Errors

**Invalid API Key**:
```json
{
  "error": "Authentication failed",
  "message": "Invalid API key or insufficient permissions"
}
```

**Empty Claim**:
```json
{
  "error": "Invalid input", 
  "message": "Claim cannot be empty"
}
```

**Rate Limit Exceeded**:
```json
{
  "error": "Rate limit exceeded",
  "message": "API rate limit reached. Try again in 60 seconds"
}
```

## Best Practices

### Writing Effective Claims

**Good**: "This document states the return policy is 30 days"
**Bad**: "What's the return policy?"

**Good**: "The Eiffel Tower is 324 meters tall"  
**Bad**: "How tall is the Eiffel Tower?"

### Performance Tips

- **Shorter claims** process faster (under 100 words)
- **Specific statements** get more accurate results than general questions
- **Document claims** work best with exact quotes or data points

### Token Usage

- **fact_check**: Typically 50-200 tokens per request
- **document_claim_check**: Varies by document size (100-2000+ tokens)
- **Large documents**: Consider breaking into smaller sections

## Integration Notes

### Tool Selection

MCP clients automatically choose the right tool:
- **fact_check** for general statements
- **document_claim_check** when documents are present

### Response Time

- **Simple claims**: two to three seconds
- **Complex claims**: three to five seconds  
- **Large documents**: five to 10 seconds

### Concurrent Requests

No artificial limits imposed by the MCP server. Limited by your kluster.ai subscription plan.

## Additional Resources

- **Quick Start**: Get up and running with the [five-minute setup guide](/get-started/mcp/self-hosted/quick-start/){target=\_self}
- **Client Setup**: Configure [different MCP clients](/get-started/mcp/self-hosted/clients/){target=\_self}
- **API Reference**: Complete [API documentation](/api-reference/reference/){target=\_blank}