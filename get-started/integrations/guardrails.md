---
title: Integrate Guardrails with kluster.ai API
description: Learn how to integrate kluster.ai Verify validator with Guardrails, a framework for validating and structuring LLM outputs, to detect hallucinations in AI-generated content.
---

# Integrate Guardrails with kluster.ai

[Guardrails](https://www.guardrailsai.com/){target=\_blank} is an open-source framework designed to validate, structure, and correct the outputs of large language models (LLMs). It enables developers to define validation rules and constraints, ensuring AI-generated content meets specific quality and accuracy standards while providing mechanisms to handle failures gracefully.

This guide walks you through integrating [kluster.ai Verify validator](https://github.com/kluster-ai/verify-guardrails-validator){target=\_blank} with Guardrails to validate AI-generated content and detect hallucinations using the kluster.ai Verify service.

## Prerequisites

Before starting, ensure you have the following prerequisites:

--8<-- 'text/kluster-api-onboarding.md'
- **Guardrails installed**: Install Guardrails with `pip install guardrails-ai>=0.4.0`. The kluster.ai validator also requires `requests>=2.25.0`.

## Install from Guardrails Hub

Install the kluster.ai Verify validator from the Guardrails Hub with the following command:

```bash
guardrails hub install hub://kluster/verify
```

## Validate AI-generated content

After installation, you can use the validator to detect hallucinations in AI-generated content. The validator can work in two modes: without context for general knowledge verification, or with context for RAG applications.

### Validation without context

Use this mode to verify general knowledge and factual accuracy:

```python
# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import KlusterVerify

# Setup Guard
guard = Guard().use(KlusterVerify, on_fail="exception")

# Validate accurate content
response = guard.validate(
    "The capital of France is Paris.",
    metadata={"prompt": "What is the capital of France?"}
)  # Validator passes

# Validate inaccurate content
try:
    response = guard.validate(
        "The capital of France is London.",
        metadata={"prompt": "What is the capital of France?"}
    )  # Validator fails
except Exception as e:
    print(e)
```

Expected output:
```console
Validation failed for field with errors: Potential hallucination detected: The user asked for the capital of France.
The correct capital of France is Paris, not London.
London is the capital of England, not France, making the response factually incorrect.
```

### Validation with context

For RAG applications, provide context to verify that responses accurately reflect the provided reference documents:

```python
# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import KlusterVerify

# Setup Guard
guard = Guard().use(KlusterVerify)

# Define context from your documents
context = "InvID:INV7701B Date:22May25"

# Validate response against context
result = guard.validate(
    "The invoice date is May 22, 2025",
    metadata={
        "prompt": "What's the invoice date?",
        "context": context
    }
)

print(f"Result: {'✅ PASSED' if result.validation_passed else '❌ FAILED'}")
```

Expected output:
```console
Result: ✅ PASSED
```

For more detailed examples and advanced usage, check out the [reliability check tutorial](/tutorials/klusterai-api/reliability-check/){target=_blank}.

And that's it! You've successfully integrated Guardrails with kluster.ai to detect hallucinations in AI-generated content!