---
title: Using Msty with the kluster.ai API
description: Learn how to integrate kluster.ai with CrewAI, a new framework for orchestrating autonomous AI agents, to launch and configure your AI agent chatbot.
---

# Using CrewAI with the kluster.ai API

[CrewAI](https://www.crewai.com/){target=\_blank} is a multi-agent platform that organizes specialized AI agents—each with defined roles, tools, and goals—within a structured process to tackle complex tasks efficiently. CrewAI agents streamline workflows and deliver reliable, scalable solutions by coordinating tasks and ensuring smooth collaboration.

This guide walks you through integrating [kluster.ai](https://www.kluster.ai/){target=\_blank} with CrewAI, from installation to creating and running a simple AI agent chatbot that leverages the kluster.ai API.

## Prerequisites

Before starting, ensure you have the following prerequisites:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide
- **CrewAI installed** - the [Installation Guide](https://docs.crewai.com/installation){target=\_blank} on the CrewAI website will walk you through installing CrewAI, setting up a virtual Python environment, and creating a new project. Note that CrewAI requires a Python version >=`3.10` and <`3.13`