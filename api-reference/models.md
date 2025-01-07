---
title: Models API Reference
description: The Models endpoint lets you list, retrieve details, and manage access to AI models, helping you select the best model for your use case.
---

# Models

## List supported models

You can use this endpoint to retrieve a list of all available models for the kluster.ai API. Currently supported models:

- `klusterai/Meta-Llama-3.1-8B-Instruct-Turbo`
- `klusterai/Meta-Llama-3.1-405B-Instruct-Turbo`
- `klusterai/Meta-Llama-3.3-70B-Instruct-Turbo`

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
      "id": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
      "object": "model",
      "created": 1731336610,
      "owned_by": "klusterai"
    },
        {
      "id": "klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
      "object": "model",
      "created": 1733777629,
      "owned_by": "klusterai"
    }
  ]
}
```

</div>
</div>

---
