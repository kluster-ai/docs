title: Start building with the kluster.ai API
description: The kluster.ai API getting started guide provides examples and instructions for submitting and managing Batch jobs using kluster.ai's OpenAI-compatible API.
---

# Start using the kluster.ai API

The [kluster.ai](https://www.kluster.ai/){target=\_blank} API provides a straightforward way to work with Large Language Models (LLMs) at scale. It is [compatible with OpenAI's API and SDKs](/get-started/openai-compatibility/){target=\_blank}, making it easy to integrate into your existing workflows with minimal code changes.

## Get your API key

Navigate to the kluster.ai developer console [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. You'll need this for all API requests.

For step-by-step instructions, refer to the [Get an API key](/get-started/get-api-key){target=\_blank} guide.

## Set up the OpenAI client library

Developers can use the OpenAI libraries with kluster.ai with no changes. To start, you need to install the library:

=== "Python"

    ```python
    pip install "openai>={{ libraries.openai_api.min_version }}"
    ```

Once the library is installed, you can instantiate an OpenAI client pointing to kluster.ai with the following code and replacing `INSERT_API_KEY`:

=== "Python"

    ```python
    from openai import OpenAI
        
    client = OpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key="INSERT_API_KEY",  # Replace with your actual API key
    )
    ```

Check the [kluster.ai OpenAI compatibility page](/get-started/openai-compatibility/){target=\_blank} for detailed information about the integration.

## API request limits

--8<-- "text/get-started/rate-limit.md"

## Where to go next

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Real-time inference__

    ---

    Build AI-powered applications that deliver instant, real-time responses.

    [:octicons-arrow-right-24: Visit the guide](/get-started/start-building/real-time/)

-   <span class="badge guide">Guide</span> __Batch inference__

    ---

    Process large-scale data efficiently with AI-powered batch inference.

    [:octicons-arrow-right-24: Visit the guide](/get-started/start-building/batch/)

-   <span class="badge guide">Reference</span> __API reference__

    ---

    Explore the complete kluster.ai API documentation and usage details.

    [:octicons-arrow-right-24: Reference](/api-reference/reference/)


</div>