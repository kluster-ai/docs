---
title: Integrate OpenAI Agents SDK with kluster Verify
description: Integrate OpenAI Agents SDK with kluster Verify to create AI agents that detect hallucinations and validate facts with real-time verification.
---

# Integrate OpenAI Agents SDK with kluster Verify

[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/){target=_blank} provides a powerful framework for building AI agents that can use tools, maintain context, and interact with external services. By integrating with [kluster Verify](/verify/overview/){target=_blank}, you can create agents that not only generate responses using [kluster.ai's](https://www.kluster.ai/){target=_blank} language models but also perform real-time reliability verification to detect hallucinations and validate factual claims with internet-sourced verification.

This guide demonstrates how to integrate the `Agent` and `Runner` classes from the OpenAI Agents SDK with kluster.ai's API and MCP server, and then walks through building an interactive chatbot that utilizes kluster Verify's hallucination detection capabilities.

## Prerequisites

--8<-- 'text/kluster-api-onboarding.md'
- **Python 3.9+**: Make sure pip is also installed.
- **[A Python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=_blank}**: This is optional but recommended. Ensure that you enter the Python virtual environment before following along with this tutorial.
- **OpenAI Agents SDK packages installed**: Use the following command to install the [`openai-agents` packages](https://github.com/openai/openai-agents-python){target=_blank}.

    ```bash
    pip install "openai>=1.93.0" "openai-agents>=0.1.0" "mcp[cli]>=1.10.1"
    ```

- **MCP enabled**: This can be done via the [platform](https://platform.kluster.ai){target=_blank} or the [API](/verify/mcp/cloud/api/){target=\_blank}.

## Quick start

It's easy to integrate kluster Verify with OpenAI Agents SDK—when configuring the agent, point your `AsyncOpenAI` instance to the correct base URL and configure the following settings:

  - **Base URL**: Use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint.
  - **API key**: Replace with your kluster.ai API key. If you don't have one yet, refer to the [Get an API key guide](/get-api-key/).
  - **Select your model**: Choose a model with tool support from [kluster.ai's models](https://platform.kluster.ai/models){target=_blank} (filter by **Tool Support**).
  - **MCP server**: Configure the MCP server URL and token for kluster Verify's Reliability service.

```python
from agents import (
    Agent, 
    Runner, 
    set_tracing_disabled, 
    set_default_openai_api, 
    OpenAIChatCompletionsModel
)
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
    },
    client_session_timeout_seconds=30  # Increase from default 5 seconds to 30 seconds
)

# Create agent with kluster Verify capabilities
agent = Agent(
    name="ReliableAgent",
    instructions="Use kluster Verify for factual claims. Verify can detect hallucinations and validate information against real-time sources.",
    model=OpenAIChatCompletionsModel(
        model="deepseek-ai/DeepSeek-V3-0324",
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

That's all you need to start with OpenAI Agents SDK and kluster Verify! Next, this guide will explore building an interactive chatbot that showcases kluster Verify's hallucination detection and real-time verification capabilities.

Only models with tool support can use MCP verification. To find compatible options, filter by **Tool Support** on the [platform models page](https://platform.kluster.ai/models){target=_blank}.

For self-hosted MCP, use `http://localhost:3001/stream` along with the kluster.ai API key.

!!! warning "Known async cleanup issue"
    Error messages about "Exception ignored in atexit callback" may appear when the script exits. This is a [known issue](https://github.com/modelcontextprotocol/python-sdk/issues/521){target=_blank} with MCP's asyncio cleanup that **does not affect functionality**. The script will work correctly despite these messages.

## Enable MCP

If you prefer, you can enable MCP and obtain your token via API calls instead of using the platform interface. This approach allows you to automate the token retrieval process and integrate it directly into your application setup workflow.

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

This example creates an interactive chatbot where you can ask questions and see kluster Verify validate the responses in real-time, demonstrating how verification enhances conversational AI.

Unlike the previous single-query example, this implementation creates a persistent conversational experience that continues until the user chooses to exit. Each interaction goes through the full verification pipeline, meaning every response is automatically checked for accuracy and potential hallucinations before being presented to the user.

```python
from agents import (
    Agent, 
    Runner, 
    set_tracing_disabled, 
    set_default_openai_api, 
    OpenAIChatCompletionsModel
)
from agents.mcp.server import MCPServerStreamableHttp
from openai import AsyncOpenAI
import asyncio
import getpass

# Configure SDK
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

# Get credentials
api_key = getpass.getpass("Enter your kluster.ai API key: ")
mcp_token = getpass.getpass("Enter your MCP token: ")

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
    },
    client_session_timeout_seconds=30  # Increase from default 5 seconds to 30 seconds
)

# Create chatbot agent
agent = Agent(
    name="VerifyChatbot",
    instructions="Use kluster Verify to validate factual claims and provide reliable responses.",
    model=OpenAIChatCompletionsModel(
        model="deepseek-ai/DeepSeek-V3-0324",
        openai_client=kluster_client
    ),
    mcp_servers=[mcp_server]
)

# Interactive chat loop
async def main():
    await mcp_server.connect()
    
    print("🤖 Chatbot ready! Type 'quit' to exit.")
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
            
        if user_input:
            result = await Runner.run(agent, user_input)
            print(f"🤖 Bot: {result.final_output}")

asyncio.run(main())
```

??? code "Complete example"

    This complete example demonstrates how OpenAI Agents can leverage kluster Verify's hallucination detection through the MCP protocol.

    ```python
    import asyncio
    import requests
    import getpass
    from agents import (
        Agent, 
        Runner, 
        set_tracing_disabled, 
        set_default_openai_api, 
        OpenAIChatCompletionsModel
    )
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
            },
            client_session_timeout_seconds=30  # Increase from default 5 seconds to 30 seconds
        )
        
        # Create agent
        agent = Agent(
            name="KlusterVerifyAgent",
            instructions="""You are a helpful assistant. Answer questions directly and accurately. 

    IMPORTANT: Always use kluster Verify's Reliability for factual claims.
    When verification shows is_hallucination=true, acknowledge the correction.

    Include Verify's explanations and search results when provided.""",
            model=OpenAIChatCompletionsModel(
                model="deepseek-ai/DeepSeek-V3-0324",
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

## Run the script


1. Use the following command to run the script:

    ```bash
    python reliable_agent.py
    ```

2. Enter your kluster.ai API key when prompted. If you don't have one yet, refer to the [Get an API key guide](/get-api-key/){target=\_blank}.

Expected output:

<div class="termynal" data-termynal>
    <span data-ty="input">python reliable_agent.py</span>
    <span data-ty="input">🔑 Enter your kluster.ai API Key: ••••••••••••••••</span>
    <span data-ty>✅ Chatbot ready! Type 'quit' to exit.</span>
    <span data-ty>💬 Ask me anything and I'll verify my responses:</span>
    <span data-ty></span>
    <span data-ty="input">👤 You: Is it true that the Eiffel Tower was moved to London in May 2025?</span>
    <span data-ty>🤖 Bot: Thinking and verifying...</span>
    <span data-ty>🤖 Bot: No, the Eiffel Tower was not moved to London in May 2025 or at any other time. It remains in its original location in Paris, France.</span>
    <span data-ty></span>
    <span data-ty>### Verification Details:</span>
    <span data-ty>- **Explanation**: The search results confirm that the Eiffel Tower is located in Paris, and there is no credible information suggesting it was relocated to London.</span>
    <span data-ty>- **Supporting Sources**:</span>
    <span data-ty>  - [Eiffel Tower - Wikipedia](https://en.wikipedia.org/wiki/Eiffel_Tower) describes its location as Paris, France.</span>
    <span data-ty>  - Other sources mention proposals or ideas for towers in London but confirm these are unrelated to the Eiffel Tower.</span>
    <span data-ty></span>
    <span data-ty>The claim about the Eiffel Tower being moved to London is false.</span>
    <span data-ty></span>
    <span data-ty></span>
    <span data-ty="input">👤 You: quit</span>
    <span data-ty></span>
    <span data-ty>👋 Goodbye!</span>
</div>

That's it! You've successfully integrated OpenAI Agents SDK with kluster Verify, and your configured agent is ready to leverage real-time hallucination detection and Reliability. For more information about the capabilities of OpenAI Agents SDK, be sure to check out the [OpenAI Agents docs](https://openai.github.io/openai-agents-python/){target=_blank}.

## Next steps

- Explore [kluster Verify's Reliability](/verify/reliability/overview/) for all verification capabilities.
- Try the [Verify API tutorial](/tutorials/klusterai-api/reliability) with detailed code examples.
- Learn about [tool filtering](https://openai.github.io/openai-agents-python/mcp/#tool-filtering){target=_blank} to control tool access.
- Check the [OpenAI Agents docs](https://openai.github.io/openai-agents-python/){target=_blank} for advanced features.