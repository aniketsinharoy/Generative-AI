#Example of downloading a LLM model locally and using it with LangChain
#NOTE: The LLM model size is around 15-20 GB, ensure you have enough disk space and a compatible GPU

import os

#By default, HuggingFace stores models in C:\Users\Username\.cache\huggingface\hub
# Set HF_HOME before importing huggingface libraries
os.makedirs("D:/huggingface_cache", exist_ok=True)
os.environ["HF_HOME"] = "D:/huggingface_cache"

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
            model_id="mistralai/Mistral-7B-Instruct-v0.2",
            task="text-generation",
            model_kwargs={"temperature":0.7, "max_new_tokens":100}
        )

model = ChatHuggingFace(llm=llm)
response = model.invoke("Explain the theory of relativity in simple terms.")
print(response.content)