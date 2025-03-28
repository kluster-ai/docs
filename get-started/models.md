---
title: Models
description: Learn what models are supported by kluster.ai API, main characteristics and API request limits for each model for both free and standard tiers.
---

# Models on kluster.ai

[kluster.ai](https://kluster.ai){target=\_blank} offers a wide variety of open-source models for both real time and batch inferences, with more being constantly added. 

This page covers all the different models that are supported by the API, with the API request limits for each.

## Model names

Each model supported by kluster.ai has a unique model that must be used when defining the `model` in the request.

|        Model         |                 Model API name                 |
|:--------------------:|:----------------------------------------------:|
|   **DeepSeek R1**    |           ` deepseek-ai/DeepSeek-R1`           |
|   **DeepSeek V3**    |           ` deepseek-ai/DeepSeek-V3`           |
| **DeepSeek V3 0324** |        ` deepseek-ai/DeepSeek-V3-0324`         |
|   **Gemma 3 27B**    |            `google/gemma-3-27b-it`             |
|   **Llama 3.1 8B**   |  `klusterai/Meta-Llama-3.1-8B-Instruct-Turbo`  |
|  **Llama 3.1 405B**  | `klusterai/Meta-Llama-3.1-405B-Instruct-Turbo` |
|  **Llama 3.3 70B**   | `klusterai/Meta-Llama-3.3-70B-Instruct-Turbo`  |
|   **Qwen 2.5 7B**    |         `Qwen/Qwen2.5-VL-7B-Instruct `         |

## Model comparison table

|        Model         |                                      Main<br>use case                                      | Real-time<br>inference support | Batch<br>inference support | Fine-tuning<br>support | Image<br>analysis  | Function<br>calling |
|:--------------------:|:------------------------------------------------------------------------------------------:|:------------------------------:|:--------------------------:|:----------------------:|:------------------:|:-------------------:|
|   **DeepSeek R1**    |          Mathematical problem-solving<br>code generation<br>complex data analysis          |       :white_check_mark:       |     :white_check_mark:     |          :x:           |        :x:         |         :x:         |
|   **DeepSeek V3**    |    Natural language generation<br>open-ended text creation<br>contextually rich writing    |       :white_check_mark:       |     :white_check_mark:     |          :x:           |        :x:         |         :x:         |
| **DeepSeek V3 0324** |    Natural language generation<br>open-ended text creation<br>contextually rich writing    |       :white_check_mark:       |     :white_check_mark:     |          :x:           |        :x:         |         :x:         |
|   **Gemma 3 27B**    | Multilingual applications<br>extended-context tasks<br>image analysis<br>complex reasoning |       :white_check_mark:       |     :white_check_mark:     |          :x:           | :white_check_mark: |         :x:         |
|   **Llama 3.1 8B**   |                  Low-latency or simple tasks<br>cost-efficient inference                   |       :white_check_mark:       |     :white_check_mark:     |   :white_check_mark:   |        :x:         | :white_check_mark:  |
|  **Llama 3.1 405B**  |               Cutting-edge research<br>detailed analysis<br>maximum accuracy               |       :white_check_mark:       |     :white_check_mark:     |   :white_check_mark:   |        :x:         | :white_check_mark:  |
|  **Llama 3.3 70B**   |                      General-purpose AI<br>balanced cost-performance                       |       :white_check_mark:       |     :white_check_mark:     |   :white_check_mark:   |        :x:         | :white_check_mark:  |
|   **Qwen 2.5 7B**    | Visual question answering<br>document analysis<br>image-based reasoning<br>multimodal chat |       :white_check_mark:       |     :white_check_mark:     |          :x:           | :white_check_mark: |         :x:         |

## API request limits

--8<-- "text/get-started/rate-limit.md"

