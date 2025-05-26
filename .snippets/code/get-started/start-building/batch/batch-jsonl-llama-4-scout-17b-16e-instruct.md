# Batch API completions with Meta Llama 4 Scout model (vision-capable)

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

# Check if API_KEY is set and not empty
if [[ -z "$API_KEY" ]]; then
    echo -e "
Error: API_KEY environment variable is not set.
" >&2
fi

# Define image URL
IMAGE_URL="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

# 1. Create input file (batch_input.jsonl) with image content
cat > batch_input.jsonl << EOF
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "meta-llama/Llama-4-Scout-17B-16E-Instruct", "messages": [{"role": "user", "content": [{"type": "text", "text": "Who can park in the area?"}, {"type": "image_url", "image_url": {"url": "$IMAGE_URL"}}]}], "max_tokens": 300}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "meta-llama/Llama-4-Scout-17B-16E-Instruct", "messages": [{"role": "user", "content": [{"type": "text", "text": "What does this sign say?"}, {"type": "image_url", "image_url": {"url": "$IMAGE_URL"}}]}], "max_tokens": 300}}
EOF

# 2. Upload batch input file
UPLOAD_RESPONSE=$(curl -X POST \
  https://api.kluster.ai/v1/files \
  -H "Authorization: Bearer $API_KEY" \
  -F "purpose=batch" \
  -F "file=@batch_input.jsonl")

# Extract file ID from upload response
FILE_ID=$(echo $UPLOAD_RESPONSE | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)

# 3. Submit batch job
curl -X POST \
  https://api.kluster.ai/v1/batches \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input_file_id": "'$FILE_ID'",
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h"
  }'
