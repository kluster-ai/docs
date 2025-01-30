# Using LangChain with the kluster.ai API

This guide demonstrates how to integrate the `ChatOpenAI` class from the `langchain_openai` package with the [kluster.ai](https://www.kluster.ai/){target=\_blank} API. By combining LangChain’s capabilities with kluster.ai’s large language models, you can seamlessly create powerful applications.

## Install prerequisites

Ensure you have the `langchain` library installed:

```bash
pip install langchain
```

## Integrate with LangChain

It is very simple to integrate kluster.ai with LangChain—just point your `ChatOpenAI` to the correct base URL and configure a few settings.

  - **Base URL -** use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint
  - **API Key -** replace `INSERT_API_KEY` in the code below with your own kluster.ai API key. If you don’t have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}
  - **Select Your Model -** choose one of kluster.ai’s available models based on your use case. For more details, see [kluster.ai’s models](/api-reference/reference/#list-supported-models){target=\_blank}

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(base_url="https://api.kluster.ai/v1",
                 api_key="INSERT_API_KEY",  # Replace with your actual API key
                 model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo"
            )

llm.invoke("What is the capital of Nepal?")
```

## Conclusion

You’ve successfully integrated LangChain with the kluster.ai API. Your configured LLM is now ready to deliver the full range of LangChain capabilities. Explore the [kluster.ai documentation](https://docs.kluster.ai/){target=\_blank} for other guides and tutorials.