---
title: Verify API endpoint
description: Validate the reliability of question-answer pairs using kluster.ai API, with or without context, to detect hallucinations and ensure response accuracy.
---

#  Reliability check via the Verify API

The `verify/reliability` endpoint allows you to validate whether an answer to a specific question contains unreliable information. This approach is ideal for verifying individual responses against the provided context (when the `context` parameter is included) or general knowledge (when no context is provided).

This guide provides a quick example of how use the `verify/reliability` endpoint for reliability check.

## Prerequisites

Before getting started with reliability verification, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'

## Endpoint parameters

The `verify/reliability` endpoint accepts the following input parameters:

- **`prompt`** (`string`| required): The question asked or instruction given. 
- **`output`** (`string`|required):  The LLM answer to verify for reliability.
- **`context`** (`string`|optional): Reference material to validate against.
- **`return_search_results`** (`boolean`|optional): Whether to include search results (default: false).

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

## How to use the Verify API

The reliability check feature operates in two distinct modes depending on whether you provide context with your request:

- **General knowledge verification**: When no context is provided, the service verifies answers against general knowledge and external sources.
- **Context validation mode**: When context is provided, the service only validates answers against the specified context.

### General knowledge verification

This example checks whether an answer contains unreliable information. As no context is provided, the answer will be verified against general knowledge to identify reliability issues.

=== "Python"

    ```python
    from os import environ
    import requests
    from getpass import getpass

    # Get API key from user input
    api_key = environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")

    print(f"📤 Sending a reliability check request to kluster.ai...\n")

    # Set up request data
    url = "https://api.kluster.ai/v1/verify/reliability"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": "Is earth flat?",
        "output": "Yes, my friend",
        "return_search_results": False #Optional
    }

    # Send the request to the reliability verification endpoint
    response = requests.post(url, headers=headers, json=payload)

    # Convert the response to JSON
    result = response.json()

    # Extract key information
    is_hallucination = result.get("is_hallucination")
    explanation = result.get("explanation")

    # Print whether reliability issue was detected
    print(f"{'🚨RELIABILITY ISSUE DETECTED' if is_hallucination else '✅NO RELIABILITY ISSUE DETECTED'}")

    # Print the explanation 
    print(f"\n🧠Explanation: {explanation}")

    # Print full response
    print(f"\n🔗API Response: {result}")
    ```
=== "CLI"

    ```bash
    #!/bin/bash
    
    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi
    
    echo -e "📤 Sending a reliability check request to kluster.ai...\n"
    
    # Submit reliability verification request
    response=$(curl --location 'https://api.kluster.ai/v1/verify/reliability' \
    --header "Authorization: Bearer $API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "prompt": "Is earth flat?",
        "output": "Yes, 100%.",
        "return_search_results": false 
    }')
    
    # Extract key information
    is_hallucination=$(echo "$response" | jq -r '.is_hallucination')
    explanation=$(echo "$response" | jq -r '.explanation')
    
    # Print whether reliability issue was detected
    if [[ "$is_hallucination" == "true" ]]; then
        echo -e "\n🚨 RELIABILITY ISSUE DETECTED"
    else
        echo -e "\n✅ NO RELIABILITY ISSUE DETECTED"
    fi
    
    # Print the explanation
    echo -e "\n🧠 Explanation: $explanation"
    
    # Print full response
    echo -e "\n🔗 API Response: $response"
    ```

### Context validation mode

When providing the `context` parameter, the service will not perform external verification. Instead, it focuses on whether the answer complies with the provided context.

!!! tip "RAG applications"
    Ensure the LLM's responses are accurate by using Verify in your Retrieval Augmented Generation (RAG) workflows.

This example checks whether an answer is correct based on the provided context.

=== "Python"

    ```python
    from os import environ
    import requests
    from getpass import getpass

    # Get API key from user input
    api_key = environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")

    print(f"📤 Sending a reliability check request with context to kluster.ai...\n")

    # Set up request data
    url = "https://api.kluster.ai/v1/verify/reliability"
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

    # Send the request to the reliability verification endpoint
    response = requests.post(url, headers=headers, json=payload)

    # Convert the response to JSON
    result = response.json()

    # Extract key information
    is_hallucination = result.get("is_hallucination")
    explanation = result.get("explanation")

    # Print whether reliability issue was detected
    print(f"{'🚨RELIABILITY ISSUE DETECTED' if is_hallucination else '✅NO RELIABILITY ISSUE DETECTED'}")

    # Print the explanation 
    print(f"\n🧠Explanation: {explanation}")

    # Print full response
    print(f"\n🔗API Response: {result}")
    ```

=== "CLI"

    ```bash
    #!/bin/bash

    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi

    echo -e "📤 Sending a reliability check request with context to kluster.ai...\n"


    # Submit reliability verification request
    response=$(curl --location 'https://api.kluster.ai/v1/verify/reliability' \
    --header "Authorization: Bearer $API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "prompt": "What is the invoice date?",
        "output": "The Invoice date is: May 22, 2025 ",
        "context": "InvID:INV7701B Co:OptiTech Client:Acme Amt:7116GBP Date:22May25 Due:21Jun2 Terms:N30 Ref:PO451C",
        "return_search_results": true
    }')

    # Extract key information
    is_hallucination=$(echo "$response" | jq -r '.is_hallucination')
    explanation=$(echo "$response" | jq -r '.explanation')
    
    # Print whether reliability issue was detected
    if [[ "$is_hallucination" == "true" ]]; then
        echo -e "\n🚨 RELIABILITY ISSUE DETECTED"
    else
        echo -e "\n✅ NO RELIABILITY ISSUE DETECTED"
    fi
    
    # Print the explanation
    echo -e "\n🧠 Explanation: $explanation"
    
    # Print full response
    echo -e "\n🔗 API Response: $response"
    ```

## Best practices

1. **Include relevant context**: When validating against specific information, provide comprehensive context.
2. **Use domain-specific context**: Include authoritative references for specialized knowledge domains.
3. **Consider general verification**: For widely known information, the service can verify against general knowledge sources.
4. **Review explanations**: The detailed explanations provide valuable insights into the reasoning process.

## Next steps

- Learn how to use [Chat completion reliability verification](/verify/reliability-check/chat-completion/){target=\_blank} for evaluating entire conversation histories
- Review the complete [API documentation](/api-reference/reference/#/http/api-endpoints/realtime/v1-verify-reliability-post){target=\_blank} for detailed endpoint specifications
