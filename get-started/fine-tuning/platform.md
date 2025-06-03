---
title: Fine-tuning with the kluster.ai Platform
description: Learn how to create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai visual interface.
---

# Fine-tuning with the kluster.ai Platform

The kluster.ai platform provides a visual, no-code approach to fine-tuning AI models. With an intuitive interface and real-time feedback, you can train customized models without writing a single line of code.

This guide walks you through the platform's fine-tuning workflow, from uploading your training data to deploying your specialized model.

## Prerequisites

Before getting started with fine-tuning, ensure you have the following:

--8<-- 'text/kluster-api-onboarding.md'
- **Prepared dataset**: You need data formatted according to kluster.ai's requirements for fine-tuning (detailed below).

## Supported models

kluster.ai currently supports fine-tuning for two base models:

- [klusterai/Meta-Llama-3.1-8B-Instruct-Turbo](https://docs.kluster.ai/get-started/models/){target=_blank}
- [klusterai/Meta-Llama-3.3-70B-Instruct-Turbo](https://docs.kluster.ai/get-started/models/){target=_blank} 

## Data preparation

High-quality, well-formatted data is crucial for successful fine-tuning:

- **Format**: Data must be in JSONL format, where each line is a valid JSON object representing a training example.
- **Structure**: Each JSON object should contain a `messages` array with system, user, and assistant messages.
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


- **Quantity**: The minimum requirement is 10 examples, but more diverse and high-quality examples yield better results.
- **Quality**: Ensure your data accurately represents the task you want the model to perform.

!!! tip "Data preparation"
    For a detailed walkthrough of data preparation, see the [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/#get-the-data){target=_blank}.

!!! example "Find Llama datasets on Hugging Face"
    There is a wide range of datasets suitable for Llama model fine-tuning on [Hugging Face Datasets](https://huggingface.co/datasets?sort=trending&search=llama){target=_blank}. Browse trending and community-curated datasets to accelerate your data preparation.

## Fine-tuning workflow

The process of fine-tuning a model using the kluster.ai platform interface involves several key steps:

### Navigate to the fine-tuning page

To begin, visit the [kluster.ai fine-tuning page](https://platform.kluster.ai/fine-tuning){target=_blank} and click the **Create new job** button.

![Create new fine-tuning job](/images/get-started/fine-tuning/fine-tuning-1.webp)

### Choose model and upload data

  1. **Select a base model**: Choose one of the available foundation models from the dropdown menu.
  2. **Upload your file**: Upload your prepared JSONL training file by dragging and dropping the file or using the file selection dialog.

![Select base model](/images/get-started/fine-tuning/fine-tuning-2.webp)

!!! note "Validation data"
    You can optionally upload a validation dataset in the same format as your training data. This helps evaluate your model's performance during training.

### Configure hyperparameters
  Customize your fine-tuning job by configuring these settings:

  1. **Nickname**: Add an optional custom suffix that will be appended to your fine-tuned model name.
  2. **Batch size**: Control how many examples are processed in each training step.
  3. **Learning rate multiplier**: Adjust how quickly the model adapts to your training data.
  4. **Number of epochs**: Define how many times the model will cycle through your entire dataset.
  5. **Create**: Click the Create button to start the fine-tuning process.

   ![Configure hyperparameters](/images/get-started/fine-tuning/fine-tuning-3.webp)

### Monitor job progress

After submitting your fine-tuning job, you can monitor the status and progress of your job on the [fine-tuning page](https://platform.kluster.ai/fine-tuning){target=_blank}.

Each job displays information including:

- Job ID
- Base model
- Training method
- Creation date
- Current status
- Training metrics (when complete)

![Job Progress](/images/get-started/fine-tuning/fine-tuning-4.webp)

!!! tip "Status Update"
    The job status updates will first display "queued," then "running," and "succeeded" when complete.

### Access your fine-tuned model

Once fine-tuning is complete, your custom model will be listed on the fine-tuning page with its unique identifier and available in the model selection dropdown in the [playground](https://platform.kluster.ai/playground){target=_blank}.

![Playground Chat](/images/get-started/fine-tuning/fine-tuning-5.webp)

## Benefits of fine-tuning

Fine-tuning offers several advantages over using general-purpose models:

- **Improved performance**: Fine-tuned models often outperform base models on specific tasks.
- **Cost efficiency**: Smaller fine-tuned models can outperform larger models at a lower cost.
- **Reduced latency**: Fine-tuned models can deliver faster responses for your applications.
- **Consistency**: More reliable outputs tailored to your specific task or domain.

## Next steps

- **Detailed tutorial**: Follow the [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/#get-the-data){target=_blank}.
- **API reference**: Review the [API reference documentation](/api-reference/reference/){target=_blank} for all fine-tuning related endpoints.
- **Explore models**: See the [Models](/get-started/models/){target=_blank} page to check which foundation models support fine-tuning.
- **API approach**: Learn how to [fine-tune models programmatically](/get-started/fine-tuning/api/){target=_blank} with the kluster.ai API.