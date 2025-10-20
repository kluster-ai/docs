from getpass import getpass
from os import environ

from openai import OpenAI

# Get API key from user input
api_key = environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")

print(f"📤 Sending a Reliability request to kluster.ai...\n")

# Initialize OpenAI client pointing to kluster.ai API
client = OpenAI(
    api_key=api_key,
    base_url="https://api.kluster.ai/v1"
)

# Create chat completion request
completion = client.chat.completions.create(
    model="klusterai/verify-reliability", # Note special model
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
)

# Extract the reliability verification response
text_response = completion.choices[0].message.content  

# Print response to console
print(text_response)
