---
title: Chat completion reliability verification
description: Learn how to use kluster verify to validate responses in full chat conversations.
---

# Reliability check via chat completion

Developers can access the reliability check feature via the regular chat completion endpoint. This allows you to validate responses in full conversation histories using the same format as the standard chat completions API. This approach enables verification of reliability within the complete context of a conversation.

This guide provides a quick example of how the chat completion endpoint can be used for reliability check.

## Prerequisites

Before getting started with reliability verification, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'

## How it works

The service evaluates the truthfulness of responses within a conversation by:

1. Analyzing the entire conversation history, including system instructions.
2. Examining the assistant's responses within context.
3. Determining if the responses contain unreliable or unsupported information.
4. Providing a detailed explanation of the reasoning behind the determination and the search results used for verification.

## Integration options

You can access the reliability verification service in two flexible ways, depending on your preferred development workflow:

- **Dedicated Endpoint**: Use the API directly without specifying a model via the `/v1/verify/reliability` endpoint.
- **OpenAI SDK**: Configure kluster.ai with [OpenAI libraries](/get-started/openai-compatibility/#configuring-openai-to-use-klusterais-api){target=\_blank}, and set the model to `klusterai/verify-reliability` via the `chat.completions.create` endpoint.

### Dedicated endpoint

The following snippet uses the `/v1/verify/reliability` endpoint to check whether an assistant's answer is reliable.

??? example "CLI"

    ```bash
    #!/bin/bash
    
    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi
    
    echo -e "📤 Sending a reliability request to kluster.ai...\n"
    
    # Submit reliability verification request
    curl --location 'https://api.kluster.ai/v1/verify/reliability' \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer $API_KEY" \
    --data '{
    "messages": [
      {
        "role": "system",
        "content": "You are a smart assistant that answers questions with full honesty and scientific accuracy"
      },
      {
        "role": "user",
        "content": "Are ghosts real?"
      },
      {
        "role": "assistant",
        "content": "Yes. There is a recent scientific study that confirms this."
      }
    ],
    "max_tokens": 3600,
    "temperature": 0.6,
    "top_p": 0.5,
    "stream": false
    }'

    ```

### OpenAI client

This example shows how to use the service with the `https://api.kluster.ai/v1` endpoint with the specialized `klusterai/verify-reliability` model.

??? example "Python"

    ```python
    from os import environ
    from openai import OpenAI
    from getpass import getpass

    # Get API key from user input
    api_key = environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")
    
    print(f"📤 Sending a reliability request to kluster.ai...\n")

    # Initialize OpenAI client pointing to kluster.ai API
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.kluster.ai/v1"
    )

    # Create chat completion request
    completion = client.chat.completions.create(
        model="klusterai/verify-reliability",
        messages = [
        {
            "role": "system",
            "content": "You are a knowledgeable assistant that provides accurate medical information."
        },
        {
            "role": "user",
            "content": "Does vitamin C cure the common cold?"
        },
        {
            "role": "assistant",
            "content": "Yes, taking large doses of vitamin C has been scientifically proven to cure the common cold within 24 hours."
        }
    ]
    )

    # Extract the reliability verification response
    text_response = completion.choices[0].message.content  

    # Print response to console
    print(text_response)
    
    ```

## Next steps

- Learn how to use the [Question/answer endpoint for reliability checks](/get-started/verify/reliability/question-answer/){target=_self} for simpler verification scenarios
- Review the complete [API documentation](/api-reference/reference/){target=_blank} for detailed endpoint specifications
