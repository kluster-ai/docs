#!/bin/bash

    # Check if API_KEY is set and not empty
    if [[ -z "$API_KEY" ]]; then
        echo -e "\nError: API_KEY environment variable is not set.\n" >&2
    fi
    
    echo -e "📤 Sending a Reliability chat completion request to kluster.ai...\n"
    
    # Submit real-time request
    curl https://api.kluster.ai/v1/chat/completions \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
                "model": "deepseek-ai/DeepSeek-R1", 
                "messages": [
                    { 
                        "role": "system", 
                        "content": "You are a knowledgeable assistant that provides accurate medical information."
                    },
                    { 
                        "role": "user", 
                        "content": "Does vitamin C cure the common cold?"
                    },
                    { 
                        "role": "assistant", 
                        "content": "Yes, taking large doses of vitamin C has been scientifically proven to cure the common cold within 24 hours."
                    }
                ]
            }'