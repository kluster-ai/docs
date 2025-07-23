---
title: Get started with MCP
description: Get kluster.ai verification tools integrated into Claude desktop in five minutes using Cloud MCP. No setup required, just enable and connect.
---

# Get started with MCP

Connect [kluster.ai's](https://www.kluster.ai/){target=\_blank} verification tools to your AI assistant through Model Context Protocol (MCP). This guide shows you how to enable [Cloud MCP](/verify/mcp/cloud/platform/) and integrate it with Claude desktop for real-time claim validation directly within your conversations.

Cloud MCP provides managed verification endpoints with no infrastructure to maintain - just enable your MCP endpoint and start verifying.

## Prerequisites

Before getting started, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'
- **[Claude desktop](https://claude.ai/download){target=\_blank}** for testing the integration.

## Enable MCP 

To enable the MCP endpoint, go to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank} and take the following steps:

1. Navigate to **MCP** and view your current MCP status.
2. Click the **Enable Verify MCP** button to activate your endpoint.
3. Copy your client configuration.

!!! success "Endpoint enabled"
    Your MCP endpoint is now active. Copy your API key and save it securely.
    
The platform provides ready-to-use integration examples for VSCode, Cursor, Claude code, and Claude desktop.

![MCP kluster.ai platform](/images/verify/mcp/cloud/platform/platform-1.webp)

## Configure Claude desktop

Edit your Claude desktop configuration file:

=== "macOS"

    ```text
    ~/Library/Application Support/Claude/claude_desktop_config.json
    ```

=== "Windows"

    ```text
    %APPDATA%/Claude/claude_desktop_config.json
    ```

Add the MCP server configuration:

```json
--8<-- 'code/verify/mcp/get-started/get-started-1.json'
```

Replace `YOUR_MCP_TOKEN` with your actual token or copy the snippet from the platform.

Restart Claude desktop. Once Claude desktop restarts, you'll see the verification tools available under `kluster-verify-mcp`.

![List tools on Claude desktop](/images/verify/mcp/get-started/get-started-1.webp)

## Available tools

Your MCP integration provides two verification tools:

--8<-- 'text/verify/mcp/overview/overview-1.md'


### Verify

Ask Claude to verify something obviously wrong:

> "The Eiffel Tower is located in Rome. Use the verify tool to check this."

Claude will automatically use the `verify` tool with:

- **`prompt`**: "Is the Eiffel Tower located in Rome?"
- **`response`**: "The Eiffel Tower is located in Rome."

And provides the following:

- **Verification result**: Whether the response contains hallucinations.
- **Detailed explanation**: Why it's wrong with supporting reasoning.
- **Source citations**: Search results used for verification.

![Verify MCP tool demo](/images/verify/mcp/get-started/get-started-2.webp)

### Verify documents

Perfect for detecting hallucinations or false claims about documents. Upload any document to Claude, then ask:

> "Does this document say that employees can work remotely full-time? The document says employees can work remotely without restrictions. Use the verify_document tool to check."

Claude will use the `verify_document` tool with:

- **`prompt`**: "Does this document say that employees can work remotely full-time?"
- **`response`**: "The document says employees can work remotely without restrictions."
- **`documentContent`**:  The content of the document as provided by the MCP client for verification.

This verifies the response against the actual document content.

## Alternative setup options

- **Other clients**: Want to use VS Code, Cursor, or Claude Code? Check the [Client integrations](/verify/mcp/integrations/){target=\_blank} guide for configuration examples.

- **Self-hosted**: Prefer to run MCP locally? Set up the [self-hosted MCP server](/verify/mcp/self-hosted/){target=\_blank} for local development with full control.

- **API activation**: Enable MCP using API calls with the [MCP API usage guide](/verify/mcp/cloud/api/){target=\_blank}.

## Next steps

- **Explore integrations**: Check [Client integrations](/verify/mcp/integrations/) for other platforms.

- **Try the tutorial**: Follow the [Reliability check notebook](/tutorials/klusterai-api/reliability/) with code examples.