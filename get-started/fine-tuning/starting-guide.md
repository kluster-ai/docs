---
title: Fine-tuning models with kluster.ai
description: Learn how to create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai platform.
---

# Fine-tuning models with kluster.ai

Fine-tuning lets you transform general-purpose models into specialized AI assistants that excel at your unique tasks. With kluster.ai, you can fine-tune models using either a [visual platform](/get-started/fine-tuning/platform/){target=_blank} or a [flexible API](/get-started/fine-tuning/api/){target=_blank}—choose the path that fits your workflow and technical needs.

## What to know

_Fine-tuning_ takes a pre-trained foundation model and further trains it on your specific dataset to enhance its performance on particular tasks. Unlike prompt engineering, which works within the constraints of the base model, fine-tuning with LoRA (Low-Rank Adaptation) **efficiently adapts the model** by adding small trainable adapter layers rather than modifying all original weights.

This process allows the model to:

- Learn domain-specific terminology and concepts
- Adopt your preferred response style and tone
- Follow consistent formatting and output structures
- Develop specialized capabilities tailored to your use cases

Fine-tuning is **particularly valuable** when you want consistent, specialized responses that would otherwise require complex prompting or when you need the model to reliably generate outputs in a specific format.

## When to fine-tune your model

Fine-tuning is ideal for scenarios where you need:

- **Domain specialization** - create models that excel in specific fields like medicine, law, finance, or technical documentation
- **Brand-aligned responses** - train models to match your company's voice, style, and communication guidelines
- **Format consistency** - ensure reliable output in specific formats like JSON, XML, or markdown
- **Enhanced reasoning** - improve analytical capabilities for specific types of problems
- **Custom behavior** - develop assistants that follow your unique processes and workflows

## Benefits of fine-tuning

Fine-tuning delivers _several key advantages_ over using general-purpose models:

- **Improved performance** - fine-tuned models consistently outperform base models on specific tasks
- **Cost efficiency** - smaller fine-tuned models can match or exceed the performance of larger models at a lower cost
- **Reduced latency** - fine-tuned models deliver faster responses, improving user experience
- **Consistency** - achieve more reliable outputs tailored to your specific requirements
- **Data privacy** - train models on your data without exposing sensitive information in prompts

## Supported models

kluster.ai supports fine-tuning for **two powerful foundation models**:

- **klusterai/Meta-Llama-3.1-8B-Instruct-Turbo** - has a 64,000 tokens max context window, best for long-context tasks and cost-sensitive scenarios
- **klusterai/Meta-Llama-3.3-70B-Instruct-Turbo** - has a 32,000 tokens max context window, best for complex reasoning and high-stakes accuracy

## Choose your fine-tuning approach

kluster.ai offers _two complementary ways_ to fine-tune models, each designed for different user preferences and requirements:

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Platform__

    ---

    Fine-tune models visually, without writing code. The platform is ideal for users who want a guided, interactive experience and real-time feedback on training progress.

    [:octicons-arrow-right-24: Visit the guide](/get-started/fine-tuning/platform/){target=_blank}

-   <span class="badge guide">Guide</span> __API__

    ---

    Fine-tune models programmatically for maximum flexibility and automation. The API is best for developers who need advanced customization, integration, or workflow automation.

    [:octicons-arrow-right-24: Visit the guide](/get-started/fine-tuning/api/){target=_blank}

</div>

## Additional resources

- **Step-by-step tutorial** - Learn the fundamentals with our [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/){target=_blank}
- **Available models** - Explore our [Models](/get-started/models/){target=_blank} page to see all foundation models that support fine-tuning
- **API reference** - Review the complete [API documentation](/api-reference/reference/){target=_blank} for all fine-tuning related endpoints
