---
title: Platform Management
description: Enable and manage kluster.ai's Stream HTTP MCP endpoints through the platform UI with one-click setup and visual client examples.
---

# Platform management

Manage your Stream HTTP MCP endpoints directly through the [kluster.ai platform](https://platform.kluster.ai){target=\_blank} interface. Enable your MCP endpoint one click, view your credentials, and access ready-to-use client examples.

This guide shows how to enable MCP through the platform UI and quickly integrate verification tools into your applications.

## Prerequisites

Before getting started with MCP management, ensure the following requirements are met:

- **A kluster.ai account**: Sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one

## Enable MCP endpoint

### Step 1: Access MCP settings

1. Log in to the [kluster.ai platform](https://platform.kluster.ai){target=\_blank}
2. Navigate to **MCP**
3. View your current MCP status

![MCP kluster.ai platform](/images/get-started/mcp/stream-http/platform/platform-get-started.webp)

### Step 2: Enable your endpoint

Click the **Enable Verify MCP** button to activate your endpoint.

The platform will:

- Generate your unique Bearer auth key.
- Activate your endpoint `https://api.kluster.ai/v1/mcp`.
- Display integration examples for popular platforms.


!!! success "Endpoint enabled"
    Your MCP endpoint is now active. Copy your API key and save it securely - you'll need it for all MCP requests.

### Step 3: Copy credentials

After enabling, you'll see:

- **MCP endpoint**: `https://api.kluster.ai/v1/mcp`.
- **Bearer auth key**: (unique to your account).


## Quick integration

The platform provides ready-to-use integrations examples for VSCode, Cursor, Claude code, and cloude dekstop


## Disable endpoint

To temporarily disable your MCP endpoint:

1. Click the **Disable MCP** button
2. Confirm the action

## Next steps

- **Explore the API**: Learn about [API usage and integration patterns](/get-started/mcp/stream-http/api/).
- **View tutorials**: Follow the [reliability check tutorial](/tutorials/klusterai-api/reliability-check/).
- **Check pricing**: Review [MCP usage pricing](https://kluster.ai/pricing){target=\_blank}.