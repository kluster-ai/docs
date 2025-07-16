---
title: Reliability check by Verify
description: Learn how to use kluster.ai reliability check and prevent unreliable content in your applications using kluster.ai's specialized Verify.
---

# Reliability check by Verify

Reliability check is one of the features offered by Verify, and it can identify when AI responses contain fabricated or inaccurate information.

With this specialized service, you can gauge the reliability of AI-generated content and build more trustworthy applications.

The service can evaluate the AI response based on a given context, which makes it ideal for RAG applications. Without providing a specific context, the service can also be used as a real-time reliability verification service.

## How reliability check works

The service evaluates the truthfulness of an answer to a question by:

1. Analyzing the original question, prompt, or entire conversation history.
2. Examining the provided answer (with context if provided).
3. Determining if the answer contains unreliable or unsupported information.
4. Providing a detailed explanation of the reasoning behind the determination as well as the search results used for verification.

The service returns a structured response that includes:

- **`is_hallucination`**: Indicates whether the response contains unreliable content.
- **`explanation`**: Provides detailed reasoning for the determination.
- **`search_results`**: Shows the reference data used for verification (when applicable).

Given the following prompt:

```json
...
    {
        "role": "user",
        "content": "Where is the Eiffel Tower?"
    },
    {
        "role": "assistant",
        "content": "The Eiffel Tower is located in Rome."
    }
...
```

The reliability check would return:

```json
{
    "is_hallucination": true,
    "usage": {
        "completion_tokens": 154,
        "prompt_tokens": 1100,
        "total_tokens": 1254
    },
    "explanation": "The response provides a wrong location for the Eiffel Tower.\n"
                 "The Eiffel Tower is actually located in Paris, France, not in Rome.\n"
                 "The response contains misinformation as it incorrectly states the tower's location.",
    "search_results": []
}
```

## When to use reliability checking

The reliability check service is ideal for scenarios where you need:

- **Model evaluation**: Easily integrate the service to compare model output quality.
- **RAG applications**: Verify that generated responses accurately reflect the provided reference documents rather than introducing fabricated information.
- **Internet-sourced verification**: Validate claims against reliable online sources with transparent citation of evidence.
- **Content moderation**: Automatically flag potentially misleading information before it reaches end users.
- **Regulatory compliance**: Ensure AI-generated content meets accuracy requirements.

## How to integrate reliability checks

Verify offers multiple ways to perform reliability checks, each designed for different use cases:

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Verify API__

    ---

    Verify the reliability and accuracy of an answer to a specific question via a dedicated API endpoint.

    [:octicons-arrow-right-24: Visit the guide](/get-started/verify/reliability/verify-api/){target=\_blank}

-   <span class="badge guide">Guide</span> Chat completion endpoint

    ---

    Validate responses in full conversation via the chat completions API using OpenAI libraries.

    [:octicons-arrow-right-24: Visit the guide](/get-started/verify/reliability/chat-completion/){target=\_blank}

</div>

## Additional resources

- **[Workflow integrations](/get-started/verify/reliability/workflow-integrations/){target=\_blank}**: Download ready-to-use workflows for Dify, n8n, and other platforms using direct API integration.
- **[Verify tutorial](/tutorials/klusterai-api/reliability-check){target=\_blank}**: Follow the Verify tutorial for step-by-step guidance on detecting and preventing reliability issues in your application.

