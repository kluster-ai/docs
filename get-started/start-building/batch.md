---

title: Perform batch inference jobs
description: This guide provides examples and instructions on how to create, submit, retrieve, and manage batch inference jobs using kluster.ai's OpenAI-compatible API.
---

# Perform batch inference jobs

## Overview

This guide provides examples and instructions on how to create, submit, retrieve, and manage batch inference jobs using the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. You will find guidance about preparing your data, selecting a model, submitting your batch job, and retrieving your results. Please make sure you check the [API request limits](/get-started/models/#api-request-limits){target=\_blank}.

## Prerequisites

This guide assumes familiarity with Large Language Model (LLM) development and OpenAI libraries. Before getting started, make sure you have:

--8<-- 'text/kluster-api-onboarding.md'
- **A virtual Python environment** - (optional) recommended for developers using Python. It helps isolate Python installations in a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=\_blank} to reduce the risk of environment or package conflicts between your projects
- **Required Python libraries** - install the following Python libraries:
    - [**OpenAI Python API library**](https://pypi.org/project/openai/) - to access the `openai` module
    - [**`getpass`**](https://pypi.org/project/getpass4/) - to handle API keys safely
- **A basic understanding of** [**JSON Lines (JSONL)**](https://jsonlines.org/){target=\_blank} - JSONL is the required text input format for performing batch inferences with the kluster.ai API

If you plan to use cURL via the CLI, you can export your kluster.ai API key as a variable:

```bash
export API_KEY=INSERT_API_KEY
```

## Supported models

Please visit the [Models](/get-started/models/){target=\_blank} page to learn more about all the models supported by the kluster.ai batch API.

In addition, you can see the complete list of available models programmatically using the [list supported models](/api-reference/reference/#list-supported-models){target=\_blank} endpoint.

## Batch job workflow overview

Working with batch jobs in the kluster.ai API involves the following steps:

1. **Create batch job file** - prepare a JSON Lines file containing one or more chat completion requests to execute in the batch
2. **Upload batch job file** - upload the file to kluster.ai to receive a unique file ID
3. **Start the batch job** - initiate a new batch job using the file ID
4. **Monitor job progress** - track the status of your batch job to ensure successful completion
5. **Retrieve results** - once the job finishes, access and process the results as needed

In addition to these core steps, this guide will give you hands-on experience to:

- **Cancel a batch job** - cancel an ongoing batch job before it completes
- **List all batch jobs** - review all of your batch jobs

!!! warning
    For the free tier, the maximum number of batch requests (lines in the JSONL file) must be less than {{ batch.max_lines_free }}, and each file must not exceed {{ batch.max_size }}. For the standard tier, there is no limit to the number of batch requests, but the maximum batch file size is {{ batch.max_size }} per file.

## Quickstart snippets

The following code snippets provide a full end-to-end batch inference example for different models supported by kluster.ai. You can simply copy and paste the snippet into your local environment.

### Python

To use these snippets, run the Python script and enter your kluster.ai API key when prompted.

??? example "DeepSeek-R1"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-deepseek-r1.py'
    ```

??? example "DeepSeek-R1-0528"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-deepseek-r1-0528.py'
    ```

??? example "DeepSeek-V3-0324"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-deepseek-v3-0324.py'
    ```

??? example "Gemma 3 27B"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-gemma-3-27b-it.py'
    ```

??? example "Magistral Small"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-magistral-small-2506.py'
    ```

??? example "Meta Llama 3.1 8B"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-meta-llama-3-1-8b-instruct-turbo.py'
    ```

??? example "Meta Llama 3.3 70B"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-meta-llama-3-3-70b-instruct-turbo.py'
    ```

??? example "Meta Llama 4 Maverick"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-llama-4-maverick-17b-128e-instruct-fp8.py'
    ```

??? example "Meta Llama 4 Scout"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-llama-4-scout-17b-16e-instruct.py'
    ```

??? example "Mistral NeMo"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-mistral-nemo-instruct-2407.py'
    ```

??? example "Mistral Small"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-mistral-small-24b-instruct-2501.py'
    ```

??? example "Qwen2.5-VL 7B"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-qwen2-5-vl-7b-instruct.py'
    ```

??? example "Qwen3-235B-A22B"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-qwen3-235b-a22b-fp8.py'
    ```
### CLI

Similarly, the following curl commands showcase how to easily send a chat completion request to kluster.ai for the different supported models. This example assumes you've exported your kluster.ai API key as the variable `API_KEY`.

??? example "DeepSeek-R1"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-deepseek-r1.md'
    ```

??? example "DeepSeek-R1-0528"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-deepseek-r1-0528.md'
    ```

??? example "DeepSeek-V3-0324"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-deepseek-v3-0324.md'
    ```

??? example "Gemma 3 27B"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-gemma-3-27b-it.md'
    ```

??? example "Magistral Small"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-magistral-small-2506.md'
    ```

??? example "Meta Llama 3.1 8B"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-meta-llama-3-1-8b-instruct-turbo.md'
    ```

??? example "Meta Llama 3.3 70B"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-meta-llama-3-3-70b-instruct-turbo.md'
    ```

??? example "Meta Llama 4 Maverick"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-llama-4-maverick-17b-128e-instruct-fp8.md'
    ```

??? example "Meta Llama 4 Scout"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-llama-4-scout-17b-16e-instruct.md'
    ```

??? example "Mistral NeMo"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-mistral-nemo-instruct-2407.md'
    ```

??? example "Mistral Small"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-mistral-small-24b-instruct-2501.md'
    ```

??? example "Qwen2.5-VL 7B"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-qwen2-5-vl-7b-instruct.md'
    ```

??? example "Qwen3-235B-A22B"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-qwen3-235b-a22b-fp8.md'
    ```


## Batch inference flow

This section details the batch inference process using the kluster.ai API and DeepSeek R1 model, but you can adapt it to any of the [supported models](/get-started/models/){target=\_blank}.

### Create batch jobs as JSON files

To begin the batch job workflow, you'll need to assemble your batch requests and add them to a [JSON Lines](https://jsonlines.org/){target=\_blank} file (`.jsonl`).

Each request must include the following arguments:

- `custom_id` ++"string"++ - a unique request ID to match outputs to inputs
- `method` ++"string"++ - the HTTP method to use for the request. Currently, only `POST` is supported
- `url` ++"string"++ -  the `/v1/chat/completions` endpoint
- `body` ++"object"++ - a request body containing:
    - `model` ++"string"++ <span class="required" markdown>++"required"++</span> - name of one of the [supported models](/get-started/models/){target=\_blank}
    - `messages` ++"array"++ <span class="required" markdown>++"required"++</span> - a list of chat messages (`system`, `user`, or `assistant` roles, and also `image_url` for images)
    - Any optional [chat completion parameters](/api-reference/reference/#create-chat-completion){target=\_blank}, such as `temperature`, `max_completion_tokens`, etc.

!!! tip
    You can use a different model for each request you submit.

The following examples generate requests and save them in a JSONL file, which is ready to be uploaded for processing.

=== "Python"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-01.py:01:78'
    ```

=== "CLI"

    ```bash
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-02.txt'
    ```

!!! warning
    For the free tier, the maximum number of batch requests (lines in the JSONL file) must be less than {{ batch.max_lines_free }}, and each file must not exceed {{ batch.max_size }}. For the standard tier, there is no limit to the number of batch requests, but the maximum batch file size is {{ batch.max_size }} per file. 

### Upload batch job files

After you've created the JSON Lines file, you need to upload it using the `files` endpoint along with the intended purpose. Consequently, you need to set the `purpose` value to `"batch"` for batch jobs.

The response will contain an `id` field; save this value as you'll need it in the next step, where it's referred to as `input_file_id`. You can view your uploaded files in the [**Files** tab](https://platform.kluster.ai/files){target=\_blank} of the kluster.ai platform.

Use the following command examples to upload your batch job files:

=== "Python"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-01.py:79:81'
    ```

=== "curl"

    ```bash
    curl -s https://api.kluster.ai/v1/files \
        -H "Authorization: Bearer $API_KEY" \
        -H "Content-Type: multipart/form-data" \
        -F "file=@my_batch_request.jsonl" \
        -F "purpose=batch"
    ```


```Json title="Response"
{
    "id": "myfile-123",
    "bytes": 2797,
    "created_at": "1733832768",
    "filename": "my_batch_request.jsonl",
    "object": "file",
    "purpose": "batch"
}
```

!!! warning
    Remember that the maximum file size permitted is {{ batch.max_size }}.

### Submit a batch job

Next, submit a batch job by calling the `batches` endpoint and providing the `id` of the uploaded batch job file (from the previous section) as the [`input_file_id`, and additional parameters](/api-reference/reference/#submit-a-batch-job){target=\_blank} to specify the job's configuration.

The response includes an `id` that can be used to monitor the job's progress, as demonstrated in the next section.

You can use the following snippets to submit your batch job:

=== "Python"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-01.py:82:88'
    ```

=== "curl"

    ```bash
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

### Monitor job progress

You can make periodic requests to the `batches` endpoint to monitor your batch job's progress. Use the `id` of the batch request from the preceding section as the [`batch_id`](/api-reference/reference/#retrieve-a-batch){target=\_blank} to check its status. The job is complete when the `status` field returns `"completed"`. You can also monitor jobs in the [**Batch** tab](https://platform.kluster.ai/batch) of the kluster.ai platform UI.

To see a complete list of the supported statuses, refer to the [Retrieve a batch](/api-reference/reference/#retrieve-a-batch){target=\_blank} API reference page.

You can use the following snippets to monitor your batch job:


=== "Python"

    ```python
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-01.py:89:101'
    ```

=== "curl"

    ```bash
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

### Retrieve results

To retrieve the content of your batch jobs output file, send a request to the `files` endpoint specifying the `output_file_id`, which is returned from querying the batch's status (from the previous section).

The output file will be a JSONL file, where each line contains the `custom_id` from your input file request and the corresponding response.

You can use the following snippets to retrieve the results from your batch job:

=== "Python"

    ```python 
    --8<-- 'code/get-started/start-building/batch/batch-jsonl-01.py:102:'
    ```

=== "curl"

    ```bash
    curl -s https://api.kluster.ai/v1/files/kluster-output-file-123/content \
        -H "Authorization: Bearer $API_KEY" > batch_results.jsonl
    ```

??? code "View the complete script"

    === "Python"

        ```python
        --8<-- 'code/get-started/start-building/batch/batch-jsonl-01.py'
        ```

## List all batch jobs

To list all of your batch jobs, send a request to the `batches` endpoint without specifying a `batch_id`. To constrain the query response, you can also use a `limit` parameter.

You can use the following snippets to list all of your batch jobs:

=== "Python"

    ```python
    import os
    from openai import OpenAI
    from getpass import getpass
    
    # Get API key from user input
    api_key = os.environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")
    
    # Initialize OpenAI client pointing to kluster.ai API
    client = OpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key=api_key,
    )

    # Log all batch jobs (limit to 3)
    print(client.batches.list(limit=3).to_dict())
    ```

=== "curl"

    ```bash
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

To cancel a batch job currently in progress, send a request to the `cancel` endpoint with your `batch_id`. Note that cancellation may take up to 10 minutes to complete, and the status will show as `canceling.` Once complete, the status will show as `cancelled`.

You can use the following snippets to cancel a batch job:

=== "Python"

    ```python title="Example"
    import os
    from openai import OpenAI
    from getpass import getpass
    
    # Get API key from user input
    api_key = os.environ.get("API_KEY") or getpass("Enter your kluster.ai API key: ")
    
    # Initialize OpenAI client pointing to kluster.ai API
    client = OpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key=api_key,
    )

    # Cancel batch job with specified ID
    client.batches.cancel("mybatch-123")
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

You have now experienced the complete batch inference job lifecycle using kluster.ai's batch API. In this guide, you've learned how to:

- Prepare and submit batch jobs with structured request inputs
- Track your job's progress in real-time
- Retrieve and handle job results
- View and manage your batch jobs
- Cancel jobs when needed

The kluster.ai batch API is designed to efficiently and reliably handle your large-scale LLM workloads. If you have questions or suggestions, the [support](mailto:support@kluster.ai){target=\_blank} team would love to hear from you.


