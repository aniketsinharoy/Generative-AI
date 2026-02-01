from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

topic = input("Enter topic name: ")
prompt = f"Write a 5 lines poem on {topic}"

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
        )

response = model.invoke(prompt)
print(response.content)