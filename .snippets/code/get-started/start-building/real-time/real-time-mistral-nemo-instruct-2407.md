<!-- filepath: /Users/franzuzz/code/kluster-mkdocs/kluster-docs/.snippets/code/get-started/start-building/real-time/real-time-mistral-nemo-instruct-2407.md -->
#!/bin/bash

# Check if API_KEY is set and not empty
if [[ -z "$API_KEY" ]]; then
    echo -e "\nError: API_KEY environment variable is not set.\n" >&2
fi

# Submit real-time request
curl https://api.kluster.ai/v1/chat/completions \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{
            \"model\": \"mistralai/Mistral-Nemo-Instruct-2407\", 
            \"messages\": [
                { 
                    \"role\": \"user\", 
                    \"content\": \"What is the ultimate breakfast sandwich?\"
                }
            ]
        }"
