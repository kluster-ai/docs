# Real-time completions with the Gemma 3 27B model on kluster.ai

from openai import OpenAI
from getpass import getpass

image_url = "https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

# Get API key from user input
api_key = getpass("Enter your kluster.ai API key: ")

# Initialize OpenAI client pointing to kluster.ai API
client = OpenAI(api_key=api_key, base_url="https://api.kluster.ai/v1")

# Create chat completion request
completion = client.chat.completions.create(
    model="google/gemma-3-27b-it",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Who can park in the area?"},
                {"type": "image_url", "image_url": {"url": image_url}},
            ],
        }
    ],
)

print(f"\nImage URL: {image_url}")

"""Logs the full AI response to terminal."""

# Extract model name and AI-generated text
model_name = completion.model
text_response = completion.choices[0].message.content

# Print response to console
print(f"\n🔍 AI response (model: {model_name}):")
print(text_response)
