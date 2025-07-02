---
title: Integrate Llama OCR with kluster.ai API
description: Learn how to use kluster.ai as an LLM provider for the Llama OCR NPM library to run vision-enabled OCR with any multimodal model on the kluster.ai platform.
---

# Integrate Llama OCR with kluster.ai

[Llama OCR](https://llamaocr.com/){target=\_blank} is an NPM library that converts images into richly formatted Markdown by sending the image and a conversion prompt to a vision-capable LLM. Llama OCR is compatible with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API with just a few changes.

Note that not all models supported by kluster.ai are capable of processing images. The [vision-capable models](/get-started/models/){target=\_blank} currently supported by kluster.ai include:

- **`google/gemma-3-27b-it`** - Google's Gemma 3 model with vision capabilities.
- **`Qwen/Qwen2.5-VL-7B-Instruct`** - Qwen's visual language model.
- **`meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`** - Meta's Llama 4 Maverick model.
- **`meta-llama/Llama-4-Scout-17B-16E-Instruct`** - Meta's Llama 4 Scout model.

This guide walks you through the minimal changes needed to:

- Clone the repo and install the dependencies.
- Configure kluster.ai as the provider.
- Run a working end-to-end OCR example against the sample grocery receipt image that ships with the repo.

## Prerequisites

--8<-- 'text/kluster-api-onboarding.md'
- Node version 18 or higher

You can clone the Llama OCR repo and install the required dependencies with the following commands:

```bash
git clone https://github.com/Nutlope/llama-ocr.git
cd llama-ocr
npm install
```

Additionally, you must install the OpenAI package to interact with kluster.ai's OpenAI-compatible API:

```bash
npm install openai
```

## Modify the OCR function

Navigate to the `src` folder, find the `index.ts` file, and make the following changes:

1. Update the imports: 
```typescript
--8<-- "code/get-started/integrations/llama-ocr/index.ts::3"
```

2. Modify the OCR function signature as follows: 
```typescript
--8<-- "code/get-started/integrations/llama-ocr/index.ts:4:12"
```

3. Initialize the OpenAI client with kluster.ai endpoint:
```typescript
--8<-- "code/get-started/integrations/llama-ocr/index.ts:13:16"
```

4. Revise the `getMarkdown` function to use the OpenAI SDK:
```typescript
--8<-- "code/get-started/integrations/llama-ocr/index.ts:20:"
```

You can find the full contents of the revised `index.ts` below:

??? code "View complete script"
    ```typescript title="src/index.ts"
    --8<-- "code/get-started/integrations/llama-ocr/index.ts"
    ```

## Create and run a test file

The below example demonstrates calling the `ocr` function from the `src/index.ts` file by passing in the file path of the image to process, along with the kluster.ai model you'd like to use and your kluster API key. Since the example grocery receipt is located in the `test` folder, you might wish to create the below file in the same directory:

```typescript title="test-receipt.ts"
import { ocr } from '../src/index';

(async () => {
  const markdown = await ocr({
    filePath: './trader-joes-receipt.jpg',
    model: 'google/gemma-3-27b-it', // Use a vision-enabled model
    apiKey: 'INSERT_API_KEY',
  });

  console.log(markdown);
})();
```

You can run the above script with the following command:

```bash
ts-node test-receipt.ts
```

The output will look similar to the following:

```txt
# Trader Joe's

785 Oak Grove Road
Concord, CA 94518
Store #0083 - 925 521-1134

SALE TRANSACTION

SOUR CREAM & ONION CORN  $2.49
SLICED WHOLE WHEAT BREAD $3.99
RICE CAKES KOREAN TTEOK $2.99
SQUASH ZUCCHINI 1.5 LB $2.49
GREENS KALE 10 OZ $1.99
SQUASH SPAGHETTI 1 EA $2.49
50% LESS SALT ROASTED SA $2.99
BANANA EACH $1.14
6 @ $0.19

PASTA GNOCCHI PRANZO $1.99
ORG COCONUT MILK $1.69
ORG YELLOW MUSTARD $1.79
HOL TRADITIONAL ACTIVE D $1.29

Items in Transaction: 17
Balance to pay $26.83
Gift Card Tendered $25.00
Visa Debit $1.83

PAYMENT CARD PURCHASE TRANSACTION
CUSTOMER COPY
```
## Summary

You've successfully integrated kluster.ai with Llama OCR. This allows you to extract text from images using kluster.ai's powerful vision-capable models and convert them into clean, structured markdown format.

Some potential use cases for this integration include:

- Processing receipts for expense tracking.
- Digitizing printed documents.
- Converting handwritten notes to digital text.
- Extracting text from screenshots.
- Processing business cards.

Experiment with different kluster.ai models to find the best one for your specific OCR needs. The OCR quality may vary depending on the image quality, text clarity, and the specific model used.