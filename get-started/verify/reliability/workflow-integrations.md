---
title: Workflow Integrations
description: Easily integrate Verify into Dify, n8n, and more with ready-made workflows to automate AI response validation via API in minutes.
---

# Workflow integrations

You can integrate the Verify reliability check feature into your favorite automation platforms with ready-to-use workflow templates. These pre-configured workflows connect directly to the kluster.ai API, allowing you to add AI verification capabilities to your existing processes in minutes.

## Prerequisites

Before getting started with the workflow integrations, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'
- **Workflow platform**: Set up [Dify](https://dify.ai/){target=\_blank}, [n8n](https://n8n.io/){target=\_blank}, or your preferred automation tool

## Available Workflows

### Dify

By using [Dify](https://dify.ai/){target=\_blank}, you can build AI applications with built-in reliability verification. 

This workflow seamlessly integrates Verify into your Dify chatbots and agents, ensuring every response is validated for accuracy and trustworthiness before reaching your users.

![Dify workflow for kluster verify](/images/get-started/verify/dify_workflow.webp)

**Configure kluster.ai as a Model Provider** 

1. Navigate to **Settings** and select **Model Provider**.
2. Click on **Add Provider** and choose **OpenAI-API-compatible**.

Enter these settings:

- **Base URL**: `https://api.kluster.ai/v1`.
- **API Key**: Your kluster.ai API key.
- **Model**: Select from [available models](https://platform.kluster.ai/models){target=\_blank}.

Save and test the connection to ensure it works properly.

**Set up the kluster verify node:**

1. Select the HTTP Request node `kluster verify`.
2. Add your API key to the Authorization header.

**Import and Configure the Workflow** 

Download the workflow template below and import it into your Dify workspace. 

The workflow comes pre-configured to verify AI responses in real-time.

[Download Dify Workflow](workflows/dify_workflow.yml){target=\_blank .md-button}

### n8n

Add verification checkpoints to your [n8n](https://n8n.io/){target=\_blank} automation pipelines.

This workflow validates AI-generated content against your source documents, tools, or real-time data, perfect for ensuring accuracy in automated content generation and data processing workflows.

![n8n workflow for kluster verify](/images/get-started/verify/n8n_workflow.webp)

**Set Up API Credentials**

- Select the OpenAI and choose **Credentials**. Then click **Create New**.

- **Base URL**: `https://api.kluster.ai/v1`.
- **API Key**: Your kluster.ai API key.
- **Model**: Select from [available models](https://platform.kluster.ai/models){target=\_blank}.

**Set up the kluster verify node API key:**

Open the kluster verify node and modify the headers as follow:

- **Header Name**: `Authorization`.
- **Header Value**: `Bearer YOUR_API_KEY`.


**Import and Configure the Workflow** 

Download the workflow template below and import it via the n8n interface. 

The workflow includes pre-configured HTTP nodes that connect to the `/v1/verify/reliability` endpoint, handle request/response formatting, and parse verification results. Connect your data sources and configure output routing as needed.

[Download n8n Workflow](workflows/n8n_workflow.json){target=\_blank .md-button}

## Next Steps

Ready to build more reliable AI applications?

- **Explore the API**: Check the [complete API reference](/api-reference/reference/#/http/api-endpoints/realtime/v1-verify-reliability-post){target=\_blank} for advanced configuration options.
- **Learn verification methods**: Dive into the [Verify API endpoint](/get-started/verify/reliability/verify-api/){target=\_blank} for detailed implementation patterns.
- **Try the tutorial**: Follow the [hands-on reliability check tutorial](/tutorials/klusterai-api/reliability-check/){target=\_blank} with code examples.