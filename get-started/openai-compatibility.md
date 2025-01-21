---
title: Compatibility with OpenAI client libraries
description: Learn how kluster.ai is fully compatible with OpenAI client libraries, enabling seamless integration with your existing applications.
---

# OpenAI compatibility

The [kluster.ai](https://www.kluster.ai/){target=\_blank} API is highly compatible with [OpenAI](https://platform.openai.com/docs/api-reference/introduction){target=\_blank}'s client libraries, allowing seamless integration into your existing applications.

If you already have an application running with the OpenAI client library, you can easily switch to **kluster.ai's** API with minimal changes. This ensures a smooth transition without the need for significant refactoring or rework.

## Configuring OpenAI to use kluster.ai's API

To start using **kluster.ai** with OpenAI's client libraries, set your API key and change the base URL to `https://api.kluster.ai/v1`:

=== "Python"

    ```python
    from openai import OpenAI
    import json

    client = OpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key="INSERT_API_KEY",  # Replace with your actual API key
    )
    ```

!!! abstract "Note"
    If you don’t have an API key yet, you can generate one by following our [Get an API key](/get-started/get-api-key/){target=\_blank} guide.

## Unsupported OpenAI features

While **kluster.ai**'s API is largely compatible with OpenAI's, the features of the [chat completion](https://github.com/api-reference/chat/){target=_blank} endpoint outlined in the following section are currently not supported.

### Create chat completion

- `name` attribute in `system`, `user`, and `assistant` messages
- `refusal` attribute in `assistant` messages
- `audio` attribute in `assistant` messages
- `tool_calls`
- `function_call` 
- `store`
- `max_tokens`
- `n`
- `modalities`
- `response_format`
- `service_tier`
- `stream_options`
- `tools`
- `tool_choice`
- `parallel_tool_calls`
- `function_call`
- `functions`

### Chat completion object

- `system_fingerprint`
- `completion_tokens_details`
- `prompt_tokens_details`