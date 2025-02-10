---
title: Using eliza with the kluster.ai API
description: Learn how to integrate kluster.ai with Eliza, a fast, lightweight, and flexible AI agent framework, to launch and configure your own AI agent chatbot. 
---

# Using Eliza with the kluster.ai API

[Eliza](https://elizaos.github.io/eliza/){target=\_blank} is an open-source framework designed to create and manage AI agents that can handle a variety of tasks, from simple chat interactions to more complex automation. In this tutorial, we'll show you how to integrate kluster.ai into Eliza so you can leverage its powerful models and quickly set up your AI-driven workflows.

## Prerequisites

Before starting, ensure you have the following kluster prerequisites:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

Next, you can clone and install the Eliza repository by following the installation instructions on the [Eliza Quick Start guide](https://elizaos.github.io/eliza/docs/quickstart/){target=\_blank}. Pay careful attention to the Eliza prerequisites, including the minimum supported versions of Node.js and pnpm. You can pause at the **Configure Environment** section in the Quick Start guide, as we will proceed with those steps in this guide.

## Configure your environment

After you have Eliza installed, it's simple to utilize kluster.ai with Eliza. Only three main changes to the `.env` file are required. You can run the following command to generate a `.env` file from the provided example. 

```bash
cp .env.example .env
```

Then, set the following variables in the `.env` file: 

  - **OPENAI_API_KEY** - replace `INSERT_API_KEY` in the code below with your own kluster.ai API key. If you don't have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}
  - **OPENAI_API_URL** - use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint
  - **OPENAI_DEFAULT_MODEL** - choose one of kluster.ai's available models based on your use case. Ensure that the model's full name starting with `klusterai/` is listed. For more details, see [kluster.ai’s models](/api-reference/reference/#list-supported-models){target=\_blank}

The OpenAI configuration section of your `.env` file should resemble the following:

```bash
# OpenAI Configuration
OPENAI_API_KEY=INSERT_KLUSTER_API_KEY
OPENAI_API_URL=https://api.kluster.ai/v1

# Community Plugin for OpenAI Configuration
OPENAI_DEFAULT_MODEL=klusterai/Meta-Llama-3.3-70B-Instruct-Turbo
```

## Run and Interact with your First Agent

Now that you've configured your environment properly you're ready to run your first agent! Eliza comes with a number of characters that you can interact with by prompting or that can autonomously perform tasks like tweeting. This guide relies on the `Dobby` character for its minimal setup requirements. Other agents, particularly those that handle tweets, would necessitate additional steps, such as X login information, etc. 

By default, `Dobby` uses the `openai` model, which we have properly configured to rely on the kluster.ai API, but it doesn't hurt to double-check the `dobby.character.json` file under the `characters` folder. You should see the configuration start with the following:

```
{
    "name": "Dobby",
    "clients": [],
    "modelProvider": "openai",
```

To run the `Dobby` agent, run the following command from the project root directory:

```bash
pnpm start --character="characters/dobby.character.json"
``` 

In another terminal window, run the following command to launch the web UI: 

```bash
pnpm start:client
```

You can now interact with Dobby by clicking on the **Chat** button and starting the conversation: 

![Chat with Dobby AI agent](/images/get-started/integrations/eliza/eliza-1.webp)

That's it! You've successfully integrated Eliza with the kluster.ai API. You're now ready to harness the power of AI agents with the kluster.ai API! 
