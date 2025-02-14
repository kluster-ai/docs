import os

from litellm import completion

# Set environment vars, shown in script for readability
os.environ["OPENAI_API_KEY"] = "INSERT_KLUSTER_API_KEY"
os.environ["OPENAI_API_BASE"] = "https://api.kluster.ai/v1"

# Basic Chat
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user",   "content": "What is the capital of California?"}
]

# Use an "openai/..." model prefix so LiteLLM treats this as an OpenAI-like call
model = "openai/klusterai/Meta-Llama-3.3-70B-Instruct-Turbo"

response = completion(
    model=model,
    messages=messages,
    max_tokens=1000, 
)

print(response)
