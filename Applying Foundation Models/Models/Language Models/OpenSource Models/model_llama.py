#Example of using LLaMA 3.2 model from Hugging Face Hub with LangChain (Facebook)
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-1B-Instruct",
        task="text-generation"
    )

model = ChatHuggingFace(llm=llm)
response = model.invoke("Explain quantum computing in simple terms")
print(response.content)