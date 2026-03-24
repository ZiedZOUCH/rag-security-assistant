import requests

OLLAMA_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "qwen3-embedding"   # ou embeddinggemma si tu l'as téléchargé

def get_embedding(text: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": EMBED_MODEL,
            "input": text
        },
        timeout=120
    )
    response.raise_for_status()
    data = response.json()
    return data["embeddings"][0]