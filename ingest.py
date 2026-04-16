import os
import pickle
from sentence_transformers import SentenceTransformer
import faiss
from utils import extract_text_from_pdf, chunk_text

# Load embedding model
model = SentenceTransformer('all-mpnet-base-v2')

def create_vector_store(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save index + chunks
    os.makedirs("vectorstore", exist_ok=True)

    faiss.write_index(index, "vectorstore/index.faiss")

    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("✅ Vector store created successfully!")