# Real-time completions with the DeepSeek-V3-0324 model on Kluster.
import os
import getpass
from openai import OpenAI

# 1. Initialize OpenAI client pointing to kluster.ai API
# Get API key securely using getpass (will not be displayed or saved)
api_key = os.environ.get("API_KEY") or getpass.getpass("Enter your Kluster API key: ")
client = OpenAI(
    api_key=api_key,
    base_url="https://api.kluster.ai/v1"
)

# 2. Example inputs
messages = [
    {"role": "user", "content": "Write a poem about artificial intelligence."}
]

# 3. Generate completion
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
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
