#Semantic Search with HuggingFace & Cosine Similarity

import os

# Set custom cache directory for HuggingFace models
os.makedirs("D:/huggingface_cache", exist_ok=True)
os.environ["HF_HOME"] = "D:/huggingface_cache"

from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
            "Virat Kohli is famous for his strong batting skills and aggressive attitude.",
            "MS Dhoni is known for his calm mind and smart captaincy.",
            "Rohit Sharma is loved for hitting big scores and elegant shots.",
            "Jasprit Bumrah is a fast bowler who takes important wickets.",
            "Sachin Tendulkar is called the greatest batsman in cricket history.",
            "Hardik Pandya is an all-rounder who helps with both batting and bowling."
            ]

question = "Who is known for his calm mind and smart captaincy?"

documents_embeddings = embedding.embed_documents(documents)
question_embedding = embedding.embed_query(question)

similarities = cosine_similarity([question_embedding], documents_embeddings)[0]     #cosine_similarity expects 2D arrays and return 2D array

#Method 1: Using argmax to get index of most similar document
max_similarity_index = similarities.argmax()
most_similar_document = documents[max_similarity_index]
print("----- Semantic Search Result using Method 1-----")
print("Question:", question)
print("Most similar document:", most_similar_document)

#Method 2: Using sorted to get documents ranked by similarity
similarities = list(enumerate(similarities))   #(index, similarity) pairs
sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
print()
print("----- Semantic Search Result using Method 2-----")
print("Question:", question)
print("Most similar document:", documents[sorted_similarities[0][0]])