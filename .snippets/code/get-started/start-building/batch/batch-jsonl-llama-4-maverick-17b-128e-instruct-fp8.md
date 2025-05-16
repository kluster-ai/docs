# Batch API completions with Meta Llama 4 Maverick model (vision-capable)

# Replace YOUR_API_KEY with your actual API key
KLUSTER_API_KEY="YOUR_API_KEY"

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
  -H "Authorization: Bearer $KLUSTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    "input_file_url": "file://batch_input.jsonl",
    "output_file_url": "file://batch_output.jsonl"
  }'
