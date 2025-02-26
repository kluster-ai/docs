---
title: Integrate SillyTavern with kluster.ai
description: This guide walks you through setting up SillyTavern, a customizable LLM interface, with the kluster.ai API to enable AI-powered conversations.
---

# Integrate SillyTavern with kluster.ai

This guide will help you set up and configure [SillyTavern](https://sillytavernai.com/){target=\_blank}, a customizable LLM interface, with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. Follow the steps below to integrate these tools seamlessly.

## Prerequisites

Before starting, ensure you have the following:

- **SillyTavern installed** - for installation instructions, refer to the SillyTavern [Installation](https://docs.sillytavern.app/installation/){target=\_blank} guide
- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

## Configure SillyTavern to use kluster.ai

1. Launch SillyTavern and open it in your browser at `http://127.0.0.1:8000/` (default port)
2. Click on the **API Connections** icon (plug) in the top navigation menu
3. In the **API** drop-down menu, select **Chat Completion**
4. In the **Chat Completion Source** option, choose **Custom (OpenAI-compatible)**
5. Enter the **kluster.ai** API endpoint in the **Custom Endpoint (Base URL)** field:

    ```text
    https://api.kluster.ai/v1
    ```

    There should be no trailing slash (`/`) at the end of the URL

6. Paste your **kluster.ai** API Key into the designated field
7. **Enter a Model ID**. For this example, you can enter:

    ```text
    klusterai/Meta-Llama-3.3-70B-Instruct-Turbo
    ```

8. Click the **Connect** button. If you've configured the API correctly, you should see a **🟢 Valid** message next to the button
9. Select one of the kluster.ai-supported models from the **Available Models** drop-down menu

![](/images/get-started/integrations/sillytavern/sillytavern-1.webp)

That's it! You're now ready to start chatting with your bot powered by kluster.ai.

## Test the connection

Now that you've configured kluster.ai with SillyTavern, you can test the API connection by starting a new conversation.

Follow these steps to get started:

1. Click the menu icon on the bottom-left corner of the page
2. Select **Start New Chat** to open a new chat with the model
3. Type a message in the **Type a message** bar at the bottom and send it
4. Verify that the chatbot has returned a response successfully

![](/images/get-started/integrations/sillytavern/sillytavern-2.webp)

!!! tip "Troubleshooting"
    If you encounter errors, revisit the [configuration instructions](#configure-sillytavern-to-use-klusterai) and double-check your API key and base URL and that you've received a **Valid** response after connecting the API (see step 8).
