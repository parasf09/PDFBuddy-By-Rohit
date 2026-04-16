import streamlit as st
from ingest import create_vector_store
from query import get_answer
import os

st.set_page_config(page_title="PDF Chatbot", layout="wide")

st.title("PDFBuddy-By Rohit")

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("📄 Process PDF"):
        create_vector_store(file_path)
        st.success("PDF processed successfully!")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
query = st.chat_input("Ask something about your PDF...")

if query:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    # Get answer
    answer = get_answer(query)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)