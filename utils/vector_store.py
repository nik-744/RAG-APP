import faiss
import numpy as np

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)  # L2 distance index
    index.add(embeddings)
    return index

def search(index, query_embedding, top_k=5):
    D, I = index.search(query_embedding, top_k)  # I contains indices of top_k matches
    return I[0]