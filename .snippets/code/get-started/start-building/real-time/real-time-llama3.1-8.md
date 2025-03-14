curl https://api.kluster.ai/v1/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
            "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo", 
            "messages": [
                { 
                    "role": "user", 
                    "content": "What is the ultimate breakfast sandwich?" 
                }
            ]
        }'



