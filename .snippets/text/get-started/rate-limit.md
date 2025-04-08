The following limits apply to API requests based on [your plan tier](https://platform.kluster.ai/plans){target=\_blank}:

=== "Trial"

    |             Model             | Context<br>size | Max<br>output | Max batch<br>requests | Concurrent<br>requests | Requests<br>per minute | Hosted fine-tuned<br>models |
    |:-----------------------------:|:---------------:|:-------------:|:---------------------:|:----------------------:|:----------------------:|:---------------------------:|
    |        **DeepSeek R1**        |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    |        **DeepSeek V3**        |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    |     **DeepSeek V3 0324**      |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    |        **Gemma 3 27B**        |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    |       **Llama 3.1 8B**        |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    |      **Llama 3.1 405B**       |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    |       **Llama 3.3 70B**       |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    | **Llama 4 Maverick 17B 128E** |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    |   **Llama 4 Scout 17B 16E**   |       32k       |      4k       |         1000          |           20           |           30           |              1              |
    |        **Qwen 2.5 7B**        |       32k       |      4k       |         1000          |           20           |           30           |              1              |

    

=== "Core"

    |             Model             | Context<br>size | Max<br>output | Max batch<br>requests | Concurrent<br>requests | Requests<br>per minute | Hosted fine-tuned<br>models |
    |:-----------------------------:|:---------------:|:-------------:|:---------------------:|:----------------------:|:----------------------:|:---------------------------:|
    |        **DeepSeek R1**        |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    |        **DeepSeek V3**        |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    |     **DeepSeek V3 0324**      |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    |        **Gemma 3 27B**        |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    |       **Llama 3.1 8B**        |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    |      **Llama 3.1 405B**       |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    |       **Llama 3.3 70B**       |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    | **Llama 4 Maverick 17B 128E** |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    |   **Llama 4 Scout 17B 16E**   |       Max       |      Max      |         100k          |          100           |          600           |             10              |
    |        **Qwen 2.5 7B**        |       Max       |      Max      |         100k          |          100           |          600           |             10              |

=== "Scale"

    |             Model             | Context<br>size | Max<br>output | Max batch<br>requests | Concurrent<br>requests | Requests<br>per minute | Hosted fine-tuned<br>models |
    |:-----------------------------:|:---------------:|:-------------:|:---------------------:|:----------------------:|:----------------------:|:---------------------------:|
    |        **DeepSeek R1**        |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    |        **DeepSeek V3**        |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    |     **DeepSeek V3 0324**      |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    |        **Gemma 3 27B**        |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    |       **Llama 3.1 8B**        |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    |      **Llama 3.1 405B**       |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    |       **Llama 3.3 70B**       |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    | **Llama 4 Maverick 17B 128E** |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    |   **Llama 4 Scout 17B 16E**   |       Max       |      Max      |         500k          |          100           |          1200          |             25              |
    |        **Qwen 2.5 7B**        |       Max       |      Max      |         500k          |          100           |          1200          |             25              |

=== "Enterprise"

    |             Model             | Context<br>size | Max<br>output | Max batch<br>requests | Concurrent<br>requests | Requests<br>per minute | Hosted fine-tuned<br>models |
    |:-----------------------------:|:---------------:|:-------------:|:---------------------:|:----------------------:|:----------------------:|:---------------------------:|
    |        **DeepSeek R1**        |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    |        **DeepSeek V3**        |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    |     **DeepSeek V3 0324**      |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    |        **Gemma 3 27B**        |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    |       **Llama 3.1 8B**        |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    |      **Llama 3.1 405B**       |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    |       **Llama 3.3 70B**       |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    | **Llama 4 Maverick 17B 128E** |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    |   **Llama 4 Scout 17B 16E**   |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
    |        **Qwen 2.5 7B**        |       Max       |      Max      |       Unlimited       |          100           |       Unlimited        |          Unlimited          |
