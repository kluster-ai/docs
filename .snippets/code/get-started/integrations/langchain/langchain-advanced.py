from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Create a memory instance to store the conversation
message_history = ChatMessageHistory()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Create your LLM, pointing to kluster.ai's endpoint
llm = ChatOpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key="INSERT_API_KEY",
    model="klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
)

# Define the prompt template, including the system instruction and placeholders
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Create the conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt
)

# Send the first user prompt
question1 = "Hello! Can you tell me something interesting about the city of Kathmandu?"
print("Question 1:", question1)
response1 = conversation.predict(input=question1)
print("Response 1:", response1)

# Send a follow-up question referencing previous context
question2 = "What is the population of that city?"
print("\nQuestion 2:", question2)
response2 = conversation.predict(input=question2)
print("Response 2:", response2)
