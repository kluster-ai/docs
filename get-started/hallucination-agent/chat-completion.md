---
title: Chat Completion Hallucination Detection
description: Learn how to use the kluster.ai Hallucination Detection API to validate responses in full chat conversations.
---

# Chat Completion Hallucination Detection

The Chat Completion hallucination detection endpoint allows you to validate responses in full conversation histories using the same format as the standard chat completions API. This approach enables detection of hallucinations within the complete context of a conversation.

## How it works

The service evaluates the truthfulness of responses within a conversation by:

1. Analyzing the entire conversation history, including system instructions
2. Examining the assistant's responses within context
3. Determining if the responses contain hallucinated or unsupported information
4. Providing a detailed explanation of the reasoning behind the determination



## API endpoint

```
https://api.kluster.ai/v1/judges/detect-hallucination
```

## Request parameters

The endpoint accepts the same format as the standard chat completions API:

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `model` | string | Yes | The model to use for hallucination detection |
| `messages` | array | Yes | Array of message objects in the conversation history |
| `max_tokens` | integer | No | The maximum number of tokens for the response |
| `temperature` | number | No | Sampling temperature (0.0 to 2.0) |
| `top_p` | number | No | Nucleus sampling parameter (0.0 to 1.0) |
| `stream` | boolean | No | Whether to stream the response (must be false) |

### Message format

Each message in the `messages` array must have the following structure:

```json
{
  "role": "system"|"user"|"assistant",
  "content": "string"
}
```

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
    "explanation": "string"
}
```

## Example: Verifying scientific claims

This example checks whether an assistant's claim about ghosts has scientific support.

### Request

```bash
curl --location 'https://api.kluster.ai/v1/judges/detect-hallucination' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--data '{
    "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are smart assistant which answer questions with full honestly and with scientific accuracy"
      },
      {
        "role": "user",
        "content": "Are ghosts real??"
      },
      {
        "role": "assistant",
        "content": "Yes. There is recent scientific study which confirms this"
      }
    ],
    "max_tokens": 3600,
    "temperature": 0.6,
    "top_p": 0.5,
    "stream": false
}'
```

### Response

```json
{
    "is_hallucination": true,
    "usage": {
        "completion_tokens": 187,
        "prompt_tokens": 1248,
        "total_tokens": 1435
    },
    "explanation": "The assistant's response contains a significant hallucination. The assistant claims 'There is recent scientific study which confirms this' regarding the existence of ghosts. This is false as there are no credible, peer-reviewed scientific studies confirming the existence of ghosts. The scientific consensus does not support the existence of ghosts, and the assistant's claim of a recent scientific study confirming their existence contradicts the system's instruction to 'answer questions with full honestly and with scientific accuracy.' The response presents speculation or falsehood as established scientific fact."
}
```

## Python implementation

```python
import requests
import json

def check_conversation_hallucination(messages, model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo", max_tokens=3600):
    """
    Verify if a conversation contains hallucinated information.
    
    Args:
        messages: Array of message objects (system, user, assistant).
        model: The model to use for hallucination detection.
        max_tokens: Maximum number of tokens for the response.
        
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
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.6,
        "top_p": 0.5,
        "stream": False
    }
    
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
messages = [
    {
        "role": "system",
        "content": "You are a knowledgeable assistant that provides accurate medical information."
    },
    {
        "role": "user",
        "content": "Does vitamin C cure the common cold?"
    },
    {
        "role": "assistant",
        "content": "Yes, taking large doses of vitamin C has been scientifically proven to cure the common cold within 24 hours."
    }
]

result = check_conversation_hallucination(messages)

if result.get("is_hallucination") is not None:
    if result["is_hallucination"]:
        print("⚠️ Hallucination detected in conversation!")
        print(f"Explanation: {result['explanation']}")
    else:
        print("✅ Conversation is factually supported.")
        print(f"Explanation: {result['explanation']}")
else:
    print(f"Error: {result.get('error')}")
```

## Use cases

### Scientific fact-checking

Verify that AI responses about scientific topics adhere to established scientific consensus and don't make unfounded claims.

```python
scientific_messages = [
    {
        "role": "system",
        "content": "You are a scientific advisor providing accurate information based on peer-reviewed research."
    },
    {
        "role": "user",
        "content": "Is there scientific evidence that drinking alkaline water prevents cancer?"
    },
    {
        "role": "assistant",
        "content": "Response to verify for hallucinations..."
    }
]
```

### Medical information validation

Ensure that health-related AI responses don't contain potentially harmful misinformation.

```python
medical_messages = [
    {
        "role": "system",
        "content": "You provide general health information based on medical consensus, always noting when evidence is limited."
    },
    {
        "role": "user",
        "content": "What treatments are effective for COVID-19?"
    },
    {
        "role": "assistant",
        "content": "Response to verify for hallucinations..."
    }
]
```

### Educational content quality control

Validate educational content for accuracy before presenting it to students.

```python
educational_messages = [
    {
        "role": "system",
        "content": "You are a history tutor providing factual information about historical events."
    },
    {
        "role": "user",
        "content": "What were the main causes of World War I?"
    },
    {
        "role": "assistant",
        "content": "Response to verify for hallucinations..."
    }
]
```

## Best practices

1. **Include clear system instructions** - The system message sets expectations for factual accuracy
2. **Provide complete conversation context** - Include all relevant messages for proper evaluation
3. **Test with different response variants** - Compare detection results across different formulations
4. **Analyze explanations** - The detailed explanations highlight specific problematic claims
5. **Implement human review** - For critical applications, combine automated detection with human oversight

## Next steps

- Learn how to use [Question/Answer Hallucination Detection](/get-started/hallucination-agent/question-answer/){target=_self} for simpler verification scenarios
- Explore [Examples](/get-started/hallucination-agent/examples/){target=_self} of hallucination detection in real-world scenarios
- Review the complete [API documentation](/api-reference/reference/){target=_blank} for detailed endpoint specifications
