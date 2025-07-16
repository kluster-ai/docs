---
title: Integrate Guardrails with kluster.ai API
description: Learn how to integrate kluster.ai Verify validator with Guardrails, a framework for validating and structuring LLM outputs, to detect hallucinations in AI-generated content.
---

# Integrate Guardrails with kluster.ai

[Guardrails](https://www.guardrailsai.com/){target=_blank} is an open-source framework designed to validate, structure, and correct the outputs of large language models (LLMs). It enables developers to define validation rules and constraints, ensuring AI-generated content meets specific quality and accuracy standards while providing mechanisms to handle failures gracefully.

This guide walks you through integrating the [kluster.ai Verify validator](https://github.com/kluster-ai/verify-guardrails-validator){target=_blank} with Guardrails to detect and prevent hallucinations and ensure AI-generated content meets your quality standards.

## Prerequisites

Before starting, ensure you have the following prerequisites:

--8<-- 'text/kluster-api-onboarding.md'
- **Guardrails installed**: Install Guardrails with `pip install guardrails-ai>=0.4.0`. The kluster.ai validator also requires `requests>=2.25.0`

## Install from Guardrails Hub

Install the kluster.ai Verify validator from the Guardrails Hub using the following command:

```bash
guardrails hub install hub://kluster/verify
```

## Validate AI-generated content

After installation, you can use the validator to detect hallucinations in AI-generated content. The validator can work in two modes: without context for general knowledge verification, or with context for RAG applications.

### Validation without context

Use this mode to verify general knowledge and factual accuracy:

```python
from guardrails import Guard
from guardrails.hub import KlusterVerify

# Setup Guard
guard = Guard().use(KlusterVerify, on_fail="exception")

# Test 1: Validate accurate content
result = guard.validate(  # Returns ValidationOutcome object
    "The capital of France is Paris.",
    metadata={"prompt": "What is the capital of France?"}
)

# Display validation results
print(f"✅ Validation passed: {result.validation_passed}")
print(f"📝 Call ID: {result.call_id}")
print(f"💬 Validated output: {result.validated_output}")

# Test 2: Intentionally provide wrong answer to test validation
try:
    result = guard.validate(
        "The capital of France is London.",  # Wrong answer for testing
        metadata={"prompt": "What is the capital of France?"}
    )
except Exception as e:
    print(f"❌ Validation failed: {e}")
```

Expected output:
```console
✅ Validation passed: True
📝 Call ID: 4995163360
💬 Validated output: The capital of France is Paris.
❌ Validation failed: Validation failed for field with errors: Potential hallucination detected: The user asked for the capital of France.
The correct capital of France is Paris, not London.
London is the capital of England, not France, making the response factually incorrect.
```

### Validation with context

For RAG applications, provide context to verify that responses accurately reflect the source documents. The context should contain the actual text from your reference documents:

```python
from guardrails import Guard
from guardrails.hub import KlusterVerify

# Setup Guard
guard = Guard().use(KlusterVerify)

# Define context from your reference documents
context = "InvID:INV7701B Date:22May25"  # Example: invoice data from your document

# Validate that the AI response accurately reflects the context
result = guard.validate(  # Returns ValidationOutcome object
    "The invoice date is May 22, 2025",
    metadata={
        "prompt": "What's the invoice date?",
        "context": context
    }
)

# Display comprehensive validation results
print(f"✅ Validation passed: {result.validation_passed}")
print(f"📝 Call ID: {result.call_id}")
print(f"📄 Raw LLM output: {result.raw_llm_output}")
print(f"✨ Validated output: {result.validated_output}")
```

Expected output:
```console
✅ Validation passed: True
📝 Call ID: 4687733984
📄 Raw LLM output: The invoice date is May 22, 2025
✨ Validated output: The invoice date is May 22, 2025
```

## Working with ValidationOutcome

The `ValidationOutcome` object returned by Guardrails provides rich information about the validation process. For complete documentation, see the [official Guardrails API reference](https://www.guardrailsai.com/docs/api_reference_markdown/guards){target=_blank}.

### Key attributes

- **`call_id`**: Unique identifier for the validation call
- **`validation_passed`**: Boolean indicating if validation succeeded
- **`raw_llm_output`**: Original unmodified output from the LLM
- **`validated_output`**: Output after validation and potential fixes
- **`validation_summaries`**: List of validation summaries from the process
- **`error`**: Error message if validation failed (None if successful)
- **`reask`**: Contains reask message if validation needs retry (None if successful)

For more detailed examples and advanced usage, check out the [reliability check tutorial](/tutorials/klusterai-api/reliability-check/){target=_blank}.