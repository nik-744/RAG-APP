import requests
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def query_groq_model(context, question, model="llama3-8b-8192"):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not set in environment variables.")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Answer the user's question **strictly based only** on the given context. If the answer is not in the context, reply with 'The answer is not in the provided context."},
            {"role": "user", "content": f"""Use the following context to answer the question.

--- BEGIN CONTEXT ---
{context}
--- END CONTEXT ---

Question: {question}
Answer:"""}
        ],
        "temperature": 0.0
    }    

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Groq API error: {response.status_code} - {response.text}")

    result = response.json()
    if "choices" not in result or not result["choices"]:
        raise Exception(f"Unexpected response: {result}")

    return result["choices"][0]["message"]["content"]
