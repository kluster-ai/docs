# Batch completions with the DeepSeek-V3-0324 model on Kluster.
import os
import json
import getpass
from openai import OpenAI

# 1. Initialize OpenAI client pointing to kluster.ai API
# Get API key securely using getpass (will not be displayed or saved)
api_key = os.environ.get("API_KEY") or getpass.getpass("Enter your Kluster API key: ")
client = OpenAI(
    api_key=api_key,
    base_url="https://api.kluster.ai/v1"
)

# 2. Create input file with multiple requests (JSONL format)
input_jsonl_path = "batch_input.jsonl"
with open(input_jsonl_path, "w") as f:
    # Example 1
    f.write(json.dumps({
        "custom_id": "request-1",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "deepseek-ai/DeepSeek-V3-0324",
            "messages": [
                {"role": "user", "content": "What is the capital of Argentina?"}
            ],
            "max_tokens": 100
        }
    }) + "\n")
    
    # Example 2
    f.write(json.dumps({
        "custom_id": "request-2",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "deepseek-ai/DeepSeek-V3-0324",
            "messages": [
                {"role": "user", "content": "Write a short poem about neural networks."}
            ],
            "max_tokens": 150
        }
    }) + "\n")
    
    # Example 3
    f.write(json.dumps({
        "custom_id": "request-3",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "deepseek-ai/DeepSeek-V3-0324",
            "messages": [
                {"role": "user", "content": "Create a short sci-fi story about AI in 50 words."}
            ],
            "max_tokens": 100
        }
    }) + "\n")

# 3. Upload batch input file
with open(input_jsonl_path, "rb") as file:
    batch_input_file = client.files.create(
        file=file,
        purpose="batch"
    )

# 4. Submit batch job
batch_request = client.batches.create(
    input_file_id=batch_input_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
)

print(f"Batch job submitted with ID: {batch_request.id}")

# 5. Check batch status (optional)
batch_status = client.batches.retrieve(batch_request.id)
print("Batch status: {}".format(batch_status.status))

# 6. When completed, retrieve and process results
# Note: In a real scenario, you would poll the status until completion
if batch_status.status == "completed":
    result_file_id = batch_status.output_file_id
    result_content = client.files.content(result_file_id)
    
    print("\nBatch results:")
    for line in result_content.iter_lines():
        if line:
            result = json.loads(line)
            print(f"\nRequest ID: {result['custom_id']}")
            if 'response' in result and 'body' in result['response']:
                response_body = result['response']['body']
                if 'choices' in response_body and len(response_body['choices']) > 0:
                    print(f"Completion: {response_body['choices'][0]['message']['content']}")
                    print(f"Finish reason: {response_body['choices'][0]['finish_reason']}")
                if 'usage' in response_body:
                    print(f"Total tokens: {response_body['usage']['total_tokens']}")
