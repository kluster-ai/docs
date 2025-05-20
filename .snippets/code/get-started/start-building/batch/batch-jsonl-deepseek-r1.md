# Batch API completions with DeepSeek-R1 model

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

# 1. Create input file (batch_input.jsonl)
cat > batch_input.jsonl << 'EOF'
{"messages": [{"role": "user", "content": "What is the capital of France?"}], "max_tokens": 100}
{"messages": [{"role": "user", "content": "What is machine learning?"}], "max_tokens": 150}
{"messages": [{"role": "user", "content": "Write a haiku about clouds."}], "max_tokens": 50}
EOF

# 2. Submit batch job
curl -X POST \
  https://api.kluster.ai/v1/batch/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-ai/DeepSeek-R1",
    "input_file_url": "file://batch_input.jsonl",
    "output_file_url": "file://batch_output.jsonl"
  }'
