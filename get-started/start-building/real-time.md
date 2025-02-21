---

title: Perform real-time inference jobs
description: This page provides examples and instructions for submitting and managing real-time jobs using kluster.ai's OpenAI-compatible API.
---

# Perform real-time inference jobs

## Overview

This guide provides guidance about how to use real-time inference with the [kluster.ai](https://platform.kluster.ai/){target=\_blank} API. This type of inference is best suited for use cases requiring instant, synchronous responses for user-facing features like chat interactions, live recommendations, or real-time decision-making.

You will learn which models are supported for real-time inference jobs, how to submit a request and retrieve responses, and where to find integration guides for using kluster.ai's API with some of your favorite third-party LLM interfaces.

## Prerequisites

This guide assumes familiarity with basic Python and Large Language Model (LLM) development. Before getting started, make sure you have:

- **An active kluster API key** - if you don't already have one, see the [Get an API key](/get-started/get-api-key/){target=\_blank} guide for instructions
- **A virtual Python environment** - this optional but recommended step helps isolate Python installations in a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=\_blank} to reduce the risk of environment or package conflicts between your projects

## Supported models

Real-time inferences through kluster.ai support the following models:

--8<-- 'text/real-time-models.md'

In addition, you can see the complete list of available models programmatically using the [list supported models](/api-reference/reference/#list-supported-models){target=\_blank} endpoint.

## Submitting a request

The kluster.ai platform offers a simple, [OpenAI-compatible](/get-started/openai-compatibility/){target=\_blank} interface, making it easy to integrate kluster.ai services seamlessly into your existing system.

The following examples demonstrate a pre-configured interface to get you started. Options are included for Python and curl.

=== "Python"

    ```python
    --8<-- 'code/get-started/integrations/start-building/real-time/real-time-01.py'
    ```

=== "curl"

    ``` curl
    curl https://api.kluster.ai/v1/chat/completions \
        -H "Authorization: Bearer YOUR_API_KEY" \ # Replace with your actual API key
        -H "Content-Type: application/json" \
        -d '{
                "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo", 
                "messages": [
                    { 
                        "role": "user", 
                        "content": "What is the most famous street in Paris?" 
                    }
                ]
            }'
    ```

There are several configurable parameters when using real-time inferences:

- `model` – name of one of the [supported models](#supported-models)

- `messages` – in the `content` parameter, you should provide the query you want to process. You can pass any input here. In this example, the query is "What is the most famous street in Paris?"

Once these parameters are configured, run your script to send the request.

## Response

If the request is successful, the response should follow the structure demonstrated below and contain relevant data such as the generated output, metadata, and token usage details. 

The following is an example of what a real-time response might look like:

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

For a detailed breakdown of the chat completion object, see the [**chat completion API reference**](/api-reference/reference#chat-completion-object){target=\_blank} section.

## Third-party integrations

You can also set up a third-party LLM interface using the kluster.ai API. For step-by-step instructions, check out the following integration guides:

- [**SillyTavern**](/get-started/integrations/sillytavern){target=\_blank} - multi-LLM chat interface
- [**LangChain**](/get-started/integrations/langchain/){target=\_blank} - multi-turn conversational agent
- [**eliza**](/get-started/integrations/eliza/){target=\_blank} - create and manage AI agents
- [**CrewAI**](/get-started/integrations/crewai/){target=\_blank} - specialized agents for complex tasks
- [**LiteLLM**](/get-started/integrations/litellm/){target=\_blank} - streaming response and multi-turn conversation handling

## Summary

You have now experienced the complete real-time inference job lifecycle using kluster.ai's chat completion API. In this guide, you've learned:

- How to submit a real-rime inference request
- How to configure real-time inference related API parameters
- How to interpret the chat completion object API response

The kluster.ai batch API is designed to efficiently and reliably handle your large-scale LLM workloads. If you have questions or suggestions, the [support](mailto:support@kluster.ai){target=\_blank} team would love to hear from you.