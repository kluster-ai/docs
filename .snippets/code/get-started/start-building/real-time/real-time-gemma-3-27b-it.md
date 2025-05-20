# Real-time API completions with Gemma 3 27B model (vision-capable)

# Ensure your API key is set in your environment
# export API_KEY="your_api_key_here"

# Define image URL 
IMAGE_URL="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

curl -X POST \
  https://api.kluster.ai/v1/real-time/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemma-3-27b-it",
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
