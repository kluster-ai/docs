---

title: Perform real-time inference jobs
description: This page provides examples and instructions for submitting and managing real-time jobs using kluster.ai's OpenAI-compatible API.
---

# Perform real-time inference jobs

## Overview

This guide provides guidance about how to use real-time inference with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. This type of inference is best suited for use cases requiring instant, synchronous responses for user-facing features like chat interactions, live recommendations, or real-time decision-making.

You will learn which models are supported for real-time inference jobs, how to submit a request and retrieve responses, and where to find integration guides for using kluster.ai's API with some of your favorite third-party LLM interfaces.

## Prerequisites

This guide assumes familiarity with Large Language Model (LLM) development and OpenAI libraries. Before getting started, make sure you have:

--8<-- 'text/kluster-api-onboarding.md'
- **A virtual Python environment** - (optional) recommended for developers using Python. It helps isolate Python installations in a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=\_blank} to reduce the risk of environment or package conflicts between your projects
- **Required Python libraries** - install the following Python libraries:
    - [**OpenAI Python API library**](https://pypi.org/project/openai/) - to access the `openai` module
    - [**`getpass`**](https://pypi.org/project/getpass4/) - to handle API keys safely

If you plan to use cURL via the CLI, you can export kluster.ai API key as a variable:

```bash
export API_KEY=INSERT_API_KEY
```

## Supported models

Real-time inferences through kluster.ai support the following models:

--8<-- 'text/real-time-models.md'

In addition, you can see the complete list of available models programmatically using the [list supported models](/api-reference/reference/#list-supported-models){target=\_blank} endpoint.

## Quickstart snippets

The following  code snippets provide a full end-to-end real-time inference example for different models supported by kluster.ai. You can simply copy the snippet and paste it into your local environment. 

### Python

To use these snippets, run the Python script and enter your kluster.ai API key when prompted.

??? example "DeepSeek R1"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-deepseekR1.py'
    ```

??? example "LLama 3.1 8B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.1-8.py'
    ```

??? example "LLama 3.1 405B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.1-405.py'
    ```

??? example "LLama 3.3 70B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.3-70.py'
    ```

### CLI

Similarly, the following curl commands showcase how to easily send a chat completion request to kluster.ai for the different supported models. This example assumes you've exported your kluster.ai API key as the variable `API_KEY`.


??? example "DeepSeek R1"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-deepseekR1.md'
    ```
    
??? example "LLama 3.1 8B"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.1-8.md'
    ```

??? example "LLama 3.1 405B"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.1-405.md'
    ```

??? example "LLama 3.3 70B"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.3-70.md'
    ```

## Real-time inference flow

This section goes through the details a real-time inference process using kluster.ai API and the DeepSeek R1 model, but you can adapt it to any of the [supported models](#supported-models).

### Submitting a request

The kluster.ai platform offers a simple, [OpenAI-compatible](/get-started/openai-compatibility/){target=\_blank} interface, making it easy to integrate kluster.ai services seamlessly into your existing system.

The following code shows how to do a chat completions request using the OpenAI library.

=== "Python"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-01.py:01:22'
    ```

If successful, the `completion` variable contains full response, which you'll need to analyze to extract the answer you are looking for. In terms of configuration for real-time inferences, there several parameters that you need to tweak:

- `model` – name of one of the [supported models](#supported-models)

- `messages` – in the `content` parameter, you should provide the query you want to process. You can pass any input here. In this example, the query is "What is the ultimate breakfast sandwich?"

Once these parameters are configured, run your script to send the request.

### Fetching the response

If the request is successful, the response is contained in the `completion` variable from the example above, and it should follow the structure demonstrated below and contain relevant data such as the generated output, metadata, and token usage details. 

```Json title="Response"
{
    "id": "chatcmpl-e9b942d1-06fb-4d1b-88c2-820c9ca7bb20",
    "choices": [
 {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "message": {
                "content": "The ultimate breakfast sandwich: toasted brioche, crispy bacon, melty cheddar, fried egg, avocado, and a dash of sriracha. Balance of crispy, creamy, savory, and spicy.",
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

The following snippet demonstrate how you can extract the data, log it to the console, and save it to a JSON file.

=== "Python"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-01.py:23:47'
    ```


For a detailed breakdown of the chat completion object, see the [**chat completion API reference**](/api-reference/reference#chat-completion-object){target=\_blank} section.

??? code "View the complete script"

    === "Python"

        ```python
        --8<-- 'code/get-started/start-building/real-time/real-time-01.py'
        ```

## Third-party integrations

You can also set up a [third-party LLM integrations](/get-started/integrations/){target=\_blank} using the kluster.ai API. For step-by-step instructions, check out the following integration guides:

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