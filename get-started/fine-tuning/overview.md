---
title: Overview of Fine-tuning models
description: Learn how to create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai platform.
---

# Overview of fine-tuning models

Fine-tuning lets you transform general-purpose models into specialized AI assistants that excel at your unique tasks. With [kluster.ai](https://www.kluster.ai/){target=\_blank}, you can fine-tune models using either the [platform](/get-started/fine-tuning/platform/) or the [API](/get-started/fine-tuning/api/)—choose the path that fits your workflow and technical needs.

## What to know

Fine-tuning involves taking a pre-trained foundation model and further training it on your specific dataset to enhance its performance on particular tasks. Unlike prompt engineering, which works within the constraints of the base model, fine-tuning with _LoRA (Low-Rank Adaptation)_ efficiently adapts the model by adding small trainable adapter layers rather than modifying all original weights.

This process allows the model to:

- Learn domain-specific terminology and concepts.
- Adopt your preferred response style and tone.
- Follow consistent formatting and output structures.
- Develop specialized capabilities tailored to your use cases.

Fine-tuning is particularly valuable when you want consistent, specialized responses that would otherwise require complex prompting or when you need the model to generate outputs in a specific format reliably.

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

kluster.ai currently supports fine-tuning for two powerful foundation models:

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
- **API reference**: Review the complete [API documentation](/api-reference/reference/){target=_blank} for all fine-tuning related endpoints.
