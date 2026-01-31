from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small",
                dimensions=32
            )

document = [
                "Quantum computing uses qubits",
                "Cats are cute animals",
                "A qubit can be in superposition"
            ]

vectors = embeddings.embed_documents(document)

print(len(vectors))      # number of texts
print(len(vectors[0]))   # embedding dimension (32)
