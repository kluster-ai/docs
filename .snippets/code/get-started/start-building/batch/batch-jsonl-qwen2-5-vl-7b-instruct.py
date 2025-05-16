# Batch completions with the Qwen2.5-VL 7B model on Kluster.
import os
import json
import kluster
from typing import Dict, Any

# 1. Initialize the Kluster SDK client
#    Your API key can also be specified via KLUSTER_API_KEY environment variable
client = kluster.Client(api_key="YOUR_API_KEY")

# 2. Set up image URL
image_url = "https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

# 3. Create input file with multiple image requests (JSONL format)
input_jsonl_path = "batch_input.jsonl"
with open(input_jsonl_path, "w") as f:
    # Example 1
    f.write(json.dumps({
        "messages": [
            {
                "role": "user", 
                "content": [
                    {"type": "text", "text": "Who can park in the area?"},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ],
        "max_tokens": 300
    }) + "\n")
    
    # Example 2
    f.write(json.dumps({
        "messages": [
            {
                "role": "user", 
                "content": [
                    {"type": "text", "text": "What does this sign say?"},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ],
        "max_tokens": 300
    }) + "\n")

# 4. Define output file path
output_jsonl_path = "batch_output.jsonl"

# 5. Submit a batch job
batch_job = client.batch.completions.create(
    model="Qwen/Qwen2.5-VL-7B-Instruct",
    input_file_path=input_jsonl_path,
    output_file_path=output_jsonl_path,
)

print(f"Batch job submitted with ID: {batch_job.id}")

# 6. Wait for job to complete (optional)
completed_job = client.batch.jobs.wait(batch_job.id)
print(f"Batch job completed with status: {completed_job.status}")

# 7. Process results from output file
print("\nBatch results:")
with open(output_jsonl_path, "r") as f:
    for i, line in enumerate(f):
        result = json.loads(line)
        print(f"\nResult {i+1}:")
        print(f"Completion: {result['choices'][0]['message']['content']}")
        print(f"Finish reason: {result['choices'][0]['finish_reason']}")
        print(f"Total tokens: {result['usage']['total_tokens']}")
