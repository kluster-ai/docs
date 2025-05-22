---
title: Fine-tuning models with kluster.ai API
description: Learn how to create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai API.
---

# Fine-tuning models with kluster.ai API

Fine-tuning allows you to adapt kluster.ai's powerful foundation models to your specific tasks and datasets, significantly improving performance for your unique use cases while potentially reducing costs compared to larger general-purpose models.

This guide will walk you through the essential steps to begin fine-tuning models using the kluster.ai API.

## Prerequisites

Before getting started with fine-tuning, ensure you have the following:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](https://docs.kluster.ai/get-started/get-api-key/){target=\_blank} guide
- **Prepared dataset** - you'll need data formatted according to kluster.ai's requirements for fine-tuning (detailed below)

## Supported models

kluster.ai currently supports fine-tuning for two base models:

- **klusterai/Meta-Llama-3.1-8B-Instruct-Turbo** - has a 64,000 tokens max context window, best for long-context tasks and cost-sensitive scenarios
- **klusterai/Meta-Llama-3.3-70B-Instruct-Turbo** - has a 32,000 tokens max context window, best for complex reasoning and high-stakes accuracy

You can query the [models endpoint](https://docs.kluster.ai/api-reference/reference/#list-supported-models){target=\_blank} in the API and filter for the tag "_fine-tunable_"

## Fine-tuning workflow

The process of fine-tuning a model using the kluster.ai API involves several key steps:

### 1. Prepare your data

High-quality, well-formatted data is crucial for successful fine-tuning:

- **Format** - data must be in JSONL format, where each line is a valid JSON object representing a training example
- **Structure** - each JSON object should contain a `messages` array with system, user, and assistant messages
- **Example format**:

```json
{
  "messages": [
    {"role": "system", "content": "You are a JSON Generation Specialist. Convert user requests into properly formatted JSON."},
    {"role": "user", "content": "Create a configuration for a web application with name 'TaskMaster', version 1.2.0, and environment set to development."},
    {"role": "assistant", "content": "{\n  \"application\": {\n    \"name\": \"TaskMaster\",\n    \"version\": \"1.2.0\",\n    \"environment\": \"development\"\n  }\n}"}
  ]
}
```

- **Quantity** - while the minimum requirement is 10 examples, more diverse and high-quality examples will yield better results
- **Quality** - ensure your data accurately represents the task you want the model to perform

!!! tip "Data preparation"
    For a detailed walkthrough of data preparation, see our [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/#get-the-data){target=\_blank}.


!!! example "Find Llama datasets on Hugging face"
    There's a wide range of datasets suitable for Llama model fine-tuning on [Hugging Face Datasets](https://huggingface.co/datasets?sort=trending&search=llama){target=_blank}. Browse trending and community-curated datasets to accelerate your data preparation.

### 2. Upload your training file

Once your data is prepared, upload it to the kluster.ai platform:

```python
# Upload fine-tuning file
with open('training_data.jsonl', 'rb') as file:
    upload_response = client.files.create(
        file=file,
        purpose="fine-tune"
    )
    
    # Get the file ID
    file_id = upload_response.id
```

### 3. Create a fine-tuning job

After uploading your data, initiate the fine-tuning job:

```python
# Create fine-tune job
fine_tuning_job = client.fine_tuning.jobs.create(
    training_file=file_id,
    model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    # Optional hyperparameters
    # hyperparameters={
    #   "batch_size": 3,
    #   "n_epochs": 2,
    #   "learning_rate_multiplier": 0.08
    # }
)
```

### 4. Monitor job progress

Track the status of your fine-tuning job:

```python
# Retrieve job status
job_status = client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
print(f"Job status: {job_status.status}")
```

### 5. Use your fine-tuned model

Once your fine-tuning job completes successfully, you'll receive a unique fine-tuned model name that you can use for inference:

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

!!! warning
    For the free tier, the maximum number of batch requests (lines in the JSONL file) must be less than 1000, and each file must not exceed 100 MB. For the standard tier, there is no limit to the number of batch requests, but the maximum batch file size is 100 MB per file.

## Benefits of fine-tuning

Fine-tuning offers several advantages over using general-purpose models:

- **Improved performance** - fine-tuned models often outperform base models on specific tasks
- **Cost efficiency** - smaller fine-tuned models can outperform larger models at a lower cost
- **Reduced latency** - fine-tuned models can deliver faster responses for your applications
- **Consistency** - more reliable outputs tailored to your specific task or domain

## Next steps

- **Detailed tutorial** - Follow our step-by-step [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/#get-the-data){target=\_blank}
- **API reference** - Review the complete [API reference documentation](/api-reference/reference/){target=\_blank} for all fine-tuning related endpoints
- **Explore models** - Check out our [Models](/get-started/models/){target=\_blank} page to see which foundation models support fine-tuning
- **Platform approach** - Try the [user-friendly platform interface](/get-started/fine-tuning/platform/){target=\_blank} for fine-tuning without writing code
