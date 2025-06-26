---
title: Overview of Fine-tuning models
description: Learn how to create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai platform.
---

# Overview of fine-tuning models

Fine-tuning lets you transform general-purpose models into specialized AI assistants that excel at your unique tasks. With [kluster.ai](https://www.kluster.ai/){target=\_blank}, you can fine-tune models using either the [platform](/get-started/fine-tuning/platform/) or the [API](/get-started/fine-tuning/api/)—choose the path that fits your workflow and technical needs.

## Fine-tuning flow

Fine-tuning on kluster.ai follows a simple, seven-step loop:

1. **Prepare your dataset**: Collect representative examples for the task and save them as a JSON Lines (`.jsonl`) file.  
2. **Upload the dataset**: Use the Platform “Upload” dialog **or** call `files.upload` via the API to receive a `file_id`.  
3. **Configure & launch a job**: Choose a base model, set LoRA-specific (Low-Rank Adaptation) hyper-parameters (epochs, learning rate, adapter rank, etc.), and start the job.  
4. **Monitor training**: Track status and metrics in the dashboard or poll `fine_tuning.jobs.retrieve` until the job reaches `succeeded` or `failed`.  
5. **Retrieve the fine-tuned model**: When the job finishes, grab the returned `fine_tuned_model` ID and treat it like any other model.  
6. **Evaluate & iterate**: Test the model on unseen prompts, compare against the base model, and re-run fine-tuning with refined data or parameters if needed. 
7. **Deploy & integrate**: Call the model in production, export its LoRA adapter, or share it with teammates through kluster.ai’s model registry.  

Fine-tuning is your go-to when you need **reliable, domain-specific outputs** (e.g., JSON-formatted responses, brand-aligned tone) that prompt engineering alone can’t guarantee.

## When to fine-tune your model

Fine-tuning is ideal for scenarios where you need:

- **Domain specialization**: Create models that excel in specific fields like medicine, law, finance, or technical documentation.
- **Brand-aligned responses**: Train models to match your company's voice, style, and communication guidelines.
- **Format consistency**: Ensure reliable output in specific formats like JSON, XML, or Markdown.
- **Enhanced reasoning**: Improve analytical capabilities for specific types of problems.
- **Custom behavior**: Develop assistants that follow your unique processes and workflows.

## Benefits of fine-tuning

Fine-tuning delivers several key advantages over using general-purpose models:

- **Improved performance**: Fine-tuned models consistently outperform base models on specific tasks.
- **Cost efficiency**: Smaller fine-tuned models can match or exceed the performance of larger models at a lower cost.
- **Reduced latency**: Fine-tuned models provide faster responses, enhancing the user experience.
- **Consistency**: Achieve more reliable outputs tailored to your specific requirements.
- **Data privacy**: Train models on your data without exposing sensitive information in prompts.

## Supported models

kluster.ai currently supports fine-tuning for the following models:

--8<-- 'text/get-started/fine-tuning-supported-models.md'

## Choose your fine-tuning approach

kluster.ai offers two ways to fine-tune models, each designed for different user preferences and requirements:

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Platform__

    ---

    Use the platform to fine-tune without writing code. The platform is ideal for users who want a guided, interactive experience and real-time feedback on training progress.

    [:octicons-arrow-right-24: Visit the guide](/get-started/fine-tuning/platform/){target=_blank}

-   <span class="badge guide">Guide</span> __API__

    ---

    Fine-tune models with code for maximum flexibility and automation. The API is best for developers who need advanced customization, integration, or workflow automation.

    [:octicons-arrow-right-24: Visit the guide](/get-started/fine-tuning/api/){target=_blank}

</div>

## Additional resources

- **Step-by-step tutorial**: Learn the fundamentals with our [Fine-tuning sentiment analysis tutorial](/tutorials/klusterai-api/finetuning-sent-analysis/){target=_blank}.
- **Available models**: Explore our [Models](/get-started/models/){target=_blank} page to see all foundation models that support fine-tuning.
- **API reference**: Review the complete [API documentation](/api-reference/reference/#tag/fine-tuning/post/v1/fine_tuning/jobs){target=_blank} for all fine-tuning related endpoints.
