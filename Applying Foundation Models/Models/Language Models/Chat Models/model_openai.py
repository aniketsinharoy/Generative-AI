#Basic example for ChatOpenAI model (Open AI)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo-instruct')
response = model.invoke("What is the capital of Germany?")
print(response)

#Basic example for ChatOpenAI model using custom base_url (OpenRouter)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
        )
response = model.invoke("What is the capital of Italy?")
print(response.content)


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1",
            temperature=0.7,
            max_completion_tokens=100
        )
response = model.invoke("What is the capital of Italy?")
print(response.content)