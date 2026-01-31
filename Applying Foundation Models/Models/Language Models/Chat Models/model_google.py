#Basic example of using Google Gemini chat model with LangChain (Google Generative AI)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="google-gemini-pro",   )
response = model.invoke("What is the capital of France?")
print(response.content)