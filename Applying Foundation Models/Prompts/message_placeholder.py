# Example of using MessagesPlaceholder in ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

chat_templete = ChatPromptTemplate(
    [
        ('system',"You are an {role}"),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human',"{query}")
    ]
)

chat_history = []
with open("./Prompts/chat_history.txt") as f:
    chat_history.extend(f.readlines())

prompt = chat_templete.invoke({
    'role': 'support staff',
    'chat_history': chat_history,
    'query': 'When will I get my refund?'
})

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
        )

response = model.invoke(prompt)
print(response.content)