from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Machine Learning is a branch of Artificial Intelligence that allows computers to learn from data without being explicitly programmed.",
    "It uses algorithms and models to recognize patterns, make predictions, or take decisions.",
    "ML is widely applied in fields like healthcare, finance, self-driving cars, and recommendation systems.",
    "There are different types of ML: supervised learning, unsupervised learning, and reinforcement learning.",
    "The more quality data an ML model gets, the better its accuracy and performance become."
]


query = 'Tell me about Machine learning'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print(score)