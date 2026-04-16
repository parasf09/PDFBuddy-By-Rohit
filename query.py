import faiss
import pickle
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model_embed = SentenceTransformer('all-mpnet-base-v2')

def load_vector_store():
    index = faiss.read_index("vectorstore/index.faiss")

    with open("vectorstore/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


def get_answer(query):
    index, chunks = load_vector_store()

    query_embedding = model_embed.encode([query])

    D, I = index.search(query_embedding, k=8)

    context = "\n".join([chunks[i] for i in I[0]])

    prompt = f"""
You are a helpful assistant.

Answer using the context below if relevant.
If the context does not fully contain the answer, use your own knowledge to help.

Context:
{context}

Question:
{query}
"""


    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text