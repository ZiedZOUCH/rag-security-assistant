import requests
from app.rag.prompts import SYSTEM_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
GEN_MODEL = "qwen2.5:3b"

def generate_answer(question: str, contexts: list, sources: list):
    context_text = "\n\n".join(contexts)
    source_text = "\n".join([f"- {s}" for s in sources])

    prompt = f"""
{SYSTEM_PROMPT}

Question:
{question}

Context:
{context_text}

Sources:
{source_text}

Now provide:
1. A concise professional answer
2. A short note if information is incomplete
3. The source list
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": GEN_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )
    response.raise_for_status()
    return response.json()["response"]