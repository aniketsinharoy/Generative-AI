from langchain_cohere import ChatCohere
from dotenv import load_dotenv
load_dotenv()

model = ChatCohere(model="command-a-03-2025")
response = model.invoke("Tell me a joke about computers.")
print(response.content)