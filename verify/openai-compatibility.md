---
title: Compatibility with OpenAI client libraries
description: Learn how kluster.ai is fully compatible with OpenAI client libraries, enabling seamless integration with your existing applications.
---

# OpenAI compatibility

The [kluster.ai](https://www.kluster.ai/){target=\_blank} API is compatible with [OpenAI](https://platform.openai.com/docs/api-reference/introduction){target=\_blank}'s API and SDKs, allowing seamless integration into your existing applications.

If you already have an application running with the OpenAI client library, you can easily switch to kluster.ai's API with minimal changes. This ensures a smooth transition without the need for significant refactoring or rework.

## Configuring OpenAI to use kluster.ai's API

Developers can use the OpenAI libraries with kluster.ai with no changes. To start, you need to install the library:

=== "Python"

    ```python
    pip install "openai>={{ libraries.openai_api.min_version }}"
    ```

To start using kluster.ai with OpenAI's client libraries, set your [API key](/get-api-key/){target=\_blank} and change the base URL to `https://api.kluster.ai/v1`:

=== "Python"

    ```python
    from openai import OpenAI
    
    client = OpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key="INSERT_API_KEY",  # Replace with your actual API key
    )
    ```

## Unsupported OpenAI features

While kluster.ai's API is largely compatible with OpenAI's, the following sections outline the specific features and fields that are currently unsupported.

### Chat completions parameters

When creating a chat completion via the [`POST https://api.kluster.ai/v1/chat/completions` endpoint](/api-reference/reference/#/http/api-endpoints/realtime/v1-chat-completions-post){target=\_blank}, the following request parameters are not supported:

- `messages[].name`: Attribute in `system`, `user`, and `assistant` type message objects.
- `messages[].refusal`: Attribute in `assistant` type message objects.
- `messages[].audio`: Attribute in `assistant` type message objects.
- `messages[].tool_calls`: Attribute in `assistant` type message objects.
- `store`
- `n`
- `modalities`
- `response_format`
- `service_tier`
- `stream_options`

The following request parameters are supported only with Llama models:

- `tools`
- `tool_choice`
- `parallel_tool_calls`

The following request parameters are *deprecated*:

- `messages[].function_call`: Attribute in `assistant` type message objects. <!-- TODO: Once `messages[].tool_calls` is supported, this should be updated to use `messages[].tool_calls instead -->
- `max_tokens`: Use `max_completion_tokens` instead.
- `function_call` <!-- TODO: Once `tool_choice` is supported, this should be updated to use `tool_choice` instead -->
- `functions` <!-- TODO: Once `tools` is supported, this should be updated to use `tools` instead -->

For more information on these parameters, refer to [OpenAI's API documentation on creating chat completions](https://platform.openai.com/docs/api-reference/chat/create){target=_blank}.

### Chat completion object

The following fields of the [chat completion object](/api-reference/reference/#/http/models/structures/v1-chat-completions-request){target=\_blank} are not supported:

- `system_fingerprint`
- `usage.completion_tokens_details`
- `usage.prompt_tokens_details`

For more information on these parameters, refer to [OpenAI's API documentation on the chat completion object](https://platform.openai.com/docs/api-reference/chat/object){target=_blank}.