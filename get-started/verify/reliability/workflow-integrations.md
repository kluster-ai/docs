---
title: Workflow Integrations
description: Download and use pre-built workflows for kluster verify in Dify, n8n, and other platforms using direct API integration.
---

# Workflow Integrations

Integrate kluster verify's reliability checking into your favorite automation platforms with our ready-to-use workflow templates. These pre-configured workflows connect directly to the kluster.ai API, allowing you to add AI verification capabilities to your existing processes in minutes.

## Prerequisites

Before getting started, you'll need:

- **kluster.ai account** - Sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you don't have one
- **API key** - After signing in, navigate to [API Keys](https://platform.kluster.ai/apikeys){target=_blank} and create a new key
- **Workflow platform** - Dify, n8n, or your preferred automation tool

## Available Workflows

### Dify

Build AI applications that fact-check themselves. This workflow seamlessly integrates kluster verify into your Dify chatbots and agents, ensuring every response is validated for accuracy before reaching your users.

![Dify workflow for kluster verify](/images/get-started/verify/dify_workflow.webp)

**Configure kluster.ai as a Model Provider** 

- Navigate to **Settings** and select **Model Provider**
- Click on **Add Provider** and choose **OpenAI-API-compatible**

Enter these settings:

- **Base URL**: `https://api.kluster.ai/v1`
- **API Key**: Your kluster.ai API key
- **Model**: Select from [available models](https://platform.kluster.ai/models){target=_blank}

Save and test the connection to ensure it works properly.

**Set up the kluster verify node:**
- Select the HTTP Request node `kluster verify`
- Add your API key to the Authorization header.

**Import and Configure the Workflow** 

- Download the workflow template below and import it into your Dify workspace. The workflow comes pre-configured to verify AI responses in real-time. Test it with sample queries to ensure everything is functioning correctly.

[Download Dify Workflow](workflows/dify_workflow.yml){target=_blank .md-button}

### n8n

Add verification checkpoints to your n8n automation pipelines. This workflow validates AI-generated content against your source documents, tools, or real-time data, perfect for ensuring accuracy in automated content generation and data processing workflows.

![n8n workflow for kluster verify](/images/get-started/verify/n8n_workflow.webp)

**Set Up API Credentials**

- Select the OpenAI and choose **Credentials**, click **Create New**,

- **Name**: kluster.ai Verify
- **Header Name**: `Authorization`
- **Header Value**: `Bearer YOUR_API_KEY`

Save the credential for use in your workflows.

**Import and Configure the Workflow** - Download the workflow template below and import it via the n8n interface. The workflow includes pre-configured HTTP nodes that connect to the `/v1/verify/reliability` endpoint, handle request/response formatting, and parse verification results. Connect your data sources and configure output routing as needed.

[Download n8n Workflow](workflows/n8n_workflow.json){target=_blank .md-button}

## How It Works

All workflows connect to kluster verify through a simple API call. Here's what happens under the hood:

**Request Format:**
```json
{
  "prompt": "What was the user's question?",
  "output": "The AI's response to verify", 
  "context": "Optional reference documents or data",
  "return_search_results": false
}
```

**Response Format:**
```json
{
  "is_hallucination": false,
  "explanation": "The response accurately reflects the information...",
  "usage": {"total_tokens": 150}
}
```

The service analyzes the AI output against the provided context (or performs real-time fact-checking) and returns a clear verdict with detailed reasoning.

## Next Steps

Ready to build more reliable AI applications?

- **Explore the API** - Check our [complete API reference](/api-reference/reference/){target=_blank} for advanced configuration options
- **Learn verification methods** - Dive into [question/answer verification](/get-started/verify/reliability/question-answer/){target=_self} for detailed implementation patterns
- **Try the tutorial** - Follow our [hands-on reliability check tutorial](/tutorials/klusterai-api/reliability-check/){target=_blank} with code examples