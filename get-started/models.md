---
title: Supported AI Models
description: Learn what models are supported by the kluster.ai API and the main characteristics and API request limits for each model for both free and standard tiers.
---

# Models on kluster.ai

[kluster.ai](https://kluster.ai){target=\_blank} offers a wide variety of open-source models for both real-time and batch inferences, with more being constantly added.
 
This page covers all the models the API supports, with the API request limits for each.

## Model names

Each model supported by kluster.ai has a unique name that must be used when defining the `model` in the request.

|             Model             |                   Model API name                    |
|:-----------------------------:|:---------------------------------------------------:|
|        **DeepSeek-R1**        |              `deepseek-ai/DeepSeek-R1`              |
|     **DeepSeek-V3-0324**      |           `deepseek-ai/DeepSeek-V3-0324`            |
|        **Gemma 3 27B**        |               `google/gemma-3-27b-it`               |
|     **Meta Llama 3.1 8B**     |    `klusterai/Meta-Llama-3.1-8B-Instruct-Turbo`     |
|    **Meta Llama 3.3 70B**     |    `klusterai/Meta-Llama-3.3-70B-Instruct-Turbo`    |
|   **Meta Llama 4 Maverick**   | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` |
|    **Meta Llama 4 Scout**     |     `meta-llama/Llama-4-Scout-17B-16E-Instruct`     |
|       **Qwen2.5-VL 7B**       |            `Qwen/Qwen2.5-VL-7B-Instruct`            |
|      **Qwen3-235B-A22B**      |             `Qwen/Qwen3-235B-A22B-FP8`              |

## Model comparison table

| Model | Description | Real-time<br>inference support | Batch<br>inference support | Fine-tuning<br>support | Image<br>analysis  |
|:-----------------------------:|:-------------------------------------------------------------------:|:------------------------------:|:--------------------------:|:----------------------:|:------------------:|
| **DeepSeek-R1** | Mathematical problem-solving<br>code generation<br>complex data analysis. | :white_check_mark: | :white_check_mark: | :x: | :x: |
| **DeepSeek-V3-0324** | Natural language generation<br>open-ended text creation<br>contextually rich writing. | :white_check_mark: | :white_check_mark: | :x: | :x: |
| **Gemma 3 27B** | Multilingual applications<br>extended-context tasks<br>image analysis<br>and complex reasoning. | :white_check_mark: | :white_check_mark: | :x: | :white_check_mark: |
| **Llama 3.1 8B** | Low-latency or simple tasks<br>cost-efficient inference. | :white_check_mark: | :white_check_mark: | :white_check_mark: | :x: |
| **Llama 3.3 70B** | General-purpose AI<br>balanced cost-performance. | :white_check_mark: | :white_check_mark: | :white_check_mark: | :x: |
| **Llama 4 Maverick** | A state-of-the-art multimodal<br>model with integrated vision<br>and language understanding,<br>optimized for complex<br>reasoning, coding, and<br>perception tasks | :white_check_mark: | :white_check_mark: | :x: | :white_check_mark: |
| **Llama 4 Scout** | General-purpose multimodal AI<br>extended context tasks<br>and balanced cost-performance across text and vision. | :white_check_mark: | :white_check_mark: | :x: | :white_check_mark: |
| **Qwen2.5-VL 7B** | Visual question answering<br>document analysis<br>image-based reasoning<br>multimodal chat. | :white_check_mark: | :white_check_mark: | :x: | :white_check_mark: |
| **Qwen3-235B-A22B** | Qwen3's flagship 235 billion<br>parameter model optimized with<br>8-bit quantization | :white_check_mark: | :white_check_mark: | :x: | :x: |

## API request limits

--8<-- "text/get-started/rate-limit.md"

