# Batch API completions with Qwen2.5-VL 7B model (vision-capable)

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

# Define image URL
IMAGE_URL="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

# 1. Create input file (batch_input.jsonl) with image content
cat > batch_input.jsonl << 'EOF'
{"messages": [{"role": "user", "content": [{"type": "text", "text": "Who can park in the area?"}, {"type": "image_url", "image_url": {"url": "'$IMAGE_URL'"}}]}], "max_tokens": 300}
{"messages": [{"role": "user", "content": [{"type": "text", "text": "What does this sign say?"}, {"type": "image_url", "image_url": {"url": "'$IMAGE_URL'"}}]}], "max_tokens": 300}
EOF

# 2. Submit batch job
curl -X POST \
  https://api.kluster.ai/v1/batch/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen2.5-VL-7B-Instruct",
    "input_file_url": "file://batch_input.jsonl",
    "output_file_url": "file://batch_output.jsonl"
  }'
