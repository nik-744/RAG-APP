import streamlit as st 
import numpy as np
from utils.file_parser import parse_doc,parse_pdf,parse_pptx
from utils.embedder import get_embeddings,chunk_text
from utils.vector_store import build_faiss_index, search
from utils.groq_llm import query_groq_model
# from sentence_transformers import SentenceTransformer

st.title("Document Search and Q&A")
upload = st.file_uploader("Upload a document (PDF, PPTX, DOCX)", type=["pdf", "pptx", "docx"])
question = st.text_input("Ask a question about the file")

if upload:
    st.success("File uploaded successfully!")
    file_type = upload.name.split('.')[-1].lower()
    path= f"temp.{file_type}"
    with open(path, "wb") as f:
        f.write(upload.read())
    if file_type == "pdf":
        content = parse_pdf(path)
    elif file_type == "pptx":
        content = parse_pptx(path)
    elif file_type == "docx":
        content = parse_doc(path)
    else:
        st.error("Unsupported file format")

    if question:
        chunk = chunk_text(content)
        print(chunk)
        embeddings = get_embeddings(chunk)
        index = build_faiss_index(np.array(embeddings))
        q_embedding = get_embeddings([question])
        top_ids = search(index,q_embedding, top_k=5)
        relevant_chunks = "\n\n".join([chunk[i] for i in top_ids])
        print(relevant_chunks)
        
        answer = query_groq_model(relevant_chunks, question)
        st.subheader("Answer")
        st.write(answer)