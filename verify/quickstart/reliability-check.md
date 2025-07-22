---
title: Reliability check quick start
description: Get started with kluster.ai's reliability check in under 5 minutes. Detect hallucinations and validate AI responses with a simple API call.
---

# Reliability check quick start

AI models can generate convincing but factually incorrect responses, known as hallucinations. Traditional approaches to validation often require manual review or complex rule-based systems that are time-consuming and difficult to scale.

The [kluster.ai](https://www.kluster.ai/){target=\_blank} reliability check service addresses these challenges by providing real-time validation of AI-generated responses. It automatically detects hallucinations and ensures accuracy by analyzing the original prompt and the AI's response to determine if the output contains unreliable or fabricated information.

This guide will walk you through setting up the reliability check service, demonstrate a quick example, and show you the different integration options available.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'

## Integration options

You can use the reliability check service through three methods:

- **[Verify API](/verify/reliability-check/verify-api/)** - direct REST API endpoint for maximum control.
- **[Chat completion](/verify/reliability-check/chat-completion/)** - OpenAI-compatible endpoint using the `klusterai/verify-reliability` model.
- **[MCP integration](/verify/mcp/get-started/)** - connect to Cursor or other AI assistants for interactive verification.

## Quick example

Here's the simplest way to check if an AI response contains hallucinations:

```python
from os import environ
import requests
from getpass import getpass

# Get API key securely
api_key = environ.get("INSERT_API_KEY") or getpass("Enter your kluster.ai API key: ")

# Check if a response is reliable
response = requests.post(
    "https://api.kluster.ai/v1/verify/reliability",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "prompt": "What is the capital of France?",
        "output": "The capital of France is London."
    }
)

result = response.json()
print(f"Hallucination detected: {result['is_hallucination']}")
print(f"Explanation: {result['explanation']}")
```

## Response format

The API returns:

```json
{
    "is_hallucination": true,
    "explanation": "The response incorrectly states that London is the capital of France. The capital of France is Paris, not London.",
    "usage": {
        "completion_tokens": 42,
        "prompt_tokens": 28,
        "total_tokens": 70
    }
}
```

## Next steps

- Add [context validation](/verify/reliability-check/verify-api/#context-validation-mode) for RAG applications.
- Use [chat completion format](/verify/reliability-check/chat-completion/) for conversation history.
- Enable [MCP](/verify/mcp/get-started/) for Claude desktop integration.
- Explore [workflow integrations](/verify/reliability-check/workflow-integrations/) for Dify and n8n.