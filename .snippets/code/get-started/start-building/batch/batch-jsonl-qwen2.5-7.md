#!/bin/bash

# Create request with specified structure
cat << EOF > my_batch_request.jsonl
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "Qwen/Qwen2.5-VL-7B-Instruct", "messages": [{"role": "system", "content": "You are an experienced cook."}, {"role": "user", "content": "What is the ultimate breakfast sandwich?"}],"max_completion_tokens":1000}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "Qwen/Qwen2.5-VL-7B-Instruct", "messages": [{"role": "system", "content": "You are an experienced maths tutor."}, {"role": "user", "content": "Explain the Pythagorean theorem."}],"max_completion_tokens":1000}}
{"custom_id": "request-4", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "Qwen/Qwen2.5-VL-7B-Instruct", "messages":[{"role": "system", "content": "You are a multilingual, experienced maths tutor."}, {"role": "user", "content": "Explain the Pythagorean theorem in Spanish"}],"max_completion_tokens":1000}}
EOF

# Upload batch job file
FILE_ID=$(curl -s https://api.kluster.ai/v1/files \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@my_batch_request.jsonl" \
    -F "purpose=batch" | jq -r '.id')
echo "File uploaded, file ID: $FILE_ID"

# Submit batch job
BATCH_ID=$(curl -s https://api.kluster.ai/v1/batches \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "input_file_id": "'"$FILE_ID"'",
        "endpoint": "/v1/chat/completions",
        "completion_window": "24h"
    }' | jq -r '.id')
echo "Batch job submitted, job ID: $BATCH_ID"


# Poll the batch status until it's completed
STATUS="in_progress"
while [[ "$STATUS" != "completed" ]]; do
    echo "Waiting for batch job to complete... Status: $STATUS"
    sleep 10 # Wait for 10 seconds before checking again

    STATUS=$(curl -s https://api.kluster.ai/v1/batches/$BATCH_ID \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: application/json" | jq -r '.status')
done

# Retrieve the batch output file
KLUSTER_OUTPUT_FILE=$(curl -s https://api.kluster.ai/v1/batches/$BATCH_ID \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" | jq -r '.output_file_id')

# Retrieve the results
OUTPUT_CONTENT=$(curl -s https://api.kluster.ai/v1/files/$KLUSTER_OUTPUT_FILE/content \
    -H "Authorization: Bearer $API_KEY")

# Log results
echo -e "\n🔍 AI batch response:"
echo "$OUTPUT_CONTENT"
