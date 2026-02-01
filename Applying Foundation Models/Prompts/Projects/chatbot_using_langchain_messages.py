#With use of SystemMessage, HumanMessage, AIMessage. AI will understand which message belong to whom while seeing text chat
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
        )

#without memory AI will not remember the previous chats
chat_history = []
chat_history.append(SystemMessage(content="You are a good friend of mine."))

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input == 'exit':
        break

    response = model.invoke(chat_history)
    print(f"AI: {response.content}")

    chat_history.append(AIMessage(content=response.content))
