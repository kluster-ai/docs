---
title: Integrate LangChain with kluster.ai
description: This guide walks you through integrating LangChain, a framework designed to simplify the development of LLM powered-applications, with the kluster.ai API.
---

# Using LangChain with the kluster.ai API

[LangChain](https://www.langchain.com/){target=\_blank} offers a range of features—like memory modules for context tracking, retrieval augmentation to feed external data into prompts, and customizable multi-step “chains” to break down complex tasks. By leveraging these capabilities with the [kluster.ai API](https://www.kluster.ai/){target=\_blank}, you can build more robust and context-aware solutions that seamlessly handle everything from short-form answers to intricate conversations.

This guide demonstrates how to integrate the `ChatOpenAI` class from the `langchain_openai` package with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API, then walks through building a multi-turn conversational agent that leverages LangChain’s memory for context-aware interactions.

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
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key="INSERT_API_KEY", # Replace with your actual API key
    model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
)

llm.invoke("What is the capital of Nepal?")
```

That's all you need to get started with LangChain and the kluster.ai API! Next, this guide will explore building a multi-turn conversational agent that showcases how memory and context can elevate your chatbot to a more interactive, intelligent experience.

## Building a Multi-Turn Conversational Agent

This section will dive deeper into exploring what LangChain can do beyond a single prompt-and-response interaction. One standout feature of LangChain is its built-in memory, which tracks conversation context across multiple user queries. In the following steps, we’ll set up a multi-turn conversational agent that takes advantage of this memory and seamlessly integrates with the kluster.ai API.

First, import the necessary LangChain components for memory management, prompt handling, and kluster.ai integration. Next, create a memory instance to store and manage the conversation’s context, allowing the chatbot to remember previous user messages. Finally, we configure the `ChatOpenAI` model to point to kluster.ai’s endpoint (with your API key and chosen model). Remember, you can always change the selected model based on your needs. 

```python
--8<-- "code/get-started/integrations/langchain/langchain.py:01:17"
```

Next, define a prompt template that includes a system instruction for the assistant, a placeholder for the conversation history, and an input slot for the user’s query. We then create the `ConversationChain` by passing in the LLM, memory, and this prompt template—so every new user query is automatically enriched with the stored conversation context and guided by the assistant’s role.

```python
--8<-- "code/get-started/integrations/langchain/langchain.py:19:30"
```

In this final portion, user inputs are crafted and sent in multiple conversation turns. First, the chatbot is prompted for interesting facts about Kathmandu. Then, a follow-up question is posed without restating the city name—allowing LangChain’s memory to handle the context implicitly. By capturing and printing both the questions and the responses, you can see how multi-turn interactions work in practice, with each new query informed by the conversation.

```python
--8<-- "code/get-started/integrations/langchain/langchain.py:33:43"
```

??? code "Complete Script"
    ```python title="langchain.py"
    --8<-- 'code/get-started/integrations/langchain/langchain.py'
    ```


Finally, upon running it you should see output like the following:

--8<-- 'code/get-started/integrations/langchain/terminal/output.md'

That’s it! You’ve successfully integrated LangChain with the kluster.ai API, and your configured multi-turn conversational agent is ready to leverage the power of LangChain and the kluster.ai API. For more information about the capabilities of LangChain, be sure to check out the [LangChain Docs](https://python.langchain.com/docs/introduction/){target=\_blank}.