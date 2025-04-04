import json
import time
from getpass import getpass

from openai import OpenAI

# Newtown's cradle
image1_url="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/balls-image.jpeg?raw=true"
# Text with typos
image2_url="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/text-typo-image.jpeg?raw=true"
# Parking sign
image3_url="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"


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
            "model": "Qwen/Qwen2.5-VL-7B-Instruct",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What is this?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image1_url
                            },
                        },
                    ],
                }
            ],
            "max_completion_tokens": 1000,
        },
    },
    {
        "custom_id": "request-2",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "Qwen/Qwen2.5-VL-7B-Instruct",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract the text, find typos if any."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image2_url
                            },
                        },
                    ],
                }
            ],
            "max_completion_tokens": 1000,
        },
    },
    {
        "custom_id": "request-3",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "Qwen/Qwen2.5-VL-7B-Instruct",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Who can park in the area?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image3_url
                            },
                        },
                    ],
                }
            ],
            "max_completion_tokens": 1000,
        },
    },
]

# Save tasks to a JSONL file (newline-delimited JSON)
file_name = "my_batch_request.jsonl"
with open(file_name, "w") as file:
    for request in requests:
        file.write(json.dumps(request) + "\n")

# Upload batch job file
batch_input_file = client.files.create(file=open(file_name, "rb"), purpose="batch")

# Submit batch job
batch_request = client.batches.create(
    input_file_id=batch_input_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
)

# Poll the batch status until it's complete
while True:
    batch_status = client.batches.retrieve(batch_request.id)
    print(f"Batch status: {batch_status.status}")
    print(
        f"Completed tasks: {batch_status.request_counts.completed} / {batch_status.request_counts.total}"
    )

    if batch_status.status.lower() in ["completed", "failed", "cancelled"]:
        break

    time.sleep(10)  # Wait for 10 seconds before checking again

print(f"\nImage1 URL: {image1_url}")
print(f"\nImage2 URL: {image2_url}")
print(f"\nImage3 URL: {image3_url}")

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
    print(batch_status)