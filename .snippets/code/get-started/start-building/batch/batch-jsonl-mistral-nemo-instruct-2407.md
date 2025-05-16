# Batch API completions with Mistral NeMo model

# Replace YOUR_API_KEY with your actual API key
KLUSTER_API_KEY="YOUR_API_KEY"

# 1. Create input file (batch_input.jsonl)
cat > batch_input.jsonl << 'EOF'
{"messages": [{"role": "user", "content": "What is the capital of France?"}], "max_tokens": 100}
{"messages": [{"role": "user", "content": "What is machine learning?"}], "max_tokens": 150}
{"messages": [{"role": "user", "content": "Write a haiku about clouds."}], "max_tokens": 50}
EOF

# 2. Submit batch job
curl -X POST \
  https://api.kluster.ai/v1/batch/completions \
  -H "Authorization: Bearer $KLUSTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistralai/Mistral-Nemo-Instruct-2407",
    "input_file_url": "file://batch_input.jsonl",
    "output_file_url": "file://batch_output.jsonl"
  }'
