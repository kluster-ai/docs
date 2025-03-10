---
title: Integrate TypingMind with the kluster.ai API
description: Learn how to configure TypingMind, an intuitive frontend chat interface that offers organization, prompt libraries, and AI agent support, with kluster.ai.
---

# Integrate TypingMind with kluster.ai

[TypingMind](https://www.typingmind.com/){target=\_blank} is an intuitive frontend chat interface that enhances the UX of LLMs. It offers flexible organization for your conversations (folders, pins, bulk delete), a customizable prompt library, and the ability to build AI agents using your training data. With plugin support for internet access, image generation, and more, TypingMind seamlessly syncs across devices, providing a simplified AI workflow with tailored, high-quality responses—all in one sleek platform.

This guide will walk you through integrating [kluster.ai](https://www.kluster.ai/){target=\_blank} with TypingMind, from configuration to hands-on interactions that tap into the kluster.ai API—all in a single, streamlined environment.

## Prerequisites

Before starting, ensure you have the following prerequisites:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

## Quick start

Navigate to [TypingMind](https://www.typingmind.com/){target=\_blank} and take the following steps to access the custom model setup:

1. Click on the model dropdown
2. Click on **Custom Models**

![Launch screen](/images/get-started/integrations/typingmind/typingmind-1.webp)

Then, take the following steps to configure TypingMind to use the kluster.ai API:

1. Provide a name, such as `kluster`
2. For the **API Type** dropdown, select **OpenAI Compatible API**
3. Provide the following URL for the **Endpoint** field:

    ```text
    https://api.kluster.ai/v1/chat/completions
    ```

4. Paste the name of the [supported kluster.ai model](/api-reference/reference/#list-supported-models){target=\_blank} you'd like to use. Note that you can specify multiple models
5. Press **Add Custom Headers** and for the **Key** value, specify `Authorization`. In the value field on the right, enter `Bearer` followed by your kluster.ai API key as follows: 

    ```text
    Bearer INSERT_KLUSTER_API_KEY
    ``` 

6. Press **Test** to ensure the connection is successful
7. Press **Add Model** to confirm adding the kluster.ai as a custom provider

![Configure kluster.ai API as a provider](/images/get-started/integrations/typingmind/typingmind-2.webp)

## Set default provider

You've configured the kluster.ai API as a provider, but it hasn't yet been selected as the default one. To change this, take the following steps: 

1. Click on **Models** on the sidebar
2. Select **kluster** (or whatever you named your custom model)
3. Press **Set Default**

![Configure kluster.ai API as a provider](/images/get-started/integrations/typingmind/typingmind-3.webp)

And that's it! You can now query the LLM successfully using kluster.ai as the default provider. For more information on TypingMind's features, be sure to check out the [TypingMind docs](https://docs.typingmind.com/){target=\_blank}. The following section will examine one of TypingMind's features: prebuilt AI agents.

![Query TypingMind](/images/get-started/integrations/typingmind/typingmind-4.webp)

## Start a chat

TypingMind has a wide variety of prebuilt AI agents that you can use as-is or clone and customize to suit your needs. These AI agents can use the kluster.ai API to perform tasks tailored to your use cases. To get started, take the following steps:

1. Click on **Agents** in the sidebar
2. Click on **Browse Agents**

![Agents home](/images/get-started/integrations/typingmind/typingmind-5.webp)

Then select the desired agent you'd like to interact with and press the green icon to install it into your TypingMind workspace. 

![Install new agent](/images/get-started/integrations/typingmind/typingmind-6.webp)

Press **Chat Now** to open up a new chat session with your AI agent:

![Install new agent](/images/get-started/integrations/typingmind/typingmind-7.webp)

Your AI agent is now ready to answer relevant questions and relies on the kluster.ai API to do so:

![Install new agent](/images/get-started/integrations/typingmind/typingmind-8.webp)

You can also clone and customize existing agents or create entirely new ones. For more information on agents on TypingMind, be sure to check out the [TypingMind docs](https://docs.typingmind.com/ai-agents/ai-agents-overview){target=\_blank}.