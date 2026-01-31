#Using LangChain's OpenAI wrapper to interact with the GPT-3.5-turbo-instruct model
#API Key is set directly in the code
from langchain_openai import OpenAI

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    api_key="sk-xxxxxxxxxxxxxxxx"
)

response = llm.invoke("What is the capital of France?")
print(response)

#Using LangChain's OpenAI wrapper to interact with the GPT-3.5-turbo-instruct model
#API Key is loaded from environment variables
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')
response = llm.invoke("What is the capital of India")
print(response)