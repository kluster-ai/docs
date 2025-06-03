---
title: Fine-tuning with the kluster.ai API
description: Learn how to programmatically create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai API.
---

# Fine-tuning with the kluster.ai API

The [kluster.ai](https://www.kluster.ai/){target=\_blank} API lets you automate and integrate fine-tuning into your development workflows. You can create, manage, and monitor fine-tuning jobs directly from your code, making it easy to customize models for your specific needs.

This guide provides a practical overview of the fine-tuning process using the API. It covers the required data format, how to upload your dataset, and how to launch and monitor a fine-tuning job. For a step-by-step walkthrough, see the linked tutorial in the tips below.

## Prerequisites

Before getting started with fine-tuning, ensure you have the following:

--8<-- 'text/kluster-api-onboarding.md'
- **Prepared dataset**: You need data formatted according to kluster.ai's requirements for fine-tuning (detailed below).

## Supported models

kluster.ai currently supports fine-tuning for the following models:

--8<-- 'text/get-started/fine-tuning-supported-models.md'

!!! note
    You can query the [models endpoint](/api-reference/reference/#list-supported-models){target=_blank} in the API and filter for the tag "fine-tunable."

## Fine-tuning workflow

Fine‑tuning a model with the kluster.ai API follows a straightforward five‑step workflow:

1. **Prepare your data**: Collect and structure high‑quality JSONL training examples that reflect the task you want the model to learn.
2. **Upload your training file**: Send the JSONL file to kluster.ai and note the returned `file_id`.
3. **Create the fine‑tuning job**: Launch a fine‑tuning job specifying the base model and training `file_id` (plus any optional hyperparameters).
4. **Monitor job progress**: Poll the job endpoint (or subscribe to webhooks) until the job reaches the `succeeded` state.
5. **Use your fine‑tuned model**: Invoke the model name returned by the job for inference in your application or the kluster.ai playground.

The following sections will provide a closer look at each step.

### Prepare your data

High-quality, well-formatted data is crucial for successful fine-tuning:

- **Format**: Data must be in JSONL format, where each line is a valid JSON object representing a training example.
- **Structure**: Each JSON object should contain a `messages` array with system, user, and assistant messages.
- **Example format**:

    ```json
    --8<-- 'code/get-started/fine-tuning/prepare.json'
    ```

- **Quantity**: The minimum requirement is 10 examples, but more diverse and high-quality examples yield better results.
- **Quality**: Ensure your data accurately represents the task you want the model to perform.

!!! tip "Data preparation"
    For a detailed walkthrough of data preparation, see the [Fine-tuning sentiment analysis tutorial](/tutorials/klusterai-api/finetuning-sent-analysis/#get-the-data){target=_blank}.

!!! example "Find Llama datasets on Hugging Face"
    There is a wide range of datasets suitable for Llama model fine-tuning on [Hugging Face Datasets](https://huggingface.co/datasets?sort=trending&search=llama){target=_blank}. Browse trending and community-curated datasets to accelerate your data preparation.

### Set up the client

First, install the OpenAI Python library:

```bash
pip install openai
```

Then initialize the client with the kluster.ai base URL:

```python
--8<-- "code/get-started/fine-tuning/fine-tune.py:1:11"
```

### Upload your training file

Once your data is prepared, upload it to the kluster.ai platform:

```python
--8<-- "code/get-started/fine-tuning/fine-tune.py:13:22"
```

!!! warning "File size & upload limits"
    Each fine-tuning file must be ≤ 100 MB on both the free and standard tiers (the standard tier simply allows more total examples).  
    When your dataset approaches this limit, use the [chunked upload](/tutorials/klusterai-api/uploads-api/){target=_blank} method for reliable multi-part uploads.

### Create a fine-tuning job

After uploading your data, initiate the fine-tuning job:

```python
--8<-- "code/get-started/fine-tuning/fine-tune.py:24:37"
```

### Monitor job progress

Track the status of your fine-tuning job:

```python
--8<-- "code/get-started/fine-tuning/fine-tune.py:39:41"
```

### Use your fine-tuned model

Once your fine-tuning job completes successfully, you will receive a unique fine-tuned model name that you can use for inference:

```python
--8<-- "code/get-started/fine-tuning/fine-tune.py:43:54"
```

You can view the end-to-end python script below:

??? code "fine-tune.py"

    ```python
    --8<-- "code/get-started/fine-tuning/fine-tune.py"
    ```

### Use your fine-tuned model in the playground (optional)

After your fine-tuned model is created, you can also test it in the kluster.ai playground:

1. Go to the [kluster.ai playground](https://platform.kluster.ai/playground){target=_blank}
2. Select your fine-tuned model from the model dropdown menu
3. Start chatting with your model to evaluate its performance on your specific task

## Benefits of fine-tuning

Fine-tuning offers several advantages over using general-purpose models:

- **Improved performance**: Fine-tuned models often outperform base models on specific tasks.
- **Cost efficiency**: Smaller fine-tuned models can outperform larger models at a lower cost.
- **Reduced latency**: Fine-tuned models can deliver faster responses for your applications.
- **Consistency**: More reliable outputs tailored to your specific task or domain.

## Next steps

- **Detailed tutorial**: Follow the [Fine-tuning sentiment analysis tutorial](/tutorials/klusterai-api/finetuning-sent-analysis/#get-the-data){target=_blank}.
- **API reference**: Review the [API reference documentation](/api-reference/reference/){target=_blank} for all fine-tuning related endpoints.
- **Explore models**: See the [Models](/get-started/models/){target=_blank} page to check which foundation models support fine-tuning.
- **Platform approach**: Try the [user-friendly platform interface](/get-started/fine-tuning/platform/){target=_blank} for fine-tuning without writing code.