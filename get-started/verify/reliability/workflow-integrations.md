---
title: Workflow Integrations
description: Easily integrate Verify into Dify, n8n, and more with ready-made workflows to automate AI response validation via API in minutes.
---

# Workflow integrations

You can integrate the Verify reliability check feature into your favorite automation platforms with ready-to-use workflow templates. These pre-configured integrations connect directly to the kluster.ai API, allowing you to add AI verification capabilities to your existing processes in minutes.

## Prerequisites

Before getting started with the workflow integrations, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'

## Choose your platform

### Dify

By leveraging kluster.ai with [Dify](https://dify.ai/){target=\_blank}, you can enhance the reliability of your AI chatbots and agents. This workflow specifically integrates kluster.ai's verification into your Dify responses, validating them before they reach your users.

![Dify workflow for kluster verify](/images/get-started/verify/dify_workflow.webp)

**Configure kluster.ai as a Model Provider** 

1. Navigate to **Settings** and select **Model Provider**.
2. Click on **Add Provider** and choose **OpenAI-API-compatible**.

Enter these settings:

- **Base URL**: `https://api.kluster.ai/v1`.
- **API Key**: Your kluster.ai API key.
- **Model**: Select from [available models](https://platform.kluster.ai/models){target=\_blank}.

Save and test the connection to ensure it works properly.

----- ERIN'S EDIT -----
Note: The above steps weren't 1:1. So, this is what I tried to do, but it didn't work. Halllpppp.

1. Navigate to **Settings** → **Model Provider**.
2. From **Install model providers**, install **OpenAI**
3. Once installed, OpenAI will appear in the **Models** section. From there, select **Add Model**
4. Enter the following details:
    - **Model Type**: **LLM**.
    - **Model Name**: Enter the name of the model you're using. Select from [available models](https://platform.kluster.ai/models){target=\_blank}. 
    - **API Key**: Enter your kluster.ai API key.
    - **API Base**: `https://api.kluster.ai/v1`.
5. Click **Save** and test the connection to ensure it is working properly.

Haha, it did not work. So... 
----- END -----

**Set up the kluster verify node:**

1. Select the HTTP Request node `kluster verify`.
2. Add your API key to the Authorization header.

**Import and Configure the Workflow** 

Download the workflow template below and import it into your Dify workspace. 

The workflow comes pre-configured to verify AI responses in real-time.

[Download Dify Workflow](workflows/dify_workflow.yml){target=\_blank .md-button}

---- ERIN's EDIT -----
Next, you can set up the Verfiy node in your Dify workflow:

1. Download the pre-configured Dify workflow template: [dify_workflow.yml](workflows/dify_workflow.yml)
2. Import the downloaded workflow template into your Dify workspace. This template is designed to verify AI responses in real-time.
3. Within the imported workflow, find the HTTP request node named **kluster verify**.
4. Add your kluster.ai API key to the Authorization header.

Note: I modified the above steps because it seemed like you needed to download the workflow first.
But I couldn't try it, so I don't really know.
----- END -----

### n8n

This section outlines how to add verification checkpoints to your [n8n](https://n8n.io/){target=\_blank} automation pipelines using kluster.ai, ensuring the accuracy of AI-generated content against your specified sources.

![n8n workflow for kluster verify](/images/get-started/verify/n8n_workflow.webp)

**Set Up API Credentials**

- Select the OpenAI and choose **Credentials**. Then click **Create New**.

- **Base URL**: `https://api.kluster.ai/v1`.
- **API key**: Your kluster.ai API key.
- **Model**: Select from [available models](https://platform.kluster.ai/models){target=\_blank}.

**Set up the kluster verify node API key:**

Open the kluster verify node and modify the headers as follow:

- **Header name**: `Authorization`
- **Header value**: `Bearer YOUR_API_KEY`


**Import and Configure the Workflow** 

Download the workflow template below and import it via the n8n interface. 

The workflow includes pre-configured HTTP nodes that connect to the `/v1/verify/reliability` endpoint, handle request/response formatting, and parse verification results. Connect your data sources and configure output routing as needed.

[Download n8n Workflow](workflows/n8n_workflow.json){target=\_blank .md-button}

## Next Steps

Ready to build more reliable AI applications?

- **Explore the API**: Check the [complete API reference](/api-reference/reference/#/http/api-endpoints/realtime/v1-verify-reliability-post){target=\_blank} for advanced configuration options.
- **Learn verification methods**: Dive into the [Verify API endpoint](/get-started/verify/reliability/verify-api/){target=\_blank} for detailed implementation patterns.
- **Try the tutorial**: Follow the [hands-on reliability check tutorial](/tutorials/klusterai-api/reliability-check/){target=\_blank} with code examples.