# 📄 RAGApplication - Document Q&A with PDF, DOCX, and PPTX

A simple and powerful Retrieval-Augmented Generation (RAG) application that enables Q&A over documents (`.pdf`, `.docx`, `.pptx`) using a custom pipeline. Built using **Python** and **Streamlit** for the frontend, and **Groq API** for language model responses.

---

## 🚀 Features

- Upload `.pdf`, `.docx`, or `.pptx` files
- Extracts and chunks text data
- Embeds text using a vectorizer
- Indexes the embeddings using FAISS
- Accepts user queries and finds the most relevant document chunks
- Uses Groq-hosted LLM to generate contextual answers

---

## 🔁 RAG Workflow

1. 📤 **Load the File**  
   Accepts PDF, Word (DOCX), and PowerPoint (PPTX) formats

2. 📄 **Extract and Chunk Text**  
   Extract content and split into manageable, overlapping chunks

3. 🧠 **Embed the Chunks**  
   Create vector representations of the chunks

4. 📦 **Index using FAISS**  
   Build a vector index for efficient similarity search

5. ❓ **Query Embedding**  
   Embed the user-entered question

6. 🔍 **Search Context Chunks**  
   Find most relevant chunks using vector similarity

7. ✍️ **Generate Answer**  
   Use Groq's LLM to frame the answer from retrieved context

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Vector Store**: FAISS
- **LLM**: Groq (e.g., Mixtral or LLaMA model)
- **File Parsing**: PyMuPDF, python-docx, python-pptx
- **Environment**: dotenv for API key management

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/RAGApplication.git
cd RAGApplication
pip install -r requirements.txt
