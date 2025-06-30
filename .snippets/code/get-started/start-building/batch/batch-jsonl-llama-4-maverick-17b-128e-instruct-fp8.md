#!/bin/bash

# Check if API_KEY is set and not empty
if [[ -z "$API_KEY" ]]; then
    echo "Error: API_KEY environment variable is not set." >&2
    exit 1
fi

echo -e "📤 Sending batch request to kluster.ai...\n"

# Define image URLs
# Newton's cradle
image1_url="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/balls-image.jpeg?raw=true"
# Text with typos
image2_url="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/text-typo-image.jpeg?raw=true"
# Parking sign
image3_url="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

# Create request with specified structure
cat << EOF > my_batch_request.jsonl
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8", "messages": [{"role": "user", "content": [{"type": "text", "text": "What is this?"}, {"type": "image_url", "image_url": {"url": "$image1_url"}}]}],"max_completion_tokens": 1000}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8", "messages": [{"role": "user", "content": [{"type": "text", "text": "Extract the text, find typos if any."}, {"type": "image_url", "image_url": {"url": "$image2_url"}}]}],"max_completion_tokens": 1000}}
{"custom_id": "request-3", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8", "messages": [{"role": "user", "content": [{"type": "text", "text": "Who can park in the area?"}, {"type": "image_url", "image_url": {"url": "$image3_url"}}]}],"max_completion_tokens": 1000}}
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
        "input_file_id": "'$FILE_ID'",
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
kluster_OUTPUT_FILE=$(curl -s https://api.kluster.ai/v1/batches/$BATCH_ID \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" | jq -r '.output_file_id')

# Retrieve the results
OUTPUT_CONTENT=$(curl -s https://api.kluster.ai/v1/files/$kluster_OUTPUT_FILE/content \
    -H "Authorization: Bearer $API_KEY")

# Log results
echo -e "\nImage1 URL: $image1_url"
echo -e "\nImage2 URL: $image2_url"
echo -e "\nImage3 URL: $image3_url"
echo -e "\n🔍 AI batch response:"
echo "$OUTPUT_CONTENT"
