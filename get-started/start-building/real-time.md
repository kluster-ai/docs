---

title: Perform real-time inference jobs
description: This page provides examples and instructions for submitting and managing real-time jobs using kluster.ai's OpenAI-compatible API.
---

# Perform real-time inference jobs

## Overview

This guide provides guidance about how to use real-time inference with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. This type of inference is best suited for use cases requiring instant, synchronous responses for user-facing features like chat interactions, live recommendations, or real-time decision-making.

You will learn how to submit a request and retrieve responses, and where to find integration guides for using kluster.ai's API with some of your favorite third-party LLM interfaces. Please make sure you check the [API request limits](/get-started/models/#api-request-limits){target=\_blank}.

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

Please visit the [Models](/get-started/models/){target=\_blank} page to learn more about all the models supported by the kluster.ai batch API.

In addition, you can see the complete list of available models programmatically using the [list supported models](/api-reference/reference/#list-supported-models){target=\_blank} endpoint.

## Quickstart snippets

The following code snippets provide a complete end-to-end real-time inference example for different models supported by kluster.ai. You can copy and paste the snippet into your local environment. 

### Python

To use these snippets, run the Python script and enter your kluster.ai API key when prompted.

??? example "DeepSeek R1"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-deepseekR1.py'
    ```

??? example "DeepSeek V3 0324"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-deepseekV3-0324.py'
    ```

??? example "Gemma 3 27B"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-gemma3-27.py'
    ```

??? example "LLama 3.1 8B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.1-8.py'
    ```

??? example "LLama 3.3 70B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.3-70.py'
    ```

??? example "Llama 4 Maverick 17B 128E"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-llama4-maverick.py'
    ```

??? example "Llama 4 Scout 17B 16E"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-llama4-scout.py'
    ```

??? example "Qwen 2.5 7B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-qwen2.5-7.py'
    ```

??? example "Qwen 3 235B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-qwen3-235.py'
    ```    

??? example "Mistral Nemo Instruct 2407"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-mistral-nemo-instruct-2407.py'
    ```

### CLI

Similarly, the following curl commands showcase how to easily send a chat completion request to kluster.ai for the different supported models. This example assumes you've exported your kluster.ai API key as the variable `API_KEY`.


??? example "DeepSeek R1"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-deepseekR1.md'
    ```

??? example "DeepSeek V3 0324"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-deepseekV3-0324.md'
    ```

??? example "Gemma 3 27B"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-gemma3-27.md'
    ```
    
??? example "LLama 3.1 8B"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.1-8.md'
    ```

??? example "LLama 3.3 70B"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-llama3.3-70.md'
    ```

??? example "Llama 4 Maverick 17B 128E"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-llama4-maverick.md'
    ```

??? example "Llama 4 Scout 17B 16E"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-llama4-scout.md'
    ```

??? example "Qwen 2.5 7B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-qwen2.5-7.md'
    ```

??? example "Qwen 3 235B"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-qwen3-235.md'
    ```   

??? example "Mistral Nemo Instruct 2407"

    ```bash
    --8<-- 'code/get-started/start-building/real-time/real-time-mistral-nemo-instruct-2407.md'
    ```   

## Real-time inference flow

This section details the real-time inference process using the kluster.ai API and DeepSeek R1 model, but you can adapt it to any of the [supported models](/get-started/models/){target=\_blank}.

### Submitting a request

The kluster.ai platform offers a simple, [OpenAI-compatible](/get-started/openai-compatibility/){target=\_blank} interface, making it easy to integrate kluster.ai services seamlessly into your existing system.

The following code shows how to do a chat completions request using the OpenAI library.

=== "Python"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-01.py:01:22'
    ```

If successful, the `completion` variable contains a full response, which you'll need to analyze to extract the answer you are looking for. In terms of configuration for real-time inferences, there are several parameters that you need to tweak:

- `model` ++"string"++ <span class="required" markdown>++"required"++</span> - name of one of the [supported models](/get-started/models/){target=\_blank}
- `messages` ++"array"++ <span class="required" markdown>++"required"++</span> - a list of chat messages (`system`, `user`, or `assistant` roles, and also `image_url` for images). In this example, the query is "What is the ultimate breakfast sandwich?". 

Once these parameters are configured, run your script to send the request.

### Fetching the response

If the request is successful, the response is contained in the `completion` variable from the example above. It should follow the structure below and include relevant data such as the generated output, metadata, and token usage details. 

```Json title="Response"
{
    "id": "a3af373493654dd195108b207e2faacf",
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "message": {
                "content": "The \"ultimate\" breakfast sandwich is subjective and can vary based on personal preferences, but here’s a classic, crowd-pleasing version that combines savory, sweet, and hearty elements for a satisfying morning meal:\n\n### **The Ultimate Breakfast Sandwich**\n**Ingredients:**\n- **Bread:** A toasted brioche bun, English muffin, or sourdough slice (your choice for texture and flavor).\n- **Protein:** Crispy bacon, sausage patty, or ham.\n- **Egg:** Fried, scrambled, or a fluffy omelet-style egg.\n- **Cheese:** Sharp cheddar, gooey American, or creamy Swiss.\n- **Sauce:** Spicy mayo, hollandaise, or a drizzle of maple syrup for sweetness.\n- **Extras:** Sliced avocado, caramelized onions, sautéed mushrooms, or fresh arugula for a gourmet touch.\n- **Seasoning:** Salt, pepper, and a pinch of red pepper flakes for heat.\n\n**Assembly:**\n1. Toast your bread or bun to golden perfection.\n2. Cook your protein to your desired crispiness or doneness.\n3. Prepare your egg—fried with a runny yolk is a classic choice.\n4. Layer the cheese on the warm egg or protein so it melts slightly.\n5. Add your extras (avocado, veggies, etc.) for freshness and flavor.\n6. Spread your sauce on the bread or drizzle it over the filling.\n7. Stack everything together, season with salt, pepper, or spices, and enjoy!\n\n**Optional Upgrades:**\n- Add a hash brown patty for extra crunch.\n- Swap regular bacon for thick-cut or maple-glazed bacon.\n- Use a croissant instead of bread for a buttery, flaky twist.\n\nThe ultimate breakfast sandwich is all about balance—crunchy, creamy, savory, and a hint of sweetness. Customize it to your taste and make it your own!",
                "refusal": null,
                "role": "assistant",
                "audio": null,
                "function_call": null,
                "tool_calls": null
            },
            "matched_stop": 1
        }
    ],
    "created": 1742378836,
    "model": "deepseek-ai/DeepSeek-V3-0324",
    "object": "chat.completion",
    "service_tier": null,
    "system_fingerprint": null,
    "usage": {
        "completion_tokens": 398,
        "prompt_tokens": 10,
        "total_tokens": 408,
        "completion_tokens_details": null,
        "prompt_tokens_details": null
    }
}
```

The following snippet demonstrates how to extract the data, log it to the console, and save it to a JSON file.

=== "Python"

    ```python
    --8<-- 'code/get-started/start-building/real-time/real-time-01.py:23:47'
    ```


For a detailed breakdown of the chat completion object, see the [chat completion API reference](/api-reference/reference#chat-completion-object){target=\_blank} section.

??? code "View the complete script"

    === "Python"

        ```python
        --8<-- 'code/get-started/start-building/real-time/real-time-01.py'
        ```

## Third-party integrations

You can also set up [third-party LLM integrations](/get-started/integrations/){target=\_blank} using the kluster.ai API. For step-by-step instructions, check out the following integration guides:

- [**SillyTavern**](/get-started/integrations/sillytavern){target=\_blank} - multi-LLM chat interface
- [**LangChain**](/get-started/integrations/langchain/){target=\_blank} - multi-turn conversational agent
- [**eliza**](/get-started/integrations/eliza/){target=\_blank} - create and manage AI agents
- [**CrewAI**](/get-started/integrations/crewai/){target=\_blank} - specialized agents for complex tasks
- [**LiteLLM**](/get-started/integrations/litellm/){target=\_blank} - streaming response and multi-turn conversation handling

## Summary

You have now experienced the complete real-time inference job lifecycle using kluster.ai's chat completion API. In this guide, you've learned:

- How to submit a real-rime inference request
- How to configure real-time inference-related API parameters
- How to interpret the chat completion object API response

The kluster.ai batch API is designed to efficiently and reliably handle your large-scale LLM workloads. If you have questions or suggestions, the [support](mailto:support@kluster.ai){target=\_blank} team would love to hear from you.