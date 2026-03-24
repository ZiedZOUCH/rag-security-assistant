import chromadb
from app.rag.embeddings import get_embedding

CHROMA_DIR = "data/chroma"
COLLECTION_NAME = "security_knowledge"

client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

def retrieve(query: str, top_k: int = 5):
    query_emb = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_emb],
        n_results=top_k
    )
    return results