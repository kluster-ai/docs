# Real-time API completions with Meta Llama 3.3 70B model

# Replace YOUR_API_KEY with your actual API key
KLUSTER_API_KEY="YOUR_API_KEY"

curl -X POST \
  https://api.kluster.ai/v1/real-time/completions \
  -H "Authorization: Bearer $KLUSTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
    "messages": [
      {
        "role": "user", 
        "content": "What is the capital of France?"
      }
    ],
    "max_tokens": 100
  }'
