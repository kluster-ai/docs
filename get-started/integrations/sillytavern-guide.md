# SillyTavern configuration guide with kluster.ai API

This guide will help you set up and configure SillyTavern to use the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. Follow the steps below to integrate these tools seamlessly.

## Prerequisites

Before starting, ensure you have the following:

- **SillyTavern** installed on your system. For installation instructions, refer to the [SillyTavern Installation Guide](https://docs.sillytavern.app/installation/){target=\_blank}.
- Access to the **kluster.ai API**:
    - **Create an account -** if you don't have an account, sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank}
    - **Generate your API Key -** after creating your account, navigate to the **kluster.ai** developer console [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key from there

---

## Configure SillyTavern to use kluster.ai

1. Open SillyTavern in your preferred browser or application and access the settings menu in the top-left corner
2. In the **API** drop-down menu, select **Chat Completion**
3. In the **Chat Completion Source** option, choose **Custom (OpenAI-compatible)**
4. Enter the **kluster.ai** API endpoint `https://api.kluster.ai/v1/` in the **Custom Endpoint (Base URL)** field
5. Paste your **kluster.ai** API Key into the designated field
6. Click the **Connect** button. If everything is configured correctly, you should see a `Valid` message next to the button
7. Select one of the available models from **kluster.ai** listed in the **Available Models** drop-down menu
8. That’s it! You’re now ready to start chatting with your bot powered by **kluster.ai**

![SillyTavern Config Guide](/images/get-started/integrations/sillytavern-guide/sillytavern.webp)

---

## Test the connection

1. Start a new conversation with the model by clicking the menu icon on the bottom-left part of the page and selecting **Start New Chat**. This will open a new chat with the model.
2. Type a message in the **Type a message** bar at the bottom of the chat interface. This is where you can interact and create your message.
3. Send your message and verify that the response comes back successfully.

![SillyTavern chat example](/images/get-started/integrations/sillytavern-guide/chat-example.webp)

!!! failure "Troubleshooting"
    - If there are any errors, double-check your API key and URL. Be sure you receive a `Valid` response in Step 6 of [SillyTavern Config](#configure-sillytavern-to-use-klusterai)