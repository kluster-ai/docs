curl https://api.kluster.ai/v1/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
            "model": "Qwen/Qwen2.5-VL-7B-Instruct", 
            "messages": [
                { 
                    "role": "user", 
                    "content": "What is the ultimate breakfast sandwich?" 
                }
            ]
        }'