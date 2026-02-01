from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

templete = load_prompt("./Prompts/poem_templete.json")

topic = input("Enter topic name: ")
tone = input("Enter tone: ")

prompt = templete.invoke({
    'topic': topic,
    'tone': tone
})

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
        )

response = model.invoke(prompt)
print(response.content)