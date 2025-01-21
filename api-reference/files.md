---
title: Files API Reference
description: The Files endpoint simplifies file management, allowing you to upload, retrieve, delete, and list files for workflows like storing datasets or configs.
---

## Upload files

`POST https://api.kluster.ai/v1/files/`

Upload a [JSON Lines](https://jsonlines.org/){target=\_blank} file to the `files` endpoint.

You can also view all your uploaded files in the [**Files** tab](https://platform.kluster.ai/files) of the kluster.ai platform.

<div class="grid" markdown>
<div markdown>

**Request**

`file` ++"file"++ <span class="required" markdown>++"required"++</span>

The File object (not file name) to be uploaded.

---

`purpose` ++"string"++ <span class="required" markdown>++"required"++</span>

The intended purpose of the uploaded file. Use `batch` for the Batch API.

**Returns**

The uploaded [File](#file-object) object.

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

    batch_input_file = client.files.create(
        file=open(file_name, "rb"),
        purpose="batch"
    )

    print(batch_input_file.to_dict())
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

</div>
</div>

---

## Retrieve file content

`GET https://api.kluster.ai/v1/files/{output_file_id}/content`

To retrieve the content of your Batch jobs output file, send a request to the `files` endpoint specifying the `output_file_id`. The output file will be a JSONL file, where each line contains the `custom_id` from your input file request, and the corresponding response.

<div class="grid" markdown>
<div markdown>

**Path parameters**

`file_id` ++"string"++ <span class="required" markdown>++"required"++</span>

The ID of the file to use for this request

---

**Returns**

The file content. Refer to the [input](/api-reference/batch/#the-request-input-object){target=\_blank} and [output](/api-reference/batch/#the-request-output-object){target=\_blank} format specifications for batch requests.

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

    # Get the status of the Batch, which returns the output_file_id
    batch_status = client.batches.retrieve(batch_request.id)

    # Check if the Batch completed successfully
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

## File object

<div class="grid" markdown>
<div markdown>

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

```Json title="File object"
{
  "id": "myfile-123",
  "bytes": 2797,
  "created_at": "1733832768",
  "filename": "mybatchtest.jsonl",
  "object": "file",
  "purpose": "batch"
}
```

</div>
</div>
