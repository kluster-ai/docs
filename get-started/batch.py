import json
from openai import OpenAI

client = OpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key="4532c187-d275-4a6b-940c-5d92f9b20ea6",  # Replace with your actual API key
)

requests = [
    {
        "custom_id": "request-1",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital of Argentina?"},
            ],
            "max_completion_tokens": 1000,
        },
    },
    {
        "custom_id": "request-2",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
            "messages": [
                {"role": "system", "content": "You are a maths tutor."},
                {"role": "user", "content": "Explain the Pythagorean theorem."},
            ],
            "max_completion_tokens": 1000,
        },
    },
    {
        "custom_id": "request-4",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a multilingual, experienced maths tutor.",
                },
                {
                    "role": "user",
                    "content": "Explain the Pythagorean theorem in Spanish",
                },
            ],
            "max_completion_tokens": 1000,
        },
    },
    # Additional tasks can be added here
]

# Save tasks to a JSONL file (newline-delimited JSON)
file_name = "mybatchtest.jsonl"
with open(file_name, "w") as file:
    for request in requests:
        file.write(json.dumps(request) + "\n")
