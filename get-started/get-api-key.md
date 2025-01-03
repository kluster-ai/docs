---
title: Get an API key
description: The API key Setup Guide provides step-by-step instructions for generating and managing your personal API key, enabling secure access to our services and ensuring seamless integration with your applications.
---

# Generate your kluster.ai API key

[Kluster.ai](https://www.kluster.ai/){target=\_blank}  provides a unique API service with an Adaptive Inference service that dynamically scales resources for high-volume, asynchronous processing, delivering lower costs than traditional batch solutions.

This guide helps you obtain an API key, the first step to leveraging kluster.ai's powerful and cost-effective AI capabilities.


## Step 1 - create an account

If you haven't already created an account with kluster.ai:

- Visit the [kluster.ai registration page](https://platform.kluster.ai/signup){target=\_blank}
- Fill in Your Details:
    - `Full name` - enter your full name
    - `Email` - provide a valid email address
    - `Password` - create a secure password
- Complete Registration:
   - Click the **Sign up** button

![Signup Page](/images/get-started/key-gen/sign-up.png){width=400px}

## Step 2 - generate a new API key
1. Log in to the platform through the [kluster.ai login page](https://platform.kluster.ai/login){target=\_blank} and select **API Keys** on the left-hand side menu
2. In the [API Keys](https://platform.kluster.ai/apikeys){target=\_blank} section, click the **Issue New API Key** button.

    ![Issue New API Key](/images/get-started/key-gen/api-key-management.png)

3. Enter a descriptive name for your API key in the popup, then click **Create Key** to generate it.

![Generate API Key](/images/get-started/key-gen/create-new-api-key.png){ width=400px }

## Step 3 - copy and secure your API key
1. Once generated, your API key will be displayed.
2. **Copy** the key and store it in a secure location.

!!! warning "Warning"
    For security reasons, you won't be able to view the key again. If lost, you will need to generate a new one.

!!! abstract "Security tips"
    - **Keep it secret** - do not share your API key publicly or commit it to version control systems.
    - **Use environment variables** - store your API key in environment variables instead of hardcoding them.
    - **Regenerate if compromised** - if you suspect your API key has been exposed, regenerate it immediately from the **API Keys** section.

!!! tip "Troubleshooting"
    - **Unable to generate API key** - ensure you are logged into your kluster.ai account.
    - **API key not working** - verify that you have copied the entire key without extra spaces.
    - **Need further assistance?** Contact our [Support Team](https://calendly.com/klusterai-jacob/support-call){target=\_blank}.

## API key management

Manage your API keys efficiently. You can handle multiple API keys and delete them as needed:

- **Navigate to API keys** - go to the [API Keys](https://platform.kluster.ai/apikeys){target=\_blank} section
- **View your keys** - all your API keys will be listed in the **API Keys Management** section
- **Delete an API key:**
    - Locate the API key you wish to delete in the list
    - Click the trash bin icon ( :octicons-trash-24: ) in the **Actions** column
    - Confirm the deletion when prompted

!!! warning "Warning"
    Once deleted, the api key cannot be used again and you must generate a new one if needed

## Next steps
Now that you have your API key, you can start integrating kluster.ai's LLMs into your applications. Refer to our [Getting Started](/tutorials/klusterai-api/getting-started/){target=\_blank} for detailed instructions on using the API.