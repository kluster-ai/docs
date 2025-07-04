---
title: OpenAI Agents SDK integration
description: Enhance OpenAI agents with kluster.ai's MCP verification tools for reliable information validation
---

# OpenAI Agents SDK

Integrate [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/){target=_blank} with kluster.ai's MCP server to add real-time verification capabilities to your AI agents.

## Prerequisites

--8<-- 'text/kluster-api-onboarding.md'
- **Python 3.9+** with pip
- **OpenAI Agents SDK**: `pip install openai-agents`
- **MCP enabled**: Via [platform](https://platform.kluster.ai){target=_blank} or [API](/get-started/mcp/cloud/api/){target=_blank}

## Quick start

Connect your OpenAI agent to kluster.ai's MCP verification tools using kluster.ai as the LLM provider:

```python
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_api, OpenAIChatCompletionsModel
from agents.mcp.server import MCPServerStreamableHttp
from openai import AsyncOpenAI
import asyncio
import os

# Disable tracing and use Chat Completions API
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

# Create kluster.ai client
kluster_client = AsyncOpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key=os.getenv("KLUSTER_API_KEY")
)

# Configure MCP server with timeout
mcp_server = MCPServerStreamableHttp(
    params={
        "url": "https://api.kluster.ai/v1/mcp",
        "headers": {"Authorization": f"Bearer {os.getenv('KLUSTER_MCP_TOKEN')}"},
        "timeout": 15,
        "sse_read_timeout": 15
    }
)

# Create agent with kluster.ai model
agent = Agent(
    name="KlusterVerifyAgent",
    instructions="""You are a helpful assistant. Answer questions directly and accurately. 

IMPORTANT: Only use the verify tool if the user explicitly asks you to verify or fact-check your previous response.

When using the verify tool, call it with this exact JSON format:
{
  "prompt": "the user's original question",
  "response": "your answer to that question", 
  "returnSearchResults": true
}

The returnSearchResults parameter must be the boolean value true, not the string "true".

Report the verification results clearly.""",
    model=OpenAIChatCompletionsModel(
        model="klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
        openai_client=kluster_client
    ),
    mcp_servers=[mcp_server]
)

# Run the agent
async def main():
    await mcp_server.connect()
    result = await Runner.run(agent, "Is the Earth flat?")
    print(result.final_output)

asyncio.run(main())
```

!!! info "Self-hosted option"
    For self-hosted MCP, use `http://localhost:3001/stream` and your kluster.ai API key.

## Enable MCP

Get your MCP token programmatically:

```python
import requests

# Enable MCP
response = requests.post(
    "https://api.kluster.ai/v1/mcp/enable",
    headers={"Authorization": f"Bearer {api_key}"}
)

# Get status with token
status = requests.get(
    "https://api.kluster.ai/v1/mcp/status", 
    headers={"Authorization": f"Bearer {api_key}"}
)
mcp_token = status.json()["apiKey"]
```

## Agent comparison

See the difference between agents with and without verification:

```python
# Basic agent (no verification)
basic_agent = Agent(
    name="BasicAgent",
    model=OpenAIChatCompletionsModel(
        model="klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
        openai_client=kluster_client
    ),
    instructions="Answer questions to the best of your knowledge."
)

# Verify agent (with MCP tools)
verify_agent = Agent(
    name="VerifyAgent",
    model=OpenAIChatCompletionsModel(
        model="klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
        openai_client=kluster_client
    ),
    instructions="Answer questions directly. Only use verify tool when explicitly asked.",
    mcp_servers=[mcp_server]
)

# Test both agents
claim = "The capital of Australia is Sydney"
basic_response = await Runner.run(basic_agent, f"Is this true: {claim}")
verify_response = await Runner.run(verify_agent, f"Is this true: {claim}. Please verify this using the verify tool.")
```

[SCREENSHOT]

## Document verification

Verify claims within documents:

```python
document = """
The Great Wall of China can be seen from space with the naked eye.
It stretches for exactly 5,000 miles across northern China.
"""

response = await Runner.run(
    verify_agent,
    f"Please verify the claims in this document: {document}"
)
print(response.final_output)
```

## Complete example

<details>
<summary>Full integration script</summary>

```python
import os
import asyncio
import requests
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_api, OpenAIChatCompletionsModel
from agents.mcp.server import MCPServerStreamableHttp
from openai import AsyncOpenAI

def setup_mcp_token():
    """Enable MCP and get token"""
    api_key = os.getenv("KLUSTER_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # Enable MCP
    requests.post("https://api.kluster.ai/v1/mcp/enable", headers=headers)
    
    # Get token
    response = requests.get("https://api.kluster.ai/v1/mcp/status", headers=headers)
    return response.json()["apiKey"]

async def main():
    # Setup
    set_tracing_disabled(True)
    set_default_openai_api("chat_completions")
    
    mcp_token = setup_mcp_token()
    
    # Create kluster.ai client
    kluster_client = AsyncOpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key=os.getenv("KLUSTER_API_KEY")
    )
    
    # Create MCP server
    mcp_server = MCPServerStreamableHttp(
        params={
            "url": "https://api.kluster.ai/v1/mcp",
            "headers": {"Authorization": f"Bearer {mcp_token}"},
            "timeout": 15,
            "sse_read_timeout": 15
        }
    )
    
    # Create verify agent
    agent = Agent(
        name="KlusterVerifyAgent",
        instructions="""You are a helpful assistant. Answer questions directly and accurately. 

IMPORTANT: Only use the verify tool if the user explicitly asks you to verify or fact-check your previous response.

When using the verify tool, call it with this exact JSON format:
{
  "prompt": "the user's original question",
  "response": "your answer to that question", 
  "returnSearchResults": true
}

The returnSearchResults parameter must be the boolean value true, not the string "true".

Report the verification results clearly.""",
        model=OpenAIChatCompletionsModel(
            model="klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
            openai_client=kluster_client
        ),
        mcp_servers=[mcp_server]
    )
    
    # Connect to MCP server
    await mcp_server.connect()
    
    # Test scenarios
    print("🤖 Testing kluster.ai agent with MCP verification...")
    print("=" * 60)
    
    # Test 1: Basic question (should answer without verification)
    print("\n❓ Question: What is the capital of Australia?")
    print("-" * 40)
    result1 = await Runner.run(agent, "What is the capital of Australia?")
    print(f"🔍 Agent Response:\n{result1.final_output}\n")
    
    # Test 2: Ask for verification of the previous response
    print("\n❓ Follow-up: Can you verify that answer using the verify tool?")
    print("-" * 40)
    result2 = await Runner.run(agent, "Can you verify that answer using the verify tool? The question was 'What is the capital of Australia?' and your answer was about Canberra.")
    print(f"🔍 Agent Response:\n{result2.final_output}\n")
    
    # Test 3: Wrong claim with verification request
    print("\n❓ Question: Is the Earth flat? Please verify your answer.")
    print("-" * 40)
    result3 = await Runner.run(agent, "Is the Earth flat? Please verify your answer using the verify tool.")
    print(f"🔍 Agent Response:\n{result3.final_output}\n")
    
    print("=" * 60)
    print("✅ All tests completed!")

if __name__ == "__main__":
    asyncio.run(main())
```
</details>

## Run the example

1. Set environment variables:
   ```bash
   export KLUSTER_API_KEY="your-api-key"
   # Note: OpenAI API key not needed since we use kluster.ai as LLM provider
   ```

2. Install dependencies:
   ```bash
   pip install openai-agents requests openai
   ```

3. Run the script:
   ```bash
   python verify_agent.py
   ```

## Next steps

- Explore [MCP tools](/get-started/mcp/tools){target=_self} for all verification capabilities
- Learn about [tool filtering](https://openai.github.io/openai-agents-python/mcp/#tool-filtering){target=_blank} to control tool access
- Check the [OpenAI Agents docs](https://openai.github.io/openai-agents-python/){target=_blank} for advanced features