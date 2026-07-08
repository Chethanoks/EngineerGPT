import streamlit as st

st.set_page_config(
    page_title="EngineerGPT",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 EngineerGPT")
st.subheader("Offline AI Engineering Assistant")

st.markdown("""
Welcome to **EngineerGPT**.

### Features
- 💬 Chat with Local AI (Ollama)
- 📄 Upload Engineering PDFs
- 🔍 Ask Questions About PDFs
- 🧠 RAG using ChromaDB
- 🔒 Runs Completely Offline

---
""")

st.info("Next step: Connect EngineerGPT to Ollama.")