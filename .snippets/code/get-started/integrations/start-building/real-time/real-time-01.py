from openai import OpenAI
import json
import os


client = OpenAI(
    api_key="INSERT_API_KEY",
    base_url="https://api.kluster.ai/v1"
)

# Create chat completion request
completion = client.chat.completions.create(
    model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[
        {"role": "user", "content": "What's the name of the most famous street in Paris?"}
    ]
)

def log_response_to_file(response, filename="response_log.json"):
    """Logs the full AI response to a JSON file in the same directory as the script."""

# Convert response to dictionary
response_data = response.dict()

# Get the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

# Write to JSON file
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(response_data, json_file, ensure_ascii=False, indent=4)
    print(f"Response logged to {file_path}")

# Log response to file
log_response_to_file(completion)