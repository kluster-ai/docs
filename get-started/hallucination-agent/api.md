---
title: Hallucination Detection with the API
description: Learn how to programmatically detect and prevent AI hallucinations in your applications by integrating kluster.ai's hallucination detection through the API.
---

# Hallucination Detection with the API

The kluster.ai API allows you to detect hallucinations in AI-generated content by comparing responses against provided context. This guide provides a practical overview of using the hallucination detection endpoint, including input parameters and interpreting the results.

## Prerequisites

Before getting started with the Hallucination Agent, ensure you have the following:

- **kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you do not have one
- **kluster.ai API key** - after signing in, go to the [API Keys](https://platform.kluster.ai/apikeys){target=_blank} section and create a new key. For detailed instructions, see the [Get an API key](https://docs.kluster.ai/get-started/get-api-key/){target=_blank} guide

## API endpoint

The hallucination detection service is accessible through the following endpoint:

```
https://api.kluster.ai/v1/judges/detect-hallucination
```

## Using the hallucination detection API

### Request parameters

The API accepts the following parameters:

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | string | Yes | The original question or instruction given to the AI |
| `output` | string | Yes | The AI-generated response to evaluate |
| `context` | string | Yes | The factual context against which to compare the output |
| `return_search_results` | boolean | No | Whether to include search results in the response (default: false) |

### Example request

```bash
curl --location 'https://api.kluster.ai/v1/judges/detect-hallucination' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data '{
    "prompt": "the eiffel tower is in paris?",
    "output": "yes, paris ",
    "context": "News Bulletin: Paris is struggling with a massive fire since 7am CET time",
    "return_search_results": true
}'
```

### Response format

The API returns a JSON object with the following structure:

```json
{
    "is_hallucination": false,
    "usage": {
        "completion_tokens": 173,
        "prompt_tokens": 1122,
        "total_tokens": 1295
    },
    "explanation": "The question asks if the Eiffel Tower is in Paris.\nThe provided document does not mention the Eiffel Tower or its location.\nThe answer 'yes, paris' confirms the Eiffel Tower is in Paris but does not provide any factual basis or reference from the document.\nThe general knowledge that the Eiffel Tower is in Paris is correct, but the answer does not use information from the provided document.\nThe response does not introduce false information, but it also does not use the provided document to support the claim.",
    "search_results": []
}
```

### Response fields

| Field | Type | Description |
| --- | --- | --- |
| `is_hallucination` | boolean | Whether the output contains hallucinated content not supported by the context |
| `usage` | object | Token usage information for billing purposes |
| `explanation` | string | Detailed reasoning for the hallucination determination |
| `search_results` | array | Optional search results when `return_search_results` is true |

## Integration examples

### Python example

```python
import requests
import json

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.kluster.ai/v1/judges/detect-hallucination"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "prompt": "What are the health benefits of apples?",
    "output": "Apples contain compounds that can help fight cancer, lower cholesterol, and improve gut health.",
    "context": "Research shows apples are high in fiber and vitamin C. They may help lower cholesterol levels and improve digestion.",
    "return_search_results": True
}

response = requests.post(API_URL, headers=headers, data=json.dumps(data))
result = response.json()

if result["is_hallucination"]:
    print("Hallucination detected!")
    print("Explanation:", result["explanation"])
else:
    print("Content is factually supported by context.")
    print("Explanation:", result["explanation"])
```

### Node.js example

```javascript
const axios = require('axios');

const API_KEY = 'YOUR_API_KEY';
const API_URL = 'https://api.kluster.ai/v1/judges/detect-hallucination';

const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Bearer ${API_KEY}`
};

const data = {
  prompt: 'What are the health benefits of apples?',
  output: 'Apples contain compounds that can help fight cancer, lower cholesterol, and improve gut health.',
  context: 'Research shows apples are high in fiber and vitamin C. They may help lower cholesterol levels and improve digestion.',
  return_search_results: true
};

axios.post(API_URL, data, { headers })
  .then(response => {
    const result = response.data;
    if (result.is_hallucination) {
      console.log('Hallucination detected!');
      console.log('Explanation:', result.explanation);
    } else {
      console.log('Content is factually supported by context.');
      console.log('Explanation:', result.explanation);
    }
  })
  .catch(error => {
    console.error('Error:', error.response?.data || error.message);
  });
```

## Use cases

### Content moderation

Implement hallucination detection as part of a content moderation pipeline to ensure AI-generated content remains factual and accurate before being presented to users.

```python
def moderate_ai_content(prompt, ai_response, context_documents):
    # Check for hallucinations
    hallucination_check = check_for_hallucinations(prompt, ai_response, context_documents)
    
    if hallucination_check["is_hallucination"]:
        # Content contains hallucinations - reject or flag for review
        return {
            "status": "rejected",
            "reason": hallucination_check["explanation"],
            "original_response": ai_response
        }
    else:
        # Content is factually consistent - approve
        return {
            "status": "approved",
            "content": ai_response
        }
```

### Educational applications

Ensure educational content remains factually accurate by validating AI-generated explanations against trusted academic sources.

```python
def generate_educational_content(topic, academic_sources):
    # Generate initial explanation
    ai_explanation = generate_ai_explanation(topic)
    
    # Validate against academic sources
    validation = validate_against_sources(topic, ai_explanation, academic_sources)
    
    if validation["is_hallucination"]:
        # Regenerate with more constraints or human review
        return handle_inaccurate_content(topic, validation["explanation"])
    else:
        # Content is academically sound
        return ai_explanation
```

### Legal compliance

Ensure AI-generated legal advice or documentation remains strictly within the bounds of provided legal texts and precedents.

```python
def generate_legal_guidance(query, legal_references):
    # Generate initial legal guidance
    initial_guidance = generate_ai_legal_response(query)
    
    # Verify against legal references
    verification = verify_legal_accuracy(query, initial_guidance, legal_references)
    
    if verification["is_hallucination"]:
        # Legal guidance contains unsupported claims
        return {
            "status": "requires_review",
            "guidance": initial_guidance,
            "issues": verification["explanation"]
        }
    else:
        # Guidance is supported by legal references
        return {
            "status": "verified",
            "guidance": initial_guidance
        }
```

## Best practices

When using the Hallucination Agent, follow these best practices for optimal results:

1. **Provide comprehensive context** - Include all relevant context to ensure accurate evaluation
2. **Be specific with prompts** - Clearly specify what you're asking to help the agent understand what to evaluate
3. **Check edge cases** - Test with various types of factual and hallucinated content to understand detection capabilities
4. **Monitor token usage** - Keep track of token consumption for cost management
5. **Implement circuit breakers** - Add fallback mechanisms when hallucinations are detected

## Next steps

- **API reference** - Review the complete [API documentation](/api-reference/reference/){target=_blank} for detailed endpoint specifications
- **Explore models** - See the [Models](/get-started/models/){target=_blank} page to learn about our AI models
