---
title: Integrate LiteLLM with kluster.ai
description: This guide walks you through integrating LiteLLM, an open-source library that simplifies access to 100+ LLMs with load balancing and spend tracking, into kluster.ai.
---

# Integrating LiteLLM with the kluster.ai API

This guide shows you how to integrate [LiteLLM](https://www.litellm.ai/){target=_blank}—an open-source library providing unified access to 100+ large language models—with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. By combining LiteLLM’s load balancing, fallback logic, and spend tracking with kluster.ai’s powerful models, you can seamlessly develop and deploy robust, AI-driven applications.

## Prerequisites

Before starting, ensure you have the following:

- [**LiteLLM installed**](https://github.com/BerriAI/litellm){target=\_blank} - to install the library, use the following command:

    ```bash
    pip install litellm
    ```

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

## Integrate with LiteLLM

It’s straightforward to integrate kluster.ai with [LiteLLM](https://github.com/BerriAI/litellm){target=_blank}—just set the base URL and your kluster.ai API key via environment variables, then specify your chosen model.

  - **Base URL** - use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint
  - **API key** - replace `INSERT_API_KEY` in the code below with your own kluster.ai API key. If you don’t have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}
  - **Select your model** - choose any of kluster.ai’s available models that best fits your needs. For more details, see [kluster.ai’s models](/api-reference/reference/#list-supported-models){target=\_blank}. Regardless of which model you choose, prepend its name with `openai/`. This ensures LiteLLM processes your requests using the OpenAI-style API

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

That's it! You’ve successfully integrated LiteLLM with the kluster.ai API. You are now ready to harness the full power of kluster.ai with LiteLLM!
