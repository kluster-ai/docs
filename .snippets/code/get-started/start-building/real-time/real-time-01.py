import json
import os
from getpass import getpass

from openai import OpenAI

# Get API key from user input
api_key = os.environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")

# Initialize OpenAI client pointing to kluster.ai API
client = OpenAI(
    api_key=api_key,
    base_url="https://api.kluster.ai/v1"
)

print(f"📤 Sending a chat completion request to kluster.ai...\n")

# Create chat completion request
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {"role": "user", "content": "What is the ultimate breakfast sandwich?"}
    ]
)

def log_response_to_file(response, filename="response_log.json"):
    """Logs the full AI response to a JSON file in the same directory as the script."""

    # Extract model name and AI-generated text
    model_name = response.model  
    text_response = response.choices[0].message.content  

    # Print response to console
    print(f"\n🔍 AI response (model: {model_name}):")
    print(text_response)

    # Convert response to dictionary
    response_data = response.model_dump()

    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    # Write to JSON file
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(response_data, json_file, ensure_ascii=False, indent=4)
        print(f"💾 Response saved to {file_path}")

# Log response to file
log_response_to_file(completion)
