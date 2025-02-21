---

title: Start performing real-time inferences
description: This page provides examples and instructions for submitting and managing real-time jobs using kluster.ai's OpenAI-compatible API.
---

This page gives a quick overview of how to use real-time inferences with the [kluster.ai](https://platform.kluster.ai/){target=\_blank} API. 

This type of inference is best suited for situations where you need **instant**, **synchronous** responses—perfect for user-facing features like chat interactions, live recommendations, or real-time decision-making.

## Supported models

Real-time inferences through kluster.ai support the following models:

--8<-- 'text/real-time-models.md'

In addition, you can see the complete list of available models programmatically using the [list supported models](/api-reference/reference/#list-supported-models){target=\_blank} endpoint.

## Submitting a request

The **kluster.ai** platform offers a simple, [OpenAI-compatible](/get-started/openai-compatibility/){target=\_blank} interface, making it easy to integrate kluster.ai services seamlessly into your existing system.

The example below demonstrates a pre-configured interface to get you started:

=== "Python"

 ```python
    from openai import OpenAI
    import json
    import os


 client = OpenAI(
        api_key="INSERT_API_KEY",
        base_url="https://api.kluster.ai/v1"
 )

    # Create chat completion request
 completion = client.chat.completions.create(
        model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[
 {"role": "user", "content": "What's the name of the most famous street in Paris?"}
 ]
 )

    def log_response_to_file(response, filename="response_log.json"):
        """Logs the full AI response to a JSON file in the same directory as the script."""
        
        # Convert response to dictionary
 response_data = response.dict()
        
        # Get the script directory
 script_dir = os.path.dirname(os.path.abspath(__file__))
 file_path = os.path.join(script_dir, filename)
        
        # Write to JSON file
        with open(file_path, "w", encoding="utf-8") as json_file:
 json.dump(response_data, json_file, ensure_ascii=False, indent=4)
        
        print(f"Response logged to {file_path}")

    # Log response to file
 log_response_to_file(completion)
 ```

=== "curl"

 ``` curl
 curl https://api.kluster.ai/v1/chat/completions \
 -H "Authorization: Bearer YOUR_API_KEY" \ # Replace with your actual API key
 -H "Content-Type: application/json" \
 -d '{
 "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo", # Can be configured to use any of models supported by kluster.ai
 "messages": [
 { "role": "user", "content": "What is the most famous street in Paris?" }
 ]
 }'
 ```

There are several configurable parameters when using real-time inferences:

- `model` – Name of one of the [supported models](#supported-models)

- `messages` – In the `content` parameter, you should provide the query you want to process. You can pass any input here. This example is querying what is the most famous street in Paris

After configuring these parameters, you can go ahead and run your script.

## Response

If the request is successfully processed, the response should follow this structure and contain relevant data such as the generated output, metadata, and token usage details. 

Here's an example of what the response should look like:

```Json title="Response"
{
    "id": "chatcmpl-e9b942d1-06fb-4d1b-88c2-820c9ca7bb20",
    "choices": [
 {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "message": {
                "content": "The most famous street in Paris is the Champs-Élysées.",
                "refusal": null,
                "role": "assistant",
                "audio": null,
                "function_call": null,
                "tool_calls": []
 },
            "stop_reason": null
 }
 ],
    "created": 1739960163,
    "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    "object": "chat.completion",
    "service_tier": null,
    "system_fingerprint": null,
    "usage": {
        "completion_tokens": 16,
        "prompt_tokens": 47,
        "total_tokens": 63,
        "completion_tokens_details": null,
        "prompt_tokens_details": null
 },
    "prompt_logprobs": null
}
```
!!! note
 Please refer to the [**chat completion API reference**](/api-reference/reference#chat-completion-object) section for a detailed response breakdown.

## Third-party integrations

You can also set up a third-party LLM interface using the kluster.ai API. For step-by-step instructions, check out the guides for integrations such as [SillyTavern](/get-started/integrations/sillytavern){target=\_blank}, [LangChain](/get-started/integrations/langchain/){target=\_blank}, [eliza](/get-started/integrations/eliza/){target=\_blank} and more, in the **Integrations** section. 

## Summary

You are set up to work with kluster.ai real-time inference, specifically the chat completion API in this guide. In this guide, you've learned:

- How to submit a real-rime inference request:
    - The kluster.ai API is OpenAI-compatible, making it easy to integrate into your existing workflow.
    - You've seen hands-on examples in Python and cURL, so you know how to send requests.

- How to configure API parameters:
    - Choosing the right `model`
    - The `messages` parameter

- How to interpret the API response:
    - Now you know what a successful response looks like—including the generated output, metadata, and token usage details.

The kluster.ai batch API is designed to efficiently and reliably handle your large-scale LLM workloads. Do you have questions or suggestions? The [support](mailto:support@kluster.ai){target=\_blank} team would love to hear from you.