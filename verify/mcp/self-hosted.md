---
title: Self-hosted MCP
description: Deploy kluster.ai's MCP server locally using Docker or Node.js for development and testing with full control over your infrastructure.
---

# Self-hosted MCP

Deploy [kluster.ai's](https://www.kluster.ai/){target=\_blank} MCP server locally for development and testing. This self-hosted implementation gives you full control over your infrastructure while providing the same verification tools as [Cloud MCP](/verify/mcp/cloud/platform/){target=\_blank}.

## Prerequisites

Before deploying the self-hosted MCP server, ensure you have:

--8<-- 'text/kluster-api-onboarding.md'
- **A runtime environment**: You can use either [Docker Desktop](https://www.docker.com/products/docker-desktop/){target=\_blank} or [Node.js 18+](https://nodejs.org/){target=\_blank}.
- **[Git](https://git-scm.com/){target=\_blank}**: For cloning the repository.

## Clone repository

First, clone the MCP server repository:

```bash
git clone https://github.com/kluster-ai/verify-mcp
cd verify-mcp
```

## Deployment options

Run one of the following commands to either get started with Docker or Node.js:

=== "Docker"

    ```bash
    docker build -t kluster-verify-mcp .
    docker run --rm -p 3001:3001 kluster-verify-mcp --api-key YOUR_API_KEY
    ```

=== "Node.js"

    ```bash
    npm install
    npm run build
    npm start -- --api-key YOUR_API_KEY
    ```

The server will start on `http://localhost:3001` with the MCP endpoint at `/stream`.

## Client integration

Once your self-hosted server is running, configure your AI clients using the [Client integrations](/verify/mcp/integrations/){target=\_blank} guide.

Use these connection details:

- **MCP endpoint**: `http://localhost:3001/stream`.
- **Authentication**: Your kluster.ai API key.

## Available tools

Your self-hosted deployment provides the same verification tools as Cloud MCP:

--8<-- 'text/verify/mcp/overview/overview-1.md'
<!-- Commenting this for safekeeping -->
<!--For detailed parameters and response formats, see the [Tools reference](/verify/mcp/tools/){target=\_blank}.-->

## Next steps

- **Configure clients**: Follow the [Client integrations](/verify/mcp/integrations/) guide for VS Code, Claude Desktop, and other platforms.
<!-- Commenting this for safekeeping -->
<!--- **Learn the tools**: See [Tools reference](/verify/mcp/tools/) for detailed examples.-->
- **Try Cloud MCP**: Consider [Cloud MCP](/verify/mcp/cloud/platform/) for managed cloud deployment.