---
title: Question - answer 
description: Learn how to use the kluster.ai Hallucination Detection API to validate the truthfulness of answers to questions.
---

# Question/Answer

The Question/Answer method allows you to validate whether an answer to a specific question contains hallucinated information. This approach is ideal for fact-checking individual responses against provided context or general knowledge.

## Prerequisites

Before getting started with fine-tuning, ensure you have the following:

- **kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you do not have one
- **kluster.ai API key** - after signing in, go to the [API Keys](https://platform.kluster.ai/apikeys){target=_blank} section and create a new key. For detailed instructions, see the [Get an API key](https://docs.kluster.ai/get-started/get-api-key/){target=_blank} guide


## How it works

The service evaluates the truthfulness of an answer to a question by:

1. Analyzing the original question or prompt.
2. Examining the provided answer.
3. Determining if the answer contains hallucinated or unsupported information.
4. Providing a detailed explanation of the reasoning behind the determination as well as the search results used for fact-checking.

### Parameters

| Parameter | Type | Required | Description |
| :---: | :---: | :---: | :---: |
| `prompt` | string | Yes | The question asked or instruction given. |
| `output` | string | Yes | The answer to verify for hallucinations. |
| `context` | string | No | Optional reference material to validate against. |
| `return_search_results` | boolean | No | Whether to include search results (default: false). |


The API returns a JSON object with the following structure:

```json
{
    "is_hallucination": boolean,
    "usage": {
        "completion_tokens": number,
        "prompt_tokens": number,
        "total_tokens": number
    },
    "explanation": "string",
    "search_results": []  // Only included if return_search_results is true
}
```
## Usage modes

The agent operates in two distinct modes depending on whether you provide context with your request:

- **Fact-checking mode** - when no context is provided, the agent verifies answers against general knowledge and external sources.
- **Context validation mode** - when context is provided, the agent only validates answers against the specified context.

### Fact-checking mode

This example checks whether an answer contains hallucinated information. As no context is provided, the answer will be fact-checked against general knowledge to identify hallucinations.

??? example "Python"

    ```python
    import requests
    from getpass import getpass

    # Get API key from user input
    api_key = getpass("Enter your kluster.ai API key: ")

    # Set up request data
    url = "https://api.kluster.ai/v1/judges/detect-hallucination"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": "Is earth flat?",
        "output": "Yes, my friend",
        "return_search_results": False #Optional
    }

    # Send the request to the hallucination detection endpoint
    response = requests.post(url, headers=headers, json=payload)

    # Convert the response to JSON
    result = response.json()

    # Extract key information
    is_hallucination = result.get("is_hallucination")
    explanation = result.get("explanation")

    # Print full response
    print(f"🔗 API Response: {result}")

    # Print whether hallucination was detected
    print(f"{'HALLUCINATION DETECTED' if is_hallucination else 'NO HALLUCINATION DETECTED'}")

    # Print the explanation 
    print(f"\nExplanation: {explanation}")
    ```
??? example "CLI"

    ```bash
    #!/bin/bash

    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi

    # Submit hallucination detection request
    curl --location 'https://api.kluster.ai/v1/judges/detect-hallucination' \
    --header "Authorization: Bearer $API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "prompt": "Is earth flat?",
        "output": "Yes, my friend",
        "return_search_results": false 
    }'
    ```

### Context validation mode

When providing the `context` parameter, the agent will not perform external fact-checking. Instead, it focuses on whether the answer complies with the provided context.

!!! tip "RAG applications"
    Ensure the LLM's responses are accurate by using the Hallucination Detection Agent in your Retrieval Augmented Generation workflows.


This example checks whether an answer is correct based on the provided context.

??? example "Python"

    ```python
    import requests
    from getpass import getpass

    # Get API key from user input
    api_key = getpass("Enter your kluster.ai API key: ")

    # Set up request data
    url = "https://api.kluster.ai/v1/judges/detect-hallucination"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": "What's the invoice date?",
        "output": "The Invoice date is: May 22, 2025 ",
        "context": "InvID:INV7701B Co:OptiTech Client:Acme Amt:7116GBP Date:22May25 Due:21Jun25 Terms:N30 Ref:PO451C",
        "return_search_results": False
    }

    # Send the request to the hallucination detection endpoint
    response = requests.post(url, headers=headers, json=payload)

    # Convert the response to JSON
    result = response.json()

    # Extract key information
    is_hallucination = result.get("is_hallucination")
    explanation = result.get("explanation")

    # Print full response
    print(f"🔗 API Response: {result}")

    # Print whether hallucination was detected
    print(f"{'HALLUCINATION DETECTED' if is_hallucination else 'NO HALLUCINATION DETECTED'}")

    # Print the explanation 
    print(f"\nExplanation: {explanation}")
    ```

??? example "CLI"

    ```bash
    #!/bin/bash

    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi

    # Submit hallucination detection request
    curl --location 'https://api.kluster.ai/v1/judges/detect-hallucination' \
    --header "Authorization: Bearer $API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "prompt": "What's the invoice date?",
        "output": "The Invoice date is: May 22, 2025 ",
        "context": "InvID:INV7701B Co:OptiTech Client:Acme Amt:7116GBP Date:22May25 Due:21Jun2 Terms:N30 Ref:PO451C",
        "return_search_results": true
    }'
    ```

## Best practices

1. **Include relevant context** - When validating against specific information, provide comprehensive context.
2. **Use domain-specific context** - Include authoritative references for specialized knowledge domains.
3. **Consider fact-checking only** - For common facts, the service can verify against general knowledge.
5. **Review explanations** - The detailed explanations provide valuable insights into the reasoning process.

## Next steps

- Learn how to use [Chat Completion Hallucination Detection](/get-started/hallucination-agent/chat-completion/){target=_self} for evaluating entire conversation histories
- Explore [Examples](/get-started/hallucination-agent/examples/){target=_self} of hallucination detection in real-world scenarios
- Review the complete [API documentation](/api-reference/reference/){target=_blank} for detailed endpoint specifications
