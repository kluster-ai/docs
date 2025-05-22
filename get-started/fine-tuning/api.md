---
title: Fine-tuning with the API
description: Learn how to programmatically create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai API.
---

# Fine-tuning with the API

The kluster.ai API lets you automate and integrate fine-tuning into your development workflows. You can create, manage, and monitor fine-tuning jobs directly from your code, making it easy to customize models for your specific needs.

This guide provides a practical overview of the fine-tuning process using the API. It covers the required data format, how to upload your dataset, and how to launch and monitor a fine-tuning job. For a step-by-step walkthrough, see the linked tutorial in the tips below.

## Prerequisites

Before getting started with fine-tuning, ensure you have the following:

- **kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=_blank} if you do not have one
- **kluster.ai API key** - after signing in, go to the [API Keys](https://platform.kluster.ai/apikeys){target=_blank} section and create a new key. For detailed instructions, see the [Get an API key](https://docs.kluster.ai/get-started/get-api-key/){target=_blank} guide
- **Prepared dataset** - you need data formatted according to kluster.ai's requirements for fine-tuning (detailed below)

## Supported models

kluster.ai currently supports fine-tuning for two base models:

- **klusterai/Meta-Llama-3.1-8B-Instruct-Turbo** - 64,000 tokens max context window, best for long-context tasks and cost-sensitive scenarios
- **klusterai/Meta-Llama-3.3-70B-Instruct-Turbo** - 32,000 tokens max context window, best for complex reasoning and high-stakes accuracy

!!! info
    You can query the [models endpoint](https://docs.kluster.ai/api-reference/reference/#list-supported-models){target=_blank} in the API and filter for the tag "fine-tunable."

## Fine-tuning workflow

The process of fine-tuning a model using the kluster.ai API involves several key steps:


### Prepare your data

High-quality, well-formatted data is crucial for successful fine-tuning:

- **Format** - data must be in JSONL format, where each line is a valid JSON object representing a training example
- **Structure** - each JSON object should contain a `messages` array with system, user, and assistant messages
- **Example format**:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a JSON Generation Specialist. Convert user requests into properly formatted JSON."
    },
    {
      "role": "user",
      "content": "Create a configuration for a web application with name 'TaskMaster', version 1.2.0, and environment set to development."
    },
    {
      "role": "assistant",
      "content": "{\n  \"application\": {\n    \"name\": \"TaskMaster\",\n    \"version\": \"1.2.0\",\n    \"environment\": \"development\"\n  }\n}"
    }
  ]
}
```

- **Quantity** - the minimum requirement is 10 examples, but more diverse and high-quality examples yield better results
- **Quality** - ensure your data accurately represents the task you want the model to perform

!!! tip "Data preparation"
    For a detailed walkthrough of data preparation, see the [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/#get-the-data){target=_blank}.

!!! example "Find Llama datasets on Hugging Face"
    There is a wide range of datasets suitable for Llama model fine-tuning on [Hugging Face Datasets](https://huggingface.co/datasets?sort=trending&search=llama){target=_blank}. Browse trending and community-curated datasets to accelerate your data preparation.

### Set up the client

First, install the OpenAI Python library:

```bash
%pip install openai
```

Then initialize the client with the kluster.ai base URL:

```python
from openai import OpenAI
from getpass import getpass

api_key = getpass("Enter your kluster.ai API key: ")

# Set up the client
client = OpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key=api_key
)
```
### Upload your training file

Once your data is prepared, upload it to the kluster.ai platform:

```python
# Upload fine-tuning file (for files under 100MB)
with open('training_data.jsonl', 'rb') as file:
    upload_response = client.files.create(
        file=file,
        purpose="fine-tune"  # Important: specify "fine-tune" as the purpose
    )
    
    # Get the file ID
    file_id = upload_response.id
    print(f"File uploaded successfully. File ID: {file_id}")
```

!!! note "Uploading large files"
    If your training dataset is large (approaching 100MB), you may need to use the chunked upload method. See the [Uploading Large Files](https://docs.kluster.ai/tutorials/klusterai-api/uploads-api/) guide for detailed instructions on multi-part uploads.

!!! warning "File size limits"
    For the free tier, each fine-tuning file must not exceed 100 MB. For the standard tier, the maximum file size is also 100 MB per file. The difference between tiers is in the number of examples allowed - free tier is limited to fewer examples.

### Create a fine-tuning job

After uploading your data, initiate the fine-tuning job:

```python
# Model
model = "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo"

# Create fine-tune job
fine_tuning_job = client.fine_tuning.jobs.create(
    training_file=file_id,
    model=model,
    # Optional hyperparameters
    # hyperparameters={
    #   "batch_size": 3,
    #   "n_epochs": 2,
    #   "learning_rate_multiplier": 0.08
    # }
)
```


### Monitor job progress

Track the status of your fine-tuning job:

```python
# Retrieve job status
job_status = client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
print(f"Job status: {job_status.status}")
```

### Use your fine-tuned model

Once your fine-tuning job completes successfully, you will receive a unique fine-tuned model name that you can use for inference:

```python
# Get the fine-tuned model name
finished_job = client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
fine_tuned_model = finished_job.fine_tuned_model

# Use the fine-tuned model for inference
response = client.chat.completions.create(
    model=fine_tuned_model,
    messages=[
        {"role": "system", "content": "You are a JSON Generation Specialist. Convert user requests into properly formatted JSON."},
        {"role": "user", "content": "Create a configuration for a web application with name 'TaskMaster', version 1.2.0, and environment set to development."}
    ]
)
```
### Use your fine-tuned model in the playground (optional)

After your fine-tuned model is created, you can also test it in the kluster.ai playground:

1. Go to the [kluster.ai playground](https://platform.kluster.ai/playground){target=_blank}
2. Select your fine-tuned model from the model dropdown menu
3. Start chatting with your model to evaluate its performance on your specific task

## Benefits of fine-tuning

Fine-tuning offers several advantages over using general-purpose models:

- **Improved performance** - fine-tuned models often outperform base models on specific tasks
- **Cost efficiency** - smaller fine-tuned models can outperform larger models at a lower cost
- **Reduced latency** - fine-tuned models can deliver faster responses for your applications
- **Consistency** - more reliable outputs tailored to your specific task or domain


## Next steps

- **Detailed tutorial** - follow the [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/#get-the-data){target=_blank}
- **API reference** - review the [API reference documentation](/api-reference/reference/){target=_blank} for all fine-tuning related endpoints
- **Explore models** - see the [Models](/get-started/models/){target=_blank} page to check which foundation models support fine-tuning
- **Platform approach** - try the [user-friendly platform interface](/get-started/fine-tuning/platform/){target=_blank} for fine-tuning without writing code
