---
title: Fine-tuning with the Platform
description: Learn how to create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai visual interface.
---

# Fine-tuning with the Platform

The kluster.ai platform provides a visual, no-code approach to fine-tuning AI models. With an intuitive interface and real-time feedback, you can train customized models without writing a single line of code.

This guide walks you through the platform's fine-tuning workflow, from uploading your training data to deploying your specialized model.

## Prerequisites

Before getting started with fine-tuning, ensure you have the following:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **Prepared dataset** - you'll need data formatted according to kluster.ai's requirements for fine-tuning (detailed below)

## Supported models

kluster.ai currently supports fine-tuning for two base models:

- **klusterai/Meta-Llama-3.1-8B-Instruct-Turbo** - has a 64,000 tokens max context window, best for long-context tasks and cost-sensitive scenarios
- **klusterai/Meta-Llama-3.3-70B-Instruct-Turbo** - has a 32,000 tokens max context window, best for complex reasoning and high-stakes accuracy

## Data preparation

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

## Fine-tuning workflow

The process of fine-tuning a model using the kluster.ai platform interface involves several key steps:

### 1. Navigate to the fine-tuning page

To begin, visit the [kluster.ai fine-tuning page](https://platform.kluster.ai/fine-tuning){target=_blank} and click on the **Create new job** button.

[INSERT_SCREENSHOT_HERE]

### 2. Select a base model

From the dropdown menu, select one of the available foundation models to fine-tune:
- klusterai/Meta-Llama-3.1-8B-Instruct-Turbo
- klusterai/Meta-Llama-3.3-70B-Instruct-Turbo

[INSERT_SCREENSHOT_HERE]

### 3. Upload your training data

Upload your prepared JSONL training file by dragging and dropping the file or using the file selection dialog.

[INSERT_SCREENSHOT_HERE]

!!! note "Validation data"
    You can optionally upload a validation dataset in the same format as your training data. This helps evaluate your model's performance during training.

### 4. Configure hyperparameters

Customize your fine-tuning job by configuring these hyperparameters:

- **Nickname** - Add an optional custom suffix that will be appended to your fine-tuned model name
- **Batch size** - Control how many examples are processed in each training step
- **Learning rate multiplier** - Adjust how quickly the model adapts to your training data
- **Number of epochs** - Define how many times the model will cycle through your entire dataset

[INSERT_SCREENSHOT_HERE]

After configuring the parameters, click the **Create** button to start the fine-tuning process.

### 5. Monitor job progress

After submitting your fine-tuning job:

1. You can monitor the status and progress of your job on the [fine-tuning page](https://platform.kluster.ai/fine-tuning){target=_blank}
2. Each job displays information including:
   - Job ID
   - Base model
   - Training method
   - Creation date
   - Current status
   - Training metrics (when complete)

[INSERT_SCREENSHOT_HERE]

The job status will update from "queued" to "running" to "succeeded" when complete.

### 6. Access your fine-tuned model

Once fine-tuning is complete, your custom model will be:

1. Listed on the fine-tuning page with its unique identifier
2. Available in the model selection dropdown in the [playground](https://platform.kluster.ai/playground){target=_blank}

[INSERT_SCREENSHOT_HERE]

### 7. Use your model in the playground

To test your fine-tuned model:

1. Navigate to the [kluster.ai playground](https://platform.kluster.ai/playground){target=_blank}
2. Select your fine-tuned model from the model dropdown menu
3. Start chatting with your model to evaluate its performance on your specific task

[INSERT_SCREENSHOT_HERE]

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
- **API approach** - Learn how to [fine-tune models programmatically](/get-started/fine-tuning/api/){target=\_blank} with the kluster.ai API
