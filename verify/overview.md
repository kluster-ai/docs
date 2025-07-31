---
title: Overview of Verify
description: Learn more about the Verify service, a trust layer for AI stacks that provides a set of features to validate LLM outputs in real-time.
---

# Verify

LLMs can generate non-factual or irrelevant information (hallucinations). For developers, this presents significant challenges:

- Difficulty in programmatically trusting LLM outputs.
- Increased complexity in error handling and quality assurance.
- Potential for cascading failures in chained AI operations.
- Requirement for manual review cycles, slowing down development and deployment.

Traditional validation methods may involve complex rule sets, fine-tuning, or exhibit high false-positive rates, adding to the development burden.

Verify is an intelligent verification service that validates LLM outputs in real-time. It's designed to give you the trust needed to deploy AI at scale in production environments where accuracy matters most.

This page provides an overview of the Verify service.

## How Verify works

Verify offers two specialized products, each designed to address specific AI validation needs:

- **[Reliability](/verify/reliability/overview/)**: An intelligent verification service that validates LLM outputs in real-time. It assesses output reliability based on prompts, outputs, and optional context, leveraging real-time internet access to validate claims against up-to-date public information.

- **[Code](/verify/code/overview/)**: A specialized verification service for AI-generated code that identifies bugs, security vulnerabilities, and quality issues. It analyzes code changes in diff format and provides detailed explanations with actionable fixes.


## Target applications & use cases

Developers can integrate Verify products into applications where AI output quality is paramount:

**For Reliability:**

- Automated content generation pipelines.
- Customer-facing chatbots and virtual assistants.
- Question-answering systems over private or public data (RAG).
- AI-driven data extraction and summarization tools.
- Internal workflow automation involving LLM-generated text.

**For Code:**

- AI coding assistants and IDE integrations.
- Automated code review pipelines.
- CI/CD security scanning for AI-generated code.
- Development workflow automation.
- Code quality assurance systems.

## Choose your Verify product

<div class="grid cards" markdown>

-   <span class="badge product">Product</span> __Reliability__

    ---

    Validate LLM outputs for accuracy and prevent hallucinations in your AI applications.

    [:octicons-arrow-right-24: Explore Reliability](/verify/reliability/overview/){target=\_blank}

-   <span class="badge product">Product</span> __Code__

    ---

    Detect bugs and security issues in AI-generated code before they reach production.

    [:octicons-arrow-right-24: Explore Code](/verify/code/overview/){target=\_blank}

</div>
