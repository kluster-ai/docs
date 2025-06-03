---
title: kluster verify
description: Learn how to detect and prevent hallucinations in your applications using kluster.ai's specialized kluster verify.
---

# kluster verify

The **kluster verify** service helps to identify when AI responses contain fabricated or inaccurate information.

With this specialized service, you can verify the factual reliability of AI-generated content and build more trustworthy applications.

The service can evaluate the AI response based on a given context, which makes it great for RAG applications. Without providing a specific context, the agent can also be used as a **real-time fact-checking tool**.

## How it works
    
The Agent evaluates AI outputs in order to identify hallucinations or incorrect facts.

For example:
   
`user: where is the Eiffel Tower?` 

`assistant: the Eiffel Tower is located in Rome.`

```json
{
    "is_hallucination": true,
    "usage": {
        "completion_tokens": 154,
        "prompt_tokens": 1100,
        "total_tokens": 1254
    },
    "explanation": "The response provides a wrong location for the Eiffel Tower.\nThe Eiffel Tower is actually located in Paris, France, which is a well-known fact.\nThe response given is factually incorrect as Rome is the capital of Italy, not the location of the Eiffel Tower.",
    "search_results": [] // Optional
}
```
       
- **is_hallucination=true/false** - indicates whether the response contains hallucinated content.
- **explanation** - provides detailed reasoning for the determination.
- **search_results** - shows the reference data used for factchecking (when applicable).

## What to know

!!! question "What's a Hallucination?"
    Hallucinations occur when models generate information that appears plausible but is factually incorrect or unsupported by the provided context. Check out our [kluster verify Tutorial](/tutorials/klusterai-api/hallucination-detection-agent){target=_blank}

**kluster verify** evaluates AI responses to determine if they contain hallucinated content, providing detailed explanations of its reasoning. 

The service offers flexible options for verification supporting both **question-answer** format and **chat completions** where the whole chat history is analyzed by the agent.

!!! tip "Hallucinations can be problematic"
    Hallucination detection is particularly valuable when accuracy is critical, such as in educational tools, healthcare applications, legal assistants, or any system where factual correctness matters.

## When to use hallucination detection

The hallucination detection service is ideal for scenarios where you need:

- **Model evaluation** - easily integrate our agent to compare models output quality.
- **RAG applications** - verify that generated responses accurately reflect the provided reference documents rather than introducing fabricated information.
- **Internet-sourced fact-checking** - validate claims against reliable online sources with transparent citation of evidence.
- **Content moderation** - automatically flag potentially misleading information before it reaches end users.
- **Regulatory compliance** - ensure AI-generated content meets accuracy requirements.

## Available detection methods

kluster.ai offers multiple ways to detect hallucinations, each designed for different use cases:

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Question/Answer Detection__

    ---

    Verify the factual accuracy of an answer to a specific question. Ideal for fact-checking individual responses against specific context.

    [:octicons-arrow-right-24: Visit the guide](/get-started/hallucination-agent/question-answer/){target=_self}

-   <span class="badge guide">Guide</span> __Chat Completion Detection__

    ---

    Validate responses in full conversation histories using the same format as the chat completions API.

    [:octicons-arrow-right-24: Visit the guide](/get-started/hallucination-agent/chat-completion/){target=_self}

-   <span class="badge guide">Guide</span> __MCP Integration__

    ---

    Add real-time fact-checking to Claude Desktop, VS Code, n8n, and other MCP clients with two specialized verification tools.

    [:octicons-arrow-right-24: Start here](/get-started/hallucination-agent/mcp/){target=_self}

</div>

## Additional resources

- **Question/Answer detection** - Learn how to [verify individual question-answer pairs](/get-started/hallucination-agent/question-answer/){target=_self}
- **Chat Completion detection** - Discover how to [validate responses in conversations](/get-started/hallucination-agent/chat-completion/){target=_self}
- **MCP Integration** - Integrate hallucination detection into [MCP-compatible applications](/get-started/hallucination-agent/mcp/){target=_self}
- **MCP Quick Start** - Get running in [5 minutes with Docker](/get-started/hallucination-agent/mcp/quick-start/){target=_self}
- **MCP Tools** - Technical reference for [fact_check and document_claim_check](/get-started/hallucination-agent/mcp/tools/){target=_self}
- **MCP Clients** - Setup guides for [Claude Desktop, VS Code, n8n, and Dify](/get-started/hallucination-agent/mcp/clients/){target=_self}
- **Practical examples** - Explore our [Tutorials](/tutorials/klusterai-api/hallucination-detection-agent){target=_blank} of hallucination detection
- **API reference** - Review the complete [API documentation](/api-reference/reference/){target=_blank} for all hallucination detection endpoints

