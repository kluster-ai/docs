---
title: Integrate OpenAI Agents SDK with kluster Verify
description: This guide walks you through integrating OpenAI Agents SDK with kluster Verify to build reliable AI agents with real-time hallucination detection and fact-checking capabilities.
---

# Integrate OpenAI Agents SDK with kluster Verify

[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/){target=_blank} provides a powerful framework for building AI agents that can use tools, maintain context, and interact with external services. By integrating with [kluster Verify](/get-started/verify/overview/){target=_blank}, you can create agents that not only generate responses using [kluster.ai's](https://www.kluster.ai/){target=_blank} language models but also perform real-time reliability checks to detect hallucinations and validate factual claims with internet-sourced verification.

This guide demonstrates how to integrate the `Agent` and `Runner` classes from the OpenAI Agents SDK with kluster.ai's API and MCP server, then walks through building an interactive chatbot with kluster Verify's hallucination detection capabilities.

## Prerequisites

--8<-- 'text/kluster-api-onboarding.md'
- **Python 3.9+** with pip installed.
- **[A Python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=_blank}** - this is optional but recommended. Ensure that you enter the Python virtual environment before following along with this tutorial.
- **OpenAI Agents SDK packages installed** - install the [`openai-agents` packages](https://github.com/openai/openai-agents-python){target=_blank}:

    ```bash
    pip install openai>=1.93.0 openai-agents>=0.1.0 "mcp[cli]>=1.10.1"
    ```

- **MCP enabled**: Via [platform](https://platform.kluster.ai){target=_blank} or [API](/get-started/mcp/cloud/api/).

## Quick start

It's easy to integrate kluster Verify with OpenAI Agents SDK—when configuring the agent, point your `AsyncOpenAI` instance to the correct base URL and configure the following settings:

  - **Base URL**: Use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint.
  - **API key**: Replace with your kluster.ai API key. If you don't have one yet, refer to the [Get an API key guide](/get-started/get-api-key/).
  - **Select your model**: Choose one of [kluster.ai's available models](/get-started/models/) based on your use case.
  - **MCP server**: Configure the MCP server URL and token for kluster Verify's reliability checking.

```python
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_api, OpenAIChatCompletionsModel
from agents.mcp.server import MCPServerStreamableHttp
from openai import AsyncOpenAI
import asyncio
import getpass

# Configure SDK for production use
set_tracing_disabled(True)  # Disable OpenAI telemetry
set_default_openai_api("chat_completions")  # Use stable Chat API

# Get credentials securely
api_key = getpass.getpass("Enter your kluster.ai API key: ")
mcp_token = getpass.getpass("Enter your MCP token: ")

# Create kluster.ai client
kluster_client = AsyncOpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key=api_key
)

# Configure MCP server for verification
mcp_server = MCPServerStreamableHttp(
    params={
        "url": "https://api.kluster.ai/v1/mcp",
        "headers": {"Authorization": f"Bearer {mcp_token}"},
        "timeout": 15,
        "sse_read_timeout": 15
    }
)

# Create agent with kluster Verify capabilities
agent = Agent(
    name="ReliableAgent",
    instructions="Use kluster Verify for factual claims. Verify can detect hallucinations and validate information against real-time sources.",
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

That's all you need to start with OpenAI Agents SDK and kluster Verify! Next, this guide will explore building a production-ready agent that showcases kluster Verify's hallucination detection and real-time verification capabilities.

!!! warning "Known async cleanup issue"
    You may see error messages about "Exception ignored in atexit callback" when the script exits. This is a [known issue](https://github.com/modelcontextprotocol/python-sdk/issues/521){target=_blank} with MCP's asyncio cleanup that **does not affect functionality**. Your script will work correctly despite these messages.

!!! info "Self-hosted option"
    For self-hosted MCP, use `http://localhost:3001/stream` and your kluster.ai API key.

## Enable MCP

If you prefer programmatic setup, you can enable MCP and obtain your token via API calls instead of using the platform interface. This approach allows you to automate the token retrieval process and integrate it directly into your application setup workflow.

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

## Build an interactive chatbot

This section will explore what OpenAI Agents SDK can do beyond basic generation. In the following steps, you'll create an interactive chatbot where you can ask questions and see kluster Verify validate the responses in real-time, demonstrating how verification enhances conversational AI.

### Create the script

First, create a new Python file that will contain our interactive chatbot implementation. This script will demonstrate a complete conversation loop with kluster Verify integration.

```bash
touch reliable_agent.py
```

### Complete implementation

This implementation shows how to build a conversational agent with secure credential handling, proper SDK configuration, and kluster Verify integration for real-time response validation.

```python
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_api, OpenAIChatCompletionsModel
from agents.mcp.server import MCPServerStreamableHttp
from openai import AsyncOpenAI
import asyncio
import getpass

def configure_sdk():
    """Configure SDK for production use"""
    set_tracing_disabled(True)  # Disable OpenAI telemetry
    set_default_openai_api("chat_completions")  # Use stable API

def get_credentials():
    """Get API credentials securely"""
    print("🔑 Enter your kluster.ai credentials:")
    api_key = getpass.getpass("API Key: ")
    
    print("\n🔌 Enter your MCP server details:")
    mcp_url = input("MCP URL (default: https://api.kluster.ai/v1/mcp): ") or "https://api.kluster.ai/v1/mcp"
    mcp_token = getpass.getpass("MCP Token: ")
    
    return api_key, mcp_url, mcp_token

async def create_reliable_agent(api_key: str, mcp_url: str, mcp_token: str) -> Agent:
    """Create agent with kluster.ai and kluster Verify"""
    
    # Initialize kluster.ai client
    kluster_client = AsyncOpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key=api_key
    )
    
    # Configure MCP server
    mcp_server = MCPServerStreamableHttp(
        params={
            "url": mcp_url,
            "headers": {"Authorization": f"Bearer {mcp_token}"},
            "timeout": 15,
            "sse_read_timeout": 15
        }
    )
    
    # Create agent
    agent = Agent(
        name="ReliableAgent",
        instructions="""You are a reliable AI assistant powered by kluster Verify.
        
        IMPORTANT: Always use kluster Verify's reliability check for factual claims.
        When verification shows is_hallucination=true, acknowledge the correction.
        
        Include Verify's explanations and search results when provided.""",
        model=OpenAIChatCompletionsModel(
            model="klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
            openai_client=kluster_client
        ),
        mcp_servers=[mcp_server]
    )
    
    await mcp_server.connect()
    return agent
```

[SCREENSHOT]

### Interactive chatbot loop

The main function creates an interactive conversation experience where users can ask questions and see kluster Verify validate each response, demonstrating real-time hallucination detection in action.

```python
async def main():
    """Interactive chatbot with kluster Verify"""
    
    print("🚀 kluster Verify + OpenAI Agents Chatbot")
    print("=" * 50)
    
    configure_sdk()
    api_key, mcp_url, mcp_token = get_credentials()
    
    print("\n🤖 Creating chatbot...")
    agent = await create_reliable_agent(api_key, mcp_url, mcp_token)
    
    print("\n✅ Chatbot ready! Type 'quit' to exit.")
    print("💬 Ask me anything and I'll verify my responses:\n")
    
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye!")
                break
                
            if not user_input:
                continue
            
            # Get agent response with verification
            print("🤖 Bot: Thinking and verifying...")
            result = await Runner.run(agent, user_input)
            print(f"🤖 Bot: {result.final_output}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())
```

## Handle async cleanup errors

Due to a known issue with MCP's asyncio cleanup process, you may see harmless error messages when the script exits. These messages don't affect functionality, but you can suppress them using this optional stderr redirection technique if you prefer cleaner output.

```python
import sys
import os

if __name__ == "__main__":
    # Temporarily redirect stderr to suppress cleanup errors
    stderr_backup = sys.stderr
    try:
        sys.stderr = open(os.devnull, 'w')
        asyncio.run(main())
    finally:
        sys.stderr.close()
        sys.stderr = stderr_backup
```

## Complete example

<details>
<summary>Full integration script</summary>
This complete example demonstrates how OpenAI Agents can leverage kluster Verify's hallucination detection through the MCP protocol.

```python
import asyncio
import requests
import getpass
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_api, OpenAIChatCompletionsModel
from agents.mcp.server import MCPServerStreamableHttp
from openai import AsyncOpenAI

def setup_mcp_token():
    """Enable MCP and get token"""
    api_key = getpass.getpass("Enter your kluster.ai API key: ")
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # Enable MCP
    requests.post("https://api.kluster.ai/v1/mcp/enable", headers=headers)
    
    # Get token
    response = requests.get("https://api.kluster.ai/v1/mcp/status", headers=headers)
    return api_key, response.json()["apiKey"]

async def main():
    set_tracing_disabled(True)
    set_default_openai_api("chat_completions")
    
    api_key, mcp_token = setup_mcp_token()
    
    # Create kluster.ai client
    kluster_client = AsyncOpenAI(
        base_url="https://api.kluster.ai/v1",
        api_key=api_key
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
    
    # Create agent
    agent = Agent(
        name="KlusterVerifyAgent",
        instructions="""You are a helpful assistant. Answer questions directly and accurately. 

IMPORTANT: Always use kluster Verify's reliability check for factual claims.
When verification shows is_hallucination=true, acknowledge the correction.

Include Verify's explanations and search results when provided.""",
        model=OpenAIChatCompletionsModel(
            model="klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
            openai_client=kluster_client
        ),
        mcp_servers=[mcp_server]
    )
    
    await mcp_server.connect()
    
    print("\n✅ Chatbot ready! Type 'quit' to exit.")
    print("💬 Ask me anything and I'll verify my responses:\n")
    
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye!")
                break
                
            if not user_input:
                continue
            
            # Get agent response with verification
            print("🤖 Bot: Thinking and verifying...")
            result = await Runner.run(agent, user_input)
            print(f"🤖 Bot: {result.final_output}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())
```
</details>

## Run the script

```bash
python reliable_agent.py
```

Enter your credentials when prompted:
- kluster.ai API key (get one from [platform.kluster.ai](https://platform.kluster.ai){target=_blank}).
- MCP token (obtained after [enabling MCP](/get-started/mcp/cloud/platform/)).

Expected output:
```
🚀 kluster Verify + OpenAI Agents Chatbot
==================================================
🔑 Enter your kluster.ai credentials:
API Key: 

🔌 Enter your MCP server details:
MCP URL (default: https://api.kluster.ai/v1/mcp): 
MCP Token: 

🤖 Creating chatbot...

✅ Chatbot ready! Type 'quit' to exit.
💬 Ask me anything and I'll verify my responses:

👤 You: What is the capital of Japan?
🤖 Bot: Thinking and verifying...
🤖 Bot: The capital of Japan is Tokyo. ✓ Verified by kluster Verify

👤 You: Is the Earth flat?
🤖 Bot: Thinking and verifying...
🤖 Bot: No, the Earth is not flat. It is an oblate spheroid. ✓ Verified with search results

👤 You: quit

👋 Goodbye!
```

That's it! You've successfully integrated OpenAI Agents SDK with kluster Verify, and your configured agent is ready to leverage real-time hallucination detection and reliability checking. For more information about the capabilities of OpenAI Agents SDK, be sure to check out the [OpenAI Agents docs](https://openai.github.io/openai-agents-python/){target=_blank}.

## Next steps

- Explore [kluster Verify's reliability checking](/get-started/verify/reliability/overview/) for all verification capabilities.
- Try the [Verify API tutorial](/tutorials/klusterai-api/reliability-check) with detailed code examples.
- Learn about [tool filtering](https://openai.github.io/openai-agents-python/mcp/#tool-filtering){target=_blank} to control tool access.
- Check the [OpenAI Agents docs](https://openai.github.io/openai-agents-python/){target=_blank} for advanced features.