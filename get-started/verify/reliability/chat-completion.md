---
title: Chat completion reliability verification
description: Learn how to use kluster verify to validate responses in full chat conversations.
---

# Chat completion

The Chat Completion method allows you to validate responses in full conversation histories using the same format as the standard chat completions API. This approach enables verification of reliability within the complete context of a conversation.

## Prerequisites

Before getting started with reliability verification, ensure the following requirements are met:

- **kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you do not have one
- **kluster.ai API key** - after signing in, go to the [API Keys](https://platform.kluster.ai/apikeys){target=_blank} section and create a new key. For detailed instructions, see the [Get an API key](https://docs.kluster.ai/get-started/get-api-key/){target=_blank} guide

## How it works

The service evaluates the truthfulness of responses within a conversation by:

1. Analyzing the entire conversation history, including system instructions.
2. Examining the assistant's responses within context.
3. Determining if the responses contain unreliable or unsupported information.
4. Providing a detailed explanation of the reasoning behind the determination and the search results used for fact-checking.

## Usage modes

The service operates in two distinct modes depending on whether you provide context with your request:

- **Dedicated Endpoint** - use the API directly without specifying a model.
- **OpenAI SDK** - select the verify-reliability model and use the SDK in a familiar way.

### Dedicated endpoint

By using the `/v1/verify/reliability` endpoint to check whether an assistant's answer is reliable.

??? example "CLI"

    ```bash
    #!/bin/bash
    
    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi
    
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
        "content": "Yes. There is a recent scientific study that confirms this
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
    from openai import OpenAI
    from getpass import getpass

    # Get API key from user input
    api_key = getpass("Enter your kluster.ai API key: ")

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

- Learn how to use [Question/answer reliability verification](/get-started/verify/reliability/question-answer/){target=_self} for simpler verification scenarios
- Review the complete [API documentation](/api-reference/reference/){target=_blank} for detailed endpoint specifications
