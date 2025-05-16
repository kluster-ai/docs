# Real-time completions with the Gemma 3 27B model on Kluster.
import os
import kluster
from typing import Dict, Any

# 1. Initialize the Kluster SDK client
#    Your API key can also be specified via KLUSTER_API_KEY environment variable
client = kluster.Client(api_key="YOUR_API_KEY")

# 2. Example inputs
messages = [
    {"role": "user", "content": "What is the capital of France?"}
]

# 3. Generate completion
response = client.real_time.completions.create(
    model="google/gemma-3-27b-it",
    messages=messages,
    max_tokens=100,
)

# 4. Process response
print("Model:", response.model)
print("Completion:", response.choices[0].message.content)
print("Finish reason:", response.choices[0].finish_reason)
print("Prompt tokens:", response.usage.prompt_tokens)
print("Completion tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)

# 5. Example with image input
image_url = "https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

vision_messages = [
    {
        "role": "user", 
        "content": [
            {"type": "text", "text": "Describe what you see in this image."},
            {"type": "image_url", "image_url": {"url": image_url}}
        ]
    }
]

vision_response = client.real_time.completions.create(
    model="google/gemma-3-27b-it",
    messages=vision_messages,
    max_tokens=300,
)

print("\nVision Completion:", vision_response.choices[0].message.content)
