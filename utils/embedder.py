from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
def chunk_text(text, chunk_size=300,overlap=50):
    words = text.split()
    chunks = []
    for i in range(0,len(words),chunk_size-overlap):
        chunks.append(' '.join(words[i:i+chunk_size]))
    return chunks

def get_embeddings(text_chunks):
    return model.encode(text_chunks)