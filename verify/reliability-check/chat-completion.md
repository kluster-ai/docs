---
title: Chat completion Verify API
description: Validate full chat conversations for reliability using the kluster.ai chat completion endpoint. Analyze context and detect misinformation.
---

# Reliability check via chat completion

Developers can access the reliability check feature via the regular chat completion endpoint. This allows you to validate responses in full conversation histories using the same format as the standard chat completions API. This approach enables verification of reliability within the complete context of a conversation.

This guide provides a quick example of how the chat completion endpoint can be used for reliability checks.

## Prerequisites

Before getting started with reliability verification, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'
- **A virtual Python environment**: (Optional) Recommended for developers using Python. It helps isolate Python installations in a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=\_blank} to reduce the risk of environment or package conflicts between your projects
- **Required Python libraries**: Install the following Python libraries:
    - [**OpenAI Python API library**](https://pypi.org/project/openai/){target=\_blank}: to access the `openai` module
    - [**`getpass`**](https://pypi.org/project/getpass4/){target=\_blank}: To handle API keys safely


## Integration options

You can access the reliability verification service in two flexible OpenAI compatible ways, depending on your preferred development workflow. For both, you'll need to set the model to `klusterai/verify-reliability`:

- **OpenAI compatible endpoint**: Use the OpenAI API `/v1/chat/completions` pointing to kluster.ai.
- **OpenAI SDK**: Configure kluster.ai with [OpenAI libraries](/verify/openai-compatibility/#configuring-openai-to-use-klusterais-api){target=\_blank}. Next, the `chat.completions.create` endpoint.

## Reliability checks via chat completions

This example shows how to use the service with the chat completion endpoint via the OpenAI `/v1/chat/completions` endpoint and OpenAI libraries, using the specialized `klusterai/verify-reliability` model to enable Verify reliability check.

=== "Python"

    ```python
    from os import environ
    from openai import OpenAI
    from getpass import getpass

    # Get API key from user input
    api_key = environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")
    
    print(f"📤 Sending a reliability check request to kluster.ai...\n")

    # Initialize OpenAI client pointing to kluster.ai API
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.kluster.ai/v1"
    )

    # Create chat completion request
    completion = client.chat.completions.create(
        model="klusterai/verify-reliability", # Note special model
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

=== "CLI"

    ```bash
    #!/bin/bash

    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi
    
    echo -e "📤 Sending a chat completion request to kluster.ai...\n"
    
    # Submit real-time request
    curl https://api.kluster.ai/v1/chat/completions \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
                "model": "deepseek-ai/DeepSeek-R1", 
                "messages": [
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
            }'
    ```

## Next steps

- Learn how to use the [Verify API](/verify/reliability-check/verify-api/){target=\_blank} for simpler verification scenarios
- Review the complete [API documentation](/api-reference/reference/#/http/api-endpoints/realtime/v1-verify-reliability-post){target=\_blank} for detailed endpoint specifications
