---

title: Perform batch inference jobs
description: This guide provides examples and instructions on how to create, submit, retrieve, and manage batch inference jobs using kluster.ai's OpenAI-compatible API.
---

# Perform batch inference jobs

## Overview

This guide provides examples and instructions on how to create, submit, retrieve, and manage batch inference jobs using the [kluster.ai](https://platform.kluster.ai/){target=\_blank} API. You will find guidance through the entire process from preparing your data, selecting a model, and submitting your batch job through retrieving your results.
 
## Prerequisites

This guide assumes familiarity with basic Python and Large Language Model (LLM) development. Before getting started, make sure you have:

- **An active kluster API key** - if you don't already have one, see the [Get an API key]

Before proceeding, ensure you're familiar with the **JSONL (JSON Lines)** format, the required input format for performing batch inferences with the kluster.ai API.

## Supported models

Batch inference using kluster.ai supports the following models:

--8<-- 'text/batch-models.md'

In addition, you can see the complete list of available models programmatically using the [list supported models](/api-reference/reference/#list-supported-models){target=\_blank} endpoint.

## Batch job workflow overview

Working with batch jobs in the kluster.ai API involves the following steps:

1. **Create batch job file** - prepare a JSON Lines file containing one or more chat completion requests to be executed in the batch
2. **Upload batch job file** - upload the file to kluster.ai to receive a unique file ID
3. **Start the batch job** - initiate a new batch job using the file ID
4. **Monitor job progress** - track the status of your batch job to ensure successful completion
5. **Retrieve results** - once the job finishes, access and process the results as needed

This streamlined process enables efficient handling of large-scale requests.

In addition to these core steps, this guide will give you hands-on experience with:

- **Cancel a batch job** - cancel an ongoing batch job if necessary before it completes
- **List all batch jobs** - review all of your batch jobs

## Create batch jobs as JSON files

To begin the batch job workflow, you'll need to assemble your batch requests and add them to a [JSON Lines](https://jsonlines.org/) file (`.jsonl`).

Each request needs to include the following arguments:

- `custom_id` ++"string"++ - a unique request ID that will be used to match outputs to inputs
- `method` ++"string"++ - the HTTP method to be used for the request. Currently, only `POST` is supported
- `url` ++"string"++ -  the `/v1/chat/completions` endpoint
- `body` ++"object"++ - a request body containing:
    - `model` ++"string"++ <span class="required" markdown>++"required"++</span> - name of one of the [supported models](#supported-models)
    - `messages` ++"array"++ <span class="required" markdown>++"required"++</span> - a list of chat messages (`system`, `user`, or `assistant` roles)
    - Any optional [chat completion parameters](/api-reference/reference/#create-chat-completion){target=\_blank}, such as `temperature`, `max_completion_tokens`, etc.

The following examples generate requests and save them in a JSONL file, which is ready for upload and processing.

=== "Python"

 ```python
    from openai import OpenAI
    import json

 client = OpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key="INSERT_API_KEY",  # Replace with your actual API key
 )

 requests = [
 {
            "custom_id": "request-1",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
                "messages": [
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "What is the capital of Argentina?"},
 ],
                "max_completion_tokens": 1000,
 },
 },
 {
            "custom_id": "request-2",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
                "messages": [
 {"role": "system", "content": "You are a maths tutor."},
 {"role": "user", "content": "Explain the Pythagorean theorem."},
 ],
                "max_completion_tokens": 1000,
 },
 },
 {
            "custom_id": "request-4",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
                "messages": [
 {
                        "role": "system",
                        "content": "You are a multilingual, experienced maths tutor.",
 },
 {
                        "role": "user",
                        "content": "Explain the Pythagorean theorem in Spanish",
 },
 ],
                "max_completion_tokens": 1000,
 },
 },
        # Additional tasks can be added here
 ]

    # Save tasks to a JSONL file (newline-delimited JSON)
 file_name = "mybatchtest.jsonl"
    with open(file_name, "w") as file:
        for request in requests:
 file.write(json.dumps(request) + "\n")
 ```

=== "curl"

 ```bash
    cat << EOF > mybatchtest.jsonl
 {"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of Argentina?"}],"max_completion_tokens":1000}}
 {"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo", "messages": [{"role": "system", "content": "You are an experienced maths tutor."}, {"role": "user", "content": "Explain the Pythagorean theorem."}],"max_completion_tokens":1000}}
 {"custom_id": "request-3", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "klusterai/Meta-Llama-3.1-405B-Instruct-Turbo", "messages": [{"role": "system", "content": "You are an astronomer."}, {"role": "user", "content": "What is the distance between the Earth and the Moon"}],"max_completion_tokens":1000}}
 {"custom_id": "request-4", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo", "messages":[{"role": "system", "content": "You are a multilingual, experienced maths tutor."}, {"role": "user", "content": "Explain the Pythagorean theorem in Spanish"}],"max_completion_tokens":1000}}
 EOF
 ```

## Upload batch job files

Upload your [JSON Lines](https://jsonlines.org/){target=\_blank} file to the `files` endpoint along with the intended purpose of the upload. For batch jobs, set the `purpose` value to `"batch"`.

The response will contain an `id` field; save this value as you'll need it in the next step, where it's referred to as `input_file_id`.

!!! note
 You can also view all your uploaded files in the [**Files** tab](https://platform.kluster.ai/files){target=\_blank} of the kluster.ai platform.

=== "Python"

 ```python title="Example request"

 batch_input_file = client.files.create(
        file=open(file_name, "rb"),
        purpose="batch"
 )
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
    "created_at": "1733832768",
    "filename": "mybatchtest.jsonl",
    "object": "file",
    "purpose": "batch"
}
```

## Submit a batch job

Next, submit a batch job by calling the `batches` endpoint and providing the `id` of the uploaded batch job file (from the previous section) as the [`input_file_id`, and additional parameters](/api-reference/reference/#submit-a-batch-job){target=\_blank} to specify the job's configuration.

The response includes an `id` that can be used to monitor the job's progress, as demonstrated in the next section.

=== "Python"

 ```python title="Example request"

 batch_request = client.batches.create(
        input_file_id=batch_input_file.id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
 )
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
    "created_at": 1733832777,
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
    "expires_at": 1733919177,
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

## Monitor job progress

To monitor your batch job's progress, make periodic requests to the `batches` endpoint using the `id` of the batch request (from the previous section) as the [`batch_id`](/api-reference/reference/#retrieve-a-batch){target=\_blank} to check its status. The job is complete when the `status` field returns `"completed"`.

To see a complete list of the supported statuses, refer to the [Retrieve a batch](/api-reference/reference/#retrieve-a-batch){target=\_blank} API reference page.

!!! note
 You can also monitor jobs in the [**Batch** tab](https://platform.kluster.ai/batch) of the kluster.ai platform UI.

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

 time.sleep(10)  # Wait for 10 seconds before checking again
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
    "created_at": "1733832777",
    "in_progress_at": "1733832777",
    "expires_at": "1733919177",
    "finalizing_at": "1733832781",
    "completed_at": "1733832781",
    "failed_at": null,
    "expired_at": null,
    "cancelling_at": null,
    "cancelled_at": null,
    "request_counts": {
        "total": 4,
        "completed": 4,
        "failed": 0
 },
    "metadata": {}
}
```

## Retrieve results

To retrieve the content of your batch jobs output file, send a request to the `files` endpoint specifying the `output_file_id`, which is returned from querying the batch's status (from the previous section).

The output file will be a JSONL file, where each line contains the `custom_id` from your input file request and the corresponding response.

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

## List all batch jobs

To list all of your batch jobs, send a request to the `batches` endpoint without specifying a `batch_id`. To constrain the query response, you can also use a `limit` parameter.

=== "Python"

 ```python title="Example request"
    from openai import OpenAI

    # Configure OpenAI client
 client = OpenAI(
        base_url="https://api.kluster.ai/v1", 
        api_key="INSERT_API_KEY" # Replace with your actual API key
 )

    print(client.batches.list(limit=2).to_dict())
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
    "created_at": "1733832777",
    "in_progress_at": "1733832777",
    "expires_at": "1733919177",
    "finalizing_at": "1733832781",
    "completed_at": "1733832781",
    "failed_at": null,
    "expired_at": null,
    "cancelling_at": null,
    "cancelled_at": null,
    "request_counts": {
        "total": 4,
        "completed": 4,
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

## Cancel a batch job

To cancel a batch job currently in progress, send a request to the `cancel` endpoint with your `batch_id`. Note that cancellation may take up to 10 minutes to complete, when the status will show as `cancelling`. Once complete, the status will show as `cancelled`.

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

## Summary

You now have all the tools to work with the kluster.ai batch API. In this guide, you've learned how to:

- Prepare and submit batch jobs with structured request inputs
- Track your job's progress in real-time
- Retrieve and handle job results
- View and manage your batch jobs
- Cancel jobs when needed
- View supported models

The kluster.ai batch API is designed to efficiently and reliably handle your large-scale LLM workloads. Do you have questions or suggestions? The [support](mailto:support@kluster.ai){target=\_blank} team would love to hear from you.
