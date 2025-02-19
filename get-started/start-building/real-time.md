---

title: Start Performing Real-Time Inferences
description: This page provides examples and instructions for submitting and managing real time jobs using kluster.ai's OpenAI-compatible API.
---

This page gives a quick overview of how to use real-time inferences with the Kluster API. This type of inference is best suited for situations where you need instant, synchronous responses—perfect for user-facing features like chat interactions, live recommendations, or real-time decision-making.

## Submitting a Request

The **kluster.ai** platform offers a simple, OpenAI-compatible interface, making it easy to integrate Kluster services seamlessly into your existing system.

The example below demonstrates a pre-configured interface to get you started:

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
    api_key="INSERT_API_KEY", # Replace with your actual API key
    base_url="https://api.kluster.ai/v1"
    )

    completion = client.chat.completions.create(
    model = "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo", # Configure which model uoi want to use
    messages = [
        { "role": "user", "content": "What are some fun things to do?" } 
    ]
    )
    ```

=== "curl"

    ``` curl
    curl https://api.kluster.ai/v1/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \ # Replace with your actual API key
    -H "Content-Type: application/json" \
    -d '{
        "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo", # Can be configured to use any of models supported by Kluster
        "messages": [
        { "role": "user", "content": "What are some fun things to do?" }
        ]
    }'
    ```

There are several configurable parimiters when using real-time inferences:

-  `model` – This can be set based on your specific needs. **Kluster** supports multiple models, allowing you to choose the best fit for your use case. Simply replace the model parameter with one of the options below:

    - `klusterai/Meta-Llama-3.1-8B-Instruct-Turbo`
    - `klusterai/Meta-Llama-3.1-405B-Instruct-Turbo`
    - `klusterai/Meta-Llama-3.3-70B-Instruct-Turbo`
    - `deepseek-ai/DeepSeek-R1`

- `messages` – In the `content` parameter, you should provide the query you want to process. You can pass any input here. In our case, we are querying...

## Response
```Json title="Response"
{
    "id": "chatcmpl-e9b942d1-06fb-4d1b-88c2-820c9ca7bb20",
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "message": {
                "content": "The most famous street in Paris is the Champs-Élysées.",
                "refusal": null,
                "role": "assistant",
                "audio": null,
                "function_call": null,
                "tool_calls": []
            },
            "stop_reason": null
        }
    ],
    "created": 1739960163,
    "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    "object": "chat.completion",
    "service_tier": null,
    "system_fingerprint": null,
    "usage": {
        "completion_tokens": 16,
        "prompt_tokens": 47,
        "total_tokens": 63,
        "completion_tokens_details": null,
        "prompt_tokens_details": null
    },
    "prompt_logprobs": null
}
```