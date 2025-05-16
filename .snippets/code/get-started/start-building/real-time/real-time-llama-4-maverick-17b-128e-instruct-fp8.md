# Real-time API completions with Meta Llama 4 Maverick model (vision-capable)

# Replace YOUR_API_KEY with your actual API key
KLUSTER_API_KEY="YOUR_API_KEY"

# Define image URL 
IMAGE_URL="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

curl -X POST \
  https://api.kluster.ai/v1/real-time/completions \
  -H "Authorization: Bearer $KLUSTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
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
