# Real-time API completions with Meta Llama 4 Scout model (vision-capable)

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

# Check if API_KEY is set and not empty
if [[ -z "$API_KEY" ]]; then
    echo -e "
Error: API_KEY environment variable is not set.
" >&2
fi

# Define image URL 
IMAGE_URL="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

curl -X POST \
  https://api.kluster.ai/v1/real-time/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
    "messages": [
      {
        "role": "user", 
        "content": [
          { "type": "text", "text": "Describe what you see in this image." },
          { "type": "image_url", "image_url": { "url": "'$IMAGE_URL'" } }
        ]
      }
    ],
    "max_tokens": 300
  }'
