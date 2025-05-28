---
title: Chat Completion Hallucination Detection
description: Learn how to use the kluster.ai Hallucination Detection API to validate responses in full chat conversations.
---

# Chat Completion

The Chat Completion method allows you to validate responses in full conversation histories using the same format as the standard chat completions API. This approach enables detection of hallucinations within the complete context of a conversation.

## Prerequisites

Before getting started with hallucination detection, ensure the following requirements are met:

- **kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you do not have one
- **kluster.ai API key** - after signing in, go to the [API Keys](https://platform.kluster.ai/apikeys){target=_blank} section and create a new key. For detailed instructions, see the [Get an API key](https://docs.kluster.ai/get-started/get-api-key/){target=_blank} guide

## How it works

The service evaluates the truthfulness of responses within a conversation by:

1. Analyzing the entire conversation history, including system instructions.
2. Examining the assistant's responses within context.
3. Determining if the responses contain hallucinated or unsupported information.
4. Providing a detailed explanation of the reasoning behind the determination as well as the search results used for fact checking.

## Usage modes

The agent operates in two distinct modes depending on whether you provide context with your request:

- **Dedicated Endpoint** - no need to specify a model, via API.
- **OpenAI SDK** - define the Hallucination Detection Agent and use the SDK as normal.

### Dedicated endpoint

By using the `/v1/judges/detect-hallucination` endpoint to check whether an assistant's answer is hallucination.

??? example "CLI"

    ```bash
    #!/bin/bash
    
    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi
    
    # Submit hallucination detection request
    curl --location 'https://api.kluster.ai/v1/judges/detect-hallucination' \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer $API_KEY" \
    --data '{
    "messages": [
      {
        "role": "system",
        "content": "You are smart assistant which answer questions with full honestly and with scientific accuracy"
      },
      {
        "role": "user",
        "content": "Are ghosts real??"
      },
      {
        "role": "assistant",
        "content": "Yes. There is recent scientific study which confirms this"
      }
    ],
    "max_tokens": 3600,
    "temperature": 0.6,
    "top_p": 0.5,
    "stream": false
    }'

    ```

### OpenAI client

This example shows how to use the agent with the `https://api.kluster.ai/v1` endpoint with the specialized `klusterai/hallucination-detection` model.

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
        model="klusterai/hallucination-detection",
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

    #Extract the hallucination detection response
    text_response = completion.choices[0].message.content  

    # Print response to console
    print(text_response)
    
    ```

## Next steps

- Learn how to use [Question/Answer Hallucination Detection](/get-started/hallucination-agent/question-answer/){target=_self} for simpler verification scenarios
- Explore [Examples](/get-started/hallucination-agent/examples/){target=_self} of hallucination detection in real-world scenarios
- Review the complete [API documentation](/api-reference/reference/){target=_blank} for detailed endpoint specifications
