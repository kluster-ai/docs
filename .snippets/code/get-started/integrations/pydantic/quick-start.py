import asyncio

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel


async def main():
    # Configure pydantic-ai to use your custom base URL and model name
    model = OpenAIModel(
        model_name='klusterai/Meta-Llama-3.3-70B-Instruct-Turbo',
        base_url='https://api.kluster.ai/v1',
        api_key='INSERT_KLUSTER_API_KEY',
    )

    # Create an Agent with that model
    agent = Agent(model)

    # Send a test prompt to verify connectivity
    # The result object will contain the model's response
    result = await agent.run('Hello, can you confirm this is working?')
    print("Response:", result.data)


if __name__ == '__main__':
    asyncio.run(main())
