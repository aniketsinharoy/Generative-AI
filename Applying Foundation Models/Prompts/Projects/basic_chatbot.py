from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
            model='openai/gpt-oss-20b:free',
            base_url="https://openrouter.ai/api/v1"
        )

#without memory AI will not remember the previous chats
chat_history = []

while True:
    user_input = input("User: ")
    chat_history.append(user_input)
    
    if user_input == 'exit':
        break

    response = model.invoke(chat_history)
    print(f"AI: {response.content}")

    chat_history.append(response.content)
