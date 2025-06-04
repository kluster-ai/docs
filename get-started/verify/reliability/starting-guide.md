---
title: kluster verify
description: Learn how to verify reliability and prevent unreliable content in your applications using kluster.ai's specialized kluster verify.
---

# kluster verify

The **kluster verify** service helps to make sure AI responses are accurate and compliant. The **Reliability check agent** is able to identify when AI responses contain fabricated or inaccurate information.

With this specialized service, you can verify the reliability of AI-generated content and build more trustworthy applications.

The service can evaluate the AI response based on a given context, which makes it great for RAG applications. Without providing a specific context, the service can also be used as a **real-time reliability verification service**.

## How it works
    
The service evaluates AI outputs in order to identify reliability issues or incorrect information.

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
    "explanation": "The response provides a wrong location for the Eiffel Tower.\nThe Eiffel Tower is actually located in Paris, France, not in Rome.\nThe response contains misinformation as it incorrectly states the tower's location.",
    "search_results": [] // Optional
}
```
       
- **is_hallucination=true/false**: indicates whether the response contains unreliable content.
- **explanation**: provides detailed reasoning for the determination.
- **search_results**: shows the reference data used for verification (when applicable).

## What to know

!!! question "What are Reliability Issues?"
    Reliability issues occur when models generate information that appears plausible but is unreliable or unsupported by the provided context. Check out the [kluster verify Tutorial](/tutorials/klusterai-api/reliability-check){target=_blank}

**kluster verify** evaluates AI responses to determine if they contain unreliable content, providing detailed explanations of its reasoning. 

The service offers flexible options for verification supporting both **question-answer** format and **chat completions** where the whole chat history is analyzed by the agent.

!!! tip "Reliability issues can be problematic"
    Reliability checking is particularly valuable when accuracy is critical, such as in educational tools, healthcare applications, legal assistants, or any system where information accuracy and trustworthiness matter.

## When to use reliability checking

The reliability check service is ideal for scenarios where you need:

- **Model evaluation**: easily integrate the service to compare models output quality.
- **RAG applications**: verify that generated responses accurately reflect the provided reference documents rather than introducing fabricated information.
- **Internet-sourced verification**: validate claims against reliable online sources with transparent citation of evidence.
- **Content moderation**: automatically flag potentially misleading information before it reaches end users.
- **Regulatory compliance**: ensure AI-generated content meets accuracy requirements.

## Available verification methods

kluster.ai offers multiple ways to verify reliability, each designed for different use cases:

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Question/Answer Verification__

    ---

    Verify the reliability and accuracy of an answer to a specific question. Ideal for validating individual responses against specific context or general knowledge.

    [:octicons-arrow-right-24: Visit the guide](/get-started/verify/reliability/question-answer/){target=_self}

-   <span class="badge guide">Guide</span> __Chat Completion Verification__

    ---

    Validate responses in full conversation histories using the same format as the chat completions API.

    [:octicons-arrow-right-24: Visit the guide](/get-started/verify/reliability/chat-completion/){target=_self}

-   <span class="badge integration">Integration</span> __Workflow Integrations__

    ---

    Download ready-to-use workflows for Dify, n8n, and other platforms using direct API integration.

    [:octicons-arrow-right-24: Get workflows](/get-started/verify/reliability/workflow-integrations/){target=_self}

</div>

## Additional resources

- **Workflow Integrations**: Download [ready-to-use workflows for Dify, n8n](/get-started/verify/reliability/workflow-integrations/){target=_self}
- **Tutorial**: Explore the [kluster verify tutorial](/tutorials/klusterai-api/reliability-check){target=_blank} with code examples

