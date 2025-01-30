# Using LangChain with the kluster.ai API

This guide demonstrates how to integrate the ChatOpenAI class from the langchain_openai package with the kluster.ai API for advanced natural language processing tasks. By combining LangChain’s capabilities with kluster.ai’s large language models, you can seamlessly create powerful applications that leverage the best of both worlds.

## Install prerequisites

Ensure you have the `langchain` library installed:

```bash
pip install langchain
```

## Integrate with LangChain

It is very simple to integrate kluster.ai with LangChain—just point your `ChatOpenAI` to the correct base URL and configure a few settings.

**Key configuration points:**

  - **Base URL:** Use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint.
  - **API Key:** Replace `INSERT_API_KEY` in the code below with your own kluster.ai API key. If you don’t have one yet, refer to the [Get an API key guide](https://docs.kluster.ai/get-started/get-api-key/).
  - **Select Your Model:** Choose one of kluster.ai’s available models based on your use case. For more details, see [kluster.ai’s models](https://docs.kluster.ai/get-started/models/).

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(base_url="https://api.kluster.ai/v1",
                 api_key="INSERT_API_KEY",  # Replace with your actual API key
                 model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo"
            )

llm.invoke("What is the capital of Nepal?")
```

## Conclusion

By following these steps, you've successfully integrated LangChain with the kluster.ai API. This setup allows you to leverage kluster.ai's large language models within your applications efficiently.

For more information, visit the [kluster.ai documentation](https://docs.kluster.ai/).
