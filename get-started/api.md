---
title: kluster.ai API
description: The kluster.ai API getting started guide provides examples and instructions for submitting and managing Batch jobs using kluster.ai's OpenAI-compatible API.
---

# Start using the kluster.ai API

The kluster.ai API provides a straightforward way to work with Large Language Models (LLMs) at scale. It is compatible with OpenAI Python library and Batch API, making it easy to integrate into your existing workflows with minimal code changes.

Choose your preferred way to interact with the API:

- Use the OpenAI Python library (recommended)
- Make direct HTTP requests using curl
- Use any HTTP client that supports REST APIs

This guide provides copy-and-paste examples for both Python and curl, along with detailed explanations to help you get started quickly.

The OpenAI python library (version 1.0.0 or higher) is recommended, which can be installed with:

```bash
pip install "openai>=1.0.0"
```

## Get your API key

Navigate to the [platform.kluster.ai](http://platform.kluster.ai){target=\_blank} web app and select **API Keys** from the left-hand menu. Create a new API key by specifying the API key name. You'll need this for all API requests.

## Creating Batch jobs as JSON files

To create a Batch job, you'll need to:

1. Create a [JSON Lines](https://jsonlines.org/) file (`.jsonl`)
2. Add one or more batch requests to the file
3. Ensure each request includes:
    - A unique `custom_id`
    - The endpoint `/v1/chat/completions`
    - A request body containing:
        - Required: `model` - one of:
            - `klusterai/Meta-Llama-3.1-8B-Instruct-Turbo`
            - `klusterai/Meta-Llama-3.1-70B-Instruct-Turbo` 
            - `klusterai/Meta-Llama-3.1-405B-Instruct-Turbo`
        - Required: `messages` array with chat messages (system, user, or assistant roles)
        - Optional: Additional chat completion parameters like temperature, max_tokens, etc.

You can see the full list of available models programmatically using the [list supported models](#list-supported-models) endpoint.

<div class="grid" markdown>
<div markdown>

**Batch request input object**

`custom_id` ++"string"++

A developer-provided per-request ID that will be used to match outputs to inputs.

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

    A list of messages comprising the conversation so far. The `messages` object can be one of `system`, `user`, or `assistant`.
    
    ??? child "Show possible types"

        System message ++"object"++
        
        ??? child "Show properties"

            `content` ++"string or array"++

            The contents of the assistant message.  

            ---
           
            `role` ++"string or null"++ <span class="required" markdown>++"required"++</span>

            The role of the messages author, in this case, `assistant`.

            ---

            `name` ++"string"++ <span class="future" markdown>++"future enhancement"++</span>
            
            <!--
            An optional name for the participant. Provides the model information to differentiate between participants of the same role.
            -->

        ---

        User message ++"object"++

        ??? child "Show properties"

            `content` ++"string or array"++

            The contents of the assistant message.  

            ---
           
            `role` ++"string or null"++ <span class="required" markdown>++"required"++</span>

            The role of the messages author, in this case, `assistant`.

            ---

            `name` ++"string"++ <span class="future" markdown>++"future enhancement"++</span>
            
            <!--
            An optional name for the participant. Provides the model information to differentiate between participants of the same role.
            -->

        ---

        Assistant message ++"object"++

        ??? child "Show properties"

            `content` ++"string or array"++

            The contents of the assistant message.  

            ---

            `refusal` ++"string or null"++ <span class="future" markdown>++"future enhancement"++</span>
            
            <!--
            The refusal message by the assistant.
            -->
            
            ---

            `role` ++"string or null"++ <span class="required" markdown>++"required"++</span>

            The role of the messages author, in this case, `assistant`.

            ---

            `name` ++"string"++ <span class="future" markdown>++"future enhancement"++</span>
            
            <!--
            An optional name for the participant. Provides the model information to differentiate between participants of the same role.
            -->
            
            ---

            `audio` ++"object or null"++ <span class="future" markdown>++"future enhancement"++</span>
            
            <!--
            Data about a previous audio response from the model.
            -->
            
            ---

            `tool_calls` ++"array"++ <span class="future" markdown>++"future enhancement"++</span>
            
            <!--
            The tool calls generated by the model, such as function calls.
            -->
            
            ---

            `function_call` ++"object or null"++ *deprecated*

            Deprecated and replaced by `tool_calls`. 
        
        ---
            
        Tool message ++"object"++ <span class="future" markdown>++"future enhancement"++</span>

        ---

        Function message ++"object"++ *deprecated*

    ---

    `store` ++"boolean or null"++ <span class="future" markdown>++"future enhancement"++</span>
    
    <!--
    Whether or not to store the output of this chat completion request for use in our model distillation or evals products. Defaults to `false`.
    -->
  
    ---

    `metadata` ++"object or null"++ 
    <!--
    Developer-defined tags and values used for filtering completions in the dashboard.
    -->

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

    <!--
    This value is now deprecated in favor of `max_completion_tokens`.

    The maximum number of tokens that can be generated in the chat completion. This value can be used to control costs for text generated via API.
    -->

    ---

    `max_completion_tokens` ++"integer or null"++

    An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens.

    ---

    `n` ++"integer or null"++ <span class="future" markdown>++"future enhancement"++</span>

    <!--
    The number of chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs. Defaults to `1`.
    -->

    ---

    `modalities` ++"array or null"++ <span class="future" markdown>++"future enhancement"++</span>
    
    <!--
    Output types that you would like the model to generate for this request. Most models are capable of generating text, which is the default:

    `["text"]`

    The gpt-4o-audio-preview model can also be used to generate audio. To request that this model generate both text and audio responses, you can use:

    `["text", "audio"]`
    -->

    ---

    `audio` ++"object or null"++ <span class="future" markdown>++"future enhancement"++</span>
    
    <!--
    Parameters for audio output. Required when audio output is requested with modalities: ["audio"].
    -->

    ---

    `presence_penalty` ++"number or null"++

    Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. Defaults to `0`.

    ---

    `response_format` ++"object"++ <span class="future" markdown>++"future enhancement"++</span>
    
    <!--
    An object specifying the format that the model must output. Compatible with Meta-Llama-3.1-405B-Instruct-Turbo.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema.

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.
    -->

    ---

    `seed` ++"integer or null"++ 

    If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed.

    ---

    `service_tier` ++"string or null"++ <span class="future" markdown>++"future enhancement"++</span>
    
    <!--
    Specifies the latency tier to use for processing the request. Defaults to `null`. This parameter is relevant for customers subscribed to the scale tier service:

    - If set to `auto`, and the Project is Scale tier enabled, the system will utilize scale tier credits until they are exhausted
    - If set to `auto`, and the Project is not Scale tier enabled, the request will be processed using the default service tier with a lower uptime SLA and no latency guarantee
    - If set to `default`, the request will be processed using the default service tier with a lower uptime SLA and no latency guarantee
    - When not set, the default behavior is `auto`
    - When this parameter is set, the response body will include the `service_tier` utilized
    -->

    ---

    `stop` ++"string or array or null"++

    Up to four sequences where the API will stop generating further tokens. Defaults to `null`.

    ---

    `stream` ++"boolean or null"++

    If set, partial message deltas will be sent. Tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a `data: [DONE]` message. Defaults to `false`.

    ---

    `stream_options` ++"object or null"++ <span class="future" markdown>++"future enhancement"++</span>
    
    <!--
    Options for streaming response. Only set this when you set `stream: true`. Defaults to `null`
    -->

    ---

    `temperature` ++"number or null"++

    The sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. Defaults to `1`.

    It is generally recommended to alter this or `top_p` but not both.

    ---

    `top_p` ++"number or null"++

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. Defaults to `1`.

    It is generally recommended to alter this or `temperature` but not both.

    ---

    `tools` ++"array"++ <span class="future" markdown>++"future enhancement"++</span>
    
    <!--
    A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.
    -->

    ---

    `tool_choice` ++"string or object"++ <span class="future" markdown>++"future enhancement"++</span>
    
    <!--
    Controls which (if any) tool is called by the model.

    - `none` means the model will not call any tool and instead generates a message
    - `auto` means the model can pick between generating a message or calling one or more tools
    - `required` means the model must call one or more tools. Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool

    `none` is the default when no tools are present. `auto` is the default if tools are present.
    -->

    ---

    `parallel_tool_calls` ++"boolean"++ <span class="future" markdown>++"future enhancement"++</span>
   
    <!--
    Whether to enable [**parallel function calling**](https://platform.openai.com/docs/guides/function-calling/parallel-function-calling){target=\_blank} during tool use. Defaults to `true`.
    -->

    ---

    `user` ++"string"++

    <!--
    A unique identifier representing your end-user. It is recommended not to supply identifying information, hashing usernames, or email addresses instead.
    -->

    ---

    `function_call` ++"string or object"++ *deprecated*

    <!--
    This value is now deprecated in favor of `tool_choice`.

    Controls which (if any) function is called by the model.

    - `none` means the model will not call a function and instead generates a message
    - `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"name": "my_function"}` forces the model to call that function

    `none` is the default when no functions are present. `auto` is the default if functions are present.
    -->

    ---

    `functions` ++"array"++ *deprecated*

    <!--
    This value is now deprecated in favor of `tools`.

    A list of functions the model may generate JSON inputs for.
    -->

</div>
<div markdown>

=== "Python"

    ```python title="Example: collection of Batch requests"
    from openai import OpenAI
    client = OpenAI(
        base_url="https://api.kluster.ai/v1",  
        api_key="INSERT_API_KEY", # Replace with your actual API key
    )

    tasks = [{
            "custom_id": "request-1",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
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
                "model": "klusterai/Meta-Llama-3.1-70B-Instruct-Turbo",
                "messages": [
                    {"role": "system", "content": "You are a maths tutor."},
                    {"role": "user", "content": "Explain the Pythagorean theorem."},
                ],
                "max_tokens": 1000,
            },
        }
        # Additional tasks can be added here
    ]

    # Save tasks to a JSONL file (newline-delimited JSON)
    file_name = "mybatchtest.jsonl"
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")
    ```

=== "curl"

    ```bash title="Example: collection of Batch requests"
    cat << EOF > mybatchtest.jsonl
    {"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of Argentina?"}],"max_tokens":1000}}
    {"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "klusterai/Meta-Llama-3.1-70B-Instruct-Turbo", "messages": [{"role": "system", "content": "You are an experienced maths tutor."}, {"role": "user", "content": "Explain the Pythagorean theorem."}],"max_tokens":1000}}
    {"custom_id": "request-3", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "klusterai/Meta-Llama-3.1-405B-Instruct-Turbo", "messages": [{"role": "system", "content": "You are an astronomer."}, {"role": "user", "content": "What is the distance between the Earth and the Moon"}],"max_tokens":1000}}
    EOF
    ```

</div>
</div>

---

## Uploading Batch job files

Upload your [JSON Lines](https://jsonlines.org/){target=\_blank} file to the `files` endpoint. The response will contain a `id` field - save this value as you'll need it in the next step where it's referred to as `input_file_id`. You can also view all your uploaded files in the [Files tab](https://platform.kluster.ai/files) of the kluster.ai platform.

<div class="grid" markdown>
<div markdown>

**Request**

`file` ++"file"++ <span class="required" markdown>++"required"++</span>

The File object (not file name) to be uploaded.

---

`purpose` ++"string"++ <span class="required" markdown>++"required"++</span>

The intended purpose of the uploaded file. Use `batch` for the Batch API.

**Returns**

The uploaded File object.

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

=== "Python"

    ```python title="Example request"

    batch_input_file = client.files.create(
        file=open(file_name, "rb"),
        purpose="batch"
    )

    batch_input_file.to_dict()
    ```

=== "curl"

    ```bash title="Example request"
    curl -s https://api.kluster.ai/v1/files \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: multipart/form-data" \
        -F "file=@mybatchtest.jsonl" \
        -F "purpose=batch"
    ```

```Json title="Response"
{
  "id": "myfile-123",
  "bytes": 2797,
  "created_at": "1698959748",
  "filename": "mybatchtest.jsonl",
  "object": "file",
  "purpose": "batch"
}
```

</div>
</div>

---

## Submit your Batch job

`POST https://api.kluster.ai/v1/batches`

Next, to submit a Batch job, you invoke the `batches` endpoint using the `input_file_id` from the previous step.

<div class="grid" markdown>
<div markdown>

**Request**

`input_file_id` ++"string"++ <span class="required" markdown>++"required"++</span>

The ID of an uploaded file that contains requests for the new Batch.

Your input file must be formatted as a [JSONL file](https://jsonlines.org/){target=\_blank}, and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests and currently a maximum of 6GB per file.

---

`endpoint` ++"string"++ <span class="required" markdown>++"required"++</span>

The endpoint to be used for all requests in the Batch. Currently, only `/v1/chat/completions` is supported.

---

`completion_window` ++"string"++ <span class="required" markdown>++"required"++</span>

The time frame within which the Batch should be processed. Currently, only **24h** is supported.

---

`metadata` ++"Object or null"++

Custom metadata for the Batch.

---

**Returns**

The created Batch object.

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

---

`metadata` ++"Object or null"++

<!--
Set of 16 key-value pairs that can be attached to an object. This is useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long, and values can be a maximum of 512 characters long.
--> 

</div>
<div markdown>

=== "Python"

    ```python title="Example request"

    batch_request = client.batches.create(
        input_file_id=batch_input_file.id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )

    batch_request.to_dict()
    ```

=== "curl"

    ```bash title="Example request"
    curl -s https://api.kluster.ai/v1/batches \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
        "input_file_id": "myfile-123",
        "endpoint": "/v1/chat/completions",
        "completion_window": "24h"
        }'
    ```

```Json title="Response"
{
	"id": "mybatch-123",
	"completion_window": "24h",
	"created_at": 1732714585,
	"endpoint": "/v1/chat/completions",
	"input_file_id": "myfile-123",
	"object": "batch",
	"status": "validating",
	"cancelled_at": null,
	"cancelling_at": null,
	"completed_at": null,
	"error_file_id": null,
	"errors": null,
	"expired_at": null,
	"expires_at": 1732800985,
	"failed_at": null,
	"finalizing_at": null,
	"in_progress_at": null,
	"metadata": {},
	"output_file_id": null,
	"request_counts": {
		"completed": 0,
		"failed": 0,
		"total": 0
	}
}
```

</div>
</div>

---

## Monitor job progress

`GET https://api.kluster.ai/v1/batches/{batch_id}`

To monitor your Batch job's progress, make periodic requests to the `batches` endpoint using your `batch_id` to check its status. The job is complete when the `status` field is `"completed"`. You can also monitor jobs in the [Batch tab](https://platform.kluster.ai/batch) of the kluster.ai platform UI.

<div class="grid" markdown>
<div markdown>

**Path parameters**

`batch_id` ++"string"++ <span class="required" markdown>++"required"++</span>

The ID of the Batch to retrieve.

---

**Returns**

The Batch object matching the specified `id`.

</div>
<div markdown>

=== "Python"

    ```python title="Example request"
    import time

    # Poll the batch status until it's complete
    while True:
        batch_status = client.batches.retrieve(batch_request.id)
        print("Batch status: {}".format(batch_status.status))
        print(
            f"Completed tasks: {batch_status.request_counts.completed} / {batch_status.request_counts.total}"
        )

        if batch_status.status.lower() in ["completed", "failed", "cancelled"]:
            break

        time.sleep(10)  # Wait for 10 seconds before checking again

    batch_status.to_dict()
    ```

=== "curl"

    ```bash title="Example request"
    curl -s https://api.kluster.ai/v1/batches/mybatch-123 \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: application/json"
    ```

```Json title="Response"
{
  "id": "mybatch-123",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "myfile-123",
  "completion_window": "24h",
  "status": "completed",
  "output_file_id": "myfile-123-output",
  "error_file_id": null,
  "created_at": "1730821906",
  "in_progress_at": null,
  "expires_at": "1730821906",
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

## Retrieve results

`GET https://api.kluster.ai/v1/files/{output_file_id}/content`

To retrieve the content of your Batch jobs output file, send a request to the `files` endpoint specifying the `output_file_id`. The output file will be a JSONL file, where each line contains the `custom_id` from your input file request, and the corresponding response.


<div class="grid" markdown>
<div markdown>

**Path parameters**

`file_id` ++"string"++ <span class="required" markdown>++"required"++</span>

The ID of the file to use for this request

---

**Returns**

The Batch object matching the specified file ID.

`id` ++"string"++

A unique identifier for the chat completion.

---

`custom_id` ++"string"++

A developer-provided per-request ID that will be used to match outputs to inputs.

---

`response` ++"object or null"++

??? child "Show properties"

    `status_code` ++"integer"++

    The HTTP status code of the response.

    ---

    `request_id` ++"string"++

    A unique identifier for the request. Please include this request ID when contacting support.

    ---

    `body` ++"map"++

    The JSON body of the response. In this case, the Chat Completion object.

    ??? child "Chat Completion object"

        `id` ++"string"++

        A unique identifier for the chat completion.

        ---

        `choices` ++"array"++

        A list of chat completion choices. <!-- Can be more than one if `n` is greater than 1.-->

        ??? child "Show properties"

            `finish_reason` ++"string"++

            The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence, or length if the maximum number of tokens specified in the request was reached.

            ---

            `index` ++"integer"++

            The index of the choice in the list of choices.

            ---

            `message` ++"object"++

            A chat completion message generated by the model.

            ??? child "Show properties"

                `content` ++"string or null"++

                The contents of the message.

                ---

                `refusal` ++"string or null"++ <span class="future" markdown>++"future enhancement"++</span>

                ---

                `tool_calls` ++"array"++ <span class="future" markdown>++"future enhancement"++</span>

                ---
                
                `role` ++"string"++

                The role of the author of this message.

                ---

                `functional_call` ++"object"++ *deprecated*

                ---

                `audio` ++"object or null"++ <span class="future" markdown>++"future enhancement"++</span>

            ---

            `log_probs` ++"object or null"++

            Log probability information for the choice.

            ??? child "Show properties"

                `content` ++"array or null"++

                A list of message content tokens with log probability information.

                ??? child "Show properties"

                    `token` ++"string"++

                    The token.

                    ---

                    `logprob` ++"number"++

                    The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

                    ---

                    `bytes` ++"array or null"++

                    A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. `null` if there is no bytes representation for the token.

                    ---

                    `top_logprobs` ++"array or null"++

                    The associated log probability for each token.

                    ??? child "Show properties"
                        
                        `token` ++"string"++

                        The token.

                        ---

                        `logprob` ++"number"++

                        The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

                        ---

                        `bytes` ++"array or null"++

                        A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. `null` if there is no bytes representation for the token.

                ---

                `refusal` ++"array or null"++ <span class="future" markdown>++"future enhancement"++</span>

        ---

        `created` ++"integer"++

        The Unix timestamp (in seconds) of when the chat completion was created.

        ---

        `model`  ++"string"++
        
        The model used for the chat completion.

        ---

        `service_tier` ++"string or null"++ <span class="future" markdown>++"future enhancement"++</span>

        ---

        `system_fingerprint` ++"string"++ <span class="future" markdown>++"future enhancement"++</span>

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

            `completion_token_details` ++"null"++ <span class="not-supported" markdown>++"Not supported"++</span>

            ---

            `prompt_token_details` ++"object"++ <span class="future" markdown>++"future enhancement"++</span>

---

`error` ++"object or null"++

For requests that failed with a non-HTTP error, this will contain more information on the cause of the failure.

??? child "Show properties"

    `code` ++"string"++ 
   
    A machine-readable error code.
   
    ---

    `message` ++"string"++
   
    A human-readable error message. 

</div>
<div markdown>

=== "Python"

    ```python title="Example request"
    # Check if the batch completed successfully
    if batch_status.status.lower() == "completed":
        # Retrieve the results
        result_file_id = batch_status.output_file_id
        results = client.files.content(result_file_id).content

        # Save results to a file
        result_file_name = "batch_results.jsonl"
        with open(result_file_name, "wb") as file:
            file.write(results)
        print(f"Results saved to {result_file_name}")
    else:
        print(f"Batch failed with status: {batch_status.status}")
    ```

=== "curl"

    ```bash title="Example request"
    curl -s https://api.kluster.ai/v1/files/kluster-output-file-123/content \
        -H "Authorization: Bearer $API_KEY" > batch_output.jsonl
    ```

</div>
</div>

---

## List all Batch jobs

`GET https://api.kluster.ai/v1/batches`

To list all of your Batch jobs, send a request to the `batches` endpoint without specifying a `batch_id`. To constrain the query response, you can also use a limit parameter.

<div class="grid" markdown>
<div markdown>

**Query parameters**

`after` ++"string"++

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `after=obj_foo` in order to fetch the next page of the list.

---

`limit` ++"integer"++

A limit on the number of objects to be returned. Limit can range between 1 and 100. Default is 20.

---

**Returns**

A list of paginated Batch objects.

The status of a Batch object can be one of the following:

<style>
table th:first-child {
    width: 120px;
}
</style>

| Status        | Description                                                             |
|---------------|-------------------------------------------------------------------------|
| `validating`  | The input file is being validated.                                      |
| `failed`      | The input file failed the validation process.                           |
| `in_progress` | The input file was successfully validated and the Batch is in progress. |
| `finalising`  | The Batch job has completed and the results are being finalized.        |
| `completed`   | The Batch has completed and the results are ready.                      |
| `expired`     | The Batch was not completed within the 24-hour time window.             |
| `cancelling`  | The Batch is being cancelled (may take up to 10 minutes).               |
| `cancelled`   | The Batch was cancelled.                                                |

</div>

<div markdown>

=== "Python"

    ```python title="Example request"
    from openai import OpenAI

    # Configure OpenAI client
    client = OpenAI(
        base_url="https://api.kluster.ai/v1", 
        api_key="INSERT_API_KEY" # Replace with your actual API key
    )

    client.batches.list(limit=2).to_dict()
    ```

=== "curl"

    ```bash title="Example request" 
    curl -s https://api.kluster.ai/v1/batches \
        -H "Authorization: Bearer $API_KEY"
    ```

```Json title="Response"
{
"object": "list",
"data": [
    {
    "id": "mybatch-123",
    "object": "batch",
    "endpoint": "/v1/chat/completions",
    "errors": null,
    "input_file_id": "myfile-123",
    "completion_window": "24h",
    "status": "completed",
    "output_file_id": "myfile-123-output",
    "error_file_id": null,
    "created_at": "1730821906",
    "in_progress_at": null,
    "expires_at": "1730821906",
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
"first_id": "mybatch-123",
"last_id": "mybatch-789",
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

## Cancelling a Batch job

`POST https://api.kluster.ai/v1/batches/{batch_id}/cancel`

To cancel a Batch job that is currently in progress, send a request to the `cancel` endpoint with your `batch_id`. Note that cancellation may take up to 10 minutes to complete, during which time the status will show as `cancelling`.

<div class="grid" markdown>
<div markdown>

**Path parameters**

`batch_id` ++"string"++ <span class="required" markdown>++"required"++</span>

The ID of the Batch to cancel.

---

**Returns**

The Batch object matching the specified ID.

</div>
<div markdown>

=== "Python"

    ```python title="Example"
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.kluster.ai/v1",  
        api_key="INSERT_API_KEY" # Replace with your actual API key
    )
    client.batches.cancel("mybatch-123") # Replace with your batch id
    ```

=== "curl"

    ```bash title="Example"
    curl -s https://api.kluster.ai/v1/batches/$BATCH_ID/cancel \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: application/json" \
        -X POST
    ```

```Json title="Response"
{
  "id": "mybatch-123",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "myfile-123",
  "completion_window": "24h",
  "status": "cancelling",
  "output_file_id": "myfile-123-output",
  "error_file_id": null,
  "created_at": "1730821906",
  "in_progress_at": "1730821911",
  "expires_at": "1730821906",
  "finalizing_at": null,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": "1730821906",
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


## List supported models

You can use this endpoint to retrieve a list of all available models for the kluster.ai API. Currently supported models:

- `klusterai/Meta-Llama-3.1-8B-Instruct-Turbo`
- `klusterai/Meta-Llama-3.1-70B-Instruct-Turbo`
- `klusterai/Meta-Llama-3.1-405B-Instruct-Turbo`

<div class="grid" markdown>
<div markdown>

**Request**

`GET https://api.kluster.ai/v1/models`

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

=== "Python"

    ```python title="Example request"
    from openai import OpenAI

    client = OpenAI(
        base_url="http://api.kluster.ai/v1",
        api_key="INSERT_API_KEY" # Replace with your actual API key
    )

    client.models.list().to_dict()
    ```

=== "curl"

    ```bash title="Example request"
    curl https://api.kluster.ai/v1/models \
        -H "Authorization: Bearer $API_KEY" 
    ```

```Json title="Response"
{
  "object": "list",
  "data": [
    {
      "id": "klusterai/Meta-Llama-3.1-405B-Instruct-Turbo",
      "object": "model",
      "created": 1731336418,
      "owned_by": "klusterai"
    },
    {
      "id": "klusterai/Meta-Llama-3.1-70B-Instruct-Turbo",
      "object": "model",
      "created": 1731336610,
      "owned_by": "klusterai"
    },
    {
      "id": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
      "object": "model",
      "created": 1731336610,
      "owned_by": "klusterai"
    }
  ]
}
```

</div>
</div>

---

## Summary

Congratulations! You now have all the tools needed to work with the kluster.ai Batch API. In this guide, you've learned how to:

- Prepare and submit Batch jobs with structured request inputs
- Track your jobs' progress in real-time
- Retrieve and handle job results
- View and manage your Batch jobs
- Cancel jobs when needed
- View supported models

The kluster.ai Batch API is designed to efficiently and reliably handle your large-scale LLM workloads. Do you have questions or suggestions? The [support](mailto:support@kluster.ai) team would love to hear from you.
