from openai import OpenAI
from getpass import getpass

# Get API key from user input
api_key = getpass("Enter your kluster.ai API key: ")

# Initialize OpenAI client pointing to kluster.ai API
client = OpenAI(
    api_key=api_key,
    base_url="https://api.kluster.ai/v1"
)

# Create chat completion request
completion = client.chat.completions.create(
    model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    messages=[
        {"role": "user", "content": "What is the ultimate breakfast sandwich?"}
    ]
)

"""Logs the full AI response to terminal."""

# Extract model name and AI-generated text
model_name = completion.model  
text_response = completion.choices[0].message.content  

# Print response to console
print(f"\n🔍 AI response (model: {model_name}):")
print(text_response)