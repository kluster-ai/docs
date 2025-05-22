# Batch API completions with Mistral NeMo model

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

# Check if API_KEY is set and not empty
if [[ -z "$API_KEY" ]]; then
    echo -e "
Error: API_KEY environment variable is not set.
" >&2
fi

# 1. Create input file (batch_input.jsonl)
cat > batch_input.jsonl << 'EOF'
{"messages": [{"role": "user", "content": "What is the capital of Argentina?"}], "max_tokens": 100}
{"messages": [{"role": "user", "content": "Write a short poem about neural networks."}], "max_tokens": 150}
{"messages": [{"role": "user", "content": "Create a short sci-fi story about AI in 50 words."}], "max_tokens": 50}
EOF

# 2. Submit batch job
curl -X POST \
  https://api.kluster.ai/v1/batch/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistralai/Mistral-Nemo-Instruct-2407",
    "input_file_url": "file://batch_input.jsonl",
    "output_file_url": "file://batch_output.jsonl"
  }'
