from openai import OpenAI
from getpass import getpass
import json
import time

# Get API key from user input
api_key = getpass("Enter your kluster.ai API key: ")

# Initialize OpenAI client pointing to kluster.ai API
client = OpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key=api_key,
)

# Create request with specified structure
requests = [
    {
        "custom_id": "request-1",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "mistralai/Mistral-Nemo-Instruct-2407",
            "messages": [
                {"role": "system", "content": "You are an experienced cook."},
                {"role": "user", "content": "What is the ultimate breakfast sandwich?"},
            ],
            "max_completion_tokens": 1000,
        },
    },
    {
        "custom_id": "request-2",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "mistralai/Mistral-Nemo-Instruct-2407",
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
            "model": "mistralai/Mistral-Nemo-Instruct-2407",
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
file_name = "my_batch_request.jsonl"
with open(file_name, "w") as file:
    for request in requests:
        file.write(json.dumps(request) + "\n")

# Upload batch job file
batch_input_file = client.files.create(
        file=open(file_name, "rb"),
        purpose="batch"
)

# Submit batch job
batch_request = client.batches.create(
    input_file_id=batch_input_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
)

# Poll the batch status until it's complete
while True:
    batch_status = client.batches.retrieve(batch_request.id)
    print("Batch status: {}".format(batch_status.status))
    print(
        f"Completed tasks: {batch_status.request_counts.completed} / {batch_status.request_counts.total}"
    )

    if batch_status.status.lower() in ["completed", "failed", "cancelled"]:
        break

    time.sleep(10)  # Wait for 10 seconds before checking again

# Check if the Batch completed successfully
if batch_status.status.lower() == "completed":
    # Retrieve the results and log
    result_file_id = batch_status.output_file_id
    results = client.files.content(result_file_id).content

    # Print response to console
    print(f"\n🔍 AI batch response:")
    print(results)
else:
    print(f"Batch failed with status: {batch_status.status}")