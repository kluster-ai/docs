---
title: Integrate LangChain with kluster.ai
description: This guide walks you through integrating LangChain, a framework designed to simplify the development of LLM powered-applications, with the kluster.ai API.
---

# Using LangChain with the kluster.ai API

[LangChain](https://www.langchain.com/){target=\_blank} offers a range of features—like memory modules for context tracking, retrieval augmentation to feed external data into prompts, and customizable multi-step “chains” to break down complex tasks. By leveraging these capabilities with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API, you can build more robust and context-aware solutions that seamlessly handle everything from short-form answers to intricate conversations.

This guide demonstrates how to integrate the `ChatOpenAI` class from the `langchain_openai` package with the kluster.ai API, then walks through building a multi-turn conversational agent that leverages LangChain’s memory for context-aware interactions.

## Prerequisites

Before starting, ensure you have the following:

- **LangChain packages installed** - install the [`langchain` packages](https://github.com/langchain-ai/langchain){target=\_blank}:

    ```bash
    pip install langchain langchain_community langchain_core langchain_openai
    ```

    As a shortcut, you can also run:

    ```bash
    pip install "langchain[all]"
    ```

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

## Integrate with LangChain - Quick Start

It's easy to integrate kluster.ai with LangChain—just point your `ChatOpenAI` instance to the correct base URL and configure the following settings:

  - **Base URL** - use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint
  - **API key** - replace `INSERT_API_KEY` in the code below with your kluster.ai API key. If you don’t have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}
  - **Select your model** - choose one of kluster.ai’s available models based on your use case. For more details, see [kluster.ai’s models](/api-reference/reference/#list-supported-models){target=\_blank}

```python
--8<-- "code/get-started/integrations/langchain/langchain-quickstart.py"
```

That's all you need to start with LangChain and the kluster.ai API! Next, this guide will explore building a multi-turn conversational agent that showcases how memory and context can elevate your chatbot to a more interactive, intelligent experience.

## Building a multi-turn conversational agent

This section will explore what LangChain can do beyond a single prompt-and-response interaction. One standout feature of LangChain is its built-in memory, which tracks conversation context across multiple user queries. In the following steps, you'll set up a multi-turn conversational agent that takes advantage of this memory and seamlessly integrates with the kluster.ai API: 

1. First, import the necessary LangChain components for memory management, prompt handling, and kluster.ai integration 
```python title="hello_langchain.py"
--8<-- "code/get-started/integrations/langchain/langchain.py:01:06"
```
2. Next, create a memory instance to store and manage the conversation’s context, allowing the chatbot to remember previous user messages. Finally, you'll configure the `ChatOpenAI` model to point to kluster.ai’s endpoint (with your API key and chosen model). Remember, you can always change the selected model based on your needs 
```python title="hello_langchain.py"
--8<-- "code/get-started/integrations/langchain/langchain.py:08:10"
```
3. Next, define a prompt template that includes a system instruction for the assistant, a placeholder for the conversation history, and an input slot for the user’s query 
```python title="hello_langchain.py"
--8<-- "code/get-started/integrations/langchain/langchain.py:19:24"
```
4. You'll then create the `ConversationChain` by passing in the LLM, memory, and this prompt template—so every new user query is automatically enriched with the stored conversation context and guided by the assistant’s role
```python
--8<-- "code/get-started/integrations/langchain/langchain.py:26:31"
```
5. Now, it's time to prompt the model with the first question. You can prompt it with any question; the example chosen here is designed to demonstrate context awareness between questions
```python
--8<-- "code/get-started/integrations/langchain/langchain.py:33:37"
```
6. Finally, a follow-up question is posed without restating the city name—allowing LangChain’s memory to handle the context implicitly. By capturing and printing both the questions and the responses, you can see how multi-turn interactions work in practice, with each new query informed by the conversation
```python
--8<-- "code/get-started/integrations/langchain/langchain.py:39:43"
```

??? code "Complete script"
    ```python title="langchain.py"
    --8<-- 'code/get-started/integrations/langchain/langchain.py'
    ```

When running the complete script, you should see output that resembles the following:

--8<-- 'code/get-started/integrations/langchain/terminal/output.md'

That’s it! You’ve successfully integrated LangChain with the kluster.ai API, and your configured multi-turn conversational agent is ready to leverage the power of LangChain and the kluster.ai API. For more information about the capabilities of LangChain, be sure to check out the [LangChain docs](https://python.langchain.com/docs/introduction/){target=\_blank}.