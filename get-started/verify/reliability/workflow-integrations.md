---
title: Workflow Integrations
description: Download and use pre-built workflows for kluster verify in Dify, n8n, and other platforms using direct API integration.
---

# Workflow Integrations

Ready-to-use workflow templates that integrate kluster verify's reliability checking directly into your automation platforms using HTTP API calls.

## Prerequisites

Before using these workflows, ensure you have:

- **kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you don't have one
- **kluster.ai API key** - after signing in, go to the [API Keys](https://platform.kluster.ai/apikeys){target=_blank} section and create a new key
- **Target platform** - Dify, n8n, or other workflow automation tool

## Clients

### Dify

**Fact-Check Assistant** - Real-time verification of AI claims
Pre-built Dify workflows that add reliability checking to your AI applications.

<!-- TODO: Add screenshot -->

**Setup kluster.ai Provider:**

1. Navigate to **Settings** → **Model Provider**
2. Click **Add Provider** → **Custom Provider**
3. Configure kluster.ai:
   - **Name**: kluster.ai
   - **Base URL**: `https://api.kluster.ai/v1`
   - **API Key**: Your kluster.ai API key
4. Save and test connection

**Workflow Setup:**

1. Download the workflow JSON file
2. Import into your Dify workspace
3. Configure your kluster.ai API key in the HTTP node
4. Test with sample data

[Download Dify Workflows](#){target=_blank .md-button}

### n8n

**RAG Reliability Check** - Validates AI responses against document context or tools 

Automation workflows for n8n that integrate reliability checking into your data pipelines.

<!-- TODO: Add screenshot -->

**Setup kluster.ai Provider:**

1. In n8n, add a new **HTTP Request** node
2. Configure authentication:
   - **Authentication**: Header Auth
   - **Header Name**: `Authorization`
   - **Header Value**: `Bearer YOUR_API_KEY`
3. Set default request options:
   - **URL**: `https://api.kluster.ai/v1/verify/reliability`
   - **Method**: POST
   - **Content Type**: JSON
4. Save as credential for reuse

**Workflow Setup:**

1. Download the n8n workflow JSON
2. Import via n8n interface
3. Set your kluster.ai API credentials
4. Configure input/output nodes as needed

[Download n8n Workflows](#){target=_blank .md-button}

## API Integration

All workflows use the `/v1/verify/reliability` endpoint with standard HTTP requests:

```json
{
  "prompt": "Your question or context",
  "output": "AI response to verify", 
  "context": "Optional reference material",
  "return_search_results": false
}
```

**Response:**
```json
{
  "is_hallucination": false,
  "explanation": "Detailed reasoning...",
  "usage": {"total_tokens": 150}
}
```

## Next Steps

- Review [API documentation](/api-reference/reference/){target=_blank} for advanced parameters
- Explore [Question/Answer verification](/get-started/verify/reliability/question-answer/){target=_self} for implementation details