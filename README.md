\# RAG Security Assistant



Assistant RAG local pour exploiter des documents internes et aider à répondre à des questionnaires sécurité.



\## Fonctionnalités



\- Ingestion de fichiers PDF, DOCX, PPTX et XLSX

\- Extraction du texte

\- Chunking

\- Embeddings via Ollama

\- Stockage vectoriel avec ChromaDB

\- Recherche sémantique

\- Génération de réponses avec un LLM local

\- Interface Streamlit



\## Structure du projet



```text

app/

&#x20; ingestion/

&#x20; rag/

&#x20; ui/

data/

&#x20; raw/

&#x20; chroma/

main\_index.py

requirements.txt

README.md

