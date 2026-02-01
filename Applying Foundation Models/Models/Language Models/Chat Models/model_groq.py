from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
response = model.invoke("Tell me a joke about computers.")
print(response.content)