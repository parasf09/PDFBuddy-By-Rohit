# PDFBuddy-By-Rohit
PDF Buddy is a smart RAG-based chatbot that allows users to upload PDFs and ask questions in natural language. It uses semantic search with embeddings and a vector database to retrieve relevant content and generate accurate, context-aware answers using a large language model.


PDFBuddy - Smart RAG Chatbot

-Features:
  Upload and process PDF files
  Smart text chunking for better context handling
  Semantic search using embeddings
  Fast retrieval with FAISS vector database
  Context-aware answer generation using Gemini LLM
  Simple and interactive UI using Streamlit

-Architecture :
  Pipeline:
    1. PDF Upload
    2. Text Extraction (PyMuPDF)
    3. Chunking
    4. Embedding Generation (Sentence Transformers)
    5. Storage in FAISS Vector DB
    6. Query Processing
    7. Similarity Search
    8. Context + Query → LLM
    9. Final Answer Generation

-Tech Stack :
    Frontend/UI: Streamlit  
    PDF Processing: PyMuPDF  
    Embeddings: Sentence-Transformers (all-MiniLM-L6-v2)  
    Vector Database: FAISS  
    LLM: Gemini API  
    Orchestration: LangChain  

Built as a GenAI project to demonstrate RAG architecture, embeddings, and LLM integration.
