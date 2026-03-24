import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
GEN_MODEL = "qwen2.5:7b"

SYSTEM_PROMPT = """
You are a senior cybersecurity expert helping answer client security questionnaires.

STRICT RULES:
- Use ONLY the provided context
- NEVER invent information
- If information is missing, clearly say it
- Be precise and factual
- Use professional audit language

OUTPUT FORMAT:

Answer:
<clear structured answer>

Evidence:
- <fact from context>
- <fact from context>

Gap:
<missing info if any>

Sources:
<list sources>
"""

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
    answer = response.json()["response"]

    # disclaimer sécurité
    answer += "\n\n---\n⚠️ Draft generated from internal documents. Human validation required."

    return answer