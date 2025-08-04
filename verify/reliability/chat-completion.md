---
title: Chat completion Verify API
description: Validate full chat conversations for reliability using the kluster.ai chat completion endpoint. Analyze context and detect misinformation.
---

# Reliability via chat completion

Developers can access Reliability via the regular chat completion endpoint. This allows you to validate responses in full conversation histories using the same format as the standard chat completions API. This approach enables verification of reliability within the complete context of a conversation.

This guide provides a quick example of how the chat completion endpoint can be used for reliability checks.

## Prerequisites

Before getting started with Reliability, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'
- **A virtual Python environment**: (Optional) Recommended for developers using Python. It helps isolate Python installations in a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=\_blank} to reduce the risk of environment or package conflicts between your projects
- **Required Python libraries**: Install the following Python libraries:
    - [**OpenAI Python API library**](https://pypi.org/project/openai/){target=\_blank}: to access the `openai` module
    - [**`getpass`**](https://pypi.org/project/getpass4/){target=\_blank}: To handle API keys safely


## Integration options

You can access the reliability verification service in two flexible OpenAI compatible ways, depending on your preferred development workflow. For both, you'll need to set the model to `klusterai/verify-reliability`:

- **OpenAI compatible endpoint**: Use the OpenAI API `/v1/chat/completions` pointing to kluster.ai.
- **OpenAI SDK**: Configure kluster.ai with [OpenAI libraries](/verify/openai-compatibility/#configuring-openai-to-use-klusterais-api){target=\_blank}. Next, the `chat.completions.create` endpoint.

## Reliability via chat completions

This example shows how to use the service with the chat completion endpoint via the OpenAI `/v1/chat/completions` endpoint and OpenAI libraries, using the specialized `klusterai/verify-reliability` model to enable Verify Reliability check.

=== "Python"

    ```python
    --8<-- 'code/verify/reliability/python-example.py'
    ```

=== "CLI"

    ```bash
    --8<-- 'code/verify/reliability/bash-example.sh'
    ```

## Next steps

- Learn how to use the [Verify API](/verify/reliability/verify-api/){target=\_blank} for simpler verification scenarios
