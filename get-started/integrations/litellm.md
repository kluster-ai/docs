---
title: Integrate LiteLLM with kluster.ai
description: This guide shows how to integrate LiteLLM, an open-source library that simplifies access to 100+ LLMs with load balancing and spend tracking, into kluster.ai.
---

# Integrating LiteLLM with the kluster.ai API

This guide shows you how to integrate [LiteLLM](https://www.litellm.ai/){target=_blank}—an open-source library providing unified access to 100+ large language models—with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. You can seamlessly develop and deploy robust, AI-driven applications by combining LiteLLM's load balancing, fallback logic, and spend tracking with kluster.ai's powerful models.

## Prerequisites

Before starting, ensure you have the following:

- [**LiteLLM installed**](https://github.com/BerriAI/litellm){target=\_blank} - to install the library, use the following command:

    ```bash
    pip install litellm
    ```

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

## Integrate with LiteLLM

It's straightforward to integrate kluster.ai with [LiteLLM](https://github.com/BerriAI/litellm){target=_blank}—just set the base URL and your kluster.ai API key via environment variables, then specify your chosen model.

  - **Base URL** - use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint
  - **API key** - replace `INSERT_API_KEY` in the code below with your kluster.ai API key. If you don't have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}
  - **Select your model** - choose the kluster.ai model that best fits your needs. For more details, see [kluster.ai's models](/api-reference/reference/#list-supported-models){target=\_blank}. Prepend the name of your selected model with `openai/` to ensure LiteLLM processes your requests using the OpenAI-style API

```python
import os

from litellm import completion

# Set environment vars, shown in script for readability
os.environ["OPENAI_API_KEY"] = "INSERT_KLUSTER_API_KEY"
os.environ["OPENAI_API_BASE"] = "https://api.kluster.ai/v1"

# Basic Chat
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user",   "content": "What is the capital of California?"}
]

response = completion(
    # Use an "openai/..." model prefix so LiteLLM treats this as an OpenAI-like call
    model="openai/klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
    messages=messages,
    max_tokens=1000, 
)

print(response)
```

That's it! You've successfully integrated LiteLLM with the kluster.ai API. You are now ready to harness the full power of kluster.ai with LiteLLM!

## Exploring LiteLLM Features

In the previous section, you learned how to use LiteLLM with the kluster.ai API by properly configuring the model via an OpenAI-like call and configuring the API key and API base URL. This section will dive deeper into some of the interesting features offered by LiteLLM and how you can use them in conjunction with the kluster.ai API.

To set up the demo file, go ahead and create a new python file, then take the following steps:

1. Import LiteLLM and its dependencies:  
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py::04"
```
2. Set your kluster API key and base URL:
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:06:09"
```
3. Set your desired kluster model:
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:10:11"
```
4. Define the system prompt and your first user message:
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:13:16"
```

### Streaming Responses

You can enable streaming by simply passing `stream=True` to the `completion()` function. This returns a generator instead of a static response, letting you iterate over partial output chunks as they arrive. In the code sample below, each chunk is accessed in a for chunk in response: loop, and you can extract just the textual content (e.g., `chunk.choices[0].delta.content)` rather than printing all metadata. 

To configure a streaming response, take the following steps:

1. Initiate a streaming request to the model by setting `stream=True` in the `completion()` function. This tells LiteLLM to return partial pieces (chunks) of the response as they become available, rather than waiting for the entire response to be ready.
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:18:32"
```
2. However, if we just return all of the streamed data, it's going to include a lot of excessive noise like token counts, etc. For readability, you probably prefer just the text content of the response. Isolate that from the rest of the streamed response with the following code:
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:34:42"
```

### Multi-Turn Conversation Handling

LiteLLM can facilitate multi-turn conversations by maintaining message history in a sequential chain, enabling the model to consider the context of previous messages. This section demonstrates multi-turn conversation handling by updating the messages list each time we receive a new response from the assistant. This pattern can be repeated for as many turns as you need, continuously appending messages to maintain the conversational flow.

Let's take a closer look at each step:

1. First, we need to combine the streamed chunks of the first message. Since they were streamed, they need to be re-assembled into a single message. After collecting partial responses in `streamed_text`, join them into a single string called `complete_first_answer`.
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:44:45"
```
2. Next, append the assistant’s reply to enhance the context of the conversation. Add this `complete_first_answer` back into messages under the "assistant" role as follows:
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:47:48"
```
3. Then, craft the 2nd message to the assistant. Append a new message object to messages with the user’s next question as follows:
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:50:57"
```
4. Now, ask the model for the response to the 2nd question, this time without the streaming feature enabled. Pass the updated messages to completion() with `stream=False`, prompting LiteLLM to generate a standard (single-shot) response as follows:
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:59:69"
```
5. Finally, parse and print the second answer. Extract `response_2.choices[0].message["content"]`, store it in `second_answer_text`, and print to the console for your final output: 
```python
--8<-- "code/get-started/integrations/litellm/litellm_features.py:71:76"
```

### Putting it All Together

You can find the full code file below, demonstrating a comparison of a streamed response vs. a regular response alongside handling a multi-turn conversation. 

??? code "litellm_features.py"
    ```python
    --8<-- "code/get-started/integrations/litellm/litellm_features.py"
    ```

Upon running it you'll see output like the following:

--8<-- 'code/get-started/integrations/litellm/terminal/output.md'

Both responses appear to trail off abruptly, but that's because we limited the output to `300` tokens each. Feel free to tweak the parameters and rerun the script at your leisure!