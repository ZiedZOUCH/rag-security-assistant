import streamlit as st
from app.rag.retriever import retrieve
from app.rag.generator import generate_answer

st.set_page_config(page_title="RAG Sécurité Interne", layout="wide")
st.title("Assistant RAG - Questionnaires Sécurité")

question = st.text_area("Pose ta question sécurité client", height=150)

if st.button("Générer une réponse"):
    if question.strip():
        with st.spinner("Analyse en cours..."):

            docs, metas, distances = retrieve(question, top_k=5)
            sources = [m["source"] for m in metas]

            answer = generate_answer(question, docs, sources)

            st.subheader("Réponse proposée")
            st.code(answer)

            st.subheader("Sources")
            for meta in metas:
                st.write(f"- {meta['source']} (chunk {meta['chunk_index']})")

            confidence = round(1 - min(distances), 2)
            st.subheader("Confidence score")
            st.write(confidence)

    else:
        st.warning("Merci de saisir une question.")