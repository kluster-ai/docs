# Using LangChain with the kluster.ai API

This guide demonstrates how to integrate the ChatOpenAI class from the langchain_openai package with the kluster.ai API for advanced natural language processing tasks. By combining LangChain’s capabilities with kluster.ai’s large language models, you can seamlessly create powerful applications that leverage the best of both worlds.

## Install prerequisites

Ensure you have the `langchain` library installed:

```bash
pip install langchain
```

## Integrate with LangChain

Utilize LangChain’s `ChatOpenAI` model to interact with the kluster.ai API. 

Before using the API, you need to set your API key. If you don't have one, follow the steps in the [Get an API key guide](https://docs.kluster.ai/get-started/get-api-key/).

- The base_url is set to "https://api.kluster.ai/v1", directing requests to the kluster.ai API.
	•	You need to replace "INSERT_API_KEY" with your personal API key to authenticate your requests.
	•	The model parameter must be set to one of kluster.ai’s available models.
	•	Check our models to find the best option for your use case.

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
