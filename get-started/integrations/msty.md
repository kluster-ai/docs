---
title: Using Msty with the kluster.ai API
description: Learn how to integrate kluster.ai with CrewAI, a new framework for orchestrating autonomous AI agents, to launch and configure your AI agent chatbot.
---

# Using Msty with the kluster.ai API

[Msty](https://msty.app/){target=_blank} is a user-friendly local AI toolkit that also supports popular online model providers— all within a sleek, powerful interface. By eliminating tedious setup steps (no Docker or terminal required) and helping you manage attachments, Msty makes large language models more accessible than ever while making every conversation fully informed and flexible.

This guide will walk you through integrating [kluster.ai](https://www.kluster.ai/){target=\_blank} with Msty, from installation to hands-on interactions that tap into the kluster.ai API—all in a single, streamlined environment.

## Prerequisites

Before starting, ensure you have the following prerequisites:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide
- **Msty App installed** - The [Msty App](https://msty.app/){target=_blank} can be downloaded with one click. You can also find an [Installation Guide](https://docs.msty.app/getting-started/download){target=\_blank} on the Msty docs site

## Quick Start

Upon launching the Msty app for the first time, you'll be prompted to configure either a local AI or a remote AI provider. Select **Add Remote Model Provider**:

![Launch screen](/images/get-started/integrations/msty/msty-1.webp)

Then, take the following steps to configure Msty to use the kluster.ai API:

1. For the **Provider** dropdown, select **Open AI Compatible**

2. Provide a name, such as `kluster`

3. Provide the kluster.ai API URL for the **API endpoint** field:
    ```text
    https://api.kluster.ai/v1
    ```

4. Paste your API key and ensure **Save key securely in keychain** is selected
5. Paste the name of the [supported kluster.ai model](/api-reference/reference/#list-supported-models){target=\_blank} you'd like to use. Note that you can specify multiple models
6. Press **Add** to finalize the addition of kluster.ai API as a provider

![Configure remote model screen](/images/get-started/integrations/msty/msty-2.webp)

Great job! You’re now ready to use Msty to query LLMs through the kluster.ai API. For more information on Msty's features, be sure to check out the [Msty docs](https://docs.msty.app/getting-started/onboarding){target=\_blank}.

![Interact with LLM](/images/get-started/integrations/msty/msty-3.webp)
