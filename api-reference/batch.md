---
title: Batches
description: TODO
---

## Submit a Batch job

`POST https://api.kluster.ai/v1/batches`

To submit a Batch job, send a request to the `batches` endpoint.

<div class="grid" markdown>
<div markdown>

**Request**

`input_file_id` ++"string"++ <span class="required" markdown>++"required"++</span>

The ID of an [uploaded file](/api-reference/files/#upload-files){target=\_blank} that contains requests for the new Batch.

Your input file must be formatted as a [JSONL file](https://jsonlines.org/){target=\_blank}, and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests and currently a maximum of 6GB per file.

---

`endpoint` ++"string"++ <span class="required" markdown>++"required"++</span>

The endpoint to be used for all requests in the Batch. Currently, only `/v1/chat/completions` is supported.

---

`completion_window` ++"string"++ <span class="required" markdown>++"required"++</span>

The supported completion windows are 1, 3, 6, 12, and 24 hours to accommodate a range of use cases and budget requirements. The code samples provided utilize the 24-hour completion window. 

Learn more about how completion window selection affects cost by visiting the pricing section of the [kluster.ai website](https://www.kluster.ai){target=\_blank}.

---

`metadata` ++"Object or null"++

Custom metadata for the Batch.

---

**Returns**

The created [Batch](#batch-object) object.

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

</div>
</div>

---

## Retrieve a Batch

`GET https://api.kluster.ai/v1/batches/{batch_id}`

To retrieve a Batch job, send a request to the `batches` endpoint with your `batch_id`.

You can also monitor jobs in the [**Batch** tab](https://platform.kluster.ai/batch){target=\_blank} of the kluster.ai platform UI.

<div class="grid" markdown>
<div markdown>

**Path parameters**

`batch_id` ++"string"++ <span class="required" markdown>++"required"++</span>

The ID of the Batch to retrieve.

---

**Returns**

The [Batch](#batch-object) object matching the specified `batch_id`.

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

</div>
</div>

---

## Cancel a Batch

`POST https://api.kluster.ai/v1/batches/{batch_id}/cancel`

To cancel a Batch job that is currently in progress, send a request to the `cancel` endpoint with your `batch_id`. Note that cancellation may take up to 10 minutes to complete, during which time the status will show as `cancelling`.

<div class="grid" markdown>
<div markdown>

**Path parameters**

`batch_id` ++"string"++ <span class="required" markdown>++"required"++</span>

The ID of the Batch to cancel.

---

**Returns**

The [Batch](#batch-object) object matching the specified ID.

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

## List all Batch jobs

`GET https://api.kluster.ai/v1/batches`

To list all Batch jobs, send a request to the `batches` endpoint without specifying a `batch_id`. To constrain the query response, you can also use a `limit` parameter.

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

A list of paginated [Batch](#batch-object) objects.

The status of a Batch object can be one of the following:

<style>
table th:first-child {
  width: 10em;
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

</div>
</div>

---

## Batch object

<div class="grid" markdown>
<div markdown>

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

The current status of the Batch.

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

```Json title="Batch object"
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

</div>
