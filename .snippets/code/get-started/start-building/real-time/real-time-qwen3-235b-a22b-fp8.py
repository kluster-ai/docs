# Real-time completions with the Qwen3-235B-A22B model on Kluster.
import os
import getpass
import kluster
from typing import Dict, Any

# 1. Initialize the Kluster SDK client
# Get API key securely using getpass (will not be displayed or saved)
api_key = os.environ.get("API_KEY") or getpass.getpass("Enter your Kluster API key: ")
client = kluster.Client(api_key=api_key)

# 2. Example inputs
messages = [
    {"role": "user", "content": "Write a poem about artificial intelligence."}
]

# 3. Generate completion
response = client.real_time.completions.create(
    model="Qwen/Qwen3-235B-A22B-FP8",
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
