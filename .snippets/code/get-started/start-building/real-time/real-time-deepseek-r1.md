# Real-time API completions with DeepSeek-R1 model

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

curl -X POST \
  https://api.kluster.ai/v1/real-time/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-ai/DeepSeek-R1",
    "messages": [
      {
        "role": "user", 
        "content": "Write a poem about artificial intelligence."
      }
    ],
    "max_tokens": 100
  }'
