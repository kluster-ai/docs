#!/bin/bash

# Check if API_KEY is set and not empty
if [[ -z "$API_KEY" ]]; then
    echo -e "\nError: API_KEY environment variable is not set.\n" >&2
fi

image_url="https://github.com/kluster-ai/klusterai-cookbook/blob/main/images/parking-image.jpeg?raw=true"

# Submit real-time request
curl https://api.kluster.ai/v1/chat/completions \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{
        \"model\": \"meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8\",
        \"messages\": [
            {
                \"role\": \"user\",
                \"content\": [
                    {\"type\": \"text\", \"text\": \"Who can park in the area?\"},
                    {\"type\": \"image_url\", \"image_url\": {\"url\": \"$image_url\"}}
                ]
            }
        ]
    }"
