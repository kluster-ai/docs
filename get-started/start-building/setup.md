title: Start building with the kluster.ai API
description: The kluster.ai API getting started guide provides examples and instructions for submitting and managing Batch jobs using kluster.ai's OpenAI-compatible API.
---

# Start using the kluster.ai API

The [kluster.ai](https://www.kluster.ai/){target=\_blank} API provides a straightforward way to work with Large Language Models (LLMs) at scale. It is compatible with OpenAI's API and SDKs, making it easy to integrate into your existing workflows with minimal code changes.

This guide provides copy-and-paste examples for both Python and curl (although all OpenAI's SDKs are supported) and detailed explanations to help you get started quickly.

## Install prerequisites

The OpenAI Python library (version 1.0.0 or higher) is recommended, which can be installed with:

```bash
pip install "openai>=1.0.0"
```

## Get your API key

Navigate to the kluster.ai developer console [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key from there. You'll need this for all API requests.

For step-by-step instructions, refer to the [Get an API key](/get-started/get-api-key){target=\_blank} guide.

## API request limits

The following limits apply to API requests based upon your plan tier:

--8<-- "text/get-started/start-api/rate-limit.md"