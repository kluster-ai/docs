from openai import OpenAI
from getpass import getpass
import json
import os

# Get API key from user input
api_key = getpass("Enter your kluster.ai API key: ")

# Initialize OpenAI client pointing to kluster.ai API
client = OpenAI(
    api_key=api_key,
    base_url="https://api.kluster.ai/v1"
)

# Create chat completion request
completion = client.chat.completions.create(
    model="klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {"role": "user", "content": "What is the ultimate breakfast sandwich?"}
    ]
)

def log_response_to_file(response):
    """Logs the full AI response to a JSON file in the same directory as the script."""

    # Extract model name and AI-generated text
    model_name = response.model  
    text_response = response.choices[0].message.content  

    # Print response to console
    print(f"\n🔍 AI response (model: {model_name}):")
    print(text_response)

# Log response to file
log_response(completion)