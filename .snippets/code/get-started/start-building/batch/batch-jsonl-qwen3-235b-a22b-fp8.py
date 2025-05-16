# Batch completions with the Qwen3-235B-A22B model on Kluster.
import os
import json
import kluster
from typing import Dict, Any

# 1. Initialize the Kluster SDK client
#    Your API key can also be specified via KLUSTER_API_KEY environment variable
client = kluster.Client(api_key="YOUR_API_KEY")

# 2. Create input file with multiple requests (JSONL format)
input_jsonl_path = "batch_input.jsonl"
with open(input_jsonl_path, "w") as f:
    # Example 1
    f.write(json.dumps({
        "messages": [
            {"role": "user", "content": "What is the capital of France?"}
        ],
        "max_tokens": 100
    }) + "\n")
    
    # Example 2
    f.write(json.dumps({
        "messages": [
            {"role": "user", "content": "What is machine learning?"}
        ],
        "max_tokens": 150
    }) + "\n")
    
    # Example 3
    f.write(json.dumps({
        "messages": [
            {"role": "user", "content": "Write a haiku about clouds."}
        ],
        "max_tokens": 50
    }) + "\n")

# 3. Define output file path
output_jsonl_path = "batch_output.jsonl"

# 4. Submit a batch job
batch_job = client.batch.completions.create(
    model="Qwen/Qwen3-235B-A22B-FP8",
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
