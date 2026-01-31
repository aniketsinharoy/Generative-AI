#Example code to generate embedding for a single text using HuggingFace Embeddings
#Downloaded the model locally and use it with LangChain
#The Model size is around 90 MB

import os

#By default, HuggingFace stores models in C:\Users\Username\.cache\huggingface\hub
# Set HF_HOME before importing huggingface libraries
os.makedirs("D:/huggingface_cache", exist_ok=True)
os.environ["HF_HOME"] = "D:/huggingface_cache"

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document = [
                "Quantum computing uses qubits",
                "Cats are cute animals",
                "A qubit can be in superposition"
            ]

vectors = embeddings.embed_documents(document)
print(len(vectors))      # number of texts
print(len(vectors[0]))   # embedding dimension (384)