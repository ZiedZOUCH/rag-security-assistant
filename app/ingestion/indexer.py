from pathlib import Path
import chromadb
from app.ingestion.loaders import load_file
from app.ingestion.chunker import chunk_text
from app.rag.embeddings import get_embedding

RAW_DIR = Path("data/raw")
CHROMA_DIR = "data/chroma"
COLLECTION_NAME = "security_knowledge"

client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

def index_documents():
    doc_id = 0
    for file_path in RAW_DIR.glob("*"):
        if not file_path.is_file():
            continue

        text = load_file(file_path)
        if not text.strip():
            continue

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            emb = get_embedding(chunk)
            collection.add(
                ids=[f"{file_path.name}_{i}_{doc_id}"],
                embeddings=[emb],
                documents=[chunk],
                metadatas=[{
                    "source": file_path.name,
                    "chunk_index": i,
                    "type": file_path.suffix.lower()
                }]
            )
            doc_id += 1