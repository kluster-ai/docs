# Batch API completions with DeepSeek-V3-0324 model

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

# Check if API_KEY is set and not empty
if [[ -z "$API_KEY" ]]; then
    echo -e "
Error: API_KEY environment variable is not set.
" >&2
fi

# 1. Create input file (batch_input.jsonl)
cat > batch_input.jsonl << EOF
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "deepseek-ai/DeepSeek-V3-0324", "messages": [{"role": "user", "content": "What is the capital of Argentina?"}], "max_tokens": 100}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "deepseek-ai/DeepSeek-V3-0324", "messages": [{"role": "user", "content": "Write a short poem about neural networks."}], "max_tokens": 150}}
{"custom_id": "request-3", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "deepseek-ai/DeepSeek-V3-0324", "messages": [{"role": "user", "content": "Create a short sci-fi story about AI in 50 words."}], "max_tokens": 100}}
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
