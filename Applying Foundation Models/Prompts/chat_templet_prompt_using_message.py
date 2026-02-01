# Example of using ChatPromptTemplate with role
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

chat_templete = ChatPromptTemplate(
    [
        ('system',"You are my {role}"),
        ('human',"{query}")
    ]
)

prompt = chat_templete.invoke({
    'role': 'friend',
    'query': 'Tell me about today in 1 line.'
})

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
        )

response = model.invoke(prompt)
print(response.content)