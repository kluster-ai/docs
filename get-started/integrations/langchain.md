---
title: Integrate LangChain with kluster.ai
description: This guide walks you through integrating LangChain, a framework designed to simplify the development of LLM-powered applications with the kluster.ai API.
---

# Integrate LangChain with kluster.ai

[LangChain](https://www.langchain.com/){target=\_blank} offers a range of features—like memory modules for context tracking, retrieval augmentation to feed external data into prompts, and customizable multi-step “chains" to break down complex tasks. By leveraging these capabilities with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API, you can build more robust and context-aware solutions that seamlessly handle everything from short-form answers to intricate conversations.

This guide demonstrates how to integrate the `ChatOpenAI` class from the `langchain_openai` package with the kluster.ai API, then walks through building a multi-turn conversational agent that leverages LangChain's memory for context-aware interactions.

## Prerequisites

Before starting, ensure you have the following:

--8<-- 'text/kluster-api-onboarding.md'
- **[A python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=\_blank}**: This is optional but recommended. Ensure that you enter the Python virtual environment before following along with this tutorial.
- **LangChain packages installed**: Install the [`langchain` packages](https://github.com/langchain-ai/langchain){target=\_blank}:

    ```bash
    pip install langchain langchain_community langchain_core langchain_openai
    ```

    As a shortcut, you can also run:

    ```bash
    pip install "langchain[all]"
    ```

## Quick Start

It's easy to integrate kluster.ai with LangChain—when configuring the chat model, point your `ChatOpenAI` instance to the correct base URL and configure the following settings:

  - **Base URL**: Use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint.
  - **API key**: Replace `INSERT_API_KEY` in the code below with your kluster.ai API key. If you don't have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}.
  - **Select your model**: Choose one of [kluster.ai's available models](/get-started/models/){target=\_blank} based on your use case.

```python
--8<-- "code/get-started/integrations/langchain/langchain-quickstart.py"
```

That's all you need to start with LangChain and the kluster.ai API! Next, this guide will explore building a multi-turn conversational agent that showcases how memory and context can elevate your chatbot to a more interactive, intelligent experience.

## Build a multi-turn conversational agent

This section will explore what LangChain can do beyond a single prompt-and-response interaction. One standout feature of LangChain is its built-in memory, which tracks conversation context across multiple user queries. In the following steps, you'll set up a multi-turn conversational agent that takes advantage of this memory and seamlessly integrates with the kluster.ai API.

1. **Create file**: Create a new file called `langchain-advanced.py` using the following command in your terminal:
```bash
touch langchain-advanced.py
```

2. **Import LangChain components**: Inside your new file, import the following components for memory management, prompt handling, and kluster.ai integration:
```python
--8<-- "code/get-started/integrations/langchain/langchain-advanced.py:01:06"
```
3. **Create a memory instance**: To store and manage the conversation's context, allowing the chatbot to remember previous user messages.
```python
--8<-- "code/get-started/integrations/langchain/langchain-advanced.py:08:10"
```
4. **Configure the `ChatOpenAI` model**: Point to kluster.ai's endpoint with your API key and chosen model. Remember, you can always change the selected model based on your needs.
```python
--8<-- "code/get-started/integrations/langchain/langchain-advanced.py:12:17"
```
5. **Define a prompt template**: Include a system instruction for the assistant, a placeholder for the conversation history, and an input slot for the user's query.
```python
--8<-- "code/get-started/integrations/langchain/langchain-advanced.py:19:24"
```
6. **Create the `ConversationChain`**: Pass in the LLM, memory, and this prompt template so every new user query is automatically enriched with the stored conversation context and guided by the assistant's role.
```python
--8<-- "code/get-started/integrations/langchain/langchain-advanced.py:26:31"
```
7. **Prompt the model with the first question**: You can prompt the model with any question. The example chosen here is designed to demonstrate context awareness between questions.
```python
--8<-- "code/get-started/integrations/langchain/langchain-advanced.py:33:37"
```
8. **Pose a follow-up question**: Ask another question without resupplying the city name and notice how LangChain's memory implicitly handles the context. Return and print the questions and responses to see how the conversation informs each new query to create multi-turn interactions.
```python
--8<-- "code/get-started/integrations/langchain/langchain-advanced.py:39:43"
```

??? code "View complete script"
    ```python title="langchain-advanced.py"
    --8<-- 'code/get-started/integrations/langchain/langchain-advanced.py'
    ```
    
## Put it all together

1. Use the following command to run your script:
```bash
python langchain-advanced.py
```

2. You should see output that resembles the following:
    --8<-- 'code/get-started/integrations/langchain/terminal/output.md'

That's it! You've successfully integrated LangChain with the kluster.ai API, and your configured multi-turn conversational agent is ready to leverage the power of LangChain and the kluster.ai API. For more information about the capabilities of LangChain, be sure to check out the [LangChain docs](https://python.langchain.com/docs/introduction/){target=\_blank}.