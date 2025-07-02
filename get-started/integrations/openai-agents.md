---
title: Integrate OpenAI Agents SDK with kluster.ai
description: Learn how to enhance OpenAI agents with kluster.ai's MCP verify tools for reliable information validation
---

# Integrate OpenAI Agents SDK with kluster.ai

[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/){target=_blank} is a Python framework for building stateful, structured AI agents that can use tools and maintain conversation history. By integrating with kluster.ai's Model Context Protocol (MCP) server, your agents gain access to powerful verification tools that can validate claims and information in real-time.

## Prerequisites

Before getting started with OpenAI Agents integration, ensure the following requirements are met:

--8<-- 'text/kluster-api-onboarding.md'
- **Python 3.9 or higher** with pip package manager
- **OpenAI Agents SDK**: Install with `pip install openai-agents`
- **MCP enabled**: Enable MCP for your account via the [platform](https://platform.kluster.ai){target=_blank} or [API](/get-started/mcp/cloud/api/){target=_blank}

## Quick Start

Here's a minimal example to get your OpenAI agent connected with kluster.ai's MCP verify tools:

```python
from agents import Agent
from agents.mcp.server import MCPServerStreamableHttp
import asyncio
import os

# Configure MCP server for kluster.ai
mcp_server = MCPServerStreamableHttp(
    params={
        "url": "https://api.kluster.ai/v1/mcp",
        "headers": {"Authorization": f"Bearer {os.getenv('KLUSTER_MCP_TOKEN')}"}
    }
)

# Create agent with MCP tools
agent = Agent(
    name="VerifyAgent",
    instructions="You are a helpful assistant that verifies information using available tools.",
    mcp_servers=[mcp_server]
)

# Run the agent
async def main():
    response = await agent.run("Is the Earth flat?")
    print(response.content)

if __name__ == "__main__":
    asyncio.run(main())
```

!!! note "Self-hosted MCP"
    If you're using self-hosted MCP, change the URL to `http://localhost:3001/stream` and use your kluster.ai API key directly in the Authorization header instead of an MCP token.

## Enable MCP and get your token

To access kluster.ai's MCP verification tools, you need to enable MCP and obtain your MCP token. You can do this through the [platform interface](/get-started/mcp/cloud/platform/){target=_blank} or programmatically:

```python
import requests
import os

# Enable MCP using your API key
api_key = os.getenv("KLUSTER_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}

# Enable MCP
enable_response = requests.post(
    "https://api.kluster.ai/v1/mcp/enable",
    headers=headers
)

if enable_response.status_code == 200:
    # Get MCP status to retrieve token
    status_response = requests.get(
        "https://api.kluster.ai/v1/mcp/status",
        headers=headers
    )
    mcp_token = status_response.json()["mcp_token"]
    print(f"MCP Token: {mcp_token}")
else:
    print("Failed to enable MCP")
```

## Create agents for comparison

Let's build a comparison between two agents - one with MCP verify tools and one without - to showcase the power of kluster.ai's verification capabilities:

```python
from agents import Agent
from agents.mcp.server import MCPServerStreamableHttp

# Agent WITHOUT MCP verify tools
basic_agent = Agent(
    name="BasicAgent",
    model="gpt-4",
    instructions="You are a helpful assistant that answers questions to the best of your knowledge."
)

# Agent WITH MCP verify tools
mcp_server = MCPServerStreamableHttp(
    params={
        "url": "https://api.kluster.ai/v1/mcp",
        "headers": {"Authorization": f"Bearer {mcp_token}"}
    }
)

verify_agent = Agent(
    name="VerifyAgent",
    model="gpt-4",
    instructions="""You are a helpful assistant that verifies information before responding.
    Always use the verify tool when making factual claims to ensure accuracy.""",
    mcp_servers=[mcp_server]
)
```

## Compare agent responses

Test both agents with claims that need verification:

```python
# Test claims that need verification
test_claims = [
    "The capital of Australia is Sydney",
    "Python was created in 1991",
    "The speed of light is approximately 300,000 km/s"
]

async def compare_agents():
    for claim in test_claims:
        print(f"\nClaim: {claim}")
        print("-" * 50)
        
        # Basic agent response
        basic_response = await basic_agent.run(f"Is this true: {claim}")
        print(f"Basic Agent: {basic_response.content}")
        
        # Verify agent response
        verify_response = await verify_agent.run(f"Is this true: {claim}")
        print(f"Verify Agent: {verify_response.content}")

# Run the comparison
asyncio.run(compare_agents())
```

## Document verification

The MCP server also provides document verification capabilities:

```python
# Example with document verification
document_content = """
The Great Wall of China was built in a single dynasty and can be seen from space 
with the naked eye. It stretches for exactly 5,000 miles across northern China.
"""

async def verify_document():
    verify_response = await verify_agent.run(
        f"Verify the claims in this document: {document_content}"
    )
    print(verify_response.content)

# Run document verification
asyncio.run(verify_document())
```

## Put it All Together

<details>
<summary>Complete example script</summary>

```python
import os
import asyncio
import requests
from agents import Agent
from agents.mcp.server import MCPServerStreamableHttp

def setup_mcp_token():
    """Enable MCP and get token"""
    api_key = os.getenv("KLUSTER_API_KEY")
    if not api_key:
        raise ValueError("Please set KLUSTER_API_KEY environment variable")
    
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # Enable MCP
    enable_response = requests.post(
        "https://api.kluster.ai/v1/mcp/enable",
        headers=headers
    )
    
    if enable_response.status_code != 200:
        raise Exception(f"Failed to enable MCP: {enable_response.text}")
    
    # Get MCP token
    status_response = requests.get(
        "https://api.kluster.ai/v1/mcp/status",
        headers=headers
    )
    
    return status_response.json()["mcp_token"]

async def main():
    # Get MCP token
    mcp_token = setup_mcp_token()
    
    # Create agents
    basic_agent = Agent(
        name="BasicAgent",
        model="gpt-4",
        instructions="You are a helpful assistant that answers questions."
    )
    
    mcp_server = MCPServerStreamableHttp(
        params={
            "url": "https://api.kluster.ai/v1/mcp",
            "headers": {"Authorization": f"Bearer {mcp_token}"}
        }
    )
    
    verify_agent = Agent(
        name="VerifyAgent",
        model="gpt-4",
        instructions="""You are a helpful assistant that always verifies information.
        Use the verify tool for any factual claims.""",
        mcp_servers=[mcp_server]
    )
    
    # Test various claims
    test_scenarios = [
        "The capital of Australia is Sydney",
        "OpenAI was founded in 2015",
        "Water boils at 100°C at sea level",
        "The Moon is made of cheese"
    ]
    
    print("Comparing Basic Agent vs Verify Agent\n" + "=" * 60)
    
    for scenario in test_scenarios:
        print(f"\n📝 Claim: {scenario}")
        print("-" * 60)
        
        # Basic agent
        basic_response = await basic_agent.run(f"Is this true: {scenario}")
        print(f"❌ Basic Agent:\n{basic_response.content}\n")
        
        # Verify agent
        verify_response = await verify_agent.run(f"Is this true: {scenario}")
        print(f"✅ Verify Agent:\n{verify_response.content}")
        
        print("-" * 60)
    
    # Document verification example
    print("\n📄 Document Verification Example")
    print("=" * 60)
    
    document = """
    The Eiffel Tower in Paris is 324 meters tall and was completed in 1889.
    It was originally intended to be a temporary structure for the World's Fair.
    The tower is painted every seven years and requires 60 tons of paint.
    """
    
    doc_response = await verify_agent.run(
        f"Verify all claims in this document:\n{document}"
    )
    print(doc_response.content)

if __name__ == "__main__":
    asyncio.run(main())
```
</details>

To run this example:

1. Set your kluster.ai API key:
   ```bash
   export KLUSTER_API_KEY="your-api-key"
   export OPENAI_API_KEY="your-openai-key"
   ```

2. Run the script:
   ```bash
   python verify_comparison.py
   ```

## Next Steps

- Explore the [MCP tools documentation](/get-started/mcp/tools){target=_self} to learn about all available verification capabilities
- Check out the [OpenAI Agents SDK documentation](https://openai.github.io/openai-agents-python/){target=_blank} for advanced agent features
- Learn about [tool filtering](https://openai.github.io/openai-agents-python/mcp/#tool-filtering){target=_blank} to control which MCP tools your agents can access
- Try building multi-agent systems where specialized agents use different verification strategies