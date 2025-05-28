---
title: Hallucination Detection Agent with kluster.ai
description: Learn how to detect and prevent hallucinations in your applications using kluster.ai's specialized Hallucination Detection Agent.
---

# Hallucination Detection Agent with kluster.ai

The kluster.ai **Hallucination Detection Agent** service helps you identify when AI responses contain fabricated or inaccurate information.

With this specialized service, you can verify the factual reliability of AI-generated content and build more trustworthy applications.

The service can evaluate the AI response based on a given context, which makes it great for RAG applications. Without context, the agent can also be used as **real-time fact checking tool**.

## How it works
    
The Agent evaluates AI outputs in order to identify hallucinations or incorrect facts.

For example:
   
`user: where is the Eiffel tower?` 

`assistant: the Eiffel tower is located in Rome.`

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
       
- `is_hallucination=true/false` - indicates whether the response contains hallucinated content.
- `explanation` - provides detailed reasoning for the determination.
- `search_results` (optional) - shows the reference data used for factchecking.

## What to know

!!! question "What's a Hallucination?"
    Hallucinations occur when models generate information that appears plausible but is factually incorrect or unsupported by the provided context. 

The kluster.ai **Hallucination Detection Agent** evaluates AI responses to determine if they contain hallucinated content, providing detailed explanations of its reasoning. 

The service offers flexible options for verification supporting both **question-answer** format and **chat completions** where the whole chat history is analyzed by the agent.

!!! tip "Hallucinations can be problematic"
    Hallucination detection is particularly valuable when accuracy is critical, such as in educational tools, healthcare applications, legal assistants, or any system where factual correctness matters.

## When to use hallucination detection

The hallucination detection service is ideal for scenarios where you need:

- **Content verification** - validate AI-generated content against trusted source materials
- **Factual consistency** - ensure responses are grounded in provided context
- **Risk mitigation** - prevent misleading or fabricated information in sensitive applications
- **Quality assurance** - implement automated checks for AI response accuracy
- **Educational tools** - develop learning applications that provide factually correct information

## Benefits of hallucination detection

Detecting and preventing hallucinations delivers several key advantages:

- **Enhanced reliability** - build AI systems users can trust for critical tasks
- **Reduced misinformation** - prevent the spread of incorrect or fabricated information
- **Quality control** - implement automated verification in your AI pipeline
- **Transparent reasoning** - understand why content is flagged as hallucinated
- **Contextual awareness** - ensure AI responses remain grounded in provided facts


## Available detection methods

kluster.ai offers two ways to detect hallucinations, each designed for different use cases:

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Question/Answer Detection__

    ---

    Verify the factual accuracy of an answer to a specific question. Ideal for fact-checking individual responses against specific context.

    [:octicons-arrow-right-24: Visit the guide](/get-started/hallucination-agent/question-answer/){target=_self}

-   <span class="badge guide">Guide</span> __Chat Completion Detection__

    ---

    Validate responses in full conversation histories using the same format as the chat completions API.

    [:octicons-arrow-right-24: Visit the guide](/get-started/hallucination-agent/chat-completion/){target=_self}

</div>

## Additional resources

- **Question/Answer detection** - Learn how to [verify individual question-answer pairs](/get-started/hallucination-agent/question-answer/){target=_self}
- **Chat Completion detection** - Discover how to [validate responses in conversations](/get-started/hallucination-agent/chat-completion/){target=_self}
- **Practical examples** - Explore [real-world applications](/get-started/hallucination-agent/examples/){target=_self} of hallucination detection
- **API reference** - Review the complete [API documentation](/api-reference/reference/){target=_blank} for all hallucination detection endpoints
- **Available models** - Explore our [Models](/get-started/models/){target=_blank} page to learn about the foundation models that power our hallucination detection
