from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()

# Chat prompt template (same role logic as before)
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a good friend of mine."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1"
)

# Manual memory (same as your first code)
chat_history = []

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    # Build prompt with history
    prompt = chat_template.invoke({
        "chat_history": chat_history,
        "query": user_input
    })

    response = model.invoke(prompt)
    print(f"AI: {response.content}")

    # Store messages exactly like before
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response.content))

    # Optional safety cap
    chat_history = chat_history[-20:]
