---
title: Integrate Immersive Translate
description: Learn how to integrate the Immersive Translate browser extension with kluster.ai in your workflows for seamless, real-time multilingual content handling.
---

# Integrate Immersive Translate with kluster.ai

[Immersive Translate](https://immersivetranslate.com/){target=_blank} is an  AI-powered bilingual translation extension that automatically identifies the main text on any web page and provides parallel translations in real-time. This context-driven approach streamlines reading and collaboration across languages with additional features like efficient document translation, hover translation, and support for 10+ translation services.

In this guide, you'll learn how to integrate Immersive Translate with the [kluster.ai](https://www.kluster.ai/){target=_blank} API—from installation through configuration—so you can seamlessly handle multilingual content within your workflows. You will enable Immersive Translate's core capabilities with kluster.ai's powerful models, helping you build more robust and accessible AI-driven applications.

## Prerequisites

Before starting, ensure you have the following:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide
- **Installed the Immersive Translate plugin** - you can download the Immersive Translate plugin for your respective browser on the [Immersive Translate homepage](https://immersivetranslate.com/){target=\_blank}

## Configure Immersive Translate

First, open the Immersive Translate extension and click on the **Options** button in the lower left corner of the extension.

![](/images/get-started/integrations/immersivetranslate/immersive-1.webp)

Then, take the following steps:

1. Navigate to **Translatation Services**
2. Press **Add OpenAI Compatible Service**

![](/images/get-started/integrations/immersivetranslate/immersive-2.webp)

Take the following steps to configure the kluster.ai API as a custom translation service for Immersive Translate:

1. Enter a name
2. For the custom API interface address, enter the following:

    ```text
    https://api.kluster.ai/v1/chat/completions
    ```

3. Paste in your kluster.ai [API key](https://platform.kluster.ai/apikeys){target=\_blank}
4. **Check** the box to enable custom models 
5. Paste in the name of the kluster.ai [supported model](https://docs.kluster.ai/api-reference/reference/#list-supported-models){target=\_blank} you'd like to use
6. Specify a value of `1` for max requests per second to avoid rate limits. Paid kluster.ai API accounts may have higher rate limits
7. Press **Verify Service** in the upper right corner to validate the input values

![](/images/get-started/integrations/immersivetranslate/immersive-3.webp)

You must take one more step before using kluster.ai with Immersive Translate. Although kluster.ai has been added as a provider, it is disabled by default. To enable it, take the following steps:

1. Click on the **Translation Services** section of settings
2. Toggle the switch to enable kluster.ai as a provider

That's it! The next section will demonstrate using Immersive Translate with the kluster.ai API to perform webpage translations.

![](/images/get-started/integrations/immersivetranslate/immersive-4.webp)

## Translate content

With Immersive Translate, you can easily translate content with just a few clicks. To do so, navigate to the page with the foreign language content. Open the Immersive Translate plugin and take the following steps:

1. The language of the existing content is auto-detected by the plugin, but it's a good idea to verify it
2. Select the language to translate the content into. This is set by default to your native language 
3. Press **Translate**

![](/images/get-started/integrations/immersivetranslate/immersive-5.webp)

Then, the content translated by the Immersive Translate plugin will begin to appear on the page. 

![](/images/get-started/integrations/immersivetranslate/immersive-6.webp)

And that's it! You've now set up Immersive Translate to use the kluster.ai API and learned how to translate content.
