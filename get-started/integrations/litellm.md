---
title: Integrate LiteLLM with kluster.ai
description: This guide shows how to integrate LiteLLM, an open-source library that simplifies access to 100+ LLMs with load balancing and spend tracking, into kluster.ai.
---

# Integrating LiteLLM with the kluster.ai API

[LiteLLM](https://www.litellm.ai/){target=_blank} is an open-source Python library that streamlines access to a broad range of Large Language Model (LLM) providers through a standardized interface inspired by the OpenAI format. By providing features like fallback mechanisms, cost tracking, and streaming support, LiteLLM reduces the complexity of working with different models, ensuring a more reliable and cost-effective approach to AI-driven applications.

Integrating LiteLLM with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API enables the use of kluster.ai's powerful models alongside LiteLLM's flexible orchestration. This combination makes it simple to switch between models on the fly, handle token usage limits with context window fallback, and monitor usage costs in real-time—leading to robust, scalable, and adaptable AI workflows.

## Prerequisites

Before starting, ensure you have the following:

- **[A python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=\_blank}** - This is optional but recommended. Ensure that you enter the Python virtual environment before following along with this tutorial
- [**LiteLLM installed**](https://github.com/BerriAI/litellm){target=\_blank} - to install the library, use the following command:

    ```bash
    pip install litellm
    ```

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

## Integrate with LiteLLM

In this section, you'll learn how to integrate kluster.ai with LiteLLM. You’ll configure your environment variables, specify a kluster.ai model, and make a simple request using LiteLLM’s OpenAI-like interface.

1. **Import LiteLLM and its dependencies** - Create a new file (e.g., `hello-litellm.py`) and start by importing the necessary Python modules:
```python
--8<-- "code/get-started/integrations/litellm/hello-litellm.py::04"
```
2. **Set your kluster.ai API key and Base URL** - Replace INSERT_API_KEY with your actual API key. If you don't have one yet, refer to the [Get an API key](/get-started/get-api-key/){target=\_blank}
```python
--8<-- "code/get-started/integrations/litellm/hello-litellm.py:05:08"
```
3. **Define your conversation (system + user messages)** - Set up your initial system prompt and user message. The system message defines your AI assistant’s role, while the user message is the actual question or prompt
```python
--8<-- "code/get-started/integrations/litellm/hello-litellm.py:09:13"
```
4. **Select your kluster.ai model** - Choose one of the kluster.ai [models](/api-reference/reference/#list-supported-models){target=_blank} that best fits your use case. Prepend the model name with `openai/` so LiteLLM recognizes it as an OpenAI-like model request.
```python
--8<-- "code/get-started/integrations/litellm/hello-litellm.py:15:16"
```
5. **Call the LiteLLM completion function** - Finally, invoke the completion function to send your request:
```python
--8<-- "code/get-started/integrations/litellm/hello-litellm.py:18:24"
```

??? code "View full code file"
    ```python
    --8<-- "code/get-started/integrations/litellm/hello-litellm.py"
    ```

Use the following command to run your script:

```python
python hello-litellm.py
```

--8<-- 'code/get-started/integrations/litellm/terminal/hello-litellm-output.md'

That's it! You've successfully integrated LiteLLM with the kluster.ai API. Continue on to learn how to experiment with more advanced features of LiteLLM.

## Exploring LiteLLM Features

In the previous section, you learned how to use LiteLLM with the kluster.ai API by properly configuring the model via an OpenAI-like call and configuring the API key and API base URL. This section will dive deeper into some of the interesting features offered by LiteLLM and how you can use them in conjunction with the kluster.ai API.

To set up the demo file, go ahead and create a new python file, then take the following steps:

1. Import LiteLLM and its dependencies:  
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py::04"
```
2. Set your kluster API key and base URL:
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:06:09"
```
3. Set your desired kluster model:
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:10:11"
```
4. Define the system prompt and your first user message:
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:13:16"
```

### Streaming Responses

You can enable streaming by simply passing `stream=True` to the `completion()` function. This returns a generator instead of a static response, letting you iterate over partial output chunks as they arrive. In the code sample below, each chunk is accessed in a for chunk in response: loop, and you can extract just the textual content (e.g., `chunk.choices[0].delta.content)` rather than printing all metadata. 

To configure a streaming response, take the following steps:

1. Initiate a streaming request to the model by setting `stream=True` in the `completion()` function. This tells LiteLLM to return partial pieces (chunks) of the response as they become available, rather than waiting for the entire response to be ready.
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:18:32"
```
2. However, if we just return all of the streamed data, it's going to include a lot of excessive noise like token counts, etc. For readability, you probably prefer just the text content of the response. Isolate that from the rest of the streamed response with the following code:
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:34:42"
```

### Multi-Turn Conversation Handling

LiteLLM can facilitate multi-turn conversations by maintaining message history in a sequential chain, enabling the model to consider the context of previous messages. This section demonstrates multi-turn conversation handling by updating the messages list each time we receive a new response from the assistant. This pattern can be repeated for as many turns as you need, continuously appending messages to maintain the conversational flow.

Let's take a closer look at each step:

1. First, we need to combine the streamed chunks of the first message. Since they were streamed, they need to be re-assembled into a single message. After collecting partial responses in `streamed_text`, join them into a single string called `complete_first_answer`.
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:44:45"
```
2. Next, append the assistant’s reply to enhance the context of the conversation. Add this `complete_first_answer` back into messages under the "assistant" role as follows:
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:47:48"
```
3. Then, craft the 2nd message to the assistant. Append a new message object to messages with the user’s next question as follows:
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:50:57"
```
4. Now, ask the model for the response to the 2nd question, this time without the streaming feature enabled. Pass the updated messages to completion() with `stream=False`, prompting LiteLLM to generate a standard (single-shot) response as follows:
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:59:69"
```
5. Finally, parse and print the second answer. Extract `response_2.choices[0].message["content"]`, store it in `second_answer_text`, and print to the console for your final output: 
```python
--8<-- "code/get-started/integrations/litellm/litellm-features.py:71:76"
```

### Putting it All Together

You can find the full code file below, demonstrating a comparison of a streamed response vs. a regular response alongside handling a multi-turn conversation. 

??? code "litellm-features.py"
    ```python
    --8<-- "code/get-started/integrations/litellm/litellm-features.py"
    ```

Upon running it you'll see output like the following:

--8<-- 'code/get-started/integrations/litellm/terminal/output.md'

Both responses appear to trail off abruptly, but that's because we limited the output to `300` tokens each. Feel free to tweak the parameters and rerun the script at your leisure!