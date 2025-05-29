---
title: Launch dedicated endpoints
description: Deploy private model instances on kluster.ai with dedicated hardware, full control, and transparent per-hour pricing. No per-token fees, just predictable costs.
---

# Dedicated deployments

Dedicated deployments let you run a private instance of any [Hugging Face text model](https://huggingface.co/models){target=\_blank} on hardware reserved just for you. Enjoy full control, predictable per‑minute billing, and zero per‑token costs.

This page covers how to create, use, and stop your dedicated deployments.

## Create a deployment

Ensure you're logged in to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank}, then navigate to the [**Dedicated deployments**](https://platform.kluster.ai/dedicated-deployments){target=\_blank} page, then press **Launch deployment**.

![Launch deployment](/images/get-started/dedicated-endpoints/dedicated-1.webp)

Then, complete the following fields to configure your deployment:

1. **Deployment name**: Enter a clear deployment name (e.g., `mydedicated`) so you can spot it later in the console.
2. **Model selection**: Paste the Hugging Face model ID or URL (e.g., `deepseek-ai/DeepSeek-R1`). If the model is private, provide a Hugging Face access token.
3. **Select hardware**: Confirm a GPU configuration.
4. **Specify auto-shutdown**: Set an auto‑shutdown window for your instance to power down after a specified period of inactivity, between 15 minutes to 12 hours. 
4. **Launch**: Review the estimated price and then Click **Launch deployment**. Spin‑up takes ≈10–20 min; once the status shows `Running`, copy the endpoint ID, as you'll use that to submit requests. 

![Configure deployment](/images/get-started/dedicated-endpoints/dedicated-2.webp)


## Use your dedicated deployment

After waiting 10-20 minutes for your instance to spin up, you can call it by using the endpoint ID as the model name when making a request. If you're unsure of your endpoint ID, look for it in the [**Dedicated deployments** page](https://platform.kluster.ai/dedicated-deployments){target=\_blank}.

![Copy endpoint ID](/images/get-started/dedicated-endpoints/dedicated-3.webp)

To call your dedicated endpoint, you'll need to provide the endpoint ID as the model name when making a request (`INSERT_ENDPOINT_ID` in the following example):

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_API_KEY",
        base_url="https://api.kluster.ai/v1"
    )

    response = client.chat.completions.create(
        model="INSERT_ENDPOINT_ID",   # Your endpoint ID
        messages=[{"role": "user", "content": "What is the best taco place in SF?"}],
    )

    print(response.choices[0].message.content)
    ```

=== "curl"

    ```bash
    curl https://api.kluster.ai/v1/chat/completions \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "INSERT_ENDPOINT_ID",
        "messages": [{"role": "user", "content": "What is the best taco place in SF?"}]
      }'
    ```

## Stop your deployment

Click **Stop** next to your deployment on the [**Dedicated Deployments**](https://platform.kluster.ai/dedicated-deployments){target=\_blank} page to shut your VM down immediately. Billing ends the moment it powers off. Otherwise, an auto‑shutdown timer kicks in after your specified auto-shutdown period (between 15 minutes to 12 hours of inactivity), depending on the period you chose when spinning up the instance. 

![Stop deployment](/images/get-started/dedicated-endpoints/dedicated-4.webp)

Questions? Email [support@kluster.ai](mailto:support@kluster.ai), and we’ll be happy to help!
