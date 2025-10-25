# 📚 Retrieval-Augmented Generation (RAG) Chatbot

## 👨‍💻 Developer
**Name:** Zhichuan Jing  
**Course:** INFO 5940 – AI Application Development  
**Assignment:** Assignment 1  
**Date:** October 2025  

---

## 🧠 Project Overview
This project builds a Retrieval-Augmented Generation (RAG) chatbot using LangChain and Streamlit.  
Users can upload multiple `.txt` and `.pdf` documents, which are automatically split into chunks, embedded with `text-embedding-3-small`, and stored in a ChromaDB vector database.  
The system retrieves relevant document sections for each query and generates responses with `gpt-4o-mini`, providing an interactive, document-grounded chat experience.

---

## ✨ Features
- Upload and process `.txt` and `.pdf` files  
- Support for multiple document uploads  
- Automatic chunking and embedding  
- Retrieval-Augmented Generation pipeline  
- Multi-turn conversational interface  
- “Clear Chat History” button  
- Persistent ChromaDB storage  

---

## ⚙️ Setup and Run
Use the provided Cornell Codespace environment (assignment1 branch).

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt


Set your API key and run
export LITELLM_API_KEY="sk-xxxx"
export OPENAI_API_KEY=$LITELLM_API_KEY
streamlit run chat_with_pdf.py


Indexed 20 chunks from 4 file(s).

User: Summarize Zhichuan Jing’s resume.
Assistant: Zhichuan Jing’s resume highlights interdisciplinary experience in systems engineering,
data science, and backend development, including projects in e-bus scheduling and financial modeling.
