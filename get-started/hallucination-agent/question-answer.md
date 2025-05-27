---
title: Question/Answer Hallucination Detection
description: Learn how to use the kluster.ai Hallucination Detection API to validate the truthfulness of answers to questions.
---

# Question/Answer Hallucination Detection

The Question/Answer hallucination detection endpoint allows you to validate whether an answer to a specific question contains hallucinated information. This approach is ideal for fact-checking individual responses against provided context or general knowledge.

## How it works

The service evaluates the truthfulness of an answer to a question by:

1. Analyzing the original question or prompt
2. Examining the provided answer
3. Comparing the answer against the provided context (if supplied)
4. Determining if the answer contains hallucinated or unsupported information
5. Providing a detailed explanation of the reasoning behind the determination

## API endpoint

```
https://api.kluster.ai/v1/judges/detect-hallucination
```

## Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | string | Yes | The question asked or instruction given |
| `output` | string | Yes | The answer to verify for hallucinations |
| `context` | string | No | Optional reference material to validate against |
| `return_search_results` | boolean | No | Whether to include search results (default: false) |

## Response format

The API returns a JSON object with the following structure:

```json
{
    "is_hallucination": boolean,
    "usage": {
        "completion_tokens": number,
        "prompt_tokens": number,
        "total_tokens": number
    },
    "explanation": "string",
    "search_results": []  // Only included if return_search_results is true
}
```

## Example 1: Basic verification

This example checks whether an answer about the Earth's shape contains hallucinated information.

### Request

```bash
curl --location 'https://api.kluster.ai/v1/judges/detect-hallucination' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data '{
    "prompt": "Is earth flat?",
    "output": "Yes, my friend",
    "context": "Scientific discussion",
    "return_search_results": false
}'
```

### Response

```json
{
    "is_hallucination": true,
    "usage": {
        "completion_tokens": 165,
        "prompt_tokens": 1034,
        "total_tokens": 1199
    },
    "explanation": "The question asks if the Earth is flat. The provided answer 'Yes, my friend' affirms that the Earth is flat. However, this contradicts well-established scientific knowledge. The Earth has been proven to be approximately spherical through multiple lines of evidence including satellite imagery, circumnavigation, observation of ships disappearing hull-first over the horizon, and the curved shadow of the Earth during lunar eclipses. The answer provided is scientifically inaccurate and constitutes a hallucination."
}
```

## Example 2: Verifying against specific context

This example checks whether an answer about the Eiffel Tower's location is supported by the provided context.

### Request

```bash
curl --location 'https://api.kluster.ai/v1/judges/detect-hallucination' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data '{
    "prompt": "the eiffel tower is in paris?",
    "output": "yes, paris",
    "context": "News Bulletin: Paris is struggling with a massive fire since 7am CET time",
    "return_search_results": true
}'
```

### Response

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

## Python implementation

```python
import requests
import json

def check_hallucination(question, answer, context=None, return_search_results=False):
    """
    Verify if an answer to a question contains hallucinated information.
    
    Args:
        question: The question or prompt.
        answer: The answer to verify.
        context: Optional reference material for verification.
        return_search_results: Whether to include search results in the response.
        
    Returns:
        Dictionary with verification results.
    """
    API_KEY = "YOUR_API_KEY"
    API_URL = "https://api.kluster.ai/v1/judges/detect-hallucination"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "prompt": question,
        "output": answer
    }
    
    # Add optional parameters if provided
    if context:
        data["context"] = context
        
    if return_search_results:
        data["return_search_results"] = return_search_results
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        result = response.json()
        return result
    except Exception as e:
        return {
            "error": f"Verification failed: {str(e)}",
            "is_hallucination": None
        }

# Example usage
result = check_hallucination(
    question="Is Mount Everest the tallest mountain in the world?",
    answer="Yes, Mount Everest is the tallest mountain in the world, with a height of 8,849 meters above sea level.",
    context="Mount Everest, located in the Mahalangur Himal sub-range of the Himalayas, is Earth's highest mountain above sea level, with an elevation of 8,848.86 meters (29,031.7 ft)."
)

if result.get("is_hallucination") is not None:
    if result["is_hallucination"]:
        print("⚠️ Hallucination detected!")
        print(f"Explanation: {result['explanation']}")
    else:
        print("✅ Answer is factually supported.")
        print(f"Explanation: {result['explanation']}")
else:
    print(f"Error: {result.get('error')}")
```

## Best practices

1. **Provide specific questions** - Clearly defined questions yield more accurate hallucination detection
2. **Include relevant context** - When validating against specific information, provide comprehensive context
3. **Use domain-specific context** - Include authoritative references for specialized knowledge domains
4. **Consider general knowledge** - For common facts, the service can verify against general knowledge
5. **Review explanations** - The detailed explanations provide valuable insights into the reasoning process

## Next steps

- Learn how to use [Chat Completion Hallucination Detection](/get-started/hallucination-agent/chat-completion/){target=_self} for evaluating entire conversation histories
- Explore [Examples](/get-started/hallucination-agent/examples/){target=_self} of hallucination detection in real-world scenarios
- Review the complete [API documentation](/api-reference/reference/){target=_blank} for detailed endpoint specifications
