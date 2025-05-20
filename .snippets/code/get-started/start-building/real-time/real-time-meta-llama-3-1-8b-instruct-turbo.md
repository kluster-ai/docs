# Real-time API completions with Meta Llama 3.1 8B model

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

curl -X POST \
  https://api.kluster.ai/v1/real-time/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    "messages": [
      {
        "role": "user", 
        "content": "What is the capital of France?"
      }
    ],
    "max_tokens": 100
  }'
