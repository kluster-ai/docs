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
|        **DeepSeek R1**        |              `deepseek-ai/DeepSeek-R1`              |
|        **DeepSeek V3**        |              `deepseek-ai/DeepSeek-V3`              |
|     **DeepSeek V3 0324**      |           `deepseek-ai/DeepSeek-V3-0324`            |
|        **Gemma 3 27B**        |               `google/gemma-3-27b-it`               |
|       **Llama 3.1 8B**        |    `klusterai/Meta-Llama-3.1-8B-Instruct-Turbo`     |
|      **Llama 3.1 405B**       |   `klusterai/Meta-Llama-3.1-405B-Instruct-Turbo`    |
|       **Llama 3.3 70B**       |    `klusterai/Meta-Llama-3.3-70B-Instruct-Turbo`    |
| **Llama 4 Maverick 17B 128E** | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` |
|   **Llama 4 Scout 17B 16E**   |     `meta-llama/Llama-4-Scout-17B-16E-Instruct`     |
|       **Llama 3.3 70B**       |    `klusterai/Meta-Llama-3.3-70B-Instruct-Turbo`    |
|        **Qwen 2.5 7B**        |            `Qwen/Qwen2.5-VL-7B-Instruct`            |

## Model comparison table

|             Model             |                          Main<br>use case                           | Real-time<br>inference support | Batch<br>inference support | Fine-tuning<br>support | Image<br>analysis  | Function<br>calling |
|:-----------------------------:|:-------------------------------------------------------------------:|:------------------------------:|:--------------------------:|:----------------------:|:------------------:|:-------------------:|
|        **DeepSeek R1**        |              Code generation<br>Complex data analysis               |       :white_check_mark:       |     :white_check_mark:     |          :x:           |        :x:         |         :x:         |
|        **DeepSeek V3**        |      Natural language generation<br>Contextually rich writing       |       :white_check_mark:       |     :white_check_mark:     |          :x:           |        :x:         |         :x:         |
|     **DeepSeek V3 0324**      |      Natural language generation<br>Contextually rich writing       |       :white_check_mark:       |     :white_check_mark:     |          :x:           |        :x:         |         :x:         |
|        **Gemma 3 27B**        |  Multilingual applications<br>Image analysis<br>Complex reasoning   |       :white_check_mark:       |     :white_check_mark:     |          :x:           | :white_check_mark: |         :x:         |
|       **Llama 3.1 8B**        |       Low-latency or simple tasks<br>Cost-efficient inference       |       :white_check_mark:       |     :white_check_mark:     |   :white_check_mark:   |        :x:         | :white_check_mark:  |
|      **Llama 3.1 405B**       |                Detailed analysis<br>Maximum accuracy                |       :white_check_mark:       |     :white_check_mark:     |          :x:           |        :x:         | :white_check_mark:  |
|       **Llama 3.3 70B**       |           General-purpose AI<br>Balanced cost-performance           |       :white_check_mark:       |     :white_check_mark:     |   :white_check_mark:   |        :x:         | :white_check_mark:  |
| **Llama 4 Maverick 17B 128E** | Advanced multimodal reasoning<br>Long-context, high-accuracy tasks  |       :white_check_mark:       |     :white_check_mark:     |          :x:           | :white_check_mark: |         :x:         |
|   **Llama 4 Scout 17B 16E**   | Efficient multimodal performance<br>Extended context, general tasks |       :white_check_mark:       |     :white_check_mark:     |          :x:           | :white_check_mark: |         :x:         |
|        **Qwen 2.5 7B**        |    Document analysis<br>Image-based reasoning<br>Multimodal chat    |       :white_check_mark:       |     :white_check_mark:     |          :x:           | :white_check_mark: |         :x:         |

## API request limits

--8<-- "text/get-started/rate-limit.md"

