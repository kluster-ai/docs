from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key="INSERT_API_KEY", # Replace with your actual API key
    model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
)

llm.invoke("What is the capital of Nepal?")