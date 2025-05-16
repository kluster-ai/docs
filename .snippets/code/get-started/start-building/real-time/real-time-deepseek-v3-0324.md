# Real-time API completions with DeepSeek-V3-0324 model

# Replace YOUR_API_KEY with your actual API key
KLUSTER_API_KEY="YOUR_API_KEY"

curl -X POST \
  https://api.kluster.ai/v1/real-time/completions \
  -H "Authorization: Bearer $KLUSTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-ai/DeepSeek-V3-0324",
    "messages": [
      {
        "role": "user", 
        "content": "What is the capital of France?"
      }
    ],
    "max_tokens": 100
  }'
