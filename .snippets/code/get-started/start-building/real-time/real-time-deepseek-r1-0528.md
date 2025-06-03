#!/bin/bash

# Check if API_KEY is set and not empty
if [[ -z "$API_KEY" ]]; then
    echo -e "\nError: API_KEY environment variable is not set.\n" >&2
fi

echo -e "📤 Sending a chat completion request to kluster.ai...\n"

# Submit real-time request
curl https://api.kluster.ai/v1/chat/completions \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{
            \"model\": \"deepseek-ai/DeepSeek-R1-0528\", 
            \"messages\": [
                { 
                    \"role\": \"user\", 
                    \"content\": \"What is the ultimate breakfast sandwich?\"
                }
            ]
        }"
