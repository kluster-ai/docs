---
title: Getting Started Guide
description: The kluster.ai getting started guide provides examples and instructions for submitting and managing Batch jobs using kluster.ai's OpenAI-compatible API.
hide:
- footer
---

# Getting started guide

Welcome to the Kluster.ai getting started guide! This guide provides a quick introduction to submitting Batch jobs.

Kluster.ai is API-compatible with the OpenAI library, supporting `model`, `messages`, and `stream` functions. If additional request properties are needed, they can be requested during the Early Access Plan. To install the OpenAI Python library, follow the [instructions](https://platform.openai.com/docs/libraries/python-library){target=\_blank} on OpenAI's documentation.

OpenAI object definitions are included to help you get started. For more details, refer to the OpenAI [API reference](https://platform.openai.com/docs/api-reference/introduction){target=\_blank}. The following sections offer Curl and Python examples on locating the API key, defining Batch jobs as a JSON Lines file, uploading the file to the Kluster.ai endpoint, invoking the chat completion endpoint, monitoring job progress, retrieving results, listing Batch objects, and canceling requests.

## Get Your API Key

Navigate to the [platform.kluster.ai](http://platform.kluster.ai){target=\_blank} web app and select **API Keys** from the left-hand menu. Create a new API key by specifying the API key name. You'll need this to set the auth header in all of the API requests.

## List Supported Models

First, you can use the models endpoint to list out the supported models that. Currently, only Meta-Llama-3.1-8B-Instruct, Meta-Llama-3.1-70B-Instruct, and Meta-Llama-3.1-405B-Instruct are supported. The response is a list of model objects.

<div class="grid" markdown>
<div markdown>

**Request**

`get https://api.kluster.ai/v1/models`

Lists the currently available models.

**Returns**

`id` ++"string"++

The model identifier, which can be referenced in the API endpoints.

---

`created` ++"integer"++

The Unix timestamp (in seconds) when the model was created.

---

`object` ++"string"++

The object type, which is always `model`.

---

`owned_by` ++"string"++

The organization that owns the model.

</div>
<div markdown>

```bash title="Example request"
curl https://api.kluster.ai/v1/models \
-H "Authorization: Bearer $API_KEY" 
```

```json title="Response"
[
   {
      "id":"meta-llama/Meta-Llama-3.1-70B-Instruct",
      "object":"model",
      "created":"1970-01-01T00:00:00Z",
      "owned_by":"owner1"
   },
   {
      "id":"meta-llama/Meta-Llama-3.1-8B-Instruct",
      "object":"model",
      "created":"1970-01-01T00:00:00Z",
      "owned_by":"owner2"
   },
   {
      "id":"meta-llama/Meta-Llama-3.1-405B-Instruct",
      "object":"model",
      "created":"1970-01-01T00:00:00Z",
      "owned_by":"owner3"
   }
]
```

</div>
</div>

---

## Create a Batch File with a Collection of Jobs

Create a [JSON Lines](https://jsonlines.org/) file containing a collection of `batch request input` objects. The body of each request is a `chat completion` object with the endpoint `/v1/chat/completions`. Each request must include a unique `custom_id` used to reference results after the Batch job has been completed.

<div class="grid" markdown>
<div markdown>

**Batch request input object**

`custom_id` ++"string"++

A developer-provided per-request ID that will be used to match outputs to inputs. Must be unique for each request in a Batch.

---

`method` ++"string"++

The HTTP method to be used for the request. Currently, only `POST` is supported.

---

`url` ++"string"++

The `/v1/chat/completions` API relative URL.

---

**Request body**

`body` ++"object"++ <span class="required" markdown>++"required"++</span>

The request body object (chat completion object).

??? child "Show properties"

    `model` ++"string"++ <span class="required" markdown>++"required"++</span>

    ID of the model to use. See the model endpoint compatibility table for details on which models work with the Chat API.

    ---

    `messages` ++"array"++ <span class="required" markdown>++"required"++</span>

    A list of messages comprising the conversation so far.

    ??? child "Show properties"

        `role` ++"string"++ <span class="required" markdown>++"required"++</span>

        The role of the messages author, in this case `assistant`.

        ---

        `content` ++"string or array"++

        The contents of the assistant message.  

        ---

        `refusal` ++"string or null"++

        The refusal message by the assistant.
        
        ---

        `name` ++"string"++

        An optional name for the participant. Provides the model information to differentiate between participants of the same role.

    ---

    `store` ++"boolean or null"++

    Whether or not to store the output of this chat completion request for use in our model distillation or evals products. Defaults to `false`.

    ---

    `metadata` ++"object or null"++

    Developer-defined tags and values used for filtering completions.

    ---

    `frequency_penalty` ++"number or null"++

    Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood of repeating the same line verbatim. Defaults to `0`.

    ---

    `logit_bias` ++"map"++

    Modify the likelihood of specified tokens appearing in the completion. Defaults to `null`.

    Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase the likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

    ---

    `logprobs` ++"boolean or null"++

    Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. Defaults to `false`.

    ---

    `top_logprobs` ++"integer or null"++

    An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.

    ---

    `max_tokens` ++"integer or null"++ *deprecated*

    This value is now deprecated in favor of `max_completion_tokens`.

    The maximum number of tokens that can be generated in the chat completion. This value can be used to control costs for text generated via API.

    ---

    `max_completion_tokens` ++"integer or null"++

    An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens.

    ---

    `n` ++"integer or null"++

    The number of chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs. Defaults to `1`.

    ---

    `presence_penalty` ++"number or null"++

    Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. Defaults to `0`.

    ---

    `response_format` ++"object"++

    An object specifying the format that the model must output. Compatible with Meta-Llama-3.1-8B-Instruct, Meta-Llama-3.1-70B-Instruct, and Meta-Llama-3.1-405B-Instruct.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema.

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    ---

    `seed` ++"integer or null"++

    This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

    ---

    `service_tier` ++"string or null"++

    Specifies the latency tier to use for processing the request. Defaults to `null`. This parameter is relevant for customers subscribed to the scale tier service:

    - If set to `auto`, and the Project is Scale tier enabled, the system will utilize scale tier credits until they are exhausted
    - If set to `auto`, and the Project is not Scale tier enabled, the request will be processed using the default service tier with a lower uptime SLA and no latency guarantee
    - If set to `default`, the request will be processed using the default service tier with a lower uptime SLA and no latency guarantee
    - When not set, the default behavior is `auto`
    - When this parameter is set, the response body will include the `service_tier` utilized

    ---

    `stop` ++"string or array or null"++

    Up to four sequences where the API will stop generating further tokens. Defaults to `null`.

    ---

    `stream` ++"boolean or null"++

    If set, partial message deltas will be sent, like in ChatGPTpl. Tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a `data: [DONE]` message. Defaults to `false`.

    ---

    `stream_options` ++"object or null"++

    Options for streaming response. Only set this when you set `stream: true`. Defaults to `null`

    ---

    `temperature` ++"number or null"++

    The sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. Defaults to `1`.

    It is generally recommended to alter this or `top_p` but not both.

    ---

    `top_p` ++"number or null"++

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. Defaults to `1`.

    It is generally recommended to alter this or `temperature` but not both.

    ---

    `tools` ++"array"++

    A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

    ---

    `tool_choice` ++"string or object"++

    Controls which (if any) tool is called by the model.

    - `none` means the model will not call any tool and instead generates a message
    - `auto` means the model can pick between generating a message or calling one or more tools
    - `required` means the model must call one or more tools. Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool

    `none` is the default when no tools are present. `auto` is the default if tools are present.

    ---

    `parallel_tool_calls` ++"boolean"++

    Whether to enable [**parallel function calling**](https://platform.openai.com/docs/guides/function-calling/parallel-function-calling){target=\_blank} during tool use. Defaults to `true`.

    ---

    `user` ++"string"++

    A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.

    ---

    `function_call` ++"string or object"++ *deprecated*

    This value is now deprecated in favor of `tool_choice`.

    Controls which (if any) function is called by the model.

    - `none` means the model will not call a function and instead generates a message
    - `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"name": "my_function"}` forces the model to call that function

    `none` is the default when no functions are present. `auto` is the default if functions are present.

    ---

    `functions` ++"array"++ *deprecated*

    This value is now deprecated in favor of `tools`.

    A list of functions the model may generate JSON inputs for.

**Returns**

A chat completion object, or a streamed sequence of chat completion chunk objects if the request is streamed.

`id` ++"string"++

A unique identifier for the chat completion.

---

`choices` ++"array"++

A list of chat completion choices. Can be more than one if `n` is greater than `1`.

??? child "Show properties"

    `finish_reason` ++"string"++
    
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters, `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

    ---

    `index` ++"integer"++
    
    The index of the choice in the list of choices.

    ---

    `message` ++"object"++ <span class="required" markdown>++"required"++</span>
    
    A chat completion message generated by the model.

    ??? child "Show properties"

        `content` ++"array or null"++
        
        A list of message content tokens with log probability information.
        
        ---
        
        `refusal` ++"array or null"++
        
        A list of message refusal tokens with log probability information.
        
        ---

        `tool_calls` ++"array"++
        
        The tool calls generated by the model, such as function calls.

        ??? child "Show properties"

            `id` ++"string"++
            
            The ID of the tool call.

            ---

            `type` ++"string"++
            
            The type of the tool. Currently, only `function` is supported.

            ---

            `function` ++"object"++ <span class="required" markdown>++"required"++</span>
                
            The function that the model called.

            ??? child "Show properties"

                `name` ++"string"++
                        
                The name of the function to call.

                ---

                `arguments` ++"string"++
                         
                The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
        
        ---

        `role` ++"string"++
        
        The role of the author of this message.
        
        --- 
        
        `function_call` ++"object"++ *deprecated*

        This value is now deprecated in favor of `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

        ??? child "Show properties" 

            `arguments` ++"string"++
            
            The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
            
            ---
            
            `name` ++"string"++

            The name of the function to call.      

    ---

    `logprobs` ++"object or null"++

    Log probability information for the choice.

    ??? child "Show properties" 

        `content` ++"array or null"++
        
        A list of message content tokens with log probability information.
        
        ---
        
        `refusal` ++"array or null"++
        
        A list of message refusal tokens with log probability information.

---

`created` ++"integer"++

The Unix timestamp (in seconds) of when the chat completion was created.

---

`model` ++"string"++

The model used for the chat completion.

---

`service_tier` ++"string or null"++

The service tier used for processing the request. This field is only included if the `service_tier` parameter is specified in the request.

---

`system_fingerprint` ++"string"++

This fingerprint represents the backend configuration that the model runs with. It can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

---

`object` ++"string"++

The object type, which is always `chat.completion`.

---

`usage` ++"object"++

Usage statistics for the completion request.

??? child "Show properties"

    `completion_tokens` ++"integer"++
    
    Number of tokens in the generated completion.

    ---

    `prompt_tokens` ++"integer"++
    
    Number of tokens in the prompt.

    ---

    `total_tokens` ++"integer"++
    
    Total number of tokens used in the request (prompt + completion).

    ---

    `completion_tokens_details` ++"object"++
    
    Breakdown of tokens used in a completion.

    ??? child "Show properties" 

        `audio_tokens` ++"integer"++
        
        Audio input tokens generated by the model.
        
        ---
        
        `reasoning_tokens` ++"integer"++
        
        Tokens generated by the model for reasoning.
    
    ---

    `prompt_tokens_details` ++"object"++
    
    Breakdown of tokens used in the prompt.

    ??? child "Show properties" 

        `audio_tokens` ++"integer"++
        
        Audio input tokens present in the prompt.

        ---

        `cached_tokens` ++"integer"++
        
        Cached tokens present in the prompt.

</div>
<div markdown>

=== "Curl"

    ```json title="Example: Collection of Batch Jobs"
    {"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "meta-llama/Meta-Llama-3.1-8B-Instruct", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of Argentina?"}],"max_tokens":1000}}
    {"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "meta-llama/Meta-Llama-3.1-70B-Instruct", "messages": [{"role": "system", "content": "You are an experienced maths tutor."}, {"role": "user", "content": "Explain the Pythagorean theorem to a 10 year old child"}],"max_tokens":1000}}
    {"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "meta-llama/Meta-Llama-3.1-405B-Instruct", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the distance between the Earth and the Moon"}],"max_tokens":1000}}
    ```

=== "Python"

    ```python title="Example: Collection of Batch Jobs"
    tasks = [{
            "custom_id": "request-1",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "What is the capital of Argentina?"},
                ],
                "max_tokens": 1000,
            },
        },
        {
            "custom_id": "request-2",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "meta-llama/Meta-Llama-3.1-70B-Instruct",
                "messages": [
                    {"role": "system", "content": "You are a maths tutor."},
                    {"role": "user", "content": "You are an experienced maths tutor."}, {"role": "user", "content": "Explain the Pythagorean theorem."},
                ],
                "max_tokens": 1000,
            },
        },
        {
            "custom_id": "request-3",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "meta-llama/Meta-Llama-3.1-405B-Instruct",
                "messages": [
                    {"role": "system", "content": "You are an astronomer."},
                    {"role": "user", "content": "You are an experienced maths tutor."}, {"role": "user", "content": "What is the distance between the Earth and the Moon?"},
                ],
                "max_tokens": 1000,
            },
        }
        # Additional tasks can be added here
    ]

    # Save tasks to a JSONL file (newline-delimited JSON)
    file_name = "batch_tasks.jsonl"
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")
    ```

</div>
</div>

---

## Upload Your Batch Input File

`https://api.kluster.ai/v1/files`

Upload a [JSON Lines](https://jsonlines.org/){target=\_blank} document to the Kluster.ai endpoint and take a note of the `id` in the response object.

<div class="grid" markdown>
<div markdown>

**Request**

`file` ++"file"++ <span class="required" markdown>++"Required"++</span>

The [File](#the-file-object) object (not file name) to be uploaded.

---

`purpose` ++"string"++ <span class="required" markdown>++"Required"++</span>

The intended purpose of the uploaded file. Use `batch` for the Batch API.

**Returns**

The uploaded [File](#the-file-object) object.

`id` ++"string"++

The file identifier, which can be referenced in the API endpoints.

---

`object` ++"string"++

The object type, which is always `file`.

---

`bytes` ++"integer"++

The size of the file, in bytes.

---

`created_at` ++"integer"++

The Unix timestamp (in seconds) for when the file was created.

---

`filename` ++"string"++

The name of the file.

---

`purpose` ++"string"++

The intended purpose of the file. Currently, only `batch` is supported.

</div>
<div markdown>

=== "Curl"

    ```bash title="Example request"
    curl -s https://api.kluster.ai/v1/files \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@mybatchtest.jsonl" \
    -F "purpose=batch"
    ```

=== "Python"

    ```python title="Example request"
    # Upload the file to the platform
    batch_file = client.files.create(file=open(file_name, "rb"), purpose="batch")
    print(f"Batch file uploaded. File ID: {batch_file.id}")
    ```

</div>
</div>

---

## Invoke the Chat Completion Endpoint

`post https://api.kluster.ai/v1/batches`

Next, to create a Batch job, you invoke the chat completion API using the `input_file_id` from the previous step.

<div class="grid" markdown>
<div markdown>

**Request**

`input_file_id` ++"string"++ <span class="required" markdown>++"Required"++</span>

The ID of an uploaded file that contains requests for the new Batch.

Your input file must be formatted as a [JSONL file](https://jsonlines.org/){target=\_blank}, and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 100 MB in size.

---

`endpoint` ++"string"++ <span class="required" markdown>++"Required"++</span>

The endpoint to be used for all requests in the Batch. Currently, only `/v1/chat/completions` is supported.

---

`completion_window` ++"string"++ <span class="required" markdown>++"Required"++</span>

The time frame within which the Batch should be processed. Currently, only **24h** is supported.

---

`metadata` ++"Object or null"++

Custom metadata for the Batch.

**Returns**

The created [Batch](#batch-object) object.

`id` ++"string"++

The ID of the batch.

---

`object` ++"string"++

The object type, which is always `batch`.

---

`endpoint` ++"string"++

The Kluster.ai API endpoint used by the batch.

---

`errors` ++"object"++

Show properties.

---

`input_file_id` ++"string"++

The ID of the input file for the batch.

---

`completion_window` ++"string"++

The time frame within which the batch should be processed.

---

`status` ++"string"++

The current status of the batch.

---

`output_file_id` ++"string"++

The ID of the file containing the outputs of successfully executed requests.

---

`error_file_id` ++"string"++

The ID of the file containing the outputs of requests with errors.

---

`created_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch was created.

---

`in_progress_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch started processing.

---

`expires_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch will expire.

---

`finalizing_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch started finalizing.

---

`completed_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch was completed.

---

`failed_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch failed.

---

`expired_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch expired.

---

`cancelling_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch started cancelling.

---

`cancelled_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch was cancelled.

---

`request_counts` ++"object"++

The request counts for different statuses within the Batch.

---

`metadata` ++"map"++

Set of 16 key-value pairs that can be attached to an object. This is useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long, and values can be a maximum of 512 characters long.

</div>
<div markdown>

=== "Curl"

    ```bash title="Example request"
    curl -s https://api.kluster.ai/v1/batches \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "input_file_id": "kluster-file-123",
    "endpoint": "/v1/chat/completions",
    "completion_window": "24h"
    }'
    ```

=== "Python"

    ```python title="Example request"
    # Submit the batch request
    batch_request = client.batches.create(
        input_file_id=batch_file.id,
        endpoint="/v1/chat/completions",
        completion_window="24h",  # Maximum time allowed for the batch to complete
        metadata={"description": "Batch job for chat completions"},
    )

    print(f"Batch request submitted. Batch ID: {batch_request.id}")
    ```

```Json title="Response"
{
    "id": "2b96e3e4-cd7b-43fd-9dd3-d82153bdd752",
    "object": "batch",
    "endpoint": "/v1/chat/completions",
    "errors": null,
    "input_file_id": "kluster-input-file-123",
    "completion_window": "24h",
    "status": "Validating",
    "output_file_id": null,
    "error_file_id": null,
    "created_at": "2024-10-07T12:45:38.109049154Z",
    "in_progress_at": null,
    "expires_at": "2024-10-08T12:45:38.109049154Z",
    "finalizing_at": null,
    "completed_at": null,
    "failed_at": null,
    "expired_at": null,
    "cancelling_at": null,
    "cancelled_at": null,
    "request_counts": {
        "total": 0,
        "completed": 0,
        "failed": 0
    },
    "metadata": {}
}
```

</div>
</div>

---

## Monitor the Progress of the Batch Job

`get https://api.kluster.ai/v1/batches/{batch_id}`

To verify that the Batch job has finished, check the `status` property for `completed` using the Batch id from the previous step.

<div class="grid" markdown>
<div markdown>

**Path parameters**

`batch_id` ++"string"++ <span class="required" markdown>++"Required"++</span>

The ID of the Batch to retrieve.

**Returns**

The [Batch](#the-batch-object) object matching the specified `id`.

</div>
<div markdown>

=== "Curl"

    ```bash title="Example request"
    curl -s https://api.kluster.ai/v1/batches/2b96e3e4-cd7b-43fd-9dd3-d82153bdd752 \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json"
    ```

=== "Python"

    ```python title="Example request"
    import time

    # Poll the batch status until it's complete
    while True:
        batch_status = client.batches.retrieve(batch_request.id)
        print(f"Batch status: {batch_status.status}")
        print(
            f"Completed tasks: {batch_status.request_counts.completed} / {batch_status.request_counts.total}"
        )

        if batch_status.status.lower() in ["completed", "failed", "canceled"]:
            break

        time.sleep(10)  # Wait for 10 seconds before checking again
    ```

```Json title="Response"
{
  "id": "2b96e3e4-cd7b-43fd-9dd3-d82153bdd752",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "kluster-input-file-123",
  "completion_window": "24h",
  "status": "Completed",
  "output_file_id": "kluster-output-file-123",
  "error_file_id": null,
  "created_at": "2024-10-07T13:08:52.821427Z",
  "in_progress_at": null,
  "expires_at": "2024-10-08T13:08:52.821427Z",
  "finalizing_at": null,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": null,
  "cancelled_at": null,
  "request_counts": {
    "total": 3,
    "completed": 3,
    "failed": 0
  },
  "metadata": {}
}
```

</div>
</div>

---

## Retrieve the File Content of the Batch Job

`get https://api.kluster.ai/v1/files/{file_id}/content`

To retrieve the file content of the Batch job, send a request to the `files` end point specifying the `output_file_id` and redirecting standard output to a file.

<div class="grid" markdown>
<div markdown>

**Path parameters**

`file_id` ++"string"++ <span class="required" markdown>++"Required"++</span>

The ID of the file to use for this request

**Returns**

The output file content matching the specified file ID.

</div>
<div markdown>

=== "Curl"

    ```bash title="Example request"
    curl -s https://api.kluster.ai/v1/files/kluster-output-file-123"/content \
    -H "Authorization: Bearer $API_KEY" > batch_output.jsonl
    ```

=== "Python"

    ```python title="Example request"
        # Check if the batch completed successfully
        if batch_status.status.lower() == "completed":
            # Retrieve the results
            result_file_id = batch_status.output_file_id
            results = client.files.content(result_file_id).content

            # Save results to a file
            result_file_name = "data/batch_results.jsonl"
            with open(result_file_name, "wb") as file:
                file.write(results)
            print(f"Results saved to {result_file_name}")
        else:
            print(f"Batch failed with status: {batch_status.status}")
    ```
</div>
</div>

---

## List all Batch Jobs

`get https://api.kluster.ai/v1/batches`

To list all of your [Batch](#the-batch-object) objects, send a request to the batches endpoint without specifying a batch_id. To constrain the query response, you can also use a limit parameter.

<div class="grid" markdown>
<div markdown>

**Query parameters**

`after` ++"string"++

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `after=obj_foo` in order to fetch the next page of the list.

---

`limit` ++"integer"++

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the

**Returns**

A list of paginated [Batch](#the-batch-object) objects.

The status of a Batch object can be one of the following:

| Status          | Description                                                            |
|-----------------|------------------------------------------------------------------------|
| `validating`    | The input file is being validated.                                     |
| `failed`        | The input file failed the validation process.                          |
| `in_progress`   | The input file was successfully validated and the Batch is in progress.|
| `finalizing`    | The Batch job has completed and the results are being finalized.       |
| `completed`     | The Batch has completed and the results are ready.                     |
| `expired`       | The Batch was not completed within the 24-hour time window.            |
| `cancelling`    | The Batch is being cancelled (may take up to 10 minutes).              |
| `cancelled`     | The Batch was cancelled.                                               |

</div>
<div markdown>

=== "Curl"

    ```bash title="Example" 
    curl https://api.kluster.ai/v1/batches \
    -H "Authorization: Bearer $API_KEY"
    ```

=== "Python"

    ```Json title="Example"
    # Configure OpenAI client
    client = OpenAI(
        base_url="https://api.kluster.ai/v1",  # Change to "http://localhost:9000/api/v1" for local development
        api_key=my_api_key,  # Replace with your actual API key
    )

    print(client.batches.list(limit=2))
    ```

```Json title="Response"
    {
    "object": "list",
    "data": [
        {
        "id": "92aa978c-9dd1-49af-baa8-485ae6fb8019",
        "object": "batch",
        "endpoint": "/v1/chat/completions",
        "errors": null,
        "input_file_id": "kluster-input-file-123",
        "completion_window": "24h",
        "status": "Completed",
        "output_file_id": "kluster-output-file-123",
        "error_file_id": null,
        "created_at": "2024-10-07T16:53:53.046181Z",
        "in_progress_at": null,
        "expires_at": "2024-10-08T16:53:53.046181Z",
        "finalizing_at": null,
        "completed_at": null,
        "failed_at": null,
        "expired_at": null,
        "cancelling_at": null,
        "cancelled_at": null,
        "request_counts": {
            "total": 2,
            "completed": 2,
            "failed": 0
        },
        "metadata": {}
        },
    { ... },
    ],
    "first_id": "92aa978c-9dd1-49af-baa8-485ae6fb8019",
    "last_id": "0d29e406-51b2-4e5b-a9f4-6cb460eaeb59",
    "has_more": false,
    "count": 1,
    "page": 1,
    "page_count": -1,
    "items_per_page": 9223372036854775807
    }
```

</div>
</div>

---

## Cancelling a Batch Job

`post https://api.kluster.ai/v1/batches/{batch_id}/cancel`

To cancel an in-progress Batch job, send a cancel request to the batches endpoint specifying the `batch_id`.

<div class="grid" markdown>
<div markdown>

**Path parameters**

`batch_id` ++"string"++ <span class="required" markdown>++"Required"++</span>

The ID of the Batch to cancel.

**Returns**

The [Batch](#the-batch-object) object matching the specified ID.

</div>
<div markdown>

=== "Curl"

    ```bash title="Example"
    curl -s https://api.kluster.ai/v1/batches/$BATCH_ID/cancel \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -X POST
    ```

=== "Python"

    ```python title="Example"
    client = OpenAI(
        base_url="https://api.kluster.ai/v1",  
        api_key=my_api_key,  # Replace with your actual API key
    )
    client.batches.cancel("kluster_123")
    ```

```Json title="Response"
{
  "id": "642853d4-e816-4be2-8453-6ce6f0f00b9c",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "kluster-input-file-123",
  "completion_window": "24h",
  "status": "Cancelling",
  "output_file_id": "kluster-output-file-123",
  "error_file_id": null,
  "created_at": "2024-10-07T17:15:09.885223Z",
  "in_progress_at": null,
  "expires_at": "2024-10-08T17:15:09.885223Z",
  "finalizing_at": null,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": "2024-10-07T17:15:17.934748Z",
  "cancelled_at": null,
  "request_counts": {
    "total": 3,
    "completed": 3,
    "failed": 0
  },
  "metadata": {}
}
```

</div>
</div>

---

## Summary

You've now successfully completed a simple Batch use case by submitting a collection of Batch request input objects to the chat completion end point, monitored the job's progress, and downloaded the result of the Batch job. For further assiststance or to suggest future enhancements, please contact us at support@kluster.ai. 

## References

### The Batch Object

`id` ++"string"++

The ID of the Batch job.

---

`object` ++"string"++

The object type, which is always `batch`.

---

`endpoint` ++"string"++

The Kluster.ai API endpoint used by the batch.

---

`errors` ++"object"++

An object containing error information.

??? child "Show properties"

    `object` ++"string"++

    The object type, which is always `list`.

    ---

    `data` ++"array"++

    ??? child "Show properties"

        `code` ++"string"++
        
        An error code identifying the error type.

        ---

        `message` ++"string"++
        
        A human-readable message providing more details about the error.

        ---

        `param` ++"string or null"++
        
        The name of the parameter that caused the error, if applicable.

        ---

        `line` ++"integer or null"++
        
        The line number of the input file where the error occurred, if applicable.

---

`input_file_id` ++"string"++

The ID of the input file for the batch.

---

`completion_window` ++"string"++

The time frame within which the batch should be processed.

---

`status` ++"string"++

The current status of the batch.

---

`output_file_id` ++"string"++

The ID of the file containing the outputs of successfully executed requests.

---

`error_file_id` ++"string"++

The ID of the file containing the outputs of requests with errors.

---

`created_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch was created.

---

`in_progress_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch started processing.

---

`expires_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch will expire.

---

`finalizing_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch started finalizing.

---

`completed_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch was completed.

---

`failed_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch failed.

---

`expired_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch expired.

---

`cancelling_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch started cancelling.

---

`cancelled_at` ++"integer"++

The Unix timestamp (in seconds) for when the Batch was cancelled.

---

`request_counts` ++"object"++

The request counts for different statuses within the Batch.

??? child "Show properties"

    `total` ++"integer"++

    Total number of requests in the batch.

    ---

    `completed` ++"integer"++
    
    Number of requests that have been completed successfully.

    ---

    `failed` ++"integer"++
    
    Number of requests that have failed.

---

`metadata` ++"map"++

Set of 16 key-value pairs that can be attached to an object. This is useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long.

### The File Object

The File object represents a document that has been uploaded to Kluster.ai.

`id` ++"string"++

The file identifier referenced in the API endpoints.

---

`bytes` ++"integer"++

The size of the file in bytes.

---

`created_at` ++"integer"++

The Unix timestamp (in seconds) of when the file was created.

---

`filename` ++"string"++

The name of the file.

---

`object` ++"string"++

The object type which is always `file`.

---

`purpose` ++"string"++

The intended purpose of the file. `batch` and `batch_output` are the supported values.

---

`status` ++"string"++ *deprecated*

The current status of the file, which can be either uploaded, processed, or error.

---

`status_details` ++"string"++ *deprecated*

For details on why a fine-tuning training file failed validation, see the error field on fine_tuning.job.
