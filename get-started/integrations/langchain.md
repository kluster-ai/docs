---
title: Integrate LangChain with kluster.ai
description: This guide walks you through integrating LangChain, a framework designed to simplify development of LLM powered-applications, with the kluster.ai API.
---

# Using LangChain with the kluster.ai API

This guide demonstrates how to integrate the `ChatOpenAI` class from the `langchain_openai` package with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. By combining [LangChain](https://www.langchain.com/){target=\_blank}’s capabilities with kluster.ai’s large language models, you can seamlessly create powerful applications.

## Prerequisites

Before starting, ensure you have the following:

- **LangChain installed** - install the [`langchain` library](https://github.com/langchain-ai/langchain){target=\_blank}:

    ```bash
    pip install langchain
    ```

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

## Integrate with LangChain

It is very simple to integrate kluster.ai with LangChain—just point your `ChatOpenAI` instance to the correct base URL and configure a few settings.

  - **Base URL** - use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint
  - **API key** - replace `INSERT_API_KEY` in the code below with your own kluster.ai API key. If you don’t have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}
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

That's it! You’ve successfully integrated LangChain with the kluster.ai API. Your configured LLM is now ready to deliver the full range of LangChain capabilities.
