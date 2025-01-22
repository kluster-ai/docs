---
title: Get a kluster.ai API key
description: Follow step-by-step instructions to generate and manage API keys, enabling secure access to kluster's services and seamless integration with your applications.
---

# Generate your kluster.ai API key

The API key is a unique identifier that authenticates requests associated with your account. You must have at least one API key to access **kluster.ai**'s services.

This guide will help you obtain an API key, the first step to leveraging **kluster.ai**'s powerful and cost-effective AI capabilities.

## Create an account

If you haven't already created an account with **kluster.ai**, visit the [registration page](https://platform.kluster.ai/signup){target=\_blank} and take the following steps:

1. Enter your full name
2. Provide a valid email address
3. Create a secure password
4. Click the **Sign up** button

![Signup Page](/images/get-started/get-api-key/get-api-key-1.webp)

## Generate a new API key

After you've signed up or logged into the platform through the [login page](https://platform.kluster.ai/login){target=\_blank}, take the following steps:

1. Select **API Keys** on the left-hand side menu
2. In the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section, click the **Issue New API Key** button

    ![Issue New API Key](/images/get-started/get-api-key/get-api-key-2.webp)

3. Enter a descriptive name for your API key in the popup, then click **Create Key**

    ![Generate API Key](/images/get-started/get-api-key/get-api-key-3.webp)

## Copy and secure your API key

1. Once generated, your API key will be displayed
2. Copy the key and store it in a secure location, such as a password manager

    !!! warning "Warning"
        For security reasons, you won't be able to view the key again. If lost, you will need to generate a new one.

![Copy API key](/images/get-started/get-api-key/get-api-key-4.webp)

!!! abstract "Security tips"
    - **Keep it secret** - do not share your API key publicly or commit it to version control systems
    - **Use environment variables** - store your API key in environment variables instead of hardcoding them
    - **Regenerate if compromised** - if you suspect your API key has been exposed, regenerate it immediately from the **API Keys** section

## Managing your API keys

The **API Key Management** section allows you to efficiently manage your **kluster.ai** API keys. You can create, view, and delete API keys by navigating to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section. Your API keys will be listed in the **API Key Management** section.

To delete an API key, take the following steps:

1. Locate the API key you wish to delete in the list
2. Click the trash bin icon ( :octicons-trash-24: ) in the **Actions** column
3. Confirm the deletion when prompted

![Delete API key](/images/get-started/get-api-key/get-api-key-5.webp)

!!! warning "Warning"
    Once deleted, the API key cannot be used again and you must generate a new one if needed.

## Next steps

Now that you have your API key, you can start integrating **kluster.ai**'s LLMs into your applications. Refer to our [Getting Started](/get-started/start-api/){target=\_blank} guide for detailed instructions on using the API.
