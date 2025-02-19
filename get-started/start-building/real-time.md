---

title: Start Performing Real-Time Inferences
description: This page provides examples and instructions for submitting and managing real time jobs using kluster.ai's OpenAI-compatible API.
---

This page gives a quick overview of how to use real-time inferences with the Kluster API. This type of inference is best suited for situations where you need instant, synchronous responses—perfect for user-facing features like chat interactions, live recommendations, or real-time decision-making.

## Submitting a  request

**kluster.ai** platform provides you with a simple interface that is OpenAI compatible. This will allow you to use seamlessly integrate Kluster services within your existing platform.

Example below provides simple interface 

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
    api_key="INSERT_API_KEY", # Replace with your actual API key
    base_url="https://api.kluster.ai/v1"
    )

    completion = client.chat.completions.create(
    model = "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
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

As it
`model` parimiter can be configured per your needs, Kluster supports several models:

- `klusterai/Meta-Llama-3.1-8B-Instruct-Turbo`
- `klusterai/Meta-Llama-3.1-405B-Instruct-Turbo`
- `klusterai/Meta-Llama-3.3-70B-Instruct-Turbo`
- `deepseek-ai/DeepSeek-R1`