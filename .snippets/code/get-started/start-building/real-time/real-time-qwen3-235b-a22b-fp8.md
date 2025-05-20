# Real-time API completions with Qwen3-235B-A22B model

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

curl -X POST \
  https://api.kluster.ai/v1/real-time/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen3-235B-A22B-FP8",
    "messages": [
      {
        "role": "user", 
        "content": "Write a poem about artificial intelligence."
      }
    ],
    "max_tokens": 100
  }'
