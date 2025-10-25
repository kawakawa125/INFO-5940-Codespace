# Reference Log (ref-log.md)

## Developer
**Name:** Zhichuan Jing  
**Course:** INFO 5940 – AI Application Development  
**Assignment:** Assignment 1 – Retrieval-Augmented Generation (RAG)

---

## External References
1. **LangChain Documentation** – used to understand `RecursiveCharacterTextSplitter`, `ChatPromptTemplate`, and ChromaDB integration.  
   [https://python.langchain.com](https://python.langchain.com)

2. **Streamlit Documentation** – referenced for building the file uploader and chat interface.  
   [https://docs.streamlit.io](https://docs.streamlit.io)

3. **OpenAI API Reference** – consulted for embedding model `text-embedding-3-small` and `gpt-4o-mini`.  
   [https://platform.openai.com/docs](https://platform.openai.com/docs)

4. **Cornell Codespace Template** – used as the base environment and dependency setup for this assignment.

---

## Python Libraries Used
- **LangChain / LangChain Community / LangChain Core** – for RAG pipeline and text chunking  
- **ChromaDB** – for vector-based semantic retrieval  
- **Streamlit** – for user interface and document uploads  
- **pypdf** – for PDF text extraction  
- **OpenAI / LiteLLM** – for embeddings and chat model calls  

---

## GenAI Usage
ChatGPT (OpenAI GPT-5 via LiteLLM key) was used to:
- Debug and improve the `chat_with_pdf.py` RAG pipeline, including file parsing, text chunking, and retrieval logic.  
- Write and refine the `README.md` and `ref-log.md` for clarity and formatting consistency.  
- Suggest integration fixes for API key environment variables and embedding model compatibility.

The assistance focused on syntax correction, documentation polish, and verifying that all assignment requirements were met.  
All conceptual understanding, testing, and final implementation decisions were made by the developer.
