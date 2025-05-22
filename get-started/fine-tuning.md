---
title: Fine-tuning models with kluster.ai
description: Learn how to create custom models tailored to your specific tasks by fine-tuning foundation models with your own data using the kluster.ai platform.
---

# Fine-tuning models with kluster.ai

Fine-tuning allows you to adapt kluster.ai's powerful foundation models to your specific tasks and datasets, significantly improving performance for your unique use cases while potentially reducing costs compared to larger general-purpose models.

## Choose your approach

There are two ways to fine-tune models on kluster.ai:

### [Platform Interface](/get-started/fine-tuning/platform/)

The [kluster.ai platform](/get-started/fine-tuning/platform/){target=_blank} provides a user-friendly graphical interface for fine-tuning models without writing any code. This approach is ideal for:

- Users who prefer a visual interface
- Those who want to quickly experiment with fine-tuning
- Teams who want a simple, no-code solution

### [API Integration](/get-started/fine-tuning/api/)

The [kluster.ai API](/get-started/fine-tuning/api/){target=_blank} gives you programmatic control over the fine-tuning process. This approach is ideal for:

- Developers building applications
- Automated workflows and CI/CD pipelines
- Advanced customization of fine-tuning parameters

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

## Next steps

- **Choose your approach**: Select either the [platform](/get-started/fine-tuning/platform/){target=_blank} or [API](/get-started/fine-tuning/api/){target=_blank} route
- **Detailed tutorial** - Follow our step-by-step [Fine-tuning Sentiment Analysis Tutorial](https://docs.kluster.ai/tutorials/klusterai-api/finetuning-sent-analysis/){target=\_blank}
- **Explore models** - Check out our [Models](/get-started/models/){target=\_blank} page to see which foundation models support fine-tuning
