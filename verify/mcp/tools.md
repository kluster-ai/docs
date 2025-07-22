---
title: MCP tools reference
description: Reference guide for kluster.ai's MCP verification tools - verify claims and documents with detailed parameters and response formats.
search:
  exclude: true
---

# Tools reference

The [kluster.ai's](https://www.kluster.ai/){target=\_blank} MCP server provides two verification tools that work identically whether deployed [self-hosted](/verify/mcp/self-hosted/){target=\_blank} or via [Cloud MCP](/verify/mcp/cloud/platform/){target=\_blank}. These tools enable real-time reliability verification directly within your AI assistant conversations.

This page documents the tool parameters and response formats you'll see when using these tools in any MCP-compatible client.

## Tool overview


The following tools are available through the kluster.ai MCP server:

| Tool | Purpose | Best For |
|:---|:---|:---|
| `verify` | Verify prompt and response pairs | General statements, trivia, current events, news |
| `verify_document` | Verify prompt and response about documents | Quotes, data extraction, RAG hallucination checking |

### Verify

The verify tool allows you to check a prompt from a user and response from the agent against reliable online sources.

???+ interface "Parameters"

    `prompt` ++"string"++ <span class="required" markdown>++"required"++</span>

    The prompt the user made to the agent.

    ---

    `response` ++"string"++ <span class="required" markdown>++"required"++</span>

    The response from the agent that must be verified.

    ---

    `returnSearchResults` ++"boolean"++

    Include source citations. Defaults to `true`.

### Verify document

The verify document tool checks that a prompt from a user and a response from the agent accurately reflect the content of the uploaded document.

???+ interface "Parameters"


    `prompt` ++"string"++ <span class="required" markdown>++"required"++</span>

    The prompt the user made to the agent about the document.

    ---

    `response` ++"string"++ <span class="required" markdown>++"required"++</span>

    The response from the agent that must be verified against the document content.

    ---

    `documentContent` ++"string"++ <span class="required" markdown>++"required"++</span>

    Full document text (auto-provided by MCP client).

    ---

    `returnSearchResults` ++"boolean"++

    Include source citations. Defaults to `true`.

## Response fields

All verification tools return the same response structure:

- **`prompt`**: The user's prompt.
- **`response`**: The agent's response.
- **`is_hallucination`**: Boolean indicating if the response contains hallucinations.
- **`explanation`**: Detailed reasoning for the verdict.
- **`confidence`**: Token usage statistics `completion_tokens`, `prompt_tokens`, and `total_tokens`.
- **`search_results`**: Source citations (if requested).

An example can be seen below:

```json
{
    "prompt": "Does this employment contract allow unlimited remote work?",
    "response": "This employment contract allows unlimited remote work.",
    "is_hallucination": true,
    "explanation": "The response is incorrect. Section 4.2 explicitly requires on-site work minimum 3 days per week and residence within 50 miles of headquarters.",
    "confidence": {
        "completion_tokens": 156,
        "prompt_tokens": 890,
        "total_tokens": 1046
    },
    "search_results": []
}
```

## Next steps

- **Set up integrations**: Configure [client applications](/verify/mcp/integrations/) to use these tools.
- **Deploy locally**: Set up a [self-hosted MCP server](/verify/mcp/self-hosted/) for local development.
- **Use cloud version**: Enable [Cloud MCP](/verify/mcp/cloud/platform/) for managed deployment.