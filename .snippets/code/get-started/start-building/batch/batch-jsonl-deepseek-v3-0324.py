# Batch completions with the DeepSeek-V3-0324 model on Kluster.
import os
import json
import getpass
import kluster
from typing import Dict, Any

# 1. Initialize the Kluster SDK client
# Get API key securely using getpass (will not be displayed or saved)
api_key = os.environ.get("API_KEY") or getpass.getpass("Enter your Kluster API key: ")
client = kluster.Client(api_key=api_key)

# 2. Create input file with multiple requests (JSONL format)
input_jsonl_path = "batch_input.jsonl"
with open(input_jsonl_path, "w") as f:
    # Example 1
    f.write(json.dumps({
        "messages": [
            {"role": "user", "content": "What is the capital of Argentina?"}
        ],
        "max_tokens": 100
    }) + "\n")
    
    # Example 2
    f.write(json.dumps({
        "messages": [
            {"role": "user", "content": "Write a short poem about neural networks."}
        ],
        "max_tokens": 150
    }) + "\n")
    
    # Example 3
    f.write(json.dumps({
        "messages": [
            {"role": "user", "content": "Create a short sci-fi story about AI in 50 words."}
        ],
        "max_tokens": 100
    }) + "\n")

# 3. Define output file path
output_jsonl_path = "batch_output.jsonl"

# 4. Submit a batch job
batch_job = client.batch.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    input_file_path=input_jsonl_path,
    output_file_path=output_jsonl_path,
)

print(f"Batch job submitted with ID: {batch_job.id}")

# 5. Wait for job to complete (optional)
completed_job = client.batch.jobs.wait(batch_job.id)
print(f"Batch job completed with status: {completed_job.status}")

# 6. Process results from output file
print("\nBatch results:")
with open(output_jsonl_path, "r") as f:
    for i, line in enumerate(f):
        result = json.loads(line)
        print(f"\nResult {i+1}:")
        print(f"Completion: {result['choices'][0]['message']['content']}")
        print(f"Finish reason: {result['choices'][0]['finish_reason']}")
        print(f"Total tokens: {result['usage']['total_tokens']}")
