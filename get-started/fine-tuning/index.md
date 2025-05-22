---
title: Fine-tuning models with kluster.ai
description: Learn how to create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai platform.
---

# Fine-tuning models with kluster.ai

Fine-tuning allows you to adapt kluster.ai's powerful foundation models to your specific tasks and datasets, significantly improving performance for your unique use cases while potentially reducing costs compared to larger general-purpose models.

## What is fine-tuning?

Fine-tuning takes a pre-trained foundation model and further trains it on your specific dataset to enhance its performance on particular tasks. This process allows the model to learn the patterns, style, and domain knowledge present in your data.

## Supported models

kluster.ai currently supports fine-tuning for two base models:

- **klusterai/Meta-Llama-3.1-8B-Instruct-Turbo** - has a 64,000 tokens max context window, best for long-context tasks and cost-sensitive scenarios
- **klusterai/Meta-Llama-3.3-70B-Instruct-Turbo** - has a 32,000 tokens max context window, best for complex reasoning and high-stakes accuracy

## Benefits of fine-tuning

Fine-tuning offers several advantages over using general-purpose models:

- **Improved performance** - fine-tuned models often outperform base models on specific tasks
- **Cost efficiency** - smaller fine-tuned models can outperform larger models at a lower cost
- **Reduced latency** - fine-tuned models can deliver faster responses for your applications
- **Consistency** - more reliable outputs tailored to your specific task or domain

## Where to go next

<div class="grid cards" markdown>

-   <span class="badge guide">Guide</span> __Platform Interface__

    ---

    Use the kluster.ai platform's user-friendly graphical interface to fine-tune models without writing any code.

    [:octicons-arrow-right-24: Visit the guide](/get-started/fine-tuning/platform/)

-   <span class="badge guide">Guide</span> __API Integration__

    ---

    Gain programmatic control over the fine-tuning process with the kluster.ai API for applications, workflows, and advanced customization.

    [:octicons-arrow-right-24: Visit the guide](/get-started/fine-tuning/api/)

</div>

## Additional resources

- **Detailed tutorial** - Follow our step-by-step [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/){target=\_blank}
- **Explore models** - Check out our [Models](/get-started/models/){target=\_blank} page to see which foundation models support fine-tuning
