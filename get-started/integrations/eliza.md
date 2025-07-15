---
title: Integrate eliza with kluster.ai
description: Learn how to integrate kluster.ai with eliza, a fast, lightweight, and flexible AI agent framework, to launch and configure your own AI agent chatbot. 
---

# Integrate eliza with kluster.ai

[eliza](https://eliza.how/){target=\_blank} is an open-source framework designed to create and manage AI agents that can handle a variety of tasks, from simple chat interactions to more complex automation.

In this guide, you'll learn how to integrate [kluster.ai](https://www.kluster.ai/) into eliza to leverage its powerful models and quickly set up your AI-driven workflows.

## Prerequisites

Before starting, ensure you have the following kluster prerequisites:

--8<-- 'text/kluster-api-onboarding.md'
- **Clone and install the eliza repository**: Follow the installation instructions on the [eliza Quick Start guide](https://eliza.how/docs/quickstart){target=\_blank}.
    
!!! warning

    Pay careful attention to the eliza prerequisites, including the minimum supported versions of Node.js and pnpm. You will not be able to successfully follow this guide using npm or yarn.

- Stop at the **Configure Environment** section in the Quick Start guide, as this guide covers those steps

## Configure your environment

After installing eliza, it's simple to utilize kluster.ai with eliza. Only three main changes to the `.env` file are required. 

1. **Create `.env` file**: Run the following command to generate a `.env` file from the eliza repository example:
```bash
cp .env.example .env
```

2. **Set variables**: Update the following variables in the `.env` file:
    - **`OPENAI_API_KEY`**: Replace `INSERT_API_KEY` in the code below with your kluster.ai API key. If you don't have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}.
    - **`OPENAI_API_URL`**: Use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint.
    - **`OPENAI_DEFAULT_MODEL`**: Choose one of [kluster.ai's available models](/get-started/models/){target=\_blank} based on your use case. You should also set `SMALL_OPENAI_MODEL`, `MEDIUM_OPENAI_MODEL`, and `LARGE_OPENAI_MODEL` to the same value to allow seamless experimentation as different characters use different default models.

The OpenAI configuration section of your `.env` file should resemble the following:

```bash title=".env"
# OpenAI Configuration
OPENAI_API_KEY=INSERT_KLUSTER_API_KEY
OPENAI_API_URL=https://api.kluster.ai/v1

# Community Plugin for OpenAI Configuration
OPENAI_DEFAULT_MODEL=klusterai/Meta-Llama-3.3-70B-Instruct-Turbo
SMALL_OPENAI_MODEL=klusterai/Meta-Llama-3.3-70B-Instruct-Turbo
MEDIUM_OPENAI_MODEL=klusterai/Meta-Llama-3.3-70B-Instruct-Turbo
LARGE_OPENAI_MODEL=klusterai/Meta-Llama-3.3-70B-Instruct-Turbo
```

## Run and interact with your first agent

Now that you've configured your environment, you're ready to run your first agent! eliza has several characters you can interact with by prompting or through autonomous tasks like tweeting. This guide relies on the `Dobby` character for its minimal setup requirements.

1. **Verify character configuration**: Open the `dobby.character.json` file inside the `characters` folder. By default, `Dobby` uses the `openai` model, which you've already configured to use the kluster.ai API. The `Dobby` configuration should start with the following:
```json title="dobby.character.json"
{
  "name": "Dobby",
  "clients": [],
  "modelProvider": "openai" // json truncated for clarity
}
```

2. **Run the agent**: Run the following command from the project root directory to run the `Dobby` agent:
```bash
pnpm start --character="characters/dobby.character.json"
``` 

3. **Launch the UI**: In another terminal window, run the following command to launch the web UI: 
```bash
pnpm start:client
```
  Your terminal output should resemble the following:
  --8<-- 'code/get-started/integrations/eliza/terminal/launch-client.md'

4. **Open your browser**: Follow the prompts and open your browser to `http://localhost:5173/`.

## Put it all together

You can now interact with Dobby by selecting on the **Send Message** button and starting the conversation: 

![Chat with Dobby AI agent](/images/get-started/integrations/eliza/eliza-1.webp)

That's it! You've successfully integrated eliza with the kluster.ai API. You're now ready to harness the power of AI agents with the kluster.ai API!